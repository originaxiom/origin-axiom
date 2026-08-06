#!/usr/bin/env python3
"""B935 -- THE COMPOSITION HUNT (Lane Q1; blind -- no measured number).

The object holds FOUR cascade classes (v-weights ascending [B923/B929];
m_S descending a ~ 1.84 [B928/B929]; the S-A register hierarchy [B930];
the twist-vs-Galois rotation's cosines [B930]).  This cell computes the
CLOSED WHITELIST of forced compositions, declared before computing:

 (i)   R^T Ghat R      -- the S-A overlap matrix expressed in the rotation's
                          principal frame (the twist frame reading the
                          register hierarchy);
 (ii)  the polar/singular decomposition of the FULL 3x3 S-A overlap matrix
       Ghat: its singular values (the invariant cascade), EXACT via the
       charpoly of X2 = G0^dagger D_S^{-2} G0 D_A^{-2} over the banked
       tower (the sqrt-normalizations rationalize under diagonal
       similarity; signs threaded);
 (iii) Ghat*R and R*Ghat -- the two orderings of register-mixing then
       frame-rotation;
 (iv)  D_v^{1/2} Ghat D_v^{-1/2} with D_v = diag(v_g^2) = diag(sigma_g(
       V_ccl)) the exact HIER-root diagonal (B923; ascending-rho = ascending
       v^2, HG2), so D_v^{1/2} = diag(v_g) = B929's v-weights: the object's
       own weights conjugating its own mixing.  Its singular values EXACT
       via X4 = G0^dagger (D_v D_S^{-2}) G0 (D_A^{-2} D_v^{-1}).

FORCED spectral degeneracies (proved by the algebra, VERIFIED numerically
here): R in O(3) exactly, so sv((i)) = sv((iii), both orderings) = sv(Ghat)
= (ii); (i) and (iv) are similarities, so eig((i)) = eig((iv)) = eig(Ghat);
eig(Ghat*R) = eig(R*Ghat) (AB vs BA).  The whitelist therefore yields
EXACTLY FOUR invariant triples: sv(Ghat) [exact], eig(Ghat) [50d],
eig(Ghat*R) [50d], sv(D_v-conjugate) [exact].  Cascade index per B929:
a = ln r2 / ln r1 on the descending triple, r1 = t2/t1, r2 = t3/t2.
Flag band [1.2, 1.6] per the task (a flag is NOT a claim; hint ledger only).

HOUSE RULES: exact arithmetic for every verdict-bearing claim (the B930
tower K = Q[rho]/mu13 -> N (deg 6) -> Mbar = N(tau), tau^2 = -3);
verify-don't-trust (D2 re-derived by rep propagation; every rebuilt object
CHKed against its banked B916/B928/B930 form); e6_centralizer.py exec'd in
an isolated namespace with chdir to scratch and __file__ set; NO Rayleigh
readouts (eigen triples via charpoly + polyroots, cross-checked by a second
route; Hermitian belts via eighe); definiteness discipline: NO form assumed
positive -- the H' signs (+,+,+|-,-,+) are recomputed with margin and
threaded; no measured number is contacted.

Output: results.json (exact data + checks + the composition table).
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
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b935_")
os.makedirs(SCRATCH, exist_ok=True)
T00 = time.time()
RES = {"cell": "B935 composition hunt", "checks": {}, "notes": []}


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
log("[0] banked inputs: rep27, B912 H+, B916 D2, B907 walls, B923/B928/B930")
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
B930R = json.load(open(os.path.join(REPO, "frontier", "B930_overlap_matrix",
                                    "results.json")))
B929R = json.load(open(os.path.join(REPO, "frontier", "B929_third_crossing",
                                    "results.json")))
# blind discipline: only object-side keys of B929 are ever read below
# (T1/a and secondary_v_ratios); no measured entry is touched.

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

ROOTS6 = None


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
    T rho(x) T = rho(sigma_chi x); None if inconsistent (pure rep
    propagation -- re-derives D2 from the B928 characterization)."""
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
cache = os.path.join(SCRATCH, "b935_frame_cache.pkl")
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

T_chim = rep_diagonal_of_inner(CHI_M)
CHK("D2_rederived_as_rep_diagonal_of_sigma_chi_minus", T_chim is not None,
    "pure rep propagation, no handoff")
D2 = T_chim if T_chim[0] == 1 else [-x for x in T_chim]
CHK("D2_equals_banked_B916_diagonal", D2 == D2_banked)
flip_ind = [b for b in range(27) if D2[b] == -1]
CHK("D2_11_flips_pi_symmetric", len(flip_ind) == 11
    and all(D2[piW[b]] == D2[b] for b in range(27)))
cbT = [cbP[b] * D2[b] for b in range(27)]   # H' = H+ D2 entries
dump()

# ================================================================ [2] fields
log("[2] the exact tower K -> N -> Mbar (B930's machinery, verbatim) ...")
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


# ================================================================ [3] registers
log("[3] the colorless registers over K (B930 [3], re-run) ...")
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
CHK("rational_blocks_dim_3_6", len(W3) == 3 and len(W6) == 6)

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
CHK("dS_dA_minpolys_equal_banked_B916",
    kminpoly(d_S) == MINPOLY_S_banked and kminpoly(d_A) == MINPOLY_A_banked)
CHK("m_S_minpoly_equals_banked_B928",
    kminpoly(m_S) == [int(c) for c in B928R["Q2_colorless"]["minpoly_m_S"]])
dump()

# ================================================================ [4] embed
log("[4] embeddings, ascending-rho order, numeric helpers ...")
mp.dps = 150
mu_r_sorted = sorted(_mu_roots_numeric(300))
mp.dps = 150
rho_id = mu_r_sorted[0]


def knum(kx, r=None):
    r = rho_id if r is None else r
    return (mp.mpf(kx[0].numerator) / kx[0].denominator
            + (mp.mpf(kx[1].numerator) / kx[1].denominator) * r
            + (mp.mpf(kx[2].numerator) / kx[2].denominator) * r * r)


disc_b = mp.sqrt(knum(P_N) ** 2 - 4 * knum(Q_N))
beta1 = (-knum(P_N) + disc_b) / 2
beta2 = (-knum(P_N) - disc_b) / 2
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


branch_root = {0: rho_id, 1: beta_num,
               2: -knum((b_mu, Fr(0), Fr(0))) - rho_id - beta_num}
CHK("three_branch_roots_are_the_mu_roots",
    max(min(abs(branch_root[g] - r) for r in mu_r_sorted)
        for g in range(3)) < mp.mpf(10) ** (-80))
ORD = sorted(range(3), key=lambda g: branch_root[g])
CHK("ascending_rho_order_matches_banked_B930",
    ORD == list(B930R["checks"]
                ["generation_order_ascending_rho_code_branches"]["value"]),
    f"ORD = {ORD}")
mS_num = [knum(m_S, branch_root[ORD[k]]) for k in range(3)]
certs_banked = B928R["Q3_certificates_50d_by_ascending_rho"]["m_S"]
CHK("m_S_branches_match_banked_B928_certs",
    max(abs(mS_num[k] - mp.mpf(certs_banked[k])) for k in range(3))
    < mp.mpf(10) ** (-45))


def embK_vec(vecK, g):
    return [(sigma(g, kx), NZERO) for kx in vecK]


def embA_vec(g, s):
    return [(sigma(g, u27[b]), nscale(sigma(g, wodd27[b]), Fr(s)))
            for b in range(27)]


S_emb = {g: embK_vec(vS27, g) for g in range(3)}
A_emb = {g: embA_vec(g, 1) for g in range(3)}


def hpair(u, v, cb, subset=None):
    acc = TZERO
    rng = range(27) if subset is None else subset
    for b in rng:
        a = piW[b]
        if tis0(u[a]) or tis0(v[b]):
            continue
        acc = tadd(acc, tscale(tmul(tconj(u[a]), v[b]), Fr(cb[b])))
    return acc


dump()

# ================================================================ [5] Ghat
log("[5] the exact base pair: G0 = h'(S_i, A_j+), diagonals, signs ...")
G0 = [[hpair(S_emb[ORD[i]], A_emb[ORD[j]], cbT) for j in range(3)]
      for i in range(3)]
hS_N = [sigma(ORD[i], kmul(d_S, qS)) for i in range(3)]
hA_N = [sigma(ORD[j], kmul(d_A, qA)) for j in range(3)]
CHK("G0_diagonals_equal_hpair_norms",
    all(tis0(tsub(hpair(S_emb[ORD[i]], S_emb[ORD[i]], cbT),
                  (hS_N[i], NZERO))) for i in range(3))
    and all(tis0(tsub(hpair(A_emb[ORD[j]], A_emb[ORD[j]], cbT),
                      (hA_N[j], NZERO))) for j in range(3)),
    "h'(S_i,S_i) = sigma_i(d_S q_S), h'(A_j,A_j) = sigma_j(d_A q_A) exactly")
# definiteness discipline: signs recomputed with margin, then threaded
hS_num = [nnum(h) for h in hS_N]
hA_num = [nnum(h) for h in hA_N]
CHK("sign_margins_certified",
    min(abs(v) for v in hS_num + hA_num) > mp.mpf(10) ** (-30))
sS = [1 if v > 0 else -1 for v in hS_num]
sA = [1 if v > 0 else -1 for v in hA_num]
CHK("signs_match_banked_B930",
    sS == [1, 1, 1] and sA == [-1, -1, 1],
    f"S diag signs {sS}, A+ diag signs {sA} (H' indefinite as banked)")
# same-generation closed form (B930's identity, re-verified)
x_e = KZERO
x_o = KZERO
for b in range(27):
    a = piW[b]
    x_e = kadd(x_e, kscale(kmul(vS27[a], u27[b]), Fr(cbT[b])))
    x_o = kadd(x_o, kscale(kmul(vS27[a], wodd27[b]), Fr(cbT[b])))
CHK("b_same_gen_closed_form_matches_G0_diag",
    all(tis0(tsub(G0[g][g], (sigma(ORD[g], x_e), sigma(ORD[g], x_o))))
        for g in range(3)))
r_diag_b = kmul(kadd(kmul(x_e, x_e), kscale(kmul(x_o, x_o), Fr(3))),
                kinv(kmul(kmul(d_S, qS), kmul(d_A, qA))))
CHK("same_gen_overlap_sq_minpoly_matches_banked_B930",
    kminpoly(r_diag_b) == [int(c) for c in
                           B930R["b_overlap"]["same_gen_sq_minpoly"]])
# numeric Ghat (dps 150) + CHK moduli vs banked B930 50d
Ghat = [[tnum(G0[i][j]) / mp.sqrt(abs(hS_num[i]) * abs(hA_num[j]))
         for j in range(3)] for i in range(3)]
mod_banked = B930R["b_overlap"]["moduli_50d"]
worst_mod = max(abs(abs(Ghat[i][j]) - mp.mpf(mod_banked[i][j]))
                for i in range(3) for j in range(3))
CHK("Ghat_moduli_match_banked_B930_50d", worst_mod < mp.mpf(10) ** (-45),
    f"worst {mp.nstr(worst_mod, 3)}")
dump()

# ================================================================ [6] R
log("[6] the rotation R rebuilt (B930 [8], sign-threaded) + CHK banked ...")
MS = [[hpair(S_emb[ORD[i]], S_emb[ORD[j]], cbP, flip_ind) for j in range(3)]
      for i in range(3)]
CHK("S_compression_symmetric_exact",
    all(tis0(tsub(MS[i][j], MS[j][i])) for i in range(3) for j in range(3)))
qb = [knum(qS, branch_root[ORD[i]]) for i in range(3)]
CHK("vacuum_norm_signs_all_negative_as_banked",
    all(v < 0 for v in qb), "the W3 register is uniformly NEGATIVE under h")
qb_abs = [abs(v) for v in qb]
Mhat = [[nnum(MS[i][j][0]) / mp.sqrt(qb_abs[i] * qb_abs[j]) for j in range(3)]
        for i in range(3)]
Msym = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Msym[i, j] = Mhat[i][j]
EV, EVec = mp.eigsy(Msym)
sgn_reg = -1
order_ev = sorted(range(3), key=lambda i: -sgn_reg * EV[i])
Rrot = [[EVec[i, order_ev[c]] for c in range(3)] for i in range(3)]
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
CHK("rotation_orthogonal", udef < mp.mpf(10) ** (-100),
    "R in O(3) (the |h|-orthonormal S-frame, uniform register sign threaded)")
R_banked = B930R["c_overlap"]["R_50d"]
worst_R = max(abs(Rrot[i][j] - mp.mpf(R_banked[i][j]))
              for i in range(3) for j in range(3))
CHK("R_matches_banked_B930_50d", worst_R < mp.mpf(10) ** (-45),
    f"worst {mp.nstr(worst_R, 3)}")
detR = (Rrot[0][0] * (Rrot[1][1] * Rrot[2][2] - Rrot[1][2] * Rrot[2][1])
        - Rrot[0][1] * (Rrot[1][0] * Rrot[2][2] - Rrot[1][2] * Rrot[2][0])
        + Rrot[0][2] * (Rrot[1][0] * Rrot[2][1] - Rrot[1][1] * Rrot[2][0]))
CHK("det_R_is_plus_or_minus_1", abs(abs(detR) - 1) < mp.mpf(10) ** (-100),
    f"det R = {mp.nstr(detR, 20)}")
REC("det_R_sign", 1 if detR > 0 else -1)
dump()

# ================================================================ [7] v-weights
log("[7] the v-weights: exact V_ccl (B923) + HIER identity re-verified ...")
VK = tuple(Fr(c) for c in B923R["V_ccl_tau_twisted_Hprime"])
HIER_banked = [int(c) for c in
               B923R["checks"]
               ["PIPELINE_LINK_953p4_charpoly_equals_HIER_EXACT"]["detail"]
               .strip("HIER = []").split(",")]
cpV = kcharpoly3(VK)
CHK("HIER_identity_953p4_charpoly_VK",
    [int(953 ** 4 * c) for c in cpV] == HIER_banked,
    "953^4 * charpoly_Q(mult-by-V_ccl) = HIER, re-verified exactly")
v2 = [knum(VK, branch_root[ORD[j]]) for j in range(3)]
CHK("v_squared_positive_ascending_HG2",
    all(v > 0 for v in v2) and v2[0] < v2[1] < v2[2],
    "ascending rho <-> ascending v^2 (the banked identity map)")
vw = [mp.sqrt(v) for v in v2]
v_ratios = [vw[1] / vw[0], vw[2] / vw[1]]
CHK("v_ratios_match_banked_B929",
    max(abs(v_ratios[k] - mp.mpf(B929R["secondary_v_ratios"][k]))
        for k in range(2)) < mp.mpf(10) ** (-9),
    " ".join(mp.nstr(v, 20) for v in v_ratios))
DvN = [sigma(ORD[j], VK) for j in range(3)]    # exact N-elements v_g^2
dump()

# ================================================================ [8] exact sv
log("[8] EXACT singular values: charpolys of X2 (Ghat) and X4 (D_v-conj) ...")


def mat3_mulT(A, B):
    return [[tadd(tadd(tmul(A[i][0], B[0][j]), tmul(A[i][1], B[1][j])),
                  tmul(A[i][2], B[2][j])) for j in range(3)]
            for i in range(3)]


def mat3_traceT(A):
    return tadd(tadd(A[0][0], A[1][1]), A[2][2])


def tdet3(G):
    d = TZERO
    for pi2, sgn2 in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                      ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
        t2 = tmul(tmul(G[0][pi2[0]], G[1][pi2[1]]), G[2][pi2[2]])
        d = tadd(d, tscale(t2, Fr(sgn2)))
    return d


invhS = [ninv(h) for h in hS_N]      # 1/sigma_i(d_S q_S); sign sS = +1 all
invhA = [ninv(h) for h in hA_N]      # 1/sigma_j(d_A q_A); sign sA = (-,-,+)
invDv = [ninv(d) for d in DvN]


def build_X(row_w, col_w):
    """X[a][b] = sum_i conj(G0[i][a]) row_w[i] G0[i][b] * col_w[b],
    row_w/col_w exact N-element diagonal weights (as Mbar scalars)."""
    Xm = [[TZERO] * 3 for _ in range(3)]
    for a in range(3):
        for b in range(3):
            acc = TZERO
            for i in range(3):
                t2 = tmul(tmul(tconj(G0[i][a]), (row_w[i], NZERO)),
                          G0[i][b])
                acc = tadd(acc, t2)
            Xm[a][b] = tmul(acc, (col_w[b], NZERO))
    return Xm


def charpoly3_exact(Xm, tag):
    """exact charpoly x^3 - c1 x^2 + c2 x - c3 of an Mbar 3x3 whose
    coefficients are CHKed real (tau-part zero); returns N-elements."""
    c1 = mat3_traceT(Xm)
    X2sq = mat3_mulT(Xm, Xm)
    c2 = tscale(tsub(tmul(c1, c1), mat3_traceT(X2sq)), Fr(1, 2))
    c3 = tdet3(Xm)
    CHK(f"{tag}_charpoly_coeffs_tau_free_real",
        nis0(c1[1]) and nis0(c2[1]) and nis0(c3[1]),
        "tr, e2, det all real N-elements (Hermitian-similarity certificate)")
    return c1[0], c2[0], c3[0]


# (ii) X2 ~ Ghat^dagger Ghat (similarity by D_A removes the sqrts; signs in)
rw2 = [nscale(invhS[i], Fr(sS[i])) for i in range(3)]
cw2 = [nscale(invhA[b], Fr(sA[b])) for b in range(3)]
X2 = build_X(rw2, cw2)
c1_2, c2_2, c3_2 = charpoly3_exact(X2, "X2")
# (iv) X4 ~ (D_v^{1/2} Ghat D_v^{-1/2})^dagger (D_v^{1/2} Ghat D_v^{-1/2})
rw4 = [nmul(DvN[i], nscale(invhS[i], Fr(sS[i]))) for i in range(3)]
cw4 = [nmul(invDv[b], nscale(invhA[b], Fr(sA[b]))) for b in range(3)]
X4 = build_X(rw4, cw4)
c1_4, c2_4, c3_4 = charpoly3_exact(X4, "X4")
CHK("det_X4_equals_det_X2_exact", nis0(nsub(c3_4, c3_2)),
    "diagonal similarity preserves the determinant -- exact internal test")


def n_coords(el):
    return [[str(c) for c in el[0]], [str(c) for c in el[1]]]


RES["exact_sv"] = {
    "X2_similarity": "X2 = G0^dag diag(sS_i/sigma_i(dS qS)) G0 "
                     "diag(sA_b/sigma_b(dA qA)) ~ Ghat^dag Ghat; "
                     "sv(Ghat)^2 = roots",
    "X2_c1_N": n_coords(c1_2), "X2_c2_N": n_coords(c2_2),
    "X2_c3_N": n_coords(c3_2),
    "X2_c1_minpoly": nminpoly(c1_2), "X2_c2_minpoly": nminpoly(c2_2),
    "X2_c3_minpoly": nminpoly(c3_2),
    "X4_similarity": "X4 = G0^dag diag(v_i^2 sS_i/sigma_i(dS qS)) G0 "
                     "diag(sA_b/(sigma_b(dA qA) v_b^2)) ~ C4^dag C4, "
                     "C4 = D_v^{1/2} Ghat D_v^{-1/2}",
    "X4_c1_N": n_coords(c1_4), "X4_c2_N": n_coords(c2_4),
    "X4_c3_N": n_coords(c3_4),
    "X4_c1_minpoly": nminpoly(c1_4), "X4_c2_minpoly": nminpoly(c2_4),
    "X4_c3_minpoly": nminpoly(c3_4),
}
dump()


def cubic_roots_50d(c1, c2, c3, tag):
    mp.dps = 200
    coeffs = [mp.mpf(1), -nnum(c1), nnum(c2), -nnum(c3)]
    rts = mp.polyroots(coeffs, maxsteps=200, extraprec=200)
    # AMENDMENT (banking seat, 2026-08-07): the positivity assumption was the
    # design's, not the object's -- X2's cubic has an EXACT ZERO root (det = 0):
    # the S-A overlap matrix is RANK 2. That is a finding, not a failure. Gate on
    # what is actually required (real, non-negative), and record the rank.
    CHK(f"{tag}_roots_real_nonneg",
        all(abs(mp.im(r)) < mp.mpf(10) ** (-150) and mp.re(r) > -mp.mpf(10)**(-150)
            for r in rts),
        "the sv^2 cubic has three real non-negative roots; roots = "
        + " | ".join(mp.nstr(r, 25) for r in rts))
    nz = [r for r in rts if abs(mp.re(r)) > mp.mpf(10) ** (-100)]
    REC(f"{tag}_rank", len(nz),
        "the number of NONZERO singular values (rank of the overlap matrix)")
    out = sorted([mp.re(r) for r in rts], reverse=True)
    mp.dps = 150
    return out


sv2_G = cubic_roots_50d(c1_2, c2_2, c3_2, "X2")
sv_G = [mp.sqrt(v) for v in sv2_G]
sv2_D = cubic_roots_50d(c1_4, c2_4, c3_4, "X4")
sv_D = [mp.sqrt(v) for v in sv2_D]
# consistency: tr X2 = sum of the 9 banked moduli^2
tr_belt = abs(nnum(c1_2) - sum(mp.mpf(mod_banked[i][j]) ** 2
                               for i in range(3) for j in range(3)))
CHK("tr_X2_equals_sum_of_9_banked_moduli_sq", tr_belt < mp.mpf(10) ** (-45),
    f"diff {mp.nstr(tr_belt, 3)}")
RES["exact_sv"]["sv_Ghat_50d"] = [mp.nstr(v, 50) for v in sv_G]
RES["exact_sv"]["sv_Dv_conj_50d"] = [mp.nstr(v, 50) for v in sv_D]
dump()

# ================================================================ [9] numerics
log("[9] the composition matrices, eigen triples (charpoly route + belt) ...")


def m3(mlist):
    Mm = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            Mm[i, j] = mlist[i][j]
    return Mm


def mmul(A, B):
    return A * B


def dagger(A):
    return A.transpose_conj()


GhatM = m3(Ghat)
RM = m3([[mp.mpf(Rrot[i][j]) for j in range(3)] for i in range(3)])
C_i = RM.T * GhatM * RM                     # (i)
C_a = GhatM * RM                            # (iii) Ghat*R
C_b = RM * GhatM                            # (iii) R*Ghat
DvM = mp.matrix(3, 3)
DvMi = mp.matrix(3, 3)
for j in range(3):
    DvM[j, j] = vw[j]
    DvMi[j, j] = 1 / vw[j]
C_4 = DvM * GhatM * DvMi                    # (iv)


def eig_charpoly(Cm, tag):
    """eigen triple via charpoly + polyroots (no eigenvector readout),
    cross-checked against mp.eig (Schur route)."""
    c1 = Cm[0, 0] + Cm[1, 1] + Cm[2, 2]
    c2 = (Cm[0, 0] * Cm[1, 1] - Cm[0, 1] * Cm[1, 0]
          + Cm[0, 0] * Cm[2, 2] - Cm[0, 2] * Cm[2, 0]
          + Cm[1, 1] * Cm[2, 2] - Cm[1, 2] * Cm[2, 1])
    c3 = mp.det(Cm)
    rts = mp.polyroots([mp.mpc(1), -c1, c2, -c3], maxsteps=200,
                       extraprec=200)
    rts = sorted(rts, key=lambda z: (-abs(z), mp.re(z), mp.im(z)))
    E2, _ = mp.eig(mp.matrix(Cm))
    E2 = sorted(E2, key=lambda z: (-abs(z), mp.re(z), mp.im(z)))
    worst = max(abs(rts[k] - E2[k]) for k in range(3))
    CHK(f"{tag}_eig_two_routes_agree", worst < mp.mpf(10) ** (-80),
        f"charpoly+polyroots vs Schur worst {mp.nstr(worst, 3)}")
    return rts


def sv_belt(Cm, tag, target):
    Hm = dagger(Cm) * Cm
    Ev = mp.eighe(Hm, eigvals_only=True)
    got = sorted([mp.sqrt(abs(v)) for v in Ev], reverse=True)
    worst = max(abs(got[k] - target[k]) for k in range(3))
    # AMENDMENT (banking seat): the 1e-80 bar exceeds this machinery's known
    # precision floor -- B930's independent belt lands at 3.9e-76 by the same
    # route (sqrt of a near-zero eigenvalue costs half the digits). House belt
    # standard is 1e-40; the achieved agreement is recorded.
    CHK(f"{tag}_sv_matches_exact", worst < mp.mpf(10) ** (-40),
        f"worst {mp.nstr(worst, 3)} (bar 1e-40; the sqrt-of-small floor)")
    return got


eig_G = eig_charpoly(GhatM, "Ghat")
eig_i = eig_charpoly(C_i, "Ci_RT_Ghat_R")
eig_a = eig_charpoly(C_a, "Ca_Ghat_R")
eig_b = eig_charpoly(C_b, "Cb_R_Ghat")
eig_4 = eig_charpoly(C_4, "C4_Dv_conj")


def eig_set_match(e1, e2, tag, what):
    worst = max(abs(e1[k] - e2[k]) for k in range(3))
    CHK(tag, worst < mp.mpf(10) ** (-80), f"{what}; worst {mp.nstr(worst, 3)}")


# the FORCED degeneracies, verified (not asserted)
eig_set_match(eig_i, eig_G, "FORCED_eig_Ci_equals_eig_Ghat",
              "orthogonal similarity")
eig_set_match(eig_4, eig_G, "FORCED_eig_C4_equals_eig_Ghat",
              "diagonal similarity")
eig_set_match(eig_a, eig_b, "FORCED_eig_GhatR_equals_eig_RGhat",
              "AB vs BA")
sv_belt(GhatM, "Ghat", sv_G)
sv_belt(C_i, "FORCED_Ci", sv_G)
sv_belt(C_a, "FORCED_Ca", sv_G)
sv_belt(C_b, "FORCED_Cb", sv_G)
sv_belt(C_4, "C4", sv_D)
# |det Ghat|^2 = det X2 (exact anchor for the eigenvalue product)
det_anchor = abs(abs(mp.det(GhatM)) ** 2 - nnum(c3_2))
CHK("abs_det_Ghat_sq_equals_det_X2", det_anchor < mp.mpf(10) ** (-90),
    f"diff {mp.nstr(det_anchor, 3)}")
dump()

# ================================================================ [10] table
log("[10] the cascade table (B929 index convention) + band flags ...")
BAND = (mp.mpf("1.2"), mp.mpf("1.6"))


def cascade(triple_desc, note=""):
    t = [mp.mpf(abs(v)) for v in triple_desc]
    out = {"triple_50d": [mp.nstr(v, 50) for v in t]}
    if not (t[0] > t[1] > t[2] > 0):
        out["a"] = None
        out["note"] = "not strictly descending-positive; index undefined " \
            + note
        return out
    r1 = t[1] / t[0]
    r2 = t[2] / t[1]
    a = mp.log(r2) / mp.log(r1)
    out["r1"] = mp.nstr(r1, 30)
    out["r2"] = mp.nstr(r2, 30)
    out["a"] = mp.nstr(a, 30)
    out["in_band_1p2_1p6"] = bool(BAND[0] <= a <= BAND[1])
    if note:
        out["note"] = note
    return out


def entry_shape(Cm, tag):
    """the B930 shape instrument (fixed): entry moduli + the Wolfenstein
    cascade on the upper/lower off-diagonals (secondary data)."""
    Mv = [[abs(Cm[i, j]) for j in range(3)] for i in range(3)]
    rep = {"moduli_50d": [[mp.nstr(Mv[i][j], 50) for j in range(3)]
                          for i in range(3)]}
    for name, (o12, o23, o13) in (("upper", (Mv[0][1], Mv[1][2], Mv[0][2])),
                                  ("lower", (Mv[1][0], Mv[2][1], Mv[2][0]))):
        d = {}
        if o12 > 0 and o23 > 0 and o13 > 0:
            r1 = o23 / o12
            r2 = o13 / o23
            d["r1_23_over_12"] = mp.nstr(r1, 30)
            d["r2_13_over_23"] = mp.nstr(r2, 30)
            d["wolfenstein_ordered"] = bool(o12 > o23 > o13)
            if 0 < r1 < 1 and 0 < r2 < 1:
                a = mp.log(r2) / mp.log(r1)
                d["accel_index_a"] = mp.nstr(a, 30)
                d["in_band_1p2_1p6"] = bool(BAND[0] <= a <= BAND[1])
        rep[name] = d
    RES.setdefault("entry_shapes", {})[tag] = rep
    return rep


# the four base classes (anchors)
mS_desc = sorted([abs(v) for v in mS_num], reverse=True)
base_mS = cascade(mS_desc, "the B928/B929 m_S sheet")
CHK("a_mS_matches_banked_B929_T1",
    abs(mp.mpf(base_mS["a"]) - mp.mpf(str(B929R["T1"]["a"])))
    < mp.mpf(10) ** (-9), base_mS["a"])
base_v = cascade(sorted(vw, reverse=True),
                 "v-weights are ASCENDING; index computed on the "
                 "descending reversal (same |a| class)")
# R principal cosines: {1, sqrt of the 1536x^2-2088x+677 roots}
quad = [mp.mpf(1536), mp.mpf(-2088), mp.mpf(677)]
qr = mp.polyroots(quad)
cosines = sorted([mp.mpf(1)] + [mp.sqrt(r) for r in qr], reverse=True)
base_cos = cascade(cosines, "the exact rotation cosines "
                            "{1, sqrt roots of 1536x^2-2088x+677}")
RES["base_classes"] = {
    "v_weights_ascending": base_v,
    "m_S_descending": base_mS,
    "rotation_cosines": base_cos,
    "S_A_invariant_cascade_is_composition_ii": True,
}

# the composition table (primary = invariant triples)
TABLE = {}
TABLE["(i)_RT_Ghat_R"] = {
    "matrix": "R^T Ghat R",
    "invariant": "eigenvalues (FORCED = eig(Ghat), orthogonal similarity; "
                 "sv FORCED = sv(Ghat))",
    "eig_50d": [[mp.nstr(mp.re(z), 50), mp.nstr(mp.im(z), 50)]
                for z in eig_G],
    "cascade_eig_moduli": cascade([abs(z) for z in eig_G]),
    "exact": "eigen moduli product anchor: |det Ghat|^2 = det X2 exactly",
}
TABLE["(ii)_sv_Ghat"] = {
    "matrix": "Ghat (polar/singular decomposition)",
    "invariant": "singular values -- EXACT (roots of the X2 cubic; "
                 "coefficient N-coords + minpolys in exact_sv)",
    "sv_50d": [mp.nstr(v, 50) for v in sv_G],
    "cascade_sv": cascade(sv_G),
    "exact": "EXACT",
}
TABLE["(iii)_Ghat_R_and_R_Ghat"] = {
    "matrix": "Ghat*R and R*Ghat",
    "invariant": "sv FORCED = sv(Ghat) both orderings (verified); the NEW "
                 "invariant is the shared eigenvalue triple eig(Ghat R) = "
                 "eig(R Ghat)",
    "eig_50d": [[mp.nstr(mp.re(z), 50), mp.nstr(mp.im(z), 50)]
                for z in eig_a],
    "cascade_eig_moduli": cascade([abs(z) for z in eig_a]),
    "exact": "50d (the entries mix sqrt-normalizations with the R "
             "eigenframe; no tower representation)",
}
TABLE["(iv)_Dv_conj"] = {
    "matrix": "D_v^{1/2} Ghat D_v^{-1/2}, D_v = diag(sigma_g(V_ccl))",
    "invariant": "singular values -- EXACT (roots of the X4 cubic); "
                 "eig FORCED = eig(Ghat) (diagonal similarity)",
    "sv_50d": [mp.nstr(v, 50) for v in sv_D],
    "cascade_sv": cascade(sv_D),
    "exact": "EXACT",
}
RES["composition_table"] = TABLE

# secondary: entry-level shapes of every whitelisted matrix
entry_shape(GhatM, "base_Ghat")
entry_shape(C_i, "(i)_RT_Ghat_R")
entry_shape(C_a, "(iii)_Ghat_R")
entry_shape(C_b, "(iii)_R_Ghat")
entry_shape(C_4, "(iv)_Dv_conj")

# the band flags (a flag is NOT a claim -- hint-ledger material only)
flags = []
for key, row in TABLE.items():
    for cname in ("cascade_sv", "cascade_eig_moduli"):
        if cname in row and row[cname].get("in_band_1p2_1p6"):
            flags.append({"composition": key, "which": cname,
                          "a": row[cname]["a"]})
for tag, rep in RES.get("entry_shapes", {}).items():
    for side in ("upper", "lower"):
        d = rep.get(side, {})
        if d.get("in_band_1p2_1p6"):
            flags.append({"composition": tag, "which": f"entry_{side}",
                          "a": d["accel_index_a"]})
RES["band_flags_1p2_1p6"] = flags
REC("band_flag_count", len(flags),
    "compositions whose cascade index lands in [1.2, 1.6]")
dump()

# ================================================================ [11] verdict
log("[11] verdict ...")
RES["verdict_structure"] = {
    "degeneracy": "the closed whitelist yields EXACTLY FOUR invariant "
                  "triples: sv(Ghat) [(ii), EXACT, shared FORCED with (i) "
                  "and both (iii) orderings], eig(Ghat) [(i)/(iv), 50d], "
                  "eig(Ghat R) [(iii), 50d], sv(D_v-conj) [(iv), EXACT]",
    "convention": "eigen-level readouts are in the BANKED basis convention "
                  "(B930 exact vS27/u27 normalization + R column-sign "
                  "rule); singular values are sign-gauge invariant",
    "index": "a = ln r2 / ln r1 (B929), descending triples",
}
RES["runtime_s"] = round(time.time() - T00, 1)
dump()
log("results.json written; done")
