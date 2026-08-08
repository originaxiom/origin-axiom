#!/usr/bin/env python3
"""B972 SCOUT -- T (B914's colorless coupling invariant) against B947's statistic.

T is the programme's paradigm VALUE object: a normalisation-free, dimensionless,
branch-symmetric ratio -- "T is canonical" (B914 §1), banked in LAW_MAP as the
one-number table.  It was NOT among B947's seven.  Verify-don't-trust: the
banked 50-digit T is first checked to be a root of the banked cubic.
"""
import json
import pathlib
from decimal import Decimal, getcontext

import sympy as sp

getcontext().prec = 140
ROOT = pathlib.Path(__file__).resolve().parents[2]
d = json.load(open(ROOT / "frontier/B914_ratio_table/results.json"))
co = [int(c) for c in d["T_single"]["minpoly_desc_coeffs"]]
R = {}

R["banked_content_gcd"] = int(sp.igcd(*[abs(c) for c in co]))
R["banked_form_is_primitive"] = R["banked_content_gcd"] == 1
R["coeff_digit_sizes"] = [len(str(abs(c))) for c in co]

# --- gate: is the banked 50-digit T a root of the banked cubic? --------------
T = Decimal(d["T_single"]["value_50d"])
val = sum(Decimal(c) * T**k for c, k in zip(co, [3, 2, 1, 0]))
scale = max(abs(Decimal(c)) * abs(T)**k for c, k in zip(co, [3, 2, 1, 0]))
R["relative_residual_minpoly_at_T"] = str(abs(val) / scale)
R["T_IS_A_ROOT"] = (abs(val) / scale) < Decimal("1e-40")

# --- the leading coefficient -------------------------------------------------
L = abs(co[0])
found = {}
rest = L
for p in (179, 1759, 4889):
    m = sp.multiplicity(p, L)
    if m:
        found[p] = int(m)
    while rest % p == 0:
        rest //= p
R["lead_small_primes_found"] = found
R["lead_residual_digits"] = len(str(rest))
R["lead_residual_is_one"] = rest == 1
R["lead_support_lower_bound"] = len(found) + (0 if rest == 1 else 1)
R["P_lead_exceeds_2"] = R["lead_support_lower_bound"] > 2

# constant term, which DID fully split under trial division
C = abs(co[-1])
R["P_const"] = sorted(int(p) for p in sp.factorint(C))
R["P_const_size"] = len(R["P_const"])

R["B947_pattern_holds"] = False if R["P_lead_exceeds_2"] else None
R["VERDICT"] = ("T is a VALUE-layer family (B914: normalisation-free, canonical, "
                "banked in LAW_MAP as the one-number table) and it FAILS B947's "
                "pattern: |P_lead| >= %d > 2." % R["lead_support_lower_bound"])
R["note_computability"] = ("B947's statistic is not even COMPUTABLE for T without "
                           "factoring a %d-digit cofactor; the criterion is only "
                           "decidable on families whose coefficients happen to be "
                           "smooth." % R["lead_residual_digits"])

print(json.dumps(R, indent=1))
pathlib.Path(__file__).resolve().parent.joinpath("t_probe_out.json").write_text(
    json.dumps(R, indent=1) + "\n")
