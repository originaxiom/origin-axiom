#!/usr/bin/env python3
"""TWO_HIGGS's comparison (sealed rule: TWO_HIGGS_RULE.md, 0b192e458; committed before the outputs it reads exist).
Cells H1-H8 and controls C1-C2 exactly as the rule states them, then the read-outs.
    python3 -B two_higgs_compare.py      # writes two_higgs_compare.json and two_higgs_compare_run.txt"""
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
PAIRS6 = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T6 = np.log(np.array([v[a] / v[b] for a, b in PAIRS6]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
REL = np.array([math.hypot(s[a] / v[a], s[b] / v[b]) for a, b in PAIRS6] + [CS[0][1] / C[0][1], CS[1][2] / C[1][2], CS[0][2] / C[0][2]])
SIG = np.sqrt(REL ** 2 + 0.10 ** 2)                                         # PRECISION_BAR.md: main's definition
JPDG = 3.08e-5
IDX = json.loads((HERE / "two_higgs_index.json").read_text())
X = np.load(HERE / "two_higgs.npz")["data"].astype(np.float64)               # point, hor, model, field
CTRL = json.loads((HERE / "two_higgs_controls.json").read_text())
TASKS, LINES, MODELS, HORS = IDX["tasks"], IDX["lines"], IDX["models"], IDX["hors"]
PAIRS = [tuple(p) for p in IDX["pairs"]]
OFF = [i for i, (u, d) in enumerate(PAIRS) if u != d]
DIAG = [i for i, (u, d) in enumerate(PAIRS) if u == d]
LOG, OUT = [], {}


def say(x):
    LOG.append(x); print(x, flush=True)


def rows(models, c=3.0):
    Y = X[:, :, models]                                                      # point, hor, model, field
    L = Y[..., 0:6] * math.log(10)
    L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
    L9 = np.concatenate([L, np.log(np.maximum(Y[..., 6:9], 1e-300))], axis=-1)
    lab = [(p, h, models[mm]) for p in range(Y.shape[0]) for h in range(Y.shape[1]) for mm in range(Y.shape[2])]
    return L9.reshape(-1, 9), Y[..., 9].reshape(-1), Y[..., 10:16].reshape(-1, 6), lab


def where(l):
    p, h, mo = l
    k, re_t, im_t = TASKS[p]
    return {"model": MODELS[mo], "tau": [re_t, im_t], "line": LINES[k], "hor": HORS[h]}


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


def best(models):
    L9, J, W, lab = rows(models)
    six = np.max(np.abs(L9[:, :6] - T6), axis=1); nine = np.max(np.abs(L9 - T9), axis=1)
    chi6 = np.sum(((L9[:, :6] - T6) / SIG[:6]) ** 2, axis=1); chi9 = np.sum(((L9 - T9) / SIG) ** 2, axis=1)
    i6, i9, c6, c9 = int(np.argmin(six)), int(np.argmin(nine)), int(np.argmin(chi6)), int(np.argmin(chi9))
    R2 = np.exp(L9[:, 4] - L9[:, 2]); R1 = np.exp(L9[:, 3] - L9[:, 5])
    blocks = ["QJ", "QI", "QK"]
    al = lambda i: {"up heaviest": dict(zip(blocks, np.round(W[i, :3], 4).tolist())),
                    "down heaviest": dict(zip(blocks, np.round(W[i, 3:], 4).tolist())),
                    "same block above 1/2": bool(W[i, :3].max() > 0.5 and W[i, 3:].max() > 0.5 and int(np.argmax(W[i, :3])) == int(np.argmax(W[i, 3:])))}
    return {"rows": len(lab), "six": math.exp(six[i6]), "six at": where(lab[i6]), "nine at the best six-row": math.exp(nine[i6]),
            "D at the best six-row": float(R2[i6] * R1[i6]), "J at the best six-row": float(J[i6]),
            "six: model over measured": np.exp(L9[i6] - T9).round(3).tolist(), "alignment at the best six-row": al(i6),
            "nine": math.exp(nine[i9]), "nine at": where(lab[i9]), "J at the best nine-row": float(J[i9]),
            "nine: model over measured": np.exp(L9[i9] - T9).round(3).tolist(), "alignment at the best nine-row": al(i9),
            "min chi2_six": float(chi6[c6]), "min chi2_six at": where(lab[c6]),
            "min chi2_nine": float(chi9[c9]), "min chi2_nine at": where(lab[c9]),
            "w6": float(six[i6]), "w9": float(nine[i9]), "_L9": L9}


bOFF, bDIAG = best(OFF), best(DIAG)
per_pair = {MODELS[i]: best([i]) for i in range(len(PAIRS))}
best_off_six = min(per_pair[MODELS[i]]["six"] for i in OFF); best_diag_six = min(per_pair[MODELS[i]]["six"] for i in DIAG)
best_off_nine = min(per_pair[MODELS[i]]["nine"] for i in OFF); best_diag_nine = min(per_pair[MODELS[i]]["nine"] for i in DIAG)
f6, f9 = calibrate(bOFF["_L9"], bOFF["w6"], bOFF["w9"])
cells = {
    "H1 best off-diagonal six < best diagonal six": best_off_six < best_diag_six,
    "H2 best off-diagonal nine < best diagonal nine": best_off_nine < best_diag_nine,
    "H3 six specific on the off-diagonal rows (<= 1%)": float(np.mean(f6)) <= 0.01,
    "H4 nine specific on the off-diagonal rows (<= 1%)": float(np.mean(f9)) <= 0.01,
    "H5 some off-diagonal row with chi2_six below 16.75": bOFF["min chi2_six"] < 16.75,
    "H6 some off-diagonal row with chi2_nine below 21.67": bOFF["min chi2_nine"] < 21.67,
    "H7 at the off-diagonal best six-row the nine is within 2.5": bOFF["nine at the best six-row"] <= 2.5,
    "H8 |J| within a factor 3 of 3.08e-5 at the off-diagonal best nine-row": JPDG / 3 <= abs(bOFF["J at the best nine-row"]) <= 3 * JPDG,
    "C1 holds": bool(CTRL["C1 holds"]), "C2 holds": bool(CTRL["C2 holds"])}
strip = lambda b: {k: x for k, x in b.items() if k not in ("w6", "w9", "_L9")}
OUT["cells"] = cells
OUT["the best pairs (six, nine)"] = {"off-diagonal": [best_off_six, best_off_nine], "diagonal": [best_diag_six, best_diag_nine]}
OUT["off-diagonal rows"] = strip(bOFF)
OUT["off-diagonal rows: random as good (20 seeds)"] = {"six": f6, "nine": f9, "six mean": float(np.mean(f6)), "nine mean": float(np.mean(f9))}
OUT["diagonal rows"] = strip(bDIAG)
OUT["controls"] = CTRL
for key, ok in cells.items():
    say(f"{key}: {ok}")
say(f"best pairs: off-diagonal six {best_off_six:.3f}, nine {best_off_nine:.3f}; diagonal six {best_diag_six:.3f}, nine {best_diag_nine:.3f}")
say(f"off-diagonal: six {bOFF['six']:.3f} at {bOFF['six at']} (nine there {bOFF['nine at the best six-row']:.3f}; D {bOFF['D at the best six-row']:.3f}); alignment {bOFF['alignment at the best six-row']}")
say(f"off-diagonal: nine {bOFF['nine']:.3f} at {bOFF['nine at']} (J {bOFF['J at the best nine-row']:.2e}); alignment {bOFF['alignment at the best nine-row']}")
say(f"off-diagonal: random as good six {np.mean(f6):.4f} ({min(f6):.4f}-{max(f6):.4f}), nine {np.mean(f9):.4f} ({min(f9):.4f}-{max(f9):.4f})")
say(f"off-diagonal: min chi2_six {bOFF['min chi2_six']:.1f} at {bOFF['min chi2_six at']}; min chi2_nine {bOFF['min chi2_nine']:.1f} at {bOFF['min chi2_nine at']}")
say("off-diagonal model over measured at the best six-row: " + str(bOFF["six: model over measured"]))
say("off-diagonal model over measured at the best nine-row: " + str(bOFF["nine: model over measured"]))
say(f"controls: C1 {CTRL['C1 max |delta ln| (ratios, |V|)']}; C2 {CTRL['C2 max |delta ln| against TC.ratios_at']:.2e}")
# read-outs (not cells)
OUT["read-outs"] = {"per pair": {k: strip(b) for k, b in per_pair.items()}}
d6, d9 = calibrate(bDIAG["_L9"], bDIAG["w6"], bDIAG["w9"])
OUT["read-outs"]["diagonal rows: random as good (20 seeds)"] = {"six mean": float(np.mean(d6)), "nine mean": float(np.mean(d9))}
say(f"read-out diagonal rows: six {bDIAG['six']:.3f}, nine {bDIAG['nine']:.3f}; random as good {np.mean(d6):.4f}, {np.mean(d9):.4f}; min chi2_six {bDIAG['min chi2_six']:.1f}")
for i, name in ((9, "reference: DR split (up S~)"), (10, "reference: DR S~ in every sector")):
    b = best([i]); r6, r9 = calibrate(b["_L9"], b["w6"], b["w9"])
    OUT["read-outs"][name] = strip(b) | {"random as good, mean (six, nine)": [float(np.mean(r6)), float(np.mean(r9))]}
    say(f"read-out {name}: six {b['six']:.3f} at {b['six at']}; nine {b['nine']:.3f}; min chi2_six {b['min chi2_six']:.1f}; random as good {np.mean(r6):.4f}, {np.mean(r9):.4f}")
for k, b in per_pair.items():
    say(f"read-out pair {k}: six {b['six']:.3f}, nine {b['nine']:.3f}, min chi2_six {b['min chi2_six']:.1f}, nine at its best six-row {b['nine at the best six-row']:.3f}")
(HERE / "two_higgs_compare.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "two_higgs_compare_run.txt").write_text("\n".join(LOG) + "\n")
