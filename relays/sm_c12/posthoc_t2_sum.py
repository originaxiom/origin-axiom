#!/usr/bin/env python3
"""SM-C12 T2, post hoc and labelled: E-T2d (sum of eta_A over the non-trivial characters = 0) failed as sealed.  The
corrected cover argument: the characters' cover is T^2_M again, identified through M - I, whose determinant 2 - tr is
negative for tr > 2, so the cover carries the opposite orientation: sum over all characters of eta_chi = sgn(2 - tr) eta,
i.e. sum over the non-trivial ones = (sgn(2 - tr) - 1) eta.  Checked on every state of t2_results.json."""
import json, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
d = json.load(open(HERE / "t2_results.json"))
ok = 0; bad = []
for r in d["rows"]:
    tr = r["trace"]; e = Fr(r["eta"]); S = Fr(r["sum_eta_A"]); sg = 1 if 2 - tr > 0 else -1
    if S == (sg - 1) * e: ok += 1
    else: bad.append(r["state"])
out = {"states": len(d["rows"]), "holds": ok, "fails": bad}
json.dump(out, open(HERE / "t2_posthoc_sum.json", "w"), indent=1); print(json.dumps(out))
