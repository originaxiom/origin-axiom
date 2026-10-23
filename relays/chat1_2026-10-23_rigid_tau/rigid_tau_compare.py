#!/usr/bin/env python3
"""RIGID_TAU_HOLOMORPHIC's comparison (sealed rule: RIGID_TAU_HOLOMORPHIC_RULE.md, 51b05f7c7; committed before the
outputs it reads exist).  Cells A1-A9, B1-B2 and controls C1-C3 exactly as the rule states them, then the read-outs.
    python3 -B rigid_tau_compare.py      # writes rigid_tau_compare.json and rigid_tau_compare_run.txt"""
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
SIG = np.sqrt(REL ** 2 + 0.10 ** 2)                                         # PRECISION_BAR.md: main's definition
P094, PSIG, JPDG = 10.58, 0.11, 3.08e-5
IDX = json.loads((HERE / "rigid_tau_index.json").read_text())
X = np.load(HERE / "rigid_tau.npz")["data"].astype(np.float64)              # point, dir, hor, field
CTRL = json.loads((HERE / "rigid_tau_controls.json").read_text())
PTS = IDX["points"]; DIRS = IDX["dirs"]; HORS = IDX["hors"]
MENU = ["F_6", "F_-2", "F_22"]
SECI = {"S": (0, 4, 8), "St": (2, 6, 10)}
CKMI = {("S", "S"): 12, ("S", "St"): 16, ("St", "S"): 20, ("St", "St"): 24}
LOG, OUT = [], {}


def say(x):
    LOG.append(x); print(x, flush=True)


def rows(dirs, ru, rd, c, sel):
    """rows over the selected points -> ln nine, J, labels; up read ru, down and leptons read rd"""
    Ls, Js, lab = [], [], []
    for d in dirs:
        Y = X[sel][:, DIRS.index(d)]
        iu, idn, il = SECI[ru][0], SECI[rd][1], SECI[rd][2]
        L = np.concatenate([Y[..., iu:iu + 2], Y[..., idn:idn + 2], Y[..., il:il + 2]], axis=-1) * math.log(10)
        L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
        k = CKMI[(ru, rd)]
        L9 = np.concatenate([L, np.log(np.maximum(Y[..., k:k + 3], 1e-300))], axis=-1)
        Ls.append(L9.reshape(-1, 9)); Js.append(Y[..., k + 3].reshape(-1))
        lab += [(d, int(p), h) for p in sel for h in range(len(HORS))]
    return np.concatenate(Ls), np.concatenate(Js), lab


def where(l):
    d, p, h = l
    f, label, re_t, im_t, a, b = PTS[p]
    return {"direction": d, "point": label, "tau": [re_t, im_t], "hor": HORS[h]}


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
    for sd in range(1720, 1740):
        rng = random.Random(sd)
        d6 = np.log(np.array([r_masses(rng) for _ in range(4000)]))
        d9 = np.log(np.array([r_masses(rng) + r_ckm(rng) for _ in range(4000)]))
        q6, _ = t6.query(d6, k=1, p=np.inf); q9, _ = t9.query(d9, k=1, p=np.inf)
        f6.append(float(np.mean(q6 <= w6 + 1e-12))); f9.append(float(np.mean(q9 <= w9 + 1e-12)))
    return f6, f9


def best(L9, J, lab):
    six = np.max(np.abs(L9[:, :6] - T6), axis=1); nine = np.max(np.abs(L9 - T9), axis=1)
    chi6 = np.sum(((L9[:, :6] - T6) / SIG[:6]) ** 2, axis=1); chi9 = np.sum(((L9 - T9) / SIG) ** 2, axis=1)
    i6, i9, c6, c9 = int(np.argmin(six)), int(np.argmin(nine)), int(np.argmin(chi6)), int(np.argmin(chi9))
    R2 = np.exp(L9[:, 4] - L9[:, 2]); R1 = np.exp(L9[:, 3] - L9[:, 5])
    return {"six": math.exp(six[i6]), "six at": where(lab[i6]), "nine at the best six-row": math.exp(nine[i6]),
            "D at the best six-row": float(R2[i6] * R1[i6]), "six: model over measured": np.exp(L9[i6] - T9).round(3).tolist(),
            "nine": math.exp(nine[i9]), "nine at": where(lab[i9]), "J at the best nine-row": float(J[i9]),
            "nine: model over measured": np.exp(L9[i9] - T9).round(3).tolist(),
            "min chi2_six": float(chi6[c6]), "min chi2_six at": where(lab[c6]), "min chi2_nine": float(chi9[c9]),
            "min chi2_nine at": where(lab[c9]), "w6": float(six[i6]), "w9": float(nine[i9]), "rows": len(lab)}


A = [i for i, p in enumerate(PTS) if p[0] == "A"]
B_cusp = [i for i, p in enumerate(PTS) if p[0] == "B" and p[1].startswith("2 sqrt3 i")]
B_end = [i for i, p in enumerate(PTS) if p[0] == "B" and p[1].startswith("1/2 + sqrt3 i")]
L9, J, lab = rows(MENU, "S", "S", 3, A)
bS = best(L9, J, lab)
f6, f9 = calibrate(L9, bS["w6"], bS["w9"])
LT, JT, labT = rows(MENU, "St", "St", 3, A)
bT = best(LT, JT, labT)
bB1 = best(*rows(MENU, "S", "S", 3, B_cusp)); bB2 = best(*rows(MENU, "S", "S", 3, B_end))
cells = {
    "A1 six within 2.0": bS["six"] <= 2.0,
    "A2 six specific (mean over 20 seeds <= 1%)": float(np.mean(f6)) <= 0.01,
    "A3 nine within 2.5": bS["nine"] <= 2.5,
    "A4 nine specific (<= 1%)": float(np.mean(f9)) <= 0.01,
    "A5 min chi2_six below 16.75": bS["min chi2_six"] < 16.75,
    "A6 min chi2_nine below 21.67": bS["min chi2_nine"] < 21.67,
    "A7 S beats S~ on both the six and the nine": bS["six"] < bT["six"] and bS["nine"] < bT["nine"],
    "A8 |J| within a factor 3 of 3.08e-5 at the best nine-row": JPDG / 3 <= abs(bS["J at the best nine-row"]) <= 3 * JPDG,
    "A9 D within 3 sigma of P-094 at the best six-row": abs(bS["D at the best six-row"] - P094) <= 3 * PSIG,
    "B1 tau = 2 sqrt3 i: six within 2.0": bB1["six"] <= 2.0,
    "B2 tau = 1/2 + sqrt3 i: six within 2.0": bB2["six"] <= 2.0,
    "C1 holds": bool(CTRL["C1 holds"]), "C2 holds": bool(CTRL["C2 holds"]), "C3 holds": bool(CTRL["C3 holds"])}
OUT["cells"] = cells
OUT["family A, menu, S, c = 3"] = {k: x for k, x in bS.items() if k not in ("w6", "w9")}
OUT["family A: random as good (20 seeds)"] = {"six": f6, "nine": f9, "six mean": float(np.mean(f6)), "nine mean": float(np.mean(f9))}
OUT["family A, menu, S~, c = 3 (A7)"] = {k: x for k, x in bT.items() if k not in ("w6", "w9")}
OUT["family B, 2 sqrt3 i"] = {k: x for k, x in bB1.items() if k not in ("w6", "w9")}
OUT["family B, 1/2 + sqrt3 i"] = {k: x for k, x in bB2.items() if k not in ("w6", "w9")}
OUT["controls"] = CTRL
for key, ok in cells.items():
    say(f"{key}: {ok}")
say(f"A: six {bS['six']:.3f} at {bS['six at']} (nine there {bS['nine at the best six-row']:.3f}; D {bS['D at the best six-row']:.3f})")
say(f"A: nine {bS['nine']:.3f} at {bS['nine at']} (J {bS['J at the best nine-row']:.2e})")
say(f"A: random as good six {np.mean(f6):.4f} ({min(f6):.4f}-{max(f6):.4f}), nine {np.mean(f9):.4f} ({min(f9):.4f}-{max(f9):.4f})")
say(f"A: min chi2_six {bS['min chi2_six']:.1f} at {bS['min chi2_six at']}; min chi2_nine {bS['min chi2_nine']:.1f} at {bS['min chi2_nine at']}")
say(f"A with S~: six {bT['six']:.3f}, nine {bT['nine']:.3f}")
say(f"B 2 sqrt3 i: six {bB1['six']:.3f} at {bB1['six at']}; nine {bB1['nine']:.3f}; min chi2_six {bB1['min chi2_six']:.1f}")
say(f"B 1/2 + sqrt3 i: six {bB2['six']:.3f} at {bB2['six at']}; nine {bB2['nine']:.3f}; min chi2_six {bB2['min chi2_six']:.1f}")
say("model over measured at A's best six-row: " + str(bS["six: model over measured"]))
say("model over measured at A's best nine-row: " + str(bS["nine: model over measured"]))
say(f"controls: C1 {CTRL['C1 max |delta ln| against TC.ratios_at']:.2e}; C2 {CTRL['C2 max |delta ln| under T (ratios, |V| above 1e-12), F_6']}; C3 {CTRL['C3 max |delta ln| against B1720' + chr(39) + 's stored six']:.2e}")
# read-outs (not cells)
OUT["read-outs"] = {}
for label, dirs, ru, rd, c in (("family A, each direction, S, c = 3", None, "S", "S", 3),
                               ("family A, menu, S, c = 1", MENU, "S", "S", 1),
                               ("family A, DR, up S~, down and leptons S, c = 3 (B1720's best reading)", ["dR"], "St", "S", 3),
                               ("family A, DR, S, c = 3", ["dR"], "S", "S", 3),
                               ("family A, DR, S~, c = 3 (the sealed census's model)", ["dR"], "St", "St", 3)):
    if dirs is None:
        for d in MENU:
            b = best(*rows([d], ru, rd, c, A))
            OUT["read-outs"][f"family A, {d}, S, c = 3"] = {k: x for k, x in b.items() if k not in ("w6", "w9")}
            say(f"read-out {d}: six {b['six']:.3f} at {b['six at']}; nine {b['nine']:.3f} at {b['nine at']}")
        continue
    b = best(*rows(dirs, ru, rd, c, A))
    OUT["read-outs"][label] = {k: x for k, x in b.items() if k not in ("w6", "w9")}
    say(f"read-out {label}: six {b['six']:.3f} at {b['six at']}; nine {b['nine']:.3f}; min chi2_six {b['min chi2_six']:.1f}")
(HERE / "rigid_tau_compare.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "rigid_tau_compare_run.txt").write_text("\n".join(LOG) + "\n")
