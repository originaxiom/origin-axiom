#!/usr/bin/env python3
"""B1470 -- the completed t12835 run against B1418's banked rows and the sep16 lane's xB031 table (its x2_t12835.json, read
from the lane at 3205984b and kept here as xB031_x2_t12835.json)."""
import json, glob, pathlib, collections, sys
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]
mine = json.load(open(HERE / "t12835_complete.json"))["rows"]
b = json.load(open(next((ROOT / "frontier").glob("B1418_*")) / "verification" / "c2_modules_compact.json"))["t12835"]
x = json.load(open(HERE / "xB031_x2_t12835.json"))
key = lambda r: (str(r.get("locus")), r.get("m"), str(r.get("twist")))
M = {key(r): r for r in mine}; B = {key(r): r for r in b}; X = {key(r): r for r in x}
ran = [k for k, r in B.items() if r.get("status") == "RUN"]; notrun = [k for k, r in B.items() if str(r.get("status", "")).startswith("NOT RUN")]
out = dict(modules=len(mine), not_run=sum(1 for r in mine if str(r.get("status", "")).startswith("NOT RUN")),
           b1418_run=len(ran), b1418_not_run=len(notrun), agree_with_b1418_on_run=sum(1 for k in ran if str(B[k].get("I")) == str(M[k].get("I"))),
           xB031_rows=len(x), keys_overlap_xB031=len(set(M) & set(X)), agree_with_xB031=sum(1 for k in set(M) & set(X) if str(M[k].get("I")) == str(X[k].get("I"))),
           I_values=dict(collections.Counter(str(r.get("I")) for r in mine)), completion_I=dict(collections.Counter(str(M[k].get("I")) for k in notrun)),
           max_abs_I=max(abs(int(r.get("I", 0) or 0)) for r in mine), any_three=any(abs(int(r.get("I", 0) or 0)) == 3 for r in mine))
ok = out["not_run"] == 0 and out["agree_with_b1418_on_run"] == out["b1418_run"] == 3110 and out["agree_with_xB031"] == out["xB031_rows"] == 6435 and not out["any_three"] and out["max_abs_I"] == 2
out["verdict"] = "PASS" if ok else "FAIL"
json.dump(out, open(HERE / "compare.json", "w"), indent=1); print(json.dumps(out, indent=1)); print("VERDICT t12835-complete: %s" % out["verdict"]); sys.exit(0 if ok else 1)
