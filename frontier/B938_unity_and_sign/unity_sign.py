#!/usr/bin/env python3
"""B938 -- THE UNITY COLUMN + THE SIGN OF FULL FLIP (lanes Q4+Q5; blind).

PART A (Q4): identify the rotation's unity column -- the rational line
F cap W3 (B930's exact unity principal angle between the twist frame and
the vacuum register) -- STRUCTURALLY: its exact integer 27-vector, its
branch expansion v* = Tr_{K/Q}(kappa . vS) (which S-combination), the
equal-angle theorem 3 kappa^2 q_S = h(v*,v*) in Q (the banked cos^2 = 1/3
elevated to a K-identity), its weight/charge data, and its stabilizer
under the banked S3 (Galois) branch action, at three levels of structure.

PART B (Q5): the sign question.  B931's ADDENDUM (the level song): the
flip-mass level norms carry 11 at m = +1 and 7^2 at m = -1, both
families, for the twist D2 = +-rho27(sigma_chi-).  B928 banked the full
2-torsion {I, D2, D, D2D} = +-rho27({1, sigma_chi-, sigma_-1,
sigma_chi+}) (D = B912's wall twist, H- = H+ D).  Compute the SAME level
tables for the other two Klein members (each re-derived by pure rep
propagation and sign-pinned by its banked diagonal): do 7 and 11 swap
sides?  Track?  Or is the split D2-specific?

HOUSE RULES: exact arithmetic for every verdict-bearing claim (K =
Q[rho]/mu13 only -- no N/Mbar tower is needed here: every Part A/B object
is a K-element or rational); verify-don't-trust (D2/D/D2D re-DERIVED from
the wall sign vectors by rep propagation, then compared to the banked
B916/B912 diagonals; m_S/m_A for D2 re-derived and gated against the
banked B928 K-coordinates AND the B931 ADDENDUM norm table before any new
number is trusted); e6_centralizer.py exec'd in an isolated namespace
with chdir to scratch and __file__ set; no Rayleigh eigenreads (the only
numerics are polynomial-root evaluations with residual/product belts);
DEFINITENESS DISCIPLINE: no form assumed positive -- the register norms
are negative (B912/B930), signs threaded, |.| used only after the sign
vector is computed and recorded.  BLIND: no measured number contacted.

Output: results.json (exact data + checks).
"""
import io
import os
import json
import math
import time
import pickle
import tempfile
import contextlib
import itertools
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b938_")
os.makedirs(SCRATCH, exist_ok=True)
T00 = time.time()
RES = {"cell": "B938 unity column + sign of full flip", "checks": {},
       "notes": []}


def log(*a):
    print(f"[{time.time()-T00:7.1f}s]", *a, flush=True)


def dump():
    json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)


def CHK(name, ok, detail=""):
    RES["checks"][name] = {"pass": bool(ok), "detail": str(detail)}
    log(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        RES["verdict"] = "UNSTABLE"
        dump()
        raise SystemExit(f"UNSTABLE at {name}")


def REC(name, value, detail=""):
    RES["checks"][name] = {"value": value, "detail": str(detail)}
    log(f"  [DATA] {name} = {str(value)[:110]} {detail}")


# ================================================================ [0] inputs
log("[0] banked inputs: rep27, B912 H+/D, B916 D2, B907 walls, B928/B930/B931"
    " gates")
REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27",
                                   "rep27.json")))
REP = [[[int(x) for x in row] for row in REPJ["rep"][str(k)]]
       for k in range(78)]
WT = [tuple(REP[i][a][a] for i in range(6)) for a in range(27)]
CHK("rep27_cartan_diagonal_27_distinct_weights",
    all(all(REP[i][a][b] == 0 for a in range(27) for b in range(27) if a != b)
        for i in range(6)) and len(set(WT)) == 27)

B912 = json.load(open(os.path.join(REPO, "frontier", "B912_norm_cell",
                                   "results.json")))
cbP = [int(x) for x in B912["H_plus_entries_c_b"]]
D_banked = [int(x) for x in B912["D_diag"]]
B916 = json.load(open(os.path.join(REPO, "frontier", "B916_lambda_bridge",
                                   "results.json")))
D2_banked = [int(x) for x in B916["H_prime_diag_vs_H_plus"]["D2"]]
B907V = json.load(open(os.path.join(REPO, "frontier",
                                    "B907_real_form_selector", "verdict.json")))
CHI_P = tuple(int(x) for x in B907V[0]["signs"])
CHI_M = tuple(int(x) for x in B907V[1]["signs"])
CHK("banked_wall_pair_is_a_global_negation",
    CHI_M == tuple(-x for x in CHI_P), f"chi+ = {CHI_P}")
B928R = json.load(open(os.path.join(REPO, "frontier", "B928_d2_decode",
                                    "results.json")))
B930R = json.load(open(os.path.join(REPO, "frontier", "B930_overlap_matrix",
                                    "results.json")))

FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}


def flipw(w):
    return tuple(w[FLIP[i]] for i in range(6))


negflip = {tuple(-x for x in flipw(WT[b])): b for b in range(27)}
piW = [negflip[WT[b]] for b in range(27)]
CHK("weight_pairing_pi_recomputed_and_involutive",
    sorted(piW) == list(range(27)) and all(piW[piW[b]] == b for b in range(27)))
CHK("H_plus_symmetric", all(cbP[piW[b]] == cbP[b] for b in range(27)))

ROOTS6 = None  # set in [1]


def chi_of(signs):
    def ch(r):
        v = 1
        for i in range(6):
            if r[i] % 2:
                v *= signs[i]
        return v
    return ch


def rep_diagonal_of_inner(signs):
    """the unique (up to global sign) +-1 diagonal T with
    T rho(x) T = rho(sigma_chi x); None if inconsistent.  Pure rep
    propagation (the B928/B930 instrument)."""
    ch = chi_of(signs)
    T_ = [None] * 27
    T_[0] = 1
    changed = True
    while changed:
        changed = False
        for kr, r in enumerate(ROOTS6):
            M = REP[6 + kr]
            c = ch(r)
            for a in range(27):
                for b in range(27):
                    if M[a][b]:
                        if T_[b] is not None and T_[a] is None:
                            T_[a] = c * T_[b]
                            changed = True
                        elif T_[a] is not None and T_[b] is None:
                            T_[b] = c * T_[a]
                            changed = True
    if any(t is None for t in T_):
        return None
    for kr, r in enumerate(ROOTS6):
        M = REP[6 + kr]
        c = ch(r)
        for a in range(27):
            for b in range(27):
                if M[a][b] and T_[a] != c * T_[b]:
                    return None
    return T_


# ================================================================ [1] frame
log("[1] B854 frame (isolated exec, chdir scratch, __file__ set) ...")
cache = os.path.join(SCRATCH, "b930_frame_cache.pkl")
if os.path.exists(cache):
    FR = pickle.load(open(cache, "rb"))
else:
    cwd = os.getcwd()
    g6 = {"__file__": os.path.join(SCRATCH, "e6_centralizer.py"),
          "__name__": "b854_frame"}
    src = open(os.path.join(REPO, "frontier", "B854_centralizer_exact",
                            "e6_centralizer.py")).read()
    try:
        os.chdir(SCRATCH)
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, "b854", "exec"), g6)
    finally:
        os.chdir(cwd)
    FR = {"ROOTS": [tuple(r) for r in g6["ROOTS"]],
          "ns": list(g6["ns"]),
          "INV": {n: [Fr(c) for c in g6["INV"][n]] for n in g6["ns"]}}
    pickle.dump(FR, open(cache, "wb"))
ROOTS6 = FR["ROOTS"]
ns = FR["ns"]
INV = FR["INV"]
CHK("frame_72_roots_ns_8_14_16_22", len(ROOTS6) == 72
    and sorted(ns) == [8, 14, 16, 22])

Rex = {}
for n in ns:
    M = [[Fr(0)] * 27 for _ in range(27)]
    for k, c in enumerate(INV[n]):
        if c:
            Rk = REP[k]
            for a in range(27):
                ra = Rk[a]
                for b in range(27):
                    if ra[b]:
                        M[a][b] += c * ra[b]
    Rex[n] = M
CHK("four_charges_commute_exactly",
    all(all(sum(Rex[m_][i][t] * Rex[n_][t][j] for t in range(27))
            == sum(Rex[n_][i][t] * Rex[m_][t][j] for t in range(27))
            for i in range(27) for j in range(27))
        for m_, n_ in itertools.combinations(ns, 2)))
EPSPAT = {8: -1, 14: 1, 16: -1, 22: 1}
ok = True
for n in ns:
    for a in range(27):
        for b in range(27):
            v = Rex[n][piW[b]][a] * cbP[b] \
                + EPSPAT[n] * cbP[piW[a]] * Rex[n][piW[a]][b]
            if v != 0:
                ok = False
CHK("H_plus_charge_equivariance_eps_m1_p1_m1_p1_exact", ok,
    "Rn^T H+ = -eps_n H+ Rn, eps = (-1,+1,-1,+1)")

# THE KLEIN GROUP re-derived: D2 = rho27(sigma_chi-), D = rho27(sigma_-1),
# D2D = rho27(sigma_chi+) -- each by pure rep propagation, each sign-pinned
# at entry 0 = +1 (the convention BOTH banked diagonals satisfy).
T_chim = rep_diagonal_of_inner(CHI_M)
CHK("D2_rederived_as_rep_diagonal_of_sigma_chi_minus", T_chim is not None)
D2 = T_chim if T_chim[0] == 1 else [-x for x in T_chim]
CHK("D2_equals_banked_B916_diagonal", D2 == D2_banked)
T_m1 = rep_diagonal_of_inner((-1, -1, -1, -1, -1, -1))
CHK("D_rederived_as_rep_diagonal_of_sigma_minus1", T_m1 is not None)
Dw = T_m1 if T_m1[0] == 1 else [-x for x in T_m1]
CHK("D_equals_banked_B912_wall_diagonal", Dw == D_banked,
    "H- = H+ D: the wall twist, sign-pinned by the bank")
T_chip = rep_diagonal_of_inner(CHI_P)
CHK("D2D_rederived_as_rep_diagonal_of_sigma_chi_plus", T_chip is not None)
DD = T_chip if T_chip[0] == 1 else [-x for x in T_chip]
CHK("klein_closure_D2_times_D_equals_D2D",
    [D2[b] * Dw[b] for b in range(27)] == DD,
    "{I, D2, D, D2D} = rho27 of the wall pair's 2-torsion, entry0-pinned: "
    "an honest Klein four-group of diagonals")
TWISTS = [("D2", D2), ("D", Dw), ("D2D", DD)]
for nm, T in TWISTS:
    CHK(f"{nm}_pi_symmetric_flip_count",
        all(T[piW[b]] == T[b] for b in range(27)),
        f"flips = {sum(1 for x in T if x == -1)}")
REC("flip_counts", {nm: sum(1 for x in T if x == -1) for nm, T in TWISTS},
    "tr Pi_T = flip count; D2: 11 (B928), D: 12, D2D: 15")
dump()

# ================================================================ [2] K
log("[2] exact K = Q[rho]/mu13 arithmetic ...")
MU = [500716339200, -2075673600, -4769856, 2197]
A_, B_, C_, D_ = MU
R3K = [Fr(-D_, A_), Fr(-C_, A_), Fr(-B_, A_)]
R4K = [R3K[2] * R3K[0], R3K[0] + R3K[2] * R3K[1], R3K[1] + R3K[2] * R3K[2]]
KZERO = (Fr(0), Fr(0), Fr(0))
KONE = (Fr(1), Fr(0), Fr(0))
b_mu = Fr(MU[1], MU[0])
c_mu = Fr(MU[2], MU[0])
d_mu = Fr(MU[3], MU[0])


def kmul(x, y):
    c0 = x[0] * y[0]
    c1 = x[0] * y[1] + x[1] * y[0]
    c2 = x[0] * y[2] + x[1] * y[1] + x[2] * y[0]
    c3 = x[1] * y[2] + x[2] * y[1]
    c4 = x[2] * y[2]
    if c4:
        c0 += c4 * R4K[0]
        c1 += c4 * R4K[1]
        c2 += c4 * R4K[2]
    if c3:
        c0 += c3 * R3K[0]
        c1 += c3 * R3K[1]
        c2 += c3 * R3K[2]
    return (c0, c1, c2)


def kadd(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


def ksub(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2])


def kscale(x, s):
    return (x[0] * s, x[1] * s, x[2] * s)


def kis0(x):
    return not (x[0] or x[1] or x[2])


def kinv(x):
    cols = [kmul(x, KONE), kmul(x, (Fr(0), Fr(1), Fr(0))),
            kmul(x, (Fr(0), Fr(0), Fr(1)))]
    Aug = [[cols[j][i] for j in range(3)] + [Fr(1) if i == 0 else Fr(0)]
           for i in range(3)]
    for c in range(3):
        pr = next(r for r in range(c, 3) if Aug[r][c] != 0)
        Aug[c], Aug[pr] = Aug[pr], Aug[c]
        iv = Aug[c][c]
        Aug[c] = [e / iv for e in Aug[c]]
        for r in range(3):
            if r != c and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[c][j] for j in range(4)]
    return (Aug[0][3], Aug[1][3], Aug[2][3])


def kmultmat(x):
    """3x3 rational multiplication matrix of x in basis (1, rho, rho^2)."""
    cols = [kmul(x, KONE), kmul(x, (Fr(0), Fr(1), Fr(0))),
            kmul(x, (Fr(0), Fr(0), Fr(1)))]
    return [[cols[j][i] for j in range(3)] for i in range(3)]


def ktrace(x):
    Mv = kmultmat(x)
    return Mv[0][0] + Mv[1][1] + Mv[2][2]


def knorm(x):
    Mv = kmultmat(x)
    return (Mv[0][0] * (Mv[1][1] * Mv[2][2] - Mv[1][2] * Mv[2][1])
            - Mv[0][1] * (Mv[1][0] * Mv[2][2] - Mv[1][2] * Mv[2][0])
            + Mv[0][2] * (Mv[1][0] * Mv[2][1] - Mv[1][1] * Mv[2][0]))


def qkernel(M):
    m, n = len(M), len(M[0])
    A2 = [row[:] for row in M]
    piv = []
    rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if A2[r][c] != 0), None)
        if pr is None:
            continue
        A2[rr], A2[pr] = A2[pr], A2[rr]
        iv = A2[rr][c]
        A2[rr] = [e / iv for e in A2[rr]]
        for r in range(m):
            if r != rr and A2[r][c]:
                f = A2[r][c]
                A2[r] = [A2[r][j] - f * A2[rr][j] for j in range(n)]
        piv.append(c)
        rr += 1
    ker = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -A2[i][fc]
        ker.append(v)
    return ker


def qsolve_span(basis, vec):
    k, n = len(basis), len(basis[0])
    Aug = [[basis[j][i] for j in range(k)] + [vec[i]] for i in range(n)]
    piv = []
    rr = 0
    for c in range(k):
        pr = next((r for r in range(rr, n) if Aug[r][c] != 0), None)
        if pr is None:
            continue
        Aug[rr], Aug[pr] = Aug[pr], Aug[rr]
        iv = Aug[rr][c]
        Aug[rr] = [e / iv for e in Aug[rr]]
        for r in range(n):
            if r != rr and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[rr][j] for j in range(k + 1)]
        piv.append(c)
        rr += 1
    sol = [Fr(0)] * k
    for i, c in enumerate(piv):
        sol[c] = Aug[i][k]
    for i in range(n):
        if sum(sol[j] * basis[j][i] for j in range(k)) != vec[i]:
            return None
    return sol


def matmulQ(Xm, Ym):
    n = len(Xm)
    m = len(Ym[0])
    kk = len(Ym)
    return [[sum(Xm[i][t2] * Ym[t2][j] for t2 in range(kk) if Xm[i][t2])
             for j in range(m)] for i in range(n)]


def kkernel(M):
    m, n = len(M), len(M[0])
    A2 = [row[:] for row in M]
    piv = []
    rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if not kis0(A2[r][c])), None)
        if pr is None:
            continue
        A2[rr], A2[pr] = A2[pr], A2[rr]
        iv = kinv(A2[rr][c])
        A2[rr] = [kmul(iv, e) for e in A2[rr]]
        for r in range(m):
            if r != rr and not kis0(A2[r][c]):
                f = A2[r][c]
                A2[r] = [ksub(A2[r][j], kmul(f, A2[rr][j])) for j in range(n)]
        piv.append(c)
        rr += 1
    ker = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [KZERO] * n
        v[fc] = KONE
        for i, c in enumerate(piv):
            v[c] = kscale(A2[i][fc], Fr(-1))
        ker.append(v)
    return ker


import sympy as sp
from sympy import factorint
import mpmath
from mpmath import mp


def _ratrec_real(x, maxden):
    f = mp.mpf(x)
    p0, q0, p1, q1 = mp.mpf(0), mp.mpf(1), mp.mpf(1), mp.mpf(0)
    r = f
    for _ in range(4000):
        a = mp.floor(r)
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        if q1 > maxden or r == a:
            break
        den = r - a
        if den == 0:
            break
        r = 1 / den
    if q1 > maxden:
        p1, q1 = p0, q0
    if q1 == 0:
        return None
    num, den = int(mp.nint(p1)), int(mp.nint(q1))
    if den < 0:
        num, den = -num, -den
    return Fr(num, den) if den else None


def _mu_roots_numeric(dps=400):
    mp.dps = dps
    rts = mp.polyroots([mp.mpf(c) for c in MU], maxsteps=300, extraprec=400)
    return [mp.re(r) for r in rts]


def _interp_K(vals, mu_roots, maxden, hmax):
    M3 = mp.matrix(3, 3)
    for i in range(3):
        M3[i, 0] = 1
        M3[i, 1] = mu_roots[i]
        M3[i, 2] = mu_roots[i] ** 2
    try:
        solv = mp.lu_solve(M3, mp.matrix(vals))
    except Exception:
        return None
    cand = []
    for v in solv:
        r = _ratrec_real(v, maxden)
        if r is None or max(abs(r.numerator), r.denominator) > hmax:
            return None
        cand.append(r)
    return tuple(cand)


def keval_poly(coeffs, kx):
    acc = (Fr(sp.Rational(coeffs[0]).p, sp.Rational(coeffs[0]).q),
           Fr(0), Fr(0))
    for c in coeffs[1:]:
        acc = kmul(acc, kx)
        acc = (acc[0] + Fr(sp.Rational(c).p, sp.Rational(c).q),
               acc[1], acc[2])
    return acc


def root_in_K(h_coeffs, dps=400, hmax=10 ** 120):
    mu_roots = _mu_roots_numeric(dps)
    hh = [mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q)
          for c in h_coeffs]
    h_roots = mp.polyroots(hh, maxsteps=400, extraprec=400)
    reals = [mp.re(r) for r in h_roots
             if abs(mp.im(r)) < mp.mpf(10) ** (-dps // 2)]
    maxden = mp.mpf(10) ** (dps // 3)
    for pick in itertools.permutations(range(len(reals)), 3):
        cand = _interp_K([reals[pick[j]] for j in range(3)], mu_roots,
                         maxden, hmax)
        if cand is None:
            continue
        if kis0(keval_poly([sp.Rational(c) for c in h_coeffs], cand)):
            return cand
    return None


def sqrt_in_K(targetk, dps=400, hmax=10 ** 120):
    mu_roots = _mu_roots_numeric(dps)

    def kev(x, r):
        return (mp.mpf(x[0].numerator) / x[0].denominator
                + (mp.mpf(x[1].numerator) / x[1].denominator) * r
                + (mp.mpf(x[2].numerator) / x[2].denominator) * r * r)
    tv = [kev(targetk, r) for r in mu_roots]
    if any(t < 0 for t in tv):
        return None
    sq = [mp.sqrt(t) for t in tv]
    maxden = mp.mpf(10) ** (dps // 3)
    for sgs in itertools.product((1, -1), repeat=2):
        vals = [sq[0], sgs[0] * sq[1], sgs[1] * sq[2]]
        cand = _interp_K(vals, mu_roots, maxden, hmax)
        if cand is None:
            continue
        if kis0(ksub(kmul(cand, cand), targetk)):
            return cand
    return None


def kcharpoly3(kx):
    Mv = kmultmat(kx)
    x = sp.Symbol("x")
    Msp = sp.Matrix(3, 3, lambda i, j: sp.Rational(Mv[i][j].numerator,
                                                   Mv[i][j].denominator))
    return [sp.Rational(c) for c in Msp.charpoly(x).all_coeffs()]


def int_primitive(coeffs):
    den = 1
    for c in coeffs:
        den = den * sp.Rational(c).q // math.gcd(den, sp.Rational(c).q)
    ints = [int(sp.Rational(c) * den) for c in coeffs]
    g = 0
    for v in ints:
        g = math.gcd(g, abs(v))
    ints = [v // g for v in ints] if g else ints
    if ints and ints[0] < 0:
        ints = [-v for v in ints]
    return ints


def kminpoly(kx):
    cp = kcharpoly3(kx)
    x = sp.Symbol("x")
    poly = sp.Poly([sp.Rational(c) for c in cp], x)
    for f, _m in sorted(sp.factor_list(poly.as_expr())[1],
                        key=lambda t: sp.degree(t[0], x)):
        fc = sp.Poly(f, x).all_coeffs()
        if kis0(keval_poly([sp.Rational(c) for c in fc], kx)):
            return int_primitive(fc)
    return int_primitive(cp)


def knum(kx, r):
    return (mp.mpf(kx[0].numerator) / kx[0].denominator
            + (mp.mpf(kx[1].numerator) / kx[1].denominator) * r
            + (mp.mpf(kx[2].numerator) / kx[2].denominator) * r * r)


# ================================================================ [3] lines
log("[3] the colorless registers and lines over K (B930 route, re-run) ...")
CO = {8: 3, 14: 7, 16: 13, 22: 17}
Mc = [[sum(Fr(CO[n]) * Rex[n][i][j] for n in ns) for j in range(27)]
      for i in range(27)]
x = sp.Symbol("x")
cp27 = sp.Matrix(27, 27, lambda i, j: sp.Rational(Mc[i][j].numerator,
                                                  Mc[i][j].denominator)
                 ).charpoly(x)
fl = sp.factor_list(cp27.as_expr())
facs = sorted([(sp.degree(f, x), m, sp.Poly(f, x)) for f, m in fl[1]])
CHK("charpoly_Mc_factors_3_1__6_1__6_3",
    [(d, m) for d, m, _ in facs] == [(3, 1), (6, 1), (6, 3)])
h_S = [int(c) for c in facs[0][2].all_coeffs()]
h_A = [int(c) for c in facs[1][2].all_coeffs()]
h_col_ints = [sp.Rational(c) for c in facs[2][2].all_coeffs()]


def poly_mat(coeffs):
    Acc = [[Fr(sp.Rational(coeffs[0]).p, sp.Rational(coeffs[0]).q)
            if i == j else Fr(0) for j in range(27)] for i in range(27)]
    for c in coeffs[1:]:
        Acc = matmulQ(Acc, Mc)
        cf = Fr(sp.Rational(c).p, sp.Rational(c).q)
        for i in range(27):
            Acc[i][i] += cf
    return Acc


W3 = qkernel(poly_mat(h_S))
W6 = qkernel(poly_mat(h_A))
W18 = qkernel(poly_mat(h_col_ints))
CHK("rational_blocks_dim_3_6_18", len(W3) == 3 and len(W6) == 6
    and len(W18) == 18)
stack = W3 + W6 + W18
rk = 27 - len(qkernel([[stack[a][i] for a in range(27)] for i in range(27)]))
CHK("register_blocks_span_Q27", rk == 27)

Me = [[Fr(3) * Rex[8][i][j] + Fr(13) * Rex[16][i][j] for j in range(27)]
      for i in range(27)]
Mo = [[Fr(7) * Rex[14][i][j] + Fr(17) * Rex[22][i][j] for j in range(27)]
      for i in range(27)]


def restrict(Mbig, W):
    Crows = []
    for w in W:
        img = [sum(Mbig[i][j] * w[j] for j in range(27) if w[j])
               for i in range(27)]
        solv = qsolve_span(W, img)
        assert solv is not None
        Crows.append(solv)
    return [[Crows[b][a] for b in range(len(W))] for a in range(len(W))]


C_S = restrict(Mc, W3)
C_E = restrict(Me, W6)
C_O = restrict(Mo, W6)
cpE = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_E[i][j].numerator,
                                               C_E[i][j].denominator)
                ).charpoly(x)
flE = sp.factor_list(cpE.as_expr())
gs = [(f, m) for f, m in flE[1] if sp.degree(f, x) > 0]
CHK("char_Me_W6_is_g_squared_cubic", len(gs) == 1 and gs[0][1] == 2
    and sp.degree(gs[0][0], x) == 3)
g_even = sp.Poly(gs[0][0], x).all_coeffs()
g_even = [sp.Rational(c, g_even[0]) for c in g_even]
cpO = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_O[i][j].numerator,
                                               C_O[i][j].denominator)
                ).charpoly(x)
co = sp.Poly(cpO.as_expr(), x).all_coeffs()
CHK("char_Mo_W6_even", co[1] == 0 and co[3] == 0 and co[5] == 0)
h_B = [co[0], co[2], co[4], co[6]]
xS = root_in_K([sp.Rational(c) for c in h_S])
alph = root_in_K(g_even)
Bk = root_in_K(h_B)
CHK("K_roots_xS_alpha_B_found", None not in (xS, alph, Bk))
wK = sqrt_in_K(kscale(Bk, Fr(-1, 3)))
CHK("B_equals_minus_3_w_squared", wK is not None
    and kis0(ksub(kmul(wK, wK), kscale(Bk, Fr(-1, 3)))))

CmK = [[ksub((Fr(C_S[i][j]), Fr(0), Fr(0)), xS if i == j else KZERO)
        for j in range(3)] for i in range(3)]
kerS = kkernel(CmK)
CHK("kernel_S_dim_1", len(kerS) == 1)
vS3 = kerS[0]


def fmulB(a, b):
    return (kadd(kmul(a[0], b[0]), kmul(Bk, kmul(a[1], b[1]))),
            kadd(kmul(a[0], b[1]), kmul(a[1], b[0])))


def fsubB(a, b):
    return (ksub(a[0], b[0]), ksub(a[1], b[1]))


def fis0B(a):
    return kis0(a[0]) and kis0(a[1])


def finvB(a):
    den = ksub(kmul(a[0], a[0]), kmul(Bk, kmul(a[1], a[1])))
    di = kinv(den)
    return (kmul(a[0], di), kscale(kmul(a[1], di), Fr(-1)))


rowsF = []
for i in range(6):
    rowsF.append([(ksub((Fr(C_E[i][j]), Fr(0), Fr(0)),
                        alph if i == j else KZERO), KZERO) for j in range(6)])
for i in range(6):
    rowsF.append([((Fr(C_O[i][j]), Fr(0), Fr(0)),
                   (Fr(-1), Fr(0), Fr(0)) if i == j else KZERO)
                  for j in range(6)])
A2m = [row[:] for row in rowsF]
piv = []
rr = 0
for c in range(6):
    pr = next((r for r in range(rr, 12) if not fis0B(A2m[r][c])), None)
    if pr is None:
        continue
    A2m[rr], A2m[pr] = A2m[pr], A2m[rr]
    iv = finvB(A2m[rr][c])
    A2m[rr] = [fmulB(iv, e) for e in A2m[rr]]
    for r in range(12):
        if r != rr and not fis0B(A2m[r][c]):
            f = A2m[r][c]
            A2m[r] = [fsubB(A2m[r][j], fmulB(f, A2m[rr][j])) for j in range(6)]
    piv.append(c)
    rr += 1
FZ = (KZERO, KZERO)
kerA = []
for fc in [c for c in range(6) if c not in piv]:
    v = [FZ] * 6
    v[fc] = (KONE, KZERO)
    for i, c in enumerate(piv):
        v[c] = fsubB(FZ, A2m[i][fc])
    kerA.append(v)
CHK("kernel_nonS_dim_1_over_K_beta", len(kerA) == 1)
vA6 = kerA[0]


def lift(coords, W):
    out = []
    for i in range(27):
        acc = KZERO
        for a, cf in enumerate(coords):
            if W[a][i]:
                acc = kadd(acc, kscale(cf, W[a][i]))
        out.append(acc)
    return out


def normalize27(vec):
    L2 = 1
    for kt in vec:
        for x2 in kt:
            if x2:
                d = x2.denominator
                L2 = L2 * d // math.gcd(L2, d)
    vec2 = [kscale(kt, Fr(L2)) for kt in vec]
    G = 0
    for kt in vec2:
        for x2 in kt:
            G = math.gcd(G, abs(x2.numerator))
    if G > 1:
        vec2 = [kscale(kt, Fr(1, G)) for kt in vec2]
    return vec2


vS27 = normalize27(lift(vS3, W3))
u27 = lift([f[0] for f in vA6], W6)
wt27 = lift([f[1] for f in vA6], W6)
wodd27 = [kmul(wK, kt) for kt in wt27]
uw = normalize27(u27 + wodd27)
u27, wodd27 = uw[:27], uw[27:]


def kq(vec, cb, subset=None):
    acc = KZERO
    rng = range(27) if subset is None else subset
    for b in rng:
        a = piW[b]
        if kis0(vec[a]) or kis0(vec[b]):
            continue
        acc = kadd(acc, kscale(kmul(vec[a], vec[b]), Fr(cb[b])))
    return acc


def kq_A(cb, subset=None):
    even = KZERO
    cross = KZERO
    rng = range(27) if subset is None else subset
    for b in rng:
        a = piW[b]
        t1 = kmul(u27[a], u27[b])
        t2 = kmul(wodd27[a], wodd27[b])
        even = kadd(even, kscale(kadd(t1, kscale(t2, Fr(3))), Fr(cb[b])))
        c1 = kmul(u27[a], wodd27[b])
        c2 = kmul(wodd27[a], u27[b])
        cross = kadd(cross, kscale(ksub(c1, c2), Fr(cb[b])))
    return even, cross


qS = kq(vS27, cbP)
qA, crossA = kq_A(cbP)
CHK("A_norm_tau_free_and_q_nonzero", kis0(crossA)
    and not (kis0(qS) or kis0(qA)))
qSi = kinv(qS)
qAi = kinv(qA)

# GATE: the D2 flip masses re-derived = banked B928 K-coordinates
flip_D2 = [b for b in range(27) if D2[b] == -1]
m_S = kmul(kq(vS27, cbP, flip_D2), qSi)
evF, crF = kq_A(cbP, flip_D2)
CHK("D2_A_flip_cross_term_zero", kis0(crF))
m_A = kmul(evF, qAi)
CHK("m_S_banked_B928_coords",
    m_S == (Fr(52571, 64896), Fr(-55825, 2197), Fr(27165600, 28561)),
    "the banked B928 sheet entry 1, re-derived")
CHK("m_A_banked_B928_coords",
    m_A == (Fr(7291, 32448), Fr(31955, 2197), Fr(461815200, 28561)),
    "the banked B928 sheet entry 2, re-derived")
CHK("m_S_minpoly_equals_banked_B928",
    kminpoly(m_S) == [int(c) for c in B928R["Q2_colorless"]["minpoly_m_S"]])
dump()

# ================================================================ [4] PART A
log("[4] PART A: the unity column -- the rational line F cap W3 ...")


def gramQ(W, cb, subset=None):
    k = len(W)
    rng = range(27) if subset is None else subset
    G = [[Fr(0)] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            acc = Fr(0)
            for b in rng:
                a = piW[b]
                if W[i][a] and W[j][b]:
                    acc += W[i][a] * Fr(cb[b]) * W[j][b]
            G[i][j] = acc
    return G


def qinv_mat(G):
    k = len(G)
    Aug = [[G[i][j] for j in range(k)]
           + [Fr(1) if i == j2 else Fr(0) for j2 in range(k)]
           for i in range(k)]
    for c in range(k):
        pr = next((r for r in range(c, k) if Aug[r][c] != 0), None)
        assert pr is not None
        Aug[c], Aug[pr] = Aug[pr], Aug[c]
        iv = Aug[c][c]
        Aug[c] = [e / iv for e in Aug[c]]
        for r in range(k):
            if r != c and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[c][j] for j in range(2 * k)]
    return [[Aug[i][k + j] for j in range(k)] for i in range(k)]


G3 = gramQ(W3, cbP)
G6 = gramQ(W6, cbP)
G18 = gramQ(W18, cbP)
G3i = qinv_mat(G3)
G6i = qinv_mat(G6)
G18i = qinv_mat(G18)

Hf3_D2 = gramQ(W3, cbP, flip_D2)
Cmp3 = matmulQ(G3i, Hf3_D2)
cp3 = sp.Matrix(3, 3, lambda i, j: sp.Rational(Cmp3[i][j].numerator,
                                               Cmp3[i][j].denominator)
                ).charpoly(x)
fac3 = sp.factor_list(cp3.as_expr())
fac3_repr = sorted([(int(sp.degree(f, x)), int(m),
                     int_primitive(sp.Poly(f, x).all_coeffs()))
                    for f, m in fac3[1]])
CHK("A_W3_charpoly_matches_banked_B930",
    fac3_repr == [(1, 1, [1, -1]), (2, 1, [1536, -2088, 677])],
    "(x-1)(1536x^2-2088x+677)")
CmI = [[Cmp3[i][j] - (1 if i == j else 0) for j in range(3)]
       for i in range(3)]
ker1 = qkernel(CmI)
CHK("A_eigenvalue_1_multiplicity_one", len(ker1) == 1)
vstar_raw = [sum(ker1[0][a] * W3[a][i] for a in range(3)) for i in range(27)]
# integer normalization + sign convention: first nonzero entry positive
L = 1
for v in vstar_raw:
    if v:
        L = L * v.denominator // math.gcd(L, v.denominator)
vint = [v * L for v in vstar_raw]
G = 0
for v in vint:
    G = math.gcd(G, abs(v.numerator))
vint = [v / G for v in vint]
first = next(v for v in vint if v)
if first < 0:
    vint = [-v for v in vint]
vstar = [Fr(v) for v in vint]
CHK("A_vstar_integral_primitive",
    all(v.denominator == 1 for v in vstar)
    and math.gcd(*[abs(int(v)) for v in vstar if v]) == 1)
CHK("A_vstar_in_flip_span",
    all(vstar[b] == 0 for b in range(27) if D2[b] == 1),
    "supported entirely on the 11 D2-flipped coordinates")
CHK("A_vstar_D2_eigenvector_minus1",
    all(D2[b] * vstar[b] == -vstar[b] for b in range(27)))
SUP = [b for b in range(27) if vstar[b] != 0]
REC("A_vstar_27vector_exact", [str(int(v)) for v in vstar],
    "integer primitive, first nonzero entry positive")
REC("A_vstar_support", SUP, f"support size {len(SUP)} of 27")
REC("A_vstar_support_weights", {str(b): list(WT[b]) for b in SUP})
# the affine flip character on the support: a* = s(chi-)
a_star = tuple(1 if CHI_M[i] == -1 else 0 for i in range(6))
CHK("A_a_star_is_101011", a_star == (1, 0, 1, 0, 1, 1))
CHK("A_support_weights_even_under_a_star",
    all(sum(a_star[i] * WT[b][i] for i in range(6)) % 2 == 0 for b in SUP),
    "D2 = -(-1)^<a*,w>: flipped coords = a*-EVEN weights (B928)")
REC("A_vstar_pi_action",
    {str(b): int(piW[b]) for b in SUP},
    "the pairing pi restricted to the support")
CHK("A_vstar_pi_symmetric_support",
    sorted(piW[b] for b in SUP) == SUP)
PI_FIXED = [b for b in range(27) if piW[b] == b]
REC("A_pi_fixed_points", PI_FIXED,
    "the self-paired coordinates (w = -flip(w)) of the whole 27")
CHK("A_vstar_IS_the_pi_fixed_locus_indicator",
    SUP == PI_FIXED and all(vstar[b] == 1 for b in SUP),
    "v* = e9 + e13 + e15 = THE 0/1 INDICATOR OF THE FULL FIXED LOCUS OF "
    "THE WEIGHT PAIRING pi (w = -flip(w)): a basis-level object, defined "
    "with no reference to W3 or the twist at all")
CHK("A_support_weights_sum_to_zero_weight",
    all(sum(WT[b][i] for b in SUP) == 0 for i in range(6)),
    "the three self-paired weights sum to the zero weight")
CHK("A_pi_fixed_coords_carry_H_entry_minus1",
    all(cbP[b] == -1 for b in PI_FIXED),
    "each self-paired coordinate has H+ entry -1 (=> h(v*,v*) = -3)")
# the H-norms of the line (signs threaded, nothing assumed definite)
hvv = Fr(0)
for b in SUP:
    hvv += vstar[piW[b]] * Fr(cbP[b]) * vstar[b]
CHK("A_hvv_nonzero", hvv != 0)
hvv_num_f = {str(p): e for p, e in factorint(hvv.numerator).items()}
hvv_den_f = {str(p): e for p, e in factorint(hvv.denominator).items()}
REC("A_hplus_norm_exact", str(hvv),
    f"num factors {hvv_num_f}, den factors {hvv_den_f}; SIGN = "
    f"{'+' if hvv > 0 else '-'}")
hvv_tw = Fr(0)
for b in SUP:
    hvv_tw += vstar[piW[b]] * Fr(cbP[b] * D2[b]) * vstar[b]
CHK("A_hprime_norm_is_minus_hplus_norm", hvv_tw == -hvv,
    "v* lives in the flip span, so H' = H+ D2 negates its norm")
# charge moments (equivariance: eps=+1 charges are FORCED isotropic)
mom = {}
for n in ns:
    img = [sum(Rex[n][i][j] * vstar[j] for j in range(27) if vstar[j])
           for i in range(27)]
    inW3 = qsolve_span(W3, img)
    CHK(f"A_R{n}_vstar_stays_in_W3", inW3 is not None)
    hm = Fr(0)
    for b in range(27):
        if vstar[piW[b]] and img[b]:
            hm += vstar[piW[b]] * Fr(cbP[b]) * img[b]
    mom[n] = hm
    # eigenvector test (data, not gate): proportional to vstar?
    prop = None
    for b in SUP:
        if img[b]:
            prop = Fr(img[b], vstar[b])
            break
    is_eig = prop is not None and all(img[b] == prop * vstar[b]
                                      for b in range(27))
    REC(f"A_R{n}_moment_and_eigtest",
        {"h(v*, R v*)": str(hm), "eigenvector": bool(is_eig)},
        f"eps_{n} = {EPSPAT[n]}")
CHK("A_odd_charge_moments_forced_zero", mom[14] == 0 and mom[22] == 0,
    "eps=+1 equivariance makes h(v, R v) antisymmetric -> 0 (verified)")
REC("A_even_charge_moments",
    {"R8": str(mom[8]), "R16": str(mom[16]),
     "R8_over_hvv": str(mom[8] / hvv), "R16_over_hvv": str(mom[16] / hvv)},
    "the unity line's mean even charges (h-relative)")

# THE BRANCH EXPANSION: v* = Tr_{K/Q}(kappa . vS), kappa in K, exact solve
BAS = [KONE, (Fr(0), Fr(1), Fr(0)), (Fr(0), Fr(0), Fr(1))]
Arows = []
brows = []
for i in range(27):
    Arows.append([ktrace(kmul(BAS[j], vS27[i])) for j in range(3)])
    brows.append(vstar[i])
piv_r = []
rr = 0
Aug = [Arows[i] + [brows[i]] for i in range(27)]
for c in range(3):
    pr = next((r for r in range(rr, 27) if Aug[r][c] != 0), None)
    CHK(f"A_trace_system_pivot_{c}", pr is not None)
    Aug[rr], Aug[pr] = Aug[pr], Aug[rr]
    iv = Aug[rr][c]
    Aug[rr] = [e / iv for e in Aug[rr]]
    for r in range(27):
        if r != rr and Aug[r][c]:
            f = Aug[r][c]
            Aug[r] = [Aug[r][j] - f * Aug[rr][j] for j in range(4)]
    piv_r.append(c)
    rr += 1
kappa = (Aug[0][3], Aug[1][3], Aug[2][3])
CHK("A_kappa_solves_all_27_components",
    all(ktrace(kmul(kappa, vS27[i])) == vstar[i] for i in range(27)),
    "v*_i = Tr_{K/Q}(kappa . vS_i) exactly, all 27 coordinates")
REC("A_kappa_K_coords", [str(c) for c in kappa],
    "basis (1, rho, rho^2); gauge = the banked primitive vS27")
mp_kappa = kminpoly(kappa)
REC("A_kappa_minpoly", mp_kappa)
CHK("A_kappa_not_rational_NOT_the_vacuum_sum", len(mp_kappa) == 4,
    "deg 3: v* is NOT the naive vacuum-sum Tr(vS) in the banked gauge "
    "(kappa in Q would force qS in Q -- impossible)")
# consistency: h(S_g, v*) = sigma_g(kappa qS) -- i.e. hsv = kappa*qS in K
hsv = KZERO
for b in range(27):
    a2 = piW[b]
    if kis0(vS27[a2]) or vstar[b] == 0:
        continue
    hsv = kadd(hsv, kscale(vS27[a2], Fr(cbP[b]) * vstar[b]))
CHK("A_hsv_equals_kappa_qS", kis0(ksub(hsv, kmul(kappa, qS))),
    "h(S, v*) = kappa . h(S, S): the expansion is h-consistent "
    "(branch orthogonality)")
# THE EQUAL-ANGLE THEOREM: 3 kappa^2 qS = hvv in Q  (cos^2 = 1/3, exact)
k2q = kmul(kmul(kappa, kappa), qS)
CHK("A_EQUAL_ANGLE_3_kappa2_qS_equals_hvv_RATIONAL",
    k2q[1] == 0 and k2q[2] == 0 and 3 * k2q[0] == hvv,
    "sigma_g(kappa^2 qS) = hvv/3 for ALL g: cos^2(v*, S_g) = 1/3 exactly, "
    "every branch -- the unity line is the |h|-metric DIAGONAL of the "
    "vacuum frame (B930's banked 1/3 column, now a K-identity)")
CHK("A_equivalent_form_3_hsv2_equals_qS_hvv",
    kis0(ksub(kscale(kmul(hsv, hsv), Fr(3)), kscale(qS, hvv))))
Nk = knorm(kappa)
REC("A_kappa_norm_and_hvv_relation",
    {"N(kappa)": str(Nk), "N(kappa)^2*N(qS)": str(Nk * Nk * knorm(qS)),
     "(hvv/3)^3": str((hvv / 3) ** 3)},
    "N(kappa)^2 N(qS) = (hvv/3)^3 -- the norm shadow of the theorem")
CHK("A_norm_shadow_identity", Nk * Nk * knorm(qS) == (hvv / 3) ** 3)
# numeric belt + sign pattern (dps 80; ascending-rho branch order)
mp.dps = 80
rts = sorted(_mu_roots_numeric(300))
mp.dps = 80
qs_signs = [1 if knum(qS, r) > 0 else -1 for r in rts]
REC("A_qS_branch_signs_ascending_rho", qs_signs,
    "all -1 = the register uniformly negative (B930), sign-threaded")
cos_belt = mp.mpf(0)
sgn_pat = []
for r in rts:
    hg = knum(hsv, r)
    qg = knum(qS, r)
    c2 = hg * hg / (abs(qg) * abs(mp.mpf(hvv.numerator) / hvv.denominator))
    cos_belt = max(cos_belt, abs(c2 - mp.mpf(1) / 3))
    sgn_pat.append(1 if hg > 0 else -1)
CHK("A_cos2_belt_one_third", cos_belt < mp.mpf(10) ** (-70),
    f"worst |cos^2 - 1/3| = {mp.nstr(cos_belt, 3)}")
REC("A_normalized_sign_pattern_ascending_rho", sgn_pat,
    "signs of h(S_g, v*) in the banked vS/v* gauge; the banked B930 R "
    "unity column pattern (-,-,+) up to the global gauge sign")
# stabilizer under the S3 branch (cocycle) action, three levels
kap_conj = [knum(kappa, r) for r in rts]
CHK("A_kappa_conjugates_distinct",
    min(abs(kap_conj[i] - kap_conj[j]) for i in range(3) for j in range(3)
        if i < j) > mp.mpf(10) ** (-40),
    "deg-3 kappa: the labeled coefficient triple has TRIVIAL stabilizer")
tp = tuple(sgn_pat)
stab2 = [p for p in itertools.permutations(range(3))
         if tuple(tp[p[i]] for i in range(3)) == tp]
REC("A_stabilizer_three_levels",
    {"labeled_tuple_sigma_g_kappa": "trivial (conjugates distinct, deg 3)",
     "signed_normalized_pattern": f"order {len(stab2)} "
     f"(perms {stab2})",
     "unsigned_metric_configuration": "FULL S3 (cos^2 = 1/3 to every "
     "branch: the equal-angle diagonal)"},
    "the banked S3 cocycle acts by permuting the three vacuum branches")
# the Klein character of the unity line (uses the [1] diagonals)
CHK("A_vstar_Klein_character_D_plus_D2_minus_D2D_minus",
    all(Dw[b] * vstar[b] == vstar[b] for b in range(27))
    and all((D2[b] * Dw[b]) * vstar[b] == -vstar[b] for b in range(27)),
    "D v* = +v*, D2 v* = D2D v* = -v*: the unity line transforms by the "
    "Klein character with kernel {1, D} -- odd under BOTH wall characters "
    "chi+-, even under their inner ratio sigma_-1")
RES["part_A"] = {
    "vstar_27vector": [str(int(v)) for v in vstar],
    "support": SUP,
    "support_weights": {str(b): list(WT[b]) for b in SUP},
    "hplus_norm": str(hvv),
    "hplus_norm_factors": {"num": hvv_num_f, "den": hvv_den_f,
                           "sign": "+" if hvv > 0 else "-"},
    "charge_moments": {str(n): str(mom[n]) for n in ns},
    "kappa": [str(c) for c in kappa],
    "kappa_minpoly": mp_kappa,
    "equal_angle_theorem": "3*kappa^2*qS = h(v*,v*) in Q (cos^2 = 1/3 to "
                           "every vacuum branch, exact K-identity)",
    "sign_pattern_ascending_rho": sgn_pat,
    "W3_basis_rows": [[str(v) for v in w] for w in W3],
    "vstar_in_W3_basis": [str(c) for c in ker1[0]],
}
dump()

# ================================================================ [5] PART B
log("[5] PART B: flip-mass level tables for the WHOLE Klein 2-torsion ...")
LEVELS = [(Fr(-1), "-1"), (Fr(0), "0"), (Fr(1, 2), "1/2"), (Fr(1), "+1"),
          (Fr(2), "+2")]
# banked B931 ADDENDUM gate numbers (numerators over 2^19 3^4) for T = D2
GATE_D2 = {
    "S": {"0": 20417473, "1/2": 953 ** 2, "+1": 5 ** 3 * 11 * 257,
          "-1": -(5 ** 2) * (7 ** 2) * 199 * 991},
    "A": {"0": 29 * 72869, "1/2": 953 ** 2, "+1": 11 * 373837,
          "-1": -(7 ** 2) * 11 * 107 * 2089},
}
DEN_GATE = 2 ** 19 * 3 ** 4


def kdet_of(kx):
    return knorm(kx)


def fac_signed(q):
    """factor a nonzero rational: sign, num factors, den factors."""
    sgn = "-" if q < 0 else "+"
    nf = {str(p): e for p, e in factorint(abs(q.numerator)).items()}
    df = {str(p): e for p, e in factorint(q.denominator).items()}
    return {"value": str(q), "sign": sgn, "num_factors": nf,
            "den_factors": df}


mp.dps = 120
rts_belt = sorted(_mu_roots_numeric(400))
mp.dps = 120
PARTB = {}
val711 = {}
for nm, T in TWISTS:
    Fs = [b for b in range(27) if T[b] == -1]
    fm = {}
    # S family
    mS_T = kmul(kq(vS27, cbP, Fs), qSi)
    # A family (cross term must vanish -- Hermitianness of the restriction)
    evT, crT = kq_A(cbP, Fs)
    CHK(f"B_{nm}_A_cross_term_zero", kis0(crT),
        "m_{A+} = m_{A-} for this twist (pi-symmetric restriction)")
    mA_T = kmul(evT, qAi)
    fam = {"S": mS_T, "A": mA_T}
    # register trace split (the sum-rule rider)
    trs = []
    for W, Gi in ((W3, G3i), (W6, G6i), (W18, G18i)):
        Hf = gramQ(W, cbP, Fs)
        k = len(W)
        trs.append(sum(Gi[i][t] * Hf[t][i] for i in range(k)
                       for t in range(k)))
    CHK(f"B_{nm}_register_trace_sum_equals_flip_rank",
        sum(trs) == len(Fs),
        f"trW3 = {trs[0]}, trW6 = {trs[1]}, trW18 = {trs[2]}, "
        f"sum = {len(Fs)}")
    cpS = kcharpoly3(mS_T)
    CHK(f"B_{nm}_trW3_equals_TrK_mS", trs[0] == -sp.Rational(cpS[1]))
    cpA = kcharpoly3(mA_T)
    CHK(f"B_{nm}_trW6_equals_2TrK_mA", trs[1] == -2 * sp.Rational(cpA[1]))
    entry = {"flip_count": len(Fs),
             "register_traces": [str(t) for t in trs]}
    for famnm, mel in fam.items():
        tbl = {}
        for lv, lvnm in LEVELS:
            xi = ksub(mel, (lv, Fr(0), Fr(0)))
            Nv = knorm(xi)
            # numeric belt: product over embeddings
            prod = mp.mpf(1)
            for r in rts_belt:
                prod *= (knum(mel, r) - mp.mpf(lv.numerator) / lv.denominator)
            Nnum = mp.mpf(Nv.numerator) / Nv.denominator
            CHK(f"B_{nm}_{famnm}_level_{lvnm.replace('/', '_')}_belt",
                abs(prod - Nnum) <= mp.mpf(10) ** (-60) * max(1, abs(Nnum)),
                f"N(m - {lvnm}) = {Nv}")
            tbl[lvnm] = fac_signed(Nv) if Nv != 0 else {"value": "0"}
            val711[(nm, famnm, lvnm)] = (
                0 if Nv == 0 else factorint(abs(Nv.numerator)).get(7, 0),
                0 if Nv == 0 else factorint(abs(Nv.numerator)).get(11, 0),
                0 if Nv == 0 else factorint(abs(Nv.numerator)).get(953, 0))
        entry[famnm] = {
            "m_K_coords": [str(c) for c in mel],
            "m_minpoly": kminpoly(mel),
            "level_norms": tbl,
        }
    PARTB[nm] = entry
    dump()

# the D2 gate against the banked B931 ADDENDUM table.
# DESIGN AMENDMENT (logged, post-hoc to the first run's honest abort): the
# first gate compared SIGNED values and failed -- all seven magnitudes match
# the addendum exactly, but the addendum's sign column follows N(level - m)
# while this cell's declared convention is N(m - level) = -N(level - m).
# The signs here are FORCED (both families' branches lie in (0,1), so
# N(m-1) < 0 and N(m+1) > 0 necessarily); the addendum's table was computed
# inline in a listening session and is not in why953.py, so its convention
# cannot be re-run -- the magnitudes are the banked content.  Gate:
# magnitudes exact; the forced-sign check is separate and unconditional.
RES["notes"].append(
    "gate amendment: B931-ADDENDUM comparison is on |N| (the addendum's "
    "sign column follows N(level-m); this cell's convention N(m-level) has "
    "FORCED signs since all m-branches lie in (0,1))")
for famnm in ("S", "A"):
    for lvnm, gate in GATE_D2[famnm].items():
        got = PARTB["D2"][famnm]["level_norms"][lvnm]["value"]
        CHK(f"B_gate_B931_addendum_D2_{famnm}_{lvnm.replace('/', '_')}_abs",
            abs(Fr(got)) == Fr(abs(gate), DEN_GATE),
            f"|N(m - {lvnm})| = {abs(gate)}/2^19 3^4 (banked level song)")
mp.dps = 80
rts80 = sorted(_mu_roots_numeric(300))
mp.dps = 80
CHK("B_D2_branches_in_unit_interval_signs_forced",
    all(0 < knum(kel, r) < 1 for r in rts80
        for kel in ((Fr(52571, 64896), Fr(-55825, 2197),
                     Fr(27165600, 28561)),
                    (Fr(7291, 32448), Fr(31955, 2197),
                     Fr(461815200, 28561)))),
    "every D2 colorless flip-mass branch is in (0,1): N(m-1) < 0 and "
    "N(m+1) > 0 are forced -- the sign difference vs the addendum is "
    "notational, not arithmetic")

# THE COSET STRUCTURE (exact): D is colorless-TRIVIAL; D2D = D2 colorless
CHK("B_D_acts_as_identity_on_W3_and_W6",
    all(w[b] == 0 for w in W3 + W6 for b in range(27) if Dw[b] == -1),
    "every W3/W6 basis vector vanishes on D's flip set: the wall twist "
    "fixes the colorless register POINTWISE; its 12 flips are all colored")
mS_D = kmul(kq(vS27, cbP, [b for b in range(27) if Dw[b] == -1]), qSi)
evD, _crD = kq_A(cbP, [b for b in range(27) if Dw[b] == -1])
CHK("B_D_flip_masses_exactly_zero",
    kis0(mS_D) and kis0(evD),
    "m_D,S = m_D,A = 0 exactly: the orientation twist never touches the "
    "colorless lines")
FS_D2D = [b for b in range(27) if DD[b] == -1]
mS_D2D = kmul(kq(vS27, cbP, FS_D2D), qSi)
evDD, _crDD = kq_A(cbP, FS_D2D)
mA_D2D = kmul(evDD, qAi)
CHK("B_D2D_colorless_masses_EQUAL_D2_exactly",
    kis0(ksub(mS_D2D, m_S)) and kis0(ksub(mA_D2D, m_A)),
    "m_{D2D} = m_{D2} on BOTH colorless families as exact K-elements: "
    "the colorless flip arithmetic factors through the quotient "
    "Klein/{1,D}")

# ================================================================ [6] verdict
log("[6] the 7/11 verdict ...")
summary = {}
for nm, _T in TWISTS:
    for famnm in ("S", "A"):
        summary[f"{nm}_{famnm}"] = {
            lvnm: {"v7": val711[(nm, famnm, lvnm)][0],
                   "v11": val711[(nm, famnm, lvnm)][1],
                   "v953": val711[(nm, famnm, lvnm)][2]}
            for _lv, lvnm in LEVELS}
RES["seven_eleven_953_valuations"] = summary
# the banked D2 pattern: 11 at +1 (no 7), 7^2 at -1, both families
d2_pat = (val711[("D2", "S", "+1")][:2], val711[("D2", "S", "-1")][:2],
          val711[("D2", "A", "+1")][:2], val711[("D2", "A", "-1")][:2])
CHK("V_D2_pattern_11_at_plus1_7sq_at_minus1",
    d2_pat[0][0] == 0 and d2_pat[0][1] >= 1
    and d2_pat[1][0] == 2
    and d2_pat[2][0] == 0 and d2_pat[2][1] >= 1
    and d2_pat[3][0] == 2,
    "re-verified from scratch: 7-free with 11 at +1; 7^2 at -1, both fams")


def pat(nm):
    return {famnm: {"+1": (val711[(nm, famnm, "+1")][0],
                           val711[(nm, famnm, "+1")][1]),
                    "-1": (val711[(nm, famnm, "-1")][0],
                           val711[(nm, famnm, "-1")][1])}
            for famnm in ("S", "A")}


# the swap question is decided by exact identities, not by valuation
# pattern-matching: m_D = 0 (D colorless-trivial) and m_{D2D} = m_{D2}
# exactly (checked above), so the 7/11 split can neither swap nor change.
swap = all(val711[(nm, famnm, "-1")][1] >= 1
           and val711[(nm, famnm, "-1")][0] == 0
           and val711[(nm, famnm, "+1")][0] == 2
           for nm in ("D", "D2D") for famnm in ("S", "A"))
ident_D2D = all(
    PARTB["D2D"][famnm]["level_norms"][lvnm]["value"]
    == PARTB["D2"][famnm]["level_norms"][lvnm]["value"]
    for famnm in ("S", "A") for _lv, lvnm in LEVELS)
degen_D = all(
    PARTB["D"][famnm]["level_norms"]["0"]["value"] == "0"
    for famnm in ("S", "A"))
RES["verdict_7_11"] = {
    "D2": pat("D2"), "D": pat("D"), "D2D": pat("D2D"),
    "swap_11_to_minus1_7sq_to_plus1": bool(swap),
    "D2D_level_tables_identical_to_D2": bool(ident_D2D),
    "D_colorless_degenerate_m_equals_0": bool(degen_D),
}
CHK("V_no_swap_D2D_identical_D_degenerate",
    (not swap) and ident_D2D and degen_D,
    "the exact coset identities decide the question")
RES["verdict"] = (
    "NO SWAP -- COSET INVARIANT: the colorless flip arithmetic (and with "
    "it the 7/11 unit-level split and the 953 half-flip locus) is "
    "invariant under the full 2-torsion MODULO the wall twist D.  D acts "
    "as the identity on the colorless register (m_S = m_A = 0 exactly; "
    "its 12 flips are entirely colored), so the orientation-reversed "
    "member D2D = D2*D carries the level song of D2 UNCHANGED, and D "
    "alone is level-degenerate (N(m-l) = -l^3, no primes).  The "
    "resolvent's 7/11 factorization does NOT track the Klein element: "
    "it is a D2-COSET datum, and orientation reversal moves only colored "
    "weight (tr W18: 6 -> 10, flip rank 11 -> 15).")
log("VERDICT:", RES["verdict"])
RES["conventions"] = {
    "twist_signs": "each Klein diagonal normalized to entry0 = +1; this is "
                   "the convention of BOTH banked diagonals (B916 D2, B912 "
                   "D); the -T tables are derivable: level l of -T = "
                   "-(level 1-l of T), which the level set {-1,0,1/2,1,2} "
                   "covers for the unit levels",
    "branch_order": "ascending-rho (the banked B928/B930 convention)",
    "vstar_gauge": "integer primitive, first nonzero entry positive",
    "levels": "N_{K/Q}(m - l) as exact rationals, factored",
}
RES["runtime_s"] = round(time.time() - T00, 1)
dump()
log("results.json written; done")
