import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","line_w","OM","UNITS","nR2","D_of","np"): globals()[k] = ns[k]
for (p1, p2) in [(1/9, 1/9), (2/9, 5/9)]:
    w = line_w(p1, p2, OM)
    x, y = sector_twists(w, OM, -3, 0); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
    print((round(p1,3), round(p2,3)), "(L, nu^c) = (-3, 0): |R1|/|R| = %.3f, |D|/|R|^2 = %.4f, c =" % (abs(R['1'])/math.sqrt(nR2(R)), abs(D_of(c, R))/nR2(R)), {s: (None if c[s] is None else round(c[s], 4)) for s in UNITS})
