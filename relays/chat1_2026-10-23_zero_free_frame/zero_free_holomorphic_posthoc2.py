#!/usr/bin/env python3
"""POST HOC read-outs, labelled (ZERO_FREE_HOLOMORPHIC: written after the referee's report on the draft result note;
committed before its own run).  None is a cell.  They put the note's P2 (the tick's lines alone) beside other line sets
of the same size, so that P2 is read as what it is:
  Q1  the menu (S, c = 3) on four-line sets: the tick's four; (2/5, 4/5) with three other lines drawn at random (200
      draws, random.Random(1720)); (2/5, 1/10) with three random others; (2/5, 1/2) with three random others; the ten
      alpha = 2/5 lines; random as good, the mean of the 20 seeds, and the best six and nine on each set;
  Q2  the reference (DR, S~, c = 3) on its own best four lines (by its best six) and on the tick's four;
  Q3  F_22 alone on the tick's lines (TICK_LINE_HIGGS's best direction there).
    python3 -B zero_free_holomorphic_posthoc2.py      # writes zero_free_holomorphic_posthoc2.json"""
import hashlib, json, math, random, subprocess, pathlib
import numpy as np
from scipy.spatial import cKDTree

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
v = json.loads(bd)["masses_GeV"]["value"]; C = json.loads(bc)["ckm_abs"]["value"]
PAIRS = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T6 = np.log(np.array([v[a] / v[b] for a, b in PAIRS]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
IDX = json.loads((HERE / "zero_free_holomorphic_index.json").read_text())
X = np.load(HERE / "zero_free_holomorphic.npz")["data"].astype(np.float64)
TASKS = IDX["tasks"]; LINES = IDX["lines"]; DIRS = IDX["dirs"]
MENU = ["F_6", "F_-2", "F_22"]
SEC = {"S": (0, 4, 8), "St": (2, 6, 10)}; CK = {"S": 12, "St": 24}
TICK = ["(1/5, 2/5)", "(2/5, 4/5)", "(1/5, 3/5)", "(2/5, 1/5)"]
BYLINE = {}
for p, (k, _r, _i) in enumerate(TASKS):
    BYLINE.setdefault(LINES[k], []).append(p)


def r_masses(rng):
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2:
                break
        tg += [r2, r1]
    return tg


def r_ckm(rng):
    while True:
        a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
        if c < b < a:
            return [a, b, c]


TG = []
for sd in range(1720, 1740):
    rng = random.Random(sd)
    d6 = np.log(np.array([r_masses(rng) for _ in range(4000)]))
    d9 = np.log(np.array([r_masses(rng) + r_ckm(rng) for _ in range(4000)]))
    TG.append((d6, d9))


def rows(dirs, rd, lines):
    sel = [p for l in lines for p in BYLINE[l]]
    Ls = []
    for d in dirs:
        Y = X[sel][:, DIRS.index(d)]
        iu, idn, il = SEC[rd]
        L = np.concatenate([Y[..., iu:iu + 2], Y[..., idn:idn + 2], Y[..., il:il + 2]], axis=-1) * math.log(10)
        L[..., 4] += math.log(3); L[..., 5] -= math.log(3)
        Ls.append(np.concatenate([L, np.log(np.maximum(Y[..., CK[rd]:CK[rd] + 3], 1e-300))], axis=-1).reshape(-1, 9))
    return np.concatenate(Ls)


def calib(L9):
    six = np.max(np.abs(L9[:, :6] - T6), axis=1); nine = np.max(np.abs(L9 - T9), axis=1)
    w6, w9 = float(six.min()), float(nine.min())
    t6, t9 = cKDTree(L9[:, :6]), cKDTree(L9)
    f6, f9 = [], []
    for d6, d9 in TG:
        q6, _ = t6.query(d6, k=1, p=np.inf); q9, _ = t9.query(d9, k=1, p=np.inf)
        f6.append(float(np.mean(q6 <= w6 + 1e-12))); f9.append(float(np.mean(q9 <= w9 + 1e-12)))
    return math.exp(w6), math.exp(w9), float(np.mean(f6)), float(np.mean(f9))


def summ(vals):
    a = np.array(vals)
    return {"median": float(np.median(a)), "quartiles": [float(np.quantile(a, 0.25)), float(np.quantile(a, 0.75))]}


OUT = {}
s6, s9, f6, f9 = calib(rows(MENU, "S", TICK))
OUT["Q1 the tick's four"] = {"six": s6, "nine": s9, "six as good": f6, "nine as good": f9}
others = [l for l in LINES]
rng = random.Random(1720)
for anchor in ("(2/5, 4/5)", "(2/5, 1/10)", "(2/5, 1/2)"):
    res = []
    pool = [l for l in others if l != anchor]
    for _ in range(200):
        lines = [anchor] + rng.sample(pool, 3)
        res.append(calib(rows(MENU, "S", lines)))
    OUT[f"Q1 {anchor} with three random others (200 draws)"] = {
        "six": summ([r[0] for r in res]), "nine": summ([r[1] for r in res]),
        "six as good": summ([r[2] for r in res]), "nine as good": summ([r[3] for r in res])}
A25 = [l for l in LINES if l.startswith("(2/5,")]
s6, s9, f6, f9 = calib(rows(MENU, "S", A25))
OUT["Q1 the ten alpha = 2/5 lines"] = {"lines": A25, "six": s6, "nine": s9, "six as good": f6, "nine as good": f9}
# Q2 the reference on its own best four lines and on the tick's
best_by_line = []
for l in LINES:
    L9 = rows(["dR"], "St", [l])
    best_by_line.append((float(np.exp(np.max(np.abs(L9[:, :6] - T6), axis=1).min())), l))
own = [l for _, l in sorted(best_by_line)[:4]]
s6, s9, f6, f9 = calib(rows(["dR"], "St", own))
OUT["Q2 the reference on its own best four lines (by its best six)"] = {"lines": own, "six": s6, "nine": s9, "six as good": f6, "nine as good": f9}
s6, s9, f6, f9 = calib(rows(["dR"], "St", TICK))
OUT["Q2 the reference on the tick's four"] = {"six": s6, "nine": s9, "six as good": f6, "nine as good": f9}
L9 = rows(["dR"], "St", ["(2/5, 4/5)"])
OUT["Q2 the reference's best six on (2/5, 4/5)"] = float(np.exp(np.max(np.abs(L9[:, :6] - T6), axis=1).min()))
# Q3 F_22 alone on the tick's lines
L9 = rows(["F_22"], "S", TICK)
OUT["Q3 F_22 alone on the tick's lines"] = {"six": float(np.exp(np.max(np.abs(L9[:, :6] - T6), axis=1).min())),
                                           "nine": float(np.exp(np.max(np.abs(L9 - T9), axis=1).min()))}
(HERE / "zero_free_holomorphic_posthoc2.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
