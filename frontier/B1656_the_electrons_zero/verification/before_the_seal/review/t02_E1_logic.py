# E1's logic (spread across eps = 1e-3,1e-4,1e-5 and the residue-2 control) on a line other than the sealed one
import numpy as np, math, sys, time
sys.path.insert(0, ".")
from load_inst import load
ns = load()
globals().update({k: ns[k] for k in ("cA","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np")})
t0 = time.time()
for (p1, p2), t, tn in [((2/9, 5/9), OM, "OM"), ((2/9, 5/9), GEN, "GEN")]:
    w = line_w(p1, p2, t)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
        cs = [cA(x, y, t, R, eps=e) for e in (1e-3, 1e-4, 1e-5)]
        c2 = [cA(x, y, t, R, eps=e, scale=2.0) for e in (1e-3, 1e-4)]
        for s in UNITS:
            if cs[0][s] is None: continue
            spread = max(c[s] for c in cs) - min(c[s] for c in cs)
            ctrl = (c2[1][s] - c2[0][s])/(6*np.pi*math.log(10))
            print(tn, sec, s, "c(1e-3,1e-4,1e-5) =", [round(c[s], 9) for c in cs], "spread %.3e" % spread, "control-1 %.3e" % (ctrl - 1))
print("time", time.time() - t0)
