#!/usr/bin/env python3
"""ZERO_FREE_HOLOMORPHIC's comparison (sealed rule: ZERO_FREE_HOLOMORPHIC_RULE.md, 38e2b8062; committed before the
outputs it reads exist).  Cells Z1-Z8 and controls C1-C2 exactly as the rule states them, then the read-outs.
    python3 -B zero_free_holomorphic_compare.py      # writes zero_free_holomorphic_compare.json and _run.txt"""
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
P094, SIG, JPDG = 10.58, 0.11, 3.08e-5
IDX = json.loads((HERE / "zero_free_holomorphic_index.json").read_text())
X = np.load(HERE / "zero_free_holomorphic.npz")["data"].astype(np.float64)     # point, dir, hor, field
CTRL = json.loads((HERE / "zero_free_holomorphic_controls.json").read_text())
TASKS = IDX["tasks"]; LINES = IDX["lines"]; DIRS = IDX["dirs"]; HORS = IDX["hors"]
MENU = ["F_6", "F_-2", "F_22"]
SECI = {("up", "S"): 0, ("up", "St"): 2, ("down", "S"): 4, ("down", "St"): 6, ("lep", "S"): 8, ("lep", "St"): 10}
CKMI = {("S", "S"): 12, ("S", "St"): 16, ("St", "S"): 20, ("St", "St"): 24}
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


def rows(dirs, rd, c):
    """menu rows (direction, point, horocycle) -> ln of the nine model values, J, labels; the same reading in every sector"""
    Ls, Js, lab = [], [], []
    for d in dirs:
        Y = X[:, DIRS.index(d)]
        L = np.concatenate([Y[..., SECI[("up", rd)]:SECI[("up", rd)] + 2], Y[..., SECI[("down", rd)]:SECI[("down", rd)] + 2],
                            Y[..., SECI[("lep", rd)]:SECI[("lep", rd)] + 2]], axis=-1) * math.log(10)
        L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
        k = CKMI[(rd, rd)]
        L9 = np.concatenate([L, np.log(np.maximum(Y[..., k:k + 3], 1e-300))], axis=-1)
        Ls.append(L9.reshape(-1, 9)); Js.append(Y[..., k + 3].reshape(-1))
        lab += [(d, p, h) for p in range(len(TASKS)) for h in range(len(HORS))]
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
            "six: model over measured": np.exp(L9[i6] - T9).round(3).tolist(),
            "nine": math.exp(nine[i9]), "nine at": where(lab[i9]), "J at the best nine-row": float(J[i9]),
            "nine: model over measured": np.exp(L9[i9] - T9).round(3).tolist(), "w6": float(six[i6]), "w9": float(nine[i9])}


# the cells
L9, J, lab = rows(MENU, "S", 3)
bS = best(L9, J, lab)
f6, f9 = calibrate(L9, bS["w6"], bS["w9"])
LT, JT, labT = rows(MENU, "St", 3)
bT = best(LT, JT, labT)
alpha = bS["six at"]["line"].split(",")[0].strip("(")
cells = {
    "Z1 six within 2.0": bS["six"] <= 2.0,
    "Z2 six specific (mean over 20 seeds <= 1%)": float(np.mean(f6)) <= 0.01,
    "Z3 nine within 2.5": bS["nine"] <= 2.5,
    "Z4 nine specific (<= 1%)": float(np.mean(f9)) <= 0.01,
    "Z5 D within 3 sigma of 10.58 at the best six-row": abs(bS["D at the best six-row"] - P094) <= 3 * SIG,
    "Z6 |J| within a factor 3 of 3.08e-5 at the best nine-row": JPDG / 3 <= abs(bS["J at the best nine-row"]) <= 3 * JPDG,
    "Z7 S beats S~ on both the six and the nine": bS["six"] < bT["six"] and bS["nine"] < bT["nine"],
    "Z8 the best six-row's line has alpha = 2/5": alpha == "2/5",
    "C1 holds": bool(CTRL["C1 holds"]), "C2 holds": bool(CTRL["C2 holds"])}
OUT["cells"] = cells
OUT["menu, S, c = 3"] = {k: v for k, v in bS.items() if k not in ("w6", "w9")}
OUT["menu, S, c = 3: random as good (20 seeds)"] = {"six": f6, "nine": f9, "six mean": float(np.mean(f6)), "nine mean": float(np.mean(f9))}
OUT["menu, S~, c = 3 (Z7)"] = {k: v for k, v in bT.items() if k not in ("w6", "w9")}
OUT["controls"] = CTRL
say(f"Z1 six {bS['six']:.3f} at {bS['six at']} -> {cells['Z1 six within 2.0']}")
say(f"Z2 random as good, six: mean {np.mean(f6):.4f} over 20 seeds (range {min(f6):.4f}-{max(f6):.4f}) -> {cells['Z2 six specific (mean over 20 seeds <= 1%)']}")
say(f"Z3 nine {bS['nine']:.3f} at {bS['nine at']} -> {cells['Z3 nine within 2.5']}")
say(f"Z4 random as good, nine: mean {np.mean(f9):.4f} (range {min(f9):.4f}-{max(f9):.4f}) -> {cells['Z4 nine specific (<= 1%)']}")
say(f"Z5 D at the best six-row {bS['D at the best six-row']:.3f} (R2 {bS['R2, R1 there'][0]:.3f}, R1 {bS['R2, R1 there'][1]:.3f}) -> {cells['Z5 D within 3 sigma of 10.58 at the best six-row']}")
say(f"Z6 J at the best nine-row {bS['J at the best nine-row']:.2e} -> {cells['Z6 |J| within a factor 3 of 3.08e-5 at the best nine-row']}")
say(f"Z7 with S~: six {bT['six']:.3f}, nine {bT['nine']:.3f} -> {cells['Z7 S beats S~ on both the six and the nine']}")
z8 = cells["Z8 the best six-row's line has alpha = 2/5"]
say(f"Z8 the best six-row's line {bS['six at']['line']} -> {z8}")
say(f"C1 {CTRL['C1 max |delta ln| against TC.ratios_at']:.2e} -> {cells['C1 holds']};  C2 {CTRL['C2 max |delta ln| under T (ratios, |V|), F_6 at the first grid point']} -> {cells['C2 holds']}")
say("model over measured at the best six-row: " + str(bS["six: model over measured"]))
say("model over measured at the best nine-row: " + str(bS["nine: model over measured"]))

# read-outs (not cells)
OUT["read-outs"] = {}
for label, dirs, rd, c in (("each menu line alone, S, c = 3", None, "S", 3), ("menu, S, c = 1", MENU, "S", 1),
                           ("the reference: DR with S~, c = 3 (the sealed census's model)", ["dR"], "St", 3),
                           ("the reference without the factor: DR with S~, c = 1", ["dR"], "St", 1)):
    if dirs is None:
        for d in MENU:
            Ld, Jd, ld = rows([d], rd, c); b = best(Ld, Jd, ld)
            OUT["read-outs"][f"{d}, S, c = 3"] = {k: v for k, v in b.items() if k not in ("w6", "w9")}
            say(f"read-out {d}, S, c = 3: six {b['six']:.3f} at {b['six at']}; nine {b['nine']:.3f} at {b['nine at']}; D at the best six-row {b['D at the best six-row']:.2f}")
        continue
    Lr, Jr, lr = rows(dirs, rd, c); b = best(Lr, Jr, lr)
    rec = {k: v for k, v in b.items() if k not in ("w6", "w9")}
    if "DR" in label:
        g6, g9 = calibrate(Lr, b["w6"], b["w9"]); rec["random as good, mean of 20 seeds"] = [float(np.mean(g6)), float(np.mean(g9))]
    OUT["read-outs"][label] = rec
    say(f"read-out {label}: six {b['six']:.3f} at {b['six at']}; nine {b['nine']:.3f} at {b['nine at']}; D at the best six-row {b['D at the best six-row']:.2f}"
        + (f"; random as good {np.mean(g6):.4f} / {np.mean(g9):.4f}" if "DR" in label else ""))
(HERE / "zero_free_holomorphic_compare.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "zero_free_holomorphic_compare_run.txt").write_text("\n".join(LOG) + "\n")
