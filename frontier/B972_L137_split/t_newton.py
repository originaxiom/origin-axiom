#!/usr/bin/env python3
"""B972 SCOUT -- is T's failure normalisation-invariant?

T's coefficients cannot be fully factored here (174-digit cofactor), so F(T) is
computed as a LOWER BOUND over the primes trial division does reach.  A lower
bound is enough: F >= 5 already implies no normalisation can satisfy
|P_lead| <= 2 and |P_const| <= 2, since every forced prime must land in one of
the two extremes and the two extremes hold at most 4 primes between them.
"""
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
d = json.load(open(ROOT / "frontier/B914_ratio_table/results.json"))
co = [abs(int(c)) for c in d["T_single"]["minpoly_desc_coeffs"]]   # d = 3,2,1,0
G = range(-40, 41)

known = sorted(set().union(*[set(int(p) for p in sp.factorint(c, limit=200000)
                                 if p < 200000) for c in co]))
R = {"primes_reached_by_trial_division": known}
rows, forced = {}, []
for p in known:
    v = [int(sp.multiplicity(p, c)) for c in co]
    states = set()
    for g in G:
        w = [v[0], v[1] + g, v[2] + 2 * g, v[3] + 3 * g]
        m = min(w)
        w = [t - m for t in w]
        states.add((w[0] > 0, any(t > 0 for t in w[1:3]), w[3] > 0))
    f = not any((not a) and (not c) for a, _, c in states)
    rows[p] = {"val_d3210": v, "forced_into_an_extreme": f}
    if f:
        forced.append(p)

R["per_prime"] = rows
R["F_lower_bound"] = len(forced)
R["forced_primes_found"] = forced
R["EXCEEDS_THE_4_PRIME_CAPACITY_OF_THE_TWO_EXTREMES"] = len(forced) > 4
R["conclusion"] = (
    "F(T) >= %d.  The B947 pattern needs |P_lead| <= 2 and |P_const| <= 2, i.e. at "
    "most 4 primes may be forced into the extremes.  %s"
    % (len(forced),
       "F(T) already exceeds 4, so NO rescaling of T satisfies the pattern -- T's "
       "failure is normalisation-invariant, exactly like mu's and kappa's."
       if len(forced) > 4 else
       "The bound does not yet decide satisfiability; only the banked-normalisation "
       "failure is established."))
print(json.dumps(R, indent=1))
pathlib.Path(__file__).resolve().parent.joinpath("t_newton_out.json").write_text(
    json.dumps(R, indent=1) + "\n")
