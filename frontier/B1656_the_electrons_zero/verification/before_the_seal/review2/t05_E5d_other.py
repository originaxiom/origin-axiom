# Review 2, check 3: E5(d)'s pair (-2, 5) on the 15 W59 lines that are NOT in MIX3 (exact copy of the cell's body, other lines).
import numpy as np, math, sys, time
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","D_of","twist_of"): globals()[k] = ns[k]
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
MIX3 = [LINES18[0], LINES18[4], LINES18[13]]
others = [l for l in LINES18 if l not in MIX3]
print("MIX3 =", [tuple(round(9*v, 6) for v in l) for l in MIX3], "(in ninths);  others:", len(others))
def wpt(x, t): return x[0]*t + x[1]/2
res = []
t0 = time.time()
for (p1, p2) in others:
    w = line_w(p1, p2, OM); x, y = sector_twists(w, OM, -2, 5); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
    perp = [c[s] for s in "ijk"]
    ub = wpt(x, OM) + wpt(y, OM); de = wpt(x, OM) - wpt(y, OM)
    ok_ub = abs(ub - 3*w) < 1e-12; ok_de = abs(de - (-7*w)) < 1e-12
    rec = (abs(D_of(c, R))/nR2(R), max(perp) - min(perp), abs(R["1"])/math.sqrt(nR2(R)))
    res.append(rec)
    print((round(9*p1), round(9*p2)), "D/|R|^2 %.4f  perp spread %.2e  |R1|/|R| %.4f  ubar=3w:%s delta=-7w:%s  gap %.6f  [%.0fs]" % (rec[0], rec[1], rec[2], ok_ub, ok_de, c["1"] - sum(perp)/3, time.time()-t0), flush=True)
print("min D/|R|^2 = %.4f (thr 0.5) ; max perp spread = %.2e (thr 1e-10) ; min |R1|/|R| = %.4f (thr 0.1)" % (min(r[0] for r in res), max(r[1] for r in res), min(r[2] for r in res)))
