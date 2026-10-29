"""rf6b: as rf6, with the flat regulator transformed: under w -> w/(c tau + d) lengths scale by 1/|c tau + d|, so
L' = L + s log|c tau + d| (s = +1 or -1 tried).  Elements S and the order-3 g3 = [[1,-1],[1,0]] (whose two candidate line
conventions differ) at a generic tau0.  At a fixed point |c tau + d| = 1, so no shift arises there."""
import math
import numpy as np
from rf_common import *
def spec(tau, p, L, q):
    a = direction("DR", tau); s = np.linalg.svd(Ymat(a, tau, p, q[0], q[1], L), compute_uv=False); return s / s[0]
def act(g, tau): a, b, c, d = g; return (a * tau + b) / (c * tau + d)
tau0 = complex(0.23, 1.17); p = (0.1, 0.3); L = 2.5
for nm, g in (("S", (0, -1, 1, 0)), ("g3", (1, -1, 1, 0))):
    a, b, c, d = g; t1 = act(g, tau0); lg = math.log(abs(c * tau0 + d))
    pw = tuple(np.linalg.solve(np.array([[a, -c], [-b, d]], float), np.array(p, float)))
    pt = tuple(np.array([[a, c], [b, d]], float) @ np.array(p, float))
    for lab, pp in (("w/(c tau+d)", pw), ("transpose", pt)):
        for s in (+1, -1):
            dm = max(np.max(abs(spec(tau0, p, L, q) - spec(t1, pp, L + s * lg, q))) for q in ((1, -4), (1, 2), (-3, 6)))
            print("%-3s p'=(%.4f, %.4f) %-12s L' = L %+d log|c tau0 + d| (%.4f): max diff over sectors %.1e" % (nm, pp[0] % 1, pp[1] % 1, lab, s, lg, dm))
