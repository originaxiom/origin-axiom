#!/usr/bin/env python3
"""POST HOC, labelled (written after TICK_LINE_HIGGS's comparison was read, from its referee's questions; committed
before its run).  Not cells.  Reads the committed outputs only (tick_line.npz; the zero-free census npz) except (c3),
which recomputes six points in main's frame.
  (a) main's DR in main's split reading (up S~, down S, leptons S), c = 3, on the 2 400 tick points: six, nine and random
      as good over seeds 1720-1739 (the sealed comparison read DR only with S~ in every sector).
  (b) the zero-free census's own rows (seen before the rule) on the four distinct tick lines of its list, (1/5, 2/5),
      (2/5, 4/5), (1/5, 3/5), (2/5, 1/5): the menu with S, c = 3: six, nine and random as good over the same seeds.
  (c) the grid's symmetries: (c1) sign pairs (alpha, b) and (1 - alpha, 1 - b) at the same tau, all 28 fields;
      (c2) S1's lines under Re tau -> 1 - Re tau (fields equal, J flipped); (c3) S2's line at tau against S1's at tau + 1
      (T: (tau + 1, (a, b)) is (tau, (a, b + a))), six points recomputed, all four directions.
  (d) the menu with S at c = 1 on the tick grid: random as good over the same seeds.
    python3 -B tick_line_readouts2.py      # writes tick_line_readouts2.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ZF = HERE.parent / "chat1_2026-10-23_zero_free_frame"
sys.argv = ["x"]
src = (HERE / "tick_line_compare.py").read_text()
src = src[:src.index("# the cells")]                     # its loaders, rows(), calibrate(), best(); not its cells
g = {"__file__": str(HERE / "tick_line_compare.py"), "__name__": "tlc"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, "tick_line_compare.py", "exec"), g)
T6, T9, X, IDX, calibrate, best = g["T6"], g["T9"], g["X"], g["IDX"], g["calibrate"], g["best"]
TASKS, LINES, DIRS = IDX["tasks"], IDX["lines"], IDX["dirs"]
L10 = math.log(10)
OUT = {}


def l9(Y, ru, rd, rl, c):
    """Y: (..., 28) -> (..., 9) ln model values, J; readings per sector ('S' or 'St')"""
    off = {"S": 0, "St": 2}
    L = np.concatenate([Y[..., 0 + off[ru]:2 + off[ru]], Y[..., 4 + off[rd]:6 + off[rd]], Y[..., 8 + off[rl]:10 + off[rl]]], axis=-1) * L10
    L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
    k = {("S", "S"): 12, ("S", "St"): 16, ("St", "S"): 20, ("St", "St"): 24}[(ru, rd)]
    return np.concatenate([L, np.log(np.maximum(Y[..., k:k + 3], 1e-300))], axis=-1), Y[..., k + 3]


def summary(L9, J, lab):
    b = best(L9.reshape(-1, 9), J.reshape(-1), lab)
    f6, f9 = calibrate(L9.reshape(-1, 9), b["w6"], b["w9"])
    return {"six": b["six"], "six at": b["six at"], "nine": b["nine"], "nine at": b["nine at"], "rows": b["rows"],
            "random as good, mean of seeds 1720-1739 (six, nine)": [float(np.mean(f6)), float(np.mean(f9))],
            "range (six)": [min(f6), max(f6)], "range (nine)": [min(f9), max(f9)]}


# (a)
Y = X[:, DIRS.index("dR")]
L9, J = l9(Y, "St", "S", "S", 3.0)
lab = [("dR", p, h) for p in range(len(TASKS)) for h in range(2)]
OUT["(a) DR, main's split reading, c = 3, tick grid"] = summary(L9, J, lab)
# (b)
CI = json.loads((ZF / "zero_free_census_index.json").read_text())
CX = np.load(ZF / "zero_free_census.npz")["data"].astype(np.float64)
want = ["(1/5, 2/5)", "(2/5, 4/5)", "(1/5, 3/5)", "(2/5, 1/5)"]
pts = [p for p, t in enumerate(CI["tasks"]) if CI["lines"][t[0]] in want]
Ls, Js, labs = [], [], []
for d in ("F_6", "F_-2", "F_22"):
    L9c, Jc = l9(CX[pts][:, CI["dirs"].index(d)], "S", "S", "S", 3.0)
    Ls.append(L9c.reshape(-1, 9)); Js.append(Jc.reshape(-1))
    labs += [(d, p, h) for p in pts for h in range(2)]
g["TASKS"] = CI["tasks"]; g["LINES"] = CI["lines"]                        # where() reads these globals
bb = best(np.concatenate(Ls), np.concatenate(Js), labs)
f6, f9 = calibrate(np.concatenate(Ls), bb["w6"], bb["w9"])
OUT["(b) the census's rows on the four tick lines, menu, S, c = 3"] = {
    "six": bb["six"], "six at": bb["six at"], "nine": bb["nine"], "nine at": bb["nine at"], "rows": bb["rows"],
    "random as good, mean of seeds 1720-1739 (six, nine)": [float(np.mean(f6)), float(np.mean(f9))]}
g["TASKS"] = TASKS; g["LINES"] = LINES
# (c1), (c2)
tid = {(t[0], round(t[1], 3), round(t[2], 3)): p for p, t in enumerate(TASKS)}
pairs = [("(1/5, 2/5)", "(4/5, 3/5)"), ("(2/5, 4/5)", "(3/5, 1/5)"), ("(1/5, 3/5)", "(4/5, 2/5)"), ("(2/5, 1/5)", "(3/5, 4/5)")]
d1 = 0.0
for A, Bn in pairs:
    for p, t in enumerate(TASKS):
        if LINES[t[0]] == A:
            q = tid[(LINES.index(Bn), round(t[1], 3), round(t[2], 3))]
            d1 = max(d1, float(np.max(np.abs(X[p] - X[q]))))
OUT["(c1) sign pairs: largest difference over all fields (log10 ratios, |V|, J)"] = d1
d2, d2J = 0.0, 0.0
for A in ("(1/5, 2/5)", "(2/5, 4/5)", "(3/5, 1/5)", "(4/5, 3/5)"):
    k = LINES.index(A)
    for p, t in enumerate(TASKS):
        if t[0] == k:
            q = tid[(k, round(1 - t[1], 3), round(t[2], 3))]
            nonJ = [f for f in range(28) if f not in (15, 19, 23, 27)]
            d2 = max(d2, float(np.max(np.abs(X[p][..., nonJ] - X[q][..., nonJ]))))
            d2J = max(d2J, float(np.max(np.abs(X[p][..., [15, 19, 23, 27]] + X[q][..., [15, 19, 23, 27]]))))
OUT["(c2) S1 lines, Re tau -> 1 - Re tau: largest difference (all but J), largest |J + J'|"] = [d2, d2J]
# (c3)
_spec = importlib.util.spec_from_file_location("tlt", HERE / "tick_line_test.py")
tlt = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(tlt)
d3 = 0.0
for re_t, im_t in ((0.075, 2.225), (0.325, 2.725), (0.825, 2.725), (0.475, 3.025), (0.625, 2.425), (0.925, 3.325)):
    xa = tlt.point((LINES.index("(2/5, 1/5)"), re_t, im_t)).astype(np.float64)
    ma = tlt.rbs.channels(re_t + 1, im_t, 0.4, 0.8)
    xb = np.stack([tlt.zfc.rows_at(ma, tlt.zfc.direction(d, re_t + 1, im_t)) for d in tlt.DIRS])
    sel = xa[..., :12] > -12
    d3 = max(d3, float(np.max(np.abs(xa[..., :12] - xb[..., :12])[sel])))
OUT["(c3) S2's (2/5, 1/5) at tau against S1's (2/5, 4/5) at tau + 1: largest difference in log10 ratios (float32 side)"] = d3
# (d)
Ls, Js, labs = [], [], []
for d in ("F_6", "F_-2", "F_22"):
    L9d, Jd = l9(X[:, DIRS.index(d)], "S", "S", "S", 1.0)
    Ls.append(L9d.reshape(-1, 9)); Js.append(Jd.reshape(-1)); labs += [(d, p, h) for p in range(len(TASKS)) for h in range(2)]
OUT["(d) the menu, S, c = 1, tick grid"] = summary(np.concatenate(Ls), np.concatenate(Js), labs)
(HERE / "tick_line_readouts2.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
print("written")
