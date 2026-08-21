#!/usr/bin/env python3
"""
V1_verify.py -- value-campaign cell V-1: extend the banked Kashaev-tower
sub-leading arithmetic by one order (C_3), and attempt a second (C_4).

BACKGROUND (banked, not re-derived here; origin-axiom arc B1120/L180)
-----------------------------------------------------------------------
The figure-eight knot (4_1) Kashaev invariant

    J_N = sum_{k=0}^{N-1} prod_{j=1}^{k} |1 - e^{2*pi*i*j/N}|^2
        = sum_{k=0}^{N-1} prod_{j=1}^{k} 4*sin^2(pi*j/N)      (real, positive, finite sum)

has the asymptotic expansion

    J_N ~ N^{3/2} * exp(Vol*N/2pi) * (C_0 + C_1/N + C_2/N^2 + C_3/N^3 + ...),   Vol = vol(4_1),

with the trace field Q(sqrt(-3)) and BANKED:
    C_0 = 3^{-1/4} = |disc Q(sqrt(-3))|^{-1/4}
    C_1 = (11/108)   * sqrt(3) * pi   * C_0     [odd k  -> rational * sqrt(3), confirmed ~9e-33]
    C_2 = (697/7776) * pi^2           * C_0     [even k -> plain rational,      confirmed ~4e-29]
C_3 was previously reached only to ~11 trusted digits -- not enough to PSLQ-search confidently
at the height the C_1/C_2 pattern suggests (~17-18 digits needed). This bench pushes N far
beyond the banked run's ceiling (N~2.9e6) to try to close that gap, and takes a first look at C_4.

THE PREDICTION -- STATED HERE, BEFORE ANY PSLQ CALL BELOW
-----------------------------------------------------------------------
J_N is manifestly real (a sum of nonnegative real terms). If the standard WKB/resurgence
picture for hyperbolic 3-manifolds holds (coefficients kappa_k in the trace field Q(sqrt(-3))
multiplying (2*pi*i/N)^k), reality of J_N forces a PARITY SPLIT once C_k is divided by C_0*pi^k
(the convention the banked C_1, C_2 already instantiate):

    k EVEN  ->  C_k / (C_0 * pi^k)  is a PLAIN RATIONAL              (b_k = 0 in kappa_k = a_k)
    k ODD   ->  C_k / (C_0 * pi^k)  is a RATIONAL MULTIPLE of sqrt(3) (a_k = 0 in kappa_k = b_k*sqrt(-3))

Applied to the two new targets of this bench:
    C_3 (k=3, ODD)  PREDICTED:  C_3 = q3 * sqrt(3) * pi^3 * C_0,   q3 in Q
    C_4 (k=4, EVEN) PREDICTED:  C_4 = q4 * pi^4 * C_0,             q4 in Q
Denominators of q3, q4 are expected (not assumed as a search constraint -- just a prior, stated
for the record) to be {2,3}-smooth by analogy with 108 = 2^2*3^3 (C_1) and 7776 = 2^5*3^5 (C_2).

ANTI-COINCIDENCE CONTROLS (must find NOTHING if the pattern is genuine, run alongside the
predicted-basis search, not after it and not cherry-picked):
    - C_3 tested against plain-rational * pi^3 * C_0 (the WRONG parity: Q instead of Q(sqrt3))
    - C_4 tested against rational*sqrt(3) * pi^4 * C_0 (the WRONG parity: Q(sqrt3) instead of Q)
    - both tested against sqrt(3)-alone, 1/sqrt(3), pi^2, 4*pi bases (wrong power of pi / wrong
      parity structure) -- the same "wrong basis" family the banked C_1/C_2 search used and that
      correctly found nothing there.

METHOD (reusing the approach of the banked bench; the two bugs it caught are avoided BY
CONSTRUCTION here, not just avoided by luck)
-----------------------------------------------------------------------
1. PRECISION-CONTEXT ORDERING (bug avoided): Vol and all "exact" constants (p=3/2, growth_rate
   = Vol/2pi, C0_target = 3^-1/4, pi, sqrt(3)) are computed ONCE at DPS_VOL (very high), frozen
   with a unary "+", and passed onward as high-precision DECIMAL STRINGS to every consumer
   (including every multiprocessing worker, which runs in its own fresh process with its own
   mpmath context) -- so every downstream use ROUNDS DOWN from a fully-accurate value at
   whatever its OWN working precision is, never rounds UP from something computed by accident
   at mpmath's low default dps. mp.mp.dps in the main process is not lowered until after this
   freeze.
2. MONOMIAL ILL-CONDITIONING (bug avoided): all polynomial-in-1/N fits use a rescaled-CHEBYSHEV
   basis (see poly_fit_1_over_N), never raw monomials in 1/N, which the banked bench found
   ill-conditioned on narrow-relative-range windows at high truncation order K.
3. J_N via the fast angle-addition recursion (one complex multiply per step), cross-validated
   against a direct per-term mp.sin() path and hand-derived exact integers (N=1..4 -> 1,5,13,27).
4. PARALLELIZATION (new in this bench, not in the banked one): J_N(N) for different N are
   completely independent, so they are computed via a multiprocessing.Pool -- each worker sets
   its own mp.mp.dps and reconstructs the frozen constants from the high-precision strings
   before computing. This is what makes reaching N far beyond the banked run's ceiling tractable
   inside the time budget on a shared machine (NWORKERS defaults to 6, leaving headroom rather
   than claiming every core).
5. Multiple non-overlapping windows (W1..W5, N from ~2000 to 35,000,000 -- roughly 12x the
   banked run's top N of 2.9e6) + a POOLED fit, at several truncation orders K each, read for
   (i) within-window K-convergence and (ii) cross-window agreement -- "trusted digits" is the
   minimum of the two, exactly as the banked bench defined it, extended here to also cover C_4.
6. A precision-doubling cross-check (dps 200 -> 320) on the W4 subset.
7. PSLQ recognition sweep on C_1..C_4 (C_1, C_2 as a re-verification/continuity control against
   the banked closed forms; C_3, C_4 as the new targets), against the same 11-base family the
   banked bench used, each swept against both Q and Q(sqrt3) -- which mechanically IS the
   predicted-vs-wrong-basis comparison described above, not a separate step.

Self-contained; mpmath only; no repo imports. No machine-specific paths in the logic: output
directory is $V1_OUTDIR if set, else the directory this script lives in. Worker count is
$V1_NWORKERS if set (default 6).
"""
from __future__ import annotations

import json
import os
import sys
import time
import pickle
from multiprocessing import Pool

import mpmath as mp

# =============================================================================
# Configuration (env-var overridable; no hardcoded machine paths)
# =============================================================================
DPS_VOL = 400          # "exact" constants frozen once here, highest precision needed anywhere
DPS_MAIN = 200          # main working precision for the bulk J_N/R_N generation
DPS_CROSS = 320         # precision-doubling cross-check
NWORKERS = int(os.environ.get("V1_NWORKERS", "6"))
OUTDIR = os.environ.get("V1_OUTDIR") or os.path.dirname(os.path.abspath(__file__)) or "."
CKPT_PATH = os.path.join(OUTDIR, "V1_checkpoint.pkl")


def s(x, digits=30):
    return mp.nstr(x, digits)


# =============================================================================
# 0. Vol(4_1), independently, from closed forms (dilog / Lobachevsky)
# =============================================================================

def compute_vol_fig8():
    with mp.workdps(DPS_VOL):
        def Li2(z):
            return mp.polylog(2, z)
        routeA = 2 * mp.im(Li2(mp.e ** (1j * mp.pi / 3)))

        def lobachevsky(theta):
            return mp.mpf('0.5') * mp.im(Li2(mp.e ** (2j * theta)))
        v3 = 3 * lobachevsky(mp.pi / 3)
        routeB = 2 * v3
        agree = abs(routeA - routeB) < mp.mpf(10) ** (-(DPS_VOL - 15))
        return +routeA, +routeB, agree


# =============================================================================
# 1. J_N(4_1): fast angle-addition path + direct cross-validation path
# =============================================================================

def J_N_trig_fast(N: int, renorm_every: int = 2000) -> mp.mpf:
    """J_N = sum_{k=0}^{N-1} prod_{j=1}^{k} 4 sin^2(pi j/N), sin(pi j/N) advanced by ONE
    fixed-angle complex multiply per step (angle-addition recursion)."""
    theta = mp.pi / N
    c1 = mp.cos(theta)
    s1 = mp.sin(theta)
    c, sN = mp.mpf(1), mp.mpf(0)
    total = mp.mpf(1)
    prod = mp.mpf(1)
    for j in range(1, N):
        c, sN = c * c1 - sN * s1, sN * c1 + c * s1
        if renorm_every and j % renorm_every == 0:
            norm = mp.sqrt(c * c + sN * sN)
            c, sN = c / norm, sN / norm
        factor = 4 * sN * sN
        prod *= factor
        total += prod
    return total


def J_N_trig_direct(N: int) -> mp.mpf:
    """Independent code path: N direct mp.sin() calls, no recursion. Cross-validation only."""
    total = mp.mpf(1)
    prod = mp.mpf(1)
    for j in range(1, N):
        factor = 4 * mp.sin(mp.pi * j / N) ** 2
        prod *= factor
        total += prod
    return total


# =============================================================================
# 2. Multiprocessing worker: R_N at a given (N, dps), from FROZEN high-precision
#    constants passed in as decimal strings (see bug-avoidance note [1] above)
# =============================================================================

def _worker_R_N(args):
    N, dps, growth_rate_str, p_exact_str = args
    mp.mp.dps = dps
    growth_rate = mp.mpf(growth_rate_str)   # rounds DOWN from a DPS_VOL-accurate string
    p_exact = mp.mpf(p_exact_str)
    j = J_N_trig_fast(N)
    lj = mp.log(j)
    log_R = lj - p_exact * mp.log(N) - growth_rate * N
    R_N = mp.exp(log_R)
    return (N, mp.nstr(R_N, dps + 20))


def freeze_strings(*vals, digits=DPS_VOL + 10):
    with mp.workdps(DPS_VOL):
        return [mp.nstr(+v, digits) for v in vals]


def parallel_R_N(pool, Ns, dps, gr_str, pe_str, have=None):
    """Compute R_N for every N in Ns not already in `have` (a dict), via the shared pool.
    Returns a NEW dict N->mp.mpf covering exactly Ns (reusing `have` where present)."""
    have = have or {}
    todo = [N for N in Ns if N not in have]
    out = dict(have)
    if todo:
        args = [(N, dps, gr_str, pe_str) for N in todo]
        for N, R_str in pool.imap_unordered(_worker_R_N, args):
            out[N] = mp.mpf(R_str)
    return {N: out[N] for N in Ns}


# =============================================================================
# 3. Linear algebra: rescaled-Chebyshev basis fit (avoids monomial ill-conditioning)
# =============================================================================

def _poly_mul_trunc(p, q, K):
    result = [mp.mpf(0)] * K
    for i in range(min(len(p), K)):
        if p[i] == 0:
            continue
        for j in range(min(len(q), K - i)):
            result[i + j] += p[i] * q[j]
    return result


def _rescaled_cheb_basis(xs, K):
    xmin, xmax = min(xs), max(xs)
    center = (xmin + xmax) / 2
    halfwidth = (xmax - xmin) / 2
    alpha = 1 / halfwidth
    beta = -center / halfwidth
    lin = [2 * beta, 2 * alpha] + [mp.mpf(0)] * (K - 2)
    P = [[mp.mpf(1)] + [mp.mpf(0)] * (K - 1)]
    if K > 1:
        P.append([beta, alpha] + [mp.mpf(0)] * (K - 2))
    for k in range(2, K):
        term = _poly_mul_trunc(lin, P[k - 1], K)
        P.append([term[j] - P[k - 2][j] for j in range(K)])
    return P, center, halfwidth


def _cheb_vals(u, K):
    Tv = [mp.mpf(1)]
    if K > 1:
        Tv.append(u)
    for k in range(2, K):
        Tv.append(2 * u * Tv[-1] - Tv[-2])
    return Tv


def poly_fit_1_over_N(Ns, Rs, K):
    """Least squares fit R_N ~ sum_{k=0}^{K-1} C_k/N^k, rescaled-Chebyshev basis (QR),
    converted back to the standard power-series-in-1/N coefficients."""
    n = len(Ns)
    xs = [mp.mpf(1) / N for N in Ns]
    P, center, halfwidth = _rescaled_cheb_basis(xs, K)
    A = mp.matrix(n, K)
    b = mp.matrix(n, 1)
    for i, x in enumerate(xs):
        u = (x - center) / halfwidth
        Tv = _cheb_vals(u, K)
        for k in range(K):
            A[i, k] = Tv[k]
        b[i] = Rs[i]
    d, resid = mp.qr_solve(A, b)
    C = [mp.mpf(0)] * K
    for k in range(K):
        for j in range(K):
            C[j] += d[k] * P[k][j]
    return C, resid


def poly_exact_solve(Ns, Rs):
    K = len(Ns)
    A = mp.matrix(K, K)
    b = mp.matrix(K, 1)
    for i, N in enumerate(Ns):
        invN = mp.mpf(1) / N
        p = mp.mpf(1)
        for k in range(K):
            A[i, k] = p
            p *= invN
        b[i] = Rs[i]
    x = mp.lu_solve(A, b)
    return [x[k] for k in range(K)]


# =============================================================================
# 4. PSLQ recognition sweep
# =============================================================================

MAXCOEFF_LIST = (100, 1000, 10000, 100000, 1000000, 3000000)


def recognize_sweep(T_hp, dps_for_pslq, maxcoeff_list=MAXCOEFF_LIST, maxsteps=20000):
    """Try to recognize T as (a) rational [Q], (b) a + b*sqrt(3) [Q(sqrt3)], sweeping
    maxcoeff. Returns ALL attempts (hit or not), nothing cherry-picked."""
    attempts = []
    with mp.workdps(dps_for_pslq):
        Tm = +T_hp
        bases = {
            "Q": [Tm, mp.mpf(1)],
            "Q(sqrt3)": [Tm, mp.mpf(1), mp.sqrt(3)],
        }
        for basis_name, vec in bases.items():
            for maxcoeff in maxcoeff_list:
                r = mp.pslq(vec, maxcoeff=maxcoeff, maxsteps=maxsteps)
                found = (r is not None and r[0] != 0)
                attempts.append(dict(basis=basis_name, maxcoeff=maxcoeff, dps=dps_for_pslq,
                                      relation=(list(r) if found else None), found=found))
    return attempts


def build_candidate_bases():
    """Same 11-base family the banked C_1/C_2 search used (kept identical for direct
    comparability). Testing base B at order k via B**k, swept against BOTH Q and Q(sqrt3),
    mechanically implements the predicted-vs-wrong-parity comparison stated up front."""
    with mp.workdps(DPS_VOL):
        sqrt3 = mp.sqrt(3)
        pi = mp.pi
        return {
            "1": +mp.mpf(1),
            "pi": +pi,
            "2pi": +(2 * pi),
            "pi/sqrt3": +(pi / sqrt3),
            "2pi/sqrt3": +(2 * pi / sqrt3),
            "pi*sqrt3": +(pi * sqrt3),
            "2pi*sqrt3": +(2 * pi * sqrt3),
            "sqrt3": +sqrt3,
            "1/sqrt3": +(1 / sqrt3),
            "4pi": +(4 * pi),
            "pi^2": +(pi * pi),
        }


# predicted-correct combinations, stated BEFORE the sweep runs (used only for
# post-hoc labeling of which cells of the sweep are "the prediction" vs "anti-coincidence
# control" -- the sweep itself is exhaustive and blind to this dict).
#
# NOTE (caught testing this script in --quick mode, before the real run): the naive rule
# "odd k -> Q(sqrt3), even k -> Q" is only correct for bases with NO intrinsic sqrt(3)
# factor (m=0 below). A base that itself carries an odd power of sqrt(3) (pi/sqrt3,
# pi*sqrt3, sqrt3, 1/sqrt3, ...) FLIPS the parity: e.g. for k=1 (odd), C_1 =
# (11/108)*sqrt3*pi*C0, so T = C_1/(C0*(pi/sqrt3)^1) = C_1*sqrt3/(C0*pi) = (11/108)*3 =
# 11/36 -- a PLAIN RATIONAL, found by PSLQ as relation [36,-11] under the "Q" basis, which
# a naive classifier tags "*** WRONG-PARITY HIT ***" even though it is the exact same
# relation algebraically restated (hand-verified: 11/36 = 3*11/108 exactly). Fixed by
# computing the expected basis PER (k, base) pair from the base's own sqrt(3)-valuation
# parity, not from k alone.
BASE_SQRT3_PARITY = {   # 1 if the base carries an ODD net power of sqrt(3), else 0
    "1": 0, "pi": 0, "2pi": 0, "4pi": 0, "pi^2": 0,
    "pi/sqrt3": 1, "2pi/sqrt3": 1, "pi*sqrt3": 1, "2pi*sqrt3": 1,
    "sqrt3": 1, "1/sqrt3": 1,
}
# bases that test the WRONG POWER of pi outright (pi^0 or pi^2 instead of pi^1) -- expected
# to find NOTHING on EITHER basis, for any k; not a parity question at all.
WRONG_PI_POWER_BASES = ("1", "pi^2")


def expected_basis_kind(k, base_name):
    """Returns 'Q', 'Q(sqrt3)', or None (== expect no hit on either basis: a
    wrong-pi-power control), derived from the parity law + this base's own sqrt(3)
    content -- NOT a flat per-k lookup, and NOT a plain XOR either (a first attempt at
    this helper used `(k%2) ^ base_parity`, which is wrong for EVEN k: caught by hand
    -verifying against the actual C_2 PSLQ output before trusting it -- see below).

    Derivation: write kappa_k := C_k/(C0*pi^k), of "type" R (rational) if k even, S
    (rational*sqrt3) if k odd -- the law itself. A candidate base B = pi * sqrt(3)^m *
    (rational), so B^k carries sqrt(3)^{m*k}, itself type S iff (m*k) is odd, i.e. iff
    BOTH m and k are odd. T = kappa_k / sqrt(3)^{m*k} has type = XOR of the two types,
    using S*S=R (sqrt3*sqrt3=3, rational). So:
      k even  -> sqrt(3)^{m*k} is ALWAYS type R (m*k is even for ANY m) -> T is ALWAYS
                 type R = Q, independent of the base's own sqrt(3) content.
      k odd   -> sqrt(3)^{m*k} is type S iff m is odd -> T is type R (=Q) if the base
                 itself carries an odd sqrt(3) power, else type S (=Q(sqrt3)).
    Hand-verified: C_2 (k=2) against base=pi/sqrt3 predicts T=697/2592 (plain Q) and
    that is exactly the relation PSLQ found ([-2592,697]) -- confirms the k-even branch
    is base-independent, which the naive XOR formula got backwards.
    """
    if base_name in WRONG_PI_POWER_BASES:
        return None
    if k % 2 == 0:
        return "Q"
    base_parity = BASE_SQRT3_PARITY.get(base_name, 0)
    return "Q" if base_parity == 1 else "Q(sqrt3)"


# =============================================================================
# N-grids
# =============================================================================

def build_grids(quick: bool):
    if quick:
        CONTROL_NS = [1, 2, 3, 4, 5, 10, 20, 50, 100]
        W1 = [500, 700, 900, 1200, 1600, 2100]
        W2 = [2500, 3200, 4200, 5400, 7000, 9000]
        W3 = [11000, 14000, 18000, 23000, 29000, 37000, 47000, 60000]
        W4 = [65000, 78000, 92000, 108000, 128000, 150000, 175000, 205000]
        W5 = [220000, 260000, 305000, 360000, 420000, 495000, 580000, 680000]
        CROSS_DPS_NS = W4
    else:
        CONTROL_NS = [1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 50, 75, 100, 150, 200,
                      300, 500, 750, 1000]
        W1 = [2000, 2500, 3200, 4000, 5000, 6300, 8000, 10000, 12500, 16000, 20000]
        W2 = [25000, 32000, 40000, 50000, 63000, 80000, 100000, 125000, 160000, 200000]
        W3 = [250000, 323000, 417000, 539000, 696000, 898000, 1160000, 1499000,
              1936000, 2500000]
        W4 = [2800000, 3291000, 3869000, 4548000, 5346000, 6285000, 7388000,
              8684000, 10208000, 12000000]
        W5 = [13000000, 14512000, 16200000, 18085000, 20189000, 22537000, 25159000,
              28086000, 31353000, 35000000]
        CROSS_DPS_NS = W4  # full match -> dps-doubled check at the same K as W4's own best fit
    return dict(CONTROL=CONTROL_NS, W1=W1, W2=W2, W3=W3, W4=W4, W5=W5), CROSS_DPS_NS


# =============================================================================
# main
# =============================================================================

def main(quick: bool = False):
    t_start = time.time()
    results = {"dps_main": DPS_MAIN, "dps_cross": DPS_CROSS, "dps_vol": DPS_VOL,
               "nworkers": NWORKERS, "quick_mode": quick}

    print("=" * 92)
    print("V1 -- Kashaev tower J_N(4_1): extending the banked C_0,C_1,C_2 arithmetic pattern")
    print("      to C_3 (and attempting C_4). Value-campaign cell V-1.")
    print("=" * 92)

    # -------------------------------------------------------------------
    # Step 0: Vol(4_1) + ALL "exact" constants, frozen at DPS_VOL BEFORE
    # mp.mp.dps is ever lowered in this (main) process. See bug-avoidance note [1].
    # -------------------------------------------------------------------
    print(f"\n[0] Vol(4_1) independently (dps={DPS_VOL}):")
    volA, volB, vol_agree = compute_vol_fig8()
    Vol = volA
    print(f"    route A (2*Im Li2(e^(i pi/3))): {s(volA, 45)}")
    print(f"    route B (2*3*Lobachevsky(pi/3)): {s(volB, 45)}")
    print(f"    agree to working precision: {vol_agree}")
    results["vol"] = {"route_A": s(volA, 60), "route_B": s(volB, 60), "agree": vol_agree}

    with mp.workdps(DPS_VOL):
        p_exact = +(mp.mpf(3) / 2)
        two_pi = +(2 * mp.pi)
        growth_rate = +(Vol / two_pi)
        C0_target = +(mp.mpf(3) ** (-mp.mpf(1) / 4))
    print(f"    growth_rate = Vol/2pi = {s(growth_rate, 40)}")
    print(f"    C_0 target = 3^(-1/4) = {s(C0_target, 45)}")
    results["C0_target_3^-1/4"] = s(C0_target, 60)

    gr_str, pe_str = freeze_strings(growth_rate, p_exact)

    # -------------------------------------------------------------------
    # THE PREDICTION -- stated and recorded HERE, before any PSLQ call below.
    # -------------------------------------------------------------------
    prediction = {
        "law": "k even -> C_k/(C0*pi^k) in Q;  k odd -> C_k/(C0*pi^k) in Q*sqrt(3)",
        "C_3_predicted_form": "C_3 = q3 * sqrt(3) * pi^3 * C0,  q3 rational, {2,3}-smooth denom expected",
        "C_4_predicted_form": "C_4 = q4 * pi^4 * C0,  q4 rational, {2,3}-smooth denom expected",
        "anti_coincidence_controls": [
            "C_3 vs plain-rational*pi^3*C0 (wrong parity: Q not Q(sqrt3))",
            "C_4 vs rational*sqrt3*pi^4*C0 (wrong parity: Q(sqrt3) not Q)",
            "both vs sqrt3-alone, 1/sqrt3, pi^2, 1 (wrong power of pi / no pi)",
        ],
        "stated_before_pslq": True,
    }
    print(f"\n[PREDICTION] (stated before any PSLQ call this run)")
    print(f"    {prediction['C_3_predicted_form']}")
    print(f"    {prediction['C_4_predicted_form']}")
    results["prediction"] = prediction

    # -------------------------------------------------------------------
    # Step 1: hand control (N=1..4) + fast-vs-direct cross-validation. Small N;
    # done directly in the main process (cheap; no need to parallelize).
    # -------------------------------------------------------------------
    mp.mp.dps = DPS_MAIN  # main process context lowered only NOW, after the freeze above
    print(f"\n[1] CONTROL: hand-derived exact values (dps={DPS_MAIN})")
    hand = {1: 1, 2: 5, 3: 13, 4: 27}
    tol = mp.mpf(10) ** (-(DPS_MAIN - 20))
    control_rows = []
    all_hand_pass = True
    for N, expected in hand.items():
        jf = J_N_trig_fast(N)
        d = abs(jf - expected)
        ok = d < tol
        all_hand_pass &= ok
        print(f"    N={N}: J_N_fast={s(jf, 15)}  expected={expected}  diff={s(d, 4)}  PASS={ok}")
        control_rows.append(dict(N=N, expected=expected, diff=s(d, 6), pass_=ok))
    results["control_hand_check"] = {"rows": control_rows, "all_pass": all_hand_pass}
    if not all_hand_pass:
        print("    ABORT: hand-check failed, refusing to proceed.")
        sys.exit(1)

    print("    fast (angle-addition) vs direct (mp.sin) cross-validation:")
    cross_rows = []
    for N in ([5, 17, 30, 100] if not quick else [5, 17]):
        jf = J_N_trig_fast(N)
        jd = J_N_trig_direct(N)
        rel = abs(jf - jd) / jd
        print(f"      N={N:4d}: rel.diff(fast,direct) = {s(rel, 4)}")
        cross_rows.append(dict(N=N, rel_diff=s(rel, 6)))
    results["control_fast_vs_direct"] = cross_rows

    # -------------------------------------------------------------------
    # Step 2: N-grids
    # -------------------------------------------------------------------
    windows, CROSS_DPS_NS = build_grids(quick)
    all_Ns_main = sorted(set(n for g in windows.values() for n in g))
    total_steps = sum(all_Ns_main)
    print(f"\n[2] N-grids (quick={quick}):")
    for wname, g in windows.items():
        print(f"    {wname}: n={len(g)}, N in [{min(g):,},{max(g):,}]")
    print(f"    total main-pass N-steps (sum of N, ~ work units): {total_steps:,}")
    print(f"    NWORKERS = {NWORKERS}")
    results["grids"] = {k: v for k, v in windows.items()}
    results["cross_dps_Ns"] = CROSS_DPS_NS
    results["total_main_pass_steps"] = total_steps

    # -------------------------------------------------------------------
    # Step 3: compute R_N over all points, main dps, via a SHARED persistent pool.
    # Checkpointed after every window (resilience against a long-running background job).
    # -------------------------------------------------------------------
    print(f"\n[3] Computing R_N over {len(all_Ns_main)} points at dps={DPS_MAIN}, "
          f"{NWORKERS}-way parallel ...")
    R = {}
    if os.path.exists(CKPT_PATH):
        try:
            with open(CKPT_PATH, "rb") as f:
                ck = pickle.load(f)
            if ck.get("dps_main") == DPS_MAIN and ck.get("quick") == quick:
                R = {N: mp.mpf(v) for N, v in ck.get("R_main", {}).items()}
                print(f"    resumed {len(R)} points from checkpoint {CKPT_PATH}")
        except Exception as e:
            print(f"    (checkpoint unreadable, starting fresh: {e})")

    t0 = time.time()
    with Pool(processes=NWORKERS) as pool:
        for wname in ("CONTROL", "W1", "W2", "W3", "W4", "W5"):
            Ns = windows[wname]
            tw0 = time.time()
            R.update(parallel_R_N(pool, Ns, DPS_MAIN, gr_str, pe_str, have=R))
            dtw = time.time() - tw0
            print(f"    window {wname} (n={len(Ns)}, max N={max(Ns):,}): {dtw:.1f}s "
                  f"(cumulative {time.time()-t0:.1f}s)", flush=True)
            with open(CKPT_PATH, "wb") as f:
                pickle.dump({"dps_main": DPS_MAIN, "quick": quick,
                             "R_main": {N: mp.nstr(v, DPS_MAIN + 20) for N, v in R.items()}}, f)

        t_main_compute = time.time() - t0
        print(f"    main-dps generation done in {t_main_compute:.1f}s "
              f"({total_steps/max(t_main_compute,1e-9):.0f} steps/sec effective)")
        results["timing_main_compute_s"] = round(t_main_compute, 3)
        results["effective_steps_per_sec"] = round(total_steps / max(t_main_compute, 1e-9), 1)

        # sample table for JSON (small N only -- R_N is O(1) regardless of N, safe to store)
        table = []
        for N in windows["CONTROL"] + [windows["W1"][0], windows["W1"][-1],
                                        windows["W2"][0], windows["W2"][-1],
                                        windows["W3"][0], windows["W3"][-1],
                                        windows["W4"][-1], windows["W5"][-1]]:
            table.append({"N": N, "R_N": s(R[N], 40)})
        results["R_N_table_sample"] = table

        # -------------------------------------------------------------------
        # Step 4: control C_0 recovery (sanity gate before trusting anything else)
        # -------------------------------------------------------------------
        print(f"\n[4] CONTROL: C_0 recovery, K=3 fit on W3")
        c0_coeffs, c0_resid = poly_fit_1_over_N(windows["W3"], [R[N] for N in windows["W3"]], 3)
        C0_simple = c0_coeffs[0]
        diff_c0_simple = abs(C0_simple - C0_target)
        print(f"    C_0 (K=3 fit, W3) = {s(C0_simple, 30)}   target = {s(C0_target, 30)}")
        print(f"    |diff| = {s(diff_c0_simple, 6)}   fit residual = {s(c0_resid, 6)}")
        results["control_C0_simple_fit"] = {"C0": s(C0_simple, 40), "target": s(C0_target, 40),
                                             "diff": s(diff_c0_simple, 15)}
        c0_gate_pass = diff_c0_simple < mp.mpf('1e-10') if not quick else diff_c0_simple < mp.mpf('1e-4')
        print(f"    GATE (|diff|<1e-10): {c0_gate_pass}")
        results["control_C0_gate_pass"] = c0_gate_pass
        if not c0_gate_pass:
            print("    ABORT: C_0 control failed -- refusing to trust C_1+ from this run.")
            with open(os.path.join(OUTDIR, "V1_results.json"), "w") as f:
                json.dump(results, f, indent=1, default=str)
            sys.exit(1)

        t_checkpoint = time.time() - t_start
        print(f"\n[checkpoint] elapsed so far: {t_checkpoint:.1f}s")

        # -------------------------------------------------------------------
        # Step 5: main extraction -- multi-K least-squares fits per window + POOLED
        # -------------------------------------------------------------------
        print(f"\n[5] MAIN EXTRACTION: polynomial-in-1/N fits, per window, multiple K")
        fit_windows = {wn: windows[wn] for wn in ("W1", "W2", "W3", "W4", "W5")}
        POOLED = sorted(set(n for wn in ("W1", "W2", "W3", "W4", "W5") for n in windows[wn]))
        fit_windows["POOLED"] = POOLED
        K_CAP = 9
        K_CAP_POOLED = 16
        fits_raw = {}
        for wname, Ns in fit_windows.items():
            Rs = [R[N] for N in Ns]
            n = len(Ns)
            this_cap = K_CAP_POOLED if wname == "POOLED" else K_CAP
            kmax = min(this_cap, n - 1)
            wfits_raw = {}
            for K in range(3, kmax + 1):
                coeffs, resid = poly_fit_1_over_N(Ns, Rs, K)
                wfits_raw[K] = (coeffs, resid)
            fits_raw[wname] = wfits_raw
            c_display = "  ".join(f"C{i}={s(c,14)}" for i, c in enumerate(wfits_raw[kmax][0][:5]))
            print(f"    {wname} (n={n}, N in [{min(Ns):,},{max(Ns):,}]): K=3..{kmax}  "
                  f"@K={kmax}: {c_display}")
        results["fits_least_squares"] = {
            wn: {K: {"coeffs": [s(c, 45) for c in cf], "residual": s(rs, 8)}
                 for K, (cf, rs) in wf.items()}
            for wn, wf in fits_raw.items()
        }

        print(f"\n[5b] Cross-check: exact interpolation (zero residual) on top-K-point subsets")
        exact_fits = {}
        for wname, Ns in fit_windows.items():
            n = len(Ns)
            this_cap = K_CAP_POOLED if wname == "POOLED" else K_CAP
            kmax = min(this_cap, n)
            wexact = {}
            for K in (kmax,):
                sub_Ns = Ns[-K:]
                sub_Rs = [R[N] for N in sub_Ns]
                coeffs = poly_exact_solve(sub_Ns, sub_Rs)
                wexact[K] = {"Ns_used": sub_Ns, "coeffs": [s(c, 45) for c in coeffs]}
            exact_fits[wname] = wexact
            if kmax in fits_raw[wname]:
                d0 = abs(mp.mpf(wexact[kmax]["coeffs"][0]) - fits_raw[wname][kmax][0][0])
                print(f"    {wname}: exact-vs-LS at K={kmax}: |C0 diff| = {s(d0,4)}")
        results["fits_exact_interpolation"] = exact_fits

        # -------------------------------------------------------------------
        # Step 6: stability analysis -- C_0..C_4 (extended one order beyond the banked bench)
        # -------------------------------------------------------------------
        print(f"\n[6] STABILITY ANALYSIS: trusted digits of C_0..C_4")
        TARGET_KS = (0, 1, 2, 3, 4)
        stability = {}
        for target_k in TARGET_KS:
            stability[f"C{target_k}"] = {}
            for wname, wfits_raw in fits_raw.items():
                Ks = sorted(k for k in wfits_raw if k > target_k)
                if len(Ks) < 2:
                    continue
                diffs = []
                for i in range(1, len(Ks)):
                    K_prev, K_cur = Ks[i - 1], Ks[i]
                    d = abs(wfits_raw[K_cur][0][target_k] - wfits_raw[K_prev][0][target_k])
                    diffs.append((K_prev, K_cur, d))
                best_K = Ks[-1]
                best_val = wfits_raw[best_K][0][target_k]
                last_diff = diffs[-1][2] if diffs else mp.mpf(1)
                stable_digits = max(0, int(-mp.log10(last_diff))) if last_diff > 0 else DPS_MAIN
                stability[f"C{target_k}"][wname] = dict(
                    best_K=best_K, best_value=s(best_val, 45),
                    consecutive_K_diffs=[dict(K_prev=a, K_cur=b, diff=s(d, 6)) for a, b, d in diffs],
                    stable_digits_est=stable_digits)
            row = "  ".join(f"{wn}:{stability[f'C{target_k}'][wn]['stable_digits_est']}d"
                             for wn in fit_windows if wn in stability[f"C{target_k}"])
            print(f"    C{target_k}: {row}")
        results["stability_analysis"] = stability

        print(f"\n    Cross-window agreement (genuine independent evidence):")
        GENUINE_WINDOWS = [w for w in ("W1", "W2", "W3", "W4", "W5") if w in fit_windows]
        cross_window = {}
        for target_k in TARGET_KS:
            vals = {wn: mp.mpf(stability[f"C{target_k}"][wn]["best_value"])
                    for wn in fit_windows if wn in stability[f"C{target_k}"]}
            pairs = []
            wnames = list(vals.keys())
            for i in range(len(wnames)):
                for j in range(i + 1, len(wnames)):
                    a, b = wnames[i], wnames[j]
                    d = abs(vals[a] - vals[b])
                    digits = max(0, int(-mp.log10(d))) if d > 0 else DPS_MAIN
                    pairs.append(dict(pair=f"{a}_vs_{b}", diff=s(d, 8), agree_digits=digits))
            cross_window[f"C{target_k}"] = pairs
            genuine_pairs = [p for p in pairs if p["pair"].split("_vs_")[0] in GENUINE_WINDOWS
                              and p["pair"].split("_vs_")[1] in GENUINE_WINDOWS]
            if genuine_pairs:
                worst = min(genuine_pairs, key=lambda p: p["agree_digits"])
                print(f"    C{target_k}: worst genuine-window pair = {worst['pair']} "
                      f"({worst['agree_digits']} digits); all pairs: "
                      + ", ".join(f"{p['pair']}={p['agree_digits']}d" for p in genuine_pairs))
        results["cross_window_agreement"] = cross_window

        GENUINE_WINDOWS_SET = set(GENUINE_WINDOWS)
        final_estimates = {}
        print(f"\n    FINAL estimates (source: best-converged window; trust = independent "
              f"W1..W5 agreement only):")
        for target_k in TARGET_KS:
            candidates = [(wname, stability[f"C{target_k}"][wname]["stable_digits_est"])
                          for wname in fit_windows if wname in stability[f"C{target_k}"]]
            if not candidates:
                continue
            source_window = max(candidates, key=lambda t: t[1])[0]
            source_K = stability[f"C{target_k}"][source_window]["best_K"]
            val = fits_raw[source_window][source_K][0][target_k]
            conv_digits = stability[f"C{target_k}"][source_window]["stable_digits_est"]
            cw_digits_list = [p["agree_digits"] for p in cross_window[f"C{target_k}"]
                               if p["pair"].split("_vs_")[0] in GENUINE_WINDOWS_SET
                               and p["pair"].split("_vs_")[1] in GENUINE_WINDOWS_SET]
            cw_digits = min(cw_digits_list) if cw_digits_list else 0
            trusted_digits = min(conv_digits, cw_digits)
            final_estimates[f"C{target_k}"] = dict(value=s(val, 50), source_window=source_window,
                                                    source_K=source_K, trusted_digits=trusted_digits)
            print(f"    FINAL C{target_k} = {s(val,30)}  (source={source_window} K={source_K}, "
                  f"~{trusted_digits} trusted digits)")
        results["final_estimates"] = final_estimates

        # per-window-only (self) digit estimate for C_3, used later to extrapolate a
        # precision floor if 17-18 digits are not reached this run
        precision_scaling = []
        for wname in ("W3", "W4", "W5"):
            if wname in stability["C3"]:
                precision_scaling.append(dict(window=wname, max_N=max(windows[wname]),
                                               self_digits=stability["C3"][wname]["stable_digits_est"]))
        results["precision_scaling_C3"] = precision_scaling
        print(f"    C_3 self-convergence vs window max-N (for floor extrapolation): "
              f"{precision_scaling}")

        # -------------------------------------------------------------------
        # Step 7: precision cross-check (dps DPS_MAIN -> DPS_CROSS) on the W4 subset
        # -------------------------------------------------------------------
        print(f"\n[7] PRECISION CROSS-CHECK: W4 subset recomputed at dps={DPS_CROSS} "
              f"(vs main dps={DPS_MAIN})")
        t0c = time.time()
        R_cross = parallel_R_N(pool, CROSS_DPS_NS, DPS_CROSS, gr_str, pe_str)
        t_cross_compute = time.time() - t0c
        print(f"    done in {t_cross_compute:.1f}s")
        results["timing_cross_dps_compute_s"] = round(t_cross_compute, 3)

        rn_compare = []
        for N in CROSS_DPS_NS:
            d = abs(R[N] - R_cross[N])
            rn_compare.append(dict(N=N, diff=s(d, 10)))
        results["cross_dps_R_N_compare"] = rn_compare
        print("    R_N agreement at shared N (sample): "
              + ", ".join(f"N={r['N']}:{r['diff']}" for r in rn_compare[:3]))

        Ks_cross = list(range(3, min(K_CAP, len(CROSS_DPS_NS)) + 1))
        cross_fits = {}
        for K in Ks_cross:
            coeffs, resid = poly_fit_1_over_N(CROSS_DPS_NS, [R_cross[N] for N in CROSS_DPS_NS], K)
            cross_fits[K] = (coeffs, resid)
        dps_check = {}
        if Ks_cross:
            best_K_cross = Ks_cross[-1]
            print(f"    dps={DPS_CROSS} fit (K={best_K_cross}) vs dps={DPS_MAIN} final estimates:")
            for target_k in TARGET_KS:
                if target_k < best_K_cross and f"C{target_k}" in final_estimates:
                    val_cross = cross_fits[best_K_cross][0][target_k]
                    val_main = mp.mpf(final_estimates[f"C{target_k}"]["value"])
                    d = abs(val_cross - val_main)
                    digits = max(0, int(-mp.log10(d))) if d > 0 else DPS_MAIN
                    print(f"      C{target_k}: diff={s(d,6)} (~{digits} digits agree)")
                    dps_check[f"C{target_k}"] = dict(dps_main=s(val_main, 40),
                                                      dps_cross=s(val_cross, 40),
                                                      diff=s(d, 10), agree_digits=digits)
        results["cross_dps_fit_compare"] = dps_check

    # pool closed here (all parallel work done)

    # -------------------------------------------------------------------
    # Step 8: PSLQ recognition sweep -- C_1, C_2 (re-verification/continuity control
    # against the banked closed forms) and C_3, C_4 (the new targets)
    # -------------------------------------------------------------------
    print(f"\n[8] PSLQ RECOGNITION SWEEP")
    bases = build_candidate_bases()
    print(f"    candidate bases: {list(bases.keys())}")
    SUFFICIENT_DIGITS_GATE = 17  # this task's own stated threshold (banked bench used 15)
    pslq_results = {}
    for target_k in (1, 2, 3, 4):
        if f"C{target_k}" not in final_estimates:
            continue
        Ck = mp.mpf(final_estimates[f"C{target_k}"]["value"])
        trusted_digits = final_estimates[f"C{target_k}"]["trusted_digits"]
        if f"C{target_k}" in dps_check:
            trusted_digits = min(trusted_digits, dps_check[f"C{target_k}"]["agree_digits"])
        pslq_dps = max(20, trusted_digits - 5)
        sufficient_precision = trusted_digits >= SUFFICIENT_DIGITS_GATE
        print(f"\n    C_{target_k} = {s(Ck,30)}  (trusted_digits={trusted_digits}, "
              f"gate={SUFFICIENT_DIGITS_GATE}, sufficient={sufficient_precision})")
        k_results = {"C_k_value": s(Ck, 50), "trusted_digits": trusted_digits,
                     "pslq_dps": pslq_dps, "sufficient_precision": sufficient_precision,
                     "attempts": {}}
        for base_name, B in bases.items():
            with mp.workdps(DPS_VOL):
                Bk = B ** target_k
                T = Ck / (C0_target * Bk)
            attempts = recognize_sweep(T, pslq_dps)
            hit_attempts = [a for a in attempts if a["found"]]
            expected = expected_basis_kind(target_k, base_name)
            k_results["attempts"][base_name] = dict(T=s(T, min(40, pslq_dps + 5)),
                                                      all_attempts=attempts,
                                                      any_hit=len(hit_attempts) > 0,
                                                      expected_basis_kind=expected)
            if hit_attempts:
                best_hit = min(hit_attempts, key=lambda a: a["maxcoeff"])
                if expected is None:
                    tag = "*** UNEXPECTED HIT ON WRONG-PI-POWER CONTROL ***"
                elif best_hit["basis"] == expected:
                    tag = "PREDICTED"
                else:
                    tag = "*** PARITY-VIOLATING HIT ***"
                print(f"      base={base_name:12s}: HIT  {best_hit['basis']} "
                      f"maxcoeff={best_hit['maxcoeff']}  relation={best_hit['relation']}  [{tag}]")
            else:
                print(f"      base={base_name:12s}: no relation (up to maxcoeff="
                      f"{max(a['maxcoeff'] for a in attempts)})")
        pslq_results[f"C{target_k}"] = k_results
    results["pslq_sufficient_digits_gate"] = SUFFICIENT_DIGITS_GATE
    results["pslq_sweep"] = pslq_results

    # -------------------------------------------------------------------
    # Step 8b: cross-window validation of any hits
    # -------------------------------------------------------------------
    print(f"\n[8b] CROSS-WINDOW VALIDATION of any PSLQ hits")
    validated_hits = []
    for target_k in (1, 2, 3, 4):
        if f"C{target_k}" not in pslq_results:
            continue
        kres = pslq_results[f"C{target_k}"]
        for base_name, att in kres["attempts"].items():
            if not att["any_hit"]:
                continue
            hit_attempts = [a for a in att["all_attempts"] if a["found"]]
            best_hit = min(hit_attempts, key=lambda a: a["maxcoeff"])
            relation = best_hit["relation"]
            basis_kind = best_hit["basis"]
            with mp.workdps(DPS_VOL):
                B = bases[base_name]
                Bk = B ** target_k
                if basis_kind == "Q":
                    c0r, c1r = relation
                    closed_val = mp.mpf(-c1r) / c0r
                else:
                    c0r, c1r, c2r = relation
                    closed_val = (-mp.mpf(c1r) - mp.mpf(c2r) * mp.sqrt(3)) / c0r
                predicted_Ck = closed_val * C0_target * Bk
            cross_checks = []
            for wname in fit_windows:
                if wname not in stability[f"C{target_k}"]:
                    continue
                w_val = mp.mpf(stability[f"C{target_k}"][wname]["best_value"])
                w_trusted = stability[f"C{target_k}"][wname]["stable_digits_est"]
                d = abs(w_val - predicted_Ck)
                digits = max(0, int(-mp.log10(d))) if d > 0 else DPS_MAIN
                cross_checks.append(dict(window=wname, diff=s(d, 8), agree_digits=digits,
                                          window_own_trusted_digits=w_trusted))
            expected = expected_basis_kind(target_k, base_name)
            record = dict(C_k=f"C{target_k}", base=base_name, basis_kind=basis_kind,
                           relation=relation, maxcoeff=best_hit["maxcoeff"],
                           expected_basis_kind=expected,
                           matches_prediction=(expected is not None and basis_kind == expected),
                           is_wrong_pi_power_control=(expected is None),
                           predicted_value=s(predicted_Ck, 40), cross_checks=cross_checks)
            validated_hits.append(record)
            print(f"    C_{target_k}/base={base_name} relation={relation} "
                  f"(matches_prediction={record['matches_prediction']}): "
                  f"predicted={s(predicted_Ck,20)}")
    results["validated_hits"] = validated_hits

    # -------------------------------------------------------------------
    # Step 9: verdict
    # -------------------------------------------------------------------
    print(f"\n[9] VERDICT")
    ROBUST_MAXCOEFF = 3000000
    ROBUST_MIN_DIGITS = 10
    robust_hits = []
    for h in validated_hits:
        if h["maxcoeff"] > ROBUST_MAXCOEFF or not h["matches_prediction"]:
            continue
        other_ok = sum(1 for c in h["cross_checks"]
                        if c["window"] in GENUINE_WINDOWS_SET
                        and c["agree_digits"] >= min(ROBUST_MIN_DIGITS, c["window_own_trusted_digits"]))
        if other_ok >= 2:
            robust_hits.append(h)

    # genuine anomalies only: matches_prediction is now computed PER (k,base) pair (see the
    # expected_basis_kind fix above), so a base like pi/sqrt3 hitting "Q" at odd k is correctly
    # counted as matching (it is the same relation, algebraically restated) and does NOT land
    # here. What lands here are real surprises: a hit on the wrong Q/Q(sqrt3) basis for a
    # genuine pi-power base, or any hit at all on the wrong-pi-power controls ("1","pi^2").
    wrong_parity_hits = [h for h in validated_hits
                          if not h["matches_prediction"] and not h["is_wrong_pi_power_control"]]
    wrong_pi_power_hits = [h for h in validated_hits if h["is_wrong_pi_power_control"]]

    precision_by_k = {k: pslq_results[k]["sufficient_precision"] for k in pslq_results}
    sufficient_ks = [k for k, ok in precision_by_k.items() if ok]
    robust_ks = sorted(set(h["C_k"] for h in robust_hits) & set(sufficient_ks))
    clean_miss_ks = [k for k in sufficient_ks
                      if not any(att["any_hit"] for att in pslq_results[k]["attempts"].values())]

    print(f"    coefficients with >= {SUFFICIENT_DIGITS_GATE} trusted digits: {sufficient_ks}")
    print(f"    robust predicted-parity hits: {robust_ks}")
    print(f"    clean misses (sufficient precision, nothing found anywhere): {clean_miss_ks}")
    print(f"    GENUINE parity-violating hits (would contradict the prediction): "
          f"{[(h['C_k'], h['base']) for h in wrong_parity_hits]}")
    print(f"    hits on wrong-pi-power controls (should be empty): "
          f"{[(h['C_k'], h['base']) for h in wrong_pi_power_hits]}")

    c3_status = None
    if "C3" in robust_ks:
        c3_status = "CONFIRMED"
    elif "C3" in clean_miss_ks:
        c3_status = "CLEAN_NEGATIVE"
    else:
        c3_status = "PRECISION_FLOOR"

    c4_status = None
    if "C4" in robust_ks:
        c4_status = "CONFIRMED"
    elif "C4" in clean_miss_ks:
        c4_status = "CLEAN_NEGATIVE"
    else:
        c4_status = "PRECISION_FLOOR"

    # precision-floor extrapolation for C_3 (only meaningful if not already decided)
    floor_estimate = None
    ps = results.get("precision_scaling_C3", [])
    if len(ps) >= 2:
        import math
        pts = [(math.log10(p["max_N"]), p["self_digits"]) for p in ps if p["self_digits"] > 0]
        if len(pts) >= 2:
            x0, y0 = pts[0]
            x1, y1 = pts[-1]
            if x1 != x0:
                slope = (y1 - y0) / (x1 - x0)
                intercept = y0 - slope * x0
                if slope > 0:
                    need_x = (18 - intercept) / slope
                    floor_estimate = dict(model="digits ~ slope*log10(N_max) + intercept",
                                           slope=slope, intercept=intercept,
                                           points_used=pts,
                                           N_max_for_18_digits=10 ** need_x)
    results["precision_floor_extrapolation_C3"] = floor_estimate
    if floor_estimate:
        print(f"    C_3 precision-floor extrapolation: need N_max ~ "
              f"{floor_estimate['N_max_for_18_digits']:.3e} for ~18 digits "
              f"(linear fit in log10(N_max), slope={floor_estimate['slope']:.3f})")

    if c3_status == "CONFIRMED":
        verdict = "EULER-STRUCTURE-EXTENDED"
        c3_hit = [h for h in robust_hits if h["C_k"] == "C3"][0]
        verdict_reason = (f"C_3 recognized on the PREDICTED basis (Q(sqrt3), base={c3_hit['base']}, "
                           f"maxcoeff={c3_hit['maxcoeff']}), cross-window validated" +
                           (f"; C_4 ALSO confirmed" if c4_status == "CONFIRMED" else
                            f"; C_4 {c4_status.lower().replace('_',' ')}"))
    elif c3_status == "CLEAN_NEGATIVE":
        verdict = "ARITHMETIC-STOPS-AT-3"
        verdict_reason = (f"C_3 reached >={SUFFICIENT_DIGITS_GATE} trusted digits with a thorough "
                           f"PSLQ sweep (11 bases x {{Q,Q(sqrt3)}} x up to maxcoeff={ROBUST_MAXCOEFF}) "
                           f"and found NOTHING on the predicted OR any wrong basis")
    else:
        verdict = "PRECISION-FLOOR"
        c3_digits = final_estimates.get("C3", {}).get("trusted_digits", 0)
        verdict_reason = (f"C_3 reached only {c3_digits} trusted digits (<{SUFFICIENT_DIGITS_GATE} "
                           f"needed); see precision_floor_extrapolation_C3 for the N/dps that would "
                           f"decide it")

    print(f"\n    VERDICT: {verdict}")
    print(f"    reason: {verdict_reason}")
    results["c3_status"] = c3_status
    results["c4_status"] = c4_status
    results["verdict"] = verdict
    results["verdict_reason"] = verdict_reason
    results["robust_hits"] = robust_hits
    results["wrong_parity_hits"] = wrong_parity_hits
    results["wrong_pi_power_hits"] = wrong_pi_power_hits
    results["precision_sufficient_by_k"] = precision_by_k
    results["clean_miss_ks"] = clean_miss_ks

    t_total = time.time() - t_start
    results["timing_total_s"] = round(t_total, 3)
    print(f"\nTotal runtime: {t_total:.2f}s ({t_total/60:.1f} min)")

    outname = os.path.join(OUTDIR, "V1_results_quick.json" if quick else "V1_results.json")
    with open(outname, "w") as f:
        json.dump(results, f, indent=1, default=str)
    print(f"Wrote {outname}")
    if os.path.exists(CKPT_PATH):
        os.remove(CKPT_PATH)

    return results


if __name__ == "__main__":
    quick_flag = "--quick" in sys.argv
    main(quick=quick_flag)
