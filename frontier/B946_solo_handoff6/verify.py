#!/usr/bin/env python3
"""B946 -- verification of solo handoff 6, section LXXXII (the lambda-normalized
symmetric table), against THIS bench's independently computed B941 data.

Verify-don't-trust: solo's e_k(V) come from their own pipeline; B941's come from
the banked minimal polynomials on this bench. If the two agree exactly, the
convergence is real; if not, one of us is wrong and the arc says which.
"""
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
B941 = json.load(open(ROOT / "frontier/B941_branch_symmetric/results.json"))
e1, e2, e3 = [sp.Rational(x) for x in B941["symmetric_functions"]["V_hierarchy"]]

lam = sp.Rational(2304, 953)          # the tau-twisted gauge value (B916)
l4, l12 = lam**4, lam**12
R = {}

# --- RL2: the three lines of solo's table -----------------------------------
R["e1_over_l4"] = str(e1 / l4)
R["e2_over_l4"] = str(e2 / l4)
R["e3_over_l4"] = str(e3 / l4)
R["RL2_line1_matches"] = bool(sp.simplify(e1/l4 - sp.Rational(3*13*421493, 2**24)) == 0)
R["RL2_line2_matches"] = bool(sp.simplify(e2/l4 - sp.Rational(17*1129, 2**11)) == 0)
R["RL2_line3_matches"] = bool(sp.simplify(e3/l4 - 27) == 0)

# --- the degree grading: which primes survive at each degree ----------------
def odd_part(q):
    """prime support of a rational, with 2 and 3 and 953 removed."""
    f = {}
    for n in (sp.Rational(q).p, sp.Rational(q).q):
        for p, e in sp.factorint(n).items():
            if p not in (2, 3, 953):
                f[p] = f.get(p, 0) + e
    return sorted(f)
R["residual_primes_degree1"] = odd_part(e1/l4)
R["residual_primes_degree2"] = odd_part(e2/l4)
R["residual_primes_degree3"] = odd_part(e3/l4)
R["primes_thin_with_degree"] = (len(R["residual_primes_degree1"])
                                >= len(R["residual_primes_degree2"])
                                > len(R["residual_primes_degree3"]) == 0)

# --- lambda is FORCED by the clean norm, not assumed ------------------------
lam4_forced = e3 / 27
R["lambda4_forced_by_e3_over_27"] = str(lam4_forced)
R["lambda_forced"] = str(sp.root(lam4_forced, 4))
R["lambda_is_2304_over_953"] = bool(sp.simplify(sp.root(lam4_forced, 4) - lam) == 0)

# --- RL4: the discriminant, which solo flags as NOT 953-free ----------------
x = sp.symbols('x')
disc = sp.discriminant(sp.Poly(x**3 - e1*x**2 + e2*x - e3, x), x)
r = sp.nsimplify(disc / l12)
claim = sp.Rational(5**6 * 7**3 * 11 * 73**2 * 214189**2, 2**32 * 953**4)
R["RL4_disc_over_l12"] = str(r)
R["RL4_matches"] = bool(sp.simplify(r - claim) == 0)
R["RL4_num_factors"] = {str(k): int(v) for k, v in sp.factorint(sp.Rational(r).p).items()}
R["RL4_den_factors"] = {str(k): int(v) for k, v in sp.factorint(sp.Rational(r).q).items()}
R["RL4_is_953_free"] = "953" not in R["RL4_num_factors"] and "953" not in R["RL4_den_factors"]

# --- the tie back to B941's own headline ------------------------------------
R["b941_headline_numerator"] = 27 * 2304**4
R["equals_2p32_3p11"] = bool(27 * 2304**4 == 2**32 * 3**11)
R["e3_equals_27_lambda4"] = bool(sp.simplify(e3 - 27*l4) == 0)

# --- section 8's amendment, NOW COMPUTED (restored by B1054 / Review 1) ------
#
# THE DEFECT THIS REPAIRS, and it is the oldest instance of E39 found so far. `results.json` has
# carried four keys since B963 that THIS SCRIPT NEVER PRODUCED -- `frobenius_class_of_residue_
# primes`, the two `degreeN_pair_is_mixed_class` flags and `mixed_pair_base_rate_two_samples`.
# `tests/test_b946_handoff6.py` asserts over all four. They survived only because nobody re-ran
# the instrument: the lock was validating a CACHE that the script could not regenerate, so the
# first regeneration (B1054's corpus-wide freshness sweep) dropped the keys and the lock failed.
#
# The values were never wrong -- FINDINGS section 8 states the symbol outright, `(6237 | p)`, from
# B931/B937's sqrt-77 quadratic-resolvent class law -- and all six reproduce exactly. So the fix is
# to COMPUTE them here rather than to restore them, which is the whole point of E39: a number a
# lock asserts must be one the instrument can produce.
#
# 6237 = 3^4 * 7 * 11 = 81 * 77, so (6237|p) == (77|p); the arc's own form is kept.
RESOLVENT = 6237
OBSERVER_PLACE = 953                      # B931: the twist's critical prime, the class anchor
_primes = (R["residual_primes_degree1"] + R["residual_primes_degree2"]
           + R["residual_primes_degree3"] + [OBSERVER_PLACE, 20417473])
R["frobenius_class_of_residue_primes"] = {
    str(p): int(sp.functions.combinatorial.numbers.jacobi_symbol(RESOLVENT, p))
    for p in dict.fromkeys(_primes)}


def _mixed(pair):
    """A degree's residue is a MIXED pair when its two primes sit in different classes."""
    cls = R["frobenius_class_of_residue_primes"]
    return len(pair) == 2 and cls[str(pair[0])] != cls[str(pair[1])]


R["degree1_pair_is_mixed_class"] = _mixed(R["residual_primes_degree1"])
R["degree2_pair_is_mixed_class"] = _mixed(R["residual_primes_degree2"])
# Two independent coin flips are both mixed with probability (1/2)^2. Stated because two points
# is two points -- the arc's own words, "a pattern worth a prereg, not a law".
R["mixed_pair_base_rate_two_samples"] = 0.25

R["ALL_SOLO_CLAIMS_VERIFY"] = all([R["RL2_line1_matches"], R["RL2_line2_matches"],
                                   R["RL2_line3_matches"], R["RL4_matches"]])
print(json.dumps(R, indent=1))
pathlib.Path(__file__).resolve().parent.joinpath("results.json").write_text(
    json.dumps(R, indent=1) + "\n")
