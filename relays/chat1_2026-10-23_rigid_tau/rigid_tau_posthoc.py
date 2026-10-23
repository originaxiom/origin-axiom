#!/usr/bin/env python3
"""POST HOC read-outs, labelled (RIGID_TAU_HOLOMORPHIC: written after the sealed cells and the referee's report were
read; committed before its own run).  They check the referee's points before the result note states them; none is a cell.
  R1  the best rows moved to 0 <= Re tau < 1 (tau -> tau - n, b -> b + n alpha), and whether the moved line is the tick's;
  R2  main's DR at c = 3 on the same 3 249 points, calibrated the same way (20 seeds): the split reading (up S~, down and
      leptons S), up S or S~ pooled, S in every sector, S~ in every sector (THREADS_WITH_INGREDIENTS's model);
  R3  the menu at c = 1, calibrated with its own best widths; the menu's sensitivity to its model space (S and S~ rows;
      menu and DR rows; F_22 alone);
  R4  CP: the family-A points whose configuration maps to itself under tau -> -conj(tau), b -> -b (up to T, sign and
      integer shifts), the largest |J| there, and the largest |J| among menu rows with nine <= 5;
  R5  rows meeting both A1's and A3's bars; chi2_nine at the best nine-row;
  R6  TICK_LINE_HIGGS's grid points nearest the moved best six-row (read before the rule);
  R7  the instrument at the best nine-row's moved configuration with Re tau moved off 0, and at the best six-row's with
      Re tau moved off 1/2 (main's frame, recomputed).
    python3 -B rigid_tau_posthoc.py      # writes rigid_tau_posthoc.json"""
import contextlib, hashlib, importlib.util, io, json, math, random, subprocess, sys, pathlib
from fractions import Fraction as Fr
import numpy as np
from scipy.spatial import cKDTree

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
TL = HERE.parent / "chat1_2026-10-23_tick_line"


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
m = json.loads(bd)["masses_GeV"]; v, s = m["value"], m["sigma"]; ck = json.loads(bc)["ckm_abs"]; C, CS = ck["value"], ck["sigma"]
PAIRS = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T6 = np.log(np.array([v[a] / v[b] for a, b in PAIRS]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
REL = np.array([math.hypot(s[a] / v[a], s[b] / v[b]) for a, b in PAIRS] + [CS[0][1] / C[0][1], CS[1][2] / C[1][2], CS[0][2] / C[0][2]])
SIG = np.sqrt(REL ** 2 + 0.10 ** 2)
JPDG = 3.08e-5
IDX = json.loads((HERE / "rigid_tau_index.json").read_text())
X = np.load(HERE / "rigid_tau.npz")["data"].astype(np.float64)
PTS = IDX["points"]; DIRS = IDX["dirs"]; HORS = IDX["hors"]
MENU = ["F_6", "F_-2", "F_22"]
SECI = {"S": (0, 4, 8), "St": (2, 6, 10)}
CKMI = {("S", "S"): 12, ("S", "St"): 16, ("St", "S"): 20, ("St", "St"): 24}
A = [i for i, p in enumerate(PTS) if p[0] == "A"]
OUT = {}


def rows(dirs, ru, rd, c, sel, X=X, nh=2):
    Ls, Js, lab = [], [], []
    for d in dirs:
        Y = X[sel][:, DIRS.index(d)]
        iu, idn, il = SECI[ru][0], SECI[rd][1], SECI[rd][2]
        L = np.concatenate([Y[..., iu:iu + 2], Y[..., idn:idn + 2], Y[..., il:il + 2]], axis=-1) * math.log(10)
        L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
        k = CKMI[(ru, rd)]
        L9 = np.concatenate([L, np.log(np.maximum(Y[..., k:k + 3], 1e-300))], axis=-1)
        Ls.append(L9.reshape(-1, 9)); Js.append(Y[..., k + 3].reshape(-1))
        lab += [(d, int(p), h, ru, rd) for p in sel for h in range(nh)]
    return np.concatenate(Ls), np.concatenate(Js), lab


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


def calib(L9):
    six = np.max(np.abs(L9[:, :6] - T6), axis=1); nine = np.max(np.abs(L9 - T9), axis=1)
    w6, w9 = float(six.min()), float(nine.min())
    t6, t9 = cKDTree(L9[:, :6]), cKDTree(L9)
    f6, f9 = [], []
    for d6, d9 in TG:
        q6, _ = t6.query(d6, k=1, p=np.inf); q9, _ = t9.query(d9, k=1, p=np.inf)
        f6.append(float(np.mean(q6 <= w6 + 1e-12))); f9.append(float(np.mean(q9 <= w9 + 1e-12)))
    return {"rows": int(len(L9)), "six": math.exp(w6), "nine": math.exp(w9),
            "six as good, mean of 20 seeds": float(np.mean(f6)), "seed 1720": f6[0], "range": [min(f6), max(f6)],
            "nine as good, mean of 20 seeds": float(np.mean(f9)), "seed 1720 (nine)": f9[0], "range (nine)": [min(f9), max(f9)],
            "standard error of the mean (six, nine)": [float(np.std(f6, ddof=1) / math.sqrt(20)), float(np.std(f9, ddof=1) / math.sqrt(20))]}


def stack(*parts):
    return (np.concatenate([p[0] for p in parts]), np.concatenate([p[1] for p in parts]), sum((p[2] for p in parts), []))


# the sealed best rows, recomputed
L9, J, lab = rows(MENU, "S", "S", 3, A)
six = np.max(np.abs(L9[:, :6] - T6), axis=1); nine = np.max(np.abs(L9 - T9), axis=1)
chi9 = np.sum(((L9 - T9) / SIG) ** 2, axis=1)
i6, i9 = int(np.argmin(six)), int(np.argmin(nine))


def moved(p):
    f, label, re_t, im_t, a, b = PTS[p]
    n = math.floor(re_t + 1e-9); a, b = Fr(a), Fr(b)
    b2 = (b + n * a) % 1
    return n, re_t - n, im_t, a, b2


TICK = {(Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5)), (Fr(4, 5), Fr(3, 5)),
        (Fr(1, 5), Fr(3, 5)), (Fr(2, 5), Fr(1, 5)), (Fr(3, 5), Fr(4, 5)), (Fr(4, 5), Fr(2, 5))}


def on_tick(a, b):
    return (a % 1, b % 1) in TICK or ((-a) % 1, (-b) % 1) in TICK


R1 = {}
for name, i in (("best six-row", i6), ("best nine-row", i9)):
    d, p, h, _, _ = lab[i]
    n, re_m, im_m, a, b2 = moved(p)
    R1[name] = {"as stored": PTS[p][1], "tau as stored": PTS[p][2:4], "direction": d, "horocycle": HORS[h],
                "moved by": n, "moved tau": [re_m, im_m], "moved line": f"({a}, {b2})", "moved line is the tick's": on_tick(a, b2),
                "six": math.exp(six[i]), "nine": math.exp(nine[i]), "J": float(J[i]), "chi2_nine": float(chi9[i])}
OUT["R1 the best rows moved"] = R1

# R2 DR at c = 3 on the same points
dr_split = rows(["dR"], "St", "S", 3, A)
dr_S = rows(["dR"], "S", "S", 3, A)
dr_St = rows(["dR"], "St", "St", 3, A)
OUT["R2 DR, c = 3, family A"] = {
    "split (up S~, down and leptons S)": calib(dr_split[0]),
    "up S or S~ pooled (down and leptons S)": calib(stack(dr_split, dr_S)[0]),
    "S in every sector": calib(dr_S[0]),
    "S~ in every sector (THREADS_WITH_INGREDIENTS's model)": calib(dr_St[0])}

# R3 the menu at c = 1, and the menu's model space
menu_c1 = rows(MENU, "S", "S", 1, A)
menu_St = rows(MENU, "St", "St", 3, A)
OUT["R3 the menu's specificity"] = {
    "sealed (menu, S, c = 3), recomputed": calib(L9),
    "menu, S, c = 1": calib(menu_c1[0]),
    "menu, S and S~ rows, c = 3": calib(stack((L9, J, lab), menu_St)[0]),
    "menu and DR (split) rows, c = 3": calib(stack((L9, J, lab), dr_split)[0]),
    "F_22 alone, S, c = 3": calib(rows(["F_22"], "S", "S", 3, A)[0])}

# R4 CP
selfc = []
for p in A:
    f, label, re_t, im_t, a, b = PTS[p]
    a, b = Fr(a), Fr(b)
    n2 = 2 * re_t
    if abs(n2 - round(n2)) > 1e-9:
        continue
    n = int(round(n2))
    bb = (-b - n * a)                                   # the CP image (a, -b) moved back by T^n
    plus = ((bb - b) % 1 == 0)
    minus = ((2 * a) % 1 == 0) and ((bb + b) % 1 == 0)
    if plus or minus:
        selfc.append(p)
Jabs = np.abs(J).reshape(len(MENU), len(A), 2)
pos = {p: k for k, p in enumerate(A)}
sc_idx = [pos[p] for p in selfc]
good = nine <= math.log(5)
OUT["R4 CP"] = {"self-conjugate family-A points": len(selfc), "of": len(A),
                "max |J| there (menu, S, c = 3)": float(Jabs[:, sc_idx, :].max()) if sc_idx else None,
                "best six-row and best nine-row self-conjugate": [lab[i6][1] in selfc, lab[i9][1] in selfc],
                "menu rows with nine <= 5": int(good.sum()),
                "max |J| among them": float(np.abs(J[good]).max()),
                "median |J| over the other points (F_22, S, c = 3)": float(np.median(
                    Jabs[MENU.index("F_22"), [k for k in range(len(A)) if A[k] not in set(selfc)], :]))}

# R5 both bars
both = (six <= math.log(2.0)) & (nine <= math.log(2.5))
OUT["R5 both bars"] = {"rows with six <= 2.0": int((six <= math.log(2.0)).sum()), "rows with nine <= 2.5": int((nine <= math.log(2.5)).sum()),
                       "rows with both": int(both.sum()),
                       "six at the best nine-row": math.exp(six[i9]), "nine at the best six-row": math.exp(nine[i6]),
                       "which rows have six <= 2.0": [PTS[lab[i][1]][1] + f" {lab[i][0]} {HORS[lab[i][2]]}" for i in np.where(six <= math.log(2.0))[0]],
                       "which rows have nine <= 2.5": [PTS[lab[i][1]][1] + f" {lab[i][0]} {HORS[lab[i][2]]}" for i in np.where(nine <= math.log(2.5))[0]],
                       "chi2_nine at the best nine-row": float(chi9[i9]), "min chi2_nine": float(chi9.min())}

# R6 TICK_LINE_HIGGS's grid neighbours of the moved best six-row
TI = json.loads((TL / "tick_line_index.json").read_text()); TX = np.load(TL / "tick_line.npz")["data"].astype(np.float64)
li = TI["lines"].index("(2/5, 4/5)")
near = []
for t, (l, re_t, im_t) in enumerate(TI["tasks"]):
    if l == li and abs(im_t - 2.725) < 1e-9 and abs(re_t - 0.5) < 0.03:
        for h in range(2):
            Y = TX[t, TI["dirs"].index("F_22"), h]
            Lr = np.array([Y[0], Y[1], Y[4], Y[5], Y[8], Y[9]]) * math.log(10)
            Lr[4] += math.log(3); Lr[5] -= math.log(3)
            near.append({"tau": [re_t, im_t], "hor": TI["hors"][h], "six": math.exp(float(np.max(np.abs(Lr - T6))))})
OUT["R6 TICK_LINE_HIGGS's grid points beside the moved best six-row (F_22, S, c = 3)"] = near

# R7 the instrument off the symmetric points
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("rtt", HERE / "rigid_tau_test.py")
rtt = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rtt)
zfc, rbs = rtt.zfc, rtt.rbs


def evaluate(re_t, im_t, a, b, d, h):
    x = zfc.rows_at(rbs.channels(re_t, im_t, float(a), float(b)), zfc.direction(d, re_t, im_t))[h]
    Lr = np.array([x[0], x[1], x[4], x[5], x[8], x[9]]) * math.log(10)
    Lr[4] += math.log(3); Lr[5] -= math.log(3)
    L9r = np.concatenate([Lr, np.log(np.maximum(x[12:15], 1e-300))])
    return {"Re tau": re_t, "six": math.exp(float(np.max(np.abs(Lr - T6)))), "nine": math.exp(float(np.max(np.abs(L9r - T9)))),
            "J": float(x[15]), "model over measured": np.exp(L9r - T9).round(3).tolist()}


R7 = {}
for name, i, offs in (("best nine-row", i9, (0.0, 0.01, 0.02, 0.05)), ("best six-row", i6, (0.0, 0.01, 0.02, 0.05))):
    d, p, h, _, _ = lab[i]
    n, re_m, im_m, a, b2 = moved(p)
    R7[name] = {"moved configuration": [re_m, im_m, f"({a}, {b2})", d, HORS[h]],
                "scan": [evaluate(re_m + o, im_m, a, b2, d, h) for o in offs]}
OUT["R7 off the symmetric points"] = R7
(HERE / "rigid_tau_posthoc.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
print("written")
