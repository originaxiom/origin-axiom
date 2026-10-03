#!/usr/bin/env python3
"""B1529 post-run check (written after the census found its one word-state failure of the four's base condition; disclosed in
FINDINGS): m135 = -LLRR in exact arithmetic.

Why. The census finds the four's base condition failing on one word state, -LLRR (SnapPy: m135), at two of its eight characters,
where (h1, h1*, t0, s0) = (2, 2, 1, 1). It also finds the interior polynomial vanishing at 1 (am(C; 1) = 4) at six of them.
Routes T, Fox and W agree at 60 digits (post_run_fox.py). This check reads the same numbers in exact arithmetic, with code that
shares nothing with those routes but the group presentation.

How.
  - The field. m135's shapes are 1 + i, i, 1 + i and (1 + i)/2 (SnapPy), so its cusp field is Q(i). The 60-digit hyperbolic
    point (sm:B1527's family_lib.hyperbolic_sl2) is conjugated so that the cusp's fixed point p0 goes to infinity, a(p0) to 0
    and b(p0) to 1. That puts every generator in PGL(2, Q(i)). Each generator is divided by its largest entry, and the entries
    are read as Gaussian rationals (denominators at most 10^9; every reading is checked to 10^-50).
  - The checks, exact. The two bundle relators hold in PGL(2, Q(i)). The cusp's two generators commute and are parabolic.
  - The four. g acts on Hermitian matrices by H -> g H g* / |det g|. With g in GL(2, Q(i)), |det g|^2 is rational, and here
    |det g| lies in Q(sqrt 2), so the four is defined over Q(sqrt 2). Twisted by a character of order 4 it lies over
    Q(zeta_8). All arithmetic below is in Q(zeta_8), with exact fractions.
  - h1 by Fox calculus, for V and V*: Z^1 is the kernel of the relators' Fox matrix, B^1 the image of the coboundary. Also t0,
    s0, a0 and b0 from the cusp. n(V), the interior classes, is the kernel of the restriction to the cusp.
  - The fibre's chi_C. S_0 acts on H^1(F; nu_0 (x) W) = V^2 / B^1(F) by (S_0 z)(g) = W(t')^-1 z(phi'(g)), with
    t' g t'^-1 = phi'(g). Its characteristic polynomial is chi_C, and am(C; 1) is the multiplicity of s = 1. chi_D is W(t')^-1
    on the coinvariants W_l.
  - Each number is compared with the census record of -LLRR.
Writes post_run_exact_m135.json and prints one line per character."""
import json
import sys
import time
import warnings
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402

import fibre_lib as T  # noqa: E402

SIGN, WORD = "-", "LLRR"
DEN_MAX = 10 ** 9
READ_TOL = mp.mpf(10) ** -50


# ------------------------------------------------------------------------------------------- Q(zeta_8), zeta = e^{i pi/4}
class Z8:
    """c0 + c1 z + c2 z^2 + c3 z^3 with z^4 = -1, exact"""
    __slots__ = ("c",)

    def __init__(self, c):
        self.c = tuple(Fraction(x) for x in c)

    @staticmethod
    def of(x):
        return x if isinstance(x, Z8) else Z8((x, 0, 0, 0))

    def __add__(self, o):
        o = Z8.of(o)
        return Z8(tuple(a + b for a, b in zip(self.c, o.c)))

    __radd__ = __add__

    def __neg__(self):
        return Z8(tuple(-a for a in self.c))

    def __sub__(self, o):
        return self + (-Z8.of(o))

    def __rsub__(self, o):
        return Z8.of(o) - self

    def __mul__(self, o):
        o = Z8.of(o)
        r = [Fraction(0)] * 4
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    if b:
                        k = i + j
                        if k < 4:
                            r[k] += a * b
                        else:
                            r[k - 4] -= a * b
        return Z8(r)

    __rmul__ = __mul__

    def is_zero(self):
        return not any(self.c)

    def sigma(self, k):
        """the Galois automorphism z -> z^k (k odd)"""
        r = [Fraction(0)] * 4
        for i, a in enumerate(self.c):
            m = (i * k) % 8
            if m < 4:
                r[m] += a
            else:
                r[m - 4] -= a
        return Z8(r)

    def conj(self):
        return self.sigma(7)

    def inv(self):
        assert not self.is_zero()
        p = self.sigma(3) * self.sigma(5) * self.sigma(7)
        n = (self * p).c
        assert n[1] == n[2] == n[3] == 0, n
        return p * Z8((1 / n[0], 0, 0, 0))

    def __truediv__(self, o):
        return self * Z8.of(o).inv()

    def __eq__(self, o):
        return (self - Z8.of(o)).is_zero()

    def exact(self):
        """the element written out: p + q sqrt2 when it lies in Q(sqrt 2), else its coordinates on 1, z, z^2, z^3"""
        c0, c1, c2, c3 = self.c
        if c2 == 0 and c1 == -c3:
            if c1 == 0:
                return str(c0)
            q = f"{abs(c1)} sqrt2" if abs(c1) != 1 else "sqrt2"
            return (("-" if c1 < 0 else "") + q) if c0 == 0 else f"{c0} {'-' if c1 < 0 else '+'} {q}"
        return "(" + ", ".join(str(x) for x in self.c) + ") on (1, z, z^2, z^3), z = e^(i pi/4)"

    def num(self):
        z = mp.expjpi(mp.mpf(1) / 4)
        return sum((mp.mpf(a.numerator) / a.denominator) * z ** i for i, a in enumerate(self.c))


ZERO, ONE = Z8((0, 0, 0, 0)), Z8((1, 0, 0, 0))
I_ = Z8((0, 0, 1, 0))
SQRT2 = Z8((0, 1, 0, -1))                     # z - z^3 = sqrt 2


def gauss(re, im):
    return Z8((re, 0, im, 0))


def root_of_unity(fr):
    """e^{2 pi i fr} for fr in (1/8)Z"""
    k = (fr * 8)
    assert k.denominator == 1
    k = int(k) % 8
    return Z8((1, 0, 0, 0)) if k == 0 else Z8([1 if i == k % 4 else 0 for i in range(4)]) * (1 if k < 4 else -1)


# ------------------------------------------------------------------------------------------- matrices over Z8
def mat(rows):
    return [[Z8.of(x) for x in r] for r in rows]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), ZERO) for j in range(len(B[0]))] for i in range(len(A))]


def madd(A, B, s=1):
    return [[A[i][j] + B[i][j] * s for j in range(len(A[0]))] for i in range(len(A))]


def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def scal(A, s):
    return [[x * s for x in r] for r in A]


def transpose(A):
    return [list(r) for r in zip(*A)]


def rank(A):
    M = [list(r) for r in A]
    if not M:
        return 0
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if not M[i][c].is_zero()), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pinv = M[r][c].inv()
        M[r] = [x * pinv for x in M[r]]
        for i in range(rows):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r


def minv(A):
    n = len(A)
    M = [list(A[i]) + eye(n)[i] for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if not M[i][c].is_zero())
        M[c], M[p] = M[p], M[c]
        pinv = M[c][c].inv()
        M[c] = [x * pinv for x in M[c]]
        for i in range(n):
            if i != c and not M[i][c].is_zero():
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[c])]
    return [r[n:] for r in M]


def nullspace(A, ncols):
    """a basis of {x : A x = 0}"""
    M = [list(r) for r in A]
    piv, r = [], 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if not M[i][c].is_zero()), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pinv = M[r][c].inv()
        M[r] = [x * pinv for x in M[r]]
        for i in range(len(M)):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [ZERO] * ncols
        v[fc] = ONE
        for k, pc in enumerate(piv):
            v[pc] = -M[k][fc]
        basis.append(v)
    return basis


def charpoly(A):
    """Faddeev-LeVerrier: coefficients of det(s - A), highest first"""
    n = len(A)
    coeffs = [ONE]
    Mk = [[ZERO] * n for _ in range(n)]
    for k in range(1, n + 1):
        Mk = madd(mmul(A, Mk), eye(n), coeffs[-1])
        AM = mmul(A, Mk)
        tr = sum((AM[i][i] for i in range(n)), ZERO)
        coeffs.append(tr * Z8((Fraction(-1, k), 0, 0, 0)))
    return coeffs


def mult_at_one(coeffs):
    """the multiplicity of s = 1 as a root (synthetic division)"""
    m = 0
    p = list(coeffs)
    while len(p) > 1:
        q, acc = [], ZERO
        for c in p:
            acc = acc + c
            q.append(acc)
        if not q[-1].is_zero():
            break
        p = q[:-1]
        m += 1
    return m


# ------------------------------------------------------------------------------------------- the representation
def read_gaussian(x):
    out = []
    for part in (mp.re(x), mp.im(x)):
        f = Fraction(mp.nstr(part, 58, min_fixed=-200, max_fixed=200)).limit_denominator(DEN_MAX)
        assert abs(part - mp.mpf(f.numerator) / f.denominator) < READ_TOL, (part, f)
        out.append(f)
    return gauss(*out)


def exact_sl2():
    mp.mp.dps = 60
    FL = T.load_b1527("family_lib")
    A, B, Tm, _ = FL.hyperbolic_sl2(SIGN, WORD)
    M = {"a": A, "b": B, "t": Tm}
    lm = FL.sl2_word("abAB", M)
    p0 = (lm[0, 0] - lm[1, 1]) / (2 * lm[1, 0])

    def mob(g, z):
        return (g[0, 0] * z + g[0, 1]) / (g[1, 0] * z + g[1, 1])
    p1, p2 = mob(A, p0), mob(B, p0)
    Cm = mp.matrix([[p2 - p0, -p1 * (p2 - p0)], [p2 - p1, -p0 * (p2 - p1)]])
    Ci = mp.inverse(Cm)
    out = {}
    for g in "abt":
        gp = Cm * M[g] * Ci
        piv = max(((i, j) for i in range(2) for j in range(2)), key=lambda ij: abs(gp[ij]))
        gq = gp / gp[piv]
        out[g] = [[read_gaussian(gq[i, j]) for j in range(2)] for i in range(2)]
    return out


def word_mat(w, mats, invs):
    X = eye(len(mats["a"]))
    for c in w:
        X = mmul(X, mats[c] if c.islower() else invs[c.lower()])
    return X


def is_scalar(X):
    return X[0][1].is_zero() and X[1][0].is_zero() and X[0][0] == X[1][1]


def det2(g):
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


def sqrt_rational_in_q2(q):
    """sqrt(q) for rational q > 0 when it lies in Q(sqrt 2)"""
    for k, root in ((1, ONE), (2, SQRT2)):
        r2 = q / k
        n, d = r2.numerator, r2.denominator
        rn, rd = int(round(n ** 0.5)), int(round(d ** 0.5))
        for an in (rn - 1, rn, rn + 1):
            for ad in (rd - 1, rd, rd + 1):
                if an > 0 and ad > 0 and an * an == n and ad * ad == d:
                    return root * Z8((Fraction(an, ad), 0, 0, 0))
    raise ValueError(f"sqrt({q}) is not in Q(sqrt 2)")


HERM = [mat([[1, 0], [0, 0]]), mat([[0, 0], [0, 1]]), mat([[0, 1], [1, 0]]), [[ZERO, I_], [-I_, ZERO]]]


def four(g):
    """H -> g H g* / |det g| on Hermitian H = [[x1, x3 + i x4], [x3 - i x4, x2]], in the coordinates (x1, x2, x3, x4)"""
    gs = [[g[j][i].conj() for j in range(2)] for i in range(2)]
    d = det2(g)
    nrm = (d * d.conj()).c
    assert nrm[1] == nrm[2] == nrm[3] == 0 and nrm[0] > 0
    absdet = sqrt_rational_in_q2(nrm[0])
    cols = []
    for H in HERM:
        Hn = mmul(mmul(g, H), gs)
        z = Hn[0][1]
        re = (z + z.conj()) * Z8((Fraction(1, 2), 0, 0, 0))
        im = (z - z.conj()) / (I_ * 2)
        cols.append([Hn[0][0], Hn[1][1], re, im])
    return [[cols[j][i] / absdet for j in range(4)] for i in range(4)]


# ------------------------------------------------------------------------------------------- cohomology
def cocycle_blocks(w, rho, inv_rho, gens):
    """z(w) = sum_g K_g z_g for the cocycle rule z(xy) = z(x) + x z(y)"""
    n = len(rho["a"])
    K = {g: [[ZERO] * n for _ in range(n)] for g in gens}
    P = eye(n)
    for c in w:
        g = c.lower()
        if c.islower():
            K[g] = madd(K[g], P)
            P = mmul(P, rho[g])
        else:
            P = mmul(P, inv_rho[g])
            K[g] = madd(K[g], P, -1)
    return K, P


def h0(rho, words, inv_rho):
    n = len(rho["a"])
    rows = []
    for w in words:
        X = word_mat(w, rho, inv_rho)
        rows += madd(X, eye(n), -1)
    return n - rank(rows)


def readings(rho, rels, cusp, gens=("a", "b", "t")):
    n = len(rho["a"])
    inv_rho = {g: minv(rho[g]) for g in gens}
    fox = []
    for r in rels:
        K, P = cocycle_blocks(r, rho, inv_rho, gens)
        assert all((P[i][j] == (ONE if i == j else ZERO)) for i in range(n) for j in range(n)), "relator not 1"
        fox += [sum((K[g][i] for g in gens), []) for i in range(n)]
    Z = nullspace(fox, n * len(gens))
    a0 = h0(rho, list(gens), inv_rho)
    h1 = len(Z) - (n - a0)
    t0 = h0(rho, list(cusp), inv_rho)
    # interior classes: cocycles whose restriction to the cusp is a cusp coboundary, modulo B^1
    res_rows = []
    for w in cusp:
        K, _ = cocycle_blocks(w, rho, inv_rho, gens)
        res_rows.append(K)
    if Z:
        # unknowns: coefficients x of the basis Z, and v in V; equations z_x(w) - (rho(w) - 1) v = 0 for w in cusp
        eqs = []
        for k, w in enumerate(cusp):
            K = res_rows[k]
            X = madd(word_mat(w, rho, inv_rho), eye(n), -1)
            for i in range(n):
                row = []
                for zb in Z:
                    s = ZERO
                    for gi, g in enumerate(gens):
                        for j in range(n):
                            s = s + K[g][i][j] * zb[gi * n + j]
                    row.append(s)
                row += [-x for x in X[i]]
                eqs.append(row)
        sol = len(Z) + n - rank(eqs)
        n_int = sol - t0 - (n - a0)
    else:
        n_int = 0
    return {"h1": h1, "a0": a0, "t0": t0, "n": n_int}


def fibre_chi(W, nu0, img_prime):
    """chi_C of S_0 on H^1(F; nu0 (x) W) = V^2 / B^1(F), and am(C; 1); W the four on a, b, t' (no character)"""
    n = len(W["a"])
    rhoF = {g: scal(W[g], nu0[g]) for g in "ab"}
    invF = {g: minv(rhoF[g]) for g in "ab"}
    Wtp_inv = minv(W["tp"])
    # S_0 on V^2 (the cocycle values on a, b)
    S = [[ZERO] * (2 * n) for _ in range(2 * n)]
    for gi, g in enumerate("ab"):
        K, _ = cocycle_blocks(img_prime[g], rhoF, invF, ("a", "b"))
        for hi, h in enumerate("ab"):
            blk = mmul(Wtp_inv, K[h])
            for i in range(n):
                for j in range(n):
                    S[gi * n + i][hi * n + j] = blk[i][j]
    # B^1(F) and a complement: the quotient's matrix
    Bcols = [[x for x in col] for col in transpose(madd(rhoF["a"], eye(n), -1) + madd(rhoF["b"], eye(n), -1))]
    Bbasis = []
    for v in Bcols:
        if rank([*Bbasis, v]) > len(Bbasis):
            Bbasis.append(v)
    full = list(Bbasis)
    for k in range(2 * n):
        e = [ONE if i == k else ZERO for i in range(2 * n)]
        if rank([*full, e]) > len(full):
            full.append(e)
    P = transpose(full)                          # columns: B^1 basis, then the complement
    Pi = minv(P)
    SP = mmul(mmul(Pi, S), P)
    m = len(Bbasis)
    for i in range(m, 2 * n):
        for j in range(m):
            assert SP[i][j].is_zero(), "B^1 not invariant"
    Q = [row[m:] for row in SP[m:]]
    chi = charpoly(Q)
    return chi, mult_at_one(chi), 2 * n - m


def main():
    t0 = time.time()
    FL = T.load_b1527("family_lib")
    G, img = FL.word_group(SIGN, WORD)
    chars, D = FL.torsion_characters(img)
    g2 = exact_sl2()
    inv2 = {g: minv(g2[g]) for g in "abt"}
    checks = {}
    for r in G.rels:
        checks["relator " + r + " scalar in PGL(2, Q(i))"] = is_scalar(word_mat(r, g2, inv2))
    lm, tp = word_mat(G.cusp[0], g2, inv2), word_mat(G.cusp[1], g2, inv2)
    checks["cusp generators commute"] = all((mmul(lm, tp)[i][j] == mmul(tp, lm)[i][j]) for i in range(2) for j in range(2))
    for name, X in (("l", lm), ("t'", tp)):
        tr, d = X[0][0] + X[1][1], det2(X)
        checks[name + " parabolic (tr^2 = 4 det)"] = (tr * tr == d * 4) and not is_scalar(X)
    W = {g: four(g2[g]) for g in "abt"}
    Winv = {g: minv(W[g]) for g in "abt"}
    for r in G.rels:
        X = word_mat(r, W, Winv)
        checks["the four: relator " + r + " = 1"] = all(X[i][j] == (ONE if i == j else ZERO) for i in range(4)
                                                           for j in range(4))
    trs = {w: sum((word_mat(w, W, Winv)[i][i] for i in range(4)), ZERO) for w in ("a", "b", "t", "ab", "abt")}
    checks["traces of the four (a, b, t, ab, abt)"] = [trs[w].exact() for w in trs]
    assert all(v for k, v in checks.items() if not k.startswith("traces")), checks
    W["tp"] = word_mat(G.cusp[1], W, Winv)
    # phi': t' g t'^-1 as a word in a, b (t' = abt for sign -)
    img_prime = {g: L_reduce("ab" + img[g] + "BA") for g in "ab"}
    census = next(json.loads(line) for line in (HERE / "census.jsonl").read_text().splitlines()
                  if json.loads(line)["state"] == SIGN + WORD)
    fail_base = {tuple(p["u"]): tuple(p["(h1, h1*, t0, s0)"]) for p in census["4"]["base condition fails at"]}
    fail_sr = {tuple(p["u"]): p["am(C)"] for p in census["4"]["SR fails at"]}
    rows = []
    for u in chars:
        nua, nub = root_of_unity(u[0]), root_of_unity(u[1])
        lam = ONE if SIGN == "+" else (nua * nub).inv()
        nu = {"a": nua, "b": nub, "t": lam}
        rho = {g: scal(W[g], nu[g]) for g in "abt"}
        rhod = {g: transpose(minv(rho[g])) for g in "abt"}
        V = readings(rho, G.rels, G.cusp)
        Vd = readings(rhod, G.rels, G.cusp)
        chiC, amC, dimC = fibre_chi(W, {"a": nua, "b": nub}, img_prime)
        I = Vd["h1"] - V["h1"] + 2 * (V["a0"] - Vd["a0"]) + Vd["t0"] - V["t0"]
        key = (str(u[0]), str(u[1]))
        want = fail_base.get(key, (1, 1, 1, 1))
        want_am = fail_sr.get(key, 2)
        got = (V["h1"], Vd["h1"], V["t0"], Vd["t0"])
        row = {"u": list(key), "nu(t)": mp.nstr(lam.num(), 5), "(h1, h1*, t0, s0)": list(got), "a0, b0": [V["a0"], Vd["a0"]],
               "n(V), n(V*)": [V["n"], Vd["n"]], "I (Lemma E)": I, "dim C": dimC, "am(C; 1)": amC,
               "chi_C (highest first)": [c.exact() for c in chiC],
               "agrees with the census": got == tuple(want) and amC == want_am}
        rows.append(row)
        print(f"u = {key}: (h1, h1*, t0, s0) = {got}, n = {row['n(V), n(V*)']}, I = {I}, am(C; 1) = {amC}; census "
              f"{tuple(want)}, {want_am}: {'agree' if row['agrees with the census'] else 'DISAGREE'}", flush=True)
    out = {"manifold": SIGN + WORD, "SnapPy": "m135", "D": D,
           "the representation (PGL(2, Q(i)), each generator divided by its largest entry)":
               {g: [[[str(x.c[0]), str(x.c[2])] for x in r] for r in g2[g]] for g in "abt"},
           "exact checks": checks, "rows": rows,
           "every row agrees with the census": all(r["agrees with the census"] for r in rows),
           "seconds": round(time.time() - t0)}
    (HERE / "post_run_exact_m135.json").write_text(json.dumps(out, indent=1, default=str))
    print("every row agrees with the census:", out["every row agrees with the census"], f"({out['seconds']} s)")


def L_reduce(w):
    out = []
    for c in w:
        if out and out[-1] != c and out[-1].lower() == c.lower():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


if __name__ == "__main__":
    main()
