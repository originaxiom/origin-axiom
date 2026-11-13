#!/usr/bin/env python3
"""Post hoc, on SM-C6 E6's committed output (relays/sm_c6/e6_results.json); no new computation on the record's objects.
Two consequences of Poincare-Lefschetz duality with twisted coefficients and Euler characteristic zero, checked on every
sector module V = V(l, alpha) of the 24 levels, paired with its dual V* = V(l, beta^-1), beta^-1 = l - alpha:
  (a) on the filled (closed) manifold: h1(V) = h1(V*), because h0(V) = h0(V*) = 0 there;
  (b) on the cusped manifold: h1(V*) - h1(V) = h0(dM; V) - dim A_V, A_V the image of H1(M; V) in H1(dM; V).
      This file checks only the left side against the record's index I = n - n*; dim A_V is not computed here.
    python3 duality_check.py [e6_results.json] [out.json]"""
import sys, json, pathlib
from collections import Counter
HERE = pathlib.Path(__file__).resolve().parent
src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "sm_c6" / "e6_results.json"
out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "duality_check.json"
d = json.load(open(src))
N = {(l["state"], l["level"]): l["N"] for l in d["levels"]}
rows = {(r["state"], r["level"], tuple(r["l"]), tuple(r["alpha"])): r for r in d["rows"]}
pairs = a_ok = b_ok = exc = exc_a_ok = missing = 0
census = Counter()
for (st, lv, l, a), r in rows.items():
    n = N[(st, lv)]
    dual = rows.get((st, lv, l, tuple((x - y) % n for x, y in zip(l, a))))
    if dual is None:
        missing += 1
        continue
    pairs += 1
    a_ok += r["h1_filled"] == dual["h1_filled"]
    b_ok += (dual["h1_M"] - r["h1_M"]) == (r["n"] - r["nstar"])
    if r["h1_filled"] != r["n"] + r["nstar"]:
        exc += 1
        exc_a_ok += r["h1_filled"] == dual["h1_filled"]
    census["I=%+d h1(V)=%d h1(V*)=%d" % (r["n"] - r["nstar"], r["h1_M"], dual["h1_M"])] += 1
res = {"source": "relays/sm_c6/e6_results.json", "modules": len(rows), "paired_with_dual": pairs,
       "dual_missing": missing, "a_filled_h1_symmetric": a_ok, "b_h1_asymmetry_equals_I": b_ok,
       "E6_exceptions_h1_ne_n_plus_nstar": exc, "of_which_symmetric": exc_a_ok, "census": dict(sorted(census.items()))}
json.dump(res, open(out, "w"), indent=1)
print(json.dumps(res, indent=1))
