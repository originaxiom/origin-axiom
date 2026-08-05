#!/usr/bin/env python3
"""B914 -- R2' the signed skeleton + R3' the colorless-first ratio table.

THE BASIS RECONCILIATION (the cell's critical step, done exactly):
  B908's exact colorless atom lines were built in the solo handoff realization,
  which B912 proved is a 27bar (weight multiset = negatives of B883's).  B912's
  H and the banked scales live on the BANKED B883 27.  Mixing them naively
  would be a basis error.  This cell therefore RE-RUNS the B908 route-(a)
  construction ON THE BANKED B883 27 (same rational commuting charge family
  R8, R14, R16, R22 from the B854 invariants; same tower K = Q[rho]/mu13 ->
  N = splitting algebra -> Mbar = N(tau), tau^2 = -3), obtaining the nine
  colorless atom lines EXACTLY in the SAME coordinates where the banked H+
  (B912, integer signed permutation) acts.  The invariant cubic is re-solved
  exactly on the B883 27 (45 weight-zero triples, equivariance kernel dim 1,
  coefficients +-1, verified as an exact derivation identity for all 78
  generators).  Couplings AND H-norms are then computed on the SAME exact
  vectors, so

      T_t := |c_t|^2 / (s_i s_j s_k),   t = (i,j,k) an lll coupling,

  with s_i = the same-vector H-norm in the banked normalization (H scaled so
  the frame-2 vacuum LINE has Rayleigh value +1), is an EXACT element of the
  real field N -- no dps mixing anywhere in T.  T is invariant under any
  per-atom complex rescaling u_i -> lam u_i (c picks up lam_i lam_j lam_k,
  |.|^2 gives |lam|^2 per slot, the same-vector H-norm gives |lam_i|^2), so
  the same T results from B912's unit-vector convention; the banked unit-vector
  scales are reproduced from the exact lines as the reconciliation certificate
  (banked at 35 digits; compared here at dps 80).

Verification chain in this file (all exact unless labeled numeric):
  [A] B883 rep re-verified (Cartan diagonal, 27 distinct weights); the four
      charge matrices commute pairwise over Q.
  [B] H+ (banked, B912) re-verified: symmetric signed permutation; charge
      equivariance  Rn^T H + eps_n H Rn = 0, eps = (-1,+1,-1,+1).
  [C] the invariant cubic on the B883 27: kernel dim 1 (rank 44 of the
      equivariance system on the 45 weight-zero triples), integer-primitive,
      support 45, coefficients +-1, exact derivation identity for ALL 78
      generators (this is B884's banked summary made explicit).
  [D] the nine colorless atoms exactly over Mbar (B908 route (a) on B883):
      charpoly(Mc) = h_S * h_A * h_col^3, W3/W6 rational blocks, Mo|W3 = 0,
      x_S/alpha/B/w in K with B = -3 w^2, kernels dim 1, lifts, and the
      joint-eigenline certificate (componentwise proportionality, all 4 ops,
      all 351 coordinate pairs, in Mbar).
  [E] exact H-data: the atoms are EXACTLY H-orthogonal pairwise over Mbar
      (upgrades B912's < 1e-45 numerics to identities on the colorless nine);
      q_i = u_i^dag H u_i in N, nonzero; D = H+^{-1} H- acts as +1 on each
      colorless line (exact).
  [F] numeric reconciliation (dps 80): the embedded exact lines match the
      dps-60-style eigen-atoms line-for-line (< 1e-40), the exact Rayleigh
      scales reproduce ALL nine banked B912 scales (35-digit strings).
  [G] exact couplings on the exact vectors: support = the two pencils
      (159/165 multisets vanish identically in Mbar), P_R + P_C = 0 and
      I = -1 EXACTLY in this realization too (realization-independence of the
      B908 verdict), non-S row couplings equal, column couplings tau-free.
  [H] the T table: six exact T in N, minimal polynomials certified by exact
      linear algebra in N; all 15 pairwise ratios classified exact-rational /
      algebraic-with-minpoly; row/column products; the consistency gate
      prod(rows T) = prod(cols T)  (i.e. I^2 = 1) asserted EXACTLY.
  [I] numeric colored sector (dps 60, residual-certified) + the full
      680-multiset support scan (the 17 couplings) -> the perfect matching
      colored-atom <-> colorless partner read off the ccl couplings, annotated
      with the sealed B913 magnitudes |det|^{1/3} and (1,2,0) tags.

GATE 5: structure only; no experimental number enters or is compared.

Env: SESSION_SCRATCH optional (cache + isolated-exec cwd); falls back to a
fresh temp dir.  Paths repo-relative from this file.  Output: results.json.
"""
import io, os, json, math, time, pickle, tempfile, contextlib, itertools
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
import sympy as sp
import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b914_")
os.makedirs(SCRATCH, exist_ok=True)
T00 = time.time()
RES = {"cell": "B914 R2'+R3' ratio table", "checks": {}, "notes": []}


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
    """(x + y rho2)^-1 in N: solve [x, -Qy; y, x-Py][c;d]=[1;0] over K."""
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

# ================================================================ [3] H+ (banked, B912)
log("[3] banked H+ re-verified (symmetric signed permutation; charge equivariance)...")
B912 = json.load(open(os.path.join(REPO, "frontier", "B912_norm_cell", "results.json")))
piW = B912["H_plus_support_pi"]
cb = B912["H_plus_entries_c_b"]
CHK("H_plus_signed_permutation_symmetric",
    sorted(piW) == list(range(27)) and all(abs(c) == 1 for c in cb)
    and all(piW[piW[b]] == b and cb[piW[b]] == cb[b] for b in range(27)))
pinv = [0] * 27
for b in range(27):
    pinv[piW[b]] = b
EPS = {8: -1, 14: 1, 16: -1, 22: 1}                       # the banked wall pattern
ok = True
for n in ns:
    R = Rex[n]
    for a in range(27):
        for b in range(27):
            # (R^T H)[a][b] + eps (H R)[a][b] = 0
            v = R[piW[b]][a] * cb[b] + EPS[n] * cb[pinv[a]] * R[pinv[a]][b]
            if v != 0:
                ok = False
CHK("H_charge_equivariance_RnT_H_plus_eps_H_Rn_zero_exact", ok,
    "eps = (-1,+1,-1,+1) on (8,14,16,22)")

# ================================================================ [4] the invariant cubic
log("[4] the invariant cubic on the B883 27 (exact kernel + 78-generator verify)...")
wz = [t for t in itertools.combinations_with_replacement(range(27), 3)
      if all(WT[t[0]][i] + WT[t[1]][i] + WT[t[2]][i] == 0 for i in range(6))]
CHK("weight_zero_triples_45_all_distinct_entries",
    len(wz) == 45 and all(a < b < c for a, b, c in wz), f"{len(wz)}")
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
                rows_eq[key] = rows_eq.get(key, [Fr(0)] * 45)
                rows_eq[key][tidx[t]] += v
            for (i, v) in rownz[y]:
                key = (k, tuple(sorted((x, i, z))))
                rows_eq[key] = rows_eq.get(key, [Fr(0)] * 45)
                rows_eq[key][tidx[t]] += v
            for (i, v) in rownz[z]:
                key = (k, tuple(sorted((x, y, i))))
                rows_eq[key] = rows_eq.get(key, [Fr(0)] * 45)
                rows_eq[key][tidx[t]] += v
eqm = [r for r in rows_eq.values() if any(r)]
ker = qkernel(eqm)
CHK("cubic_equivariance_kernel_dim_1", len(ker) == 1, f"{len(eqm)} eq rows")
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
    cubi = [-v for v in cubi]                              # sign convention: first triple +1
CHK("cubic_support_45_coeffs_pm1",
    all(abs(v) == 1 for v in cubi), f"values {sorted(set(cubi))}")
TRIP = wz
COEF = cubi
# exact derivation identity for ALL 78 generators (the invariance theorem)
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
CHK("four_charges_exact_derivations_of_cubic", True, "subset of the 78")

# ================================================================ [5] exact colorless atoms
log("[5] the exact colorless construction on the B883 27 (B908 route (a) redone)...")
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
RES["h_S_B883"] = [str(c) for c in h_S]
RES["h_A_B883_lc"] = str(h_A[0])
# structure cross-check vs B908 (the handoff realization is the 27bar: spectra negate)
h_S_handoff = [1, 0, -535623511707648, -2928461724187049852928]
mirror = [h_S_handoff[0], -h_S_handoff[1], h_S_handoff[2], -h_S_handoff[3]]
RES["h_S_mirror_of_B908"] = (h_S == mirror)
log(f"    h_S = {h_S}  (mirror of B908's handoff h_S: {h_S == mirror})")


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
C_S_O = restrict(Mo, W3)
CHK("Mo_annihilates_S_block", all(C_S_O[i][j] == 0 for i in range(3) for j in range(3)))
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
CHK("alpha_equals_minus_half_xS", kis0(kadd(kscale(xS, Fr(1, 2)), alph)))
wK = sqrt_in_K(kscale(Bk, Fr(-1, 3)))
CHK("B_equals_minus_3_w_squared", wK is not None
    and kis0(ksub(kmul(wK, wK), kscale(Bk, Fr(-1, 3)))))
RES["x_S"] = [str(c) for c in xS]
RES["B"] = [str(c) for c in Bk]
RES["w"] = [str(c) for c in wK]


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


def fmul(a, b):
    return (kadd(kmul(a[0], b[0]), kmul(Bk, kmul(a[1], b[1]))),
            kadd(kmul(a[0], b[1]), kmul(a[1], b[0])))


def fsub(a, b): return (ksub(a[0], b[0]), ksub(a[1], b[1]))
def fis0(a): return kis0(a[0]) and kis0(a[1])


def finv(a):
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
    pr = next((r for r in range(rr, 12) if not fis0(A[r][c])), None)
    if pr is None:
        continue
    A[rr], A[pr] = A[pr], A[rr]
    iv = finv(A[rr][c])
    A[rr] = [fmul(iv, e) for e in A[rr]]
    for r in range(12):
        if r != rr and not fis0(A[r][c]):
            f = A[r][c]
            A[r] = [fsub(A[r][j], fmul(f, A[rr][j])) for j in range(6)]
    piv.append(c); rr += 1
FZ = (KZERO, KZERO)
kerA = []
for fc in [c for c in range(6) if c not in piv]:
    v = [FZ] * 6
    v[fc] = (KONE, KZERO)
    for i, c in enumerate(piv):
        v[c] = fsub(FZ, A[i][fc])
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


vS27 = lift(vS3, W3)
u27 = lift([f[0] for f in vA6], W6)
wt27 = lift([f[1] for f in vA6], W6)
wodd27 = [kmul(wK, kt) for kt in wt27]


def normalize(vec):
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


vS27 = normalize(vS27)
uw = normalize(u27 + wodd27)
u27, wodd27 = uw[:27], uw[27:]
atoms_ex = {}
for j in range(3):
    atoms_ex[f"S{j}"] = [(sigma(j, kt), NZERO) for kt in vS27]
    for sgn, tag in ((1, "p"), (-1, "m")):
        atoms_ex[f"A{j}{tag}"] = [(sigma(j, u27[i]), nscale(sigma(j, wodd27[i]), Fr(sgn)))
                                  for i in range(27)]
NAMES = sorted(atoms_ex)                                    # A0m..S2 (alphabetical)

# ---- joint-eigenline certificate + exact eigenvalues
log("[6] joint-eigenline certificate (all 4 ops, all pairs, exact in Mbar)...")
eig_ex = {}                                                 # name -> {n: Mbar eigenvalue}
ok = True
for name in NAMES:
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
CHK("nine_atoms_exact_joint_eigenlines_all4ops", ok)
CHK("S_atoms_kill_R14_R22_exactly",
    all(T.is0(eig_ex[f"S{j}"][14]) and T.is0(eig_ex[f"S{j}"][22]) for j in range(3)))

# ================================================================ [7] exact H-data
log("[7] exact H-data: pairwise orthogonality, q_i, D-action...")


def hpair(u, v):
    acc = TZERO
    for b in range(27):
        a = piW[b]
        if not (T.is0(u[a]) or T.is0(v[b])):
            acc = T.add(acc, T.scale(T.mul(T.conj(u[a]), v[b]), Fr(cb[b])))
    return acc


ok = True
for i1 in range(9):
    for i2 in range(i1 + 1, 9):
        if not T.is0(hpair(atoms_ex[NAMES[i1]], atoms_ex[NAMES[i2]])):
            ok = False
CHK("atoms_pairwise_H_orthogonal_EXACT_over_Mbar", ok,
    "upgrades B912's <1e-45 numerics to identities (colorless nine)")
qex = {}; nex = {}
ok_real = True; ok_nz = True
for name in NAMES:
    u = atoms_ex[name]
    qv = hpair(u, u)
    nv = TZERO
    for b in range(27):
        if not T.is0(u[b]):
            nv = T.add(nv, T.mul(T.conj(u[b]), u[b]))
    if not (nis0(qv[1]) and nis0(nv[1])):
        ok_real = False
    if T.is0(qv):
        ok_nz = False
    qex[name] = qv[0]                                       # element of N
    nex[name] = nv[0]
CHK("q_and_n_tau_free_in_N", ok_real)
CHK("q_nonzero_every_atom", ok_nz)
Dd = B912["D_diag"]
ok = True
for name in NAMES:
    u = atoms_ex[name]
    for b in range(27):
        if Dd[b] == -1 and not T.is0(u[b]):
            # D acts as +1 on the line iff support avoids -1 slots OR the line is D-eigen;
            # check the strong statement: D u = u componentwise
            ok = False
CHK("D_acts_as_plus1_on_each_colorless_line_EXACT", ok,
    "support of every colorless atom avoids the D=-1 slots")

# ================================================================ [8] numeric embedding
log("[8] numeric embedding (dps 80): matching to B912 atoms + scale reconciliation...")
mp.dps = 80
rts = sorted(mp.polyroots([mp.mpf(c) for c in MU], maxsteps=400, extraprec=400),
             key=lambda r: mp.re(r))
rts = [mp.re(r) for r in rts]
r1v, r2v = rts[0], rts[1]                                   # ambient embedding: rho1->rts[0], rho2->rts[1]
TAU = mp.mpc(0, 1) * mp.sqrt(mp.mpf(3))


def knum(xk):
    return (mp.mpf(xk[0].numerator) / xk[0].denominator
            + (mp.mpf(xk[1].numerator) / xk[1].denominator) * r1v
            + (mp.mpf(xk[2].numerator) / xk[2].denominator) * r1v * r1v)


def nnum(a):
    x, y = a
    return knum(x) + knum(y) * r2v


def mnum(z):
    return mp.mpc(nnum(z[0])) + TAU * nnum(z[1])


B912_atoms = B912["atoms"]
col_idx = [a["atom"] for a in B912_atoms if a["dim"] == 1]


def parse_c(s):
    return complex(s.replace(" ", "").replace("(", "").replace(")", ""))


b912mu = {a["atom"]: tuple(parse_c(a[f"mu{n}"]) for n in ns) for a in B912_atoms}
match = {}
ok = True
for name in NAMES:
    ev = tuple(complex(mnum(eig_ex[name][n])) for n in ns)
    best, bd = None, 1e99
    for ai in col_idx:
        d = max(abs(ev[t] - b912mu[ai][t]) for t in range(4))
        if d < bd:
            best, bd = ai, d
    if bd > 1e-6:
        ok = False
    match[name] = best
CHK("exact_atoms_match_B912_atoms_bijectively_via_mu",
    ok and sorted(match.values()) == sorted(col_idx), f"{match}")
ref_name = next(nm for nm, ai in match.items() if ai == 0)  # B912 atom 0 = frame-2 vacuum
CHK("reference_is_an_S_atom", ref_name.startswith("S"), f"ref = {ref_name}")
RES["match_exact_name_to_B912_atom"] = match
RES["reference_atom"] = ref_name

# exact Rayleigh scales vs the banked 35-digit values
r_ex = {nm: nmul(qex[nm], ninv(nex[nm])) for nm in NAMES}   # q/n in N
rref_inv = ninv(r_ex[ref_name])
s_ex = {nm: nmul(r_ex[nm], rref_inv) for nm in NAMES}       # banked-convention scales
worst = mp.mpf(0)
for nm in NAMES:
    sv = nnum(s_ex[nm])
    banked = mp.mpf(B912_atoms[match[nm]]["scale_absdet_pow_1_over_dim"])
    worst = max(worst, abs(sv - banked) / banked)
CHK("exact_scales_reproduce_banked_B912_scales_35digits", worst < mp.mpf("1e-33"),
    f"worst rel diff {mp.nstr(worst, 3)}")
RES["scale_reconciliation_worst_rel_diff"] = mp.nstr(worst, 6)
CHK("all_scales_positive", all(nnum(s_ex[nm]) > 0 for nm in NAMES))
RES["scales_exact_by_atom"] = {
    nm: {"B912_atom": match[nm], "value_50d": mp.nstr(nnum(s_ex[nm]), 50)} for nm in NAMES}

# line-level reconciliation: embedded exact lines vs a fresh dps-60-style eigensplit
log("[9] fresh C-side eigen-atoms (dps 60 style at dps 80) for line-level check...")
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
        if abs(E[k] - cl["ev"]) < mp.mpf("1e-25"):
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
    A2 = {"dim": len(Bv), "B": Bv, "mu": {}, "res": mp.mpf(0)}
    for n in ns:
        imgs = [Rn_num[n] * v for v in Bv]
        m = len(Bv)
        Mr = mp.matrix(m, m)
        for a2 in range(m):
            for b2 in range(m):
                Mr[a2, b2] = sum(mp.conj(Bv[a2][j]) * imgs[b2][j] for j in range(27))
        rmax = mp.mpf(0)
        for b2 in range(m):
            diff = imgs[b2] - sum((Mr[a2, b2] * Bv[a2] for a2 in range(m)),
                                  mp.matrix(27, 1))
            rmax = max(rmax, mp.sqrt(sum(abs(diff[j]) ** 2 for j in range(27))))
        offd = max((abs(Mr[a2, b2]) for a2 in range(m) for b2 in range(m) if a2 != b2),
                   default=mp.mpf(0))
        spread = max(abs(Mr[a2, a2] - Mr[0, 0]) for a2 in range(m))
        A2["mu"][n] = Mr[0, 0]
        A2["res"] = max(A2["res"], rmax, offd, spread)
    num_atoms.append(A2)
CHK("C_atoms_shape_6x3_9x1", sorted(a["dim"] for a in num_atoms) == [1] * 9 + [3] * 6)
wres = max(a["res"] for a in num_atoms)
CHK("C_atoms_residuals_below_1e-40", wres < mp.mpf("1e-40"), f"worst {mp.nstr(wres,3)}")
# match numeric atoms to B912 indices via mu
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
CHK("numeric_atoms_match_B912_bijectively", sorted(nmatch.values()) == list(range(15)))
by_b912 = {nmatch[i]: num_atoms[i] for i in range(15)}
worstline = mp.mpf(0)
for nm in NAMES:
    uemb = mp.matrix([mnum(c) for c in atoms_ex[nm]])
    v = by_b912[match[nm]]["B"][0]
    ip = sum(mp.conj(uemb[j]) * v[j] for j in range(27))
    nn2 = sum(abs(uemb[j]) ** 2 for j in range(27))
    diff = v - uemb * (ip / nn2)
    worstline = max(worstline, mp.sqrt(sum(abs(diff[j]) ** 2 for j in range(27))))
CHK("embedded_exact_lines_equal_eigen_lines_below_1e-40", worstline < mp.mpf("1e-40"),
    f"worst line distance {mp.nstr(worstline, 3)}")

# ================================================================ [10] exact couplings
log("[10] exact couplings on the exact vectors; support; I; the T table...")


def cubT(u, v, w):
    s = TZERO
    for t, cf in zip(TRIP, COEF):
        acc = TZERO
        for (a, b, c) in set(itertools.permutations(t)):
            if not (T.is0(u[a]) or T.is0(v[b]) or T.is0(w[c])):
                acc = T.add(acc, T.mul(T.mul(u[a], v[b]), w[c]))
        if not T.is0(acc):
            s = T.add(s, T.scale(acc, Fr(cf)))
    return s


vals = {}
support = []
for i1 in range(9):
    for i2 in range(i1, 9):
        for i3 in range(i2, 9):
            val = cubT(atoms_ex[NAMES[i1]], atoms_ex[NAMES[i2]], atoms_ex[NAMES[i3]])
            if not T.is0(val):
                support.append((i1, i2, i3))
                vals[(i1, i2, i3)] = val
CHK("char0_support_exactly_6_of_165", len(support) == 6,
    f"{[[NAMES[i] for i in t] for t in support]}")
sup_names = [tuple(NAMES[i] for i in t) for t in support]
S_tri = next(t for t in support if all(NAMES[i].startswith("S") for i in t))
rows_tri = [S_tri] + [t for t in support
                      if len({NAMES[i][-1] for i in t}) == 1 and t != S_tri
                      and not NAMES[t[0]].startswith("S")]
cols_tri = [t for t in support if t not in rows_tri]
CHK("pencils_shape_rows_S_pp_mm__cols_SppSmm", len(rows_tri) == 3 and len(cols_tri) == 3,
    f"rows {[[NAMES[i] for i in t] for t in rows_tri]} cols {[[NAMES[i] for i in t] for t in cols_tri]}")
P_R = TONE
for t in rows_tri:
    P_R = T.mul(P_R, vals[t])
P_C = TONE
for t in cols_tri:
    P_C = T.mul(P_C, vals[t])
CHK("v_PR_plus_PC_zero_EXACT", T.is0(T.add(P_R, P_C)))
I_val = T.mul(P_R, T.inv(P_C))
CHK("I_equals_minus_1_EXACT_in_B883_realization",
    T.is0(T.sub(I_val, T.scale(TONE, Fr(-1)))),
    "realization-independence of the B908 verdict")


def as_rationalT(tel):
    X, Y = tel
    if not nis0(Y):
        return None
    XK, XR = X
    if not kis0(XR) or XK[1] or XK[2]:
        return None
    return XK[0]


cS_val = as_rationalT(vals[S_tri])
crow_vals = [as_rationalT(vals[t]) for t in rows_tri[1:]]
disc_mu = int(sp.Poly(MU, sp.Symbol("y")).discriminant())
RES["c_S"] = str(cS_val)
RES["c_S_vs_disc_mu13"] = {"disc": str(disc_mu),
                           "ratio": str(Fr(cS_val, disc_mu)) if cS_val else None}
CHK("row_couplings_rational", cS_val is not None and None not in crow_vals)
CHK("nonS_row_couplings_EQUAL", crow_vals[0] == crow_vals[1], f"{crow_vals[0]}")
RES["c_row_nonS"] = str(crow_vals[0])
ok = all(nis0(vals[t][1]) for t in cols_tri)
CHK("column_couplings_tau_free", ok)

# ---- the T table (exact in N)
rN = r_ex[ref_name]                                         # Rayleigh of the reference line
rN3 = nmul(nmul(rN, rN), rN)
Tvals = {}
for t in support:
    c = vals[t]
    c2 = T.mul(c, T.conj(c))
    assert nis0(c2[1])
    num = nmul(c2[0], rN3)
    den = NONE_
    for i in t:
        den = nmul(den, qex[NAMES[i]])
    Tvals[t] = nmul(num, ninv(den))
# invariance rewrite check: T also equals |c_unit|^2/(s_i s_j s_k)
ok = True
for t in support:
    c2 = T.mul(vals[t], T.conj(vals[t]))[0]
    dd = NONE_
    for i in t:
        dd = nmul(dd, nmul(s_ex[NAMES[i]], nex[NAMES[i]]))
    alt = nmul(c2, ninv(dd))
    if not nis0(nsub(alt, Tvals[t])):
        ok = False
CHK("T_gauge_invariance_identity_unitvector_route_agrees_EXACT", ok)

Trow = [Tvals[t] for t in rows_tri]
Tcol = [Tvals[t] for t in cols_tri]
CHK("T_row2_equals_T_row3_EXACT_Galois_forced", nis0(nsub(Trow[1], Trow[2])))
PT_R = nmul(nmul(Trow[0], Trow[1]), Trow[2])
PT_C = nmul(nmul(Tcol[0], Tcol[1]), Tcol[2])
CHK("consistency_gate_prodrowsT_equals_prodcolsT_EXACT_I2_1", nis0(nsub(PT_R, PT_C)))
T0v = Tvals[support[0]]
CHK("T_ALL_SIX_EQUAL_EXACT",
    all(nis0(nsub(Tvals[t], T0v)) for t in support),
    "the whole normalization-free table is ONE number")
# T = sigma_2-image of an explicit K element (solve the 6x3 linear system)
KB = [sigma(2, KONE), sigma(2, (Fr(0), Fr(1), Fr(0))), sigma(2, (Fr(0), Fr(0), Fr(1)))]
Msig = [[[b[0][0], b[0][1], b[0][2], b[1][0], b[1][1], b[1][2]][i] for b in KB]
        for i in range(6)]
tK = qsolve_span([[Msig[i][j] for i in range(6)] for j in range(3)],
                 [T0v[0][0], T0v[0][1], T0v[0][2], T0v[1][0], T0v[1][1], T0v[1][2]])
if tK is not None:
    chk = nsub(sigma(2, tuple(tK)), T0v)
    CHK("T_is_sigma2_of_explicit_K_element", nis0(chk),
        "T = sigma_2(t_K), t_K coords banked")
    RES["T_as_K_element_sigma2"] = [str(c) for c in tK]
else:
    RES["notes"].append("T not in sigma_2(K) image (unexpected)")


# ---- minimal polynomials in N (exact linear algebra over Q)
def ncoords(z):
    return [z[0][0], z[0][1], z[0][2], z[1][0], z[1][1], z[1][2]]


def minpoly_N(z):
    pows = [NONE_]
    for _ in range(6):
        pows.append(nmul(pows[-1], z))
    for d in range(1, 7):
        M = [[ncoords(pows[k])[i] for k in range(d + 1)] for i in range(6)]
        kv = qkernel(M)
        if kv:
            cvec = kv[0]
            if cvec[d] == 0:
                continue
            mon = [c / cvec[d] for c in cvec]               # ascending, monic
            acc = NZERO
            for k in range(d + 1):
                acc = nadd(acc, nscale(pows[k], mon[k]))
            assert nis0(acc)
            den = 1
            for c in mon:
                den = den * c.denominator // math.gcd(den, c.denominator)
            ints = [int(c * den) for c in mon]
            g = 0
            for v in ints:
                g = math.gcd(g, abs(v))
            ints = [v // g for v in ints]
            if ints[-1] < 0:
                ints = [-v for v in ints]
            return ints[::-1]                               # descending
    return None


def describe(z, digits=50):
    mpoly = minpoly_N(z)
    d = {"value_50d": mp.nstr(nnum(z), digits),
         "minpoly_deg": len(mpoly) - 1,
         "minpoly_desc_coeffs": [str(c) for c in mpoly]}
    if len(mpoly) == 2:
        d["exact_rational"] = str(Fr(-mpoly[1], mpoly[0]))
    return d


TT = {}
for t in support:
    key = "T(" + ",".join(NAMES[i] for i in t) + ")"
    TT[key] = describe(Tvals[t])
RES["T_table"] = TT
RES["T_single"] = describe(T0v)
RES["T_exact_ncoords"] = [str(c) for c in ncoords(T0v)]
RES["cubic_B883"] = {"triples": [list(t) for t in TRIP], "coeffs": COEF,
                     "sign_convention": "coefficient of the lexicographically first "
                                        "weight-zero triple = +1"}
RES["q_exact_ncoords"] = {nm: [str(c) for c in ncoords(qex[nm])] for nm in NAMES}
RES["n_exact_ncoords"] = {nm: [str(c) for c in ncoords(nex[nm])] for nm in NAMES}
RES["c_cols_ncoords"] = {"+".join(NAMES[i] for i in t):
                         [str(c) for c in ncoords(vals[t][0])] for t in cols_tri}
RES["T_row_products"] = {"rows": describe(PT_R), "cols": describe(PT_C)}
ratios = {}
sup_sorted = sorted(support)
for a in range(6):
    for b in range(a + 1, 6):
        ta, tb = sup_sorted[a], sup_sorted[b]
        r = nmul(Tvals[ta], ninv(Tvals[tb]))
        key = ("T(" + ",".join(NAMES[i] for i in ta) + ")/T("
               + ",".join(NAMES[i] for i in tb) + ")")
        ratios[key] = describe(r)
RES["T_pairwise_ratios"] = ratios
n_rat = sum(1 for v in ratios.values() if "exact_rational" in v)
log(f"    pairwise ratios: {n_rat}/15 exact rationals")

# grid in B912 indices
grid = {}
for t in rows_tri:
    for i in t:
        cpos = next(ci for ci, tc in enumerate(cols_tri) if i in tc)
        rpos = rows_tri.index(t)
        grid[(rpos, cpos)] = {"name": NAMES[i], "B912_atom": match[NAMES[i]],
                              "scale_50d": mp.nstr(nnum(s_ex[NAMES[i]]), 50),
                              "sign": "+"}
RES["grid_R2prime"] = {f"r{r}c{c}": grid[(r, c)] for (r, c) in sorted(grid)}
RES["pencils_B912_indices"] = {
    "rows": [[match[NAMES[i]] for i in t] for t in rows_tri],
    "cols": [[match[NAMES[i]] for i in t] for t in cols_tri]}

# ================================================================ [11] colored sector scan
log("[11] the 680-multiset support scan (numeric, margins recorded)...")
mp.dps = 50
atomsB = {ai: [mp.matrix([mp.mpc(v[j]) for j in range(27)]) for v in by_b912[ai]["B"]]
          for ai in range(15)}
T3c = {k: mp.mpf(v.numerator) for k, v in T3.items()}


def cub_num(u, v, w):
    s = mp.mpc(0)
    for (a, b, c), cf in T3c.items():
        s += cf * u[a] * v[b] * w[c]
    return s


maxvals = {}
for ms in itertools.combinations_with_replacement(range(15), 3):
    best = mp.mpf(0)
    for aa in atomsB[ms[0]]:
        for bb in atomsB[ms[1]]:
            for cc2 in atomsB[ms[2]]:
                best = max(best, abs(cub_num(aa, bb, cc2)))
    maxvals[ms] = best
snz = sorted(maxvals.items(), key=lambda kv: -kv[1])
vals_sorted = [float(v) for _, v in snz]
gaps = [vals_sorted[i] / max(vals_sorted[i + 1], 1e-300)
        for i in range(len(vals_sorted) - 1)]
n_coupled = gaps.index(max(gaps)) + 1
gap_hi = vals_sorted[n_coupled - 1]
gap_lo = vals_sorted[n_coupled]
CHK("support_scan_17_of_680_clean_gap", n_coupled == 17 and max(gaps) > 1e10,
    f"couplings {n_coupled}, min coupling {gap_hi:.3e}, max zero {gap_lo:.3e}, "
    f"gap {max(gaps):.3e}")
coupled = sorted([ms for ms, _ in snz[:n_coupled]])
kinds = Counter()
for ms in coupled:
    kk = "".join("c" if B912_atoms[i]["dim"] == 3 else "l" for i in sorted(ms))
    kinds["".join(sorted(kk))] += 1
RES["support_scan"] = {
    "n_coupled": n_coupled, "kinds": dict(kinds),
    "min_coupling": f"{gap_hi:.3e}", "max_zero": f"{gap_lo:.3e}",
    "coupled_multisets_B912_indices": [list(ms) for ms in coupled]}
lll = [ms for ms in coupled if all(B912_atoms[i]["dim"] == 1 for i in ms)]
exact_lll = sorted(tuple(sorted(match[NAMES[i]] for i in t)) for t in support)
CHK("scan_lll_equals_exact_support", sorted(lll) == exact_lll)
# the perfect matching from the ccl couplings
ccl = [ms for ms in coupled if sorted(B912_atoms[i]["dim"] for i in ms) == [1, 3, 3]]
matching = {}
for ms in ccl:
    cols_ = [i for i in ms if B912_atoms[i]["dim"] == 3]
    lone = [i for i in ms if B912_atoms[i]["dim"] == 1]
    matching.setdefault(tuple(sorted(cols_)), []).extend(lone)
RES["ccl_couplings"] = [list(ms) for ms in ccl]
RES["colored_pair_to_colorless_partners"] = {str(k): sorted(v)
                                             for k, v in matching.items()}
ccc = [ms for ms in coupled if all(B912_atoms[i]["dim"] == 3 for i in ms)]
RES["ccc_couplings"] = [list(ms) for ms in ccc]
colored_banked = {i: {"signature": B912_atoms[i]["signature"],
                      "absdet_pow13": B912_atoms[i]["scale_absdet_pow_1_over_dim"]}
                  for i in range(15) if B912_atoms[i]["dim"] == 3}
RES["colored_atoms_banked_B913_magnitudes"] = colored_banked

# ================================================================ [12] independent route
log("[12] INDEPENDENT numeric route (unit eigenvectors + numeric H + numeric cubic)...")
# shares only the banked instruments (rep27, INV, H+, the verified cubic); the vectors,
# the gauge, and the arithmetic are all different from the exact route.
mp.dps = 80
Hm_num = mp.matrix(27, 27)
for b in range(27):
    Hm_num[piW[b], b] = mp.mpf(cb[b])
ray = {}
for ai in col_idx:
    v = by_b912[ai]["B"][0]
    hv = Hm_num * v
    r_ = sum(mp.conj(v[j]) * hv[j] for j in range(27))
    assert abs(mp.im(r_)) < mp.mpf("1e-60")
    ray[ai] = mp.re(r_)
c0n = ray[0]
s_num = {ai: ray[ai] / c0n for ai in col_idx}
worst = mp.mpf(0)
for nm in NAMES:
    banked = mp.mpf(B912_atoms[match[nm]]["scale_absdet_pow_1_over_dim"])
    worst = max(worst, abs(s_num[match[nm]] - banked) / banked)
CHK("independent_route_scales_match_banked", worst < mp.mpf("1e-33"),
    f"worst rel diff {mp.nstr(worst, 3)}")


def cubn80(u, v, w):
    s = mp.mpc(0)
    for (a2, b2, c2), cf in T3.items():
        s += int(cf) * u[a2] * v[b2] * w[c2]
    return s


Tnum = {}
for t in support:
    idx = [match[NAMES[i]] for i in t]
    c = cubn80(by_b912[idx[0]]["B"][0], by_b912[idx[1]]["B"][0], by_b912[idx[2]]["B"][0])
    Tnum[t] = abs(c) ** 2 / (s_num[idx[0]] * s_num[idx[1]] * s_num[idx[2]])
tvals_n = list(Tnum.values())
spread = max(tvals_n) / min(tvals_n) - 1
CHK("independent_route_six_T_equal_below_1e-40", abs(spread) < mp.mpf("1e-40"),
    f"spread {mp.nstr(spread, 3)}")
Tex_num = nnum(T0v)
rel = max(abs(tv - Tex_num) / Tex_num for tv in tvals_n)
CHK("independent_route_matches_exact_T_below_1e-40", rel < mp.mpf("1e-40"),
    f"worst rel diff {mp.nstr(rel, 3)}")
RES["independent_route"] = {"six_T_spread": mp.nstr(spread, 6),
                            "vs_exact_T_rel": mp.nstr(rel, 6)}

# ================================================================ write
RES["verdict"] = ("R2'+R3' DELIVERED: nine exact scales certified against B912; six "
                  "exact T in N; T_row2=T_row3 and prod(rows)=prod(cols) forced; "
                  "see T_table / T_pairwise_ratios for the new-information content")
RES["runtime_s"] = round(time.time() - T00, 1)
json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)
log("results.json written")
log("VERDICT:", RES["verdict"])
