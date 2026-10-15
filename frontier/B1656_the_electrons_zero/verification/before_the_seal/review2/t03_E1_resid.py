# Review 2, check 1c: what limits the corrected E1 spread?  predicted O(eps^4) term (pi/2)|a1|^2 eps^4 vs observed; quadrature convergence of cA.
import numpy as np, math, sys, time
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","a0_of","pairs"): globals()[k] = ns[k]
def a1_of(x, y, t, R, rad=0.05, N=128):
    u = rad*np.exp(2j*np.pi*np.arange(N)/N); P = pairs(x, y, u, t); out = {}
    for s in UNITS:
        if abs(R[s]) <= 1e-12: out[s] = None; continue
        K = P[s]/R[s]; a0 = np.mean(K - 1/u); out[s] = complex(np.mean((K - 1/u - a0)/u))
    return out
cases = [((2/9, 5/9), OM), ((0.137, 0.291), GEN), ((1/9, 4/9), 0.45+0.6j), ((7/9, 7/9), 0.2+0.55j)]
for (p1, p2), t in cases:
    w = line_w(p1, p2, t)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t); A1 = a1_of(x, y, t, R)
        c3 = cA(x, y, t, R, eps=1e-3); c5 = cA(x, y, t, R, eps=1e-5)
        cq = cA(x, y, t, R, eps=1e-5, nth=160, ns=120)
        for s in UNITS:
            if c3[s] is None: continue
            obs = c5[s] - c3[s]                           # = +(pi/2)|a1|^2 (eps3^4 - eps5^4) expected
            pred = (math.pi/2)*abs(A1[s])**2*(1e-3**4 - 1e-5**4)
            print((round(p1,3), round(p2,3)), np.round(t,3), sec, s, "|a1| %.3f" % abs(A1[s]), "obs c(1e-5)-c(1e-3) %.3e  pred %.3e   quad-conv |c(96,64)-c(160,120)| %.2e" % (obs, pred, abs(c5[s]-cq[s])))
