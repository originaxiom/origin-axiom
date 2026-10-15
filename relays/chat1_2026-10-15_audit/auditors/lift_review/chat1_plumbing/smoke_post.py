# smoke test of lift_cells.py's post-processing (Q(c), cells, Q(f), read-outs) on SYNTHETIC rows: random numbers only,
# no forms, no c~, no kappa. Exercises the admitted branches and the guards.
import json, math, pathlib, sys
import numpy as np
from scipy.stats import spearmanr
SRC = pathlib.Path(sys.argv[1]).read_text()
post = SRC[SRC.index("# ------------------------------------------------------------------ Q(c)"):]
HERE = pathlib.Path(sys.argv[1]).resolve().parent
def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()
words = [w for w in lyndon(8) if len(w) >= 2]
LS = (10.0, 100.0, 1000.0, 1.0e7)
CELLS = [("C1", None), ("C2", "E4"), ("C2", "THETA2"), ("C2", "ORTH"), ("C3", "E4"), ("C3", "THETA2"), ("C3", "ORTH")]
R2CELLS = ("C2/E4", "C3/E4", "C3/THETA2", "C3/ORTH")
def synth(scenario, rng):
    per = {}
    for w in words:
        row = {"y_max": float(rng.uniform(1, 4))}
        for cell, comp in CELLS:
            n = cell if comp is None else f"{cell}/{comp}"
            r2 = n in R2CELLS
            x = {"pd": True, "m2/m3": float(rng.uniform(1e-3, 0.9)), "m1/m3": float(rng.uniform(0, 1e-12) if r2 else rng.uniform(0, .5))}
            x["rank 2"] = bool(x["m1/m3"] < 1e-10)
            if r2:
                k = float(rng.uniform(0.01, 3)); x["kappa"] = k
                x["kappa (delta + R)"] = k * (1 + 1e-15); x["kappa (delta + c~^2 o R)"] = k * rng.uniform(0.5, 2)
            for L in LS:
                x[f"L={int(L)}: m1/m3"] = float(rng.uniform(0, .1)); x[f"L={int(L)}: m2/m3"] = x["m2/m3"]
                x[f"L={int(L)}: 4 pi L m1/m3"] = (x.get("kappa", 1.0)) * (1 + rng.normal(0, 1e-3))
            x["N256 vs N384"] = 1e-7; x["admitted"] = bool(rng.uniform() < 0.8)
            if scenario == 2 and w == "LR" and n in ("C3/ORTH", "C1"):
                x = {"pd": False, "admitted": False}
            if scenario == 3 and n == "C3/THETA2":
                x["admitted"] = False
            row[n] = x
        per[w] = row
    return per
for scenario in (1, 2, 3):
    ns = dict(json=json, math=math, np=np, spearmanr=spearmanr, HERE=HERE, words=words, LS=LS, R2CELLS=R2CELLS,
              per=synth(scenario, np.random.default_rng(scenario)), inv_by={"K32": 1e-15}, qa=1e-9, qa2=1e-9, q_beta=1e-30,
              qe=1e-15, out={}, save=lambda: None, time=__import__("time"), t0=0.0)
    exec(post, ns)
    o = ns["out"]
    print("scenario", scenario, "OK; cells", o["cells"], "| Q(f)", {k: (round(v, 3) if isinstance(v, float) else v)
          for k, v in o[[k for k in o if k.startswith("Q(f)")][0]].items()})
    print("   readout keys", len(o["readouts"]), "| L3 margin", {k: (None if v is None else round(v[0], 1))
          for k, v in o["L3"]["read-out: the margin, largest P4' m1/m3 / (eps kappa) at L = 1e7"].items()})
    json.dumps(o, default=str)
