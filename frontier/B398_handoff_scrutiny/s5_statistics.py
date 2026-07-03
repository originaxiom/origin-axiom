"""B398 S5 -- the adversarial statistics gate (per the committed prereg).

Formula space: v = n/d, n and d products of <=3 factors from the registered pool,
d <= 1050, 0 < v < 1, reduced. Targets: 5 PMNS + 15 dimensionless SM observables at
experimental 1-sigma. Statistics: per-target hit densities; the probability of the
observed PMNS ensemble under honest independence structure (theta12 data-derived;
theta23 independent pattern; theta13 = theta12/DIVISOR with the divisor selected from
the pool's small elements; delta consequential -- NOT counted as independent)."""
import json, os
from fractions import Fraction as Fr
from itertools import combinations_with_replacement

POOL = [2,3,5,6,7,8,11,12,14,23,26,49,52,75,78,98,100,200]

def products(maxval):
    out = set(POOL) | {1}
    for a, b in combinations_with_replacement(POOL, 2):
        if a*b <= maxval: out.add(a*b)
    for a, b, c in combinations_with_replacement(POOL, 3):
        if a*b*c <= maxval: out.add(a*b*c)
    return sorted(out)

NUMS = products(1050)          # numerators (n < d <= 1050)
DENS = [d for d in products(1050) if d > 1]
space = set()
for d in DENS:
    for n in NUMS:
        if 0 < n < d:
            space.add(Fr(n, d))
space = sorted(space)
print(f"formula space: {len(space)} distinct reduced fractions in (0,1)")

# targets: (name, central, one sigma)
TARGETS = [
    ("pmns_s12", 0.307, 0.013), ("pmns_s23", 0.545, 0.023), ("pmns_s13", 0.0220, 0.0007),
    ("weinberg_MZ", 0.23122, 0.00004), ("alpha", 0.0072974, 0.0000001),
    ("alpha_s_MZ", 0.1179, 0.0009), ("ckm_lambda", 0.2250, 0.0007),
    ("ckm_A", 0.826, 0.012), ("ckm_rhobar", 0.159, 0.010), ("ckm_etabar", 0.348, 0.010),
    ("mmu_mtau", 0.05946, 0.00005), ("me_mmu", 0.004836, 0.000001),
    ("mc_mt", 0.0074, 0.0004), ("ms_mb", 0.022, 0.002), ("mu_md", 0.47, 0.06),
    ("mb_mt", 0.0243, 0.0005), ("mtau_mt", 0.01027, 0.00005),
    ("md_ms", 0.050, 0.004), ("theta_c_sin2", 0.0506, 0.0003), ("jcp_ckm_e5", 0.3, 0.01),
]
import bisect
vals = [float(v) for v in space]
def hits(center, sigma):
    lo, hi = center - sigma, center + sigma
    i = bisect.bisect_left(vals, lo); j = bisect.bisect_right(vals, hi)
    return j - i

report = {}
for name, c, s in TARGETS:
    h = hits(c, s)
    report[name] = dict(center=c, sigma=s, hits_1sigma=h)
    print(f"{name:16s} center {c:.6g} sigma {c and s:.2g}: {h} formula hits within 1 sigma")

# the honest ensemble probability:
# - theta12: the 23/75 came from the data (F4 Gram) -- the relevant chance is that a
#   DATA-DERIVED ratio (one of the handful of natural Gram ratios in the banked spectra)
#   lands within 1 sigma of ANY of the 20 targets. Natural data ratios available:
DATA_RATIOS = [Fr(23,75), Fr(23,25), Fr(1,3), Fr(7,5)-Fr(1,1)+Fr(0,1)]  # bounded to (0,1): 23/75, 23/25, 5/7 reciprocal etc.
DATA_RATIOS = [Fr(23,75), Fr(23,25), Fr(5,7), Fr(1,2), Fr(1,4), Fr(3,8), Fr(23,200), Fr(75,200), Fr(69,200)]
n_data = len(DATA_RATIOS)
# per data-ratio: probability it lands in some target's 1-sigma window by chance =
# sum of window widths / the spread of plausible ratio range (0,1) -- conservative uniform.
width_sum = sum(2*s for _, c, s in TARGETS if 0 < c < 1)
p_one = min(1.0, width_sum)     # ~ probability a random value in (0,1) hits some window
import math
p_theta12_class = 1 - (1 - p_one)**n_data
# - theta23: an independent pattern-match from the space against ITS window:
p_theta23 = report["pmns_s23"]["hits_1sigma"] / len(space) * len(space) and (2*0.023)  # window fraction of (0,1)
p_theta23 = min(1.0, report["pmns_s23"]["hits_1sigma"] and (report["pmns_s23"]["hits_1sigma"]/len(space)) * 1.0)
# cleaner: chance that at least one space element lies in the window is ~1 given density;
# the honest statistic: the FRACTION of space in the window = the prior of a random
# pool-formula matching. For a scanned search (~1550 formulas per the handoff):
frac23 = report["pmns_s23"]["hits_1sigma"] / len(space)
p_scan_23 = 1 - (1 - frac23)**1550
# - theta13: theta12/k for k in the pool's small divisors (<=26): count how many k give a
#   1-sigma hit:
ks = [k for k in POOL if k <= 26]
hits13 = [k for k in ks if abs(23/75/k - 0.0220) <= 0.0007]
p_theta13_given12 = len(hits13) / len(ks) if ks else 0
report["_ensemble"] = dict(
    space_size=len(space), window_sum=width_sum,
    p_data_ratio_hits_some_target=round(p_theta12_class, 4),
    frac_space_in_s23_window=round(frac23, 5),
    p_scan1550_hits_s23=round(p_scan_23, 4),
    theta13_divisor_hits=f"{len(hits13)}/{len(ks)}",
    p_theta13_given_theta12=round(p_theta13_given12, 3),
)
print(report["_ensemble"])
# combined (the three quasi-independent selections):
p_combined = p_theta12_class * p_scan_23 * max(p_theta13_given12, 1/len(ks))
report["_ensemble"]["p_combined_raw"] = p_combined
# trials correction: the coordinator could have reported any of ~C(20,3) target triples
# and several cascade orderings; multiply by the reporting freedom ~ C(20,3) is too harsh
# (the PMNS triple is a natural family); use family-level correction x (number of natural
# observable families ~ 5: PMNS angles, CKM params, mass ratios, gauge couplings, phases):
report["_ensemble"]["p_combined_family_corrected"] = min(1.0, p_combined * 5)
print("combined p (raw, family-corrected):", p_combined, report["_ensemble"]["p_combined_family_corrected"])
json.dump(report, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "s5_statistics.json"), "w"), indent=1)
print("DONE")
