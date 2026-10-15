import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("pairs","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","np"): globals()[k] = ns[k]
rng = np.random.default_rng(3)
z = 0.3*(rng.normal(size=10) + 1j*rng.normal(size=10))
worst = 0
for t in (OM, GEN, -0.17+0.95j):
    for (p1, p2) in [(2/9, 5/9), (1/9, 2/9), (0.137, 0.291)]:
        w = line_w(p1, p2, t)
        for sec, (fl, fr) in SECTORS.items():
            x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
            P0 = pairs(x, y, z, t); P1 = pairs(x, y, z + 1, t); Pt = pairs(x, y, z + t, t)
            for s in UNITS:
                if abs(R[s]) < 1e-12: continue
                e1 = np.max(np.abs(np.abs(P1[s]) - np.abs(P0[s]))/np.abs(P0[s])); e2 = np.max(np.abs(np.abs(Pt[s]) - np.abs(P0[s]))/np.abs(P0[s]))
                worst = max(worst, e1, e2)
print("max relative violation of |P_s(z+1)|=|P_s(z)|, |P_s(z+tau)|=|P_s(z)| :", worst)
