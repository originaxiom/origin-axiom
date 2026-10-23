#!/usr/bin/env python3
"""POST HOC, labelled (committed before its run; prompted by the owner's request to verify the framing).  Not a test.
Does the tick select the line, or only include lines that fit?  For a stored scan (the zero-free census, seen before
TICK_LINE_HIGGS's rule; later, ZERO_FREE_HOLOMORPHIC's output once read), the menu F_6, F_-2, F_22 read through S with
c = 3: for every line, its best six and best nine over the scan's points and both horocycles; the rank of the tick's
lines among all lines; how many lines fit at least as well as the tick's best; and the chance that four lines drawn at
random from the list (the tick gives four up to sign) include one that fits at least as well.
    python3 -B line_selection_control.py census      # writes line_selection_control_census.json
    python3 -B line_selection_control.py holo        # writes line_selection_control_holo.json"""
import json, math, sys, subprocess, hashlib, pathlib
from math import comb
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
ZF = HERE.parent / "chat1_2026-10-23_zero_free_frame"
which = sys.argv[1]
if which == "census":
    IDX = json.loads((ZF / "zero_free_census_index.json").read_text()); X = np.load(ZF / "zero_free_census.npz")["data"]
else:
    IDX = json.loads((ZF / "zero_free_holomorphic_index.json").read_text()); X = np.load(ZF / "zero_free_holomorphic.npz")["data"]


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
v = json.loads(bd)["masses_GeV"]["value"]; C = json.loads(bc)["ckm_abs"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
LINES = IDX["lines"]; line_of = np.array([t[0] for t in IDX["tasks"]])
TICK = ["(1/5, 2/5)", "(2/5, 4/5)", "(1/5, 3/5)", "(2/5, 1/5)"]          # the list's forms of S1 and S2 up to sign
per = {}
for k, name in enumerate(LINES):
    m = line_of == k
    b6, b9 = np.inf, np.inf
    for d in ("F_6", "F_-2", "F_22"):
        Y = X[m, IDX["dirs"].index(d)].astype(np.float64)                 # point, hor, field
        L = np.concatenate([Y[..., 0:2], Y[..., 4:6], Y[..., 8:10]], axis=-1) * math.log(10)
        L[..., 4] += math.log(3); L[..., 5] -= math.log(3)
        L9 = np.concatenate([L, np.log(np.maximum(Y[..., 12:15], 1e-300))], axis=-1)
        b6 = min(b6, float(np.min(np.max(np.abs(L9[..., :6] - T6), axis=-1))))
        b9 = min(b9, float(np.min(np.max(np.abs(L9 - T9), axis=-1))))
    per[name] = (math.exp(b6), math.exp(b9))
order6 = sorted(LINES, key=lambda n: per[n][0]); order9 = sorted(LINES, key=lambda n: per[n][1])
t6 = min(per[n][0] for n in TICK if n in per); t9 = min(per[n][1] for n in TICK if n in per)
n6 = sum(1 for n in LINES if per[n][0] <= t6 + 1e-12); n9 = sum(1 for n in LINES if per[n][1] <= t9 + 1e-12)
N = len(LINES)
OUT = {"scan": which, "lines": N,
       "tick lines in the list": [n for n in TICK if n in per],
       "tick's best six, nine": [t6, t9],
       "ranks of the tick lines (six)": {n: order6.index(n) + 1 for n in TICK if n in per},
       "ranks of the tick lines (nine)": {n: order9.index(n) + 1 for n in TICK if n in per},
       "lines fitting at least as well as the tick's best (six, nine)": [n6, n9],
       "chance that 4 random lines include one as good (six, nine)": [1 - comb(N - n6, 4) / comb(N, 4), 1 - comb(N - n9, 4) / comb(N, 4)],
       "top 15 lines by six": [[n, round(per[n][0], 3), round(per[n][1], 3)] for n in order6[:15]],
       "top 15 lines by nine": [[n, round(per[n][0], 3), round(per[n][1], 3)] for n in order9[:15]],
       "alpha = 2/5 lines": {n: [round(per[n][0], 3), round(per[n][1], 3)] for n in LINES if n.startswith("(2/5")}}
(HERE / f"line_selection_control_{which}.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
