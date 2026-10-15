# the instrument's cB at small n, on a case NOT among E2's three (line (2/9,5/9), tau = OM, sector down), vs route A with eps=1e-6
import numpy as np, math, sys, time
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","cB","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","mp"): globals()[k] = ns[k]
p1, p2 = 2/9, 5/9; t = OM; sec = "down"
w = line_w(p1, p2, t); fl, fr = SECTORS[sec]; x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
ca = cA(x, y, t, R, eps=1e-6)
print("route A eps=1e-6:", ca)
for n in (6, 8, 12):
    t0 = time.time()
    out = {s: cB(x, y, t, s, R[s], n=n) for s in ("i",)}
    print("n =", n, {s: (out[s], abs(out[s] - ca[s])) for s in out}, "%.1fs" % (time.time() - t0))
