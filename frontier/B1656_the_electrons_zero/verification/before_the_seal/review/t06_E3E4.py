# E3/E4 logic over the 18 lines (the author already saw these D values in twisted_D_lines_output.txt)
import numpy as np, math, sys, time, warnings, json
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","D_of","np"): globals()[k] = ns[k]
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
t0 = time.time(); rec = []; perp_spread = 0.0; gaps = []; split = 0.0; worst = {}
for (p1, p2) in LINES18:
    w = line_w(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
        perp = [c[s] for s in "ijk"]; ps = max(perp) - min(perp); perp_spread = max(perp_spread, ps)
        cp = sum(perp)/3; D = D_of(c, R)
        if c["1"] is not None:
            gaps.append(c["1"] - cp); sp = abs(D - (c["1"] - cp)*R["1"]**2)/nR2(R); split = max(split, sp)
        rec.append({"line": [p1, p2], "sector": sec, "R1_rel": abs(R["1"])/math.sqrt(nR2(R)), "D_rel": abs(D)/nR2(R), "perp_spread": ps, "absR": math.sqrt(nR2(R))})
print("perp_spread_max %.3e (thr 1e-10)" % perp_spread, "gap minmax", min(gaps), max(gaps), "gap spread %.3e (thr 1e-9)" % (max(gaps)-min(gaps)), "split %.3e (thr 1e-10)" % split)
lep = [r for r in rec if r["sector"] == "lep"]; qk = [r for r in rec if r["sector"] != "lep"]
print("lep R1_rel max %.3e (thr 1e-12)" % max(r["R1_rel"] for r in lep), "lep D_rel max %.3e (thr 1e-10)" % max(r["D_rel"] for r in lep))
print("quark R1_rel min %.4f (thr .1)" % min(r["R1_rel"] for r in qk), "quark D_rel min %.4f (thr .5)" % min(r["D_rel"] for r in qk), sorted({round(r["D_rel"], 6) for r in qk}))
print("|R| range", min(r["absR"] for r in rec), max(r["absR"] for r in rec))
print("time %.1f" % (time.time() - t0))
json.dump(rec, open("t06_rec.json", "w"))
