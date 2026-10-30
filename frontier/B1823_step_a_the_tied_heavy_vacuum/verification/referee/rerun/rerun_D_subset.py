"""Rerun the draft's own section-D routine (one_config: 24 seeded starts, mpmath Newton, Hessian classes, free numbers) on a
subset, with the draft's seeds, and compare with the draft's step_a_v2.json."""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import step_a_v2 as S
orig = {(r["menu"], r["n"], r["mu2"], round(r["m02"], 10), r["lv"], r["tnorm"]): r
        for r in json.loads((HERE.parent.parent / "step_a_v2.json").read_text())["D"]["configs"]}
jobs = {(j[0], j[1], j[2], round(j[3], 10), j[4], j[7]): j for j in S.grid_D()}
want = [("Z", 2, 0.5, 0.005, 0.3, "N"), ("H", 2, 0.8, 0.008, 0.3, "N"), ("Z", 2, 0.3, 0.003, 0.3, "N"), ("Z", 4, 0.5, 0.005, 0.3, "N")]
out = []
for w in want:
    key = (w[0], w[1], w[2], round(w[3], 10), w[4], w[5])
    r = S.one_config(jobs[key]); o = orig[key]
    row = dict(config=list(key), tau=r["best"]["tau"], tau_draft=o["best"]["tau"], V=r["best"]["V"], V_draft=o["best"]["V"],
               isolated=r["best"]["isolated"], isolated_draft=o["best"]["isolated"], n_flat=r["best"]["n_flat"], n_flat_draft=o["best"]["n_flat"],
               free_rank=r.get("free_numbers", {}).get("rank"), free_rank_draft=o.get("free_numbers", {}).get("rank"))
    out.append(row); print(json.dumps(row), flush=True)
(HERE / "rerun_D_subset.json").write_text(json.dumps(out, indent=1))
