import numpy as np, math, sys, time
sys.path.insert(0, ".")
from load_inst import load
from cbfast import cB_np
ns = load()
for k in ("cA","cB","pairs","rmax_np","vangles","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","mp"): globals()[k] = ns[k]
def case(p1, p2, t, sec, n_list, chans=("i","1")):
    w = line_w(p1, p2, t); fl, fr = SECTORS[sec]; x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
    ca = cA(x, y, t, R, eps=1e-6, nth=96, ns=64)
    for s in chans:
        if ca[s] is None: continue
        row = []
        for n in n_list:
            v, _ = cB_np(pairs, rmax_np, vangles, x, y, t, s, R[s], n=n)
            row.append("n=%d: %.2e" % (n, abs(v - ca[s])))
        print((round(p1, 3), round(p2, 3)), "tau=", t, sec, s, " | ".join(row))
# 1) replicate cB (mp) at n=8,12 vs the numpy replica on the same case as t03 -> same errors?
case(2/9, 5/9, OM, "down", [6, 8, 12, 16, 24, 32, 40, 48], chans=("i", "1"))
