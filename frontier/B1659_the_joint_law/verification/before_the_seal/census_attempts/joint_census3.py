"""EXPLORATION (P-168; data SEEN — a scoreboard). The inverse map by GLOBAL search: differential evolution over the Higgs in
the chart S = [[1, a], [b, c]] (a, b, c complex in [-4, 4]^2; ratios are scale-free) and log L in [log 3, log 3e3],
two seeds, polished; per line the minimum chi2 (5% floor) and its residuals. Mode 'plant': targets made by the model at
the data fit's own best point (data-like hierarchy) must be recovered (chi2 -> 0) by the same search."""
import json, math, pathlib, sys
import numpy as np
from scipy.optimize import differential_evolution
src = pathlib.Path(__file__).with_name("joint_census2.py").read_text(encoding="utf-8")
sys.argv = ["x", "5", "1"]
NS = {"__file__": str(pathlib.Path(__file__).with_name("joint_census2.py")), "__name__": "jc2"}
exec(compile(src.split("out = []")[0], "jc2", "exec"), NS)
svs, DATA, TGT = NS["svs"], NS["DATA"], NS["TGT"]
MODE = sys.argv_mode if hasattr(sys, "argv_mode") else None
import os; MODE = os.environ.get("MODE", "data"); SEEDS = (1, 2)
B = [(-4, 4)]*6 + [(math.log(3), math.log(3e3))]
def toS(x): return np.array([[1, x[0] + 1j*x[1]], [x[2] + 1j*x[3], x[4] + 1j*x[5]]]), math.exp(x[6])
KEYS = [(sec, k) for sec, k, _ in TGT]; SIG = {(sec, k): sg for sec, k, (mu, sg) in TGT}
def chi2(x, ln, mus):
    S, L = toS(x); q = svs(S, ln, L)
    return float(sum(((math.log(max(q[s][k]/q[s][0], 1e-300)) - mus[(s, k)])/SIG[(s, k)])**2 for s, k in KEYS))
def search(ln, mus):
    best = None
    for sd in SEEDS:
        r = differential_evolution(chi2, B, args=(ln, mus), seed=sd, popsize=40, maxiter=600, tol=1e-10, polish=True, updating="deferred", workers=1)
        if best is None or r.fun < best.fun: best = r
        yield sd, r
DMUS = {(sec, k): mu for sec, k, (mu, sg) in TGT}
out = []
lines = (sorted(DATA) if MODE == "data" else sorted(DATA)[::6])[:int(os.environ.get("LIMIT", "99"))]
prev = {}
if MODE == "plant":
    prev = {tuple(r["line"]): r for r in json.load(open(pathlib.Path(__file__).with_name("joint_census3_data.json")))}
for ln in lines:
    if MODE == "data":
        mus = DMUS
    else:   # plant: the model's own ratios at the data fit's best point
        x0 = np.array(prev[ln]["x"]); S, L = toS(x0); q = svs(S, ln, L)
        mus = {(s, k): math.log(q[s][k]/q[s][0]) for s, k in KEYS}
    res = list(search(ln, mus))
    vals = [r.fun for _, r in res]; b = min(res, key=lambda t: t[1].fun)[1]
    S, L = toS(b.x); q = svs(S, ln, L)
    rec = {"line": list(ln), "chi2_by_seed": vals, "chi2": b.fun, "x": b.x.tolist(), "L": L,
           "ratios": {s: [q[s][1]/q[s][0], q[s][2]/q[s][0]] for s in ("up", "down", "lep")},
           "planted": {f"{s}{k}": math.exp(mus[(s, k)]) for s, k in KEYS} if MODE == "plant" else None}
    out.append(rec)
    print(f"[{MODE}] {ln[0]:.3f},{ln[1]:.3f}  chi2 by seed {np.round(vals, 3).tolist()}  L {L:.2f}  "
          + "  ".join(f"{s}:{q[s][1]/q[s][0]:.3e}/{q[s][2]/q[s][0]:.2e}" for s in ("up", "down", "lep")), flush=True)
json.dump(out, open(pathlib.Path(__file__).with_name(f"joint_census3_{MODE}.json"), "w"), indent=1, default=float)
