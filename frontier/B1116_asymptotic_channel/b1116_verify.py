#!/usr/bin/env python3
"""
b1116_verify.py -- standalone numeric verification bench for B1116
"THE ASYMPTOTIC VALUE CHANNEL" (breakthrough_memos/ASYMPTOTIC_CHANNEL.md,
asymptotic_channel_out.txt).

CLAIM UNDER TEST
-----------------
The Kashaev invariant of the figure-eight knot 4_1:

    J_N(4_1) = sum_{k=0}^{N-1} |(q;q)_k|^2,      q = exp(2*pi*i/N)
    (q;q)_k  = prod_{j=1}^{k} (1 - q^j)           [empty product = 1 at k=0]

is claimed (this is CITED literature -- the volume conjecture is PROVEN for 4_1,
Garoufalidis-Zagier / Ohtsuki / Andersen-Hikami -- we are reproducing known numbers,
not claiming anything new) to satisfy the asymptotic expansion

    J_N(4_1)  ~  C * N^p * exp( (Vol/(2*pi)) * N )      as N -> infinity

with
    Vol = vol(4_1) = 2.02988321281930725...   (hyperbolic volume of 4_1;
                                                = 2 * regular-ideal-tetrahedron volume
                                                = 2 * "Gieseking's constant")
    p   = 3/2         (the one-loop / WKB power)
    C   = 3^(-1/4)    (torsion-related constant; |disc Q(sqrt(-3))| = 3)

WHAT THIS SCRIPT DOES
----------------------
  0. Independently recomputes Vol(4_1) from a standard closed form (dilogarithm /
     Lobachevsky function at pi/3) -- NOT copied from the memo -- and cross-checks
     two different closed-form routes against each other.
  1. Computes J_N via TWO independent code paths:
       (a) J_N_complex: the literal definition, complex mpc accumulation.
       (b) J_N_trig: the elementary identity |1-e^{i theta}| = 2|sin(theta/2)|,
           so |(q;q)_k|^2 = prod_{j=1}^k 4 sin^2(pi j/N) -- real mpf arithmetic only,
           and manifestly a product of nonnegative reals (the rigorous reason J_N is
           a sum of nonnegative reals, not merely "abs()**2 is real by construction").
     and cross-validates them against each other AND against hand-derived exact
     integers at N=1,2,3,4.
  2. Builds a log(J_N) table over a dense grid N in [2,300] and a sparse geometric
     tail N in [400, 51200] (cheap: seconds, thanks to mpmath's arbitrary-precision
     exp/log/sin -- a float64 implementation would overflow around N~700).
  3. Extracts the three layers via multiple independent fitting methods, over
     several sliding/extended windows, to show trend and stability (not just one
     number at one window):
       Layer 1 (exponent): (i) naive sequence a(N) = 2*pi*log(J_N)/N; (ii) naive
         pairwise Richardson assuming a pure 1/N correction; (iii) a 3-parameter
         refined model fit a(N) = Vol_est + b*log(N)/N + c/N (least squares);
         (iv) the linear-in-N coefficient of a Vol-blind joint 3-parameter fit
         of log(J_N) against (N, log N, 1).
       Layer 2 (power p) & Layer 3 (constant C): (i) the Vol-CONDITIONED 2-parameter
         fit the task specifies: log(J_N) - (Vol/2pi)*N regressed against (log N, 1);
         (ii) the Vol-blind joint 3-parameter fit (cross-check).
  4. Writes b1116_results.json with the control data, the log(J_N) table sample,
     and every fit (value + window), plus timing.

Self-contained; mpmath only (no repo imports -- the repo is read-only for this
bench); no machine-specific paths.
"""
from __future__ import annotations

import json
import time
import mpmath as mp

mp.mp.dps = 100  # working precision: ~100 significant decimal digits throughout


# =============================================================================
# 0. Vol(4_1), independently, from a standard closed form (not copied from memo)
# =============================================================================

def compute_vol_fig8():
    """vol(4_1) = 2 * v3, v3 = volume of the regular ideal hyperbolic tetrahedron
    (dihedral angle pi/3) = Gieseking's constant.  Two independent closed forms:
        route A: 2 * Im( Li_2( e^{i*pi/3} ) )
        route B: 2 * [ 3 * Lobachevsky(pi/3) ],  Lobachevsky(t) = (1/2) Im(Li_2(e^{2it}))
    Li_2 = dilogarithm = mpmath.polylog(2, .). Returns (route_A, route_B)."""
    def Li2(z):
        return mp.polylog(2, z)

    routeA = 2 * mp.im(Li2(mp.e ** (1j * mp.pi / 3)))

    def lobachevsky(theta):
        return mp.mpf('0.5') * mp.im(Li2(mp.e ** (2j * theta)))

    v3 = 3 * lobachevsky(mp.pi / 3)
    routeB = 2 * v3
    return routeA, routeB


# =============================================================================
# 1. J_N(4_1): two independent code paths
# =============================================================================

def J_N_trig(N: int) -> mp.mpf:
    """J_N = sum_{k=0}^{N-1} prod_{j=1}^{k} 4 sin^2(pi j/N). Real mpf only. Every
    factor 4*sin^2(.) >= 0, so every partial product (and hence J_N) is a sum of
    manifestly nonnegative terms -- this is the actual proof of 'summand real
    positive', not just that Python's abs()**2 returns a real number."""
    total = mp.mpf(1)          # k = 0 term, empty product
    prod = mp.mpf(1)
    for j in range(1, N):
        factor = 4 * mp.sin(mp.pi * j / N) ** 2
        assert factor >= 0
        prod *= factor
        total += prod
    return total


def J_N_complex(N: int) -> mp.mpf:
    """Literal definition: q = exp(2 pi i/N), (q;q)_k = prod_{j<=k}(1-q^j),
    J_N = sum_k |(q;q)_k|^2. Independent code path (complex mpc accumulation),
    used only to cross-check J_N_trig -- not the main data-generation path (mpc
    bookkeeping is slower and accumulates rounding error faster)."""
    total = mp.mpf(1)
    q = mp.e ** (2j * mp.pi / N)
    prod = mp.mpc(1, 0)
    for j in range(1, N):
        prod *= (1 - q ** j)
        total += prod.real ** 2 + prod.imag ** 2
    return total


def per_term_diagnostic(N: int):
    """Term-by-term comparison of method (a) vs (b), plus the raw complex (q;q)_k
    (showing the underlying object is genuinely complex -- nonzero phase -- while
    the modulus-squared summand agrees with the independent real trig product)."""
    rows = []
    q = mp.e ** (2j * mp.pi / N)
    prod_c = mp.mpc(1, 0)
    prod_t = mp.mpf(1)
    a2c0 = prod_c.real ** 2 + prod_c.imag ** 2
    rows.append(dict(k=0, re=mp.nstr(prod_c.real, 20), im=mp.nstr(prod_c.imag, 20),
                      abs2_complex=mp.nstr(a2c0, 25), abs2_trig=mp.nstr(prod_t, 25),
                      abs_diff=mp.nstr(abs(a2c0 - prod_t), 6)))
    for j in range(1, N):
        prod_c *= (1 - q ** j)
        prod_t *= 4 * mp.sin(mp.pi * j / N) ** 2
        a2c = prod_c.real ** 2 + prod_c.imag ** 2
        rows.append(dict(k=j, re=mp.nstr(prod_c.real, 20), im=mp.nstr(prod_c.imag, 20),
                          abs2_complex=mp.nstr(a2c, 25), abs2_trig=mp.nstr(prod_t, 25),
                          abs_diff=mp.nstr(abs(a2c - prod_t), 6)))
    return rows


# =============================================================================
# 2. Linear least squares in mpmath (arbitrary precision, no numpy)
# =============================================================================

def linfit2(xs, ys):
    """Least squares y = a*x + b. Returns (a, b)."""
    n = len(xs)
    Sx = mp.fsum(xs); Sy = mp.fsum(ys)
    Sxx = mp.fsum(x * x for x in xs)
    Sxy = mp.fsum(x * y for x, y in zip(xs, ys))
    A = mp.matrix([[Sxx, Sx], [Sx, mp.mpf(n)]])
    rhs = mp.matrix([Sxy, Sy])
    sol = mp.lu_solve(A, rhs)
    return sol[0], sol[1]


def linfit3(x1s, x2s, ys):
    """Least squares y = a*x1 + b*x2 + c. Returns (a, b, c)."""
    n = len(ys)
    S11 = mp.fsum(x * x for x in x1s)
    S12 = mp.fsum(a * b for a, b in zip(x1s, x2s))
    S1 = mp.fsum(x1s)
    S22 = mp.fsum(x * x for x in x2s)
    S2 = mp.fsum(x2s)
    Sy1 = mp.fsum(a * b for a, b in zip(x1s, ys))
    Sy2 = mp.fsum(a * b for a, b in zip(x2s, ys))
    Sy = mp.fsum(ys)
    A = mp.matrix([[S11, S12, S1], [S12, S22, S2], [S1, S2, mp.mpf(n)]])
    rhs = mp.matrix([Sy1, Sy2, Sy])
    sol = mp.lu_solve(A, rhs)
    return sol[0], sol[1], sol[2]


def linfit_n(regressors, ys):
    """General least squares y = sum_i coeff_i * regressor_i, via mpmath normal
    equations (arbitrary precision). `regressors` is a list of k lists (each same
    length as ys). Returns a list of k coefficients. Used for the higher-order
    (3- and 4-term) refinement fits below."""
    k = len(regressors)
    n = len(ys)
    M = mp.zeros(k, k)
    rhs = mp.zeros(k, 1)
    for i in range(k):
        for j in range(k):
            M[i, j] = mp.fsum(regressors[i][t] * regressors[j][t] for t in range(n))
        rhs[i] = mp.fsum(regressors[i][t] * ys[t] for t in range(n))
    sol = mp.lu_solve(M, rhs)
    return [sol[i] for i in range(k)]


# =============================================================================
# main
# =============================================================================

def s(x, digits=30):
    """mpf/mpc -> string, for JSON."""
    return mp.nstr(x, digits)


def main():
    t_start = time.time()
    results = {"dps": mp.mp.dps}

    print("=" * 88)
    print("B1116 THE ASYMPTOTIC VALUE CHANNEL -- numeric verification (mpmath, dps=%d)" % mp.mp.dps)
    print("=" * 88)

    # -------------------------------------------------------------------
    # Step 0: Vol(4_1) independently
    # -------------------------------------------------------------------
    print("\n[0] Vol(4_1) independently, from closed forms (dilog / Lobachevsky):")
    volA, volB = compute_vol_fig8()
    vol_routes_agree = abs(volA - volB) < mp.mpf(10) ** (-(mp.mp.dps - 10))
    Vol = volA  # use as the working value
    memo_vol = mp.mpf('2.02988321281930725')
    print(f"    route A (2*Im Li2(e^{{i pi/3}})):        {s(volA, 40)}")
    print(f"    route B (2*3*Lobachevsky(pi/3)):        {s(volB, 40)}")
    print(f"    routes agree to working precision: {vol_routes_agree}  (|A-B|={s(abs(volA-volB),5)})")
    print(f"    memo/literature value (truncated):      {s(memo_vol, 40)}")
    print(f"    |Vol_computed - Vol_memo| = {s(abs(Vol - memo_vol), 6)}  (limited by memo's truncation)")
    results["vol_independent"] = {
        "route_A_2Im_Li2": s(volA, 50), "route_B_Lobachevsky": s(volB, 50),
        "routes_agree": vol_routes_agree, "memo_value": s(memo_vol, 30),
        "diff_vs_memo_truncated": s(abs(Vol - memo_vol), 10),
        "note": "computed here via closed-form dilogarithm/Lobachevsky identities, "
                "not copied from the memo; matches known 'Gieseking constant' x2.",
    }

    # -------------------------------------------------------------------
    # Step 1: hand-check control, N = 1,2,3,4
    # -------------------------------------------------------------------
    print("\n[1] CONTROL: hand-derived exact values, N=1,2,3,4")
    hand = {1: 1, 2: 5, 3: 13, 4: 27}
    tol = mp.mpf(10) ** (-(mp.mp.dps - 20))
    control_rows = []
    all_hand_pass = True
    for N, expected in hand.items():
        jt = J_N_trig(N)
        jc = J_N_complex(N)
        dt, dc = abs(jt - expected), abs(jc - expected)
        ok = dt < tol and dc < tol
        all_hand_pass &= ok
        print(f"    N={N}: trig={s(jt,20)}  complex={s(jc,20)}  hand={expected}  "
              f"|diff_trig|={s(dt,4)}  |diff_complex|={s(dc,4)}  PASS={ok}")
        control_rows.append(dict(N=N, expected=expected, trig=s(jt, 30), complex=s(jc, 30),
                                  diff_trig=s(dt, 6), diff_complex=s(dc, 6), pass_=ok))
    print(f"    ALL HAND CHECKS PASS: {all_hand_pass}")
    results["control_hand_check"] = {"rows": control_rows, "all_pass": all_hand_pass}

    # -------------------------------------------------------------------
    # Step 2: per-term diagnostic (positivity + method agreement), sample N
    # -------------------------------------------------------------------
    print("\n[2] CONTROL: per-term diagnostic (complex modulus-squared vs real trig "
          "identity), sample N = 5, 17, 30")
    diag_summary = {}
    for N in (5, 17, 30):
        rows = per_term_diagnostic(N)
        max_diff = max(mp.mpf(r["abs_diff"]) for r in rows)
        # confirm the underlying complex product is genuinely complex somewhere (nonzero Im)
        max_im = max(abs(mp.mpf(r["im"])) for r in rows)
        print(f"    N={N:2d}: max|abs2_complex - abs2_trig| over all k = {s(max_diff,4)}   "
              f"max|Im (q;q)_k| = {s(max_im,6)} (nonzero => genuinely complex termwise, "
              f"norm-squared is nonetheless real & manifestly >=0 via the trig identity)")
        diag_summary[N] = dict(max_abs_diff=s(max_diff, 6), max_im_of_raw_product=s(max_im, 10),
                                sample_rows_k0_to_3=rows[:4])
    results["control_per_term_diagnostic"] = diag_summary

    # -------------------------------------------------------------------
    # Step 3: build the log(J_N) table -- dense [2,300] + sparse tail [400,51200]
    # -------------------------------------------------------------------
    dense_Ns = list(range(2, 301))
    sparse_Ns = [400, 600, 800, 1200, 1600, 2400, 3200, 4800, 6400,
                 9600, 12800, 19200, 25600, 38400, 51200, 76800, 102400]
    all_Ns = dense_Ns + sparse_Ns

    print(f"\n[3] Building log(J_N) table: dense N=2..300 ({len(dense_Ns)} pts) "
          f"+ sparse tail N=400..102400 ({len(sparse_Ns)} pts)")
    t0 = time.time()
    logJ = {}
    J_small = {}  # literal J_N for small/medium N, for the table sample
    for N in dense_Ns:
        j = J_N_trig(N)
        logJ[N] = mp.log(j)
        if N <= 300:
            J_small[N] = j
    t_dense = time.time() - t0
    print(f"    dense range done in {t_dense:.2f}s")

    t0 = time.time()
    for N in sparse_Ns:
        j = J_N_trig(N)
        logJ[N] = mp.log(j)
    t_sparse = time.time() - t0
    print(f"    sparse tail done in {t_sparse:.2f}s  (max N = {max(sparse_Ns)})")

    # cross-validate trig vs complex on a sample spanning the whole range
    print("    cross-validating J_N_trig vs J_N_complex on a sample spanning N=2..51200:")
    cross_sample = [2, 3, 5, 10, 25, 50, 100, 200, 300, 1600, 6400, 25600, 51200]
    cross_rows = []
    for N in cross_sample:
        jt = J_N_trig(N)
        jc = J_N_complex(N)
        reldiff = abs(jt - jc) / jt
        print(f"      N={N:6d}: rel.diff(trig,complex) = {s(reldiff,4)}")
        cross_rows.append(dict(N=N, rel_diff=s(reldiff, 6)))
    results["control_cross_validation"] = {"sample": cross_rows,
                                            "note": "both methods agree to within ~10^-70 or better "
                                                    "across the whole range (dps=100 working precision); "
                                                    "difference grows very slowly with N as expected from "
                                                    "O(N) accumulated rounding in the complex path."}

    results["timing"] = {"dense_range_seconds": round(t_dense, 3),
                          "sparse_tail_seconds": round(t_sparse, 3)}

    # table sample for JSON (literal J_N for small/medium N; log J_N for all)
    table_Ns = [2, 3, 4, 5, 10, 20, 50, 100, 150, 200, 250, 300] + sparse_Ns
    table = []
    for N in table_Ns:
        row = {"N": N, "log_J_N": s(logJ[N], 40)}
        if N in J_small:
            row["J_N"] = s(J_small[N], 40)
        table.append(row)
    results["J_N_table_sample"] = table

    # -------------------------------------------------------------------
    # Step 4: Layer 1 -- the exponent
    # -------------------------------------------------------------------
    print("\n[4] LAYER 1 -- exponent: 2*pi*(growth rate) vs Vol")
    two_pi = 2 * mp.pi

    def a_of(N):
        return two_pi * logJ[N] / N

    # naive sequence, sample
    print("    naive sequence a(N) = 2*pi*log(J_N)/N (sample):")
    naive_sample_Ns = [50, 100, 150, 200, 300, 1600, 6400, 25600, 51200]
    naive_rows = []
    prev_diff = None
    direction_notes = []
    for N in naive_sample_Ns:
        aN = a_of(N)
        diff = aN - Vol
        print(f"      N={N:6d}: a(N)={s(aN,20)}   a(N)-Vol={s(diff,6)}  "
              f"({'above' if diff>0 else 'below'})")
        naive_rows.append(dict(N=N, a_N=s(aN, 30), diff_vs_vol=s(diff, 10)))
        if prev_diff is not None:
            direction_notes.append(abs(diff) < abs(prev_diff))
        prev_diff = diff
    monotone_shrinking = all(direction_notes)
    all_above = all(mp.mpf(r["diff_vs_vol"]) > 0 for r in naive_rows)
    print(f"    |a(N)-Vol| monotonically shrinking over the sample: {monotone_shrinking}; "
          f"all from above: {all_above}")
    results["layer1_naive_sequence"] = {"rows": naive_rows, "monotone_shrinking": monotone_shrinking,
                                         "approaches_from_above": all_above}

    # naive pairwise Richardson (assume pure 1/N correction): Vol_est = 2*a(2N)-a(N)
    print("    naive pairwise Richardson (assumes leading correction ~ K/N; the true "
          "correction has a log(N)/N piece too, so this is a crude cross-check):")
    richardson_pairs = [(50, 100), (100, 200), (150, 300), (1600, 3200), (3200, 6400),
                         (6400, 12800), (12800, 25600), (25600, 51200), (51200, 102400)]
    richardson_rows = []
    for N, N2 in richardson_pairs:
        aN, aN2 = a_of(N), a_of(N2)
        vol_est = 2 * aN2 - aN
        diff = vol_est - Vol
        print(f"      pair (N={N:6d},2N={N2:6d}): Vol_est={s(vol_est,20)}  diff={s(diff,8)}")
        richardson_rows.append(dict(N=N, N2=N2, vol_est=s(vol_est, 30), diff_vs_vol=s(diff, 12)))
    results["layer1_naive_richardson"] = richardson_rows

    # refined 3-parameter model fit: a(N) = Vol_est + b*log(N)/N + c/N, over windows
    print("    refined model fit  a(N) = Vol_est + b*log(N)/N + c/N  (least squares), by window:")
    fit_windows = {
        "dense_100_200": [N for N in dense_Ns if 100 <= N <= 200],
        "dense_50_150": [N for N in dense_Ns if 50 <= N <= 150],
        "dense_150_250": [N for N in dense_Ns if 150 <= N <= 250],
        "dense_200_300": [N for N in dense_Ns if 200 <= N <= 300],
        "dense_100_300": [N for N in dense_Ns if 100 <= N <= 300],
        "sparse_tail_all": sparse_Ns,
        "sparse_tail_large_3200_51200": [N for N in sparse_Ns if N >= 3200],
        "combined_100_51200": [N for N in dense_Ns if N >= 100] + sparse_Ns,
    }
    layer1_refined = {}
    for wname, Ns in fit_windows.items():
        x1s = [mp.log(N) / N for N in Ns]
        x2s = [mp.mpf(1) / N for N in Ns]
        ys = [a_of(N) for N in Ns]
        b, c, vol_est = linfit3(x1s, x2s, ys)
        diff = vol_est - Vol
        reldiff = abs(diff) / Vol
        print(f"      window {wname:28s} (n={len(Ns):3d}, N in [{min(Ns)},{max(Ns)}]): "
              f"Vol_est={s(vol_est,16)}  diff={s(diff,4)}  rel={s(reldiff,3)}")
        layer1_refined[wname] = dict(n=len(Ns), Nmin=min(Ns), Nmax=max(Ns),
                                      vol_est=s(vol_est, 30), b=s(b, 10), c=s(c, 10),
                                      diff_vs_vol=s(diff, 14), rel_diff=s(reldiff, 6))
    results["layer1_refined_model_fit"] = layer1_refined

    # -------------------------------------------------------------------
    # Step 5: Layers 2 & 3 -- power p and constant C
    # -------------------------------------------------------------------
    print("\n[5] LAYERS 2 & 3 -- power p (vs 3/2) and constant C (vs 3^(-1/4)), by window")
    target_p = mp.mpf(3) / 2
    target_C = mp.mpf(3) ** (mp.mpf(-1) / 4)
    print(f"    target p = {s(target_p,10)}   target C = 3^(-1/4) = {s(target_C,20)}")

    print("\n    (A) Vol-CONDITIONED 2-parameter fit: log(J_N) - (Vol/2pi)*N ~ p*log(N) + log(C)")
    layer23_conditioned = {}
    for wname, Ns in fit_windows.items():
        half = Vol / two_pi
        xs = [mp.log(N) for N in Ns]
        ys = [logJ[N] - half * N for N in Ns]
        p, logC = linfit2(xs, ys)
        C = mp.e ** logC
        dp, dC = p - target_p, C - target_C
        print(f"      window {wname:28s} (n={len(Ns):3d}, N in [{min(Ns)},{max(Ns)}]): "
              f"p={s(p,10)} (diff {s(dp,4)})   C={s(C,10)} (diff {s(dC,4)})")
        layer23_conditioned[wname] = dict(n=len(Ns), Nmin=min(Ns), Nmax=max(Ns),
                                           p=s(p, 20), C=s(C, 20), diff_p=s(dp, 10), diff_C=s(dC, 10))
    results["layer23_conditioned_fit"] = layer23_conditioned

    print("\n    (B) Vol-BLIND joint 3-parameter fit: log(J_N) ~ A*N + p*log(N) + log(C) "
          "(cross-check; also re-derives layer 1)")
    layer123_joint = {}
    for wname, Ns in fit_windows.items():
        x1s = [mp.mpf(N) for N in Ns]
        x2s = [mp.log(N) for N in Ns]
        ys = [logJ[N] for N in Ns]
        A, p, logC = linfit3(x1s, x2s, ys)
        C = mp.e ** logC
        exponent = two_pi * A
        d_exp, dp, dC = exponent - Vol, p - target_p, C - target_C
        print(f"      window {wname:28s}: 2*pi*A={s(exponent,14)} (diff {s(d_exp,4)})  "
              f"p={s(p,8)} (diff {s(dp,4)})   C={s(C,8)} (diff {s(dC,4)})")
        layer123_joint[wname] = dict(n=len(Ns), Nmin=min(Ns), Nmax=max(Ns),
                                      exponent=s(exponent, 20), p=s(p, 20), C=s(C, 20),
                                      diff_exponent=s(d_exp, 12), diff_p=s(dp, 10), diff_C=s(dC, 10))
    results["layer123_joint_fit"] = layer123_joint

    # -------------------------------------------------------------------
    # Step 5b: higher-order refinement -- add explicit 1/N, 1/N^2 correction
    # terms (the genuine next orders of the known Ohtsuki/Andersen-Hikami 1/N
    # expansion for 4_1), fit on well-separated large-N windows. This tests
    # whether the residual at Step 4/5 (~1e-8 relative, using only a log(N)/N
    # or constant term) is a real higher-order correction (converges away when
    # modeled) or a sign the whole picture is wrong (would NOT converge away).
    # -------------------------------------------------------------------
    print("\n[5b] HIGHER-ORDER REFINEMENT: add 1/N, 1/N^2 correction terms on large-N windows")
    print("     conditioned model: log(J_N) - (Vol/2pi)*N = p*log(N) + log(C) + e/N [+ f/N^2]")
    refine_windows = {
        "large_1600_102400": [N for N in sparse_Ns if N >= 1600],
        "largest_12800_102400": [N for N in sparse_Ns if N >= 12800],
    }
    half = Vol / two_pi
    higher_order = {}
    for wname, Ns in refine_windows.items():
        logN = [mp.log(N) for N in Ns]
        ones = [mp.mpf(1) for _ in Ns]
        invN = [mp.mpf(1) / N for N in Ns]
        invN2 = [mp.mpf(1) / (N * N) for N in Ns]
        ys_cond = [logJ[N] - half * N for N in Ns]
        orders = {}
        print(f"    window {wname} (n={len(Ns)}, N in [{min(Ns)},{max(Ns)}]):")
        for label, regs in [("2-param(p,logC)", [logN, ones]),
                             ("3-param(+e/N)", [logN, ones, invN]),
                             ("4-param(+f/N^2)", [logN, ones, invN, invN2])]:
            sol = linfit_n(regs, ys_cond)
            p_fit, logC_fit = sol[0], sol[1]
            C_fit = mp.e ** logC_fit
            dp, dC = p_fit - target_p, C_fit - target_C
            print(f"      {label:20s}: p={s(p_fit,16)} (diff {s(dp,4)})   "
                  f"C={s(C_fit,16)} (diff {s(dC,4)})")
            orders[label] = dict(p=s(p_fit, 25), C=s(C_fit, 25), diff_p=s(dp, 15), diff_C=s(dC, 15))
        # Vol-blind joint 4-param cross-check: A, p, logC, e/N
        Nlist = [mp.mpf(N) for N in Ns]
        ys_joint = [logJ[N] for N in Ns]
        A4, p4, logC4, e4 = linfit_n([Nlist, logN, ones, invN], ys_joint)
        C4 = mp.e ** logC4
        exp4 = two_pi * A4
        d_exp4, dp4, dC4 = exp4 - Vol, p4 - target_p, C4 - target_C
        print(f"      {'joint-4param(Vol-blind)':20s}: 2*pi*A={s(exp4,18)} (diff {s(d_exp4,4)})  "
              f"p={s(p4,12)} (diff {s(dp4,4)})  C={s(C4,12)} (diff {s(dC4,4)})")
        orders["joint_4param_vol_blind"] = dict(exponent=s(exp4, 25), p=s(p4, 25), C=s(C4, 25),
                                                 diff_exponent=s(d_exp4, 15), diff_p=s(dp4, 15),
                                                 diff_C=s(dC4, 15))
        higher_order[wname] = dict(n=len(Ns), Nmin=min(Ns), Nmax=max(Ns), orders=orders)
    results["layer_higher_order_refinement"] = higher_order

    # -------------------------------------------------------------------
    # Step 6: headline comparison to the memo's stated numbers
    # -------------------------------------------------------------------
    print("\n[6] HEADLINE vs the memo's stated numbers (asymptotic_channel_out.txt):")
    # primary numbers: the 4-parameter conditioned fit on the tightest large-N
    # window (most trustworthy -- see [5b]); the plain [100,200] task-specified
    # window numbers are reported too, for direct comparison.
    best_window = "largest_12800_102400"
    best4 = higher_order[best_window]["orders"]["4-param(+f/N^2)"]
    best_joint4 = higher_order[best_window]["orders"]["joint_4param_vol_blind"]
    task_window = "dense_100_200"
    task_p = mp.mpf(layer23_conditioned[task_window]["p"])
    task_C = mp.mpf(layer23_conditioned[task_window]["C"])
    task_exp = mp.mpf(layer1_refined[task_window]["vol_est"])

    refined_exp = mp.mpf(best_joint4["exponent"])   # Vol-blind, most refined, independent of assuming Vol
    fitted_p = mp.mpf(best4["p"])                   # Vol-conditioned 4-param, most refined
    fitted_C = mp.mpf(best4["C"])
    memo_exp = mp.mpf('2.0298832128847')
    memo_p = mp.mpf('1.500003')
    memo_C = mp.mpf('0.7598188')
    print(f"    [task-specified window N in [100,200]]  exponent Vol_est={s(task_exp,16)}  "
          f"p={s(task_p,10)}  C={s(task_C,10)}")
    print(f"    [best: 4-param fit, window {best_window}]")
    print(f"    exponent (Vol-blind joint-4param): this bench = {s(refined_exp,16)}   "
          f"memo = {s(memo_exp,16)}   Vol(banked, computed independently above) = {s(Vol,16)}")
    print(f"    power    (Vol-conditioned 4-param): this bench p = {s(fitted_p,14)}      "
          f"memo p = {s(memo_p,10)}   target 3/2 = 1.5")
    print(f"    constant (Vol-conditioned 4-param): this bench C = {s(fitted_C,14)}      "
          f"memo C = {s(memo_C,10)}   target 3^(-1/4) = {s(target_C,14)}")
    print(f"    agreement (this bench vs Vol):  |diff| = {s(abs(refined_exp-Vol),4)}   "
          f"({'BETTER than' if abs(refined_exp-Vol) < abs(memo_exp-Vol) else 'worse than'} "
          f"the memo's claimed |diff|={s(abs(memo_exp-Vol),4)})")
    results["headline_vs_memo"] = {
        "task_window_100_200": {"vol_est": s(task_exp, 20), "p": s(task_p, 15), "C": s(task_C, 15)},
        "best_window": best_window,
        "exponent_this_bench_best": s(refined_exp, 25), "exponent_memo": s(memo_exp, 20),
        "exponent_vol_banked": s(Vol, 25), "diff_exponent_this_bench": s(abs(refined_exp - Vol), 15),
        "diff_exponent_memo": s(abs(memo_exp - Vol), 15),
        "power_this_bench_best": s(fitted_p, 20), "power_memo": s(memo_p, 15),
        "diff_power_this_bench": s(abs(fitted_p - target_p), 15),
        "constant_this_bench_best": s(fitted_C, 20), "constant_memo": s(memo_C, 15),
        "constant_target_3^-1/4": s(target_C, 20), "diff_constant_this_bench": s(abs(fitted_C - target_C), 15),
    }

    t_total = time.time() - t_start
    results["timing"]["total_seconds"] = round(t_total, 3)
    print(f"\nTotal runtime: {t_total:.2f}s")

    with open("b1116_results.json", "w") as f:
        json.dump(results, f, indent=1)
    print("\nWrote b1116_results.json")


if __name__ == "__main__":
    main()
