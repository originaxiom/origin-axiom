import sys, io, json, math, contextlib
from fractions import Fraction
import numpy as np
sys.path.insert(0, "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification")
sys.path.insert(0, "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification")
with contextlib.redirect_stdout(io.StringIO()):
    import compare, cm_zero_line as C
T9 = np.array(compare.arrays()["T9"], float)
tt = np.concatenate([T9, [math.log(3.12e-5)]]); tt[4] -= math.log(3); tt[5] += math.log(3)
sig = np.array(json.load(open("scripts/stepb/sigma/SIGMA_ONLY.json"))["sigma_natural_log"])
names = ["c/t","u/t","s/b","d/b","mu/tau","e/tau","|V_us|","|V_cb|","|V_ub|","|J|"]
line = (Fraction(3, 8), Fraction(3, 8))
def ev(x, y):
    res = []
    with contextlib.redirect_stdout(io.StringIO()):
        rows = C.rows_at(complex(x, y), line)
    for r in rows:
        if r["direction"] == C.DIRS[6]: continue
        a = [r["up"][1], r["up"][0], r["down"][1], r["down"][0], r["lepton"][1], r["lepton"][0], *r["V"], abs(r["J"])]
        if not r["V defined"] or min(a) <= 0: continue
        z = (np.log(a) - tt) / sig
        res.append((float((z**2).sum()), r["direction"], r["radius"], r["reading"], z.tolist()))
    return min(res, key=lambda t: t[0]) if res else None
x0, y0 = 0.093359375, 2.742578125
b = ev(x0, y0)
out = {"address": [x0, y0], "least": {"chi2_ten": b[0], "direction": b[1], "radius": b[2], "reading": b[3], "pulls": dict(zip(names, b[4]))}, "grid": []}
for dx in (-0.02, -0.01, 0, 0.01, 0.02):
    for dy in (-0.05, -0.025, 0, 0.025, 0.05):
        g = ev(x0 + dx, y0 + dy)
        out["grid"].append({"dx": dx, "dy": dy, "chi2_ten": g and g[0], "row": g and g[1:4]})
out["grid_min"] = min(g["chi2_ten"] for g in out["grid"] if g["chi2_ten"] is not None)
json.dump(out, open("frontier/B1825_step_b_the_nine_from_one_address/verification/referee/fresh_address.json", "w"), indent=1)
print(json.dumps(out["least"], indent=1), out["grid_min"])
