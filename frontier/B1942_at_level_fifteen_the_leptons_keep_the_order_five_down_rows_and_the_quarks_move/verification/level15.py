"""X-SURVIVAL's S3 on main's frame (exact weight, canonical end): at the points of exact order 15, the leptons' charges
(6Y = -3, 6) are divisible by 3, so their twists see only the order-5 part of the point; the down quarks' (1, 2) see all
of it. Expectations, written before the run: (E1) the lepton average over the 192 points of exact order 15 equals the
down average over the 24 points of order 5, to roundoff (the copy of B1934 moved down a level); (E2) the down average
over order 15 differs from the down average over order 5 well above roundoff; (E3) the up sector, whose charges (1, -4)
are not divisible by 3, also samples all of order 15. Prints differences only."""
import sys, pathlib, math
from fractions import Fraction as Fr
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
EB = next((ROOT / "frontier").glob("B1932_*")) / "verification"
sys.path.insert(0, str(EB)); sys.argv = ["x"]
import fiber_grid_t90 as G
C, CR = G.C, G.CR
def order(a, b, N):
    from math import gcd
    return N // gcd(gcd(a, b), N)
P5 = [(i / 5, j / 5) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
P15 = [(i / 15, j / 15) for i in range(15) for j in range(15) if order(i, j, 15) == 15]
assert len(P5) == 24 and len(P15) == 192
KS = ["down|L_2|S", "lep|L_2|S", "up|L_2|St", "down|L_2|St", "lep|L_2|St"]
def avg(t, pts):
    L = CR.canon(t); L.pop("_extrapolated"); G.L2_NOW[0] = L["L_2"]
    acc = None
    try:
        for a, b in pts:
            f = C.frame(t, a, b, L); v = np.concatenate([np.array(f[k]) for k in KS])
            acc = v / len(pts) if acc is None else acc + v / len(pts)
    finally:
        G.L2_NOW[0] = None       # [2026-11-18: the exact weight is switched off again; left on, it changed other arcs' frames in one process]
    return acc
B = C._modules()["B"]; B.cA = G.cA_t90
for t in (complex(0.13, 1.5), complex(-0.31, 2.4), complex(0.27, 3.6)):
    a5, a15 = avg(t, P5), avg(t, P15)
    d5, l5, u5, d5t, l5t = (a5[2*i:2*i+2] for i in range(5)); d15, l15, u15, d15t, l15t = (a15[2*i:2*i+2] for i in range(5))
    rel = lambda x, y: float(np.max(np.abs(x - y) / np.abs(y)))
    print("tau %s: E1 lepton(15) vs down(5): S %.1e, S~ %.1e | E2 down(15) vs down(5): S %.2e, S~ %.2e | E3 up(15) vs up(5) %.2e | lepton(15) vs down(15): %.2e"
          % (t, rel(l15, d5), rel(l15t, d5t), rel(d15, d5), rel(d15t, d5t), rel(u15, u5), rel(l15, d15)), flush=True)
