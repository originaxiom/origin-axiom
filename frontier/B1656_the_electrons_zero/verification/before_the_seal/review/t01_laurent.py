# Laurent coefficients a0, a1 of K_s = P_s/R_s at 0, per channel, per sector, on a W59 line other than the sealed (1/9,1/9)
import numpy as np, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
globals().update({k: ns[k] for k in ("pairs","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np")})
def laurent(x, y, t, R, rad=0.05, N=128):
    u = rad*np.exp(2j*np.pi*np.arange(N)/N); P = pairs(x, y, u, t); out = {}
    for s in UNITS:
        if abs(R[s]) < 1e-12: out[s] = None; continue
        K = P[s]/R[s]
        a0 = np.mean(K - 1/u); a1 = np.mean((K - 1/u - a0)/u); out[s] = (a0, a1)
    return out
for (p1, p2) in [(2/9, 5/9), (4/9, 4/9)]:
    w = line_w(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM)
        L = laurent(x, y, OM, R)
        print((p1, p2), sec, {s: (None if L[s] is None else (round(abs(L[s][0]), 5), round(abs(L[s][1]), 5))) for s in UNITS})
# generic tau
w = line_w(1/9, 1/9, GEN)
for sec, (fl, fr) in SECTORS.items():
    x, y = sector_twists(w, GEN, SIXY[fl], SIXY[fr]); R = residues(x, y, GEN)
    L = laurent(x, y, GEN, R)
    print("GEN", sec, {s: (None if L[s] is None else (round(abs(L[s][0]), 5), round(abs(L[s][1]), 5))) for s in UNITS})
