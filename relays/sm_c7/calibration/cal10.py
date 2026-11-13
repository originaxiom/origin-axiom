# calibration C10 (steps 3-4, outside the population): B1656's c_s(tau, ubar) against 2 K_c(tau), K_c = -2 pi log|g_Jc|,
# with Jc = the real coordinates of ubar shifted by the channel's half-period; the difference h should be tau-only
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np, sm_c7_lib as L, b1656_kernel as B
from fractions import Fraction as Fr
HALF = {"1": (0.0, 0.0), "i": (0.0, 0.5), "j": (0.5, 0.0), "k": (0.5, 0.5)}
def cs_all(t, p1, p2):
    w = B.line_w(p1, p2, t); x, y = B.sector_twists(w, t, 1, 0); R = B.residues(x, y, t); return B.cA(x, y, t, R)
def twoK(t, a1, a2, s):
    h = HALF[s]; a = (a1 + h[0], a2 + h[1]); c = (a[1], -a[0])     # Jc = a
    return 2 * L.kron(c, t)
random.seed(7)
for t in [0.21 + 1.13j, -0.37 + 0.92j, 0.05 + 1.6j, 0.44 + 0.71j]:
    rows = []
    for _ in range(3):
        p1, p2 = random.uniform(0.05, 0.45), random.uniform(0.05, 0.95)
        c = cs_all(t, p1, p2); a1, a2 = p1, -p2
        rows.append({s: c[s] - twoK(t, a1, a2, s) for s in c if c[s] is not None})
    print("tau", t)
    for s in "1ijk":
        v = [r[s] for r in rows if s in r]
        print("   channel %s  h = c_s - 2K:" % s, " ".join("%.9f" % x for x in v), "  spread %.1e" % (max(v) - min(v)))
