"""B615 addendum — the robustness (algebraic-mimic) ensemble, per design
section 4: 'a claimed signal must survive BOTH ensembles.' The verdict
was AMBIGUOUS (no claimed signal), but the packet for seat 4 is complete
only with this computed. Mechanical; no choices beyond the design's
declared mimic families ((a+b*sqrt5)/c, (a+b*sqrt2)/c, p/q with
|a|,|b|,|p|,|q|,|c| <= 50), filtered to (0,1]; 10^6 draws per family.

Question answered: under the mimic null, what is the expected number of
(value, target) matches for the G2 grid (25 values x 6 angle targets,
tier 1e-2), and how unusual is the observed count of 3?
"""
import math

import numpy as np

rng = np.random.default_rng(20260715)
N = 10 ** 6
s5, s2 = math.sqrt(5), math.sqrt(2)

T_M = {"sin^2th12": 0.307, "sin^2th23": 0.546, "sin^2th13": 0.0220,
       "lambda_C": 0.22501, "|Vcb|": 0.0408, "|Vub|": 0.00382}
DELTA = 1e-2

fams = {}
a = rng.integers(-50, 51, N); b = rng.integers(-50, 51, N)
c = rng.integers(1, 51, N)
fams["(a+b*sqrt5)/c"] = (a + b * s5) / c
a2 = rng.integers(-50, 51, N); b2 = rng.integers(-50, 51, N)
c2 = rng.integers(1, 51, N)
fams["(a+b*sqrt2)/c"] = (a2 + b2 * s2) / c2
p_ = rng.integers(-50, 51, N); q_ = rng.integers(1, 51, N)
fams["p/q"] = p_ / q_

print("the mimic ensemble (per family): P(a mimic value in (0,1] lands "
      f"in a target window, tier {DELTA}):", flush=True)
rates = {}
for fname, arr in fams.items():
    inunit = arr[(arr > 0) & (arr <= 1)]
    per_t = {}
    tot = 0.0
    for tn, t in T_M.items():
        r = np.mean(np.abs(inunit - t) / t <= DELTA)
        per_t[tn] = r
        tot += r
    rates[fname] = tot
    print(f"  {fname:>15s}: kept {len(inunit)} of {N}; "
          + "  ".join(f"{tn}:{per_t[tn]:.5f}" for tn in T_M)
          + f"  | expected pairs per value: {tot:.5f}", flush=True)

print("\nthe G2 comparison under the mimic null (25 object values):",
      flush=True)
for fname, tot in rates.items():
    exp_pairs = 25 * tot
    # binomial-ish tail for >= 3 pair-matches with per-value rate tot
    lam = exp_pairs
    p_ge3 = 1 - math.exp(-lam) * (1 + lam + lam ** 2 / 2)
    print(f"  mimic family {fname:>15s}: expected pairs = {exp_pairs:.2f}; "
          f"P(X >= 3) ~ {p_ge3:.4f} (Poisson)", flush=True)

print("\nROBUSTNESS READING (mechanical): the observed 3 coarse-tier "
      "angle matches sit at the quoted tail probabilities under each "
      "mimic family; algebraic numbers of matched complexity land in "
      "angle windows at the printed rates. No verdict change (AMBIGUOUS "
      "stands; the design's gate applies to MATCH claims only).",
      flush=True)
print("B615 ROBUSTNESS DONE", flush=True)
