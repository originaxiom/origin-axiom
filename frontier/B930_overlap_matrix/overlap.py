#!/usr/bin/env python3
"""B930 -- THE OVERLAP MATRIX (the map hunt; blind -- no measured number).

B929's lesson: mixing is the overlap between TWO bases; B929 compared ONE
frame's masses.  This cell identifies the object's natural BASE-PAIRS and
computes the exact 3x3 overlap matrices between them, H-relative, per
generation index:

 (a) the two colored triples (the two global omega-branches; B912 atom
     triples [1,5,10] vs [2,6,11] -- the two ccc transversals);
 (b) the S-register frame vs the A-frame on the colorless nine;
 (c) the D2-flip eigenbasis vs the generation-frame basis (the twist frame
     against the Galois frame): the flip projector Pi_F = (1-D2)/2
     compressed to the rational register blocks W3/W6/W18 (rational
     charpolys = exact principal spectra) and the 3x3 rotation R between
     the S-frame and the flip-principal frame of W3.

Every pair is computed under BOTH Hermitian instruments: the canonical
charge-equivariant H+ (B912) and the tau-twisted H' = H+ D2 (B916) -- B923
proved the entire generation hierarchy is carried by D2, so the twist gauge
is where a nontrivial overlap can live.  Selection-rule predictions
(verified exactly here): under H+ the (a)/(b) overlaps are FORCED zero by
charge orthogonality; only H' can mix.

HOUSE RULES: exact arithmetic for every verdict-bearing claim (tower
K = Q[rho]/mu13 -> N (splitting, deg 6) -> Mbar = N(tau), tau^2 = -3;
colored over K(omega), omega^2 = -231, omega = S77*tau with S77 in N);
verify-don't-trust (H+ re-verified from symmetry + exact charge
equivariance; D2 RE-DERIVED from the banked B928 characterization
D2 = +-rho_27(sigma_chi-) by pure rep propagation, then compared to the
banked B916 diagonal); e6_centralizer.py exec'd in an isolated namespace
with chdir to scratch and __file__ set; NO Rayleigh-quotient eigenreads
(componentwise readouts with residual certificates on the numeric belt);
structural verdicts only -- NO measured value is contacted or compared.

Output: results.json (exact data + checks).
"""
import io
import os
import json
import math
import time
import pickle
import random
import tempfile
import contextlib
import itertools
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b930_")
os.makedirs(SCRATCH, exist_ok=True)
T00 = time.time()
RES = {"cell": "B930 overlap matrix", "checks": {}, "notes": []}


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
log("[0] banked inputs: rep27, B912 H+, B916 D2, B907 walls; own re-derivations")
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
piW_banked = list(B912["H_plus_support_pi"])
cbP = [int(x) for x in B912["H_plus_entries_c_b"]]
B916 = json.load(open(os.path.join(REPO, "frontier", "B916_lambda_bridge",
                                   "results.json")))
D2_banked = [int(x) for x in B916["H_prime_diag_vs_H_plus"]["D2"]]
MINPOLY_S_banked = [int(c) for c in B916["d_ratio_minpolys_desc"]["S0"]]
MINPOLY_A_banked = [int(c) for c in B916["d_ratio_minpolys_desc"]["A0p"]]
B907V = json.load(open(os.path.join(REPO, "frontier",
                                    "B907_real_form_selector", "verdict.json")))
CHI_P = tuple(int(x) for x in B907V[0]["signs"])
CHI_M = tuple(int(x) for x in B907V[1]["signs"])
CHK("banked_wall_pair_is_a_global_negation",
    CHI_M == tuple(-x for x in CHI_P), f"chi+ = {CHI_P}")
B928R = json.load(open(os.path.join(REPO, "frontier", "B928_d2_decode",
                                    "results.json")))
B923R = json.load(open(os.path.join(REPO, "frontier", "B923_exactification",
                                    "results.json")))

FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}


def flipw(w):
    return tuple(w[FLIP[i]] for i in range(6))


negflip = {tuple(-x for x in flipw(WT[b])): b for b in range(27)}
piW = [negflip[WT[b]] for b in range(27)]
CHK("weight_pairing_pi_recomputed_and_involutive",
    sorted(piW) == list(range(27)) and all(piW[piW[b]] == b for b in range(27))
    and piW == piW_banked)
CHK("H_plus_symmetric", all(cbP[piW[b]] == cbP[b] for b in range(27)),
    "c_{pi(b)} = c_b => the banked H+ matrix is symmetric")

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
    propagation -- re-derives D2 from the B928 characterization."""
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

# H+ charge equivariance Rn^T H + eps_n H Rn = 0 (the property the selection
# rules use; B914's banked certificate, recomputed here)
# exact: (Rn^T H)[a][b] = sum_t Rn[t][a] H[t][b] = Rn[pi(b)][a] c_b
#        (H Rn)[a][b]  = sum_t H[a][t] Rn[t][b] = c_{pi(a)} Rn[pi(a)][b]
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
    "Rn^T H+ = -eps_n H+ Rn, eps = (-1,+1,-1,+1) -- the selection-rule input")

# D2 re-derived from the banked characterization (B928): D2 = rho27(sigma_chi-)
T_chim = rep_diagonal_of_inner(CHI_M)
CHK("D2_rederived_as_rep_diagonal_of_sigma_chi_minus",
    T_chim is not None, "pure rep propagation, no handoff")
D2 = T_chim if T_chim[0] == 1 else [-x for x in T_chim]
CHK("D2_equals_banked_B916_diagonal", D2 == D2_banked)
flip_ind = [b for b in range(27) if D2[b] == -1]
unflip = [b for b in range(27) if D2[b] == 1]
CHK("D2_11_flips_pi_symmetric", len(flip_ind) == 11
    and all(D2[piW[b]] == D2[b] for b in range(27)))
cbT = [cbP[b] * D2[b] for b in range(27)]   # H' = H+ D2 entries
dump()

# ================================================================ [2] fields
log("[2] the exact tower K -> N -> Mbar and K(omega) ...")
MU = [500716339200, -2075673600, -4769856, 2197]
A_, B_, C_, D_ = MU
R3K = [Fr(-D_, A_), Fr(-C_, A_), Fr(-B_, A_)]
R4K = [R3K[2] * R3K[0], R3K[0] + R3K[2] * R3K[1], R3K[1] + R3K[2] * R3K[2]]
KZERO = (Fr(0), Fr(0), Fr(0))
KONE = (Fr(1), Fr(0), Fr(0))


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


b_mu = Fr(MU[1], MU[0])
c_mu = Fr(MU[2], MU[0])
P_N = (b_mu, Fr(1), Fr(0))
Q_N = (c_mu, b_mu, Fr(1))
NZERO = (KZERO, KZERO)
NONE_ = (KONE, KZERO)


def nmul(a, b):
    a0, a1 = a
    b0, b1 = b
    x00 = kmul(a0, b0)
    x11 = kmul(a1, b1)
    x01 = kadd(kmul(a0, b1), kmul(a1, b0))
    return (ksub(x00, kmul(x11, Q_N)), ksub(x01, kmul(x11, P_N)))


def nadd(a, b):
    return (kadd(a[0], b[0]), kadd(a[1], b[1]))


def nsub(a, b):
    return (ksub(a[0], b[0]), ksub(a[1], b[1]))


def nscale(a, s):
    return (kscale(a[0], s), kscale(a[1], s))


def nis0(a):
    return kis0(a[0]) and kis0(a[1])


def ninv(a):
    x, y = a
    det = kadd(ksub(kmul(x, x), kmul(kmul(P_N, x), y)), kmul(Q_N, kmul(y, y)))
    di = kinv(det)
    return (kmul(ksub(x, kmul(P_N, y)), di), kscale(kmul(y, di), Fr(-1)))


def nfromK(x):
    return ((x[0], x[1], x[2]), KZERO)


def sigma(j, x):
    c0, c1, c2 = x
    if j == 0:
        return ((c0, c1, c2), KZERO)
    if j == 1:
        return (ksub((c0, Fr(0), Fr(0)), kscale(Q_N, c2)),
                ksub((c1, Fr(0), Fr(0)), kscale(P_N, c2)))
    R3N = ((-b_mu, Fr(-1), Fr(0)), (Fr(-1), Fr(0), Fr(0)))
    acc = ((Fr(c0), Fr(0), Fr(0)), KZERO)
    acc = nadd(acc, nscale(R3N, c1))
    acc = nadd(acc, nscale(nmul(R3N, R3N), c2))
    return acc


# Mbar = N(tau), tau^2 = -3: elements (X, Y) = X + Y tau, X, Y in N
TZERO = (NZERO, NZERO)
TONE = (NONE_, NZERO)


def tmul(a, b):
    return (nsub(nmul(a[0], b[0]), nscale(nmul(a[1], b[1]), Fr(3))),
            nadd(nmul(a[0], b[1]), nmul(a[1], b[0])))


def tadd(a, b):
    return (nadd(a[0], b[0]), nadd(a[1], b[1]))


def tsub(a, b):
    return (nsub(a[0], b[0]), nsub(a[1], b[1]))


def tscale(a, s):
    return (nscale(a[0], s), nscale(a[1], s))


def tis0(a):
    return nis0(a[0]) and nis0(a[1])


def tconj(a):
    return (a[0], nscale(a[1], Fr(-1)))


def tinv(a):
    nrm = nadd(nmul(a[0], a[0]), nscale(nmul(a[1], a[1]), Fr(3)))
    ni = ninv(nrm)
    return (nmul(a[0], ni), nscale(nmul(a[1], ni), Fr(-1)))


# K(omega), omega^2 = -231: elements (x, y) = x + y omega, x, y in K
FTZERO = (KZERO, KZERO)
FTONE = (KONE, KZERO)


def ftmul(a, b):
    return (ksub(kmul(a[0], b[0]), kscale(kmul(a[1], b[1]), Fr(231))),
            kadd(kmul(a[0], b[1]), kmul(a[1], b[0])))


def ftadd(a, b):
    return (kadd(a[0], b[0]), kadd(a[1], b[1]))


def ftsub(a, b):
    return (ksub(a[0], b[0]), ksub(a[1], b[1]))


def ftscale(a, s):
    return (kscale(a[0], s), kscale(a[1], s))


def ftscaleK(a, kx):
    return (kmul(a[0], kx), kmul(a[1], kx))


def ftis0(a):
    return kis0(a[0]) and kis0(a[1])


def ftconj(a):
    return (a[0], kscale(a[1], Fr(-1)))


def ftinv(a):
    nrm = kadd(kmul(a[0], a[0]), kscale(kmul(a[1], a[1]), Fr(231)))
    ni = kinv(nrm)
    return (kmul(a[0], ni), kscale(kmul(a[1], ni), Fr(-1)))


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
import sympy.ntheory as nt
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
        acc = (Fr(sp.Rational(h_coeffs[0]).p, sp.Rational(h_coeffs[0]).q),
               Fr(0), Fr(0))
        for c in h_coeffs[1:]:
            acc = kmul(acc, cand)
            acc = (acc[0] + Fr(sp.Rational(c).p, sp.Rational(c).q),
                   acc[1], acc[2])
        if kis0(acc):
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
    cols = [kmul(kx, KONE), kmul(kx, (Fr(0), Fr(1), Fr(0))),
            kmul(kx, (Fr(0), Fr(0), Fr(1)))]
    Mv = [[cols[j][i] for j in range(3)] for i in range(3)]
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


def keval_poly(coeffs, kx):
    acc = (Fr(sp.Rational(coeffs[0]).p, sp.Rational(coeffs[0]).q),
           Fr(0), Fr(0))
    for c in coeffs[1:]:
        acc = kmul(acc, kx)
        acc = (acc[0] + Fr(sp.Rational(c).p, sp.Rational(c).q),
               acc[1], acc[2])
    return acc


def kminpoly(kx):
    """primitive integer minpoly of a K-element (deg 1 or 3)."""
    cp = kcharpoly3(kx)
    x = sp.Symbol("x")
    poly = sp.Poly([sp.Rational(c) for c in cp], x)
    for f, _m in sorted(sp.factor_list(poly.as_expr())[1],
                        key=lambda t: sp.degree(t[0], x)):
        fc = sp.Poly(f, x).all_coeffs()
        if kis0(keval_poly([sp.Rational(c) for c in fc], kx)):
            return int_primitive(fc)
    return int_primitive(cp)


def neval_poly(coeffs, xN):
    acc = nfromK((Fr(sp.Rational(coeffs[0]).p, sp.Rational(coeffs[0]).q),
                  Fr(0), Fr(0)))
    for c in coeffs[1:]:
        acc = nmul(acc, xN)
        acc = nadd(acc, nfromK((Fr(sp.Rational(c).p, sp.Rational(c).q),
                                Fr(0), Fr(0))))
    return acc


def nminpoly(xN):
    """primitive integer minpoly of an N-element (deg | 6) via the 6x6
    multiplication matrix in the basis (1,rho,rho^2) x (1,beta)."""
    basis = []
    for t in range(2):
        for p in range(3):
            kc = [Fr(0)] * 3
            kc[p] = Fr(1)
            basis.append((tuple(kc), KZERO) if t == 0
                         else (KZERO, tuple(kc)))
    cols = []
    for b in basis:
        y = nmul(xN, b)
        cols.append([y[0][0], y[0][1], y[0][2], y[1][0], y[1][1], y[1][2]])
    x = sp.Symbol("x")
    Msp = sp.Matrix(6, 6, lambda i, j: sp.Rational(cols[j][i].numerator,
                                                   cols[j][i].denominator))
    cp = sp.Poly(Msp.charpoly(x).as_expr(), x)
    for f, _m in sorted(sp.factor_list(cp.as_expr())[1],
                        key=lambda t: sp.degree(t[0], x)):
        fc = [sp.Rational(c) for c in sp.Poly(f, x).all_coeffs()]
        if nis0(neval_poly(fc, xN)):
            return int_primitive(fc)
    return int_primitive(cp.all_coeffs())


# ================================================================ [3] colorless
log("[3] the colorless nine, abstract over K (B914/B928 route, re-run) ...")
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
# completeness: W3 + W6 + W18 spans Q^27
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


def k_eigenvalue_of(Rn, vec):
    k0 = next(i for i in range(27) if not kis0(vec[i]))
    img = KZERO
    for j in range(27):
        if Rn[k0][j] and not kis0(vec[j]):
            img = kadd(img, kscale(vec[j], Rn[k0][j]))
    lam = kmul(img, kinv(vec[k0]))
    for i in range(27):
        acc = KZERO
        for j in range(27):
            if Rn[i][j] and not kis0(vec[j]):
                acc = kadd(acc, kscale(vec[j], Rn[i][j]))
        if not kis0(ksub(acc, kmul(lam, vec[i]))):
            return None
    return lam


c8vac = k_eigenvalue_of(Rex[8], vS27)
c8oct = k_eigenvalue_of(Rex[8], u27)
c16vac = k_eigenvalue_of(Rex[16], vS27)
c16oct = k_eigenvalue_of(Rex[16], u27)
CHK("S_and_A_exact_R8_R16_eigenvectors_over_K",
    None not in (c8vac, c8oct, c16vac, c16oct))
CHK("even_labels_irreducible_deg3",
    len(kminpoly(c8vac)) == 4 and len(kminpoly(c8oct)) == 4,
    "c8vac/c8oct have degree-3 minpolys => the three Galois branches are "
    "pairwise DISTINCT: the even-charge selection rule separates generations")

# abstract q, d, m (B928 [9] re-run -- the banked instrument re-derivation)
def kq(vec, cb):
    acc = KZERO
    for b in range(27):
        a = piW[b]
        if kis0(vec[a]) or kis0(vec[b]):
            continue
        acc = kadd(acc, kscale(kmul(vec[a], vec[b]), Fr(cb[b])))
    return acc


def kq_A(cb):
    even = KZERO
    cross = KZERO
    for b in range(27):
        a = piW[b]
        t1 = kmul(u27[a], u27[b])
        t2 = kmul(wodd27[a], wodd27[b])
        even = kadd(even, kscale(kadd(t1, kscale(t2, Fr(3))), Fr(cb[b])))
        c1 = kmul(u27[a], wodd27[b])
        c2 = kmul(wodd27[a], u27[b])
        cross = kadd(cross, kscale(ksub(c1, c2), Fr(cb[b])))
    return even, cross


qS = kq(vS27, cbP)
qS_tw = kq(vS27, cbT)
qA, crossA = kq_A(cbP)
qA_tw, crossA_tw = kq_A(cbT)
CHK("A_norms_tau_free_both_gauges", kis0(crossA) and kis0(crossA_tw))
CHK("q_nonzero_all", not (kis0(qS) or kis0(qS_tw) or kis0(qA)
                          or kis0(qA_tw)))
d_S = kmul(qS_tw, kinv(qS))
d_A = kmul(qA_tw, kinv(qA))
m_S = kscale(ksub(KONE, d_S), Fr(1, 2))
m_A = kscale(ksub(KONE, d_A), Fr(1, 2))
CHK("dS_dA_minpolys_equal_banked_B916",
    kminpoly(d_S) == MINPOLY_S_banked and kminpoly(d_A) == MINPOLY_A_banked)
CHK("m_S_minpoly_equals_banked_B928",
    kminpoly(m_S) == [int(c) for c in
                      B928R["Q2_colorless"]["minpoly_m_S"]])
dump()

# ================================================================ [4] colored
log("[4] the colored atoms over K(omega) (B923/B928 route, re-run) ...")
C18 = restrict(Mc, W18)
mp.dps = 400
hh = [mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q)
      for c in h_col_ints]
rts6 = mp.polyroots(hh, maxsteps=400, extraprec=400)
pairs = []
usedr = [False] * 6
for i in range(6):
    if usedr[i] or mp.im(rts6[i]) <= 0:
        continue
    for j in range(6):
        if j != i and not usedr[j] and abs(rts6[j] - mp.conj(rts6[i])) \
                < mp.mpf(10) ** (-150):
            pairs.append((rts6[i], rts6[j]))
            usedr[i] = usedr[j] = True
            break
CHK("h_col_roots_three_conjugate_pairs", len(pairs) == 3)
mu_roots = _mu_roots_numeric(400)
maxden = mp.mpf(10) ** 133
pK = qKq = None
for perm in itertools.permutations(range(3)):
    pv = [-2 * mp.re(pairs[perm[g]][0]) for g in range(3)]
    qv = [mp.re(pairs[perm[g]][0]) ** 2 + mp.im(pairs[perm[g]][0]) ** 2
          for g in range(3)]
    pc = _interp_K(pv, mu_roots, maxden, 10 ** 130)
    qc = _interp_K(qv, mu_roots, maxden, 10 ** 130)
    if pc is None or qc is None:
        continue
    lc = sp.Rational(h_col_ints[0])
    hmon = [sp.Rational(c) / lc for c in h_col_ints]
    prodN = [NONE_]
    for gg in range(3):
        qg = [sigma(gg, qc), sigma(gg, pc), sigma(gg, KONE)]
        new = [NZERO] * (len(prodN) + 2)
        for a2, ca in enumerate(prodN):
            for b2, cb_ in enumerate(qg):
                new[a2 + b2] = nadd(new[a2 + b2], nmul(ca, cb_))
        prodN = new
    okp = all(nis0(nsub(prodN[d],
                        (((Fr(hmon[6 - d].p, hmon[6 - d].q), Fr(0), Fr(0)),
                          KZERO)))) for d in range(7))
    if okp:
        pK, qKq = pc, qc
        break
CHK("h_col_is_K_norm_form_of_one_quadratic", pK is not None)
disc_c = ksub(kmul(pK, pK), kscale(qKq, Fr(4)))
w_c = sqrt_in_K(kscale(disc_c, Fr(-1, 231)))
CHK("colored_disc_minus_231_wc_squared", w_c is not None)
r1N = ((Fr(0), Fr(1), Fr(0)), KZERO)
r2N = (KZERO, KONE)
r3N = nsub(nsub(((Fr(-b_mu), Fr(0), Fr(0)), KZERO), r1N), r2N)
delta = nmul(nmul(nsub(r1N, r2N), nsub(r1N, r3N)), nsub(r2N, r3N))
dd2 = nmul(delta, delta)
CHK("delta_squared_rational", kis0(dd2[1]) and dd2[0][1] == 0
    and dd2[0][2] == 0)
t77 = sp.sqrt(sp.Rational(dd2[0][0].numerator, dd2[0][0].denominator) / 77)
CHK("disc_mu_77_times_square", t77.is_rational)
t77f = Fr(sp.Rational(t77).p, sp.Rational(t77).q)
S77 = nscale(delta, 1 / t77f)
CHK("S77_squared_77", nis0(nsub(nmul(S77, S77),
                                ((Fr(77), Fr(0), Fr(0)), KZERO))))
omega_M = (NZERO, S77)     # omega = S77 * tau in Mbar
CHK("omega_squared_minus_231_in_Mbar",
    tis0(tsub(tmul(omega_M, omega_M),
              (((Fr(-231), Fr(0), Fr(0)), KZERO), NZERO))))
_test = ((Fr(2), Fr(1), Fr(0)), (Fr(0), Fr(3), Fr(1))), \
    ((Fr(1), Fr(0), Fr(2)), (Fr(5), Fr(0), Fr(0)))
CHK("tinv_self_test", tis0(tsub(tmul(_test, tinv(_test)), TONE)))
theta_x = kscale(pK, Fr(-1, 2))
theta_y = kscale(w_c, Fr(1, 2))
Mft = [[((ksub((Fr(C18[i][j]), Fr(0), Fr(0)), theta_x),
          kscale(theta_y, Fr(-1))) if i == j else
         ((Fr(C18[i][j]), Fr(0), Fr(0)), KZERO)) for j in range(18)]
       for i in range(18)]
Aft = [row[:] for row in Mft]
piv = []
rr = 0
for c in range(18):
    pr = next((r for r in range(rr, 18) if not ftis0(Aft[r][c])), None)
    if pr is None:
        continue
    Aft[rr], Aft[pr] = Aft[pr], Aft[rr]
    iv = ftinv(Aft[rr][c])
    Aft[rr] = [ftmul(iv, e) for e in Aft[rr]]
    for r in range(18):
        if r != rr and not ftis0(Aft[r][c]):
            f = Aft[r][c]
            Aft[r] = [ftsub(Aft[r][j], ftmul(f, Aft[rr][j]))
                      for j in range(18)]
    piv.append(c)
    rr += 1
kerC = []
for fc in [c for c in range(18) if c not in piv]:
    v = [FTZERO] * 18
    v[fc] = FTONE
    for i, c in enumerate(piv):
        v[c] = ftsub(FTZERO, Aft[i][fc])
    kerC.append(v)
CHK("colored_eigenspace_dim_3_over_K_omega", len(kerC) == 3)


def ftlift(coords):
    out = []
    for i in range(27):
        ax, ay = KZERO, KZERO
        for a, cf in enumerate(coords):
            if W18[a][i]:
                ax = kadd(ax, kscale(cf[0], W18[a][i]))
                ay = kadd(ay, kscale(cf[1], W18[a][i]))
        out.append((ax, ay))
    return out


def ftnormalize27(vec):
    L = 1
    for (ax, ay) in vec:
        for kt in (ax, ay):
            for x2 in kt:
                if x2:
                    L = L * x2.denominator // math.gcd(L, x2.denominator)
    vec2 = [(kscale(ax, Fr(L)), kscale(ay, Fr(L))) for (ax, ay) in vec]
    G = 0
    for (ax, ay) in vec2:
        for kt in (ax, ay):
            for x2 in kt:
                G = math.gcd(G, abs(x2.numerator))
    if G > 1:
        vec2 = [(kscale(ax, Fr(1, G)), kscale(ay, Fr(1, G)))
                for (ax, ay) in vec2]
    return vec2


colB = [ftnormalize27(ftlift(v)) for v in kerC]

# the four charge labels on the colored atom, with their omega-parity
mu_lab = {}
okc = True
for n in ns:
    lab = None
    for a in range(3):
        u = colB[a]
        w = []
        for i in range(27):
            ax, ay = KZERO, KZERO
            for jj in range(27):
                if Rex[n][i][jj] and not ftis0(u[jj]):
                    ax = kadd(ax, kscale(u[jj][0], Rex[n][i][jj]))
                    ay = kadd(ay, kscale(u[jj][1], Rex[n][i][jj]))
            w.append((ax, ay))
        k0 = next(i for i in range(27) if not ftis0(u[i]))
        mu_a = ftmul(w[k0], ftinv(u[k0]))
        for i in range(27):
            if not ftis0(ftsub(w[i], ftmul(mu_a, u[i]))):
                okc = False
        if lab is None:
            lab = mu_a
        elif not ftis0(ftsub(lab, mu_a)):
            okc = False
    mu_lab[n] = lab
CHK("colored_all_four_charges_scalar", okc)
CHK("colored_even_labels_omega_free",
    kis0(mu_lab[8][1]) and kis0(mu_lab[16][1])
    and kis0(ksub(mu_lab[8][0], c8oct)) and kis0(ksub(mu_lab[16][0], c16oct)),
    "mu8 = octet label (branch alignment); mu8, mu16 in K")
CHK("colored_odd_labels_PURELY_omega_imaginary",
    kis0(mu_lab[14][0]) and kis0(mu_lab[22][0])
    and not (kis0(mu_lab[14][1]) and kis0(mu_lab[22][1])),
    "mu14, mu22 have ZERO K-part and nonzero omega-part: the exact input of "
    "the (+,-) selection rule -- conj(mu_odd) = -mu_odd on every branch")
y14 = mu_lab[14][1]
y22 = mu_lab[22][1]
REC("colored_mu14_omega_part_K", [str(c) for c in y14])
REC("colored_mu22_omega_part_K", [str(c) for c in y22])

# abstract H-Grams on the + atom, both gauges (B928 [11] instruments)
def gram_colored(cb):
    G = [[FTZERO] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            acc = FTZERO
            for b in range(27):
                a2 = piW[b]
                if ftis0(colB[i][a2]) or ftis0(colB[j][b]):
                    continue
                acc = ftadd(acc, ftscale(ftmul(ftconj(colB[i][a2]),
                                               colB[j][b]), Fr(cb[b])))
            G[i][j] = acc
    return G


def gram_colored_pm(cb):
    """the (+,-) cross block: h(colB_i, conj colB_j) under cb."""
    G = [[FTZERO] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            acc = FTZERO
            for b in range(27):
                a2 = piW[b]
                if ftis0(colB[i][a2]) or ftis0(colB[j][b]):
                    continue
                acc = ftadd(acc, ftscale(ftmul(ftconj(colB[i][a2]),
                                               ftconj(colB[j][b])),
                                         Fr(cb[b])))
            G[i][j] = acc
    return G


def ftdet3(G):
    d = FTZERO
    for pi2, sgn2 in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                      ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
        t2 = ftmul(ftmul(G[0][pi2[0]], G[1][pi2[1]]), G[2][pi2[2]])
        d = ftadd(d, ftscale(t2, Fr(sgn2)))
    return d


def ftinv3(G):
    d = ftdet3(G)
    di = ftinv(d)
    C2 = [[FTZERO] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            i1, i2 = [a2 for a2 in range(3) if a2 != i]
            j1, j2 = [a2 for a2 in range(3) if a2 != j]
            m = ftsub(ftmul(G[i1][j1], G[i2][j2]),
                      ftmul(G[i1][j2], G[i2][j1]))
            if (i + j) % 2:
                m = ftscale(m, Fr(-1))
            C2[j][i] = ftmul(m, di)
    return C2, d


Gp = gram_colored(cbP)          # H+ Gram on the + atom (abstract)
Gt = gram_colored(cbT)          # H' Gram on the + atom
CHK("colored_gram_Hplus_invertible", not ftis0(ftdet3(Gp)))
CHK("colored_gram_Hprime_invertible", not ftis0(ftdet3(Gt)))
Gpi, _dp = ftinv3(Gp)
Gti, _dt = ftinv3(Gt)
Xm = [[FTZERO] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        acc = FTZERO
        for t2 in range(3):
            acc = ftadd(acc, ftmul(Gpi[i][t2], Gt[t2][j]))
        Xm[i][j] = acc
e1 = ftadd(ftadd(Xm[0][0], Xm[1][1]), Xm[2][2])
CHK("colored_twist_trace_minpoly_equals_banked_B928",
    kis0(e1[1]) and kminpoly(e1[0]) ==
    [int(c) for c in B928R["Q3_colored"]["minpoly_e1"]],
    "the abstract colored machinery reproduces the banked twist spectrum")

# THE ABSTRACT (a) FORCED ZERO under H+: the (+,-) cross block
Bpm_plus = gram_colored_pm(cbP)
CHK("FORCED_a_Hplus_same_generation_cross_branch_block_ZERO",
    all(ftis0(Bpm_plus[i][j]) for i in range(3) for j in range(3)),
    "h_{H+}(atom(g,+), atom(g,-)) = 0 EXACTLY (abstract, all branches at "
    "once): the odd labels are purely omega-imaginary and nonzero, so the "
    "selection rule kills the whole 3x3 color block")
Bpm_tw = gram_colored_pm(cbT)
REC("a_Hprime_same_generation_cross_branch_nonzero",
    any(not ftis0(Bpm_tw[i][j]) for i in range(3) for j in range(3)),
    "the twisted gauge DOES couple the two branches (same generation)")
dump()

# ================================================================ [5] embed
log("[5] embeddings into Mbar per generation; ascending-rho order ...")
mp.dps = 120
mu_r_sorted = sorted(_mu_roots_numeric(300))
mp.dps = 120
rho_id = mu_r_sorted[0]      # the identity embedding K -> R sends rho here


def knum(kx, r=None):
    r = rho_id if r is None else r
    return (mp.mpf(kx[0].numerator) / kx[0].denominator
            + (mp.mpf(kx[1].numerator) / kx[1].denominator) * r
            + (mp.mpf(kx[2].numerator) / kx[2].denominator) * r * r)


# beta = the N-generator: root of x^2 + P_N x + Q_N over K
disc_b = mp.sqrt(knum(P_N) ** 2 - 4 * knum(Q_N))
beta1 = (-knum(P_N) + disc_b) / 2
beta2 = (-knum(P_N) - disc_b) / 2
# beta_num = whichever of beta1/beta2 is closest to an actual mu root
others = [mu_r_sorted[1], mu_r_sorted[2]]
cands = [(abs(beta1 - o), beta1) for o in others] \
    + [(abs(beta2 - o), beta2) for o in others]
beta_num = min(cands)[1]
CHK("beta_matches_a_mu_root",
    min(abs(beta_num - o) for o in others) < mp.mpf(10) ** (-80))


def nnum(xN):
    return knum(xN[0]) + knum(xN[1]) * beta_num


def tnum(a):
    return mp.mpc(nnum(a[0])) + mp.mpc(0, 1) * mp.sqrt(3) * mp.mpc(nnum(a[1]))


# code branch g -> numeric root of mu13
branch_root = {0: rho_id, 1: beta_num,
               2: -knum((b_mu, Fr(0), Fr(0))) - rho_id - beta_num}
CHK("three_branch_roots_are_the_mu_roots",
    max(min(abs(branch_root[g] - r) for r in mu_r_sorted)
        for g in range(3)) < mp.mpf(10) ** (-80))
# ascending-rho order: ORD[k] = code branch with k-th smallest root
ORD = sorted(range(3), key=lambda g: branch_root[g])
REC("generation_order_ascending_rho_code_branches", ORD,
    "reported matrices use ascending-rho generation indexing (the banked "
    "B928/B929 sheet convention = ascending v_g^2, HG2)")
# CHK the m_S branches against the banked B928 50d certificates
mS_num = [knum(m_S, branch_root[ORD[k]]) for k in range(3)]
certs_banked = B928R["Q3_certificates_50d_by_ascending_rho"]["m_S"]
CHK("m_S_branches_match_banked_B928_certs",
    max(abs(mS_num[k] - mp.mpf(certs_banked[k])) for k in range(3))
    < mp.mpf(10) ** (-45),
    " ".join(mp.nstr(v, 20) for v in mS_num))


def embK_vec(vecK, g):
    return [(sigma(g, kx), NZERO) for kx in vecK]


def embA_vec(g, s):
    return [(sigma(g, u27[b]), nscale(sigma(g, wodd27[b]), Fr(s)))
            for b in range(27)]


def embC_vec(g, s):
    out = []
    for b in range(27):
        xx, yy = colB_cur[b]
        out.append((sigma(g, xx), nscale(nmul(sigma(g, yy), S77), Fr(s))))
    return out


S_emb = {g: embK_vec(vS27, g) for g in range(3)}
A_emb = {(g, s): embA_vec(g, s) for g in range(3) for s in (1, -1)}
C_emb = {}
for a in range(3):
    colB_cur = colB[a]
    for g in range(3):
        for s in (1, -1):
            C_emb.setdefault((g, s), []).append(embC_vec(g, s))
log("    embeddings built")
dump()

# ================================================================ [6] (b)
log("[6] (b) the colorless master Grams 9x9, both gauges, exact in Mbar ...")
NINE = [("S", g) for g in range(3)] + [("A+", g) for g in range(3)] \
    + [("A-", g) for g in range(3)]


def vec_of(tag):
    kind, g = tag
    if kind == "S":
        return S_emb[g]
    return A_emb[(g, 1 if kind == "A+" else -1)]


def hpair(u, v, cb, subset=None):
    acc = TZERO
    rng = range(27) if subset is None else subset
    for b in rng:
        a = piW[b]
        if tis0(u[a]) or tis0(v[b]):
            continue
        acc = tadd(acc, tscale(tmul(tconj(u[a]), v[b]), Fr(cb[b])))
    return acc


G9P = [[hpair(vec_of(NINE[i]), vec_of(NINE[j]), cbP) for j in range(9)]
       for i in range(9)]
G9T = [[hpair(vec_of(NINE[i]), vec_of(NINE[j]), cbT) for j in range(9)]
       for i in range(9)]
CHK("FORCED_b_Hplus_gram_is_exactly_diagonal",
    all(tis0(G9P[i][j]) for i in range(9) for j in range(9) if i != j),
    "the colorless nine are pairwise H+-orthogonal INCLUDING all cross-"
    "generation and cross-register pairs (B914's identity, recomputed in "
    "Mbar): under the canonical gauge there is NO overlap to read")
CHK("b_Hplus_diagonal_matches_q",
    all(tis0(tsub(G9P[i][i], (sigma(NINE[i][1], qS if NINE[i][0] == "S"
                                    else qA), NZERO))) for i in range(9)))
CHK("b_Hprime_diagonal_is_d_times_q",
    all(tis0(tsub(G9T[i][i],
                  (sigma(NINE[i][1], kmul(d_S if NINE[i][0] == "S" else d_A,
                                          qS if NINE[i][0] == "S" else qA)),
                   NZERO))) for i in range(9)))
CHK("b_Hprime_gram_hermitian",
    all(tis0(tsub(G9T[j][i], tconj(G9T[i][j]))) for i in range(9)
        for j in range(9)))
# signature of H' on the colorless nine (diag signs, ascending-rho)
sig_diag = []
for i in range(9):
    v = nnum(G9T[i][i][0])
    sig_diag.append(1 if v > 0 else -1)
REC("b_Hprime_diag_signs_NINE_order", sig_diag,
    str([f"{k}{g}" for k, g in NINE]))

# normalized overlap moduli^2 as exact N-elements: |G_ij|^2/(|G_ii||G_jj|)
def mbar_abs2(a):
    return nadd(nmul(a[0], a[0]), nscale(nmul(a[1], a[1]), Fr(3)))


R9 = {}
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        num = mbar_abs2(G9T[i][j])
        den = nmul(G9T[i][i][0], G9T[j][j][0])
        R9[(i, j)] = nmul(num, ninv(den))
Ghat_mod = [[mp.mpf(1) if i == j else
             mp.sqrt(abs(nnum(R9[(i, j)]))) for j in range(9)]
            for i in range(9)]
# the (b) deliverable blocks in ascending-rho order: S x A+ and S x A-
bSAp = [[Ghat_mod[NINE.index(("S", ORD[i]))][NINE.index(("A+", ORD[j]))]
         for j in range(3)] for i in range(3)]
bSAm = [[Ghat_mod[NINE.index(("S", ORD[i]))][NINE.index(("A-", ORD[j]))]
         for j in range(3)] for i in range(3)]
CHK("b_SA_plus_minus_moduli_FORCED_equal_EXACT",
    all(nis0(nsub(R9[(NINE.index(("S", g1)), NINE.index(("A+", g2)))],
                  R9[(NINE.index(("S", g1)), NINE.index(("A-", g2)))]))
        for g1 in range(3) for g2 in range(3)),
    "h'(S, A-) = conj h'(S, A+) (S is real): the two A-columns carry "
    "identical moduli EXACTLY -- the 3x6 collapses to one 3x3")
# exact closed form, same generation: x_e, x_o in K
x_e = KZERO
x_o = KZERO
for b in range(27):
    a = piW[b]
    x_e = kadd(x_e, kscale(kmul(vS27[a], u27[b]), Fr(cbT[b])))
    x_o = kadd(x_o, kscale(kmul(vS27[a], wodd27[b]), Fr(cbT[b])))
gg0 = ORD[0]
CHK("b_same_gen_closed_form_matches_embedded",
    tis0(tsub(G9T[NINE.index(("S", gg0))][NINE.index(("A+", gg0))],
              (sigma(gg0, x_e), sigma(gg0, x_o)))),
    "h'(S_g, A_g+) = sigma_g(x_e) + tau sigma_g(x_o), x_e, x_o in K")
r_diag_b = kmul(kadd(kmul(x_e, x_e), kscale(kmul(x_o, x_o), Fr(3))),
                kinv(kmul(kmul(d_S, qS), kmul(d_A, qA))))
REC("b_same_gen_overlap_sq_K_coords", [str(c) for c in r_diag_b],
    "|Ghat(S_g, A_g)|^2 as ONE K-element (3 Galois branches)")
REC("b_same_gen_overlap_sq_minpoly", kminpoly(r_diag_b))
# minpolys of the cross-generation moduli^2 (N-elements)
b_minpolys = {}
for i in range(3):
    for j in range(3):
        el = R9[(NINE.index(("S", ORD[i])), NINE.index(("A+", ORD[j])))]
        try:
            b_minpolys[f"{i+1}{j+1}"] = nminpoly(el)
        except Exception as e:
            b_minpolys[f"{i+1}{j+1}"] = f"SKIPPED ({e})"
RES["b_overlap"] = {
    "definition": "Ghat_ij = h'(S_i, A_j+)/sqrt(|h'(S_i,S_i)||h'(A_j,A_j)|),"
                  " ascending-rho generations; H+ version is EXACTLY zero",
    "moduli_50d": [[mp.nstr(bSAp[i][j], 50) for j in range(3)]
                   for i in range(3)],
    "moduli_sq_minpolys": b_minpolys,
    "same_gen_sq_K": [str(c) for c in r_diag_b],
    "same_gen_sq_minpoly": kminpoly(r_diag_b),
    "Hprime_diag_signs": sig_diag,
}
# the S x S and A x A off-diagonal moduli (secondary: the full master table)
RES["b_master_9x9_moduli_50d"] = {
    "order": [f"{k}{g}(asc rho pos {ORD.index(g)})" for k, g in NINE],
    "moduli": [[mp.nstr(Ghat_mod[i][j], 30) for j in range(9)]
               for i in range(9)],
}
dump()

# ================================================================ [7] (a)
log("[7] (a) the two colored triples: blocks, projector overlaps, exact ...")


def mat3_from_pairs(ui, vj, cb):
    return [[hpair(ui[a], vj[b], cb) for b in range(3)] for a in range(3)]


def mat3_mul(A, B):
    return [[tadd(tadd(tmul(A[i][0], B[0][j]), tmul(A[i][1], B[1][j])),
                  tmul(A[i][2], B[2][j])) for j in range(3)]
            for i in range(3)]


def mat3_dagger(A):
    return [[tconj(A[j][i]) for j in range(3)] for i in range(3)]


def mat3_inv(A):
    Aug = [[A[i][j] for j in range(3)]
           + [TONE if i == j2 else TZERO for j2 in range(3)]
           for i in range(3)]
    for c in range(3):
        pr = next((r for r in range(c, 3) if not tis0(Aug[r][c])), None)
        assert pr is not None
        Aug[c], Aug[pr] = Aug[pr], Aug[c]
        iv = tinv(Aug[c][c])
        Aug[c] = [tmul(iv, e) for e in Aug[c]]
        for r in range(3):
            if r != c and not tis0(Aug[r][c]):
                f = Aug[r][c]
                Aug[r] = [tsub(Aug[r][j], tmul(f, Aug[c][j]))
                          for j in range(6)]
    return [[Aug[i][3 + j] for j in range(3)] for i in range(3)]


def mat3_trace(A):
    return tadd(tadd(A[0][0], A[1][1]), A[2][2])


# H+ forced zeros: ALL cross blocks (branch and generation)
allzero = True
for i in range(3):
    for j in range(3):
        for (s1, s2) in ((1, -1), (1, 1)):
            if i == j and s1 == s2:
                continue
            Bblk = mat3_from_pairs(C_emb[(i, s1)], C_emb[(j, s2)], cbP)
            if not all(tis0(Bblk[a][b]) for a in range(3) for b in range(3)):
                allzero = False
CHK("FORCED_a_Hplus_ALL_cross_blocks_ZERO", allzero,
    "under H+ every colored cross pairing vanishes EXACTLY -- cross-branch "
    "(odd-label rule) and cross-generation (even-label rule): the canonical "
    "gauge sees NO up/down overlap at all; the overlap can only live in D2")

# H' Grams (within-atom) and cross blocks
Gc = {}
for g in range(3):
    for s in (1, -1):
        Gc[(g, s)] = mat3_from_pairs(C_emb[(g, s)], C_emb[(g, s)], cbT)
CHK("a_Hprime_atom_grams_match_abstract",
    all(tis0(tsub(Gc[(g, 1)][a][b],
                  (sigma(g, Gt[a][b][0]),
                   nmul(sigma(g, Gt[a][b][1]), S77))))
        for g in range(3) for a in range(3) for b in range(3)),
    "embedded H' atom Grams = sigma_g of the abstract Gt (omega -> S77 tau)")
Gci = {k: mat3_inv(v) for k, v in Gc.items()}

t_pm = [[None] * 3 for _ in range(3)]
t_pp = [[None] * 3 for _ in range(3)]
B_store = {}
for i in range(3):
    for j in range(3):
        Bpm = mat3_from_pairs(C_emb[(i, 1)], C_emb[(j, -1)], cbT)
        B_store[(i, j, "pm")] = Bpm
        Tm = mat3_mul(mat3_mul(Gci[(i, 1)], Bpm),
                      mat3_mul(Gci[(j, -1)], mat3_dagger(Bpm)))
        t_pm[i][j] = mat3_trace(Tm)
        Bpp = mat3_from_pairs(C_emb[(i, 1)], C_emb[(j, 1)], cbT)
        B_store[(i, j, "pp")] = Bpp
        Tm2 = mat3_mul(mat3_mul(Gci[(i, 1)], Bpp),
                       mat3_mul(Gci[(j, 1)], mat3_dagger(Bpp)))
        t_pp[i][j] = mat3_trace(Tm2)
CHK("a_tij_tau_free_real",
    all(nis0(t_pm[i][j][1]) and nis0(t_pp[i][j][1])
        for i in range(3) for j in range(3)),
    "every projector overlap tr(P_i Q_j) is real (an element of N)")
# abstract check of the diagonal: t_ii = sigma_i(t_diag), t_diag in K
# trace of Gt^{-1} Bpm (conjGt)^{-1} Bpm^dagger, abstract over K(omega)
Gt_m = [[ftconj(Gt[i][j]) for j in range(3)] for i in range(3)]
Gti_m, _ = ftinv3(Gt_m)
tr_abs = FTZERO
M1 = [[FTZERO] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        acc = FTZERO
        for a in range(3):
            acc = ftadd(acc, ftmul(Gti[i][a], Bpm_tw[a][j]))
        M1[i][j] = acc
M2 = [[FTZERO] * 3 for _ in range(3)]
Bd = [[ftconj(Bpm_tw[j][i]) for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        acc = FTZERO
        for a in range(3):
            acc = ftadd(acc, ftmul(Gti_m[i][a], Bd[a][j]))
        M2[i][j] = acc
for i in range(3):
    for j in range(3):
        tr_abs = ftadd(tr_abs, ftmul(M1[i][j], M2[j][i]))
CHK("a_t_diag_abstract_omega_free", kis0(tr_abs[1]),
    "the same-generation +- projector overlap is ONE K-element")
t_diag_K = tr_abs[0]
CHK("a_t_diag_embeds_to_diagonal",
    all(tis0(tsub(t_pm[g][g], (sigma(g, t_diag_K), NZERO)))
        for g in range(3)))
REC("a_t_diag_K_coords", [str(c) for c in t_diag_K])
REC("a_t_diag_minpoly", kminpoly(t_diag_K))
# minpolys of the off-diagonal t (N-elements)
a_minpolys = {}
for i in range(3):
    for j in range(3):
        if i != j:
            try:
                a_minpolys[f"{ORD.index(i)+1}{ORD.index(j)+1}"] = \
                    nminpoly(t_pm[i][j][0])
            except Exception as e:
                a_minpolys[f"{ORD.index(i)+1}{ORD.index(j)+1}"] = \
                    f"SKIPPED ({e})"
# report in ascending-rho order; overlap modulus per color: sqrt(|t|/3)
t_pm_num = [[nnum(t_pm[ORD[i]][ORD[j]][0]) for j in range(3)]
            for i in range(3)]
t_pp_num = [[nnum(t_pp[ORD[i]][ORD[j]][0]) for j in range(3)]
            for i in range(3)]
aG = [[mp.sqrt(abs(t_pm_num[i][j]) / 3) for j in range(3)] for i in range(3)]
# span-projector row sums (the honest unitarity diagnostic): 9x9 minus-span
SPAN = [C_emb[(g, -1)][a] for g in range(3) for a in range(3)]
G99 = [[hpair(SPAN[p], SPAN[q], cbT) for q in range(9)] for p in range(9)]
# invert 9x9 over Mbar
Aug9 = [[G99[i][j] for j in range(9)]
        + [TONE if i == j2 else TZERO for j2 in range(9)] for i in range(9)]
ok9 = True
for c in range(9):
    pr = next((r for r in range(c, 9) if not tis0(Aug9[r][c])), None)
    if pr is None:
        ok9 = False
        break
    Aug9[c], Aug9[pr] = Aug9[pr], Aug9[c]
    iv = tinv(Aug9[c][c])
    Aug9[c] = [tmul(iv, e) for e in Aug9[c]]
    for r in range(9):
        if r != c and not tis0(Aug9[r][c]):
            f = Aug9[r][c]
            Aug9[r] = [tsub(Aug9[r][j], tmul(f, Aug9[c][j]))
                       for j in range(18)]
CHK("a_minus_span_gram_invertible_Hprime", ok9,
    "the 9-dim minus-triple span is H'-nondegenerate")
G99i = [[Aug9[i][9 + j] for j in range(9)] for i in range(9)]
row_leak = []
for pos in range(3):
    i = ORD[pos]
    Bfull = [[hpair(C_emb[(i, 1)][a], SPAN[q], cbT) for q in range(9)]
             for a in range(3)]
    # tr(Gi^{-1} Bfull G99^{-1} Bfull^dagger)
    M1b = [[TZERO] * 9 for _ in range(3)]
    for a in range(3):
        for q in range(9):
            acc = TZERO
            for b in range(3):
                acc = tadd(acc, tmul(Gci[(i, 1)][a][b], Bfull[b][q]))
            M1b[a][q] = acc
    M2b = [[TZERO] * 3 for _ in range(9)]
    for p in range(9):
        for a in range(3):
            acc = TZERO
            for q in range(9):
                acc = tadd(acc, tmul(G99i[p][q], tconj(Bfull[a][q])))
            M2b[p][a] = acc
    tr = TZERO
    for a in range(3):
        for p in range(9):
            tr = tadd(tr, tmul(M1b[a][p], M2b[p][a]))
    row_leak.append(nnum(tr[0]) / 3)
RES["a_overlap"] = {
    "definition": "t_ij = tr(P_(i,+) P_(j,-)) with H'-orthogonal projectors "
                  "onto the 3-dim colored atoms; |G_ij| = sqrt(|t_ij|/3); "
                  "ascending-rho generations; H+ version EXACTLY zero "
                  "(all 9 blocks, forced)",
    "t_pm_50d": [[mp.nstr(t_pm_num[i][j], 50) for j in range(3)]
                 for i in range(3)],
    "t_pp_50d": [[mp.nstr(t_pp_num[i][j], 50) for j in range(3)]
                 for i in range(3)],
    "t_diag_K": [str(c) for c in t_diag_K],
    "t_diag_minpoly": kminpoly(t_diag_K),
    "t_offdiag_minpolys": a_minpolys,
    "moduli_50d": [[mp.nstr(aG[i][j], 50) for j in range(3)]
                   for i in range(3)],
    "row_projection_onto_full_minus_span_per_color":
        [mp.nstr(v, 30) for v in row_leak],
}
dump()

# ================================================================ [8] (c)
log("[8] (c) the flip compressions: rational charpolys + the W3 rotation ...")


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


def compression(W):
    G = gramQ(W, cbP)
    Hf = gramQ(W, cbP, flip_ind)
    Gi = qinv_mat(G)
    return matmulQ(Gi, Hf), G


Cmp3, G3 = compression(W3)
Cmp6, G6 = compression(W6)
Cmp18, G18 = compression(W18)
cp3 = sp.Matrix(3, 3, lambda i, j: sp.Rational(Cmp3[i][j].numerator,
                                               Cmp3[i][j].denominator)
                ).charpoly(x)
cp6 = sp.Matrix(6, 6, lambda i, j: sp.Rational(Cmp6[i][j].numerator,
                                               Cmp6[i][j].denominator)
                ).charpoly(x)
log("    3x3 and 6x6 charpolys done; 18x18 ...")
t18 = time.time()
cp18 = sp.Matrix(18, 18, lambda i, j: sp.Rational(Cmp18[i][j].numerator,
                                                  Cmp18[i][j].denominator)
                 ).charpoly(x)
log(f"    18x18 charpoly in {time.time()-t18:.1f}s")
# sum rule: total trace = 11
tr3 = sum(Cmp3[i][i] for i in range(3))
tr6 = sum(Cmp6[i][i] for i in range(6))
tr18 = sum(Cmp18[i][i] for i in range(18))
CHK("c_traces_sum_rule_11", tr3 + tr6 + tr18 == 11,
    f"tr W3 = {tr3}, tr W6 = {tr6}, tr W18 = {tr18}; the three register "
    "compressions exhaust tr Pi_F = 11 exactly")
KcpS = kcharpoly3(m_S)
CHK("c_trace_W3_equals_Tr_m_S", tr3 == -sp.Rational(KcpS[1]))
KcpA = kcharpoly3(m_A)
CHK("c_trace_W6_equals_2_Tr_m_A", tr6 == -2 * sp.Rational(KcpA[1]))
fac3 = sp.factor_list(cp3.as_expr())
fac6 = sp.factor_list(cp6.as_expr())
fac18 = sp.factor_list(cp18.as_expr())


def fac_repr(fl_):
    out = []
    for f, m in sorted(fl_[1], key=lambda t: sp.degree(t[0], x)):
        out.append({"deg": int(sp.degree(f, x)), "mult": int(m),
                    "coeffs": [str(c) for c in
                               int_primitive(sp.Poly(f, x).all_coeffs())]})
    return out


REC("c_W3_charpoly_factors", json.dumps(fac_repr(fac3)))
REC("c_W6_charpoly_factors", json.dumps(fac_repr(fac6)))
REC("c_W18_charpoly_factors", json.dumps(fac_repr(fac18)))
# eigenvalue-1 line in W3 (dim F cap W3 = 1, banked B928; recompute)
CmI = [[Cmp3[i][j] - (1 if i == j else 0) for j in range(3)]
       for i in range(3)]
ker1 = qkernel([[CmI[i][j] for j in range(3)] for i in range(3)])
CHK("c_W3_eigenvalue_1_multiplicity_one", len(ker1) == 1,
    "the W3 compression has eigenvalue 1 with multiplicity exactly 1 "
    "(= dim(F cap W3), the banked B928 intersection)")
vstar27 = [sum(ker1[0][a] * W3[a][i] for a in range(3)) for i in range(27)]
CHK("c_intersection_line_inside_flip_span",
    all(vstar27[b] == 0 for b in unflip),
    "the eigenvalue-1 principal direction IS the rational line "
    "F cap W3: one exact unity principal angle between the twist "
    "frame and the vacuum register")
# the S-frame compression matrix in N (ascending-rho) and its identity with
# the S x S block of the H' gram: M_ij = (delta_ij q_i - h'(S_i,S_j))/2
MS = [[hpair(S_emb[ORD[i]], S_emb[ORD[j]], cbP, flip_ind) for j in range(3)]
      for i in range(3)]
ok_id = True
for i in range(3):
    for j in range(3):
        rhs = tscale(tsub((sigma(ORD[i], qS), NZERO)
                          if i == j else TZERO,
                          G9T[NINE.index(("S", ORD[i]))]
                          [NINE.index(("S", ORD[j]))]), Fr(1, 2))
        if not tis0(tsub(MS[i][j], rhs)):
            ok_id = False
CHK("c_S_compression_equals_half_q_minus_HprimeSS", ok_id,
    "M_ij = (delta_ij q_i - h'(S_i, S_j))/2 EXACTLY: the (c) matrix and "
    "the S x S block of the twist gram carry the same information")
CHK("c_S_compression_symmetric_exact",
    all(tis0(tsub(MS[i][j], MS[j][i])) for i in range(3) for j in range(3)))
qb = [knum(qS, branch_root[ORD[i]]) for i in range(3)]
# DESIGN AMENDMENT at completion (logged): the positivity assumption was wrong
# BY BANKED KNOWLEDGE (B912: the twist gauge is indefinite) -- the abort fired
# honestly. Signature-aware treatment (the B913 pattern): normalize by |q| and
# carry the sign vector as data; principal angles are w.r.t. the |.|-metric.
REC("c_vacuum_norm_signs", [1 if v > 0 else -1 for v in qb],
     "the W3 register's h-signs (indefinite is EXPECTED per B912)")
qb_abs = [abs(v) for v in qb]
Mhat = [[nnum(MS[i][j][0]) / mp.sqrt(qb_abs[i] * qb_abs[j]) for j in range(3)]
        for i in range(3)]
# charpoly consistency: Mhat similar to Cmp3
cp3n = [mp.mpf(1)]
for c in sp.Poly(cp3.as_expr(), x).all_coeffs()[1:]:
    cp3n.append(mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q))
# eigenvalues of Mhat (symmetric): mp.eigsy
Msym = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Msym[i, j] = Mhat[i][j]
EV, EVec = mp.eigsy(Msym)
evs = sorted([EV[i] for i in range(3)], reverse=True)


# evaluate the rational charpoly at the numeric eigenvalues
def cp3_eval(v):
    acc = mp.mpf(0)
    for c in cp3n:
        acc = acc * v + c
    return acc


# sign convention (design amendment 2, logged): with the register uniformly
# NEGATIVE under h (the [−1,−1,−1] sign vector just recorded), the |q|-
# normalized eigenvalues are the NEGATIVES of the rational charpoly's roots;
# thread the sign through rather than assuming positivity.
sgn_reg = -1 if all(v < 0 for v in qb) else 1
evs_conv = [sgn_reg * v for v in evs]
CHK("c_S_frame_eigs_are_rational_charpoly_roots",
    max(abs(cp3_eval(v)) for v in evs_conv) < mp.mpf(10) ** (-90),
    "sign-threaded: " + " ".join(mp.nstr(v, 20) for v in evs_conv))
# the rotation R: columns = principal vectors (desc eigenvalue), rows = S-frame
order_ev = sorted(range(3), key=lambda i: -sgn_reg * EV[i])
Rrot = [[EVec[i, order_ev[c]] for c in range(3)] for i in range(3)]
# fix column signs: largest |entry| positive
for c in range(3):
    imax = max(range(3), key=lambda i: abs(Rrot[i][c]))
    if Rrot[imax][c] < 0:
        for i in range(3):
            Rrot[i][c] = -Rrot[i][c]
udef = mp.mpf(0)
for i in range(3):
    for j in range(3):
        s = sum(Rrot[k][i] * Rrot[k][j] for k in range(3)) \
            - (1 if i == j else 0)
        udef = max(udef, abs(s))
CHK("c_rotation_orthogonal", udef < mp.mpf(10) ** (-90),
    "R in O(3) exactly (the S-frame |h|-orthonormal; the register's "
    "uniform sign threaded): the ONE genuinely unitary overlap matrix")
# exact |R_i1|^2 for the unity column: h(S_i, v*)^2/(q_i h(v*,v*))
Rcol1_sq = []
vstar_e = [((( vv, Fr(0), Fr(0)), KZERO), NZERO) for vv in vstar27]
hvv = hpair(vstar_e, vstar_e, cbP)
col1_belt = mp.mpf(0)
for i in range(3):
    hsv = hpair(S_emb[ORD[i]], vstar_e, cbP)
    el = nmul(nmul(hsv[0], hsv[0]),
              ninv(nmul(sigma(ORD[i], qS), hvv[0])))
    try:
        mpo = nminpoly(el)
    except Exception as e:
        mpo = f"SKIPPED ({e})"
    Rcol1_sq.append({"N_value_50d": mp.nstr(nnum(el), 50),
                     "minpoly": mpo})
    col1_belt = max(col1_belt, abs(abs(nnum(el)) - Rrot[i][0] ** 2))
CHK("c_unity_column_exact_matches_numeric_R",
    col1_belt < mp.mpf(10) ** (-80),
    "the exact F-cap-W3 line reproduces the first R column entrywise")
RES["c_overlap"] = {
    "definition": "Pi_F = (1-D2)/2 compressed to the register blocks by the "
                  "H+-orthogonal projectors; rational charpolys = exact "
                  "principal spectra of the twist frame against the Galois "
                  "frame; R = eigenframe of the W3 compression in the "
                  "h-orthonormal S-frame (columns desc eigenvalue, "
                  "ascending-rho rows)",
    "W3_charpoly_factors": fac_repr(fac3),
    "W6_charpoly_factors": fac_repr(fac6),
    "W18_charpoly_factors": fac_repr(fac18),
    "traces": {"W3": str(tr3), "W6": str(tr6), "W18": str(tr18)},
    "W3_eigs_50d": [mp.nstr(v, 50) for v in evs],
    "R_50d": [[mp.nstr(Rrot[i][j], 50) for j in range(3)] for i in range(3)],
    "R_unity_column_sq_exact": Rcol1_sq,
    "S_frame_compression_Mhat_50d":
        [[mp.nstr(Mhat[i][j], 50) for j in range(3)] for i in range(3)],
}
dump()

# ================================================================ [9] ident
log("[9] identification: the two triples vs B912 atom indices [1,5,10]/[2,6,11]")


def parse_c(s):
    return complex(s.strip("()").replace(" ", ""))


b912_mu14 = {a["atom"]: parse_c(a["mu14"]) for a in B912["atoms"]
             if a["kind"] == "colored"}
b912_mu8 = {a["atom"]: parse_c(a["mu8"]) for a in B912["atoms"]
            if a["kind"] == "colored"}
S77_num = nnum(S77)
match = {}
for g in range(3):
    for s in (1, -1):
        mu14_emb = knum(y14, branch_root[g]) * S77_num * mp.sqrt(3) * s
        mu8_emb = knum(c8oct, branch_root[g])
        best = None
        for idx, v in b912_mu14.items():
            if abs(b912_mu8[idx].real - float(mu8_emb)) > 1e-10 * \
                    max(1.0, abs(b912_mu8[idx].real)):
                continue
            d = abs(v.imag - float(mu14_emb))
            if best is None or d < best[0]:
                best = (d, idx)
        match[(g, s)] = best[1]
        CHK(f"ident_atom_g{g}{'p' if s == 1 else 'm'}_matches_B912",
            best[0] < 1e-12 * max(1.0, abs(float(mu14_emb))),
            f"-> B912 atom {best[1]}")
trip_plus = sorted(match[(g, 1)] for g in range(3))
trip_minus = sorted(match[(g, -1)] for g in range(3))
CHK("ident_triples_are_the_two_ccc_transversals",
    {tuple(trip_plus), tuple(trip_minus)} ==
    {(1, 5, 10), (2, 6, 11)},
    f"+ branch = {trip_plus}, - branch = {trip_minus}")
CHK("ident_matches_banked_B923_map",
    all(match[(g, 1)] == B923R["colored_match_g_s_to_B912"][f"g{g}p"]
        and match[(g, -1)] == B923R["colored_match_g_s_to_B912"][f"g{g}m"]
        for g in range(3)))
RES["identification"] = {
    "plus_branch_triple_B912": trip_plus,
    "minus_branch_triple_B912": trip_minus,
    "map": {f"g{g}{'p' if s == 1 else 'm'}": match[(g, s)]
            for g in range(3) for s in (1, -1)}}
dump()

# ================================================================ [10] shape
log("[10] shape analysis: Wolfenstein orderings + cascade indices ...")


def shape_report(M3, name):
    """M3: 3x3 moduli (mpf), ascending-rho indexing."""
    diag = [M3[i][i] for i in range(3)]
    off = {"12": M3[0][1], "23": M3[1][2], "13": M3[0][2],
           "21": M3[1][0], "32": M3[2][1], "31": M3[2][0]}
    allm = sorted([M3[i][j] for i in range(3) for j in range(3)],
                  reverse=True)
    rep = {"moduli_descending": [mp.nstr(v, 25) for v in allm],
           "diag": [mp.nstr(v, 25) for v in diag],
           "offdiag": {k: mp.nstr(v, 25) for k, v in off.items()}}
    def cascade(a12, a23, a13):
        out = {}
        if a12 > 0 and a23 > 0 and a13 > 0:
            r1 = a23 / a12
            r2 = a13 / a23
            out["r1_23_over_12"] = mp.nstr(r1, 25)
            out["r2_13_over_23"] = mp.nstr(r2, 25)
            if r1 not in (0, 1) and r1 < 1 and r2 < 1 and r2 > 0:
                out["accel_index_a"] = mp.nstr(mp.log(r2) / mp.log(r1), 25)
            out["wolfenstein_ordered"] = bool(a12 > a23 > a13)
        return out
    rep["upper"] = cascade(off["12"], off["23"], off["13"])
    rep["lower"] = cascade(off["21"], off["32"], off["31"])
    mind = min(diag)
    maxoff = max(off.values())
    rep["diag_dominant"] = bool(mind > maxoff)
    # priced scan: all 6 generation relabelings
    perms_hit = []
    for pperm in itertools.permutations(range(3)):
        Mp = [[M3[pperm[i]][pperm[j]] for j in range(3)] for i in range(3)]
        dmin = min(Mp[i][i] for i in range(3))
        moff = max(Mp[i][j] for i in range(3) for j in range(3) if i != j)
        if Mp[0][1] > Mp[1][2] > Mp[0][2] and dmin > moff:
            perms_hit.append(list(pperm))
    rep["wolfenstein_perms_upper_hit_of_6"] = perms_hit
    RES.setdefault("shape", {})[name] = rep
    log(f"    {name}: desc {['%.3g' % float(v) for v in allm]}")
    return rep


sh_a = shape_report(aG, "a_colored_pm_Hprime")
sh_b = shape_report([[bSAp[i][j] for j in range(3)] for i in range(3)],
                    "b_S_vs_A_Hprime")
sh_c = shape_report([[abs(Rrot[i][j]) for j in range(3)] for i in range(3)],
                    "c_twist_vs_galois_rotation")
dump()

# ================================================================ [11] belt
log("[11] independent numeric belt (dps 80; componentwise readouts) ...")
mp.dps = 80
RnB = {}
for n in ns:
    M = mp.matrix(27, 27)
    for a in range(27):
        for b in range(27):
            if Rex[n][a][b]:
                M[a, b] = mp.mpf(Rex[n][a][b].numerator) \
                    / Rex[n][a][b].denominator
    RnB[n] = M
Zc = mp.matrix(27, 27)
ZB = 3 * RnB[8] + 17 * RnB[14] + 5 * RnB[16] + 7 * RnB[22]
for i in range(27):
    for j in range(27):
        Zc[i, j] = mp.mpc(ZB[i, j])
Ev, ER = mp.eig(Zc, left=False, right=True)
order = sorted(range(27), key=lambda k: (mp.re(Ev[k]), mp.im(Ev[k])))
clusters = []
for k in order:
    for cl in clusters:
        if abs(Ev[k] - cl["ev"]) < mp.mpf("1e-30"):
            cl["ks"].append(k)
            break
    else:
        clusters.append({"ev": Ev[k], "ks": [k]})
lines = [cl for cl in clusters if len(cl["ks"]) == 1]
atoms3 = [cl for cl in clusters if len(cl["ks"]) == 3]
CHK("belt_9_lines_6_colored_clusters",
    len(lines) == 9 and len(atoms3) == 6)
worst_resid = mp.mpf(0)
for cl in clusters:
    for k in cl["ks"]:
        v = mp.matrix([ER[j, k] for j in range(27)])
        nrm = mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27)))
        v = v / nrm
        istar = max(range(27), key=lambda i2: abs(v[i2]))
        lam = sum(Zc[istar, j] * v[j] for j in range(27)) / v[istar]
        resid = max(abs(sum(Zc[i2, j] * v[j] for j in range(27))
                        - lam * v[i2]) for i2 in range(27))
        worst_resid = max(worst_resid, resid)
        cl.setdefault("vecs", []).append(v)
CHK("belt_eigen_residual_certificates", worst_resid < mp.mpf("1e-55"),
    f"worst componentwise residual {mp.nstr(worst_resid, 3)} (no Rayleigh)")
HPn = mp.matrix(27, 27)
HTn = mp.matrix(27, 27)
for b in range(27):
    HPn[piW[b], b] = cbP[b]
    HTn[piW[b], b] = cbT[b]


def hnum(u, v, Hm):
    return sum(mp.conj(u[piW[b]]) * Hm[piW[b], b] * v[b] for b in range(27))


# identify numeric clusters: lines by Zc eigenvalue vs embedded labels
zS = [3 * knum(c8vac, branch_root[g]) + 5 * knum(c16vac, branch_root[g])
      for g in range(3)]
zA = [3 * knum(c8oct, branch_root[g]) + 5 * knum(c16oct, branch_root[g])
      for g in range(3)]
line_map = {}
for cl in lines:
    ev = mp.re(cl["ev"])
    best = min([(abs(ev - zS[g]), ("S", g)) for g in range(3)]
               + [(abs(ev - zA[g]), ("A", g)) for g in range(3)])
    line_map.setdefault(best[1], []).append(cl)
CHK("belt_line_identification",
    all(len(line_map.get(("S", g), [])) == 1
        and len(line_map.get(("A", g), [])) == 2 for g in range(3)))
zode = [(17 * knum(y14, branch_root[g]) + 7 * knum(y22, branch_root[g]))
        * S77_num * mp.sqrt(3) for g in range(3)]
col_map = {}
worst_ident = mp.mpf(0)
for cl in atoms3:
    ev = cl["ev"]
    best = min([(abs(ev - (zA[g] + mp.mpc(0, 1) * zode[g] * s)), (g, s))
                for g in range(3) for s in (1, -1)])
    worst_ident = max(worst_ident, best[0])
    col_map[best[1]] = cl
CHK("belt_colored_identification", len(col_map) == 6
    and worst_ident < mp.mpf("1e-40"),
    f"worst eigenvalue match {mp.nstr(worst_ident, 3)}")
# numeric (b) moduli
bnum = [[None] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        Sv = line_map[("S", ORD[i])][0]["vecs"][0]
        # the two A lines of branch j: pick either (moduli forced equal);
        # compare BOTH to the exact value
        vals = []
        for Acl in line_map[("A", ORD[j])]:
            Av = Acl["vecs"][0]
            num = abs(hnum(Sv, Av, HTn))
            den = mp.sqrt(abs(hnum(Sv, Sv, HTn)) * abs(hnum(Av, Av, HTn)))
            vals.append(num / den)
        bnum[i][j] = vals
worst_b = max(abs(v - bSAp[i][j]) for i in range(3) for j in range(3)
              for v in bnum[i][j])
CHK("belt_b_moduli_match_exact", worst_b < mp.mpf("1e-30"),
    f"worst {mp.nstr(worst_b, 3)} (independent eig route, both A lines)")
# numeric (a) t_ij
def gram_num(vs, ws, Hm):
    return mp.matrix([[hnum(vs[a], ws[b], Hm) for b in range(len(ws))]
                      for a in range(len(vs))])


t_num_worst = mp.mpf(0)
for i in range(3):
    for j in range(3):
        vp = col_map[(ORD[i], 1)]["vecs"]
        vm = col_map[(ORD[j], -1)]["vecs"]
        Gi_ = gram_num(vp, vp, HTn)
        Gj_ = gram_num(vm, vm, HTn)
        Bij = gram_num(vp, vm, HTn)
        Tm = Gi_ ** -1 * Bij * Gj_ ** -1 * Bij.transpose_conj()
        tval = mp.re(Tm[0, 0] + Tm[1, 1] + Tm[2, 2])
        t_num_worst = max(t_num_worst, abs(tval - t_pm_num[i][j]))
CHK("belt_a_tij_match_exact", t_num_worst < mp.mpf("1e-25"),
    f"worst {mp.nstr(t_num_worst, 3)}")
# numeric (c): S-frame compression eigs
# design amendment 4 (the last belt): the numeric eigenvectors carry arbitrary
# solver phases; the S-lines are RATIONAL lines, so phase-align each vector
# (largest component real-positive) before building the compression -- the b/a
# belts compared phase-free quantities and never saw this.
def phase_fix(v):
    imax = max(range(27), key=lambda k: abs(v[k]))
    ph = v[imax] / abs(v[imax])
    return [x / ph for x in v]
S_fixed = {i: phase_fix(line_map[("S", ORD[i])][0]["vecs"][0]) for i in range(3)}
Msn = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Sv = S_fixed[i]
        Sw = S_fixed[j]
        num = sum(mp.conj(Sv[piW[b]]) * HPn[piW[b], b] * Sw[b]
                  for b in flip_ind)
        den = mp.sqrt(abs(hnum(Sv, Sv, HPn)) * abs(hnum(Sw, Sw, HPn)))
        Msn[i, j] = mp.re(num) / den
EVn = mp.eigsy(Msn, eigvals_only=True)
# design amendment 3 (sign threading, same as the exact side): the belt's
# independent compression carries the register's uniform sign too
worst_c = max(min(abs(sgn_reg * EVn[i] - evs_conv[j]) for j in range(3))
              for i in range(3))
CHK("belt_c_eigs_match_exact", worst_c < mp.mpf("1e-30"),
    f"worst {mp.nstr(worst_c, 3)}")
RES["belt"] = {"eigen_residual": mp.nstr(worst_resid, 4),
               "b_worst": mp.nstr(worst_b, 4),
               "a_worst": mp.nstr(t_num_worst, 4),
               "c_worst": mp.nstr(worst_c, 4)}
dump()

# ================================================================ [12] verdict
log("[12] verdict ...")
RES["verdict_structure"] = {
    "Hplus": "FORCED ZERO overlap for (a) and (b): exact charge-orthogonality"
             " (even labels separate generations, purely-omega-imaginary odd"
             " labels separate the branches). The canonical gauge cannot mix.",
    "Hprime": "the twist gauge carries ALL the overlap; see shape reports",
    "c": "the W3 compression has ONE exact unity principal angle (the "
         "rational line F cap W3) + a rational quadratic pair; R in O(3)",
}
RES["runtime_s"] = round(time.time() - T00, 1)
dump()
log("results.json written; done")
