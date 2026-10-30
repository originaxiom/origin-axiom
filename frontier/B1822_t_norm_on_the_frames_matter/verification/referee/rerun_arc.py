#!/usr/bin/env python3
"""Referee rerun of B1822's own instrument, from a byte-identical copy (tnorm_copy.py), on six twist classes.
Compares every number gram_job writes with the arc's stored tnorm_results.json (read-only). Data-free.
    OMP_NUM_THREADS=1 nice -n 10 python3 -I rerun_arc.py"""
import json, pathlib, sys, time
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tnorm_copy as T

ARC = HERE.parent / "B1822_t_norm_on_the_frames_matter" / "verification" / "tnorm_results.json"
R = json.loads(ARC.read_text()); G = R["G_results"]; M = R["G_config_to_class"]
WANT = ["Q|zero|1j", "e|2/5,3/10|(0.35+2.75j)", "u|ord7 2/7,3/7|(0.85+3.45j)", "L|ord12 5/12,1/12|(0.3+6j)",
        "d|ord9 1/9,1/9|(0.05+2.05j)", "Q|ord4 0,1/4|(0.3+6j)"]
out = {"rows": []}
worst = 0.0
rng = np.random.default_rng(7)
for w in WANT:
    g = G[M[w]]
    a, b = Fr(g["a"]), Fr(g["b"]); tau = complex(*g["tau"])
    t0 = time.time()
    mine = T.gram_job((g["key"], a, b, tau))
    st, P1, Pt, chi = T.structure(a, b, tau, rng)
    row = {"config": w, "class": g["key"], "a": g["a"], "b": g["b"], "tau": g["tau"], "seconds": round(time.time() - t0, 1)}
    # compare every stored scalar
    diffs = {}
    for blk in ("cover", "cell_P0", "cell_Phalf", "cell_P0+1", "cell_P0+tau", "polar_P0"):
        for k in ("max_offdiag", "norm_F2"):
            x, y = g[blk][k], mine[blk][k]
            diffs[blk + "." + k] = abs(x - y) if k == "max_offdiag" else abs(x / y - 1)
        if "offdiag_entries_normalised" in g[blk]:
            for e, v in g[blk]["offdiag_entries_normalised"].items():
                diffs[blk + ".entry." + e] = max(abs(v[0] - mine[blk]["offdiag_entries_normalised"][e][0]), abs(v[1] - mine[blk]["offdiag_entries_normalised"][e][1]))
    row["max_abs_diff_vs_stored"] = max(diffs.values()); worst = max(worst, row["max_abs_diff_vs_stored"])
    row["cover_max_offdiag (rerun)"] = mine["cover"]["max_offdiag"]
    row["cell_P0 entries (rerun)"] = mine["cell_P0"]["offdiag_entries_normalised"]
    row["cell_P0+1 entries (rerun)"] = mine["cell_P0+1"]["offdiag_entries_normalised"]
    row["norm_F2 cover/P0/polar (rerun)"] = mine["norm_F2: cover vs P0 (Duffy) vs P0 (polar)"]
    row["structure"] = {k: (v if not isinstance(v, float) else float(v)) for k, v in st.items()}
    out["rows"].append(row)
    print(json.dumps({k: row[k] for k in ("config", "class", "max_abs_diff_vs_stored", "cover_max_offdiag (rerun)", "seconds")}), flush=True)
out["worst_abs_diff_vs_stored"] = worst
st, P1, Pt, chi = T.structure(Fr(2, 5), Fr(-1, 5), 0.35 + 2.75j, rng)
out["K_invariant_metrics (rerun)"] = T.invariant_metrics(P1, Pt, chi)
print("K", out["K_invariant_metrics (rerun)"], flush=True)
json.dump(out, open(HERE / "rerun_arc.json", "w"), indent=1, default=str)
print("worst |stored - rerun|:", worst)
