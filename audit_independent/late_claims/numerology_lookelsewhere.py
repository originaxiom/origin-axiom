"""How cheap are agy's closed-form 'hits'? Enumerate formula families of the same complexity.

G   gauge: agy sets alpha_12^-1 = 21 Vol and ln(M12/MZ)/(2pi) = 2 Vol. Compute the actual SM 1-loop
    alpha_1 = alpha_2 crossing from PDG inputs and count how many (p/q) Vol with p,q <= 30 land as close.
P   Planck: M_Pl_red = r * M_Z * exp(k pi Vol). Count simple prefactors r (products of up to two
    'natural' constants incl. Vol, pi, phi, sqrt2, sqrt3, sqrt5, e, small rationals) and k in 1..8 hitting
    the reduced OR unreduced Planck mass to <= 0.194% (agy's quoted error).
D   Omega_DM/Omega_b = 5.3643 +- 1.2% (Planck 2018: 0.1200+-0.0012 / 0.02237+-0.00015). Count expressions
    n + x, n*x, n/x (n = 1..9, x from the same constant set) within agy's 0.33% and within 1 sigma.
"""
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction

VOL = 2.0298832128193072
PHI = (1 + 5 ** 0.5) / 2
MZ = 91.1876
OUT = {}

# ---------- G ----------
aem, s2w = 127.951, 0.23122
a1 = 0.6 * aem * (1 - s2w); a2 = aem * s2w
b1, b2 = 41 / 10, -19 / 6
t12 = (a1 - a2) / (b1 - b2); a12 = a1 - b1 * t12
OUT["G_true_sm_1loop_crossing"] = {"t12": t12, "alpha12_inv": a12, "agy_2Vol": 2 * VOL, "agy_21Vol": 21 * VOL,
                                   "rel_err_t12": 2 * VOL / t12 - 1, "rel_err_a12": 21 * VOL / a12 - 1}
fr = sorted({Fraction(p, q) for p in range(1, 61) for q in range(1, 31)})
def best_frac(target):
    vals = [(abs(float(f) * VOL / target - 1), f) for f in fr]
    vals.sort()
    return vals
for nm, tgt, agy in [("t12", t12, 2 * VOL), ("alpha12_inv", a12, 21 * VOL)]:
    e_agy = abs(agy / tgt - 1)
    n_better = sum(1 for f in fr if abs(float(f) * VOL / tgt - 1) <= e_agy and f.denominator <= 3)
    OUT["G_" + nm] = {"agy_rel_err": e_agy,
                      "n_fractions_den<=3_as_good_or_better": n_better,
                      "best_den<=3": [(str(f), e) for e, f in best_frac(tgt) if f.denominator <= 3][:3],
                      "best_den<=30": [(str(f), e) for e, f in best_frac(tgt)][:3]}
# chance that integer*Vol lands within agy's error of an arbitrary number near alpha12 (spacing Vol):
OUT["G_chance_integer_multiple_within_err_of_a12"] = 2 * abs(21 * VOL - a12) / VOL
OUT["G_chance_halfinteger_multiple_within_err_of_t12"] = 2 * abs(2 * VOL - t12) / (VOL / 2)

# ---------- shared constant set ----------
base = {"1": 1.0, "Vol": VOL, "pi": math.pi, "phi": PHI, "sqrt2": 2 ** 0.5, "sqrt3": 3 ** 0.5, "sqrt5": 5 ** 0.5, "e": math.e,
        "2": 2.0, "3": 3.0, "4": 4.0, "5": 5.0, "6": 6.0, "7": 7.0, "8": 8.0}
singles = {}
for (n1, v1) in base.items():
    for s1 in (1, -1):
        singles[f"{n1}^{s1}"] = v1 ** s1
pairs = {}
items = list(singles.items())
for (n1, v1), (n2, v2) in itertools.combinations_with_replacement(items, 2):
    pairs[f"{n1}*{n2}"] = v1 * v2
consts = {**singles, **pairs}
uniq = {}
for k, v in consts.items():
    key = round(v, 12)
    if key not in uniq:
        uniq[key] = k
consts = {key: name for key, name in uniq.items()}  # value -> name
OUT["n_distinct_prefactors"] = len(consts)

# ---------- P ----------
MPL_RED = 2.43536e18; MPL = 1.220890e19
hits = []
for k in range(1, 9):
    for tgt_name, tgt in [("reduced", MPL_RED), ("unreduced", MPL)]:
        need = tgt / (MZ * math.exp(k * math.pi * VOL))
        for r, nm in consts.items():
            if abs(r / need - 1) <= 0.00194:
                hits.append((k, tgt_name, nm, r / need - 1))
OUT["P_planck_hits_within_0.194pct"] = {"n_hits": len(hits), "examples": hits[:15],
                                        "agy_formula": "k=6, reduced, Vol*pi^-1"}

# ---------- D ----------
target, sig = 0.1200 / 0.02237, (0.1200 / 0.02237) * math.hypot(0.0012 / 0.12, 0.00015 / 0.02237)
dh_033, dh_1s = [], []
for n in range(1, 10):
    for r, nm in consts.items():
        for form, val in ((f"{n}+{nm}", n + r), (f"{n}*{nm}", n * r), (f"{n}/{nm}", n / r)):
            if abs(val / target - 1) <= 0.0033:
                dh_033.append((form, val))
            if abs(val - target) <= sig:
                dh_1s.append(form)
OUT["D_omega_ratio"] = {"target": target, "sigma": sig, "rel_sigma": sig / target,
                        "n_forms_within_0.33pct": len(dh_033), "n_forms_within_1sigma": len(set(dh_1s)),
                        "examples_0.33pct": dh_033[:12]}
print(json.dumps(OUT, indent=1, default=str))
json.dump(OUT, open("numerology_results.json", "w"), indent=1, default=str)
