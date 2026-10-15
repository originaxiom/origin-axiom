# function-level check: |K_s(omega z)|^2 vs |K_s'(z)|^2 on a W59 line, all three sectors, random z (reduced into/outside P)
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("pairs","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","np"): globals()[k] = ns[k]
rng = np.random.default_rng(7)
z = 0.4*(rng.normal(size=12) + 1j*rng.normal(size=12))
def Ksq(x, y, t, R, zz):
    P = pairs(x, y, zz, t); return {s: np.abs(P[s]/R[s])**2 for s in UNITS if abs(R[s]) > 1e-12}
for (p1, p2) in [(2/9, 5/9), (1/9, 7/9), (8/9, 8/9)]:
    w = line_w(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM)
        A = Ksq(x, y, OM, R, OM*z); B = Ksq(x, y, OM, R, z)
        res = {}
        for s in A:
            # which target s' makes |K_s(omega z)|^2 == |K_s'(z)|^2 ?
            best = min(B, key=lambda sp: np.max(np.abs(A[s] - B[sp])/np.abs(B[sp])))
            res[s] = (best, "%.1e" % np.max(np.abs(A[s] - B[best])/np.abs(B[best])))
        print((round(p1,3), round(p2,3)), sec, res)
# generic tau: the same test should fail
w = line_w(2/9, 5/9, GEN)
x, y = sector_twists(w, GEN, SIXY["Q"], SIXY["u"]); R = residues(x, y, GEN)
