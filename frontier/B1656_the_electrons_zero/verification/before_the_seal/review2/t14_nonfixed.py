# Review 2: verify the numbers quoted in the prereg's section 0b for the exploration (non-fixed lines, fictitious charges) with the revised cA
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","line_w","OM","GEN","UNITS","nR2","D_of","np"): globals()[k] = ns[k]
def row(p1, p2, ql, qr, t=OM):
    w = line_w(p1, p2, t); x, y = sector_twists(w, t, ql, qr); R = residues(x, y, t); c = cA(x, y, t, R, nth=64, ns=48)
    return abs(D_of(c, R))/nR2(R), abs(R["1"])/math.sqrt(nR2(R)), {s: (None if c[s] is None else round(c[s], 3)) for s in UNITS}
for (p1, p2) in [(1/9, 2/9), (1/9, 0.0), (2/9, 1/9)]:
    print("lep, line", (round(9*p1), round(9*p2)), "->", row(p1, p2, -3, 6))
print("fictitious (-3,5) on (1/9,1/9):", row(1/9, 1/9, -3, 5))
print("true leptons on (1/9,1/9):", row(1/9, 1/9, -3, 6)[:2])
print("nu pair (-3,0) on (1/9,1/9):", row(1/9, 1/9, -3, 0)[:2])
