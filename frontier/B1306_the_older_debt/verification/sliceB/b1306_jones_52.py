"""B1306 slice B, Q5 -- a colored Jones calculator of main's own (U_q(sl2) R-matrix in the weight basis, from the universal R-matrix formula), and the
two ends of J_n(m(5_2)) at n = 6..9 (cloud memo 184 @ 02a885ca: the bottom end is the false theta sum (-1)^k q^{k(k+1)/2}).
Construction: V_N with K e_m = v^{2(N-1-2m)} e_m, F e_m = e_{m+1}, E e_m = [m][N-m] e_{m-1}, v = q^{1/2};
R = q^{H(x)H/2} sum_n q^{n(n-1)/2} (q - q^{-1})^n / [n]!  E^n (x) F^n  (Kassel's U_h(sl2) universal R-matrix, K = q^H), R-hat = P R;
R-hat^{-1} exact per 2-strand weight sector (sympy); braids on V^{(x)3}; quantum trace with the pivotal element K^{+-1} (the sign chosen by the
control that the kinked unknot's trace is a monomial times [N] -- the ribbon twist theta); J(beta) = qtr(beta) theta^{-writhe} / [N].
Exactness: all entries are Laurent polynomials in v; the 3-strand products are evaluated modulo two primes at D = 4096 roots of unity and the
Laurent polynomial J is recovered by an inverse DFT (exact when the support fits the window and both primes agree -- both asserted).
Controls (all must fire): braid relation and R R^{-1} = 1 (exact, N = 2, 3, 4); the unknot closure of sigma_1 sigma_2 gives J = 1; the figure-eight
sigma_1 sigma_2^{-1} sigma_1 sigma_2^{-1} gives GM (166) at N = 2, 3, 4; the trefoil sigma_1^3 sigma_2 gives Habiro's series (or its mirror --
this fixes the chirality convention) at N = 2, 3, 4; J_2 of Park's word sigma_2^{-3} sigma_1^{-1} sigma_2 sigma_1^{-1} is the Jones polynomial of
5_2 or its mirror with |V(-1)| = 7 = det(5_2).  Usage: b1306_jones_52.py [NMAX]"""
import sys, json, time, itertools, math
import numpy as np, sympy as sp
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
v = sp.symbols('v'); D = 4096
def qint(k): return sum(v ** (2 * k - 2 - 4 * s) for s in range(k)) if k > 0 else sp.Integer(1)
def qfact(k):
    p = sp.Integer(1)
    for s in range(1, k + 1): p *= qint(s)
    return sp.expand(p)
def qbinom(i, n): return sp.expand(sp.cancel(qfact(i) / (qfact(n) * qfact(i - n))))
def lpoly(expr):                       # sympy Laurent poly in v -> dict exp->int
    expr = sp.expand(expr); out = {}
    if expr == 0: return out
    for term in sp.Add.make_args(expr):
        c, e = term.as_coeff_exponent(v); assert c.is_Integer and e.is_Integer, term; out[int(e)] = out.get(int(e), 0) + int(c)
    return {e: c for e, c in out.items() if c}
def rhat_sym(N):
    """R-hat = P R on V_N (x) V_N as sympy exprs: RH[(i,j)] = {(i',j'): expr} meaning e_i (x) e_j -> sum expr e_{i'} (x) e_{j'}"""
    lam = lambda m: N - 1 - 2 * m; RH = {}
    for i in range(N):
        for j in range(N):
            RH[(i, j)] = {}
            for n in range(0, min(i, N - 1 - j) + 1):
                coeff = v ** (n * (n - 1)) * (v ** 2 - v ** -2) ** n * qbinom(i, n)
                for s in range(n): coeff *= qint(N - i + s)
                coeff *= v ** (lam(i - n) * lam(j + n))
                RH[(i, j)][(j + n, i - n)] = sp.expand(coeff)
    return RH
def sector_matrices(N, RH):
    """per 2-strand weight sector s = i + j: basis, M (R-hat), Minv (exact), and the checks R R^-1 = 1"""
    out = {}
    for s in range(0, 2 * N - 1):
        basis = [(i, s - i) for i in range(N) if 0 <= s - i < N]; idx = {b: k for k, b in enumerate(basis)}
        M = sp.zeros(len(basis), len(basis))
        for b in basis:
            for b2, c in RH[b].items(): M[idx[b2], idx[b]] = c
        Minv = M.inv(); Minv = Minv.applyfunc(lambda e: sp.expand(sp.cancel(e)))
        assert (M * Minv - sp.eye(len(basis))).applyfunc(sp.expand) == sp.zeros(len(basis), len(basis))
        out[s] = dict(basis=basis, idx=idx, M=M, Minv=Minv)
    return out
def braid_relation_exact(N, RH):
    """sigma1 sigma2 sigma1 = sigma2 sigma1 sigma2 on V^{(x)3}, checked exactly on every basis vector"""
    def s1(vec):
        out = {}
        for (i, j, k), c in vec.items():
            for (i2, j2), c2 in RH[(i, j)].items(): out[(i2, j2, k)] = sp.expand(out.get((i2, j2, k), 0) + c * c2)
        return {b: c for b, c in out.items() if c != 0}
    def s2(vec):
        out = {}
        for (i, j, k), c in vec.items():
            for (j2, k2), c2 in RH[(j, k)].items(): out[(i, j2, k2)] = sp.expand(out.get((i, j2, k2), 0) + c * c2)
        return {b: c for b, c in out.items() if c != 0}
    for b in itertools.product(range(N), repeat=3):
        if s1(s2(s1({b: sp.Integer(1)}))) != s2(s1(s2({b: sp.Integer(1)}))): return False
    return True
# ---------------- modular evaluation machinery ----------------
def find_primes(k=2):
    ps = []; p = (2 ** 28 // D) * D + 1
    while len(ps) < k:
        p -= D
        if sp.isprime(p): ps.append(p)
    return ps
def root_of_unity(p):
    g = sp.primitive_root(p); return pow(g, (p - 1) // D, p)
class Bench:
    def __init__(self, N, p):
        self.N, self.p = N, p; self.g = root_of_unity(p)
        self.pts = np.array([pow(self.g, t, p) for t in range(D)], dtype=np.int64)
        self.RH = rhat_sym(N); self.sec = sector_matrices(N, self.RH)
        # exact entries as Laurent dicts for R-hat and its inverse: E[+1][(i,j)] = {(i',j'): poly}, E[-1] likewise
        self.E = {1: {}, -1: {}}
        for s, d in self.sec.items():
            for b in d["basis"]:
                self.E[1][b] = {}; self.E[-1][b] = {}
                for b2 in d["basis"]:
                    c = d["M"][d["idx"][b2], d["idx"][b]]
                    if c != 0: self.E[1][b][b2] = lpoly(c)
                    c = d["Minv"][d["idx"][b2], d["idx"][b]]
                    if c != 0: self.E[-1][b][b2] = lpoly(c)
        exps = {e for sign in (1, -1) for b in self.E[sign] for poly in self.E[sign][b].values() for e in poly}
        self.emin, self.emax = min(exps), max(exps)
        self.powtab = {}                                           # v^e at all points, mod p
        for e in range(self.emin, self.emax + 1): self.powtab[e] = np.array([pow(int(x), e, p) if e >= 0 else pow(pow(int(x), -e, p), p - 2, p) for x in self.pts], dtype=np.int64)
        self.entry_vals = {}
        for sign in (1, -1):
            for b, row in self.E[sign].items():
                for b2, poly in row.items():
                    acc = np.zeros(D, dtype=np.int64)
                    for e, c in poly.items(): acc = (acc + (c % p) * self.powtab[e]) % p
                    self.entry_vals[(sign, b, b2)] = acc
        lam = lambda m: N - 1 - 2 * m; self.lam = lam
        self.qN = sum(self.powtab.get(2 * lam(m), None) if 2 * lam(m) in self.powtab else np.array([pow(int(x), 2 * lam(m), p) if lam(m) >= 0 else pow(pow(int(x), -2 * lam(m), p), p - 2, p) for x in self.pts], dtype=np.int64) for m in range(N)) % p  # [N] = sum v^{2 lam}
        # 3-strand sectors
        self.sec3 = {}
        for S_ in range(0, 3 * (N - 1) + 1):
            basis = [t for t in itertools.product(range(N), repeat=3) if sum(t) == S_]; idx = {b: k for k, b in enumerate(basis)}
            self.sec3[S_] = dict(basis=basis, idx=idx)
    def letter_matrix(self, S_, letter, sign_piv):
        """dense (D, d, d) matrix of sigma_letter (letter in {1,-1,2,-2}) on 3-strand sector S_"""
        d = self.sec3[S_]; n = len(d["basis"]); M = np.zeros((D, n, n), dtype=np.int64); sign = 1 if letter > 0 else -1
        for b in d["basis"]:
            i, j, k = b
            if abs(letter) == 1:
                for (i2, j2), _ in self.E[sign][(i, j)].items(): M[:, d["idx"][(i2, j2, k)], d["idx"][b]] = self.entry_vals[(sign, (i, j), (i2, j2))]
            else:
                for (j2, k2), _ in self.E[sign][(j, k)].items(): M[:, d["idx"][(i, j2, k2)], d["idx"][b]] = self.entry_vals[(sign, (j, k), (j2, k2))]
        return M
    def qtrace3(self, word, piv):
        """quantum trace of the braid word on V^{(x)3} with pivotal element v^{2 piv (lam1+lam2+lam3)}; returns values at all points"""
        p = self.p; tot = np.zeros(D, dtype=np.int64)
        for S_, d in self.sec3.items():
            M = None
            for letter in word:
                L = self.letter_matrix(S_, letter, piv); M = L if M is None else (M @ L) % p
            for b in d["basis"]:
                e = 2 * piv * sum(self.lam(m) for m in b); w = self.powtab[e] if e in self.powtab else np.array([pow(int(x), e, p) if e >= 0 else pow(pow(int(x), -e, p), p - 2, p) for x in self.pts], dtype=np.int64)
                tot = (tot + M[:, d["idx"][b], d["idx"][b]] * w) % p
        return tot
    def qtrace2(self, letter, piv):
        p = self.p; tot = np.zeros(D, dtype=np.int64); sign = 1 if letter > 0 else -1
        for b, row in self.E[sign].items():
            if b in row:
                e = 2 * piv * (self.lam(b[0]) + self.lam(b[1])); w = np.array([pow(int(x), e, p) if e >= 0 else pow(pow(int(x), -e, p), p - 2, p) for x in self.pts], dtype=np.int64)
                tot = (tot + self.entry_vals[(sign, b, b)] * w) % p
        return tot
    def idft(self, vals):
        """values at g^t -> Laurent dict in v on the window [-D/2, D/2); symmetric residues"""
        p = self.p; ginv = pow(self.g, p - 2, p); Dinv = pow(D, p - 2, p); out = {}
        gpow = np.array([pow(ginv, t, p) for t in range(D)], dtype=np.int64)
        for e in range(-D // 2, D // 2):
            # c_e = D^-1 sum_t vals[t] g^{-e t}
            idxs = (np.arange(D) * (e % D)) % D
            c = int(np.sum((vals * gpow[idxs]) % p) % p) * Dinv % p
            if c > p // 2: c -= p
            if c: out[e] = c
        return out
def dict_mul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items(): r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}
def J41(n):                            # GM (166), in q: dict q-exp -> int
    tot = {0: 1}
    for m in range(1, n):
        term = {0: 1}
        for j in range(1, m + 1): term = dict_mul(term, {n: 1, -n: 1, j: -1, -j: -1})
        for e, c in term.items(): tot[e] = tot.get(e, 0) + c
    return {e: c for e, c in tot.items() if c}
def J31(n):                            # Habiro's cyclotomic expansion, one chirality: sum_k (-1)^k q^{-k(k+3)/2} prod_{j<=k} (q^n + q^-n - q^j - q^-j)
    tot = {}
    for k in range(0, n):
        term = {-(k * (k + 3)) // 2 if (k * (k + 3)) % 2 == 0 else None: (-1) ** k}
        assert None not in term
        for j in range(1, k + 1): term = dict_mul(term, {n: 1, -n: 1, j: -1, -j: -1})
        for e, c in term.items(): tot[e] = tot.get(e, 0) + c
    return {e: c for e, c in tot.items() if c}
def mirror(d): return {-e: c for e, c in d.items()}
def to_q(dv):
    """v-exponents -> the standard Jones variable: the calculator's v is t^{1/4} (the unknot-with-kink control gives theta = v^{N^2-1} = t^{(N^2-1)/4},
    and J_2 of Park's word came out as V_{5_2}(t) with t = v^4); every exponent must be divisible by 4"""
    assert all(e % 4 == 0 for e in dv), sorted(dv)[:5]
    return {e // 4: c for e, c in dv.items()}
def show(d, k=12):
    ks = sorted(d); return " ".join(f"{d[e]:+d}q^{e}" for e in ks[:k]) + (" ..." if len(ks) > k else "")
def ends(d, N=24):
    ks = sorted(d)
    return [d.get(ks[0] + t, 0) for t in range(N)], [d.get(ks[-1] - t, 0) for t in range(N)]
def stable(a, b):
    out = []
    for x, y in zip(a, b):
        if x == y: out.append(x)
        else: break
    return out
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)
def ldiv(num, den):
    """exact division of Laurent dicts (den's top coefficient +-1); asserts a zero remainder"""
    num = dict(num); out = {}; top = max(den); c0 = den[top]
    while num:
        e = max(num); c = num[e] // c0; assert c * c0 == num[e]; out[e - top] = c
        for e2, c2 in den.items():
            num[e2 + e - top] = num.get(e2 + e - top, 0) - c * c2
            if num[e2 + e - top] == 0: del num[e2 + e - top]
    return out
def colored_jones(N, word, primes, piv_sign=None, verbose=False):
    """J_N(closure of word) as a Laurent dict in q, from two primes; also returns the pivotal sign and theta used.
    No pointwise division: qtr(beta) theta^{-w} is reconstructed as a Laurent polynomial and divided by [N] EXACTLY (the remainder must vanish)."""
    res = []
    for p in primes:
        B = Bench(N, p); w = sum(1 if l > 0 else -1 for l in word); qN = {2 * B.lam(m): 1 for m in range(N)}
        best = None
        for piv in ((piv_sign,) if piv_sign else (1, -1)):
            th = ldiv(B.idft(B.qtrace2(1, piv)), qN)
            if len(th) == 1: best = (piv, th); break
        assert best, "the kinked unknot's trace is not a monomial times [N] for either pivotal sign"
        piv, th = best; (te, tc), = th.items()          # theta = tc v^{te}, tc = +-1
        assert abs(tc) == 1
        tr = B.qtrace3(word, piv)
        vpow = np.array([pow(int(x), (-te * w) % (p - 1), p) for x in B.pts], dtype=np.int64)
        P = B.idft((tr * vpow) % p)
        if tc == -1 and w % 2: P = {e: -c for e, c in P.items()}
        if P: assert min(P) > -D // 2 + 40 and max(P) < D // 2 - 40, "support touches the window"
        res.append((piv, (te, tc), ldiv(P, qN)))
    assert res[0][2] == res[1][2], "the two primes disagree"
    return to_q(res[0][2]), res[0][0], res[0][1]
if __name__ == "__main__":
    t0 = time.time(); primes = find_primes(2); print("primes:", primes, "D =", D)
    out = dict(primes=primes, D=D, controls={}, m52={})
    # exact controls: braid relation, R R^-1
    for N in (2, 3, 4):
        RH = rhat_sym(N); sector_matrices(N, RH)          # asserts R R^-1 = 1 in every sector
        check(f"N={N}: R-hat R-hat^-1 = 1 exactly in every weight sector", True)
        check(f"N={N}: braid relation s1 s2 s1 = s2 s1 s2 exactly on V^(x)3", braid_relation_exact(N, RH))
    # the unknot, the figure-eight, the trefoil, and 5_2 at N = 2, 3, 4
    UNKNOT, FIG8, TREF, PARK = [1, 2], [1, -2, 1, -2], [1, 1, 1, 2], [-2, -2, -2, -1, 2, -1]
    chir = None
    for N in (2, 3, 4):
        Ju, piv, th = colored_jones(N, UNKNOT, primes); check(f"N={N}: unknot (closure of s1 s2, writhe 2) J = 1  [pivotal sign {piv:+d}, theta = {th[1]:+d} v^{th[0]}]", Ju == {0: 1})
        J8, _, _ = colored_jones(N, FIG8, primes, piv); check(f"N={N}: figure-eight = GM (166)", J8 == J41(N))
        J3, _, _ = colored_jones(N, TREF, primes, piv); h = J31(N)
        if chir is None: chir = "same" if J3 == h else ("mirror" if J3 == mirror(h) else None)
        check(f"N={N}: trefoil (s1^3 s2) = Habiro's series ({chir}; chirality convention fixed at N=2)", J3 == (h if chir == "same" else mirror(h)))
        J5, _, _ = colored_jones(N, PARK, primes, piv)
        if N == 2:
            V = J5; Vm1 = sum(c * (-1) ** e for e, c in V.items())
            print("   J_2(Park's word) =", show(V), "| V(-1) =", Vm1)
            check("N=2: Park's word gives a Jones polynomial with |V(-1)| = 7 = det(5_2) and V(1) = 1", abs(Vm1) == 7 and sum(V.values()) == 1)
            target = {1: 1, 2: -1, 3: 2, 4: -1, 5: 1, 6: -1}
            out["m52_orientation"] = "as-is" if V == target else ("mirror" if mirror(V) == target else "neither")
            check("N=2: it is memo 184's J_2(m(5_2)) = q - q^2 + 2q^3 - q^4 + q^5 - q^6, as-is or as its mirror", out["m52_orientation"] != "neither")
        out["controls"][N] = dict(J2=show(J5, 40) if N == 2 else None)
    print(f"  controls done in {time.time()-t0:.0f}s; orientation of Park's word here: {out['m52_orientation']}")
    # the ends of J_n(m(5_2)), n = 6..NMAX (memo 184: bottom end = false theta [1,-1,0,1,0,0,-1,0,...]; top end not stabilised at n <= 9)
    piv = colored_jones(2, UNKNOT, primes)[1]
    prev = None; phi = [1, -1, 0, 1, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, -1]
    for n in range(6, NMAX + 1):
        t1 = time.time(); J, _, _ = colored_jones(n, PARK, primes, piv)
        if out["m52_orientation"] == "mirror": J = mirror(J)
        b, t = ends(J); ks = sorted(J)
        print(f"   n={n}: q^{ks[0]} .. q^{ks[-1]} ({len(ks)} terms) bottom {b[:10]} top {t[:10]}  [{time.time()-t1:.0f}s]")
        out["m52"][n] = dict(lo=ks[0], hi=ks[-1], bottom=b, top=t)
        if prev:
            sb, st = stable(prev[0], b), stable(prev[1], t)
            print(f"        stabilised vs n={n-1}: bottom {sb} | top {st}")
            out["m52"][n]["stable_bottom"], out["m52"][n]["stable_top"] = sb, st
        prev = (b, t)
    if NMAX >= 7:
        sb = out["m52"][NMAX]["stable_bottom"]; st = out["m52"][NMAX]["stable_top"]
        check(f"bottom end of J_n(m(5_2)) stabilised on >= 8 coefficients and equals the false theta sum (-1)^k q^(k(k+1)/2): {sb[:8]}", len(sb) >= 8 and sb[:8] == phi[:8])
        check(f"top end not stabilised beyond a few coefficients at n <= {NMAX} (memo 184 read it as empty): {st}", len(st) <= 2)
    # memo 184 section 3: 1/Phi grows like 1.2880^n (a zero of the false theta inside the unit disc)
    M = 3000; phi_c = [0] * (M + 1)
    k = 0
    while k * (k + 1) // 2 <= M: phi_c[k * (k + 1) // 2] += (-1) ** k; k += 1
    inv = [0] * (M + 1); inv[0] = 1
    for m in range(1, M + 1): inv[m] = -sum(phi_c[j] * inv[m - j] for j in range(1, m + 1))
    growth = {m: math.exp((abs(inv[m]).bit_length() * math.log(2) + math.log(abs(inv[m]) / 2 ** (abs(inv[m]).bit_length()))) / m) if inv[m] else None for m in (100, 500, 1500, 3000)}
    print("   1/Phi: |a_n|^(1/n) at n=100,500,1500,3000 =", {k2: round(x, 5) for k2, x in growth.items()})
    check("1/Phi's coefficients grow geometrically with |a_n|^(1/n) -> 1.288 +- 0.002 (memo 184: 1.2880)", abs(growth[3000] - 1.2880) < 0.002)
    out["inv_phi_growth"] = growth; out["fails"] = fails
    json.dump(out, open(f"b1306_jones_52_N{NMAX}.json", "w"), indent=1, default=str)
    print(f"Q5: {'PASS' if not fails else 'FAIL'}  [{time.time()-t0:.0f}s]"); sys.exit(1 if fails else 0)
