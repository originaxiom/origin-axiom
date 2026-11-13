"""P-783's scan: every R in [0.25, 3.40] in the four classes; each local minimum of the least singular value refined;
an eigenvalue is a minimum that falls to rounding and stays at the same R under a second height Y and a larger M."""
import json, math, sys, numpy as np
from scipy.optimize import minimize_scalar
sys.path.insert(0, "."); import hejhal_level5 as H
R0 = math.pi / (2 * math.log((1 + math.sqrt(5)) / 2))
grid = np.arange(0.25, 3.40, 0.004)
out = {"R0": R0, "classes": {}}
for par, ep in (("sin", -1), ("sin", 1), ("cos", -1), ("cos", 1)):
    s = np.array([H.least_singular(R, parity=par, eps=ep)[0] for R in grid])
    mins = [i for i in range(1, len(grid) - 1) if s[i] < s[i - 1] and s[i] < s[i + 1]]
    found = []
    for i in mins:
        r = minimize_scalar(lambda R: H.least_singular(R, parity=par, eps=ep)[0], bracket=(grid[i - 1], grid[i], grid[i + 1]), tol=1e-12)
        Rm, sm = r.x, r.fun
        s2 = H.least_singular(Rm, M=40, Y=0.10, Q=72, parity=par, eps=ep)[0]          # a second height, more terms
        second = H.least_singular(Rm, parity=par, eps=ep, k=2)[1]                      # the next singular value: simplicity
        found.append({"R": Rm, "least": sm, "least at Y=0.10, M=40": s2, "second least": second})
    eig = [f for f in found if f["least"] < 1e-8 and f["least at Y=0.10, M=40"] < 1e-8]
    out["classes"]["%s, Fricke %+d" % (par, ep)] = {"grid min": float(s.min()), "local minima": found, "eigenvalues R <= 3.40": eig}
    print("%s eps=%+d: %d local minima; eigenvalues: %s" % (par, ep, len(found), ["R=%.10f (least %.1e, at Y=0.10 %.1e, second %.1e)" % (f["R"], f["least"], f["least at Y=0.10, M=40"], f["second least"]) for f in eig]), flush=True)
json.dump(out, open("scan.json", "w"), indent=1, default=float)
