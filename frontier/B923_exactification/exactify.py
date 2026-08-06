#!/usr/bin/env python3
"""B923 -- V-L2 REMAINDER: the colored sector exact + the pipeline link exact.

WHAT THIS CELL DELIVERS (everything exact unless labeled numeric):
  (1) THE COLORED SECTOR EXACT.  The six 3-dim colored atoms are built in
      characteristic 0 as joint eigenspaces of the SAME rational commuting
      charge family (R8, R14, R16, R22 on the banked B883 27) used for the
      colorless nine (B908/B914).  Structure found and certified:
        charpoly(Mc) = h_S * h_A * h_col^3;  the colored sextic h_col is
        the K-norm form of ONE quadratic  x^2 + p x + q,  p, q in
        K = Q[rho]/mu13 (certified: sigma_0(quad) sigma_1(quad)
        sigma_2(quad) = h_col as an exact polynomial identity in N[x]);
        disc = p^2 - 4q = -231 w_c^2 with w_c in K -- NOT the colorless
        -3 w^2 mechanism: the colored sector opens the quadratic extension
        K(omega), omega = sqrt(-231) = sqrt(77) * tau.  231 = 3 * 77: the
        KUMMER FIELD F = Q(sqrt77, sqrt-3) of the value arc (B910/B918)
        appears INSIDE the object's colored sector.  Because mu13 is in
        the sqrt77 family, sqrt(77) = sqrt(disc mu)/rational is ALREADY an
        element S77 of the splitting field N (delta = prod (r_i - r_j),
        delta^2 = 77 * rational^2, certified exactly), so the six colored
        Mc-eigenvalues theta_{g,+-} = (-p +- w_c omega)/2 and the whole
        colored sector STILL live in Mbar = N(tau) -- through the sqrt77
        route, no new field.
        The 3-dim eigenspace of C18 - theta is computed ONCE over the
        abstract field K(omega); the four charges act as SCALARS on it
        (certified exactly, all 4 ops x 3 basis vectors x 27 coordinates);
        the six embedded atoms match B912's colored atoms bijectively via
        their exact joint eigenvalues (numeric identification, dps 60).
  (2) CCC EXACT, BOTH GAUGES.  The banked B883 cubic restricted to the two
      CCC triples (one atom from each generation; the two triples are the
      two global tau-branches), contracted with inverse H-Grams
      (the basis-free coupling invariant |T|^2_G of the relay pipeline):
        tau-twisted gauge H' = H+ D2 (the transported solo M, B916):
                                    CCC = +13824/953 = 3! * 2304/953
        canonical gauge  H+ (charge-equivariant, B912):  CCC = -6,
                                    |CCC| = 6 = 3! * 1
      i.e. CCC = 3! * lambda IS AN IDENTITY in both gauges (lambda =
      2304/953 and lambda = 1 are the banked exact lambdas of B916/B917);
      the canonical sign -1 is the same negative-q-product structure as
      B916's c^2 = -(q q q) unimodularity identity.
  (3) THE PIPELINE LINK EXACT.  The three diagonal CCl invariants
      (C_g+, C_g-, S_g) are the sigma_g-images of ONE abstract element
      V_ccl of K (the entire diagonal computation is generation-free over
      K(tau)); certified:
        953^4 * charpoly_Q(mult-by-V_ccl) = HIER exactly, and
        V_ccl = B918's exact K-root V(rho) of HIER coefficient-for-
        coefficient.  Hence  {v_g^2} = {roots of HIER}  AS AN IDENTITY --
        the last numeric link of the value arc (7.3e-88) is closed.
      DISCOVERY: in the CANONICAL gauge the same diagonal invariant is
      the RATIONAL -3, identical for all three generations -- the
      hierarchy cubic collapses to (x+3)^3.  The ENTIRE generation
      hierarchy is carried by the Hermitian twist D2 (H' vs H+), not by
      the atoms or the cubic.
      The six off-diagonal CCl invariants satisfy
        CI(i,j)^2 = sigma_i(V_ccl) * sigma_j(V_ccl)   exactly
      (the v_i v_j product table), and the branch identity (ascending
      rho_g <-> ascending v_g^2) plus the 95-digit belt anchors are
      reproduced numerically at dps 110.

GATE 5: structure only; no experimental number enters or is compared.

Env: SESSION_SCRATCH optional (cache + isolated-exec cwd); falls back to a
fresh temp dir.  Paths repo-relative from this file.  Output: results.json.
"""
import io, os, json, math, time, pickle, tempfile, contextlib, itertools
from fractions import Fraction as Fr
from collections import Counter
import sympy as sp
import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b923_")
os.makedirs(SCRATCH, exist_ok=True)
T00 = time.time()
RES = {"cell": "B923 V-L2 exactification: colored sector + pipeline link",
       "checks": {}, "notes": []}


def log(*a):
    print(f"[{time.time()-T00:7.1f}s]", *a, flush=True)


def CHK(name, ok, detail=""):
    RES["checks"][name] = {"pass": bool(ok), "detail": str(detail)}
    log(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        RES["verdict"] = "UNSTABLE"
        json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)
        raise SystemExit(f"UNSTABLE at {name}")


# ================================================================ K = Q[rho]/mu13
MU = [500716339200, -2075673600, -4769856, 2197]          # mu13 descending (banked)
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
        c0 += c4 * R4K[0]; c1 += c4 * R4K[1]; c2 += c4 * R4K[2]
    if c3:
        c0 += c3 * R3K[0]; c1 += c3 * R3K[1]; c2 += c3 * R3K[2]
    return (c0, c1, c2)


def kadd(x, y): return (x[0] + y[0], x[1] + y[1], x[2] + y[2])
def ksub(x, y): return (x[0] - y[0], x[1] - y[1], x[2] - y[2])
def kscale(x, s): return (x[0] * s, x[1] * s, x[2] * s)
def kis0(x): return not (x[0] or x[1] or x[2])


def kinv(x):
    cols = [kmul(x, KONE), kmul(x, (Fr(0), Fr(1), Fr(0))), kmul(x, (Fr(0), Fr(0), Fr(1)))]
    Aug = [[cols[j][i] for j in range(3)] + [Fr(1) if i == 0 else Fr(0)] for i in range(3)]
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


# ---------------------------------------------------------------- N = splitting algebra
b_mu = Fr(MU[1], MU[0]); c_mu = Fr(MU[2], MU[0])
P_N = (b_mu, Fr(1), Fr(0))
Q_N = (c_mu, b_mu, Fr(1))
NZERO = (KZERO, KZERO)
NONE_ = (KONE, KZERO)


def nmul(a, b):
    a0, a1 = a; b0, b1 = b
    x00 = kmul(a0, b0); x11 = kmul(a1, b1)
    x01 = kadd(kmul(a0, b1), kmul(a1, b0))
    return (ksub(x00, kmul(x11, Q_N)), ksub(x01, kmul(x11, P_N)))


def nadd(a, b): return (kadd(a[0], b[0]), kadd(a[1], b[1]))
def nsub(a, b): return (ksub(a[0], b[0]), ksub(a[1], b[1]))
def nscale(a, s): return (kscale(a[0], s), kscale(a[1], s))
def nis0(a): return kis0(a[0]) and kis0(a[1])


def ninv(a):
    x, y = a
    det = kadd(ksub(kmul(x, x), kmul(kmul(P_N, x), y)), kmul(Q_N, kmul(y, y)))
    di = kinv(det)
    return (kmul(ksub(x, kmul(P_N, y)), di), kscale(kmul(y, di), Fr(-1)))


def sigma(j, x):
    """the embedding K -> N, rho -> r_j (r1 = rho1, r2 = rho2, r3 = -b-rho1-rho2)."""
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


# ---------------------------------------------------------------- Mbar = N[tau]/(tau^2+3)
class TR:
    def mul(self, a, b):
        X = nsub(nmul(a[0], b[0]), nscale(nmul(a[1], b[1]), Fr(3)))
        Y = nadd(nmul(a[0], b[1]), nmul(a[1], b[0]))
        return (X, Y)
    def add(self, a, b): return (nadd(a[0], b[0]), nadd(a[1], b[1]))
    def sub(self, a, b): return (nsub(a[0], b[0]), nsub(a[1], b[1]))
    def scale(self, a, s): return (nscale(a[0], s), nscale(a[1], s))
    def is0(self, a): return nis0(a[0]) and nis0(a[1])
    def conj(self, a): return (a[0], nscale(a[1], Fr(-1)))
    def inv(self, a):
        nrm = nadd(nmul(a[0], a[0]), nscale(nmul(a[1], a[1]), Fr(3)))
        ni = ninv(nrm)
        return (nmul(a[0], ni), nscale(nmul(a[1], ni), Fr(-1)))


T = TR()
TZERO = (NZERO, NZERO)
TONE = (NONE_, NZERO)


# ------------------------------------------- F = K(omega), omega^2 = -231, abstract
FTZERO = (KZERO, KZERO)
FTONE = (KONE, KZERO)


def ftmul(a, b):
    return (ksub(kmul(a[0], b[0]), kscale(kmul(a[1], b[1]), Fr(231))),
            kadd(kmul(a[0], b[1]), kmul(a[1], b[0])))


def ftadd(a, b): return (kadd(a[0], b[0]), kadd(a[1], b[1]))
def ftsub(a, b): return (ksub(a[0], b[0]), ksub(a[1], b[1]))
def ftscale(a, s): return (kscale(a[0], s), kscale(a[1], s))
def ftscaleK(a, kx): return (kmul(a[0], kx), kmul(a[1], kx))
def ftis0(a): return kis0(a[0]) and kis0(a[1])
def ftconj(a): return (a[0], kscale(a[1], Fr(-1)))


def ftinv(a):
    nrm = kadd(kmul(a[0], a[0]), kscale(kmul(a[1], a[1]), Fr(231)))
    ni = kinv(nrm)
    return (kmul(a[0], ni), kscale(kmul(a[1], ni), Fr(-1)))


def ftemb(g, a):
    """embed the abstract K(omega) element into Mbar via sigma_g,
    omega -> S77 * tau  (S77 in N, S77^2 = 77, built from sqrt(disc mu))."""
    return (sigma(g, a[0]), nmul(sigma(g, a[1]), S77))


# ---------------------------------------------------------------- Q linear algebra
def qkernel(M):
    m, n = len(M), len(M[0])
    A = [row[:] for row in M]
    piv = []; rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if A[r][c] != 0), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = A[rr][c]
        A[rr] = [e / iv for e in A[rr]]
        for r in range(m):
            if r != rr and A[r][c]:
                f = A[r][c]
                A[r] = [A[r][j] - f * A[rr][j] for j in range(n)]
        piv.append(c); rr += 1
    ker = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -A[i][fc]
        ker.append(v)
    return ker


def qsolve_span(basis, vec):
    k, n = len(basis), len(basis[0])
    Aug = [[basis[j][i] for j in range(k)] + [vec[i]] for i in range(n)]
    piv = []; rr = 0
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
        piv.append(c); rr += 1
    sol = [Fr(0)] * k
    for i, c in enumerate(piv):
        sol[c] = Aug[i][k]
    for i in range(n):
        if sum(sol[j] * basis[j][i] for j in range(k)) != vec[i]:
            return None
    return sol


def matmulQ(X, Y):
    n = len(X); m = len(Y[0]); kk = len(Y)
    return [[sum(X[i][t] * Y[t][j] for t in range(kk) if X[i][t]) for j in range(m)]
            for i in range(n)]


# ---------------------------------------------------------------- numeric-guided finders
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


def _kev_num(x, r):
    return (mp.mpf(x[0].numerator) / mp.mpf(x[0].denominator)
            + (mp.mpf(x[1].numerator) / mp.mpf(x[1].denominator)) * r
            + (mp.mpf(x[2].numerator) / mp.mpf(x[2].denominator)) * r * r)


def _interp_K(vals, mu_roots, maxden, hmax):
    M3 = mp.matrix(3, 3)
    for i in range(3):
        M3[i, 0] = 1; M3[i, 1] = mu_roots[i]; M3[i, 2] = mu_roots[i] ** 2
    try:
        sol = mp.lu_solve(M3, mp.matrix(vals))
    except Exception:
        return None
    cand = []
    for v in sol:
        r = _ratrec_real(v, maxden)
        if r is None or max(abs(r.numerator), r.denominator) > hmax:
            return None
        cand.append(r)
    return tuple(cand)


def root_in_K(h_coeffs, dps=400, hmax=10 ** 120):
    mu_roots = _mu_roots_numeric(dps)
    hh = [mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q) for c in h_coeffs]
    h_roots = mp.polyroots(hh, maxsteps=400, extraprec=400)
    reals = [mp.re(r) for r in h_roots if abs(mp.im(r)) < mp.mpf(10) ** (-dps // 2)]
    maxden = mp.mpf(10) ** (dps // 3)
    for pick in itertools.permutations(range(len(reals)), 3):
        cand = _interp_K([reals[pick[j]] for j in range(3)], mu_roots, maxden, hmax)
        if cand is None:
            continue
        acc = (Fr(sp.Rational(h_coeffs[0]).p, sp.Rational(h_coeffs[0]).q), Fr(0), Fr(0))
        for c in h_coeffs[1:]:
            acc = kmul(acc, cand)
            acc = (acc[0] + Fr(sp.Rational(c).p, sp.Rational(c).q), acc[1], acc[2])
        if kis0(acc):
            return cand
    return None


def sqrt_in_K(target, dps=400, hmax=10 ** 120):
    mu_roots = _mu_roots_numeric(dps)
    tv = [_kev_num(target, r) for r in mu_roots]
    if any(t < 0 for t in tv):
        return None
    sq = [mp.sqrt(t) for t in tv]
    maxden = mp.mpf(10) ** (dps // 3)
    for signs in itertools.product((1, -1), repeat=2):
        vals = [sq[0], signs[0] * sq[1], signs[1] * sq[2]]
        cand = _interp_K(vals, mu_roots, maxden, hmax)
        if cand is None:
            continue
        if kis0(ksub(kmul(cand, cand), target)):
            return cand
    return None


# ================================================================ [1] base: B854 INV
log("[1] B854 invariants (isolated exec, scratch cwd; cached)...")
cache = os.path.join(SCRATCH, "b914_base_cache.pkl")
if os.path.exists(cache):
    INV, ns = pickle.load(open(cache, "rb"))
else:
    cwd = os.getcwd()
    g6 = {"__file__": os.path.join(SCRATCH, "e6_centralizer.py"), "__name__": "b854_frame"}
    src = open(os.path.join(REPO, "frontier", "B854_centralizer_exact",
                            "e6_centralizer.py")).read()
    try:
        os.chdir(SCRATCH)
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, "b854", "exec"), g6)
    finally:
        os.chdir(cwd)
    ns = g6["ns"]
    INV = {n: [Fr(c.numerator, c.denominator) for c in g6["INV"][n]] for n in ns}
    pickle.dump((INV, ns), open(cache, "wb"))
CHK("base_ns_8_14_16_22", sorted(ns) == [8, 14, 16, 22])

# ================================================================ [2] the B883 27
log("[2] B883 rep27 (banked) + the four exact charge matrices...")
REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
REP = [[[int(x) for x in row] for row in REPJ["rep"][str(k)]] for k in range(78)]
WT = [tuple(REP[i][a][a] for i in range(6)) for a in range(27)]
CHK("rep27_cartan_diagonal_27_distinct_weights",
    all(all(REP[i][a][b] == 0 for a in range(27) for b in range(27) if a != b)
        for i in range(6)) and len(set(WT)) == 27)
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
CHK("four_charges_commute_exactly_over_Q",
    all(matmulQ(Rex[a], Rex[b]) == matmulQ(Rex[b], Rex[a])
        for i, a in enumerate(ns) for b in ns[i + 1:]))

# ================================================================ [3] the two gauges
log("[3] H+ (B912) + the tau-twisted H' = H+ D2 (B916)...")
B912 = json.load(open(os.path.join(REPO, "frontier", "B912_norm_cell", "results.json")))
piW = B912["H_plus_support_pi"]
cbP = B912["H_plus_entries_c_b"]
CHK("H_plus_signed_permutation_symmetric",
    sorted(piW) == list(range(27)) and all(abs(c) == 1 for c in cbP)
    and all(piW[piW[b]] == b and cbP[piW[b]] == cbP[b] for b in range(27)))
pinv = [0] * 27
for b in range(27):
    pinv[piW[b]] = b
EPS = {8: -1, 14: 1, 16: -1, 22: 1}
ok = True
for n in ns:
    R = Rex[n]
    for a in range(27):
        for b in range(27):
            v = R[piW[b]][a] * cbP[b] + EPS[n] * cbP[pinv[a]] * R[pinv[a]][b]
            if v != 0:
                ok = False
CHK("H_plus_charge_equivariance_exact", ok, "eps = (-1,+1,-1,+1)")
B916 = json.load(open(os.path.join(REPO, "frontier", "B916_lambda_bridge",
                                   "results.json")))
D2 = [int(d) for d in B916["H_prime_diag_vs_H_plus"]["D2"]]
CHK("D2_pm1_pi_symmetric_11_flips",
    all(abs(d) == 1 for d in D2) and all(D2[piW[b]] == D2[b] for b in range(27))
    and D2.count(-1) == 11)
cb2 = [cbP[b] * D2[b] for b in range(27)]          # the tau-twisted gauge H'
GAUGES = {"canonical_Hplus": cbP, "tau_twisted_Hprime": cb2}

# ================================================================ [4] the invariant cubic
log("[4] the invariant cubic on the B883 27 (exact kernel + 78-generator verify)...")
wz = [t for t in itertools.combinations_with_replacement(range(27), 3)
      if all(WT[t[0]][i] + WT[t[1]][i] + WT[t[2]][i] == 0 for i in range(6))]
CHK("weight_zero_triples_45", len(wz) == 45 and all(a < b < c for a, b, c in wz))
tidx = {t: i for i, t in enumerate(wz)}
rows_eq = {}
for k in range(78):
    Rk = REP[k]
    rownz = [[(i, Rk[l][i]) for i in range(27) if Rk[l][i]] for l in range(27)]
    for t in wz:
        for perm in set(itertools.permutations(t)):
            x, y, z = perm
            for (i, v) in rownz[x]:
                key = (k, tuple(sorted((i, y, z))))
                rows_eq.setdefault(key, [Fr(0)] * 45)[tidx[t]] += v
            for (i, v) in rownz[y]:
                key = (k, tuple(sorted((x, i, z))))
                rows_eq.setdefault(key, [Fr(0)] * 45)[tidx[t]] += v
            for (i, v) in rownz[z]:
                key = (k, tuple(sorted((x, y, i))))
                rows_eq.setdefault(key, [Fr(0)] * 45)[tidx[t]] += v
eqm = [r for r in rows_eq.values() if any(r)]
ker = qkernel(eqm)
CHK("cubic_equivariance_kernel_dim_1", len(ker) == 1)
cub = ker[0]
den = 1
for x in cub:
    den = den * x.denominator // math.gcd(den, x.denominator)
cubi = [int(x * den) for x in cub]
g = 0
for v in cubi:
    g = math.gcd(g, abs(v))
cubi = [v // g for v in cubi]
if cubi[0] < 0:
    cubi = [-v for v in cubi]
CHK("cubic_support_45_coeffs_pm1", all(abs(v) == 1 for v in cubi))
TRIP, COEF = wz, cubi
B914 = json.load(open(os.path.join(REPO, "frontier", "B914_ratio_table",
                                   "results.json")))
CHK("cubic_equals_banked_B914_cubic",
    [list(t) for t in TRIP] == B914["cubic_B883"]["triples"]
    and COEF == B914["cubic_B883"]["coeffs"])
T3 = {}
for t, cf in zip(TRIP, COEF):
    for perm in set(itertools.permutations(t)):
        T3[perm] = Fr(cf)
ok = True
for k in range(78):
    Rk = REP[k]
    rownz = [[(i, Rk[l][i]) for i in range(27) if Rk[l][i]] for l in range(27)]
    acc2 = {}
    for (x, y, z), v in T3.items():
        for (i, w) in rownz[x]:
            acc2[(i, y, z)] = acc2.get((i, y, z), Fr(0)) + w * v
        for (i, w) in rownz[y]:
            acc2[(x, i, z)] = acc2.get((x, i, z), Fr(0)) + w * v
        for (i, w) in rownz[z]:
            acc2[(x, y, i)] = acc2.get((x, y, i), Fr(0)) + w * v
    if any(v != 0 for v in acc2.values()):
        ok = False
        break
CHK("cubic_exact_derivation_identity_all_78_generators", ok)

# ================================================================ [5] colorless atoms
log("[5] the exact colorless atoms (B914/B908 route (a), re-run)...")
CO = {8: 3, 14: 7, 16: 13, 22: 17}
Mc = [[sum(Fr(CO[n]) * Rex[n][i][j] for n in ns) for j in range(27)] for i in range(27)]
x = sp.Symbol("x")
cp = sp.Matrix(27, 27, lambda i, j: sp.Rational(Mc[i][j].numerator,
                                                Mc[i][j].denominator)).charpoly(x)
fl = sp.factor_list(cp.as_expr())
facs = sorted([(sp.degree(f, x), m, sp.Poly(f, x)) for f, m in fl[1]])
CHK("charpoly_Mc_factors_3_1__6_1__6_3",
    [(d, m) for d, m, _ in facs] == [(3, 1), (6, 1), (6, 3)])
h_S = [int(c) for c in facs[0][2].all_coeffs()]
h_A = [int(c) for c in facs[1][2].all_coeffs()]
h_col = [int(c) for c in facs[2][2].all_coeffs()]
RES["h_col_ints"] = [str(c) for c in h_col]
CHK("h_col_irreducible_over_Q_squarefree",
    facs[2][2].is_irreducible and sp.gcd(facs[2][2],
                                         facs[2][2].diff(x)).degree() == 0,
    "sextic, multiplicity 3 in charpoly")


def poly_mat(coeffs):
    Acc = [[Fr(coeffs[0]) if i == j else Fr(0) for j in range(27)] for i in range(27)]
    for c in coeffs[1:]:
        Acc = matmulQ(Acc, Mc)
        for i in range(27):
            Acc[i][i] += Fr(c)
    return Acc


W3 = qkernel(poly_mat(h_S))
W6 = qkernel(poly_mat(h_A))
CHK("rational_blocks_dim_3_and_6", len(W3) == 3 and len(W6) == 6)
Me = [[Fr(3) * Rex[8][i][j] + Fr(13) * Rex[16][i][j] for j in range(27)] for i in range(27)]
Mo = [[Fr(7) * Rex[14][i][j] + Fr(17) * Rex[22][i][j] for j in range(27)] for i in range(27)]


def restrict(Mbig, W):
    Crows = []
    for w in W:
        img = [sum(Mbig[i][j] * w[j] for j in range(27) if w[j]) for i in range(27)]
        sol = qsolve_span(W, img)
        assert sol is not None, "block not invariant"
        Crows.append(sol)
    return [[Crows[b][a] for b in range(len(W))] for a in range(len(W))]


C_S = restrict(Mc, W3)
C_E = restrict(Me, W6)
C_O = restrict(Mo, W6)
cpE = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_E[i][j].numerator,
                                               C_E[i][j].denominator)).charpoly(x)
flE = sp.factor_list(cpE.as_expr())
gs = [(f, m) for f, m in flE[1] if sp.degree(f, x) > 0]
CHK("char_Me_W6_is_g_squared_cubic", len(gs) == 1 and gs[0][1] == 2
    and sp.degree(gs[0][0], x) == 3)
g_even = sp.Poly(gs[0][0], x).all_coeffs()
g_even = [sp.Rational(c, g_even[0]) for c in g_even]
cpO = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_O[i][j].numerator,
                                               C_O[i][j].denominator)).charpoly(x)
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


def kkernel(M):
    m, n = len(M), len(M[0])
    A = [row[:] for row in M]
    piv = []; rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if not kis0(A[r][c])), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = kinv(A[rr][c])
        A[rr] = [kmul(iv, e) for e in A[rr]]
        for r in range(m):
            if r != rr and not kis0(A[r][c]):
                f = A[r][c]
                A[r] = [ksub(A[r][j], kmul(f, A[rr][j])) for j in range(n)]
        piv.append(c); rr += 1
    ker = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [KZERO] * n
        v[fc] = KONE
        for i, c in enumerate(piv):
            v[c] = kscale(A[i][fc], Fr(-1))
        ker.append(v)
    return ker


CmK = [[ksub((Fr(C_S[i][j]), Fr(0), Fr(0)), xS if i == j else KZERO)
        for j in range(3)] for i in range(3)]
kerS = kkernel(CmK)
CHK("kernel_S_dim_1", len(kerS) == 1)
vS3 = kerS[0]


def fmulB(a, b):
    return (kadd(kmul(a[0], b[0]), kmul(Bk, kmul(a[1], b[1]))),
            kadd(kmul(a[0], b[1]), kmul(a[1], b[0])))


def fsubB(a, b): return (ksub(a[0], b[0]), ksub(a[1], b[1]))
def fis0B(a): return kis0(a[0]) and kis0(a[1])


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
                   (Fr(-1), Fr(0), Fr(0)) if i == j else KZERO) for j in range(6)])
A = [row[:] for row in rowsF]
piv = []; rr = 0
for c in range(6):
    pr = next((r for r in range(rr, 12) if not fis0B(A[r][c])), None)
    if pr is None:
        continue
    A[rr], A[pr] = A[pr], A[rr]
    iv = finvB(A[rr][c])
    A[rr] = [fmulB(iv, e) for e in A[rr]]
    for r in range(12):
        if r != rr and not fis0B(A[r][c]):
            f = A[r][c]
            A[r] = [fsubB(A[r][j], fmulB(f, A[rr][j])) for j in range(6)]
    piv.append(c); rr += 1
FZ = (KZERO, KZERO)
kerA = []
for fc in [c for c in range(6) if c not in piv]:
    v = [FZ] * 6
    v[fc] = (KONE, KZERO)
    for i, c in enumerate(piv):
        v[c] = fsubB(FZ, A[i][fc])
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


def normalizeK(vec):
    L = 1
    for kt in vec:
        for x2 in kt:
            if x2:
                d = x2.denominator
                L = L * d // math.gcd(L, d)
    vec2 = [kscale(kt, Fr(L)) for kt in vec]
    G = 0
    for kt in vec2:
        for x2 in kt:
            G = math.gcd(G, abs(x2.numerator))
    if G > 1:
        vec2 = [kscale(kt, Fr(1, G)) for kt in vec2]
    return vec2


vS27 = normalizeK(lift(vS3, W3))
u27 = lift([f[0] for f in vA6], W6)
wt27 = lift([f[1] for f in vA6], W6)
wodd27 = [kmul(wK, kt) for kt in wt27]
uw = normalizeK(u27 + wodd27)
u27, wodd27 = uw[:27], uw[27:]
atoms_ex = {}
for j in range(3):
    atoms_ex[f"S{j}"] = [(sigma(j, kt), NZERO) for kt in vS27]
    for sgn, tag in ((1, "p"), (-1, "m")):
        atoms_ex[f"A{j}{tag}"] = [(sigma(j, u27[i]), nscale(sigma(j, wodd27[i]), Fr(sgn)))
                                  for i in range(27)]
CL_NAMES = sorted(atoms_ex)

# exact joint-eigenline certificate + exact eigenvalues (as B914 [6])
log("[6] colorless joint-eigenline certificate + eigenvalues (exact)...")
eig_ex = {}
ok = True
for name in CL_NAMES:
    vec = atoms_ex[name]
    k0 = next(i for i in range(27) if not T.is0(vec[i]))
    ik0 = T.inv(vec[k0])
    eig_ex[name] = {}
    for n in ns:
        R = Rex[n]
        w = []
        for i in range(27):
            acc = TZERO
            for jj in range(27):
                if R[i][jj] and not T.is0(vec[jj]):
                    acc = T.add(acc, T.scale(vec[jj], R[i][jj]))
            w.append(acc)
        for i in range(27):
            for k in range(i + 1, 27):
                if not T.is0(T.sub(T.mul(w[i], vec[k]), T.mul(w[k], vec[i]))):
                    ok = False
        eig_ex[name][n] = T.mul(w[k0], ik0)
CHK("nine_colorless_atoms_exact_joint_eigenlines", ok)

# ================================================================ [7] colored sector
log("[7] THE COLORED SECTOR: W18, C18, the K-quadratic factor of h_col...")
W18 = qkernel(poly_mat(h_col))
CHK("colored_block_dim_18", len(W18) == 18, "Mc semisimple on the colored sector")
C18 = restrict(Mc, W18)

# numeric roots of h_col -> 3 conjugate pairs -> K-quadratic candidates
mp.dps = 400
hh = [mp.mpf(c) for c in h_col]
rts6 = mp.polyroots(hh, maxsteps=400, extraprec=400)
pairs = []
usedr = [False] * 6
for i in range(6):
    if usedr[i] or mp.im(rts6[i]) <= 0:
        continue
    for j in range(6):
        if j != i and not usedr[j] and abs(rts6[j] - mp.conj(rts6[i])) < mp.mpf(10) ** (-150):
            pairs.append((rts6[i], rts6[j]))
            usedr[i] = usedr[j] = True
            break
CHK("h_col_roots_three_conjugate_pairs", len(pairs) == 3)
mu_roots = _mu_roots_numeric(400)
maxden = mp.mpf(10) ** 133
pK = qK = None
for perm in itertools.permutations(range(3)):
    pv = [-2 * mp.re(pairs[perm[g]][0]) for g in range(3)]
    qv = [mp.re(pairs[perm[g]][0]) ** 2 + mp.im(pairs[perm[g]][0]) ** 2
          for g in range(3)]
    pc = _interp_K(pv, mu_roots, maxden, 10 ** 130)
    qc = _interp_K(qv, mu_roots, maxden, 10 ** 130)
    if pc is None or qc is None:
        continue
    # exact certificate: prod_g sigma_g(x^2 + p x + q) = h_col (monic) in N[x]
    lc = Fr(h_col[0])
    hmon = [Fr(c) / lc for c in h_col]
    prodN = [NONE_]                                    # poly coeffs, ascending
    for gg in range(3):
        qg = [sigma(gg, qc), sigma(gg, pc), sigma(gg, KONE)]   # ascending
        new = [NZERO] * (len(prodN) + 2)
        for a2, ca in enumerate(prodN):
            for b2, cb_ in enumerate(qg):
                new[a2 + b2] = nadd(new[a2 + b2], nmul(ca, cb_))
        prodN = new
    okp = all(nis0(nsub(prodN[d], (( (hmon[6 - d], Fr(0), Fr(0)), KZERO))))
              for d in range(7))
    if okp:
        pK, qK = pc, qc
        break
CHK("h_col_is_K_norm_form_of_ONE_quadratic_EXACT", pK is not None,
    "prod_g sigma_g(x^2+px+q) = h_col certified in N[x]")
RES["colored_quadratic_p"] = [str(c) for c in pK]
RES["colored_quadratic_q"] = [str(c) for c in qK]
disc_c = ksub(kmul(pK, pK), kscale(qK, Fr(4)))
w_c = sqrt_in_K(kscale(disc_c, Fr(-1, 231)))
CHK("colored_disc_equals_minus_231_wc_squared", w_c is not None
    and kis0(ksub(kmul(w_c, w_c), kscale(disc_c, Fr(-1, 231)))),
    "NOT the colorless -3w^2 mechanism: the colored sector opens "
    "K(sqrt(-231)); 231 = 3*77 -- the Kummer field Q(sqrt77, sqrt-3) of the "
    "value arc appears inside the object")
RES["colored_w_c_omega"] = [str(c) for c in w_c]
# S77 in N with S77^2 = 77: sqrt(disc mu) lies in the splitting field
r1N = ((Fr(0), Fr(1), Fr(0)), KZERO)                  # rho1
r2N = (KZERO, KONE)                                   # rho2
r3N = nsub(nsub(((Fr(-b_mu), Fr(0), Fr(0)), KZERO), r1N), r2N)
delta = nmul(nmul(nsub(r1N, r2N), nsub(r1N, r3N)), nsub(r2N, r3N))
d2 = nmul(delta, delta)
CHK("delta_squared_rational", kis0(d2[1]) and d2[0][1] == 0 and d2[0][2] == 0)
Dd2 = d2[0][0]
t77 = sp.sqrt(sp.Rational(Dd2.numerator, Dd2.denominator) / 77)
CHK("disc_mu_is_77_times_rational_square", t77.is_rational,
    f"delta^2 = 77 * ({t77})^2 -- mu13 is in the sqrt77 family, so sqrt77 in N")
t77f = Fr(sp.Rational(t77).p, sp.Rational(t77).q)
S77 = nscale(delta, 1 / t77f)
CHK("S77_squared_equals_77_EXACT",
    nis0(nsub(nmul(S77, S77), ((Fr(77), Fr(0), Fr(0)), KZERO))))
RES["S77_in_N"] = [str(c) for kt in S77 for c in kt]
theta_x = kscale(pK, Fr(-1, 2))                       # theta = theta_x + theta_y*omega
theta_y = kscale(w_c, Fr(1, 2))

# ---- kernel of (C18 - theta) over the abstract field K(omega), ONCE
log("[8] the 3-dim colored eigenspace over abstract K(omega) (18x18 kernel)...")
Mft = [[((ksub((Fr(C18[i][j]), Fr(0), Fr(0)), theta_x),
          kscale(theta_y, Fr(-1))) if i == j else
         ((Fr(C18[i][j]), Fr(0), Fr(0)), KZERO)) for j in range(18)]
       for i in range(18)]
Aft = [row[:] for row in Mft]
piv = []; rr = 0
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
            Aft[r] = [ftsub(Aft[r][j], ftmul(f, Aft[rr][j])) for j in range(18)]
    piv.append(c); rr += 1
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
        vec2 = [(kscale(ax, Fr(1, G)), kscale(ay, Fr(1, G))) for (ax, ay) in vec2]
    return vec2


colB = [ftnormalize27(ftlift(v)) for v in kerC]       # 3 basis vectors, 27 K(tau)-coords
hmax_c = max(max(abs(x2.numerator), x2.denominator)
             for vec in colB for (ax, ay) in vec for kt in (ax, ay) for x2 in kt)
RES["colored_basis_height_digits"] = len(str(hmax_c))
log(f"    colored basis entry height ~ 10^{len(str(hmax_c))}")

# ---- the four charges act as SCALARS on the abstract eigenspace (exact)
log("[9] scalar-action certificate (4 charges x 3 basis vectors, exact)...")
mu_col = {}
ok = True
for n in ns:
    R = Rex[n]
    mu_n = None
    for a in range(3):
        u = colB[a]
        w = []
        for i in range(27):
            ax, ay = KZERO, KZERO
            for jj in range(27):
                if R[i][jj] and not ftis0(u[jj]):
                    ax = kadd(ax, kscale(u[jj][0], R[i][jj]))
                    ay = kadd(ay, kscale(u[jj][1], R[i][jj]))
            w.append((ax, ay))
        k0 = next(i for i in range(27) if not ftis0(u[i]))
        mu_a = ftmul(w[k0], ftinv(u[k0]))
        if mu_n is None:
            mu_n = mu_a
        elif not ftis0(ftsub(mu_n, mu_a)):
            ok = False
        for i in range(27):
            if not ftis0(ftsub(w[i], ftmul(mu_a, u[i]))):
                ok = False
    mu_col[n] = mu_n
CHK("colored_space_charges_act_as_scalars_EXACT", ok,
    "each R_n = mu_n * Id on the abstract 3-space; joint atom certified")
# Mc eigenvalue consistency: sum CO[n]*mu_n = theta
acc = FTZERO
for n in ns:
    acc = ftadd(acc, ftscale(mu_col[n], Fr(CO[n])))
CHK("colored_eigenvalue_consistency_Mc",
    ftis0(ftsub(acc, (theta_x, theta_y))))

# ================================================================ [10] identification
log("[10] numeric identification against B912 (dps 80)...")
mp.dps = 80
rts = sorted(mp.polyroots([mp.mpf(c) for c in MU], maxsteps=400, extraprec=400),
             key=lambda r: mp.re(r))
rts = [mp.re(r) for r in rts]
r1v, r2v = rts[0], rts[1]
TAU = mp.mpc(0, 1) * mp.sqrt(mp.mpf(3))


def knumg(xk, g):
    r = rts[g]
    return (mp.mpf(xk[0].numerator) / xk[0].denominator
            + (mp.mpf(xk[1].numerator) / xk[1].denominator) * r
            + (mp.mpf(xk[2].numerator) / xk[2].denominator) * r * r)


def knum(xk): return knumg(xk, 0)


def nnum(a):
    xk, y = a
    return knum(xk) + knum(y) * r2v


def mnum(z):
    return mp.mpc(nnum(z[0])) + TAU * nnum(z[1])


s77num = None                                          # set after S77 exists


def ftnum(a, g, s):
    """numeric value of the abstract K(omega) element under sigma_g,
    omega -> s * S77 * tau."""
    return mp.mpc(knumg(a[0], g)) + s * TAU * knumg(a[1], g) * s77num


def parse_c(s):
    return complex(s.replace(" ", "").replace("(", "").replace(")", ""))


s77num = nnum(S77)
B912_atoms = B912["atoms"]
b912mu = {a["atom"]: tuple(parse_c(a[f"mu{n}"]) for n in ns) for a in B912_atoms}
col_idx1 = [a["atom"] for a in B912_atoms if a["dim"] == 1]
col_idx3 = [a["atom"] for a in B912_atoms if a["dim"] == 3]
# colorless match (as B914)
matchCL = {}
ok = True
for name in CL_NAMES:
    ev = tuple(complex(mnum(eig_ex[name][n])) for n in ns)
    best, bd = None, 1e99
    for ai in col_idx1:
        d = max(abs(ev[t] - b912mu[ai][t]) for t in range(4))
        if d < bd:
            best, bd = ai, d
    if bd > 1e-6:
        ok = False
    matchCL[name] = best
CHK("colorless_atoms_match_B912_bijectively",
    ok and sorted(matchCL.values()) == sorted(col_idx1), f"{matchCL}")
CHK("colorless_match_equals_banked_B914_match",
    {k: v for k, v in matchCL.items()} ==
    {k: int(v) for k, v in B914["match_exact_name_to_B912_atom"].items()})
# colored match: exact atoms (g, s) -> B912 colored indices
matchCO = {}
ok = True
for g in range(3):
    for s in (1, -1):
        ev = tuple(complex(ftnum(mu_col[n], g, s)) for n in ns)
        best, bd = None, 1e99
        for ai in col_idx3:
            d = max(abs(ev[t] - b912mu[ai][t]) for t in range(4))
            if d < bd:
                best, bd = ai, d
        if bd > 1e-6:
            ok = False
        matchCO[(g, s)] = best
CHK("six_colored_atoms_match_B912_bijectively",
    ok and sorted(matchCO.values()) == sorted(col_idx3), f"{matchCO}")
RES["colored_match_g_s_to_B912"] = {f"g{g}{'p' if s == 1 else 'm'}": matchCO[(g, s)]
                                    for g in range(3) for s in (1, -1)}
inv_match = {v: k for k, v in matchCL.items()}
inv_matchCO = {v: k for k, v in matchCO.items()}

# the banked support (B914, numeric-certified 17/680 with a 1e10 gap)
ccl_banked = [tuple(t) for t in B914["ccl_couplings"]]
ccc_banked = [tuple(t) for t in B914["ccc_couplings"]]
CHK("banked_support_9_ccl_2_ccc", len(ccl_banked) == 9 and len(ccc_banked) == 2)
# structure of the banked triples in exact names
diag_ccl, offd_ccl = [], []
for tt in ccl_banked:
    cls = [i for i in tt if i in inv_match]
    cos = [i for i in tt if i in inv_matchCO]
    assert len(cls) == 1 and len(cos) == 2
    lname = inv_match[cls[0]]
    (g1, s1), (g2, s2) = inv_matchCO[cos[0]], inv_matchCO[cos[1]]
    if lname.startswith("S"):
        diag_ccl.append((tt, lname, (g1, s1), (g2, s2)))
    else:
        offd_ccl.append((tt, lname, (g1, s1), (g2, s2)))
CHK("three_diagonal_six_offdiagonal_ccl",
    len(diag_ccl) == 3 and len(offd_ccl) == 6)
ok = True
for tt, lname, (g1, s1), (g2, s2) in diag_ccl:
    gS = int(lname[1])
    if not (g1 == g2 == gS and s1 == -s2):
        ok = False
CHK("diagonal_ccl_structure_Cg_plus_Cg_minus_Sg", ok,
    "each diagonal triple = the generation-g tau-conjugate colored pair + S_g")
ccc_names = [[inv_matchCO[i] for i in tt] for tt in ccc_banked]
ok = all(sorted(g for g, s in tri) == [0, 1, 2]
         and len(set(s for g, s in tri)) == 1 for tri in ccc_names)
CHK("ccc_triples_one_atom_per_generation_same_tau_branch", ok, f"{ccc_names}")

# ================================================================ [11] Grams
log("[11] exact H-Grams (colored 3x3 over K(tau); colorless q), both gauges...")


def gram_colored(cb):
    """G[i][j] = sum_b conj(u_i[piW b]) u_j[b] cb[b], abstract K(tau)."""
    G = [[FTZERO] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            acc = FTZERO
            for b in range(27):
                a2 = piW[b]
                if ftis0(colB[i][a2]) or ftis0(colB[j][b]):
                    continue
                acc = ftadd(acc, ftscale(ftmul(ftconj(colB[i][a2]), colB[j][b]),
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
            m = ftsub(ftmul(G[i1][j1], G[i2][j2]), ftmul(G[i1][j2], G[i2][j1]))
            if (i + j) % 2:
                m = ftscale(m, Fr(-1))
            C2[j][i] = ftmul(m, di)                     # adjugate transpose
    return C2, d


def ftconjmat(G):
    return [[ftconj(G[i][j]) for j in range(3)] for i in range(3)]


GRAM = {}
for gname, cbg in GAUGES.items():
    Gp = gram_colored(cbg)                             # Gram of the abstract '+' space
    herm = all(ftis0(ftsub(Gp[j][i], ftconj(Gp[i][j]))) for i in range(3)
               for j in range(3))
    Gpi, dp = ftinv3(Gp)
    Gm = ftconjmat(Gp)                                 # Gram of the '-' (tau-conj) space
    Gmi, dm = ftinv3(Gm)
    CHK(f"colored_gram_hermitian_invertible_{gname}", herm and not ftis0(dp))
    GRAM[gname] = {"Gp": Gp, "Gpi": Gpi, "Gm": Gm, "Gmi": Gmi, "det_p": dp}
# colorless q under both gauges (S abstract in K; A atoms in N via Mbar hpair)


def hpair_gauge(u, v, cb):
    acc = TZERO
    for b in range(27):
        a2 = piW[b]
        if T.is0(u[a2]) or T.is0(v[b]):
            continue
        acc = T.add(acc, T.scale(T.mul(T.conj(u[a2]), v[b]), Fr(cb[b])))
    return acc


qS_abs = {}                                            # abstract S-norm in K per gauge
for gname, cbg in GAUGES.items():
    acc = KZERO
    for b in range(27):
        a2 = piW[b]
        if kis0(vS27[a2]) or kis0(vS27[b]):
            continue
        acc = kadd(acc, kscale(kmul(vS27[a2], vS27[b]), Fr(cbg[b])))
    qS_abs[gname] = acc
    CHK(f"qS_nonzero_{gname}", not kis0(acc))
qCL = {}
for gname, cbg in GAUGES.items():
    qCL[gname] = {}
    for name in CL_NAMES:
        qv = hpair_gauge(atoms_ex[name], atoms_ex[name], cbg)
        CHK_ok = nis0(qv[1]) and not T.is0(qv)
        if not CHK_ok:
            CHK(f"q_{name}_{gname}_tau_free_nonzero", False)
        qCL[gname][name] = qv[0]
# sigma-consistency: sigma_g(qS_abs) = q of S_g
ok = True
for gname in GAUGES:
    for g in range(3):
        if not nis0(nsub(sigma(g, qS_abs[gname]), qCL[gname][f"S{g}"])):
            ok = False
CHK("qS_sigma_consistency_both_gauges", ok)

# ================================================================ [12] diagonal CCl
log("[12] THE DIAGONAL CCl INVARIANT, abstract over K(tau) (one computation)...")
colBm = [[ftconj(c) for c in v] for v in colB]         # the '-' space basis
# T2[a][b] = cub(colB[a], colBm[b], vS27)  in K(tau)
T2 = [[FTZERO] * 3 for _ in range(3)]
for (xx, yy, zz), cf in T3.items():
    if kis0(vS27[zz]):
        continue
    for a2 in range(3):
        ua = colB[a2][xx]
        if ftis0(ua):
            continue
        for b2 in range(3):
            vb = colBm[b2][yy]
            if ftis0(vb):
                continue
            term = ftscaleK(ftmul(ua, vb), kscale(vS27[zz], cf))
            T2[a2][b2] = ftadd(T2[a2][b2], term)
CHK("diagonal_ccl_tensor_nonzero", any(not ftis0(T2[a2][b2])
                                       for a2 in range(3) for b2 in range(3)))
V_ccl = {}
for gname in GAUGES:
    Gpi, Gmi = GRAM[gname]["Gpi"], GRAM[gname]["Gmi"]
    qSi = kinv(qS_abs[gname])
    acc = FTZERO
    for a2 in range(3):
        for b2 in range(3):
            if ftis0(T2[a2][b2]):
                continue
            for a3 in range(3):
                for b3 in range(3):
                    if ftis0(T2[a3][b3]):
                        continue
                    term = ftmul(ftmul(T2[a2][b2], ftconj(T2[a3][b3])),
                                 ftmul(Gpi[a2][a3], Gmi[b2][b3]))
                    acc = ftadd(acc, term)
    acc = ftscaleK(acc, qSi)
    CHK(f"diagonal_ccl_invariant_tau_free_{gname}", kis0(acc[1]))
    V_ccl[gname] = acc[0]
    RES[f"V_ccl_{gname}"] = [str(c) for c in acc[0]]

# ---- the pipeline link: minpoly of V_ccl (twisted) vs HIER
log("[13] THE PIPELINE LINK: 953^4 * charpoly(mult-by-V_ccl) vs HIER...")
B918 = json.load(open(os.path.join(REPO, "frontier", "B918_v_kummer",
                                   "results.json")))
HIER_ints = [int(c) for c in B918["hier_cubic"]["coeffs"]]
V2_STR = B918["anchors"]["v_sq_95d"]


def mult_matrix(kx):
    cols = [kmul(kx, KONE), kmul(kx, (Fr(0), Fr(1), Fr(0))),
            kmul(kx, (Fr(0), Fr(0), Fr(1)))]
    return [[cols[j][i] for j in range(3)] for i in range(3)]


def kcharpoly(kx):
    Mv = mult_matrix(kx)
    Msp = sp.Matrix(3, 3, lambda i, j: sp.Rational(Mv[i][j].numerator,
                                                   Mv[i][j].denominator))
    return [sp.Rational(c) for c in Msp.charpoly(x).all_coeffs()]


cpV = kcharpoly(V_ccl["tau_twisted_Hprime"])           # monic, descending
D953 = 953 ** 4
scaled = [c * D953 for c in cpV]
CHK("PIPELINE_LINK_953p4_charpoly_equals_HIER_EXACT",
    all(sp.Rational(s).q == 1 for s in scaled)
    and [int(s) for s in scaled] == HIER_ints,
    f"HIER = {HIER_ints}")
# equality with B918's exact K-root V(rho), coefficient for coefficient
rho = sp.Symbol("rho")
Vpoly = sp.Poly(sp.sympify(B918["hier_cubic"]["V_in_rho"]), rho)
vco = [sp.Rational(c) for c in Vpoly.all_coeffs()]     # descending rho^2, rho, 1
V918 = (Fr(vco[2].p, vco[2].q), Fr(vco[1].p, vco[1].q), Fr(vco[0].p, vco[0].q))
CHK("V_ccl_equals_B918_exact_HIER_root_in_K",
    kis0(ksub(V_ccl["tau_twisted_Hprime"], V918)))
# the canonical-gauge diagonal element: the hierarchy COLLAPSES to -3
CHK("canonical_gauge_diagonal_ccl_equals_MINUS_3_EXACT",
    kis0(ksub(V_ccl["canonical_Hplus"], (Fr(-3), Fr(0), Fr(0)))),
    "generation-degenerate: (x+3)^3; the ENTIRE hierarchy lives in the "
    "Hermitian twist D2, not in the atoms or the cubic")
cpVc = kcharpoly(V_ccl["canonical_Hplus"])
canon_ints = [int(c) for c in cpVc]
RES["canonical_gauge_hierarchy_cubic_ints"] = [str(c) for c in canon_ints]
Vratio = kmul(V_ccl["tau_twisted_Hprime"], kinv(V_ccl["canonical_Hplus"]))
RES["V_twisted_over_V_canonical"] = [str(c) for c in Vratio]
CHK("gauge_ratio_is_minus_V_over_3",
    kis0(ksub(Vratio, kscale(V_ccl["tau_twisted_Hprime"], Fr(-1, 3)))))

# ================================================================ [14] CCC exact
log("[14] CCC EXACT on the two banked triples, both gauges...")
# embedded colored atoms and Gram inverses per (g, s)
emb_atoms = {}
for g in range(3):
    for s in (1, -1):
        src2 = colB if s == 1 else colBm
        emb_atoms[(g, s)] = [[ftemb(g, c) for c in v] for v in src2]


def emb_gram_inv(gname, g, s):
    Gi = GRAM[gname]["Gpi"] if s == 1 else GRAM[gname]["Gmi"]
    return [[ftemb(g, Gi[i][j]) for j in range(3)] for i in range(3)]


CCC_vals = {}
for tri in ccc_names:
    key = "+".join(f"g{g}{'p' if s == 1 else 'm'}" for g, s in tri)
    U0, U1, U2 = (emb_atoms[tri[0]], emb_atoms[tri[1]], emb_atoms[tri[2]])
    Tt = [[[TZERO] * 3 for _ in range(3)] for _ in range(3)]
    for (xx, yy, zz), cf in T3.items():
        for a2 in range(3):
            ua = U0[a2][xx]
            if T.is0(ua):
                continue
            for b2 in range(3):
                vb = U1[b2][yy]
                if T.is0(vb):
                    continue
                uv = T.mul(ua, vb)
                for c2 in range(3):
                    wc = U2[c2][zz]
                    if T.is0(wc):
                        continue
                    Tt[a2][b2][c2] = T.add(Tt[a2][b2][c2],
                                           T.scale(T.mul(uv, wc), cf))
    CHK(f"ccc_tensor_nonzero_{key}",
        any(not T.is0(Tt[a2][b2][c2]) for a2 in range(3) for b2 in range(3)
            for c2 in range(3)))
    CCC_vals[key] = {}
    for gname in GAUGES:
        Gi0 = emb_gram_inv(gname, *tri[0])
        Gi1 = emb_gram_inv(gname, *tri[1])
        Gi2 = emb_gram_inv(gname, *tri[2])
        # stepwise contraction: S1[a',b,c] = sum_a T[a,b,c] Gi0[a][a']
        S1 = [[[TZERO] * 3 for _ in range(3)] for _ in range(3)]
        for a2 in range(3):
            for b2 in range(3):
                for c2 in range(3):
                    tv = Tt[a2][b2][c2]
                    if T.is0(tv):
                        continue
                    for a3 in range(3):
                        S1[a3][b2][c2] = T.add(S1[a3][b2][c2],
                                               T.mul(tv, Gi0[a2][a3]))
        S2 = [[[TZERO] * 3 for _ in range(3)] for _ in range(3)]
        for a3 in range(3):
            for b2 in range(3):
                for c2 in range(3):
                    tv = S1[a3][b2][c2]
                    if T.is0(tv):
                        continue
                    for b3 in range(3):
                        S2[a3][b3][c2] = T.add(S2[a3][b3][c2],
                                               T.mul(tv, Gi1[b2][b3]))
        # final contraction: acc = sum S2[a',b',c] Gi2[c][c'] conj(T[a',b',c'])
        acc = TZERO
        for a3 in range(3):
            for b3 in range(3):
                for c2 in range(3):
                    tv = S2[a3][b3][c2]
                    if T.is0(tv):
                        continue
                    for c3 in range(3):
                        acc = T.add(acc, T.mul(T.mul(tv, Gi2[c2][c3]),
                                               T.conj(Tt[a3][b3][c3])))
        CHK(f"ccc_invariant_rational_{key}_{gname}",
            nis0(acc[1]) and kis0((Fr(0), acc[0][0][1], acc[0][0][2]))
            and kis0(acc[0][1]),
            "the CCC invariant is an exact rational")
        CCC_vals[key][gname] = acc[0][0][0]
CHK("CCC_two_triples_equal_both_gauges",
    len(set(v["canonical_Hplus"] for v in CCC_vals.values())) == 1
    and len(set(v["tau_twisted_Hprime"] for v in CCC_vals.values())) == 1)
ccc_can = next(iter(CCC_vals.values()))["canonical_Hplus"]
ccc_tw = next(iter(CCC_vals.values()))["tau_twisted_Hprime"]
RES["CCC_canonical"] = str(ccc_can)
RES["CCC_tau_twisted"] = str(ccc_tw)
CHK("CCC_EQUALS_13824_953_TWISTED_GAUGE_EXACT", ccc_tw == Fr(13824, 953),
    "CCC = 3! * lambda AS AN IDENTITY, lambda = 2304/953 (B916 exact); "
    "the belt residual 953*CCC-13824 ~ 3.5e-85 is closed to an identity")
CHK("CCC_EQUALS_MINUS_6_CANONICAL_GAUGE_EXACT", ccc_can == Fr(-6),
    "|CCC| = 3! * lambda, lambda = 1 (B917 exact); the sign -1 is the "
    "canonical gauge's negative q-product (B916: c^2 = -(q q q))")

# ================================================================ [15] off-diagonal CCl
log("[15] the six off-diagonal CCl invariants (Mbar) + the product law...")
offd_results = {}
ok_all = True
for tt, lname, (g1, s1), (g2, s2) in offd_ccl:
    key = f"{tt}:{lname}+g{g1}{'p' if s1 == 1 else 'm'}+g{g2}{'p' if s2 == 1 else 'm'}"
    U0 = emb_atoms[(g1, s1)]
    U1 = emb_atoms[(g2, s2)]
    L = atoms_ex[lname]
    T2m = [[TZERO] * 3 for _ in range(3)]
    for (xx, yy, zz), cf in T3.items():
        wl = L[zz]
        if T.is0(wl):
            continue
        for a2 in range(3):
            ua = U0[a2][xx]
            if T.is0(ua):
                continue
            for b2 in range(3):
                vb = U1[b2][yy]
                if T.is0(vb):
                    continue
                T2m[a2][b2] = T.add(T2m[a2][b2],
                                    T.scale(T.mul(T.mul(ua, vb), wl), cf))
    entry = {}
    for gname in GAUGES:
        Gi0 = emb_gram_inv(gname, g1, s1)
        Gi1 = emb_gram_inv(gname, g2, s2)
        qLi = ninv(qCL[gname][lname])
        acc = TZERO
        for a2 in range(3):
            for b2 in range(3):
                tv = T2m[a2][b2]
                if T.is0(tv):
                    continue
                for a3 in range(3):
                    for b3 in range(3):
                        tv2 = T2m[a3][b3]
                        if T.is0(tv2):
                            continue
                        acc = T.add(acc, T.mul(T.mul(tv, T.conj(tv2)),
                                               T.mul(Gi0[a2][a3], Gi1[b2][b3])))
        acc = (nmul(acc[0], qLi), nmul(acc[1], qLi))
        if not nis0(acc[1]):
            ok_all = False
        entry[gname] = acc[0]
        # the product law: CI^2 = sigma_g1(V) sigma_g2(V) exactly, both gauges
        lhs = nmul(acc[0], acc[0])
        rhs = nmul(sigma(g1, V_ccl[gname]), sigma(g2, V_ccl[gname]))
        if not nis0(nsub(lhs, rhs)):
            ok_all = False
    offd_results[key] = entry
CHK("offdiagonal_ccl_tau_free_and_PRODUCT_LAW_CI2_eq_sgiV_sgjV_EXACT", ok_all,
    "both gauges: the full CCl table is the symmetric v_i v_j table of the "
    "gauge's diagonal element (HIER root / -3)")
offd_can_signs = {}
ok_pm3 = True
for k2, v2 in offd_results.items():
    cv = v2["canonical_Hplus"]
    if nis0(nsub(cv, nscale(NONE_, Fr(3)))):
        offd_can_signs[k2] = "+3"
    elif nis0(nadd(cv, nscale(NONE_, Fr(3)))):
        offd_can_signs[k2] = "-3"
    else:
        ok_pm3 = False
CHK("canonical_offdiag_ccl_all_pm3_EXACT", ok_pm3,
    f"{sorted(Counter(offd_can_signs.values()).items())}")
RES["offdiag_ccl_canonical_signs"] = offd_can_signs

# ================================================================ [16] numerics
log("[16] numeric certification (dps 110): belt anchors + branch identity...")
mp.dps = 110
rts110 = sorted(mp.polyroots([mp.mpf(c) for c in MU], maxsteps=400, extraprec=200),
                key=lambda r: mp.re(r))
rts110 = [mp.re(r) for r in rts110]


def knumg110(xk, g):
    r = rts110[g]
    return (mp.mpf(xk[0].numerator) / xk[0].denominator
            + (mp.mpf(xk[1].numerator) / xk[1].denominator) * r
            + (mp.mpf(xk[2].numerator) / xk[2].denominator) * r * r)


Vtw = V_ccl["tau_twisted_Hprime"]
diag_num = [knumg110(Vtw, g) for g in range(3)]
CHK("branch_identity_ascending", diag_num[0] < diag_num[1] < diag_num[2],
    "ascending rho_g <-> ascending v_g^2 (identity map), as banked in B918")
worst = mp.mpf(0)
for g in range(3):
    worst = max(worst, abs(diag_num[g] - mp.mpf(V2_STR[g])))
CHK("belt_95digit_anchors_reproduced_at_belt_floor", worst < mp.mpf("1e-85"),
    f"worst |sigma_g(V_ccl) - banked belt v_g^2| = {mp.nstr(worst, 3)} = "
    "B918's registered belt residual (7.3e-88): the exact roots hit the "
    "banked anchors at the anchors' own precision floor")
RES["belt_anchor_worst_abs_diff"] = mp.nstr(worst, 4)
RES["v_g_sq_50d_exact"] = [mp.nstr(v, 50) for v in diag_num]

# independent numeric route (fresh eigenvectors, numeric Grams, dps 60)
log("[17] independent numeric route (fresh eig, numeric H-Grams, dps 60)...")
mp.dps = 60
Rn_num = {n: mp.matrix([[mp.mpf(Rex[n][i][j].numerator) / Rex[n][i][j].denominator
                         if Rex[n][i][j] else mp.mpf(0)
                         for j in range(27)] for i in range(27)]) for n in ns}
Z = 3 * Rn_num[8] + 17 * Rn_num[14] + 5 * Rn_num[16] + 7 * Rn_num[22]
Zc = mp.matrix(27, 27)
for i in range(27):
    for j in range(27):
        Zc[i, j] = mp.mpc(Z[i, j])
E, ER = mp.eig(Zc, left=False, right=True)
order = sorted(range(27), key=lambda k: (mp.re(E[k]), mp.im(E[k])))
clusters = []
for k in order:
    for cl in clusters:
        if abs(E[k] - cl["ev"]) < mp.mpf("1e-20"):
            cl["ks"].append(k)
            break
    else:
        clusters.append({"ev": E[k], "ks": [k]})
num_atoms = []
for cl in clusters:
    Bv = []
    for k in cl["ks"]:
        w = mp.matrix([ER[j, k] for j in range(27)])
        for u in Bv:
            w = w - u * sum(mp.conj(u[j]) * w[j] for j in range(27))
        w = w / mp.sqrt(sum(abs(w[j]) ** 2 for j in range(27)))
        Bv.append(w)
    mus = {}
    for n in ns:
        img = Rn_num[n] * Bv[0]
        nz = max(range(27), key=lambda j: abs(Bv[0][j]))
        mus[n] = img[nz] / Bv[0][nz]
    num_atoms.append({"dim": len(Bv), "B": Bv, "mu": mus})
CHK("numeric_route_atom_shape", sorted(a["dim"] for a in num_atoms) == [1] * 9 + [3] * 6)
nmatch = {}
for idx, a in enumerate(num_atoms):
    ev = tuple(complex(a["mu"][n]) for n in ns)
    cands = [ai for ai in b912mu if B912_atoms[ai]["dim"] == a["dim"]]
    best, bd = None, 1e99
    for ai in cands:
        d = max(abs(ev[t] - b912mu[ai][t]) for t in range(4))
        if d < bd:
            best, bd = ai, d
    assert bd < 1e-6
    nmatch[idx] = best
by_b912 = {nmatch[i]: num_atoms[i] for i in range(15)}
Hn = {}
for gname, cbg in GAUGES.items():
    Hm = mp.matrix(27, 27)
    for b in range(27):
        Hm[piW[b], b] = mp.mpf(cbg[b])
    Hn[gname] = Hm
T3c = {k: int(v) for k, v in T3.items()}


def cubn(u, v, w):
    s = mp.mpc(0)
    for (a2, b2, c2), cf in T3c.items():
        s += cf * u[a2] * v[b2] * w[c2]
    return s


def gram_num(Bv, Hm):
    d = len(Bv)
    return mp.matrix([[sum(mp.conj(Bv[i][piW[b]]) * Bv[j][b] * Hm[piW[b], b]
                           for b in range(27)) for j in range(d)] for i in range(d)])


def ci_num(ids, gname):
    Bs = [by_b912[i]["B"] for i in ids]
    ds = [len(b) for b in Bs]
    Gi = [gram_num(b, Hn[gname]) ** -1 for b in Bs]
    Tt = {}
    for a2 in range(ds[0]):
        for b2 in range(ds[1]):
            for c2 in range(ds[2]):
                Tt[(a2, b2, c2)] = cubn(Bs[0][a2], Bs[1][b2], Bs[2][c2])
    s = mp.mpc(0)
    for (a2, b2, c2), tv in Tt.items():
        for (a3, b3, c3), tv2 in Tt.items():
            s += tv * mp.conj(tv2) * Gi[0][a2, a3] * Gi[1][b2, b3] * Gi[2][c2, c3]
    return mp.re(s)


worst_ind = mp.mpf(0)
for tt in ccc_banked:
    v = ci_num(list(tt), "tau_twisted_Hprime")
    worst_ind = max(worst_ind, abs(v - mp.mpf(13824) / 953))
    v2 = ci_num(list(tt), "canonical_Hplus")
    worst_ind = max(worst_ind, abs(v2 + 6))
for tt, lname, (g1, s1), (g2, s2) in diag_ccl:
    v = ci_num(list(tt), "tau_twisted_Hprime")
    gS = int(lname[1])
    worst_ind = max(worst_ind, abs(v - knumg110(Vtw, gS)))
    v2 = ci_num(list(tt), "canonical_Hplus")
    worst_ind = max(worst_ind, abs(v2 + 3))
CHK("independent_numeric_route_matches_exact_below_1e-40",
    worst_ind < mp.mpf("1e-40"), f"worst {mp.nstr(worst_ind, 3)}")
RES["independent_route_worst_diff"] = mp.nstr(worst_ind, 4)

# ================================================================ write
RES["offdiag_ccl_values_50d_tau_twisted"] = {
    k: mp.nstr(nnum(v["tau_twisted_Hprime"]), 50) for k, v in offd_results.items()}
RES["diag_ccl_statement"] = (
    "ONE abstract K-element V_ccl; the three diagonal CCl invariants are its "
    "sigma_g-images; 953^4 * charpoly(mult-by-V_ccl) = HIER exactly; "
    "V_ccl = B918's exact K-root of HIER coefficient-for-coefficient")
RES["verdict"] = (
    "V-L2 CLOSED: (1) the six colored 3-dim atoms are EXACT joint eigenspaces "
    "over Mbar = N(tau) (h_col = K-norm form of one quadratic; disc = -231 w^2 "
    "-- the colored sector opens K(sqrt-231): the Kummer field Q(sqrt77, "
    "sqrt-3) appears inside the object, sqrt77 = sqrt(disc mu)/rational in N; "
    "charges scalar, certified); "
    "(2) CCC = 13824/953 = 3!*(2304/953) = 3!*lambda (tau-twisted H') and "
    "CCC = -6 (canonical H+, |CCC| = 3!*lambda, sign = the negative q-product) "
    "EXACTLY on both banked CCC triples: CCC = 3!*lambda is an IDENTITY; "
    "(3) the diagonal CCl invariant is ONE K-element V_ccl with "
    "953^4*charpoly = HIER EXACTLY and V_ccl = B918's V(rho): v_g^2 = "
    "roots(HIER) is now an IDENTITY; in the canonical gauge the SAME "
    "invariant collapses to -3 (generation-degenerate, (x+3)^3): the entire "
    "hierarchy is carried by the Hermitian twist D2; the six off-diagonal CCl "
    "satisfy CI^2 = sigma_i(V) sigma_j(V) exactly in both gauges (the v_i v_j "
    "table); belt 95-digit anchors reproduced; independent numeric route agrees.")
RES["runtime_s"] = round(time.time() - T00, 1)
json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)
log("results.json written")
log("VERDICT:", RES["verdict"])
