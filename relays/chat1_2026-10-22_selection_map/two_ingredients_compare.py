#!/usr/bin/env python3
"""TWO_INGREDIENTS_RULE.md: the cells F1-F4 and C1, and the read-outs, from two_ingredients_census.jsonl (all 8 512
points required).  Main's measure of fit and main's calibration (B1720 compare.py: r_masses, r_ckm, seed 1720, 4 000).
    python3 -B two_ingredients_compare.py      # writes two_ingredients_comparison.json and _run.txt"""
import hashlib, json, math, random, subprocess, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
REV = "3412bf09d"
DATA = "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"
CKMDATA = "frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json"


def git(path):
    return subprocess.run(["git", "show", f"{REV}:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd, bc = git(DATA), git(CKMDATA)
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
v = json.loads(bd)["masses_GeV"]["value"]
C = json.loads(bc)["ckm_abs"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
T3 = np.log(np.array([C[0][1], C[1][2], C[0][2]]))
T9 = np.concatenate([T6, T3])

rows = [json.loads(l) for l in (HERE / "two_ingredients_census.jsonl").read_text().splitlines() if l.strip()]
keys = {(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows}
assert len(keys) == 8512 == len(rows), (len(keys), len(rows))
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)


def matrix(cu, cd, cl, c):
    M, lab = [], []
    for r in rows:
        for hor in ("L_max", "L_2"):
            vals = r[f"up|{hor}|{cu}"] + r[f"down|{hor}|{cd}"] + r[f"lep|{hor}|{cl}"] + r[f"ckm|{hor}|{cu}|{cd}"][:3]
            a = np.log(np.maximum(np.array(vals, dtype=float), 1e-300)); a[4] += math.log(c); a[5] -= math.log(c)
            M.append(a); lab.append({"line": r["line"], "Re_tau": r["Re_tau"], "Im_tau": r["Im_tau"], "horocycle": hor,
                                     "J": r[f"ckm|{hor}|{cu}|{cd}"][3]})
    return np.array(M), lab


def best(M, t):
    w = np.max(np.abs(M - t), axis=1); i = int(np.argmin(w)); return float(np.exp(w[i])), i


rng = random.Random(1720)


def r_masses():
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2:
                break
        tg += [r2, r1]
    return tg


def r_ckm():
    while True:
        a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
        if c < b < a:
            return [a, b, c]


N = 4000
draws6 = [np.log(np.array(r_masses())) for _ in range(N)]
draws9 = [np.log(np.array(r_masses() + r_ckm())) for _ in range(N)]


def cell_set(cu, cd, cl, c, calibrate):
    M, lab = matrix(cu, cd, cl, c)
    w6, i6 = best(M[:, :6], T6); w9, i9 = best(M, T9)
    out = {"six": {"best": w6, "row": lab[i6], "model_over_measured": np.exp(M[i6, :6] - T6).tolist()},
           "nine": {"best": w9, "row": lab[i9], "model_over_measured": np.exp(M[i9] - T9).tolist()}}
    if calibrate:
        out["six"]["random_as_good"] = float(np.mean([best(M[:, :6], d)[0] <= w6 + 1e-12 for d in draws6]))
        out["nine"]["random_as_good"] = float(np.mean([best(M, d)[0] <= w9 + 1e-12 for d in draws9]))
    return out


RES = {"rows": len(rows) * 2}
RES["sealed"] = cell_set("St", "St", "St", 3, True)
s, n9 = RES["sealed"]["six"], RES["sealed"]["nine"]
RES["F1_six_within_2"] = s["best"] <= 2.0
RES["F2_six_specific"] = s["random_as_good"] <= 0.01
RES["F3_nine_within_2.5"] = n9["best"] <= 2.5
RES["F4_nine_specific"] = n9["random_as_good"] <= 0.01
ctrl = json.loads((HERE / "two_ingredients_control.json").read_text())
RES["C1_control_max_abs_log"] = ctrl["max_abs_log"]
RES["C1_holds"] = ctrl["max_abs_log"] < 1e-9
say(f"sealed (S~ for every sector, Clebsch 3): six {s['best']:.3f} (random as good {s['random_as_good']:.4f}); "
    f"nine {n9['best']:.3f} (random as good {n9['random_as_good']:.4f})")
say(f"F1 {RES['F1_six_within_2']}  F2 {RES['F2_six_specific']}  F3 {RES['F3_nine_within_2.5']}  F4 {RES['F4_nine_specific']}  "
    f"C1 {RES['C1_holds']} ({ctrl['max_abs_log']:.2e})")
say("  six best row:", s["row"], [round(x, 3) for x in s["model_over_measured"]])
say("  nine best row:", n9["row"], [round(x, 3) for x in n9["model_over_measured"]])
RES["readouts"] = {}
for label, args in (("main readings (up S~, down S), Clebsch 3", ("St", "S", "S", 3)),
                    ("main readings (up S~, down S), no Clebsch", ("St", "S", "S", 1)),
                    ("S~ for every sector, no Clebsch", ("St", "St", "St", 1))):
    RES["readouts"][label] = cell_set(*args, calibrate=True)
    o = RES["readouts"][label]
    say(f"read-out {label}: six {o['six']['best']:.3f} ({o['six']['random_as_good']:.4f}); nine {o['nine']['best']:.3f} "
        f"({o['nine']['random_as_good']:.4f})")
(HERE / "two_ingredients_comparison.json").write_text(json.dumps(RES, indent=1, default=str) + "\n")
(HERE / "two_ingredients_compare_run.txt").write_text("\n".join(LOG) + "\n")
