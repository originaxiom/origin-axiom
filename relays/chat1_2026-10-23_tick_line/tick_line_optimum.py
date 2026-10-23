#!/usr/bin/env python3
"""POST HOC, EXPLORATORY, labelled (written after TICK_LINE_HIGGS's comparison was read; committed before its run).
Not a test: it fits tau to the data, so nothing here can earn a positive.  It asks where, given the discrete data the
sealed test selected (the tick's line, the zero-free holomorphic Higgs read through S, c = 3 by hand), the data want tau:
the target a principle for tau would have to hit.
For three combinations (F_22 on S2's (2/5, 1/5) in L_max, where the sealed best nine-row lies; F_22 on S1's (2/5, 4/5)
in L_2, the best six-row; F_6 on (2/5, 4/5) in L_2, F_6's best), start at that combination's best nine-row of the
sealed grid (tick_line.npz) and minimise the nine (the worst |ln model - ln data| over the six ratios and three |V|) over
(Re tau, Im tau) by Nelder-Mead, Im tau kept in [1.5, 4.0].  Reports tau*, the nine and the six there, model over
measured, J and D; and the nine on a 0.025 grid of +-0.05 around tau* (its flatness).
Targets: the record's pinned files at 3412bf09d, as in tick_line_compare.py.
    python3 -B tick_line_optimum.py      # writes tick_line_optimum.json"""
import contextlib, hashlib, importlib.util, io, json, math, subprocess, sys, pathlib
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import minimize

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("tlt", HERE / "tick_line_test.py")
tlt = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(tlt)
zfc, rbs = tlt.zfc, tlt.rbs


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
v = json.loads(bd)["masses_GeV"]["value"]; C = json.loads(bc)["ckm_abs"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
IDX = json.loads((HERE / "tick_line_index.json").read_text())
X = np.load(HERE / "tick_line.npz")["data"].astype(np.float64)


def l9_from_fields(x, c=3.0):
    L = np.array([x[0], x[1], x[4], x[5], x[8], x[9]]) * math.log(10)          # reading S: up, down, lep
    L[4] += math.log(c); L[5] -= math.log(c)
    return np.concatenate([L, np.log(np.maximum(x[12:15], 1e-300))]), x[15]


def model(d, line, hor, re_t, im_t):
    a, b = (float(Fr(s.strip())) for s in line.strip("()").split(","))
    M = rbs.channels(re_t, im_t, a, b)
    x = zfc.rows_at(M, zfc.direction(d, re_t, im_t))[rbs.HORS.index(hor)]
    return l9_from_fields(x)


def nine(p, d, line, hor):
    re_t, im_t = p
    if not 1.5 <= im_t <= 4.0:
        return 50.0
    L9, _J = model(d, line, hor, re_t, im_t)
    return float(np.max(np.abs(L9 - T9)))


OUT = {}
for d, line, hor in (("F_22", "(2/5, 1/5)", "L_max"), ("F_22", "(2/5, 4/5)", "L_2"), ("F_6", "(2/5, 4/5)", "L_2")):
    di, k, ih = IDX["dirs"].index(d), IDX["lines"].index(line), IDX["hors"].index(hor)
    pts = [p for p, t in enumerate(IDX["tasks"]) if t[0] == k]
    best = min(pts, key=lambda p: float(np.max(np.abs(l9_from_fields(X[p, di, ih])[0] - T9))))
    start = IDX["tasks"][best][1:]
    res = minimize(nine, x0=np.array(start), args=(d, line, hor), method="Nelder-Mead",
                   options={"xatol": 1e-4, "fatol": 1e-6, "maxfev": 250, "initial_simplex": np.array([start, [start[0] + 0.03, start[1]], [start[0], start[1] + 0.03]])})
    re_s, im_s = map(float, res.x)
    L9, J = model(d, line, hor, re_s, im_s)
    R2 = math.exp(L9[4] - L9[2]); R1 = math.exp(L9[3] - L9[5])
    grid = {}
    for dr in np.linspace(-0.05, 0.05, 5):
        for dy in np.linspace(-0.05, 0.05, 5):
            grid[f"{dr:+.2f},{dy:+.2f}"] = math.exp(nine((re_s + dr, im_s + dy), d, line, hor))
    OUT[f"{d} on {line}, {hor}"] = {
        "start (best grid nine-row)": start, "start nine": math.exp(nine(start, d, line, hor)),
        "tau*": [re_s, im_s], "nine at tau*": math.exp(res.fun), "six at tau*": math.exp(float(np.max(np.abs(L9[:6] - T6)))),
        "model over measured at tau*": np.exp(L9 - T9).round(3).tolist(), "J at tau*": float(J), "D at tau*": R2 * R1,
        "evaluations": int(res.nfev), "nine on the +-0.05 grid, step 0.025 (factor)": grid}
    print(d, line, hor, "done", flush=True)
(HERE / "tick_line_optimum.json").write_text(json.dumps(OUT, indent=1) + "\n")
