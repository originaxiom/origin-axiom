#!/usr/bin/env python3
"""POST HOC read-out, labelled (written after the TWO_INGREDIENTS comparison was read, at the referee's prompt): the
double ratio D = (y_mu y_d)/(y_s y_e) of the sealed model (S~ for every sector, Clebsch 3 on the leptons) on the sealed
census's rows, against the record's data target P-094, D = 10.58 +- 0.11 (Antusch, Hinze and Saad, arXiv:2510.01312v2,
eq. 4.7; Georgi-Jarlskog's 9 excluded).  D depends on the Clebsch c only through c^2: D_model = c^2 D_frame.
    python3 -B d_readout.py      # writes d_readout.json and d_readout_run.txt"""
import hashlib, json, math, subprocess, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
bd = subprocess.run(["git", "show", "3412bf09d:frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"],
                    cwd=ROOT, capture_output=True, check=True).stdout
bc = subprocess.run(["git", "show", "3412bf09d:frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json"],
                    cwd=ROOT, capture_output=True, check=True).stdout
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
v = json.loads(bd)["masses_GeV"]["value"]; C = json.loads(bc)["ckm_abs"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
P094, P094_SIG = 10.58, 0.11
rows = [json.loads(l) for l in (HERE / "two_ingredients_census.jsonl").read_text().splitlines() if l.strip()]
M, D = [], []
for r in rows:
    for hor in ("L_max", "L_2"):
        vals = r[f"up|{hor}|St"] + r[f"down|{hor}|St"] + r[f"lep|{hor}|St"] + r[f"ckm|{hor}|St|St"][:3]
        x = np.log(np.maximum(np.array(vals, dtype=float), 1e-300)); x[4] += math.log(3); x[5] -= math.log(3)
        M.append(x); D.append(math.exp((x[4] - x[2]) + (x[3] - x[5])))     # (mu/tau)/(s/b) * (d/b)/(e/tau)
M, D = np.array(M), np.array(D)
w6 = np.exp(np.max(np.abs(M[:, :6] - T6), axis=1)); w9 = np.exp(np.max(np.abs(M - T9), axis=1))
LOG = []


def say(s):
    LOG.append(s); print(s)


out = {"P094": [P094, P094_SIG], "D_at_best_six": float(D[np.argmin(w6)]), "D_at_best_nine": float(D[np.argmin(w9)])}
say(f"P-094: D = {P094} +- {P094_SIG}.  Sealed model: D at the best six-row {out['D_at_best_six']:.2f}, at the best nine-row "
    f"{out['D_at_best_nine']:.2f}")
for name, w, cut in (("six within 2.0", w6, 2.0), ("six within 1.8", w6, 1.8), ("nine within 2.5", w9, 2.5), ("nine within 3.0", w9, 3.0)):
    m = w <= cut
    if m.any():
        dd = D[m]; near = np.abs(dd - P094) <= 3 * P094_SIG
        out[name] = {"rows": int(m.sum()), "D_min": float(dd.min()), "D_max": float(dd.max()), "within_3_sigma_of_P094": int(near.sum())}
        say(f"rows with {name}: {int(m.sum())}; D from {dd.min():.2f} to {dd.max():.2f}; within 3 sigma of P-094: {int(near.sum())}")
(HERE / "d_readout.json").write_text(json.dumps(out, indent=1) + "\n")
(HERE / "d_readout_run.txt").write_text("\n".join(LOG) + "\n")
