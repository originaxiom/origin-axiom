#!/usr/bin/env python3
"""POST HOC read-outs, labelled (ZERO_FREE_HOLOMORPHIC: written after its sealed cells were read; committed before its
own run).  None is a cell.
  P1  precision: PRECISION_BAR.md's chi-square (sealed after this rule, so a read-out here) for the menu read S with
      c = 3 and for the reference DR read S~ with c = 3: the minima and their rows;
  P2  the tick's lines alone on this grid (B1698's S1 and S2; four in the list up to sign): the menu's best six and nine
      there and random as good (20 seeds), against TICK_LINE_HIGGS's 1.551 at 0.15% and 2.043 at 0.11% on its own
      grid; the same for the reference; F_6 alone on all lines;
  P3  CP: among the rows that fit the nine within 3 (and 2.5), the largest |J| and how many lie within a factor 3 of
      3.08e-5; the median |J| over all rows; for the menu and the reference.
    python3 -B zero_free_holomorphic_posthoc.py      # writes zero_free_holomorphic_posthoc.json"""
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
m = json.loads(bd)["masses_GeV"]; v, s = m["value"], m["sigma"]; ck = json.loads(bc)["ckm_abs"]; C, CS = ck["value"], ck["sigma"]
PAIRS = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T6 = np.log(np.array([v[a] / v[b] for a, b in PAIRS]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
REL = np.array([math.hypot(s[a] / v[a], s[b] / v[b]) for a, b in PAIRS] + [CS[0][1] / C[0][1], CS[1][2] / C[1][2], CS[0][2] / C[0][2]])
SIG = np.sqrt(REL ** 2 + 0.10 ** 2)                                        # PRECISION_BAR.md: main's definition
JPDG = 3.08e-5
IDX = json.loads((HERE / "zero_free_holomorphic_index.json").read_text())
X = np.load(HERE / "zero_free_holomorphic.npz")["data"].astype(np.float64)
TASKS = IDX["tasks"]; LINES = IDX["lines"]; DIRS = IDX["dirs"]; HORS = IDX["hors"]
MENU = ["F_6", "F_-2", "F_22"]
SECI = {"S": (0, 4, 8), "St": (2, 6, 10)}
CKMI = {"S": 12, "St": 24}
TICK = ["(1/5, 2/5)", "(2/5, 4/5)", "(1/5, 3/5)", "(2/5, 1/5)"]
OUT = {}


def rows(dirs, rd, c, sel=None):
    sel = list(range(len(TASKS))) if sel is None else sel
    Ls, Js, lab = [], [], []
    for d in dirs:
        Y = X[sel][:, DIRS.index(d)]
        iu, idn, il = SECI[rd]
        L = np.concatenate([Y[..., iu:iu + 2], Y[..., idn:idn + 2], Y[..., il:il + 2]], axis=-1) * math.log(10)
        L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
        k = CKMI[rd]
        L9 = np.concatenate([L, np.log(np.maximum(Y[..., k:k + 3], 1e-300))], axis=-1)
        Ls.append(L9.reshape(-1, 9)); Js.append(Y[..., k + 3].reshape(-1))
        lab += [(d, p, h) for p in sel for h in range(len(HORS))]
    return np.concatenate(Ls), np.concatenate(Js), lab


def where(l):
    d, p, h = l
    k, re_t, im_t = TASKS[p]
    return f"{d} at {re_t} + {im_t}i on {LINES[k]}, {HORS[h]}"


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


def summary(L9, J, lab, calibrate=True):
    six = np.max(np.abs(L9[:, :6] - T6), axis=1); nine = np.max(np.abs(L9 - T9), axis=1)
    chi6 = np.sum(((L9[:, :6] - T6) / SIG[:6]) ** 2, axis=1); chi9 = np.sum(((L9 - T9) / SIG) ** 2, axis=1)
    i6, i9, c6, c9 = int(np.argmin(six)), int(np.argmin(nine)), int(np.argmin(chi6)), int(np.argmin(chi9))
    out = {"rows": int(len(L9)), "six": math.exp(six[i6]), "six at": where(lab[i6]),
           "nine": math.exp(nine[i9]), "nine at": where(lab[i9]), "J at the best nine-row": float(J[i9]),
           "chi2_six at the best six-row": float(chi6[i6]), "chi2_nine at the best nine-row": float(chi9[i9]),
           "min chi2_six": float(chi6[c6]), "min chi2_six at": where(lab[c6]),
           "min chi2_nine": float(chi9[c9]), "min chi2_nine at": where(lab[c9]),
           "model over measured at the min chi2_nine row": np.exp(L9[c9] - T9).round(3).tolist()}
    for cut in (2.5, 3.0):
        g = nine <= math.log(cut)
        out[f"rows with nine <= {cut}"] = int(g.sum())
        if g.any():
            k = int(np.argmax(np.where(g, np.abs(J), -1)))
            out[f"max |J| among them ({cut})"] = float(abs(J[k])); out[f"its row ({cut})"] = where(lab[k])
            out[f"its nine ({cut})"] = math.exp(nine[k])
            out[f"rows among them with |J| within a factor 3 of 3.08e-5 ({cut})"] = int((g & (np.abs(J) >= JPDG / 3) & (np.abs(J) <= 3 * JPDG)).sum())
    out["median |J| over all rows"] = float(np.median(np.abs(J)))
    if calibrate:
        t6, t9 = cKDTree(L9[:, :6]), cKDTree(L9)
        f6, f9 = [], []
        for d6, d9 in TG:
            q6, _ = t6.query(d6, k=1, p=np.inf); q9, _ = t9.query(d9, k=1, p=np.inf)
            f6.append(float(np.mean(q6 <= six[i6] + 1e-12))); f9.append(float(np.mean(q9 <= nine[i9] + 1e-12)))
        out["random as good, mean of 20 seeds (six, nine)"] = [float(np.mean(f6)), float(np.mean(f9))]
        out["range (six)"] = [min(f6), max(f6)]; out["range (nine)"] = [min(f9), max(f9)]
    return out


tick_sel = [p for p, (k, re_t, im_t) in enumerate(TASKS) if LINES[k] in TICK]
OUT["P1 and P3: the menu, S, c = 3, all lines"] = summary(*rows(MENU, "S", 3))
OUT["P1 and P3: the reference DR, S~, c = 3, all lines"] = summary(*rows(["dR"], "St", 3))
OUT["P2: the menu, S, c = 3, the tick's lines"] = summary(*rows(MENU, "S", 3, tick_sel))
OUT["P2: the reference DR, S~, c = 3, the tick's lines"] = summary(*rows(["dR"], "St", 3, tick_sel))
OUT["P2: F_6 alone, S, c = 3, all lines"] = summary(*rows(["F_6"], "S", 3))
OUT["P2: points on the tick's lines"] = len(tick_sel)
(HERE / "zero_free_holomorphic_posthoc.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
