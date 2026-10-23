#!/usr/bin/env python3
"""POST HOC, labelled (written after zero_free_readout was read; committed before its run): two structural read-outs
of the zero-free census, from its stored rows (no new frame computation).
  1. Exact d = e.  At the best rows of the zero-free lines, R2 = R1 = 1 to six decimals (D exactly 1, or 9 with the
     by-hand factor 3).  For each direction and each of the readings S and S~ (the down quarks and the leptons read
     alike): on how many of the 266 lines is |ln R2| and |ln R1| below 1e-6 at every one of the 62 (Re tau, Im tau)
     points and both horocycles; which of the lines of the census's best family (alpha = 2/5) are exact; and the same
     for DR.  Also the largest |ln D| over every row of each direction (how far from d = e the frame can go).
  2. F_2's degeneracy: F_2's direction is R's (control C2), and R.R = 0.  The smallest m1/m3 over every sector, reading
     and row, for F_2 against DR.
    python3 -B zero_free_posthoc.py      # writes zero_free_posthoc.json and zero_free_posthoc_run.txt"""
import json, math, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
IDX = json.loads((HERE / "zero_free_census_index.json").read_text())
X = np.load(HERE / "zero_free_census.npz")["data"].astype(np.float64)          # point, dir, hor, field
TASKS = np.array(IDX["tasks"]); LINES = IDX["lines"]; DIRS = IDX["dirs"]
LN10 = math.log(10)
SECI = {("down", "S"): 4, ("down", "St"): 6, ("lep", "S"): 8, ("lep", "St"): 10}
LOG, OUT = [], {"exact d = e": {}, "max |ln D|": {}}


def say(s):
    LOG.append(s); print(s, flush=True)


lines_k = TASKS[:, 0].astype(int)
alpha25 = [k for k, l in enumerate(LINES) if l.startswith("(2/5,")]
for d in DIRS:
    di = DIRS.index(d)
    for rd in ("S", "St"):
        dn = X[:, di, :, SECI[("down", rd)]:SECI[("down", rd)] + 2] * LN10       # point, hor, (m2/m3, m1/m3) in ln
        lp = X[:, di, :, SECI[("lep", rd)]:SECI[("lep", rd)] + 2] * LN10
        lnR2 = lp[..., 0] - dn[..., 0]; lnR1 = dn[..., 1] - lp[..., 1]
        exact_row = (np.abs(lnR2) < 1e-6) & (np.abs(lnR1) < 1e-6)                # point, hor
        per_line = {}
        for k in range(len(LINES)):
            m = lines_k == k
            per_line[k] = bool(np.all(exact_row[m]))
        n_exact = sum(per_line.values())
        a25 = [LINES[k] for k in alpha25 if per_line[k]]
        OUT["exact d = e"][f"{d} {rd}"] = {"lines exact at every point": n_exact, "alpha = 2/5 lines exact": a25,
                                           "rows exact": int(exact_row.sum()), "rows": int(exact_row.size)}
        lnD = np.abs(lnR2 + lnR1)
        OUT["max |ln D|"][f"{d} {rd}"] = float(np.max(lnD[np.isfinite(lnD)]))
        say(f"1. {d:5s} read {rd:2s}: d = e exactly on {n_exact} of {len(LINES)} lines (rows {int(exact_row.sum())} of {exact_row.size}); "
            f"alpha = 2/5 lines exact: {', '.join(a25) if a25 else 'none'}")
# 2. F_2's degeneracy
for d in ("F_2", "dR"):
    di = DIRS.index(d)
    m13 = X[:, di, :, [1, 3, 5, 7, 9, 11]]
    OUT[f"smallest m1/m3, {d}"] = float(10 ** np.min(m13)); OUT[f"median of the smallest m1/m3 per row, {d}"] = float(10 ** np.median(np.min(m13, axis=0)))
    say(f"2. {d}: smallest m1/m3 over every sector, reading and row {10 ** np.min(m13):.2e}; per-row smallest, median {10 ** np.median(np.min(m13, axis=0)):.2e}")
(HERE / "zero_free_posthoc.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "zero_free_posthoc_run.txt").write_text("\n".join(LOG) + "\n")
