"""POST HOC (labelled), filed after the second referee: the per-thread hybrid. W72's surface Yukawa Y (the SM seat's
banked the_surface_yukawa.json at 87cf7f551, X4, Y0 = 2.0), normalised by each thread's own K from thread_frame.json
(sealed run 19417427e). The first referee computed this by hand and the findings quoted it ("reproduces that thread's
m2/m3 within about 10%") without a filed script; this files it. No new forms are built. masses() is copied verbatim
from thread_frame.py.

Read-outs, per thread: the hybrid's m2/m3 and m1/m3 beside the thread's own; the ratios hybrid / own.

Run once:  python3 -B post_hoc_hybrid.py > post_hoc_hybrid_run.txt 2>&1   (writes post_hoc_hybrid.json)
"""
import json, pathlib, subprocess
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
SMC = "87cf7f55111ec1f4019f302ffaa578376a9143e6"
banked = json.loads(subprocess.run(["git", "-C", str(REPO), "show",
                                    f"{SMC}:docs/dossiers/the_weave_2026-10-07/the_surface_yukawa.json"],
                                   check=True, capture_output=True, text=True).stdout)
Yb = np.array([[complex(*z) for z in row] for row in banked["X4"]["Y (Y0 = 2.0)"]])
per = json.loads((HERE / "thread_frame.json").read_text())["readouts"]["per thread"]


def masses(K, Y):
    ev, U = np.linalg.eigh(K)
    Kmh = U @ np.diag(ev ** -0.5) @ U.conj().T
    Yh = Kmh.T @ Y @ Kmh
    Uu, s, Vh = np.linalg.svd(Yh)
    order = np.argsort(s)
    s = s[order]; V = Vh.conj().T[:, order]
    comps = []
    for k in range(3):
        c = Kmh @ V[:, k]
        comps.append([float(abs(c[j]) ** 2 * K[j, j].real) for j in range(3)])
    return {"m": s.tolist(), "m2/m3": float(s[1] / s[2]), "m1/m3": float(s[0] / s[2]), "m1/m2": float(s[0] / s[1]),
            "K eigenvalues": ev.tolist(), "weights on (F_i, F+, F-) per state (light to heavy)": comps}


out = {"status": "post hoc (labelled), filed after the second referee", "W72 Y source": f"{SMC}: X4, Y (Y0 = 2.0)",
       "per thread": {}}
for w, r in sorted(per.items(), key=lambda kv: kv[1]["y_max"]):
    K = np.array([[complex(*z) for z in row] for row in r["K"]])
    h = masses(K, Yb)
    out["per thread"][w] = {"y_max": r["y_max"], "own m2/m3": r["m2/m3"], "hybrid m2/m3": h["m2/m3"],
                            "hybrid / own (m2/m3)": h["m2/m3"] / r["m2/m3"], "own m1/m3": r["m1/m3"],
                            "hybrid m1/m3": h["m1/m3"], "hybrid / own (m1/m3)": h["m1/m3"] / r["m1/m3"]}
    print(f"{w:<6} y {r['y_max']:.3f}  m2/m3 own {r['m2/m3']:.4g} hybrid {h['m2/m3']:.4g} (x{h['m2/m3'] / r['m2/m3']:.3f})"
          f"   m1/m3 own {r['m1/m3']:.3g} hybrid {h['m1/m3']:.3g} (x{h['m1/m3'] / r['m1/m3']:.2f})")
q2 = [v["hybrid / own (m2/m3)"] for v in out["per thread"].values()]
q1 = [v["hybrid / own (m1/m3)"] for v in out["per thread"].values()]
out["range hybrid / own"] = {"m2/m3": [min(q2), max(q2)], "m1/m3": [min(q1), max(q1)]}
print("range hybrid/own: m2/m3", [round(min(q2), 3), round(max(q2), 3)], " m1/m3", [round(min(q1), 3), round(max(q1), 3)])
(HERE / "post_hoc_hybrid.json").write_text(json.dumps(out, indent=1) + "\n")
