"""P-783, the second pass: detection at Y = 0.10 (M = 40, Q = 72) over [0.25, 3.40], confirmed at Y = 0.12; and the positive
control in the mirror-even classes: the dihedral form at R = pi/ln(phi) = 2 R0, with no sign of the norm in its character."""
import json, math, sys, numpy as np
from scipy.optimize import minimize_scalar
sys.path.insert(0, "."); import hejhal_level5 as H
R0 = math.pi / (2 * math.log((1 + math.sqrt(5)) / 2))
A = dict(M=40, Y=0.10, Q=72); B = dict(M=34, Y=0.12, Q=60)
def scan(lo, hi, step, par, ep):
    grid = np.arange(lo, hi, step)
    s = np.array([H.least_singular(R, parity=par, eps=ep, **A)[0] for R in grid])
    eig = []
    for i in range(1, len(grid) - 1):
        if s[i] < s[i - 1] and s[i] < s[i + 1]:
            r = minimize_scalar(lambda R: H.least_singular(R, parity=par, eps=ep, **A)[0], bracket=(grid[i - 1], grid[i], grid[i + 1]), tol=1e-12)
            sb = H.least_singular(r.x, parity=par, eps=ep, **B)[0]
            if r.fun < 1e-8 and sb < 1e-8:
                eig.append({"R": r.x, "least at Y=0.10": r.fun, "least at Y=0.12": sb, "second at Y=0.10": H.least_singular(r.x, parity=par, eps=ep, k=2, **A)[1]})
    return eig
out = {}
for par, ep in (("sin", -1), ("sin", 1), ("cos", -1), ("cos", 1)):
    e = scan(0.25, 3.40, 0.004, par, ep)
    out["%s, Fricke %+d, R in [0.25, 3.40]" % (par, ep)] = e
    print(par, ep, ["R=%.10f (%.1e, %.1e, second %.1e)" % (x["R"], x["least at Y=0.10"], x["least at Y=0.12"], x["second at Y=0.10"]) for x in e], flush=True)
for par, ep in (("cos", -1), ("cos", 1), ("sin", -1), ("sin", 1)):
    e = scan(2 * R0 - 0.06, 2 * R0 + 0.06, 0.003, par, ep)
    out["control near 2 R0 = %.6f: %s, Fricke %+d" % (2 * R0, par, ep)] = e
    print("control", par, ep, ["R=%.10f (%.1e, %.1e)" % (x["R"], x["least at Y=0.10"], x["least at Y=0.12"]) for x in e], flush=True)
json.dump(out, open("scan2.json", "w"), indent=1, default=float)
