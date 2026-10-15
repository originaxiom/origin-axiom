import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("pairs","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","np"): globals()[k] = ns[k]
def a0s(p, t, sec):
    w = line_w(p[0], p[1], t); fl, fr = SECTORS[sec]; x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
    u = 0.05*np.exp(2j*np.pi*np.arange(128)/128); P = pairs(x, y, u, t)
    return {s: abs(np.mean(P[s]/R[s] - 1/u)) for s in UNITS if abs(R[s]) > 1e-12}
for (p, t, sec) in [((1/9, 1/9), OM, "up"), ((1/9, 2/9), OM, "lep"), ((1/9, 1/9), GEN, "down")]:
    a = a0s(p, t, sec); print(p, sec, {s: round(v, 4) for s, v in a.items()}, " route-A eps=1e-5 bias pi*eps^2*|a0|^2 max = %.2e" % (math.pi*1e-10*max(v*v for v in a.values())))
