#!/usr/bin/env python3
"""CHIRAL-THREE UNIT, recomputed from definitions (own code; nothing of main's or agy's imported or run).

Exact throughout: monomial matrices with root-of-unity entries as rational turns; Gaussian-rational linear algebra.

  R   rho_T = multiplier of eta^-3 (theta_2^2, theta_3^2, theta_4^2) (= of eta^21 * ..., B1634): Mp2(Z) relations, exponents,
      allowed weights.
  X   Euler characteristic chi_k(rho, m) by the Borcherds-Skoruppa formula (B1632), per-line units in the T term.
  D   h0(m) directly: weight-3/2 sections with x-order >= c_j - 8 m_j on eigenline j (c = (1,7,3) on P, M=v+, N),
      via g = eta^3 Delta^N f in M_{3+12N}(A), A the weight-1 multiplier of u = (theta_2^2, theta_3^2, theta_4^2), M_d(A) =
      A-equivariant polynomial maps in u modulo u3^2 = u2^2 + u4^2.
  I   the four-dimensional index at an empty Lambda_+ = -chi (B1641's W3 at members = [], B1894 section 3).
  V   move-invariance of each m under three readings.
  C   planted controls C1-C4 (each must make its check fail).
"""
import itertools, json, sys
from fractions import Fraction as F
from math import gcd

OUT = {}

# ---------------------------------------------------------------- exact monomial matrices: col j -> (row sigma(j), turn t_j)
class Mono:
    def __init__(self, perm, turns):
        self.p = tuple(perm); self.t = tuple(F(x) % 1 for x in turns)
    def __matmul__(self, o):   # (self o)(e_j) = self(e^{2pi i t_o_j} e_{o.p[j]})
        return Mono([self.p[o.p[j]] for j in range(3)], [o.t[j] + self.t[o.p[j]] for j in range(3)])
    def scal(self, s):
        return Mono(self.p, [x + s for x in self.t])
    def inv(self):
        p = [0] * 3; t = [0] * 3
        for j in range(3):
            p[self.p[j]] = j; t[self.p[j]] = -self.t[j]
        return Mono(p, t)
    def __eq__(self, o):
        return self.p == o.p and self.t == o.t
    def is_scalar(self):
        return self.p == (0, 1, 2) and len(set(self.t)) == 1
    def eig_turns(self):
        seen, out = set(), []
        for j in range(3):
            if j in seen: continue
            cyc = [j]; k = self.p[j]
            while k != j: cyc.append(k); k = self.p[k]
            seen |= set(cyc); L = len(cyc); T = sum(self.t[c] for c in cyc)
            out += [((T + r) / L) % 1 for r in range(L)]
        return sorted(out)
    def dense(self):   # complex numpy-free list for numeric cross-checks
        import cmath
        M = [[0j] * 3 for _ in range(3)]
        for j in range(3): M[self.p[j]][j] = cmath.exp(2j * cmath.pi * float(self.t[j]))
        return M

def mpow(M, n):
    R = Mono((0, 1, 2), (0, 0, 0))
    for _ in range(n): R = R @ M
    return R

I3 = Mono((0, 1, 2), (0, 0, 0))
SW34 = Mono((0, 2, 1), (0, 0, 0))      # basis order (e2, e3, e4) = indices (0, 1, 2)
SW24 = Mono((2, 1, 0), (0, 0, 0))
# weight-1 multiplier A of u = (theta_2^2, theta_3^2, theta_4^2): u(tau+1) = A(T) u, u(-1/tau) = tau A(S) u
A_T = Mono((0, 2, 1), (F(1, 4), 0, 0))           # theta_2^2 -> i theta_2^2, theta_3^2 <-> theta_4^2
A_S = Mono((2, 1, 0), (F(3, 4),) * 3)             # (-i tau) * swap(2,4): A(S) = -i * swap
# rho_T = A (x) eta^-3 multiplier at weight -1/2: eta^-3(tau+1) = e^{-i pi/4}; eta^-3(-1/tau) = (-i tau)^{-3/2} eta^-3
#  with u's (-i tau): total (-i tau)^{-1/2} = e^{i pi/4} tau^{-1/2}  ->  rho(S) = e^{i pi/4} swap(2,4)
RT = A_T.scal(F(-1, 8))
RS = SW24.scal(F(1, 8))

def rep_checks(S, T, tag):
    r = {"S2_scalar": (S @ S).is_scalar(), "S2_eq_ST3": (S @ S) == mpow(S @ T, 3), "S8_eq_I": mpow(S, 8) == I3,
         "S2_turn": str((S @ S).t[0]) if (S @ S).is_scalar() else None, "T_exponents": [str(x) for x in T.eig_turns()]}
    r["valid"] = r["S2_scalar"] and r["S2_eq_ST3"] and r["S8_eq_I"]
    return r

OUT["R"] = {"rho_T": rep_checks(RS, RT, "rho_T"), "A": rep_checks(A_S, A_T, "A")}
assert OUT["R"]["rho_T"]["valid"] and OUT["R"]["rho_T"]["S2_turn"] == "1/4"            # S^2 = i I
assert OUT["R"]["rho_T"]["T_exponents"] == ["1/8", "3/8", "7/8"]

def allowed(k, S):   # rho(S)^2 = e^{-i pi k} I
    S2 = S @ S
    return S2.is_scalar() and S2.t[0] == F(-k, 2) % 1

OUT["R"]["allowed_weights_rho"] = [str(F(tk, 2)) for tk in range(-1, 30) if allowed(F(tk, 2), RS)]
RSb, RTb = Mono(RS.p, [-x for x in RS.t]), Mono(RT.p, [-x for x in RT.t])          # complex conjugate
OUT["R"]["allowed_weights_conj"] = [str(F(tk, 2)) for tk in range(-1, 30) if allowed(F(tk, 2), RSb)]
assert "3/2" in OUT["R"]["allowed_weights_rho"] and "3/2" not in OUT["R"]["allowed_weights_conj"]

# A factors through SL(2, Z/4): BFS over words; same matrix mod 4 must give the same A (checks A trivial on Gamma(4))
def sl2_mod(M, N):
    return tuple(x % N for x in M)
def mul2(X, Y):
    a, b, c, d = X; e, f, g, h = Y
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)
def factors_through(N, Sm, Tm):
    S2, T2 = (0, -1, 1, 0), (1, 1, 0, 1)
    start = sl2_mod((1, 0, 0, 1), N); table = {start: I3}; frontier = [((1, 0, 0, 1), I3)]
    ok = True
    while frontier:
        nxt = []
        for X, AX in frontier:
            for G, AG in ((S2, Sm), (T2, Tm)):
                Y = tuple(v % N for v in mul2(X, G)); AY = AX @ AG
                if Y in table:
                    ok &= (table[Y] == AY)
                else:
                    table[Y] = AY; nxt.append((Y, AY))
        frontier = nxt
    return ok, len(table)
ok4, n4 = factors_through(4, A_S, A_T)
OUT["R"]["A_factors_through_SL2_Z4"] = {"ok": ok4, "group_order": n4}
assert ok4 and n4 == 48

# ---------------------------------------------------------------- X: Borcherds-Skoruppa Euler characteristic, exact
def alpha(M):
    return sum(M.eig_turns(), F(0))

def chi(k, S, T, m=(0, 0, 0)):
    """B1632's formula; per-line units m on the T-eigenlines (P, M, N) lower those exponents by m_j."""
    d = 3
    a_S = alpha(S.scal(F(k, 4)))                      # e^{i pi k/2} rho(S)
    a_ST = alpha((S @ T).scal(F(k, 6)).inv())         # (e^{i pi k/3} rho(S) rho(T))^{-1}
    lines = eigenlines(T)
    a_T = sum((lines[name][0] - mj for name, mj in zip(("P", "M", "N"), m)), F(0))
    return d + F(d) * k / 12 - a_S - a_ST - a_T

def eigenlines(T):
    """the three eigenlines of rho(T) in the basis (e2, e3, e4): P = e2, M = e3 + e4, N = e3 - e4, with exact turns."""
    # T = [[t0,0,0],[0,0,c],[0,c,0]] with c = e^{2 pi i t}: e3+e4 has eigenvalue c, e3-e4 has -c
    assert T.p == (0, 2, 1) and T.t[1] == T.t[2]
    return {"P": (T.t[0] % 1, (1, 0, 0)), "M": (T.t[1] % 1, (0, 1, 1)), "N": ((T.t[1] + F(1, 2)) % 1, (0, 1, -1))}

EL = eigenlines(RT)
OUT["X"] = {"eigenlines": {k: {"turn": str(v[0]), "vector": v[1]} for k, v in EL.items()},
            "chi_3/2": str(chi(F(3, 2), RS, RT)), "chi_27/2": str(chi(F(27, 2), RS, RT)),
            "chi_uniform_n": {n: str(chi(F(3, 2) + 12 * n, RS, RT)) for n in range(-1, 4)},
            "chi_conj_1/2": str(chi(F(1, 2), RSb, RTb))}
C = tuple(int(EL[k][0] * 8) for k in ("P", "M", "N"))           # canonical x-orders
assert C == (1, 7, 3), C
# calibration: trivial rep chi_k = (1, 0, 1, 1, 2) at k = 0, 2, 4, 6, 12 (1-dim version of the same formula)
def chi1(k, s, t):
    al = lambda x: F(x) % 1
    return 1 + F(k, 12) - al(s + F(k, 4)) - al(-(s + t + F(k, 6))) - al(t)
OUT["X"]["calibration_trivial"] = [str(chi1(k, 0, 0)) for k in (0, 2, 4, 6, 12)]
OUT["X"]["calibration_eta_half"] = str(chi1(F(1, 2), F(-1, 8), F(1, 24)))
assert OUT["X"]["calibration_trivial"] == ["1", "0", "1", "1", "2"] and OUT["X"]["calibration_eta_half"] == "1"

# ---------------------------------------------------------------- Gaussian rationals and elimination
class G:
    __slots__ = ("r", "i")
    def __init__(self, r=0, i=0): self.r = F(r); self.i = F(i)
    def __add__(s, o): return G(s.r + o.r, s.i + o.i)
    def __sub__(s, o): return G(s.r - o.r, s.i - o.i)
    def __mul__(s, o): return G(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    def __truediv__(s, o):
        n = o.r * o.r + o.i * o.i
        return G((s.r * o.r + s.i * o.i) / n, (s.i * o.r - s.r * o.i) / n)
    def __bool__(s): return s.r != 0 or s.i != 0
    def conj(s): return G(s.r, -s.i)
I_POW = [G(1, 0), G(0, 1), G(-1, 0), G(0, -1)]

def nullspace(rows, n):
    """rows: list of dict col->G. Returns a basis of the nullspace as lists of G (length n)."""
    piv = {}   # pivot col -> reduced row (dict)
    for r in rows:
        r = {c: v for c, v in r.items() if v}
        # reduce by existing pivots
        while r:
            cs = [c for c in r if c in piv]
            if not cs: break
            c = cs[0]; f = r[c]
            for cc, vv in piv[c].items():
                r[cc] = r.get(cc, G()) - f * vv
                if not r[cc]: del r[cc]
        if not r: continue
        c0 = min(r); inv = G(1) / r[c0]
        r = {c: v * inv for c, v in r.items()}
        # eliminate c0 from other pivots
        for pc, pr in piv.items():
            if c0 in pr:
                f = pr[c0]
                for cc, vv in r.items():
                    pr[cc] = pr.get(cc, G()) - f * vv
                    if not pr[cc]: del pr[cc]
        piv[c0] = r
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [G() for _ in range(n)]; v[fc] = G(1)
        for pc, pr in piv.items():
            if fc in pr: v[pc] = G() - pr[fc]
        basis.append(v)
    return basis

def rank_rows(rows, n):
    return n - len(nullspace(rows, n))

# ---------------------------------------------------------------- polynomials in u modulo u3^2 = u2^2 + u4^2
from functools import lru_cache

@lru_cache(maxsize=None)
def reduce_mono(a, e, c):
    """u2^a u3^e u4^c in normal form (u3-degree <= 1): dict (a,e,c) -> int"""
    if e <= 1: return {(a, e, c): 1}
    out = {}
    for key, v in list(reduce_mono(a + 2, e - 2, c).items()) + list(reduce_mono(a, e - 2, c + 2).items()):
        out[key] = out.get(key, 0) + v
    return out

def basis(d):
    return [(a, e, d - a - e) for e in (0, 1) for a in range(d - e + 1)]

def transform(mono, gen):
    """mono(A x) for A = A_T or A_S, as dict normal-mono -> G"""
    a, e, c = mono; d = a + e + c
    if gen == "T":     # u2 -> i u2, u3 -> u4, u4 -> u3
        coef, (a2, e2, c2) = I_POW[a % 4], (a, c, e)
    else:              # u2 -> -i u4, u3 -> -i u3, u4 -> -i u2
        coef, (a2, e2, c2) = I_POW[(3 * d) % 4], (c, e, a)
    return {k: coef * G(v) for k, v in reduce_mono(a2, e2, c2).items()}

# x-series (x = q^{1/8}) of theta_2^2, theta_3^2, theta_4^2, integer coefficients, to precision PREC
def series_mul(A, B, prec):
    out = [0] * prec
    for i, x in enumerate(A):
        if x:
            for j in range(prec - i):
                if B[j]: out[i + j] += x * B[j]
    return out

def theta_squares(prec):
    th2 = [0] * prec; th3 = [0] * prec; th4 = [0] * prec
    n = 0
    while (2 * n + 1) ** 2 < prec:
        th2[(2 * n + 1) ** 2] += 2; n += 1
    n = 0
    while 4 * n * n < prec:
        mult = 1 if n == 0 else 2
        th3[4 * n * n] += mult; th4[4 * n * n] += mult * (-1) ** n; n += 1
    return [series_mul(t, t, prec) for t in (th2, th3, th4)]

def mono_series(d, prec, U):
    pw = {}
    def power(i, k):
        if (i, k) not in pw:
            pw[(i, k)] = [1] + [0] * (prec - 1) if k == 0 else series_mul(power(i, k - 1), U[i], prec)
        return pw[(i, k)]
    return {m: series_mul(series_mul(power(0, m[0]), power(1, m[1]), prec), power(2, m[2]), prec) for m in basis(d)}

_EQ = {}
def equivariant_basis(d, swap_S_sign=False):
    """basis of M_d(A): A-equivariant polynomial maps P = (P_u2, P_u3, P_u4) of degree d in normal form (cached)."""
    key = (d, swap_S_sign)
    if key in _EQ: return _EQ[key]
    B = basis(d); nb = len(B); idx = {b: i for i, b in enumerate(B)}
    n = 3 * nb
    rows = []
    tgt = {"T": {0: (0, I_POW[1]), 1: (2, G(1)), 2: (1, G(1))},              # (A_T P)_r = coef * P_src
           "S": {0: (2, I_POW[3]), 1: (1, I_POW[3]), 2: (0, I_POW[3])}}       # (A_S P)_r = -i P_{swap r}
    if swap_S_sign:
        tgt["S"] = {k: (v[0], G() - v[1]) for k, v in tgt["S"].items()}
    for gen in ("T", "S"):
        trans = {b: transform(b, gen) for b in B}
        for r in range(3):
            src, coef = tgt[gen][r]
            eqs = {}
            for b in B:                      # LHS: component r of P(Ax)
                for k, v in trans[b].items():
                    e = eqs.setdefault(k, {}); col = r * nb + idx[b]
                    e[col] = e.get(col, G()) + v
            for b in B:                      # RHS: coef * P_src(x)
                e = eqs.setdefault(b, {}); col = src * nb + idx[b]
                e[col] = e.get(col, G()) - coef
            rows += list(eqs.values())
    ns = nullspace(rows, n)
    prec = 8 * ((d - 3) // 12) + 64
    U = theta_squares(prec); MS = mono_series(d, prec, U)
    comb = {0: {0: F(1)}, 1: {1: F(1, 2), 2: F(1, 2)}, 2: {1: F(1, 2), 2: F(-1, 2)}}
    line_series = []      # for each basis vector: 3 lists (P, M, N) of G coefficients
    for vec in ns:
        ls = []
        for j in range(3):
            ser = [G() for _ in range(prec)]
            for r, w in comb[j].items():
                for b in B:
                    cf = vec[r * nb + idx[b]]
                    if cf:
                        cw = cf * G(w)
                        for e, sv in enumerate(MS[b]):
                            if sv: ser[e] = ser[e] + cw * G(sv)
            ls.append(ser)
        line_series.append(ls)
    _EQ[key] = (ns, line_series, prec, B)
    return _EQ[key]

def h0(m, c=C, swap_S_sign=False):
    """dimension of weight-3/2 sections of rho_T with x-order >= c_j - 8 m_j on lines (P, M, N); returns (dim, vectors)."""
    N = max(0, max(m)); d = 3 + 12 * N
    ns, LS, prec, B = equivariant_basis(d, swap_S_sign)
    bound = [1 + 8 * N + c[j] - 8 * m[j] for j in range(3)]
    assert max(bound) < prec - 8
    k = len(ns)
    rows = []
    for j in range(3):
        for e in range(bound[j]):
            row = {i: LS[i][j][e] for i in range(k) if LS[i][j][e]}
            if row: rows.append(row)
    sol = nullspace(rows, k) if k else []
    vecs = [[sum((s[i] * ns[i][col] for i in range(k) if s[i]), G()) for col in range(len(ns[0]))] for s in sol]
    return len(sol), vecs, (d, len(ns))

# injectivity of normal-form monomials -> q-series (so the count is of forms, not of polynomials)
def injective(d, prec):
    U = theta_squares(prec); MS = mono_series(d, prec, U); B = basis(d)
    rows = [{i: G(MS[b][e]) for i, b in enumerate(B) if MS[b][e]} for e in range(prec)]
    return rank_rows(rows, len(B)) == len(B)

OUT["D"] = {"injective_d15": injective(15, 160), "injective_d27": injective(27, 260)}
assert OUT["D"]["injective_d15"] and OUT["D"]["injective_d27"]

# whole spaces: dim M_k(rho_T) at k = 3/2 + 12N (no per-line data beyond holomorphy): m = (N, N, N) with the shift
def table(vectors, **kw):
    res = {}
    for m in vectors:
        res[m] = h0(m, **kw)[0]
    return res

E8 = list(itertools.product((0, 1), repeat=3))
T8 = table(E8)
UNI = [(n, n, n) for n in range(-1, 4)]
TU = table(UNI)
T64 = table(list(itertools.product((-1, 0, 1, 2), repeat=3)))
NONUNI3 = [(3, 0, 0), (0, 3, 0), (0, 0, 3), (2, 1, 0), (0, 2, 1), (1, 0, 2), (2, -1, 2), (3, 1, -1)]
T3 = table(NONUNI3)

def summ(m): return sum(m)
rowsout = []
for m in E8 + UNI + NONUNI3:
    hh = (T8.get(m) if m in T8 else TU.get(m) if m in TU else T3[m])
    x = chi(F(3, 2), RS, RT, m)
    rowsout.append({"m(P,M,N)": m, "h0": hh, "chi": str(x), "h1=h0-chi": str(hh - x), "index_empty_Lambda+": str(-x)})
OUT["D"]["rows"] = rowsout
OUT["D"]["formula_max0_sum_on_64"] = all(T64[m] == max(0, sum(m)) for m in T64)
OUT["D"]["formula_on_all_rows"] = all(r["h0"] == max(0, sum(r["m(P,M,N)"])) for r in rowsout)
OUT["D"]["chi_equals_sum"] = all(F(r["chi"]) == sum(r["m(P,M,N)"]) for r in rowsout)
OUT["D"]["h1_nonneg"] = all(F(r["h1=h0-chi"]) >= 0 for r in rowsout)
# compare with B1796's committed table (read as data: its run text states max(0, sum m) for all 64) and B1641's W3 (json)
REPO = str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())) + "/"
w3 = json.load(open(REPO + "frontier/B1641_w46_on_main_and_the_two_objects/verification/w46_on_main.json"))["W3"]
sealed = {n: [round(v["table"][f"0,n={n}"][0]) for v in w3.values()] for n in (-1, 0, 1)}
mine = {n: int(-chi(F(3, 2) + 12 * n, RS, RT)) for n in (-1, 0, 1)}
OUT["I"] = {"sealed_W3_empty_Lambda": sealed, "mine_minus_chi": mine,
            "agree": all(all(s == mine[n] for s in sealed[n]) for n in sealed)}
assert OUT["I"]["agree"]

# ---------------------------------------------------------------- V: move-invariance
V = {}
# (i) ruled moves through Mp2(Z): stabiliser of the cusp <rho(T), rho(S)^2>; T diagonal on (P, M, N) with distinct turns
turns = [EL[k][0] for k in ("P", "M", "N")]
V["ruled_moves"] = {"T_turns_on_lines": [str(t) for t in turns], "distinct": len(set(turns)) == 3,
                    "S2_scalar": (RS @ RS).is_scalar()}
def lattice_stable(T, vecs, m):
    """lattice sum_j x^{c_j - 8m_j} C[[x^8]] v_j: stable under T iff T maps each v_j to a multiple of a v_k with the same
    x-order residue and the same bound, i.e. iff T v_j is proportional to v_j (orders mod 8 differ between lines) or to a
    v_k with m_k = m_j. Exact on the vectors given (entries 0, +-1)."""
    import cmath
    Td = T.dense()
    for j, v in enumerate(vecs):
        w = [sum(Td[r][s] * v[s] for s in range(3)) for r in range(3)]
        ok = False
        for k, u in enumerate(vecs):
            # w proportional to u ?
            num = [(w[r], u[r]) for r in range(3)]
            lam = None; prop = True
            for a, b in num:
                if abs(b) > 1e-12:
                    lam = a / b if lam is None else lam
            if lam is None: continue
            prop = all(abs(a - lam * b) < 1e-12 for a, b in num)
            if prop and (k == j or m[k] == m[j]):
                ok = True
        if not ok: return False
    return True
eig_vecs = [EL[k][1] for k in ("P", "M", "N")]
V["ruled_moves"]["all_8_stable"] = all(lattice_stable(RT, eig_vecs, m) for m in E8)
# (ii) det -1 moves. Holomorphically (T -> T^-1, S -> S^-1): exponent set of rho o sigma
V["det-1_holomorphic"] = {"exponents_of_rho_o_sigma": [str(x) for x in RT.inv().eig_turns()],
                          "is_rho_T": RT.inv().eig_turns() == RT.eig_turns()}
# antiholomorphically, G(tau) = conj F(-conj tau): rho'(T) = conj(rho(T))^{-1}, rho'(S) = e^{-i pi k} conj(rho(S)), k = 3/2
def conjm(M): return Mono(M.p, [-x for x in M.t])
rTp = conjm(RT).inv(); rSp = conjm(RS).scal(F(-3, 4))
V["det-1_antiholomorphic"] = {"rho_prime_equals_rho": rTp == RT and rSp == RS}
# its action on each H0(m): conjugating coefficients; the space must be stable (dimension of span(basis + conj basis))
def conj_stable(m):
    dim, ns, _ = h0(m)
    if dim == 0: return True
    n = len(ns[0])
    rows = [{c: v for c, v in enumerate(vec) if v} for vec in ns] + [{c: v.conj() for c, v in enumerate(vec) if v} for vec in ns]
    return rank_rows(rows, n) == dim
V["det-1_antiholomorphic"]["H0_conj_stable_on_8"] = all(conj_stable(m) for m in E8)
# (iii) fibre loops (inner automorphisms, NOT moves; B1634): parity signs, labels from B1634 line 77
labels = {0: (1, -1), 1: (-1, -1), 2: (-1, 1)}            # theta_2^2 (+,-), theta_3^2 (-,-), theta_4^2 (-,+)
par = {}
for name, pick in (("conj(a)", lambda l: l[0]), ("conj(b)", lambda l: l[1]), ("conj(ab)", lambda l: l[0] * l[1])):
    D = [pick(labels[r]) for r in range(3)]
    act = []
    for j, v in enumerate(eig_vecs):
        w = tuple(D[r] * v[r] for r in range(3))
        k = [kk for kk, u in enumerate(eig_vecs) if all(w[r] == u[r] for r in range(3)) or all(w[r] == -u[r] for r in range(3))]
        act.append(("P", "M", "N")[k[0]])
    commutes = all(D[RT.p[j]] * 1 == D[j] for j in range(3))
    par[name] = {"signs_on_(th2,th3,th4)": D, "images_of_(P,M,N)": act, "commutes_with_rho_T(T)": commutes}
V["fibre_loops_parity"] = par
perms = [p["images_of_(P,M,N)"] for p in par.values()]
def invariant(m):
    for img in perms:
        mm = {img[j]: m[j] for j in range(3)}
        if tuple(mm[k] for k in ("P", "M", "N")) != m: return False
    return True
V["fibre_loops_parity"]["invariant_in_{0,1}^3"] = [m for m in E8 if invariant(m)]
OUT["V"] = V

# ---------------------------------------------------------------- C: planted controls (each check must FAIL)
CT = {}
# C1: M and N exponents swapped in the per-line bound -> direct count vs max(0, sum m) must disagree somewhere
c_bad = (1, 3, 7)
t_bad = {m: h0(m, c=c_bad)[0] for m in itertools.product((-1, 0, 1), repeat=3)}
CT["C1_swapped_lines"] = {"check_formula_holds": all(t_bad[m] == max(0, sum(m)) for m in t_bad),
                          "first_disagreements": [(m, t_bad[m], max(0, sum(m))) for m in t_bad if t_bad[m] != max(0, sum(m))][:6]}
# C2: the old sign (index = +chi) against B1641's sealed table
CT["C2_old_sign"] = {"check_agrees_with_sealed": all(all(s == int(chi(F(3, 2) + 12 * n, RS, RT)) for s in sealed[n]) for n in sealed)}
# C3: rho(S) -> -rho(S): Mp2(Z) relations
CT["C3_S_sign"] = rep_checks(RS.scal(F(1, 2)), RT, "bad")
CT["C3_S_sign"]["h0_table_on_8_if_used"] = {str(m): h0(m, swap_S_sign=True)[0] for m in E8}
# C4: parity-basis lattice (lines e2, e3, e4) with m3 != m4: T-stability must fail
par_vecs = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
CT["C4_parity_basis"] = {"check_stable_(0,1,0)": lattice_stable(RT, par_vecs, (0, 1, 0)),
                         "check_stable_(0,1,1)_control_pass": lattice_stable(RT, par_vecs, (0, 1, 1))}
OUT["C"] = CT
caught = {"C1": not CT["C1_swapped_lines"]["check_formula_holds"], "C2": not CT["C2_old_sign"]["check_agrees_with_sealed"],
          "C3": not CT["C3_S_sign"]["valid"], "C4": not CT["C4_parity_basis"]["check_stable_(0,1,0)"]}
OUT["C"]["caught"] = caught

def show(o):
    return json.dumps(o, indent=1, default=lambda x: list(x) if isinstance(x, tuple) else str(x))
print(show(OUT))
json.dump(json.loads(show(OUT)), open(__file__.replace(".py", "_out.json"), "w"), indent=1)
