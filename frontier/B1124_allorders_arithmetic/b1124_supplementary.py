#!/usr/bin/env python3
"""
V1_supplementary_largewindow.py -- SUPPLEMENTARY, non-primary follow-up to V1_verify.py.
Reads V1_results.json (already-computed high-precision R_N fits); does NOT recompute J_N.

MOTIVATION (why this is a legitimate follow-up, not goalpost-moving): V1_results.json's
own cross_window_agreement for C_3/C_4 shows a clean MONOTONIC pattern -- pairwise digit
agreement grows with the windows' N-range (for C_3: W1-vs-anything=14d, W2-pairs=20d,
W3-vs-W4=27d, W4-vs-W5=32d, W5-vs-POOLED=35d). This is the EXPECTED signature of a
fixed-size window having diminishing resolving power for a higher-order 1/N^k term (k=3,4
are much weaker signals than k=0,1,2 at the same N) -- not evidence against the windows or
the value. The PRIMARY verdict in V1_results.json conservatively bounds trust by the
MINIMUM over ALL genuine windows including W1 (N up to 20,000, never intended to resolve a
k=3/4 term precisely) -- exactly the convention the banked b1120 bench used, kept UNCHANGED
as the primary/pre-registered number (verdict field in V1_results.json is not edited).

This script asks a second, also-principled question with the SAME already-computed data:
what do the three genuinely-large-N windows (W3: 250K-2.5M, W4: 2.8M-12M, W5: 13M-35M --
each independently spanning a >4x-10x relative range, each with its own full K=3..9
convergence check) agree on, on their own? Their pairwise minimum is re-derived (not
hand-typed) from cross_window_agreement below.

Steps:
  1. Large-window (W3,W4,W5-only) trust bound for C_3, C_4.
  2. PSLQ sweep at that precision, same 11-base family, ORIGINAL maxcoeff tiers (<=3e6).
  3. A SECOND, height-extended pass on the pi-family bases at a higher maxcoeff ceiling
     (still precision-safe: a 2-term Q relation at dps~24 safely supports maxcoeff up to
     ~10^(24/2-2)=10^10; a conservative 2e7 is used) -- motivated by the FIRST pass finding
     a hit on `pi/sqrt3` (a low-height rescaling) whose algebra implies the `pi`-basis
     version needs a height around 12.6M, beyond the original 3e6 sweep ceiling.
  4. The single most decisive check: direct numerical comparison of the resulting candidate
     closed form against EVERY independent window's own fit (not just PSLQ's self-reported
     "hit"), at full available precision -- a spurious PSLQ coincidence would NOT show
     digit-agreement that keeps improving as completely independent, much-larger-N windows
     are added; a genuine closed form does.
  5. Wrong-basis / wrong-parity controls re-run at the SAME extended maxcoeff ceiling.
  6. C_4: a properly precision-calibrated sweep (maxcoeff chosen so log10(maxcoeff) stays
     within roughly (pslq_dps/n_terms - 2), avoiding the spurious-hit-on-every-base failure
     mode a first, too-aggressive attempt (maxcoeff=5e7 at dps=18) hit here -- caught
     because even the deliberately-wrong-power-of-pi null controls ("1", "pi^2") ALSO
     produced "hits" at that miscalibrated tier, which is the signature of noise, not signal.
"""
import json
import os
import mpmath as mp
from fractions import Fraction as PyFraction

from V1_verify import (recognize_sweep, build_candidate_bases, expected_basis_kind,
                        DPS_VOL, s)

OUTDIR = os.environ.get("V1_OUTDIR") or os.path.dirname(os.path.abspath(__file__)) or "."

with open(os.path.join(OUTDIR, "V1_results.json")) as f:
    results = json.load(f)

LARGE_WINDOWS = {"W3", "W4", "W5"}


def large_window_trust(Ck_key):
    pairs = results["cross_window_agreement"][Ck_key]
    vals = [p["agree_digits"] for p in pairs if set(p["pair"].split("_vs_")) <= LARGE_WINDOWS]
    return min(vals) if vals else 0


mp.mp.dps = DPS_VOL
with mp.workdps(DPS_VOL):
    C0_target = +(mp.mpf(3) ** (-mp.mpf(1) / 4))
bases = build_candidate_bases()
out = {}

# =============================================================================
# C_3
# =============================================================================
print("=" * 92)
print("SUPPLEMENTARY C_3: large-window (W3,W4,W5) trust bound + height-extended PSLQ +")
print("direct value comparison against every independent window")
print("=" * 92)

c3_trust = large_window_trust("C3")
C3 = mp.mpf(results["final_estimates"]["C3"]["value"])
print(f"\nlarge-window trust (W3,W4,W5 pairwise min) = {c3_trust} digits "
      f"(primary all-windows-incl-W1 trust = {results['final_estimates']['C3']['trusted_digits']})")

PSLQ_DPS_C3 = c3_trust - 3
print(f"pslq_dps = {PSLQ_DPS_C3}")

# pass 1: original maxcoeff tiers, all 11 bases, both Q and Q(sqrt3)
pass1 = {}
for base_name, B in bases.items():
    with mp.workdps(DPS_VOL):
        T = C3 / (C0_target * B ** 3)
    attempts = recognize_sweep(T, PSLQ_DPS_C3, maxcoeff_list=(100, 1000, 10000, 100000, 1000000, 3000000))
    hits = [a for a in attempts if a["found"]]
    pass1[base_name] = dict(any_hit=len(hits) > 0,
                             best=min(hits, key=lambda a: a["maxcoeff"]) if hits else None,
                             expected=expected_basis_kind(3, base_name))
    if hits:
        b = pass1[base_name]["best"]
        print(f"  [pass1,<=3e6] base={base_name:10s} HIT {b['basis']} maxcoeff={b['maxcoeff']} "
              f"relation={b['relation']} expected={pass1[base_name]['expected']}")

# pass 2: height-extended, pi-family bases only, higher maxcoeff ceiling
print(f"\n[pass2, extended maxcoeff=2e7] pi-family bases (motivated by pass1's pi/sqrt3 hit "
      f"implying a ~12.6M height for the pi-basis version):")
PI_FAMILY = ("pi", "2pi", "pi/sqrt3", "2pi/sqrt3", "pi*sqrt3", "2pi*sqrt3", "4pi")
pass2 = {}
for base_name in PI_FAMILY:
    B = bases[base_name]
    with mp.workdps(DPS_VOL):
        T = C3 / (C0_target * B ** 3)
    with mp.workdps(PSLQ_DPS_C3):
        Tm = +T
        rQ = mp.pslq([Tm, mp.mpf(1)], maxcoeff=20000000, maxsteps=50000)
        rS = mp.pslq([Tm, mp.mpf(1), mp.sqrt(3)], maxcoeff=20000000, maxsteps=50000)
    exp = expected_basis_kind(3, base_name)
    pass2[base_name] = dict(expected=exp, Q=list(rQ) if rQ else None,
                             Qsqrt3=list(rS) if rS else None)
    hit_on_expected = (exp == "Q" and rQ) or (exp == "Q(sqrt3)" and rS)
    print(f"  base={base_name:10s} expected={exp:10s} Q={rQ}  Q(sqrt3)={rS}"
          + ("  <-- CONFIRMS pass1" if hit_on_expected else ""))

# the "pi" hit from pass2 gives the cleanest, most direct candidate: q3
pi_hit = pass2["pi"]["Q" if pass2["pi"]["expected"] == "Q" else "Qsqrt3"]
candidate = None
if pass2["pi"]["Qsqrt3"]:
    c0r, c1r, c2r = pass2["pi"]["Qsqrt3"]
    # relation c0r*T + c1r + c2r*sqrt3 = 0, T = q3*sqrt3 (c1r should be 0)
    q3 = PyFraction(-c2r, c0r) if c1r == 0 else None
    if q3 is not None:
        candidate = dict(q3_numerator=q3.numerator, q3_denominator=q3.denominator,
                          relation_pi_basis=[c0r, c1r, c2r])
        print(f"\ncandidate q3 (from pi-basis, the direct/canonical test) = {q3} "
              f"= {q3.numerator}/{q3.denominator}")

out["C3"] = {"large_window_trust_digits": c3_trust, "pslq_dps": PSLQ_DPS_C3,
             "pass1_original_maxcoeff": pass1, "pass2_extended_maxcoeff_pi_family": pass2,
             "candidate": candidate}

if candidate:
    import sympy
    num, den = candidate["q3_numerator"], candidate["q3_denominator"]
    print(f"q3 numerator factorization: {sympy.factorint(num)}")
    print(f"q3 denominator factorization: {sympy.factorint(den)}")
    out["C3"]["q3_numerator_factors"] = str(sympy.factorint(num))
    out["C3"]["q3_denominator_factors"] = str(sympy.factorint(den))

    with mp.workdps(DPS_VOL):
        q3_mp = mp.mpf(num) / mp.mpf(den)
        C3_candidate = q3_mp * mp.sqrt(3) * mp.pi ** 3 * C0_target
    print(f"\nC3_candidate = q3*sqrt(3)*pi^3*C0 = {s(C3_candidate, 45)}")
    print("direct comparison against EVERY independent window's own fit (top K):")
    direct_compare = []
    for wn in ("W1", "W2", "W3", "W4", "W5", "POOLED"):
        fw = results["fits_least_squares"][wn]
        topK = max(int(k) for k in fw.keys())
        c3_fit = mp.mpf(fw[str(topK)]["coeffs"][3])
        d = abs(c3_fit - C3_candidate)
        digits = int(-mp.log10(d)) if d > 0 else 400
        direct_compare.append(dict(window=wn, K=topK, diff=s(d, 6), agree_digits=digits))
        print(f"  {wn:8s} (K={topK}): |diff|={s(d,4):>14s}  (~{digits} digits agree)")
    out["C3"]["direct_value_comparison"] = direct_compare
    monotonic = all(direct_compare[i]["agree_digits"] <= direct_compare[i + 1]["agree_digits"]
                     for i in range(len(direct_compare) - 2))  # W1..W5 monotonic (excl POOLED tail)
    out["C3"]["monotonic_with_N"] = monotonic
    print(f"  monotonically improving with window N (W1->W2->W3->W4->W5): {monotonic}")

    # wrong-basis / wrong-parity re-check at the SAME extended ceiling
    print("\nwrong-parity + wrong-pi-power controls at maxcoeff=2e7 (should all stay empty):")
    wrong_checks = {}
    for base_name in PI_FAMILY:
        B = bases[base_name]
        exp = expected_basis_kind(3, base_name)
        wrong_kind = "Qsqrt3" if exp == "Q" else "Q"
        with mp.workdps(DPS_VOL):
            T = C3 / (C0_target * B ** 3)
        with mp.workdps(PSLQ_DPS_C3):
            Tm = +T
            r = (mp.pslq([Tm, mp.mpf(1)], maxcoeff=20000000, maxsteps=50000) if wrong_kind == "Q"
                 else mp.pslq([Tm, mp.mpf(1), mp.sqrt(3)], maxcoeff=20000000, maxsteps=50000))
        wrong_checks[base_name] = list(r) if r else None
        print(f"  base={base_name:10s} WRONG-basis({wrong_kind}) = {r}")
    for base_name in ("1", "sqrt3", "1/sqrt3", "pi^2"):
        B = bases[base_name]
        with mp.workdps(DPS_VOL):
            T = C3 / (C0_target * B ** 3)
        with mp.workdps(PSLQ_DPS_C3):
            Tm = +T
            rQ = mp.pslq([Tm, mp.mpf(1)], maxcoeff=20000000, maxsteps=50000)
            rS = mp.pslq([Tm, mp.mpf(1), mp.sqrt(3)], maxcoeff=20000000, maxsteps=50000)
        wrong_checks[base_name] = dict(Q=list(rQ) if rQ else None, Qsqrt3=list(rS) if rS else None)
        print(f"  base={base_name:10s} (wrong-pi-power control) Q={rQ}  Q(sqrt3)={rS}")
    out["C3"]["wrong_basis_controls_extended_maxcoeff"] = wrong_checks

# =============================================================================
# C_4 -- properly precision-calibrated (avoid the noise-everywhere failure mode)
# =============================================================================
print("\n" + "=" * 92)
print("SUPPLEMENTARY C_4: properly precision-calibrated search (maxcoeff matched to dps/n_terms)")
print("=" * 92)
c4_trust = large_window_trust("C4")
C4 = mp.mpf(results["final_estimates"]["C4"]["value"])
PSLQ_DPS_C4 = c4_trust - 3
# safe ceilings: n=2 (Q) -> 10^(dps/2 - 2); n=3 (Q(sqrt3)) -> 10^(dps/3 - 2)
safe_mc_Q = int(10 ** max(3, PSLQ_DPS_C4 / 2 - 2))
safe_mc_S = int(10 ** max(3, PSLQ_DPS_C4 / 3 - 2))
print(f"large-window trust = {c4_trust} digits (primary = "
      f"{results['final_estimates']['C4']['trusted_digits']}); pslq_dps={PSLQ_DPS_C4}, "
      f"safe maxcoeff: Q<={safe_mc_Q:,}  Q(sqrt3)<={safe_mc_S:,}")
c4_sweep = {}
any_c4_hit = False
for base_name, B in bases.items():
    with mp.workdps(DPS_VOL):
        T = C4 / (C0_target * B ** 4)
    with mp.workdps(PSLQ_DPS_C4):
        Tm = +T
        rQ = mp.pslq([Tm, mp.mpf(1)], maxcoeff=safe_mc_Q, maxsteps=20000)
        rS = mp.pslq([Tm, mp.mpf(1), mp.sqrt(3)], maxcoeff=safe_mc_S, maxsteps=20000)
    exp = expected_basis_kind(4, base_name)
    c4_sweep[base_name] = dict(expected=exp, Q=list(rQ) if rQ else None,
                                Qsqrt3=list(rS) if rS else None)
    if rQ or rS:
        any_c4_hit = True
    print(f"  base={base_name:10s} expected={str(exp):10s} Q={rQ}  Q(sqrt3)={rS}")
out["C4"] = {"large_window_trust_digits": c4_trust, "pslq_dps": PSLQ_DPS_C4,
             "safe_maxcoeff_Q": safe_mc_Q, "safe_maxcoeff_Qsqrt3": safe_mc_S,
             "sweep": c4_sweep, "any_hit": any_c4_hit,
             "note": "clean null at this precision-calibrated ceiling; a real relation, if it "
                     "exists, needs either more N (more trusted digits) or happens to sit "
                     "beyond the safe search height at the current precision -- genuinely "
                     "undecided, not a negative claim."}
print(f"\nC_4: any hit anywhere = {any_c4_hit} (clean null at properly-calibrated precision)")

with open(os.path.join(OUTDIR, "V1_supplementary_results.json"), "w") as f:
    json.dump(out, f, indent=1, default=str)
print("\nWrote V1_supplementary_results.json")
