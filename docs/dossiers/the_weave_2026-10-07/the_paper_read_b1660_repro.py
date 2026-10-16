# Scratch: reproduce B1660's best cell with main's own code (a reproduction, not an independent instrument).
import importlib.util, json, math, sys, time
from pathlib import Path
import numpy as np
R = Path(__file__).resolve().parents[1]
V = R / "frontier/B1660_the_one_higgs_census/verification"
spec = importlib.util.spec_from_file_location("b1660", V / "the_one_higgs_census.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
d = json.load(open(V / "the_one_higgs_census.json"))
cells = [(var, i, c) for var in ("same", "tilde", "bar") for i, c in enumerate(d["C2"]["census"][var])]
best = min(cells, key=lambda t: t[2]["chi2_min"]); var, li, rec = best
pair = [i for i, c in enumerate(d["C2"]["census"][var]) if abs(c["chi2_min"] - rec["chi2_min"]) < 1e-6]
print("stored best:", var, "lines", [M.LINES18[i] for i in pair], "chi2", rec["chi2_min"])
t0 = time.time()
# build PARTS for the needed lines only, as build() does
M.PARTS, M.CMIN = {}, {}
for i in pair:
    ln = M.LINES18[i]; w = M.line_w(*ln, M.OM); M.PARTS[ln] = {}
    for sec, (fl, fr) in M.SECTORS.items():
        x, y = M.sector_twists(w, M.OM, M.SIXY[fl], M.SIXY[fr]); Rr = M.residues(x, y, M.OM)
        c = M.cA(x, y, M.OM, Rr, nth=64, ns=48); ks = [k for k in M.UNITS if c[k] is not None]
        M.PARTS[ln][sec] = (np.array([c[k] for k in ks], dtype=float), np.array([Rr[k] * M.EDUAL[k] for k in ks]))
    M.CMIN[ln] = min(float(M.PARTS[ln][s][0].min()) for s in M.PARTS[ln])
print("built in %.0f s" % (time.time() - t0))
for i in pair:
    x = d["C2"]["census"][var][i]["x"]
    r = M.resid(x, var, M.LINES18[i], M.DMU)
    print("line", M.LINES18[i], "chi2 at the stored point:", float(np.sum(r ** 2)), "residuals", np.round(r, 3).tolist())
NEW = int(sys.argv[1]) if len(sys.argv) > 1 else 40
i = pair[0]
res = [M.fit((var, i, M.DMU, 7_000_000 + k)) for k in range(NEW)]
ok = sorted(r[0] for r in res if r[1] is not None)
print("fresh multistart (%d starts, seeds unlike main's) on line %s: best %.3f; below 11.07: %d; within 5%% of 34.40: %d"
      % (NEW, M.LINES18[i], ok[0], sum(v < 11.07 for v in ok), sum(v <= rec["chi2_min"] * 1.05 for v in ok)))
print("total %.0f s" % (time.time() - t0))
