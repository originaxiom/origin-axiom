#!/usr/bin/env python3
"""POST HOC read-out, labelled (after bl_line_readout was read, at the referee's prompt): on the B - L line scan,
  (i)   how often R2 >= 2.5 on the window, per point (reading S~ in every sector);
  (ii)  the best six where both R2 and R1 lie in [2, 4.5];
  (iii) the ranges of R2 and R1 on the rows whose D is within 3 sigma of P-094;
  (iv)  over all 27 (up, down, lepton) reading combinations: the best six among the D-matched rows, separately for
        the 9 combinations with the down quarks and leptons on the same reading and the 18 mixed ones.
    python3 -B bl_line_readout2.py      # writes bl_line_readout2_run.txt"""
import hashlib, json, math, subprocess, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
bd = subprocess.run(["git", "show", "3412bf09d:frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"],
                    cwd=ROOT, capture_output=True, check=True).stdout
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
v = json.loads(bd)["masses_GeV"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
P094, SIG = 10.58, 0.11
rows = [json.loads(l) for l in (HERE / "bl_line_scan.jsonl").read_text().splitlines() if l.strip()]
RD = ("S", "St", "conjS")
LOG = []
for point in ("six_best", "nine_best", "tick_d_eq_e"):
    P = [r for r in rows if r["point"] == point]
    recs = {}
    for r in P:
        for hor in ("L_max", "L_2"):
            for cu in RD:
                for cd in RD:
                    for cl in RD:
                        x = np.log(np.maximum(np.array(r[f"up|{hor}|{cu}"] + r[f"down|{hor}|{cd}"] + r[f"lep|{hor}|{cl}"], dtype=float), 1e-300))
                        recs.setdefault((cu, cd, cl), []).append({"six": float(np.exp(np.max(np.abs(x - T6)))), "R2": math.exp(x[4] - x[2]),
                                                                  "R1": math.exp(x[3] - x[5]), "w": (r["a2"], r["b2"], hor)})
    s = recs[("St", "St", "St")]
    frac = np.mean([q["R2"] >= 2.5 for q in s])
    gj = [q for q in s if 2 <= q["R2"] <= 4.5 and 2 <= q["R1"] <= 4.5]
    dm = [q for q in s if abs(q["R2"] * q["R1"] - P094) <= 3 * SIG]
    LOG.append(f"== {point} (S~ in every sector): R2 >= 2.5 on {frac:.0%} of the window's rows")
    LOG.append(f"   rows with R2 and R1 both in [2, 4.5]: {len(gj)}; best six there {min(q['six'] for q in gj):.2f}" if gj else "   no row with R2 and R1 both in [2, 4.5]")
    if dm:
        LOG.append(f"   D-matched rows: {len(dm)}; R2 {min(q['R2'] for q in dm):.2f}-{max(q['R2'] for q in dm):.2f}, R1 {min(q['R1'] for q in dm):.2f}-{max(q['R1'] for q in dm):.2f}")
    same, mixed = [], []
    for (cu, cd, cl), lst in recs.items():
        d = [q for q in lst if abs(q["R2"] * q["R1"] - P094) <= 3 * SIG]
        if d:
            (same if cd == cl else mixed).append(min(q["six"] for q in d))
    LOG.append(f"   all 27 reading combinations, best six among D-matched rows: same down/lepton reading {min(same):.2f}"
               + (f"; mixed {min(mixed):.2f}" if mixed else "; mixed: none D-matched"))
print("\n".join(LOG))
(HERE / "bl_line_readout2_run.txt").write_text("\n".join(LOG) + "\n")
