import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","np"): globals()[k] = ns[k]
sp = []; ct = []
for (p1, p2), t in [((1/9, 1/9), OM), ((1/9, 1/9), GEN)]:
    w = line_w(p1, p2, t)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
        cs = [cA(x, y, t, R, eps=e) for e in (1e-6, 1e-7, 1e-8)]
        c2 = [cA(x, y, t, R, eps=e, scale=2.0) for e in (1e-6, 1e-7)]
        for s in UNITS:
            if cs[0][s] is None: continue
            sp.append(max(c[s] for c in cs) - min(c[s] for c in cs)); ct.append((c2[1][s] - c2[0][s])/(6*np.pi*math.log(10)) - 1)
print("fix A' (eps = 1e-6,1e-7,1e-8; control 1e-6,1e-7): spread max %.2e (thr 1e-9)  control max|v-1| %.2e (thr 1e-6)" % (max(sp), max(abs(v) for v in ct)))
