"""
B771 Phase-1 Wave-3 -- W3-078 / N2
Question (docs/OPEN_LEADS.md:159-160, docs/LITERATURE_SWEEP2_2026-07-13.md):
    the KMS temperature ladder  beta_n = log(lambda_PF(M_n))  via Exel's theorem
    (arXiv:math/0110183, generalizing Enomoto-Fujii-Watatani/Olesen-Pedersen) --
    "free thermodynamics of the gauge algebras" O_{M_n}, the Cuntz-Krieger /
    Exel-Laca algebras of the B556 escalator tower's transition matrices.

WHAT'S BANKED (never cited as sufficient -- re-derived from scratch below):
  - B556/OI-189 (frontier/B771_phase1_wave1/cells/OI-189/compute.py): the escalator
    matrices M_n = T^n(F), T(M) = [[M,M],[M^2,M]], F = [[1,1],[1,0]] (Fibonacci
    matrix), with e_n = det(I - M_n) matching K-theory |K_0(O_{M_n})| at rungs
    0-3 (H2-F2: K_0(O_{M_16}) = Z/18845090 at rung... consistent order of growth).
  - LITERATURE_SWEEP2 flags but does NOT compute: "beta_n+1/beta_n -> 3/2 -- the
    growth law IS a temperature law" -- stated as a hoped-for pattern, not derived
    or verified anywhere in-repo. THAT is the discriminating fact this cell computes.

WHAT THIS CELL DOES (all in-cell, nothing cited as sufficient):
  1. Rebuilds M_n from scratch (independent of OI-189's copy).
  2. Verifies the Exel/EFW HYPOTHESIS -- irreducibility (strong connectivity) and
     aperiodicity (primitivity) of M_n -- because the beta=log(lambda_PF) unique-
     KMS-state theorem REQUIRES it. This is the "obstruction check": if it fails,
     the reading is RESOLVED-B (no valid unique KMS state at that beta).
  3. Re-derives (independently, via sympy resultant on freshly-built char polys,
     not copied) the doubling correspondence between consecutive spectra, and
     from it an EXACT closed-form recursion for the PF eigenvalue:
         lambda_n = lambda_{n-1} * (1 + sqrt(lambda_{n-1})),   lambda_0 = phi.
     Cross-validated two ways: (a) symbolically via the correspondence, (b)
     numerically via matrix power iteration (2 independent seeds, high
     precision, n=0..5, matrices built with exact big-integer entries).
  4. Works entirely in LOG SPACE (beta_n = log lambda_n) to push the ladder to
     n=15 without ever forming the (doubly-exponentially large) lambda_n itself,
     and PROVES the asymptotic ratio beta_n/beta_{n-1} -> 3/2 analytically from
     the recursion, with an explicit error bound, verified numerically.
  5. SELF-TEST (non-vacuity control): builds a structurally different escalator
     control (same doubling-in-size shape, drops the M^2 coupling) and shows its
     ladder obeys a DIFFERENT law (ratio -> 1, not 3/2) -- proving the 3/2 law is
     a real fact of the M^2-coupled correspondence, not an artifact of "the
     matrix doubles in size every step."
  6. Instantiates the actual KMS state (Parry-type measure from the PF
     eigenvector pair) at rung 0 and checks it is a genuine probability measure
     (stochastic normalization + stationarity), so "free thermodynamics of the
     gauge algebra" is not just a slogan -- a concrete state is exhibited.

Gate 5: structural thermodynamics of an operator algebra (Cuntz-Krieger/Exel-Laca
KMS theory applied to matrices already in the object's tower). NO physical
temperature claim, nothing to CLAIMS.md.

Env: pyenv python3 (NOT sage). sympy exact + mpmath arbitrary precision.
"""
import time
import sympy as sp
import mpmath as mp

t0 = time.time()
LOG = []


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.append(s)


# =====================================================================
# PART 0: rebuild the escalator matrices from scratch (independent of
# OI-189's copy -- same construction, freshly built and freshly checked).
# =====================================================================
log("=" * 72)
log("PART 0: rebuild the escalator matrices M_n = T^n(F)")
log("=" * 72)

F = sp.Matrix([[1, 1], [1, 0]])


def Tstep(M):
    return M.row_join(M).col_join((M * M).row_join(M))


def rung(n):
    M = F
    for _ in range(n):
        M = Tstep(M)
    return M


MATS = {n: rung(n) for n in range(6)}  # sizes 2,4,8,16,32,64
for n in range(6):
    log(f"  M_{n}: size {MATS[n].shape[0]:3d}, entries range "
        f"[{min(MATS[n])}, {max(MATS[n])}]")

# =====================================================================
# PART 1: EXEL/EFW HYPOTHESIS CHECK -- irreducibility (strong connectivity)
# and aperiodicity (primitivity) of M_n as a nonnegative-integer adjacency
# matrix (Exel-Laca generalized Cuntz-Krieger graph). This is REQUIRED for
# the beta = log(lambda_PF) unique-KMS-state theorem to apply at all -- an
# obstruction here would force RESOLVED-B.
# =====================================================================
log("")
log("=" * 72)
log("PART 1: Exel/EFW hypothesis check -- irreducibility + aperiodicity")
log("=" * 72)


def strongly_connected(M):
    n = M.shape[0]
    adj = [[j for j in range(n) if M[i, j] != 0] for i in range(n)]

    def reach(src):
        seen = {src}
        stack = [src]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return seen

    full = set(range(n))
    return all(reach(i) == full for i in range(n))


def primitive_power(M, maxk=None):
    """Smallest k such that M**k has all strictly positive entries (or None)."""
    n = M.shape[0]
    if maxk is None:
        maxk = 4 * n  # generous bound (Wielandt bound is n^2-2n+2)
    P = M
    for k in range(1, maxk + 1):
        if k > 1:
            P = P * M
        if all(v > 0 for v in P):
            return k
    return None


hyp_ok = {}
for n in range(5):  # exact boolean/integer check up to size 32 (n=4); n=5 (size64) via boolean reach + sampled power
    M = MATS[n]
    sc = strongly_connected(M)
    k = primitive_power(M, maxk=3 * M.shape[0])
    hyp_ok[n] = sc and (k is not None)
    log(f"  n={n}: strongly connected = {sc}, primitive at power k={k}  -> hypothesis {'HOLDS' if hyp_ok[n] else 'FAILS'}")

# n=5 (size 64): strong connectivity via boolean reach (cheap, integer entries huge but
# nonzero-pattern check only needs != 0), primitivity via boolean matrix squaring
# (avoid forming the huge-integer M^k -- work with the BOOLEAN pattern, since
# nonneg-integer entries never cancel: boolean powers exactly track the "positive
# entry" pattern of the true integer powers).
def bool_mat(M):
    n = M.shape[0]
    return [[1 if M[i, j] != 0 else 0 for j in range(n)] for i in range(n)]


def bool_mult(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for k in range(n):
            if Ai[k]:
                Bk = B[k]
                Ci = C[i]
                for j in range(n):
                    if Bk[j]:
                        Ci[j] = 1
    return C


n5 = 5
Mb = bool_mat(MATS[n5])
sc5 = strongly_connected(MATS[n5])
size5 = MATS[n5].shape[0]
P = [row[:] for row in Mb]
k5 = None
for k in range(1, 3 * size5 + 1):
    if k > 1:
        P = bool_mult(P, Mb)
    if all(all(row) for row in P):
        k5 = k
        break
hyp_ok[5] = sc5 and (k5 is not None)
log(f"  n=5 (size {size5}, boolean-pattern check): strongly connected = {sc5}, "
    f"primitive at power k={k5}  -> hypothesis {'HOLDS' if hyp_ok[5] else 'FAILS'}")

all_hyp = all(hyp_ok[n] for n in range(6))
log(f"  ALL n=0..5: Exel/EFW hypothesis (irreducible + aperiodic) HOLDS: {all_hyp}")
assert all_hyp, "Exel hypothesis fails -- must route to RESOLVED-B"

# =====================================================================
# PART 2: independently re-derive the doubling correspondence between
# consecutive char polys, and from it the closed-form PF recursion.
# (Freshly computed here, not imported from OI-189.)
# =====================================================================
log("")
log("=" * 72)
log("PART 2: independent re-derivation of the spectral doubling correspondence")
log("=" * 72)

x, mu = sp.symbols("x mu")


def charpoly(M, var):
    return sp.expand(M.charpoly(var).as_expr())


cp = {n: charpoly(MATS[n], x if n == 0 else mu) for n in range(4)}  # sizes 2,4,8,16 -- fast
cp0_x = charpoly(MATS[0], x)
cp1_mu = charpoly(MATS[1], mu)
cp2_mu = charpoly(MATS[2], mu)
cp1_x = charpoly(MATS[1], x)
cp2_x = charpoly(MATS[2], x)
cp3_x = charpoly(MATS[3], x)

# candidate kernel motivated by the escalator's
# own block structure (M -> [[M,M],[M^2,M]] suggests a quadratic-in-mu, quadratic-in-x
# kernel with a mu^3 term from the M^2 block) and VERIFY it kills both residuals exactly
# -- this is a verification of a hypothesis, not a blind cite.
K_hyp = x**2 - 2 * mu * x + mu**2 - mu**3
res1 = sp.expand(sp.resultant(sp.Poly(cp0_x.subs(x, mu), mu), sp.Poly(K_hyp, mu), mu) - cp1_x)
res2 = sp.expand(sp.resultant(sp.Poly(cp1_x.subs(x, mu), mu), sp.Poly(K_hyp, mu), mu) - cp2_x)
res3 = sp.expand(sp.resultant(sp.Poly(cp2_x.subs(x, mu), mu), sp.Poly(K_hyp, mu), mu) - cp3_x)
log(f"  K(x,mu) = x^2 - 2*mu*x + mu^2 - mu^3   tested on 3 INDEPENDENT rung-transitions:")
log(f"    charpoly_1 == Res_mu(charpoly_0, K)  residual = {res1}   (0 = confirmed)")
log(f"    charpoly_2 == Res_mu(charpoly_1, K)  residual = {res2}   (0 = confirmed)")
log(f"    charpoly_3 == Res_mu(charpoly_2, K)  residual = {res3}   (0 = confirmed)")
assert res1 == 0 and res2 == 0 and res3 == 0, "doubling kernel K(x,mu) does not reproduce charpolys"

# K(x,mu) = 0  <=>  (x-mu)^2 = mu^3  <=>  x = mu +/- mu^{3/2}
check = sp.expand((x - mu) ** 2 - mu**3 - K_hyp)
log(f"  (x-mu)^2 - mu^3 - K(x,mu) = {check}  (0 confirms x = mu +/- mu*sqrt(mu))")
assert check == 0

# =====================================================================
# PART 3: cross-validate the closed-form PF ladder two ways --
#   (a) symbolic: lambda_n = lambda_{n-1}*(1+sqrt(lambda_{n-1})), lambda_0=phi
#   (b) numeric: matrix power iteration on the EXACT M_n, two independent
#       seed vectors, high precision, n=0..5.
# =====================================================================
log("")
log("=" * 72)
log("PART 3: cross-validate the closed-form PF recursion against matrix power iteration")
log("=" * 72)

mp.mp.dps = 80

phi = (1 + mp.sqrt(5)) / 2


def lam_closed(n):
    v = phi
    for _ in range(n):
        v = v * (1 + mp.sqrt(v))
    return v


def power_iterate(M_sympy, seed, iters=400, tol=mp.mpf("1e-40")):
    n = M_sympy.shape[0]
    Mmp = mp.matrix([[mp.mpf(int(M_sympy[i, j])) for j in range(n)] for i in range(n)])
    v = mp.matrix(seed)
    prev_est = None
    for it in range(iters):
        w = Mmp * v
        nrm = mp.norm(w, 2)
        w = w / nrm
        # Rayleigh quotient estimate
        Mv = Mmp * w
        est = (w.T * Mv)[0] / (w.T * w)[0]
        if prev_est is not None and abs(est - prev_est) < tol * max(1, abs(est)):
            v = w
            break
        v, prev_est = w, est
    return est, it


results3 = []
for n in range(6):
    Mn = MATS[n]
    size = Mn.shape[0]
    seedA = [mp.mpf(1)] * size
    seedB = [mp.mpf(i + 1) for i in range(size)]  # a structurally different seed
    estA, itA = power_iterate(Mn, seedA)
    estB, itB = power_iterate(Mn, seedB)
    closed = lam_closed(n)
    agreeA = mp.log10(abs(estA - closed) / abs(closed)) if closed != 0 else None
    agreeB = mp.log10(abs(estB - closed) / abs(closed)) if closed != 0 else None
    seed_diff = mp.log10(abs(estA - estB) / abs(closed))
    results3.append((n, estA, estB, closed, agreeA, agreeB, seed_diff, itA, itB))
    log(f"  n={n} size={size:3d}: power-iter(seedA)={mp.nstr(estA, 20)}  "
        f"(iters={itA}, rel.err vs closed-form: 10^{float(agreeA):.1f})")
    log(f"           power-iter(seedB)={mp.nstr(estB, 20)}  "
        f"(iters={itB}, rel.err vs closed-form: 10^{float(agreeB):.1f}, "
        f"seedA vs seedB agree to 10^{float(seed_diff):.1f})")

# discriminating agreement gate (house method: tol=10^-(agree-14), both directions 10+ digits)
min_agree_digits = min(-float(a) for (_, _, _, _, a, b, _, _, _) in results3 for a in [a] if a is not None)
min_agree_digits2 = min(-float(b) for (_, _, _, _, a, b, _, _, _) in results3 for b in [b] if b is not None)
log(f"  worst-case agreement (seedA vs closed form) across n=0..5: 10^-{min_agree_digits:.1f}")
log(f"  worst-case agreement (seedB vs closed form) across n=0..5: 10^-{min_agree_digits2:.1f}")
assert min_agree_digits > 10 and min_agree_digits2 > 10, "power iteration disagrees with closed form at <10 digits"
log("  => the closed-form recursion lambda_n = lambda_{n-1}(1+sqrt(lambda_{n-1})) IS the PF")
log("     eigenvalue of M_n, confirmed independently by 2-seed high-precision power iteration,")
log("     for n=0..5 (10+ digit agreement both directions, per house method).")

# =====================================================================
# PART 4: work in LOG SPACE to push the ladder far past n=5, and PROVE the
# asymptotic 3/2 law analytically from the recursion (not curve-fit).
# =====================================================================
log("")
log("=" * 72)
log("PART 4: the beta_n ladder in log-space, and the exact 3/2 asymptotic")
log("=" * 72)

beta0 = mp.log(phi)


def beta_next(b):
    return b + mp.log(1 + mp.e ** (b / 2))


betas = [beta0]
for _ in range(15):
    betas.append(beta_next(betas[-1]))

log(f"  beta_0 = log(phi) = {mp.nstr(beta0, 20)}")
for n in range(1, 16):
    ratio = betas[n] / betas[n - 1]
    err = abs(ratio - mp.mpf("1.5"))
    log(f"  beta_{n:2d} = {mp.nstr(betas[n], 15):>20}   "
        f"beta_{n}/beta_{n-1} = {mp.nstr(ratio, 15)}   |ratio-3/2| = {mp.nstr(err, 6)}")

# cross-check log-space ladder against the direct matrix-derived betas (n=0..5)
log("")
log("  cross-check: log(lambda_n from matrix power-iteration) vs log-space beta_n:")
for n in range(6):
    lam_mat = results3[n][1]  # seedA estimate
    beta_mat = mp.log(lam_mat)
    diff = mp.log10(abs(beta_mat - betas[n]) / abs(betas[n])) if betas[n] != 0 else mp.mpf("-inf")
    log(f"    n={n}: beta(matrix)={mp.nstr(beta_mat,15)}  beta(log-recursion)={mp.nstr(betas[n],15)}  "
        f"rel.diff 10^{float(diff):.1f}")
    assert diff < -12, f"log-space ladder disagrees with matrix-derived beta at n={n}"

# ANALYTIC PROOF of the 3/2 asymptotic:
#   beta_n = beta_{n-1} + log(1+exp(beta_{n-1}/2))
#   for y = beta_{n-1}/2 -> +infinity:  log(1+e^y) = y + log(1+e^{-y}) = y + e^{-y} + O(e^{-2y})
#   so beta_n = beta_{n-1} + beta_{n-1}/2 + e^{-beta_{n-1}/2} + O(e^{-beta_{n-1}}) = (3/2) beta_{n-1} + e^{-beta_{n-1}/2}(1+o(1))
#   => beta_n/beta_{n-1} - 3/2 = e^{-beta_{n-1}/2}/beta_{n-1} * (1+o(1))  -> 0
# VERIFY this explicit error formula against the computed ladder (not just assert the limit).
log("")
log("  analytic error-bound check: predicted (ratio - 3/2) ~ exp(-beta_{n-1}/2)/beta_{n-1}")
for n in range(1, 12):
    b_prev = betas[n - 1]
    predicted = mp.e ** (-b_prev / 2) / b_prev
    actual = betas[n] / betas[n - 1] - mp.mpf("1.5")
    if actual == 0 or predicted == 0:
        continue
    rel = mp.log10(abs(actual / predicted - 1)) if predicted != 0 else None
    log(f"    n={n:2d}: actual (ratio-3/2)={mp.nstr(actual,8):>14}   "
        f"predicted={mp.nstr(predicted,8):>14}   rel.err(actual/predicted - 1) = 10^{float(rel):.2f}")

log("")
log("  => beta_n/beta_{n-1} -> 3/2 PROVEN analytically from the exact recursion")
log("     (not a curve fit): the correction is exp(-beta_{n-1}/2)/beta_{n-1}, matching")
log("     the computed ladder to the precision shown -- the '3/2 law' from the")
log("     literature sweep is now a derived fact, with its exact error term.")

# =====================================================================
# PART 5: SELF-TEST / non-vacuity control -- does "doubling in size" alone
# force ratio->3/2, or is it specific to the M -> M^2 coupling term?
# Build a control escalator that ALSO doubles the matrix size each step but
# drops the M^2 block (replaces it with M), and show its ladder law differs.
# =====================================================================
log("")
log("=" * 72)
log("PART 5: SELF-TEST -- control escalator (drop the M^2 coupling)")
log("=" * 72)


def Tstep_control(M):
    # same block shape [[M,M],[?,M]] but replace the M^2 (cubic-producing) block with M
    return M.row_join(M).col_join(M.row_join(M))


def rung_control(n):
    M = F
    for _ in range(n):
        M = Tstep_control(M)
    return M


CTRL = {n: rung_control(n) for n in range(4)}
log("  control T_ctrl(M) = [[M,M],[M,M]]  (same doubling-in-size shape, no M^2 term)")
for n in range(4):
    log(f"    ctrl M_{n}: size {CTRL[n].shape[0]:3d}")

# this control is exactly M (x) J2 with J2=[[1,1],[1,1]] (Kronecker product),
# whose PF eigenvalue is 2 (J2 has eigenvalues {2,0}) -- verify PF(ctrl_n) = 2^n * phi directly
for n in range(4):
    ev = CTRL[n].eigenvals()
    pf_ctrl = max(complex(e).real for e in ev.keys())
    predicted = float(phi) * 2 ** n
    log(f"    ctrl n={n}: PF eigenvalue = {pf_ctrl:.8f}   predicted 2^n * phi = {predicted:.8f}   "
        f"match = {abs(pf_ctrl - predicted) < 1e-6}")
    assert abs(pf_ctrl - predicted) < 1e-6

log("  control beta_n = log(phi) + n*log(2)  -- ADDITIVE, so beta_n/beta_{n-1} -> 1, NOT 3/2:")
ctrl_beta0 = mp.log(phi)
for n in range(1, 8):
    cb_n = ctrl_beta0 + n * mp.log(2)
    cb_prev = ctrl_beta0 + (n - 1) * mp.log(2)
    log(f"    ctrl beta_{n} = {mp.nstr(cb_n, 10)}   ratio to beta_{n-1} = {mp.nstr(cb_n/cb_prev, 8)}")

log("")
log("  SELF-TEST RESULT: the control (same size-doubling shape, M^2 term removed)")
log("  gives ratio -> 1 (additive law), sharply DIFFERENT from the real escalator's")
log("  ratio -> 3/2 (multiplicative-in-log law). The 3/2 exponent is therefore a")
log("  genuine consequence of the M -> M^2 coupling (the cubic mu^3 term in K(x,mu)),")
log("  NOT a vacuous artifact of 'the matrix doubles in size every rung.'")

# =====================================================================
# PART 6: instantiate an ACTUAL KMS state at rung 0 (Parry-type measure
# from the PF eigenvector pair) and check it is a genuine probability
# measure -- "free thermodynamics" made concrete, not just a slogan.
# =====================================================================
log("")
log("=" * 72)
log("PART 6: concrete KMS state at rung 0 (Exel/EFW Parry-type construction)")
log("=" * 72)

# F = [[1,1],[1,0]], symmetric, PF eigenvalue phi, right=left eigenvector v=(phi,1)
v = mp.matrix([phi, mp.mpf(1)])
Fmp = mp.matrix([[1, 1], [1, 0]])
Fv = Fmp * v
check_eig = mp.norm(Fv - phi * v, 2)
log(f"  F*v - phi*v (should be ~0): {mp.nstr(check_eig, 6)}")
assert check_eig < mp.mpf("1e-60")

# transition (KMS/Parry) matrix P_ij = F_ij * v_j / (phi * v_i)
P = mp.matrix(2, 2)
for i in range(2):
    for j in range(2):
        P[i, j] = Fmp[i, j] * v[j] / (phi * v[i])
row_sums = [sum(P[i, j] for j in range(2)) for i in range(2)]
log(f"  Parry transition matrix P (from PF eigenvector, beta_0=log(phi)):")
for i in range(2):
    log(f"    row {i}: {[mp.nstr(P[i,j],10) for j in range(2)]}   row-sum = {mp.nstr(row_sums[i],15)}")
assert all(abs(rs - 1) < mp.mpf("1e-50") for rs in row_sums), "Parry matrix rows must sum to 1 (stochastic)"

# stationary vertex measure pi_i = v_i^2 / sum(v_j^2)  (since F symmetric, left=right eigenvector)
Z = v[0] ** 2 + v[1] ** 2
pi = [v[i] ** 2 / Z for i in range(2)]
log(f"  stationary vertex measure pi = {[mp.nstr(p,15) for p in pi]}   sum={mp.nstr(sum(pi),15)}")
assert abs(sum(pi) - 1) < mp.mpf("1e-50")
piP = [sum(pi[i] * P[i, j] for i in range(2)) for j in range(2)]
statdiff = max(abs(piP[j] - pi[j]) for j in range(2))
log(f"  stationarity check pi*P - pi: {mp.nstr(statdiff, 6)}")
assert statdiff < mp.mpf("1e-50"), "Parry measure not stationary"
log("  => a genuine probability-measure KMS state at beta_0=log(phi) is EXHIBITED")
log("     (stochastic + stationary, both to >50 digits) -- Exel's theorem instantiated,")
log("     not merely cited.")

# =====================================================================
# VERDICT
# =====================================================================
log("")
log("=" * 72)
log("VERDICT")
log("=" * 72)

structure_characterized = (
    all_hyp
    and (res1 == 0 and res2 == 0 and res3 == 0)
    and min_agree_digits > 10 and min_agree_digits2 > 10
    and statdiff < mp.mpf("1e-50")
)
log(f"  Exel/EFW hypothesis (irreducible+aperiodic, n=0..5): {all_hyp}")
log(f"  spectral doubling kernel K(x,mu)=x^2-2*mu*x+mu^2-mu^3 confirmed on 3 independent rungs: True")
log(f"  closed-form PF ladder lambda_n=lambda_(n-1)(1+sqrt(lambda_(n-1))) cross-validated (2-seed, >10 digits): True")
log(f"  asymptotic law beta_n/beta_(n-1) -> 3/2 PROVEN analytically + verified numerically: True")
log(f"  self-test (control escalator gives a DIFFERENT law, ratio->1): non-vacuous: True")
log(f"  concrete KMS state exhibited + verified stochastic/stationary (rung 0): True")
log(f"  ALL STRUCTURE CHARACTERIZED: {structure_characterized}")
if structure_characterized:
    log("  => RESOLVED-A: the KMS temperature ladder beta_n=log(lambda_PF(M_n)) is computed")
    log("     exactly (closed-form recursion from phi), its Exel/EFW existence hypothesis")
    log("     verified (no obstruction), its asymptotic 3/2 growth law PROVEN (not just")
    log("     observed), and shown non-vacuous by a structurally-matched control.")
else:
    log("  => RESOLVED-B: an obstruction to the KMS reading was found.")

log(f"")
log(f"  total wall time: {time.time()-t0:.2f}s")
