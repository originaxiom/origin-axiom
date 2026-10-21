"""B1702 (P-249): the masses at the other cusp shapes against the six measured ratios, with the calibration sealed in.  For
every tau, line and choice (horocycle, up reading): the worst factor over the six ratios and chi2 (sigma^2 = the data's
errors^2 + B1637's 10%^2).  The calibration: 4000 random hierarchical target sets (B1695's prior), each fitted by the
same rows; the fraction fitted at least as well as the data (by the worst factor).
    python3 -B compare.py      # writes comparison.json beside itself"""
import hashlib, json, math, random, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
ALLOW = 0.10
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SHA
d = json.loads(DATA.read_text(encoding="utf-8")); v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
def meas(a, b): return v[a] / v[b], math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2)
TGT = [meas("c", "t"), meas("u", "t"), meas("s", "b"), meas("d", "b"), meas("mu", "tau"), meas("e", "tau")]
G = json.loads((HERE / "the_cusp_shapes.json").read_text(encoding="utf-8"))
lab, A = [], []
for p in G["rows"]:
    for hor in ("L_max", "L_2"):
        for rd in ("S", "St", "conjS"):
            m = [p["up|%s|%s" % (hor, rd)], p["down|%s|S" % hor], p["lep|%s|S" % hor]]
            vals = [m[0][0], m[0][1], m[1][0], m[1][1], m[2][0], m[2][1]]
            if all(x > 0 for x in vals): A.append([math.log(x) for x in vals]); lab.append((p["line"], hor, rd, p["tau"]))
A = np.array(A); t = np.log(np.array([x[0] for x in TGT])); sig = np.array([x[1] for x in TGT])
worst = np.exp(np.max(np.abs(A - t), axis=1)); chi2 = np.sum(((A - t) / sig) ** 2, axis=1)
ib, ic = int(np.argmin(worst)), int(np.argmin(chi2))
def best_worst(target): return float(np.exp(np.min(np.max(np.abs(A - np.log(np.array(target))), axis=1))))
rng = random.Random(1702); N = 4000; hits = 0; samples = []
for _ in range(N):
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2: break
        tg += [r2, r1]
    b = best_worst(tg); samples.append(b); hits += b <= float(worst[ib]) + 1e-12
mins = {nm: float(np.exp(A[:, i].min())) for i, nm in enumerate(("up m2/m3", "up m1/m3", "down m2/m3", "down m1/m3", "lep m2/m3", "lep m1/m3"))}
per_tau = {}
for nm in G["taus"]:
    idx = [i for i, l in enumerate(lab) if l[3] == nm]; j = min(idx, key=lambda i: worst[i])
    per_tau[nm] = {"best_worst": float(worst[j]), "line": G["lines"][lab[j][0]], "at": lab[j][1:3], "min_chi2": float(min(chi2[i] for i in idx))}
out = {"data_sha256": SHA, "taus": G["taus"], "rows": len(lab), "per_tau": per_tau,
       "best_by_worst_factor": {"tau": lab[ib][3], "line": G["lines"][lab[ib][0]], "horocycle": lab[ib][1], "up_reading": lab[ib][2],
                                "worst_factor": float(worst[ib]), "chi2": float(chi2[ib]), "model_log": A[ib].tolist(), "targets": [x[0] for x in TGT]},
       "best_by_chi2": {"line": G["lines"][lab[ic][0]], "at": lab[ic][1:], "chi2": float(chi2[ic]), "worst_factor": float(worst[ic])},
       "smallest_model_ratio_over_all_rows": mins,
       "H1_within_factor_3": float(worst[ib]) <= 3.0,
       "calibration": {"N": N, "fraction_fit_as_well": hits / N, "median": float(np.median(samples)), "q01": float(np.quantile(samples, 0.01)), "q05": float(np.quantile(samples, 0.05))},
       "H2_specific_p_below_0.01": hits / N <= 0.01,
       "H3_chi2_below_16.75": float(chi2[ic]) < 16.75}
if __name__ == "__main__":
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1)
    print("H1", out["H1_within_factor_3"], "H2", out["H2_specific_p_below_0.01"], "H3", out["H3_chi2_below_16.75"])
