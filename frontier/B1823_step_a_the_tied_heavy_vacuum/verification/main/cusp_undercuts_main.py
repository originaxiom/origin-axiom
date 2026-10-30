"""Main's check of the referee's cusp-convention undercuts (B2c): V at the referee's lower points (tau, S), from
t_runaway_stable.json, evaluated with the draft's own 34-digit model (MPModel, the stable F of rerun_stableF), against
the draft's reported interior minima in the same convention (menu, n, mu^2 = 0.5, m0^2 = 0.005, lambda v = 0.3,
cusp/cusp)."""
import sys, json, pathlib
H = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(H / "rerun_stableF"))
import mpmath as mp
import step_a_v2 as sa
from search import Model, make_copies
ref = json.loads((H.parents[0] / "referee" / "t_runaway_stable.json").read_text())["rows"]
out = []
for r in ref:
    if r["tnorm"] != "cusp" or r["n"] not in (4, 5):
        continue
    w = r["wide_starts"]; tau = complex(*w["best_tau"]); S = [complex(*z) for z in w["best_S"]]
    model = Model(make_copies(r["n"], r["menu"], "cusp", "cusp"), r["mu2"], r["m02"], r["lv"])
    v = sa.MPModel(model, tau, S).V([mp.mpf(0)] * 6)
    row = dict(menu=r["menu"], n=r["n"], reported_interior=r["V_reported"], referee_point_tau=w["best_tau"],
               V_at_referee_point_main=float(v), lower=bool(v < r["V_reported"] - 1e-9))
    out.append(row); print(row, flush=True)
(H / "cusp_undercuts_main.json").write_text(json.dumps(out, indent=1))
