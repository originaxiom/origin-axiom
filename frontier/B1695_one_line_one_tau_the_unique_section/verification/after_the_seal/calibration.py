"""B1695, after the seal (labelled; not sealed): how special is the best fit? Uses only the stored grid (no new model
values).  (1) Sector permutations: the six measured ratios assigned to the sectors in all 6 orders (the true order is one):
the best worst-factor for each.  (2) Look-elsewhere: 2000 random hierarchical target sets -- per sector log10 m2/m3
uniform in [-3, -1] and log10 m1/m3 uniform in [-6, -2.5] with m1/m3 < m2/m3, the measured ranges widened -- and the
fraction for which the grid (all 12 discrete choices) achieves a worst factor <= the measured fit's 1.788.
    python3 -B calibration.py      # writes calibration.json beside itself"""
import json, math, random, itertools, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
V = HERE.parent
grid = json.loads((V / "the_grid.json").read_text(encoding="utf-8"))["grid"]
cmp_ = json.loads((V / "comparison.json").read_text(encoding="utf-8"))
T = {k: v["value"] for k, v in cmp_["targets"].items()}
SEC = ["up", "down", "lep"]
# the model as an array: rows = (point, combo), columns = 6 log-ratios in the order up r2, up r1, down r2, down r1, lep r2, lep r1
rows = []
for p in grid:
    for hor in ("L_max", "L_2"):
        for rd in ("S", "St", "conjS"):
            m = [p["up|%s|%s" % (hor, rd)], p["down|%s|S" % hor], p["lep|%s|S" % hor]]
            vals = [m[0][0], m[0][1], m[1][0], m[1][1], m[2][0], m[2][1]]
            if all(x > 0 for x in vals): rows.append([math.log(x) for x in vals])
A = np.array(rows)
def best_worst(target):                                     # target: 6 values in the same order
    t = np.log(np.array(target)); return float(np.exp(np.min(np.max(np.abs(A - t), axis=1))))
true = [T["up|m2/m3"], T["up|m1/m3"], T["down|m2/m3"], T["down|m1/m3"], T["lep|m2/m3"], T["lep|m1/m3"]]
out = {"true_order_best_worst_factor": best_worst(true), "model_rows": len(rows)}
perm = {}
for order in itertools.permutations(range(3)):
    tg = []
    for i in order: tg += true[2 * i: 2 * i + 2]
    perm["".join(SEC[i][0] for i in order)] = best_worst(tg)
out["sector_permutations_best_worst_factor"] = perm
rng = random.Random(1695); hits = 0; N = 2000; samples = []
for _ in range(N):
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2: break
        tg += [r2, r1]
    bw = best_worst(tg); samples.append(bw); hits += bw <= out["true_order_best_worst_factor"] + 1e-12
out["random_targets"] = {"N": N, "fraction_fit_as_well": hits / N, "median_best_worst": float(np.median(samples)),
                         "quantiles_5_25": [float(np.quantile(samples, 0.05)), float(np.quantile(samples, 0.25))]}
json.dump(out, open(HERE / "calibration.json", "w"), indent=1); print(json.dumps(out, indent=1))
