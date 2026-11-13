import json, math, sys, numpy as np
sys.path.insert(0, "."); import hejhal_level5 as H
A = dict(M=40, Y=0.10, Q=72); B = dict(M=34, Y=0.12, Q=60)
out = {}
for par, ep in (("sin", -1), ("sin", 1), ("cos", -1), ("cos", 1)):
    grid = np.arange(0.02, 0.26, 0.002)
    sa = np.array([H.least_singular(R, parity=par, eps=ep, **A)[0] for R in grid])
    sb = np.array([H.least_singular(R, parity=par, eps=ep, **B)[0] for R in grid])
    both = np.maximum(sa, sb)
    out["%s, Fricke %+d" % (par, ep)] = {"least of max over both heights": float(both.min()), "at R": float(grid[both.argmin()])}
    print(par, ep, "R in [0.02, 0.26]: the smallest value both heights share is %.2e at R = %.3f" % (both.min(), grid[both.argmin()]), flush=True)
json.dump(out, open("scan3.json", "w"), indent=1)
