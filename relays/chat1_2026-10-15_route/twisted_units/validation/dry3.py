"""validation of the stage-2 instrument before the seal (excluded orders only); usage: python3 <this> <forms.pkl>"""
import sys, pickle, time, copy, random
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, D); sys.argv = ["x", sys.argv[1]]
import twisted_units_seal as TS
P = pickle.load(open(sys.argv[1], "rb"))
t0 = time.time()
c = TS.controls(P)
print("controls:", {k: {kk: (f"{vv:.1e}" if isinstance(vv, float) else vv) for kk, vv in v.items()} for k, v in c.items()}, round(time.time() - t0, 1), flush=True)
rec = TS.one_configuration_safe((0, 8, "LLLRLLLRLR", (1, 7), P))
good = [v for v in rec["cells"].values() if v and v["s"][0] > 1e-30 * v["s"][2]]
bad = [v for v in rec["cells"].values() if v and v["s"][0] <= 1e-30 * v["s"][2]]
print("error:", rec.get("error"), "cells", len(rec["cells"]), "rank-three", len(good), "rank-deficient", len(bad),
      "max r_calc rank-three", max(v["r_calc"] for v in good), round(time.time() - t0, 1), flush=True)
from collections import Counter
print("rank-deficient by assignment:", Counter(k.split("|")[0] for k, v in rec["cells"].items() if v and v["s"][0] <= 1e-30 * v["s"][2]).most_common(5))
