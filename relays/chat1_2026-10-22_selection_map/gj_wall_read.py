#!/usr/bin/env python3
"""The Georgi-Jarlskog wall (GJ_WALL_RULE.md): read B1720's committed census rows and score cells G1-G3.
    python3 -B gj_wall_read.py [--source b1713]      (default: B1720 at main's 3412bf09d)"""
import json, math, subprocess, sys, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SRC = {"b1720": ("3412bf09d", "frontier/B1720_the_thread_fixes_the_point/verification/the_thread_census.json"),
       "b1713": ("3412bf09d", "frontier/B1713_the_complement_and_the_mixing/verification/the_complement_and_mixing.json")}
which = sys.argv[sys.argv.index("--source") + 1] if "--source" in sys.argv else "b1720"
rev, path = SRC[which]
root = next(q for q in HERE.parents if (q / ".git").exists())
data = json.loads(subprocess.run(["git", "show", f"{rev}:{path}"], cwd=root, capture_output=True, check=True).stdout)

# the data (Huang-Zhou 2021 at M_Z, the record's pinned transcription)
m = {"e": 0.00048307, "mu": 0.101766, "tau": 1.72856, "d": 0.00267, "s": 0.05316, "b": 2.839}
R2d = (m["mu"] / m["tau"]) / (m["s"] / m["b"])
R1d = (m["d"] / m["b"]) / (m["e"] / m["tau"])
lDd, lZd = math.log(R2d * R1d), math.log(R2d / R1d)

lR2, lR1, keys = [], [], []
for r in data["rows"]:
    for h in ("L_max", "L_2"):
        d, e = r.get(f"down|{h}|S"), r.get(f"lep|{h}|S")
        if not d or not e or min(d + e) <= 1e-12:
            continue
        lR2.append(math.log(e[0] / d[0])); lR1.append(math.log(d[1] / e[1]))
        keys.append({k: r[k] for k in r if not isinstance(r[k], list)} | {"horocycle": h})
lR2, lR1 = np.array(lR2), np.array(lR1)
lD, lZ = lR2 + lR1, lR2 - lR1
corr = float(np.corrcoef(lR2, lR1)[0, 1])
dist = np.maximum(np.abs(lD - lDd), np.abs(lZ - lZd))
ib = int(np.argmin(dist))
near_Z = np.abs(lZ - lZd) < 0.3
out = {
    "source": which, "rev": rev, "rows": int(len(lD)),
    "data": {"R2": R2d, "R1": R1d, "D": R2d * R1d, "Z": R2d / R1d},
    "G1_corr": corr, "G1_holds": corr < -0.5,
    "G2_rows_within_0.3": int(np.sum(dist < 0.3)), "G2_holds": bool(np.sum(dist < 0.3) == 0),
    "G3_max_D_where_Z_near": float(np.exp(lD[near_Z].max())) if near_Z.any() else None,
    "G3_n_Z_near": int(near_Z.sum()),
    "G3_holds": bool((not near_Z.any()) or lD[near_Z].max() < 1.9),
    "closest": {"maxdev": float(dist[ib]), "D": float(np.exp(lD[ib])), "Z": float(np.exp(lZ[ib])), "row": keys[ib]},
    "logD_quantiles": [float(x) for x in np.quantile(lD, [.01, .05, .25, .5, .75, .95, .99])],
    "logZ_quantiles": [float(x) for x in np.quantile(lZ, [.01, .05, .25, .5, .75, .95, .99])],
}
txt = json.dumps(out, indent=1, default=str)
print(txt)
if which == "b1720":
    (HERE / "gj_wall_read.json").write_text(txt + "\n")
    (HERE / "gj_wall_read_run.txt").write_text(
        f"rows {out['rows']}; G1 corr {corr:.3f} -> {'HOLDS' if out['G1_holds'] else 'FAILS'}; "
        f"G2 rows within 0.3: {out['G2_rows_within_0.3']} -> {'HOLDS' if out['G2_holds'] else 'FAILS'}; "
        f"G3 max D where Z near: {out['G3_max_D_where_Z_near']} -> {'HOLDS' if out['G3_holds'] else 'FAILS'}; "
        f"closest maxdev {out['closest']['maxdev']:.3f}\n")
