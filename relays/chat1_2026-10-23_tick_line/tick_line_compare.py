#!/usr/bin/env python3
"""TICK_LINE_HIGGS's comparison (sealed rule: TICK_LINE_HIGGS_RULE.md, e0c16e1cd; committed before the outputs it reads
exist).  Cells K1-K7 and controls C1-C2 exactly as the rule states them, then the read-outs.
    python3 -B tick_line_compare.py      # writes tick_line_compare.json and tick_line_compare_run.txt"""
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
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
JPDG = 3.08e-5
IDX = json.loads((HERE / "tick_line_index.json").read_text())
X = np.load(HERE / "tick_line.npz")["data"].astype(np.float64)                 # point, dir, hor, field
CTRL = json.loads((HERE / "tick_line_controls.json").read_text())
TASKS = IDX["tasks"]; LINES = IDX["lines"]; DIRS = IDX["dirs"]; HORS = IDX["hors"]
MENU = ["F_6", "F_-2", "F_22"]
SECI = {("up", "S"): 0, ("up", "St"): 2, ("down", "S"): 4, ("down", "St"): 6, ("lep", "S"): 8, ("lep", "St"): 10}
CKMI = {("S", "S"): 12, ("S", "St"): 16, ("St", "S"): 20, ("St", "St"): 24}
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


def rows(dirs, rd, c, lines=None):
    """rows (direction, point, horocycle) -> ln of the nine model values, J, labels; the same reading in every sector"""
    Ls, Js, lab = [], [], []
    pts = [p for p in range(len(TASKS)) if lines is None or LINES[TASKS[p][0]] in lines]
    for d in dirs:
        Y = X[pts][:, DIRS.index(d)]
        L = np.concatenate([Y[..., SECI[("up", rd)]:SECI[("up", rd)] + 2], Y[..., SECI[("down", rd)]:SECI[("down", rd)] + 2],
                            Y[..., SECI[("lep", rd)]:SECI[("lep", rd)] + 2]], axis=-1) * math.log(10)
        L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
        k = CKMI[(rd, rd)]
        L9 = np.concatenate([L, np.log(np.maximum(Y[..., k:k + 3], 1e-300))], axis=-1)
        Ls.append(L9.reshape(-1, 9)); Js.append(Y[..., k + 3].reshape(-1))
        lab += [(d, p, h) for p in pts for h in range(len(HORS))]
    return np.concatenate(Ls), np.concatenate(Js), lab


def where(l):
    d, p, h = l
    k, re_t, im_t = TASKS[p]
    return {"direction": d, "tau": [re_t, im_t], "line": LINES[k], "hor": HORS[h]}


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


def calibrate(L9, w6, w9):
    t6, t9 = cKDTree(L9[:, :6]), cKDTree(L9)
    f6, f9 = [], []
    for s in range(1720, 1740):
        rng = random.Random(s)
        d6 = np.log(np.array([r_masses(rng) for _ in range(4000)]))
        d9 = np.log(np.array([r_masses(rng) + r_ckm(rng) for _ in range(4000)]))
        q6, _ = t6.query(d6, k=1, p=np.inf); q9, _ = t9.query(d9, k=1, p=np.inf)
        f6.append(float(np.mean(q6 <= w6 + 1e-12))); f9.append(float(np.mean(q9 <= w9 + 1e-12)))
    return f6, f9


def best(L9, J, lab):
    six = np.max(np.abs(L9[:, :6] - T6), axis=1); nine = np.max(np.abs(L9 - T9), axis=1)
    i6, i9 = int(np.argmin(six)), int(np.argmin(nine))
    R2 = np.exp(L9[:, 4] - L9[:, 2]); R1 = np.exp(L9[:, 3] - L9[:, 5]); D = R2 * R1
    return {"six": math.exp(six[i6]), "six at": where(lab[i6]), "D at the best six-row": float(D[i6]), "R2, R1 there": [float(R2[i6]), float(R1[i6])],
            "six: model over measured": np.exp(L9[i6] - T9).round(3).tolist(), "nine at the best six-row": math.exp(nine[i6]),
            "nine": math.exp(nine[i9]), "nine at": where(lab[i9]), "J at the best nine-row": float(J[i9]),
            "nine: model over measured": np.exp(L9[i9] - T9).round(3).tolist(), "w6": float(six[i6]), "w9": float(nine[i9]),
            "rows": int(len(lab))}


# the cells
L9, J, lab = rows(MENU, "S", 3)
bS = best(L9, J, lab)
f6, f9 = calibrate(L9, bS["w6"], bS["w9"])
LT, JT, labT = rows(MENU, "St", 3)
bT = best(LT, JT, labT)
alpha = bS["six at"]["line"].split(",")[0].strip("(")
cells = {
    "K1 six within 2.0": bS["six"] <= 2.0,
    "K2 six specific (mean over 20 seeds <= 1%)": float(np.mean(f6)) <= 0.01,
    "K3 nine within 2.5": bS["nine"] <= 2.5,
    "K4 nine specific (<= 1%)": float(np.mean(f9)) <= 0.01,
    "K5 S beats S~ on both the six and the nine": bS["six"] < bT["six"] and bS["nine"] < bT["nine"],
    "K6 |J| within a factor 3 of 3.08e-5 at the best nine-row": JPDG / 3 <= abs(bS["J at the best nine-row"]) <= 3 * JPDG,
    "K7 the best six-row's line has alpha in {2/5, 3/5}": alpha in ("2/5", "3/5"),
    "C1 holds": bool(CTRL["C1 holds"]), "C2 holds": bool(CTRL["C2 holds"])}
OUT["cells"] = cells
OUT["menu, S, c = 3"] = {k: v for k, v in bS.items() if k not in ("w6", "w9")}
OUT["menu, S, c = 3: random as good (20 seeds)"] = {"six": f6, "nine": f9, "six mean": float(np.mean(f6)), "nine mean": float(np.mean(f9))}
OUT["menu, S~, c = 3 (K5)"] = {k: v for k, v in bT.items() if k not in ("w6", "w9")}
OUT["controls"] = CTRL
say(f"K1 six {bS['six']:.3f} at {bS['six at']} (nine there {bS['nine at the best six-row']:.3f}) -> {cells['K1 six within 2.0']}")
say(f"K2 random as good, six: mean {np.mean(f6):.4f} over 20 seeds (range {min(f6):.4f}-{max(f6):.4f}) -> {cells['K2 six specific (mean over 20 seeds <= 1%)']}")
say(f"K3 nine {bS['nine']:.3f} at {bS['nine at']} -> {cells['K3 nine within 2.5']}")
say(f"K4 random as good, nine: mean {np.mean(f9):.4f} (range {min(f9):.4f}-{max(f9):.4f}) -> {cells['K4 nine specific (<= 1%)']}")
say(f"K5 with S~: six {bT['six']:.3f}, nine {bT['nine']:.3f} -> {cells['K5 S beats S~ on both the six and the nine']}")
say(f"K6 J at the best nine-row {bS['J at the best nine-row']:.2e} -> {cells['K6 |J| within a factor 3 of 3.08e-5 at the best nine-row']}")
K7KEY = "K7 the best six-row's line has alpha in {2/5, 3/5}"
say(f"K7 the best six-row's line {bS['six at']['line']} -> {cells[K7KEY]}")
say(f"C1 {CTRL['C1 max |delta ln| against TC.ratios_at']:.2e} -> {cells['C1 holds']};  C2 {CTRL['C2 max |delta ln| under T (ratios, |V| above 1e-12), F_6 at the first grid point']} -> {cells['C2 holds']}")
say(f"P-094 (not a cell): D at the best six-row {bS['D at the best six-row']:.4f} (R2 {bS['R2, R1 there'][0]:.4f}, R1 {bS['R2, R1 there'][1]:.4f})")
say("model over measured at the best six-row: " + str(bS["six: model over measured"]))
say("model over measured at the best nine-row: " + str(bS["nine: model over measured"]))
say(f"menu rows: {bS['rows']}")

# read-outs (not cells)
OUT["read-outs"] = {}
for d in MENU:
    Ld, Jd, ld = rows([d], "S", 3); b = best(Ld, Jd, ld)
    OUT["read-outs"][f"{d}, S, c = 3"] = {k: v for k, v in b.items() if k not in ("w6", "w9")}
    say(f"read-out {d}, S, c = 3: six {b['six']:.3f} at {b['six at']}; nine {b['nine']:.3f} at {b['nine at']}")
for ln in LINES:
    Ll, Jl, ll = rows(MENU, "S", 3, lines=[ln]); b = best(Ll, Jl, ll)
    OUT["read-outs"][f"menu on {ln} alone, S, c = 3"] = {k: v for k, v in b.items() if k not in ("w6", "w9")}
    say(f"read-out menu on {ln}: six {b['six']:.3f} at tau {b['six at']['tau']} {b['six at']['hor']} ({b['six at']['direction']}); nine {b['nine']:.3f} at tau {b['nine at']['tau']}")
Lr, Jr, lr = rows(MENU, "S", 1); b = best(Lr, Jr, lr)
OUT["read-outs"]["menu, S, c = 1"] = {k: v for k, v in b.items() if k not in ("w6", "w9")}
say(f"read-out menu, S, c = 1: six {b['six']:.3f} at {b['six at']}; nine {b['nine']:.3f} at {b['nine at']}")
for label, c in (("DR with S~, c = 3 (the sealed census's model)", 3), ("DR with S~, c = 1", 1)):
    Lr, Jr, lr = rows(["dR"], "St", c); b = best(Lr, Jr, lr)
    g6, g9 = calibrate(Lr, b["w6"], b["w9"])
    rec = {k: v for k, v in b.items() if k not in ("w6", "w9")}
    rec["random as good, mean of 20 seeds"] = [float(np.mean(g6)), float(np.mean(g9))]
    OUT["read-outs"][label] = rec
    say(f"read-out {label}: six {b['six']:.3f} at {b['six at']}; nine {b['nine']:.3f} at {b['nine at']}; random as good {np.mean(g6):.4f} / {np.mean(g9):.4f}")
(HERE / "tick_line_compare.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "tick_line_compare_run.txt").write_text("\n".join(LOG) + "\n")
