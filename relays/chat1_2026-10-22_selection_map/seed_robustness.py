#!/usr/bin/env python3
"""POST HOC, labelled (after the TWO_INGREDIENTS comparison was read, at the referee's prompt): how much the sealed
specificity cells F2 and F4 depend on the calibration's seed.  The sealed model (S~ for every sector, Clebsch 3) on the
sealed census's rows; main's r_masses and r_ckm drawn as in two_ingredients_compare.py (4 000 six-target sets, then
4 000 nine-target sets, from one generator) for the sealed seed 1720 and for seeds 100-119.  The cells stand as sealed;
this only sizes the sampling.
    python3 -B seed_robustness.py      # writes seed_robustness.json and seed_robustness_run.txt"""
import hashlib, json, math, random, subprocess, pathlib
import numpy as np

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
M = []
for line in (HERE / "two_ingredients_census.jsonl").read_text().splitlines():
    if line.strip():
        r = json.loads(line)
        for hor in ("L_max", "L_2"):
            vals = r[f"up|{hor}|St"] + r[f"down|{hor}|St"] + r[f"lep|{hor}|St"] + r[f"ckm|{hor}|St|St"][:3]
            x = np.log(np.maximum(np.array(vals, dtype=float), 1e-300)); x[4] += math.log(3); x[5] -= math.log(3)
            M.append(x)
M = np.array(M); assert M.shape == (17024, 9)
w6 = float(np.min(np.max(np.abs(M[:, :6] - T6), axis=1))); w9 = float(np.min(np.max(np.abs(M - T9), axis=1)))


def best_many(Mx, D, batch=64):
    out = []
    for i in range(0, len(D), batch):
        d = D[i:i + batch]
        out.append(np.min(np.max(np.abs(Mx[:, None, :] - d[None, :, :]), axis=2), axis=0))
    return np.concatenate(out)


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


LOG, OUT = [], {"best_six": math.exp(w6), "best_nine": math.exp(w9), "per_seed": {}}
for seed in [1720] + list(range(100, 120)):
    rng = random.Random(seed)
    d6 = np.log(np.array([r_masses(rng) for _ in range(4000)]))
    d9 = np.log(np.array([r_masses(rng) + r_ckm(rng) for _ in range(4000)]))
    f6 = float(np.mean(best_many(M[:, :6], d6) <= w6 + 1e-12)); f9 = float(np.mean(best_many(M, d9) <= w9 + 1e-12))
    OUT["per_seed"][seed] = [f6, f9]
    s = f"seed {seed}: six {f6:.4f}, nine {f9:.4f}"; LOG.append(s); print(s, flush=True)
other = np.array([OUT["per_seed"][s] for s in range(100, 120)])
OUT["seeds_100_119"] = {"six_mean": float(other[:, 0].mean()), "six_sem": float(other[:, 0].std(ddof=1) / math.sqrt(20)),
                        "six_min_max": [float(other[:, 0].min()), float(other[:, 0].max())], "six_seeds_at_or_below_1pct": int((other[:, 0] <= 0.01).sum()),
                        "nine_mean": float(other[:, 1].mean()), "nine_sem": float(other[:, 1].std(ddof=1) / math.sqrt(20)),
                        "nine_min_max": [float(other[:, 1].min()), float(other[:, 1].max())], "nine_seeds_at_or_below_1pct": int((other[:, 1] <= 0.01).sum())}
o = OUT["seeds_100_119"]
s = (f"seeds 100-119 (20 x 4 000 targets): six {o['six_mean']:.4f} +- {o['six_sem']:.4f} (range {o['six_min_max'][0]:.4f}-"
     f"{o['six_min_max'][1]:.4f}; {o['six_seeds_at_or_below_1pct']} of 20 at or below 1%); nine {o['nine_mean']:.4f} +- "
     f"{o['nine_sem']:.4f} (range {o['nine_min_max'][0]:.4f}-{o['nine_min_max'][1]:.4f}; {o['nine_seeds_at_or_below_1pct']} of 20)")
LOG.append(s); print(s)
(HERE / "seed_robustness.json").write_text(json.dumps(OUT, indent=1) + "\n")
(HERE / "seed_robustness_run.txt").write_text("\n".join(LOG) + "\n")
