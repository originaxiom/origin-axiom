#!/usr/bin/env python3
"""POST HOC read-outs, labelled (TWO_HIGGS: written after the sealed cells were read; committed before its own run).
None is a cell.
  P1  the off-diagonal rows with chi2_six below 16.75: how many, which pairs, lines, tau and horocycles; at each the
      nine, the three |V| over measured, J, D, and the two sectors' heaviest left vectors on the blocks;
  P2  at the best six-row (F_6 | F_22 at 0.5625 + 2.6i on (2/5, 1/10), L_2): the other eight pairs and the two references
      at the same row; the six and chi2_six with c = 1; chi2_six against the targets run to 2e16 GeV in the SM (the
      factors of framing_readouts.json, F2);
  P3  main's frame recomputed around the best six-row for F_6 | F_22: Re tau and Im tau moved by 0.01, 0.02 and 0.05
      either way (one at a time), the six, chi2_six, the nine and J;
  P4  the rows that meet both coarse bars (six <= 2.0 and nine <= 2.5) for the off-diagonal and the diagonal pairs.
    python3 -B two_higgs_posthoc.py      # writes two_higgs_posthoc.json"""
import contextlib, hashlib, importlib.util, io, json, math, subprocess, sys, pathlib
import numpy as np

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
SIG = np.sqrt(REL ** 2 + 0.10 ** 2)
FR = json.loads((HERE.parent / "chat1_2026-10-23_framing" / "framing_readouts.json").read_text())
SHIFT = np.log(np.array(FR["F2 the running, M_Z to 2e16 GeV (one loop, SM, estimate)"]["factors on the nine targets"]))
T9H = T9 + SHIFT
IDX = json.loads((HERE / "two_higgs_index.json").read_text())
X = np.load(HERE / "two_higgs.npz")["data"].astype(np.float64)               # point, hor, model, field
TASKS, LINES, MODELS, HORS = IDX["tasks"], IDX["lines"], IDX["models"], IDX["hors"]
PAIRS = [tuple(p) for p in IDX["pairs"]]
OFF = [i for i, (u, d) in enumerate(PAIRS) if u != d]
DIAG = [i for i, (u, d) in enumerate(PAIRS) if u == d]
OUT = {}


def l9(f, c=3.0):
    L = np.array(f[0:6]) * math.log(10)
    L[4] += math.log(c); L[5] -= math.log(c)
    return np.concatenate([L, np.log(np.maximum(np.array(f[6:9]), 1e-300))])


def describe(p, h, mo, c=3.0):
    f = X[p, h, mo]; L = l9(f, c); k, re_t, im_t = TASKS[p]
    six = math.exp(float(np.max(np.abs(L[:6] - T6)))); nine = math.exp(float(np.max(np.abs(L - T9))))
    R2 = math.exp(L[4] - L[2]); R1 = math.exp(L[3] - L[5])
    return {"model": MODELS[mo], "tau": [re_t, im_t], "line": LINES[k], "hor": HORS[h], "six": six, "nine": nine,
            "chi2_six": float(np.sum(((L[:6] - T6) / SIG[:6]) ** 2)), "chi2_nine": float(np.sum(((L - T9) / SIG) ** 2)),
            "model over measured": np.exp(L - T9).round(3).tolist(), "J": float(f[9]), "D": R2 * R1,
            "up heaviest (QJ, QI, QK)": np.round(f[10:13], 4).tolist(), "down heaviest (QJ, QI, QK)": np.round(f[13:16], 4).tolist()}


# P1
P1 = []
for p in range(X.shape[0]):
    for h in range(X.shape[1]):
        for mo in OFF:
            L = l9(X[p, h, mo])
            if float(np.sum(((L[:6] - T6) / SIG[:6]) ** 2)) < 16.75:
                P1.append(describe(p, h, mo))
P1.sort(key=lambda r: r["chi2_six"])
OUT["P1 off-diagonal rows with chi2_six below 16.75"] = {"count": len(P1), "rows": P1}
# P2
best = P1[0]
pb = next(p for p, (k, re_t, im_t) in enumerate(TASKS) if LINES[k] == best["line"] and abs(re_t - best["tau"][0]) < 1e-9 and abs(im_t - best["tau"][1]) < 1e-9)
hb = HORS.index(best["hor"])
P2 = {"all eleven models at the best six-row": [describe(pb, hb, mo) for mo in range(len(MODELS))]}
mob = MODELS.index(best["model"])
P2["c = 1 at the best six-row"] = {k: describe(pb, hb, mob, c=1.0)[k] for k in ("six", "chi2_six", "model over measured")}
L = l9(X[pb, hb, mob])
P2["chi2_six against the 2e16 GeV targets (SM), the best six-row"] = float(np.sum(((L[:6] - T9H[:6]) / SIG[:6]) ** 2))
P2["model over the 2e16 GeV targets"] = np.exp(L - T9H).round(3).tolist()
OUT["P2 the best six-row"] = P2
# P4
both = {"off-diagonal": [], "diagonal": []}
for p in range(X.shape[0]):
    for h in range(X.shape[1]):
        for side, mods in (("off-diagonal", OFF), ("diagonal", DIAG)):
            for mo in mods:
                L = l9(X[p, h, mo])
                if np.max(np.abs(L[:6] - T6)) <= math.log(2.0) and np.max(np.abs(L - T9)) <= math.log(2.5):
                    both[side].append(describe(p, h, mo))
OUT["P4 rows meeting both coarse bars"] = {k: {"count": len(r), "rows": sorted(r, key=lambda x: x["nine"])[:10]} for k, r in both.items()}
# P3 main's frame around the best six-row
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("tht", HERE / "two_higgs_test.py")
tht = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(tht)
k = LINES.index(best["line"]); a, b = tht.LINES[k]
assert f"({a}, {b})" == best["line"]
u, d = PAIRS[mob]
scan = []
for dre, dim in [(0, 0)] + [(sgn * e, 0) for e in (0.01, 0.02, 0.05) for sgn in (-1, 1)] + [(0, sgn * e) for e in (0.01, 0.02, 0.05) for sgn in (-1, 1)]:
    re_t, im_t = best["tau"][0] + dre, best["tau"][1] + dim
    M = tht.rbs.channels(re_t, im_t, float(a), float(b))
    Su = tht.rbs.S_of(tht.zfc.direction(u, re_t, im_t)); Sd = tht.rbs.S_of(tht.zfc.direction(d, re_t, im_t))
    f = tht.row(M, best["hor"], Su, Sd)
    Lr = l9(f)
    scan.append({"tau": [re_t, im_t], "six": math.exp(float(np.max(np.abs(Lr[:6] - T6)))), "chi2_six": float(np.sum(((Lr[:6] - T6) / SIG[:6]) ** 2)),
                 "nine": math.exp(float(np.max(np.abs(Lr - T9)))), "J": float(f[9]), "model over measured": np.exp(Lr - T9).round(3).tolist()})
OUT["P3 main's frame around the best six-row (F_6 | F_22)"] = scan
(HERE / "two_higgs_posthoc.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
