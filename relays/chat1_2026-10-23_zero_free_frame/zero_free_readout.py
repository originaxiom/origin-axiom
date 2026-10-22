#!/usr/bin/env python3
"""EXPLORATORY read-out, labelled (committed before zero_free_census.npz exists or is read): main's frame with the
zero-free Higgs lines F_a in place of DR, against the record's targets.
For each direction (DR and the ten F_a), each reading and the lepton factor c in {1, 3} (by hand on the stored ratios,
m_mu/m_tau x c and m_e/m_tau / c, as the sealed census did):
  readings (up; down; leptons): St-all (S~ in every sector), split (S~; S; S), S-all (S; S; S), flipped (S; S~; S~);
  - the best six and nine (worst factors), where (tau, line, horocycle), and D, R2, R1 there;
  - the best six among rows with D within 3 sigma of P-094 (10.58 +- 0.11);
  - random as good: main's generator (random.Random(1720); 4 000 six-targets, then 4 000 nine-targets), the same rows.
A sanity line: DR, St-all, on the sealed census's own Im tau range (2.0-3.5) and Re tau (0.1, 0.4), must give the
census's 1.513 / 2.087 (c = 3) and 2.553 / 3.274 (c = 1).
Targets: Huang-Zhou 2021 at M_Z and PDG 2025's three moduli, from the record's pinned files at main's 3412bf09d.
    python3 -B zero_free_readout.py      # writes zero_free_readout.json and zero_free_readout_run.txt"""
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
P094, SIG = 10.58, 0.11
IDX = json.loads((HERE / "zero_free_census_index.json").read_text())
X = np.load(HERE / "zero_free_census.npz")["data"].astype(np.float64)     # point, dir, hor, field
TASKS = IDX["tasks"]; LIN = IDX["lines"]; DIRS = IDX["dirs"]; HORS = IDX["hors"]
LN10 = math.log(10)
READ = {"St-all": ("St", "St", "St"), "split": ("St", "S", "S"), "S-all": ("S", "S", "S"), "flipped": ("S", "St", "St")}
SECI = {("up", "S"): 0, ("up", "St"): 2, ("down", "S"): 4, ("down", "St"): 6, ("lep", "S"): 8, ("lep", "St"): 10}
CKMI = {("S", "S"): 12, ("S", "St"): 16, ("St", "S"): 20, ("St", "St"): 24}
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


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


d6 = np.log(np.array([r_masses() for _ in range(4000)]))
d9 = np.log(np.array([r_masses() + r_ckm() for _ in range(4000)]))


def table(d, reading, c, mask=None):
    """rows (point, hor) -> ln of the nine targets' model values, and J"""
    ru, rdn, rl = READ[reading]; di = DIRS.index(d)
    Y = X[:, di]                                                       # point, hor, field
    L = np.concatenate([Y[..., SECI[("up", ru)]:SECI[("up", ru)] + 2], Y[..., SECI[("down", rdn)]:SECI[("down", rdn)] + 2],
                        Y[..., SECI[("lep", rl)]:SECI[("lep", rl)] + 2]], axis=-1) * LN10
    L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
    k = CKMI[(ru, rdn)]
    V = np.log(np.maximum(Y[..., k:k + 3], 1e-300)); J = Y[..., k + 3]
    L9 = np.concatenate([L, V], axis=-1)
    if mask is not None:
        L9 = L9[mask]; J = J[mask]
    return L9, J


def where(i):
    p, h = i
    k, re_t, im_t = TASKS[p]
    return {"tau": [re_t, im_t], "line": LIN[k], "hor": HORS[h]}


def summarise(d, reading, c, mask=None, calibrate=True):
    L9, J = table(d, reading, c, mask)
    six = np.max(np.abs(L9[..., :6] - T6), axis=-1); nine = np.max(np.abs(L9 - T9), axis=-1)
    R2 = np.exp(L9[..., 4] - L9[..., 2]); R1 = np.exp(L9[..., 3] - L9[..., 5]); D = R2 * R1
    res = {}
    for key, arr, m in (("six", six, None), ("nine", nine, None), ("six, D at P-094", six, np.abs(D - P094) <= 3 * SIG)):
        a_ = np.where(m, arr, np.inf) if m is not None else arr
        i = np.unravel_index(np.argmin(a_), a_.shape)
        if not np.isfinite(a_[i]):
            res[key] = None; continue
        res[key] = {"value": math.exp(a_[i]), "D": float(D[i]), "R2": float(R2[i]), "R1": float(R1[i]), "J": float(J[i]),
                    "six": math.exp(six[i]), "nine": math.exp(nine[i]), "n_rows": int(m.sum()) if m is not None else int(arr.size),
                    "where": where(i) if mask is None else None,
                    "model_over_measured": np.exp(L9[i] - T9).round(3).tolist()}
    if calibrate:
        rows = L9.reshape(-1, 9)
        q6, _ = cKDTree(rows[:, :6]).query(d6, k=1, p=np.inf); q9, _ = cKDTree(rows).query(d9, k=1, p=np.inf)
        res["six random as good"] = float(np.mean(q6 <= np.min(six) + 1e-12))
        res["nine random as good"] = float(np.mean(q9 <= np.min(nine) + 1e-12))
    return res


# sanity: DR, St-all, on the census's own range
cmask = np.array([[2.0 - 1e-9 <= t[2] <= 3.5 + 1e-9] * 2 for t in TASKS])
for c in (3, 1):
    s = summarise("dR", "St-all", c, cmask, calibrate=False)
    say(f"sanity: DR, St-all, c = {c}, census range: six {s['six']['value']:.3f}, nine {s['nine']['value']:.3f} "
        f"(census: {'1.513 / 2.087' if c == 3 else '2.553 / 3.274'})")
    OUT[f"sanity c={c}"] = [s["six"]["value"], s["nine"]["value"]]

OUT["by direction"] = {}
for d in DIRS:
    OUT["by direction"][d] = {}
    for reading in READ:
        for c in (1, 3):
            s = summarise(d, reading, c)
            OUT["by direction"][d][f"{reading} c={c}"] = s
            b6, b9, bd_ = s["six"], s["nine"], s["six, D at P-094"]
            say(f"{d:6s} {reading:8s} c={c}: six {b6['value']:.3f} at {b6['where']} (D {b6['D']:.2f}, R2 {b6['R2']:.2f}, R1 {b6['R1']:.2f}; "
                f"nine there {b6['nine']:.2f}); nine {b9['value']:.3f} at {b9['where']} (J {b9['J']:.1e}); D-matched six "
                + (f"{bd_['value']:.3f} ({bd_['n_rows']} rows)" if bd_ else "none")
                + f"; random as good {s['six random as good']:.4f} / {s['nine random as good']:.4f}")
say("== summary: best six / best nine (random as good), St-all and split, c = 1 and 3")
for d in DIRS:
    parts = []
    for reading in ("St-all", "split"):
        for c in (1, 3):
            s = OUT["by direction"][d][f"{reading} c={c}"]
            parts.append(f"{reading} c={c}: {s['six']['value']:.2f} ({s['six random as good']:.3f}) / {s['nine']['value']:.2f} ({s['nine random as good']:.3f})")
    say(f"{d:6s} " + "; ".join(parts))
(HERE / "zero_free_readout.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "zero_free_readout_run.txt").write_text("\n".join(LOG) + "\n")
