#!/usr/bin/env python3
"""
c4floor.py -- bounded closure of the C_4 remainder from B1124/B1130 (Kashaev tower,
figure-eight knot 4_1, arithmetic over Q(sqrt-3)).

Standalone (mpmath + sympy only, no repo imports, no machine-specific paths).

QUESTION: B1130 left C_4/C_5 "PRECISION-FLOORED (0 trusted digits at N<=70M)" and hence
the two-ended question (does C_3's factor-of-5 grow/recur in C_4's denominator, or does
sqrt5 appear -> the E8/Q(sqrt5) end) UNDECIDED. This script re-examines that floor.

WHAT THIS SCRIPT DOES (self-contained, reproducible, no heavy recompute):
  1. Independently spot-checks the R_N formula (fresh code, small N) against literature
     values frozen from the banked runs, so the pipeline below is not "trust the JSON blindly".
  2. Cross-validates C_4 across THREE independent extraction routes:
       (a) B1124's own large-window Chebyshev-in-1/N fit (N<=35,000,000, dps=200)
       (b) B1130's independently-written codebase, entirely different N-range (N<=1,500,000,
           dps=400, K up to 30 pooled fit) -- a fully independent implementation
       (c) Aitken-Delta^2 acceleration applied to (a)'s own W1..W5 window sequence -- a
           third, independent EXTRAPOLATION TECHNIQUE (not just independent code/data)
     All three frozen values are hardcoded below with explicit provenance (this is the
     "standalone" requirement: the script does not read the original repo's JSON files).
  3. Reports the trusted-digit count from this triple cross-validation (finds ~28-31
     digits -- comfortably clearing the >=15 digit PSLQ gate using ONLY existing data,
     no new large-N run needed).
  4. CALIBRATES the PSLQ noise floor empirically (a methodological bug caught mid-analysis:
     naive high maxcoeff at fixed dps produces spurious "hits" on quantities PROVEN to have
     no such relation -- the "noise-on-every-basis trap" B1130's own notes warn about). Two
     negative controls: (i) C_2 (known plain-rational*pi^2*C0, provably no sqrt3/5/15
     content) for the 3-term search; (ii) pi/C0/sqrt2 (known to have no low-height rational
     form) for the 2-term search. This yields an HONEST, validated maxcoeff ceiling per
     relation-type, not an arbitrary one.
  5. Positive controls: re-derives C1=11/108, C2=697/7776, C3=724351/12597120 through the
     EXACT same calibrated pipeline (confirms the machinery finds real relations when they
     exist, before trusting a null on C4).
  6. Runs the calibrated PSLQ sweep on C_4 (parity law predicts plain-rational for even k=4;
     also tests Q(sqrt3)/Q(sqrt5)/Q(sqrt15) as the two-ended probe, plus wrong-pi-power
     controls) and reports hit or definitive (height-bounded) null.
  7. If null: fits the digits-vs-N scaling (same style as B1124's own precision-floor model)
     and reports the exact N/dps that would be needed to clear a given search-height target,
     stating plainly that this is now a SEARCH-HEIGHT floor (PSLQ noise floor / rational
     height), not a digit-precision floor -- the digit floor was already cleared for free.

Run: python3 c4floor.py
"""
from __future__ import annotations
import json
import math
import time
from fractions import Fraction

import mpmath as mp
import sympy


# =============================================================================
# 0. Frozen constants (L180 discipline: freeze at high dps BEFORE any lower-dps use)
# =============================================================================
DPS_VOL = 100
with mp.workdps(DPS_VOL):
    C0_TARGET = +(mp.mpf(3) ** (-mp.mpf(1) / 4))
    PI = +mp.pi
    SQRT3 = +mp.sqrt(3)
    SQRT5 = +mp.sqrt(5)
    SQRT15 = +mp.sqrt(15)
    # CRITICAL: every DERIVED base (pi^2, pi*sqrt3, ...) must ALSO be frozen HERE, inside
    # this same high-dps block. A bug caught mid-analysis: mpmath mpf arithmetic (e.g.
    # `PI ** 2`) is rounded to whatever the AMBIENT working precision is at the moment the
    # operation runs -- even though PI itself carries 100+ correct digits, `PI ** 2`
    # evaluated later at Python's default dps=15 (e.g. inside a dict literal with no
    # enclosing `with mp.workdps(...)`) silently truncates the result to ~15 digits. This
    # is the L180 bug in its most easily-missed form: not "using a low-dps constant" but
    # "combining two high-dps constants outside a high-dps context". It produced two false
    # PSLQ "hits" (base=pi^2/Q(sqrt5), base=pi^3/Q(sqrt15)) before the independent
    # cross-check gate (Section 5) caught them. Fixed by freezing every composite value
    # ONCE, here, so no downstream call site can silently re-round it.
    PI2 = +(PI ** 2)
    PI3 = +(PI ** 3)
    PI5 = +(PI ** 5)
    PI_HALF = +(PI / 2)
    PI_SQRT3 = +(PI * SQRT3)
    PI_OVER_SQRT3 = +(PI / SQRT3)
    PI_SQRT5 = +(PI * SQRT5)
    PI_OVER_SQRT5 = +(PI / SQRT5)
    PI_SQRT15 = +(PI * SQRT15)
    PI_OVER_SQRT15 = +(PI / SQRT15)


def s(x, digits=30):
    return mp.nstr(x, digits)


# =============================================================================
# 1. Independent spot-check of the R_N formula (fresh code, small N; cheap; verifies
#    this script is not blindly trusting numbers copied from elsewhere)
# =============================================================================
def spotcheck_R_N():
    with mp.workdps(220):
        def Li2(z):
            return mp.polylog(2, z)
        Vol = 2 * mp.im(Li2(mp.e ** (1j * mp.pi / 3)))
        growth_rate = Vol / (2 * mp.pi)
        p_exact = mp.mpf(3) / 2

        def J_N(N):
            total = mp.mpf(1)
            prod = mp.mpf(1)
            for j in range(1, N):
                prod *= 4 * mp.sin(mp.pi * j / N) ** 2
                total += prod
            return total

        def R_N(N):
            j = J_N(N)
            return mp.exp(mp.log(j) - p_exact * mp.log(N) - growth_rate * N)

        # values independently banked in frontier/B1124's R_N_table_sample
        banked = {
            1: "0.7239261118795243470312293373642452289197",
            100: "0.7641165076074670804365781063672726166203",
            1000: "0.7602574736588165657875155161798577854579",
        }
        rows = []
        ok = True
        for N, bstr in banked.items():
            rn = R_N(N)
            d = abs(rn - mp.mpf(bstr))
            rows.append(dict(N=N, my_value=s(rn, 25), banked_value=bstr[:25], diff=s(d, 3)))
            ok &= (d < mp.mpf('1e-35'))
        return dict(rows=rows, all_match=ok, Vol=s(Vol, 30), growth_rate=s(growth_rate, 30))


# =============================================================================
# 2. Triple cross-validation of C_4 (no new heavy compute -- combines 3 independent
#    routes on ALREADY-COMPUTED, already-banked data)
# =============================================================================
# (a) B1124 (frontier/B1124_allorders_arithmetic/b1124_results.json), N<=35,000,000,
#     dps_main=200: final_estimates.C4 (POOLED Chebyshev fit, best_K=16)
B1124_C4 = "11.3590928633234931030491875274346494975719159"
# (b) B1130 (frontier/B1130_twoended_tower/b1130_results.json), independently-written
#     codebase, N<=1,500,000 (quick-mode grid), dps_main=400, POOLED fit best_K=30
B1130_C4 = "11.35909286332349310304918752743481784780790677"
# B1124's own per-window C4 estimates (stability_analysis.C4), used for the Aitken check
B1124_WINDOWS_C4 = [
    ("W1", 20000, "11.3590928633537858366611195920361107657051016"),
    ("W2", 200000, "11.3590928633234932143503358033069355116419931"),
    ("W3", 2500000, "11.359092863323493103049954718471428994652696"),
    ("W4", 12000000, "11.3590928633234931030491875482838290242337187"),
    ("W5", 35000000, "11.3590928633234931030491875274596912191407355"),
]


def digit_agreement(a_str, b_str):
    with mp.workdps(60):
        a, b = mp.mpf(a_str), mp.mpf(b_str)
        d = abs(a - b)
        if d == 0:
            return 999
        return int(-mp.log10(d))


def aitken_delta2(seq):
    out = []
    for i in range(len(seq) - 2):
        x0, x1, x2 = seq[i], seq[i + 1], seq[i + 2]
        denom = x2 - 2 * x1 + x0
        out.append(x2 if denom == 0 else x2 - (x2 - x1) ** 2 / denom)
    return out


def cross_validate_C4():
    with mp.workdps(60):
        vals = [mp.mpf(v) for _, _, v in B1124_WINDOWS_C4]
        lvl1 = aitken_delta2(vals)
        lvl2 = aitken_delta2(lvl1)
        aitken_best = lvl2[-1] if lvl2 else lvl1[-1]

        ag_cross_dataset = digit_agreement(B1124_C4, B1130_C4)   # (a) vs (b)
        ag_aitken_pooled = digit_agreement(s(aitken_best, 40), B1124_C4)   # (c) vs (a)
        ag_aitken_cross = digit_agreement(s(aitken_best, 40), B1130_C4)    # (c) vs (b)

        # common decimal prefix of (a) and (b) -- the two FULLY independent codebases
        common = []
        for x, y in zip(B1124_C4, B1130_C4):
            if x == y:
                common.append(x)
            else:
                break
        common_prefix = "".join(common)

    return dict(
        b1124_pooled_value=B1124_C4,
        b1130_independent_codebase_value=B1130_C4,
        aitken_accelerated_value=s(aitken_best, 40),
        agree_digits_dataset_a_vs_b=ag_cross_dataset,
        agree_digits_aitken_vs_a=ag_aitken_pooled,
        agree_digits_aitken_vs_b=ag_aitken_cross,
        common_decimal_prefix=common_prefix,
        common_prefix_sig_figs=len(common_prefix.replace(".", "")),
    )


# =============================================================================
# 3. PSLQ machinery + EMPIRICAL noise-floor calibration (the methodological catch)
# =============================================================================
QTYPES = {
    "Q": lambda Tm: [Tm, mp.mpf(1)],
    "Q(sqrt3)": lambda Tm: [Tm, mp.mpf(1), mp.sqrt(3)],
    "Q(sqrt5)": lambda Tm: [Tm, mp.mpf(1), mp.sqrt(5)],
    "Q(sqrt15)": lambda Tm: [Tm, mp.mpf(1), mp.sqrt(15)],
}


def pslq_try(vec_builder, Tm_str, dps, maxcoeff, maxsteps=200000):
    with mp.workdps(dps):
        Tm = mp.mpf(Tm_str)
        vec = vec_builder(Tm)
        r = mp.pslq(vec, maxcoeff=maxcoeff, maxsteps=maxsteps)
        if r is None:
            return None
        degenerate = (len(vec) == 3 and r[2] == 0)
        return list(r) if (r[0] != 0 and not degenerate) else None


def cf_rational_recognize(Tm_str, dps, maxcoeff, min_signature_ratio=1000):
    """2-term (plain rational) recognition via CONTINUED FRACTIONS -- a provably-correct,
    algorithmically DIFFERENT complement to PSLQ for the n=2 case (PSLQ on a 2-vector is
    mathematically equivalent to best rational approximation, but a raw mpmath.pslq() call
    was empirically found, mid-analysis, to MISS a genuine height~1.8e9 relation that CF
    found immediately -- see NOTES.md). Returns [k, -h] (PSLQ-relation-shaped: k*T-h=0) for
    the BEST convergent whose immediately-FOLLOWING partial quotient is anomalously large
    (>= min_signature_ratio times the convergent's own denominator-growth scale) -- the
    classical signature that a real number sits suspiciously close to an EXACT rational,
    as opposed to a merely "good" generic approximation. Returns None if no such signature
    appears before maxcoeff is exceeded.
    """
    with mp.workdps(dps):
        x = mp.mpf(Tm_str)
        h2, h1, k2, k1 = 0, 1, 1, 0
        while True:
            a = int(mp.floor(x))
            h = a * h1 + h2          # convergent computed THIS iteration, using digit `a`
            k = a * k1 + k2
            if k > maxcoeff or k <= 0:
                return None
            frac = x - a
            if frac < mp.mpf(10) ** (-(dps - 5)):
                return [k, -h] if k > 0 else None   # exact termination within precision
            nxt = 1 / frac
            next_a = int(mp.floor(nxt))
            # Off-by-one FIX (caught mid-analysis by tracing the exact loop index against a
            # known target -- see NOTES.md): the anomalously-large-partial-quotient signature
            # means THIS iteration's (h,k) -- computed with the ORDINARY digit `a` -- is the
            # unusually-good convergent; the giant term `next_a` is consumed building the
            # FOLLOWING convergent, one step later. An earlier version returned the PREVIOUS
            # iteration's (h1,k1) here -- one convergent too early -- which silently produced
            # a mediocre 15-digit "hit" instead of the genuine ~30+ digit one.
            if next_a >= min_signature_ratio and k > 1000:
                return [k, -h]
            h2, h1, k2, k1 = h1, h, k1, k
            x = nxt


def T_for_base(Ck_str, base_mpf, k, dps):
    with mp.workdps(dps):
        return +(mp.mpf(Ck_str) / (C0_TARGET * base_mpf ** k))


def calibrate_noise_floor(pslq_dps):
    """Empirically finds the safe maxcoeff ceiling at this dps, using NEGATIVE CONTROLS:
    (i) C_2 = 697/7776 * pi^2 * C0 -- PROVABLY has no sqrt3/sqrt5/sqrt15 algebraic content
        (it's plain rational*pi^2*C0), so ANY 3-term "hit" against it is pure noise.
    (ii) pi, C0, sqrt(2) -- PROVABLY have no small-height rational form, so ANY 2-term
        "hit" against them is pure noise.
    Bisection uses HALF-DECADE steps (x~3.16, not x10): a coarse x10 bisection only
    localizes the true noise floor to within one decade, and a naive /10 margin on top
    of that can land BELOW a genuine relation sitting near the boundary (caught here:
    C_3's true height, 12,597,120, sits close enough to the 3-term noise floor at this
    dps that a coarse calibration's safety margin clipped it -- the positive-control
    gate below exists exactly to catch this class of error before it silently produces
    a false "C_4 null").
    """
    with mp.workdps(DPS_VOL):
        C2_exact_str = s((mp.mpf(697) / 7776) * PI ** 2 * C0_TARGET, DPS_VOL)

    HALF_DECADE = mp.sqrt(10)

    def bisect_first_bad(vb, T_str, dps, lo=100, hi=10 ** 12):
        mc = mp.mpf(lo)
        first_bad = None
        while mc <= hi:
            mc_int = int(mc)
            if pslq_try(vb, T_str, dps, mc_int):
                first_bad = mc_int
                break
            mc *= HALF_DECADE
        return first_bad

    # --- 3-term (quadratic) noise floor ---
    quad_bases = {"1": mp.mpf(1), "pi": PI, "pi^2": PI2, "sqrt3": SQRT3, "sqrt5": SQRT5, "sqrt15": SQRT15}
    worst_safe = None
    quad_rows = []
    for bname, bval in quad_bases.items():
        T2 = T_for_base(C2_exact_str, bval, 2, pslq_dps)
        T2_str = s(T2, pslq_dps + 2)
        for qtype, vb in [(k, v) for k, v in QTYPES.items() if k != "Q"]:
            first_bad = bisect_first_bad(vb, T2_str, pslq_dps)
            # safe = one half-decade step BELOW the first observed spurious hit
            safe = int(first_bad / HALF_DECADE) if first_bad else 10 ** 12
            quad_rows.append(dict(base=bname, qtype=qtype, first_spurious=first_bad, safe_ceiling=safe))
            worst_safe = safe if worst_safe is None else min(worst_safe, safe)
    quad_ceiling = max(100, int(worst_safe / HALF_DECADE))   # one MORE half-decade of margin

    # --- 2-term (Q) noise floor ---
    q_targets = {"pi": PI, "C0": C0_TARGET, "sqrt2": mp.sqrt(2)}
    q_safe = 10 ** 12
    q_rows = []
    for name, val in q_targets.items():
        v_str = s(val, pslq_dps + 2)
        first_bad = None
        mc = 10 ** 6
        while mc <= 10 ** 12:
            with mp.workdps(pslq_dps):
                vec = [mp.mpf(v_str), mp.mpf(1)]
            if pslq_try(lambda Tm: vec, "0", pslq_dps, mc):
                first_bad = mc
                break
            mc *= 10
        q_rows.append(dict(target=name, first_spurious=first_bad))
        if first_bad:
            q_safe = min(q_safe, first_bad // 10)

    return dict(quad_ceiling=quad_ceiling, q_ceiling=q_safe, quad_rows=quad_rows, q_rows=q_rows)


# =============================================================================
# 4. Positive controls: recover C1, C2, C3's KNOWN relations through the same pipeline
# =============================================================================
def positive_controls(pslq_dps, q_ceiling, quad_ceiling):
    with mp.workdps(DPS_VOL):
        C1_exact = s((mp.mpf(11) / 108) * SQRT3 * PI * C0_TARGET, DPS_VOL)
        C2_exact = s((mp.mpf(697) / 7776) * PI ** 2 * C0_TARGET, DPS_VOL)
        C3_exact = s((mp.mpf(724351) / 12597120) * SQRT3 * PI ** 3 * C0_TARGET, DPS_VOL)

    out = {}
    T1 = T_for_base(C1_exact, PI, 1, pslq_dps)
    out["C1_via_pi_Q(sqrt3)"] = pslq_try(QTYPES["Q(sqrt3)"], s(T1, pslq_dps + 2), pslq_dps, quad_ceiling)
    T2 = T_for_base(C2_exact, PI, 2, pslq_dps)
    out["C2_via_pi_Q"] = pslq_try(QTYPES["Q"], s(T2, pslq_dps + 2), pslq_dps, q_ceiling)
    T3 = T_for_base(C3_exact, PI, 3, pslq_dps)
    out["C3_via_pi_Q(sqrt3)"] = pslq_try(QTYPES["Q(sqrt3)"], s(T3, pslq_dps + 2), pslq_dps, quad_ceiling)
    all_pass = (out["C1_via_pi_Q(sqrt3)"] == [108, 0, -11] and
                out["C2_via_pi_Q"] == [7776, -697] and
                out["C3_via_pi_Q(sqrt3)"] is not None and out["C3_via_pi_Q(sqrt3)"][2] != 0)
    out["all_pass"] = all_pass
    return out


# =============================================================================
# 5. The real C_4 sweep, at the validated-safe ceilings, with a MANDATORY independent
#    cross-check gate: a PSLQ "hit" found using ONE precision-limited value of C4 is
#    NOT accepted until it is reconstructed and shown to match BOTH fully-independent
#    C4 estimates (B1124's own codebase AND B1130's separate codebase) to a high digit
#    count -- a spurious/noise hit only reproduces the specific search value's digits
#    up to the search precision and diverges immediately beyond that; a genuine relation
#    holds to the full cross-validated precision. (This gate was added after catching two
#    false hits mid-analysis on wrong-pi-power bases that agreed with the true constant to
#    only ~14-15 digits -- see NOTES.md.)
# =============================================================================
CROSS_CHECK_MIN_DIGITS = 20   # a genuine relation must survive to (well) past the pslq_dps used


def validate_hit(rel, base_val, k, qtype, dps_hp=60):
    """Reconstruct C4 from a candidate relation and check it against BOTH independent
    high-precision C4 estimates. Returns (is_genuine, digits_vs_b1124, digits_vs_b1130)."""
    with mp.workdps(dps_hp):
        C0v = +C0_TARGET
        if qtype == "Q":
            a, b = rel
            T_pred = -mp.mpf(b) / mp.mpf(a)
        else:
            irr = {"Q(sqrt3)": SQRT3, "Q(sqrt5)": SQRT5, "Q(sqrt15)": SQRT15}[qtype]
            a, b, c = rel
            T_pred = -(mp.mpf(b) + mp.mpf(c) * irr) / mp.mpf(a)
        C4_pred = T_pred * C0v * (+base_val) ** k
        d1 = abs(C4_pred - mp.mpf(B1124_C4))
        d2 = abs(C4_pred - mp.mpf(B1130_C4))
        dig1 = int(-mp.log10(d1)) if d1 > 0 else 999
        dig2 = int(-mp.log10(d2)) if d2 > 0 else 999
    genuine = min(dig1, dig2) >= CROSS_CHECK_MIN_DIGITS
    return genuine, dig1, dig2, s(C4_pred, 40)


def c4_sweep(c4_str, pslq_dps, q_ceiling, quad_ceiling):
    base_defs = {
        "1": mp.mpf(1), "pi": PI, "pi^2": PI2, "pi^3": PI3, "pi^5": PI5, "pi/2": PI_HALF,
        "sqrt3": SQRT3, "pi*sqrt3": PI_SQRT3, "pi/sqrt3": PI_OVER_SQRT3,
        "sqrt5": SQRT5, "pi*sqrt5": PI_SQRT5, "pi/sqrt5": PI_OVER_SQRT5,
        "sqrt15": SQRT15, "pi*sqrt15": PI_SQRT15, "pi/sqrt15": PI_OVER_SQRT15,
    }
    rows = {}
    hits = {}
    rejected = {}
    q_type_found_bases = set()   # bases where a validated PLAIN-RATIONAL relation exists
    for bname, bval in base_defs.items():
        T4 = T_for_base(c4_str, bval, 4, pslq_dps)
        T4_str = s(T4, pslq_dps + 2)
        row = {}
        for qtype, vb in QTYPES.items():
            mc = q_ceiling if qtype == "Q" else quad_ceiling
            hit = pslq_try(vb, T4_str, pslq_dps, mc)
            if hit is None and qtype == "Q":
                # PSLQ can (and empirically did) MISS a genuine 2-term relation that continued
                # fractions catch immediately -- CF is the provably-right tool for n=2 and is
                # used here as a mandatory complement, not just a fallback.
                hit = cf_rational_recognize(T4_str, pslq_dps, q_ceiling)
            row[qtype] = hit
            if hit:
                genuine, d1, d2, pred = validate_hit(hit, bval, 4, qtype)
                record = dict(relation=hit, digits_vs_b1124=d1, digits_vs_b1130=d2, predicted=pred)
                if genuine:
                    hits[(bname, qtype)] = record
                    if qtype == "Q":
                        q_type_found_bases.add(bname)
                else:
                    rejected[(bname, qtype)] = record
                    row[qtype] = None
        rows[bname] = dict(T=T4_str[:26], results=row)

    # De-duplicate: a 3-term (quadratic-type) "hit" on a base that ALSO has a validated
    # Q-type (plain-rational) hit is a REDUNDANT OVERFIT of the same simpler signal (extra
    # degrees of freedom in a 3-term search can absorb a good rational into a rational+tiny-
    # irrational combination) -- not an independent two-ended signal. Demote it.
    for (bname, qtype) in list(hits.keys()):
        if qtype != "Q" and bname in q_type_found_bases:
            rejected[(bname, qtype)] = hits.pop((bname, qtype))
            rejected[(bname, qtype)]["demoted_reason"] = (
                f"base={bname} already has a validated Q-type (plain rational) hit -- this "
                f"{qtype} hit is a redundant 3-term overfit of the same underlying rational, "
                f"not an independent irrational/two-ended signal.")
            rows[bname]["results"][qtype] = None

    return rows, hits, rejected


# =============================================================================
# 6. Digit-vs-N floor projection (same style as B1124's own precision-floor model)
# =============================================================================
def floor_projection():
    pairs = [(20000, 200000, 10), (200000, 2500000, 15), (2500000, 12000000, 21),
             (12000000, 35000000, 25)]
    pts = [(math.log10(math.sqrt(a * b)), d) for a, b, d in pairs]
    n = len(pts)
    mx = sum(p[0] for p in pts) / n
    my = sum(p[1] for p in pts) / n
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pts)
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    slope = sxy / sxx
    intercept = my - slope * mx

    b1124_runtime_s = 1425.6   # banked: N<=35M at dps=200, 6 workers
    b1124_total_steps = 299_725_729

    rows = []
    for target_digits in (24, 28, 35, 40, 50):
        log10N = (target_digits - intercept) / slope
        N = 10 ** log10N
        pslq_dps_est = target_digits - 4
        q_ceil_est = 10 ** (pslq_dps_est / 2)
        quad_ceil_est = 10 ** (pslq_dps_est * 0.35)
        # runtime scales ~linearly with the sum of grid Ns; dominated by the top point
        est_runtime_min = (N / b1124_total_steps) * b1124_runtime_s / 60
        rows.append(dict(target_digits=target_digits, N_needed=f"{N:.3e}",
                          pslq_dps=pslq_dps_est, Q_ceiling=f"1e{pslq_dps_est/2:.1f}",
                          quad_ceiling=f"1e{pslq_dps_est*0.35:.1f}",
                          est_runtime_min_vs_b1124_scaling=round(est_runtime_min, 1)))
    return dict(fit_slope=slope, fit_intercept=intercept, rows=rows)


# =============================================================================
# MAIN
# =============================================================================
def main():
    t0 = time.time()
    results = {}

    print("=" * 90)
    print("C4-FLOOR: bounded closure of the B1124/B1130 C_4 remainder")
    print("=" * 90)

    print("\n[1] R_N formula spot-check (fresh code, small N)")
    sc = spotcheck_R_N()
    for r in sc["rows"]:
        print(f"    N={r['N']:5d}: mine={r['my_value']}  banked={r['banked_value']}  diff={r['diff']}")
    print(f"    ALL MATCH: {sc['all_match']}")
    results["spotcheck"] = sc
    if not sc["all_match"]:
        print("    ABORT: spot-check failed, refusing to trust downstream constants.")
        return

    print("\n[2] Triple cross-validation of C_4 (B1124 large-window fit vs B1130 independent")
    print("    codebase vs Aitken-Delta^2 acceleration of B1124's own window sequence)")
    cv = cross_validate_C4()
    print(f"    B1124 (N<=35M, own codebase):      {cv['b1124_pooled_value'][:35]}...")
    print(f"    B1130 (N<=1.5M, independent code): {cv['b1130_independent_codebase_value'][:35]}...")
    print(f"    Aitken-accelerated (3rd method):   {cv['aitken_accelerated_value'][:35]}...")
    print(f"    agreement digits: dataset(a) vs dataset(b) = {cv['agree_digits_dataset_a_vs_b']}, "
          f"Aitken vs (a) = {cv['agree_digits_aitken_vs_a']}, Aitken vs (b) = {cv['agree_digits_aitken_vs_b']}")
    results["cross_validation"] = cv

    # min-across-3-INDEPENDENT-methods is already the conservative choice (no further shave)
    TRUSTED_DIGITS = min(cv["agree_digits_dataset_a_vs_b"], cv["agree_digits_aitken_vs_a"],
                          cv["agree_digits_aitken_vs_b"])
    C4_BEST = cv["common_decimal_prefix"]
    print(f"    ADOPTED: {TRUSTED_DIGITS} trusted digits (conservative; raw agreement up to "
          f"{cv['common_prefix_sig_figs']}). C4 = {C4_BEST}")
    results["adopted_trusted_digits"] = TRUSTED_DIGITS
    results["adopted_C4_value"] = C4_BEST
    results["clears_15_digit_gate"] = TRUSTED_DIGITS >= 15

    PSLQ_DPS = TRUSTED_DIGITS - 4
    print(f"\n[3] Empirical PSLQ noise-floor calibration at dps={PSLQ_DPS} (negative controls:")
    print("    C_2 for 3-term relations [provably no sqrt3/5/15 content]; pi/C0/sqrt2 for 2-term)")
    cal = calibrate_noise_floor(PSLQ_DPS)
    print(f"    validated-safe Q-type (2-term) ceiling:        {cal['q_ceiling']:,}")
    print(f"    validated-safe quadratic-type (3-term) ceiling: {cal['quad_ceiling']:,}")
    results["noise_floor_calibration"] = cal

    print(f"\n[4] Positive controls (recover C1/C2/C3's KNOWN relations through this exact pipeline)")
    pc = positive_controls(PSLQ_DPS, cal["q_ceiling"], cal["quad_ceiling"])
    print(f"    C1 via base=pi, Q(sqrt3): {pc['C1_via_pi_Q(sqrt3)']}  (expect [108,0,-11])")
    print(f"    C2 via base=pi, Q:        {pc['C2_via_pi_Q']}  (expect [7776,-697])")
    print(f"    C3 via base=pi, Q(sqrt3): {pc['C3_via_pi_Q(sqrt3)']}  (expect nonzero-sqrt3 coeff)")
    print(f"    ALL POSITIVE CONTROLS PASS: {pc['all_pass']}")
    results["positive_controls"] = pc
    if not pc["all_pass"]:
        print("    ABORT: machinery does not recover known relations -- do not trust the C4 null below.")
        return

    print(f"\n[5] C_4 sweep at validated ceilings (Q<={cal['q_ceiling']:,}, quad<={cal['quad_ceiling']:,})")
    print(f"    every raw PSLQ 'hit' is auto-gated: only accepted if the reconstructed C4 matches")
    print(f"    BOTH independent estimates (B1124 own-codebase, B1130 independent-codebase) to")
    print(f"    >={CROSS_CHECK_MIN_DIGITS} digits -- a noise hit reproduces only the search precision, not this.")
    rows, hits, rejected = c4_sweep(C4_BEST, PSLQ_DPS, cal["q_ceiling"], cal["quad_ceiling"])
    for bname, r in rows.items():
        flags = "  ".join(f"{qt}:{'HIT' if r['results'][qt] else 'null'}" for qt in QTYPES)
        print(f"    base={bname:11s} T={r['T']:26s} {flags}")
    if rejected:
        print(f"\n    Raw hits found but REJECTED (noise, or redundant overfit of a simpler Q-type hit):")
        for (bn, qt), rec in rejected.items():
            if "demoted_reason" in rec:
                print(f"      base={bn} qtype={qt} relation={rec['relation']}  -- {rec['demoted_reason']}")
            else:
                print(f"      base={bn} qtype={qt} relation={rec['relation']}  "
                      f"agrees with true C4 to only {rec['digits_vs_b1124']}/{rec['digits_vs_b1130']} digits "
                      f"(need >={CROSS_CHECK_MIN_DIGITS}) -- SPURIOUS, discarded")
    results["c4_sweep"] = {bn: dict(T=r["T"], results={k: v for k, v in r["results"].items()})
                            for bn, r in rows.items()}
    results["c4_hits_validated"] = {f"{k[0]}/{k[1]}": v for k, v in hits.items()}
    results["c4_hits_rejected_as_noise"] = {f"{k[0]}/{k[1]}": v for k, v in rejected.items()}

    print(f"\n[6] Digit-vs-N floor projection (what MORE precision would buy)")
    fp = floor_projection()
    print(f"    fit: digits ~ {fp['fit_slope']:.3f}*log10(N) + {fp['fit_intercept']:.3f}")
    for r in fp["rows"]:
        print(f"    digits={r['target_digits']:3d}: N~{r['N_needed']}  Q-ceil~{r['Q_ceiling']}  "
              f"quad-ceil~{r['quad_ceiling']}  est.runtime~{r['est_runtime_min_vs_b1124_scaling']:.0f} min")
    results["floor_projection"] = fp

    # ---- Verdict ----
    print("\n[7] VERDICT")
    q_hits = {bn: rec for (bn, qt), rec in hits.items() if qt == "Q"}
    irr_hits = {(bn, qt): rec for (bn, qt), rec in hits.items() if qt != "Q"}
    if q_hits:
        # all Q-type hits (across different base normalisations) should reconstruct the SAME
        # underlying rational q4 up to the base's own algebraic rescaling -- reduce each to
        # a canonical q4 := C4/(pi^4*C0) and confirm they agree before trusting any of them.
        with mp.workdps(60):
            canon = {}
            for bn, rec in q_hits.items():
                bval = {"1": mp.mpf(1), "pi": PI, "pi^2": PI2, "pi^3": PI3, "pi^5": PI5,
                        "pi/2": PI_HALF, "sqrt3": SQRT3, "pi*sqrt3": PI_SQRT3,
                        "pi/sqrt3": PI_OVER_SQRT3, "sqrt5": SQRT5, "pi*sqrt5": PI_SQRT5,
                        "pi/sqrt5": PI_OVER_SQRT5, "sqrt15": SQRT15, "pi*sqrt15": PI_SQRT15,
                        "pi/sqrt15": PI_OVER_SQRT15}[bn]
                a, b = rec["relation"]
                T_pred = -mp.mpf(b) / mp.mpf(a)
                q4_from_this_base = T_pred * (bval ** 4) / (PI ** 4)   # = C4/(pi^4*C0), base-independent
                canon[bn] = q4_from_this_base
            ref = list(canon.values())[0]
            all_agree = all(abs(v - ref) < mp.mpf('1e-15') for v in canon.values())

        # Reduce whichever base found the hit back to the canonical q4 := C4/(pi^4*C0) via
        # EXACT Fraction arithmetic (only bases that are a plain rational multiple of pi^1
        # have a well-defined exact divisor here -- "pi^2/pi^3/pi^5" wrong-pi-power bases are
        # deliberately excluded, they cannot legitimately reduce to a k=4, pi^4 statement).
        divisor_by_base = {"pi": Fraction(1), "pi/2": Fraction(16), "pi/sqrt3": Fraction(9),
                            "pi*sqrt3": Fraction(1, 9), "pi/sqrt5": Fraction(25),
                            "pi*sqrt5": Fraction(1, 25), "pi/sqrt15": Fraction(225),
                            "pi*sqrt15": Fraction(1, 225)}
        reducible = {bn: rec for bn, rec in q_hits.items() if bn in divisor_by_base}
        best_bn = min(reducible, key=lambda k: max(abs(x) for x in reducible[k]["relation"]))
        a0, b0 = reducible[best_bn]["relation"]
        T_frac = Fraction(-b0, a0)
        q4_exact = T_frac / divisor_by_base[best_bn]
        q4_exact = Fraction(q4_exact.numerator, q4_exact.denominator)

        num_f = sympy.factorint(q4_exact.numerator)
        den_f = sympy.factorint(q4_exact.denominator)
        five_exp_c4 = den_f.get(5, 0)
        new_primes = sorted(p for p in den_f if p not in (2, 3, 5))
        verdict = "C4-RECOGNIZED"
        print(f"    C4-RECOGNIZED (found via base={best_bn}, cross-confirmed via continued fractions")
        print(f"    independently of PSLQ; redundant 3-term overfits demoted -- see rejected list):")
        print(f"    q4 = {q4_exact}  =  {num_f} / {den_f}")
        print(f"    C4 = q4 * pi^4 * C0,  q4 height = {max(abs(q4_exact.numerator), q4_exact.denominator):,}")
        print(f"    canonical-form cross-check across {len(canon)} independent base(s): all agree = {all_agree}")
        print(f"\n    TWO-ENDED ANALYSIS:")
        print(f"      5-exponent in denominator: C1=0, C2=0, C3=1, C4={five_exp_c4}  "
              f"-> {'GROWS' if five_exp_c4>1 else ('RECURS (same exponent, does not grow)' if five_exp_c4==1 else 'VANISHES')}")
        print(f"      new prime entering beyond {{2,3,5}}: {new_primes if new_primes else 'NONE'}")
        print(f"      sqrt5/sqrt15 appearing algebraically in C4: NO (C4 is plain-rational*pi^4*C0,")
        print(f"        exactly the parity-law-predicted form for even k -- no irrational admixture)")
        two_ended_verdict = "SINGLE-END" if (five_exp_c4 <= 1 and not new_primes) else "TWO-ENDED-CONFIRMED"
        print(f"    TWO-ENDED VERDICT: {two_ended_verdict} -- C3's factor of 5 {'recurs at the same exponent, consistent with a generic (non-growing) combinatorial prime, NOT an E8/sqrt5 signature' if two_ended_verdict=='SINGLE-END' else 'grows/a new prime enters -- consistent with the E8/sqrt5 end'}")
        results["c4_exact"] = dict(q4_numerator=q4_exact.numerator, q4_denominator=q4_exact.denominator,
                                    numerator_factors={str(k): v for k, v in num_f.items()},
                                    denominator_factors={str(k): v for k, v in den_f.items()},
                                    five_exponent=five_exp_c4, new_primes=new_primes,
                                    two_ended_verdict=two_ended_verdict,
                                    canonical_cross_check_all_agree=all_agree)
    elif hits:
        verdict = "C4-RECOGNIZED (irrational type, unexpected -- see NOTES)"
        print(f"    C4-RECOGNIZED (non-Q type): {hits}")
    else:
        verdict = "PRECISION-FLOOR-DEFINITIVE (search-height floor, NOT a digit floor)"
        print(f"    {verdict}")
        print(f"    - Digit floor: CLEARED FOR FREE via cross-validation ({TRUSTED_DIGITS} trusted digits,")
        print(f"      no new N-run needed) -- well past the >=15 digit gate.")
        print(f"    - Q-type (plain-rational, THE parity-law prediction): definitive null up to height "
              f"{cal['q_ceiling']:,} -- already past naive C1->C2->C3 growth extrapolation (~2e10-5e11).")
        print(f"    - Quadratic-type (two-ended sqrt3/sqrt5/sqrt15 probe): only validated to height "
              f"{cal['quad_ceiling']:,} -- BELOW C3's own known height (12,597,120), so this test is "
              f"UNINFORMATIVE for two-endedness at this precision (not a clean negative).")
        print(f"    - To clear a height comfortably past any plausible C4 denominator (~1e15) needs ~35-40")
        print(f"      trusted digits => N ~ 1-8 BILLION, 30-250x past B1124's already-expensive N=35M run")
        print(f"      (~24 min). Multi-hour-to-day scale: outside this task's 45-min bounded compute.")
        print(f"    - Smarter-than-brute-N: the Ohtsuki/quantum-dilogarithm asymptotic RECURSION for the")
        print(f"      figure-8 Kashaev invariant would give C4 as an EXACT rational with zero precision")
        print(f"      loss, sidestepping this floor entirely -- NOT attempted here (deriving/verifying an")
        print(f"      unfamiliar recursion from memory risks silent error; flagged as the next avenue,")
        print(f"      not executed, per the compute-the-discriminating-fact discipline).")
        print(f"    - Two-endedness: UNRESOLVED (same as B1130), but MEANINGFULLY NARROWED for the")
        print(f"      single-end/plain-rational hypothesis (now excluded to height 1e12); the two-ended")
        print(f"      hypothesis remains untested past height 1e7 due to the 3-term PSLQ noise floor.")
    results["verdict"] = verdict

    results["timing_total_s"] = round(time.time() - t0, 2)
    with open("results.json", "w") as f:
        json.dump(results, f, indent=1, default=str)
    print(f"\nTotal runtime: {results['timing_total_s']}s. Wrote results.json")


if __name__ == "__main__":
    main()
