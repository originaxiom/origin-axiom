#!/usr/bin/env python3
"""POST HOC read-outs for the framing note, labelled (written after the referee's report on its draft; committed before
their own run).  Not tests.
  K1  every direction in each of the day's four stored scans, in each of the four readings (S in every sector; S~ in
      every sector; split: up S~, down and leptons S; flipped: up S, down and leptons S~), c = 3: the minimum chi2_six,
      where it is, how many rows are below 16.75, and |V_cb| over measured at the minimum;
  K2  RIGID_TAU's 843 CP-self-conjugate family-A points: the largest |J| for every direction and every (up, down) reading;
  K3  the CP control: for the menu read S and main's DR read S~ on the zero-free census and ZERO_FREE_HOLOMORPHIC, the
      best nine among the rows whose |J| is within a factor 3 of 3.08e-5, against the best nine among random row subsets of
      the same size (200 subsets, random.Random(1720)): median and 95th percentile;
  K4  the chi-square calibration of the six's minima on ZERO_FREE_HOLOMORPHIC's grid for main's DR split and for the
      menu flipped: for seeds 1720-1724, 4 000 random six-target sets each (main's generator), the share whose minimum
      chi2_six over the same rows (the data's sigma) is at or below the observed minimum.
    python3 -B framing_readouts3.py      # writes framing_readouts3.json"""
import hashlib, json, math, random, subprocess, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
R = HERE.parent


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
SCANS = {
    "zero-free census": (R / "chat1_2026-10-23_zero_free_frame" / "zero_free_census_index.json", R / "chat1_2026-10-23_zero_free_frame" / "zero_free_census.npz", None),
    "ZERO_FREE_HOLOMORPHIC": (R / "chat1_2026-10-23_zero_free_frame" / "zero_free_holomorphic_index.json", R / "chat1_2026-10-23_zero_free_frame" / "zero_free_holomorphic.npz", None),
    "TICK_LINE_HIGGS": (R / "chat1_2026-10-23_tick_line" / "tick_line_index.json", R / "chat1_2026-10-23_tick_line" / "tick_line.npz", None),
    "RIGID_TAU family A": (R / "chat1_2026-10-23_rigid_tau" / "rigid_tau_index.json", R / "chat1_2026-10-23_rigid_tau" / "rigid_tau.npz", "A"),
}
SEC = {"S": (0, 4, 8), "St": (2, 6, 10)}
CKMI = {("S", "S"): 12, ("S", "St"): 16, ("St", "S"): 20, ("St", "St"): 24}
READ = {"S in every sector": ("S", "S"), "S~ in every sector": ("St", "St"), "split (up S~)": ("St", "S"), "flipped (up S)": ("S", "St")}
OUT = {}


def l9(Y, ru, rd, c=3.0):
    iu, idn, il = SEC[ru][0], SEC[rd][1], SEC[rd][2]
    L = np.concatenate([Y[..., iu:iu + 2], Y[..., idn:idn + 2], Y[..., il:il + 2]], axis=-1) * math.log(10)
    L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
    k = CKMI[(ru, rd)]
    return np.concatenate([L, np.log(np.maximum(Y[..., k:k + 3], 1e-300))], axis=-1), Y[..., k + 3]


def labels(I, fam):
    if "tasks" in I:
        return [f"{I['lines'][t[0]]} at {t[1]} + {t[2]}i" for t in I["tasks"]]
    return [f"{p[1]} at {p[2]:.4f} + {p[3]:.4f}i" for p in I["points"] if p[0] == fam]


DATA = {}
for scan, (ip, dp, fam) in SCANS.items():
    I = json.loads(ip.read_text()); X = np.load(dp)["data"].astype(np.float64)
    if fam:
        X = X[[k for k, p in enumerate(I["points"]) if p[0] == fam]]
    DATA[scan] = (I, X, labels(I, fam))

# K1
K1 = {}
for scan, (I, X, lab) in DATA.items():
    res = {}
    for d in I["dirs"]:
        Y = X[:, I["dirs"].index(d)]
        for rn, (ru, rd) in READ.items():
            L9, _J = l9(Y, ru, rd)
            chi6 = np.sum(((L9[..., :6] - T6) / SIG[:6]) ** 2, axis=-1)
            p, h = np.unravel_index(int(np.argmin(chi6)), chi6.shape)
            res[f"{d}, {rn}"] = {"min chi2_six": float(chi6[p, h]), "at": f"{lab[p]}, {I['hors'][h]}",
                                 "rows below 16.75": int((chi6 < 16.75).sum()),
                                 "|V_cb| over measured there": float(np.exp(L9[p, h, 7] - T9[7]))}
    aligned = [r["min chi2_six"] for k, r in res.items() if ("every sector" in k)]
    res["_lowest min chi2_six over the aligned readings (S or S~ in every sector), all directions"] = float(min(aligned))
    K1[scan] = res
OUT["K1 the six's precision bar by direction and reading"] = K1

# K2
I, X, lab = DATA["RIGID_TAU family A"]
pts = [p for p in I["points"] if p[0] == "A"]
selfc = []
for i, p in enumerate(pts):
    re_t = p[2]; a, b = Fr(p[4]), Fr(p[5])
    n2 = 2 * re_t
    if abs(n2 - round(n2)) > 1e-9:
        continue
    n = int(round(n2)); bb = -b - n * a
    if (bb - b) % 1 == 0 or ((2 * a) % 1 == 0 and (bb + b) % 1 == 0):
        selfc.append(i)
K2 = {"self-conjugate points": len(selfc)}
for d in I["dirs"]:
    for (ru, rd), k in CKMI.items():
        K2[f"{d}, up {ru}, down {rd}: max |J|"] = float(np.abs(X[selfc][:, I["dirs"].index(d), :, k + 3]).max())
OUT["K2 J at the CP-self-conjugate apex configurations"] = K2

# K3
K3 = {}
rng = random.Random(1720)
for scan in ("zero-free census", "ZERO_FREE_HOLOMORPHIC"):
    I, X, lab = DATA[scan]
    for name, dirs, ru, rd in (("menu, S", ["F_6", "F_-2", "F_22"], "S", "S"), ("DR, S~", ["dR"], "St", "St")):
        Ls, Js = [], []
        for d in dirs:
            L9, J = l9(X[:, I["dirs"].index(d)], ru, rd)
            Ls.append(L9.reshape(-1, 9)); Js.append(J.reshape(-1))
        L9 = np.concatenate(Ls); J = np.abs(np.concatenate(Js))
        nine = np.max(np.abs(L9 - T9), axis=1)
        ok = (J >= JPDG / 3) & (J <= 3 * JPDG)
        n = int(ok.sum())
        idx = list(range(len(nine)))
        sub = [float(np.exp(nine[rng.sample(idx, n)].min())) for _ in range(200)]
        K3[f"{scan}: {name}"] = {"rows with |J| within a factor 3": n, "best nine among them": float(np.exp(nine[ok].min())),
                                 "best nine overall": float(np.exp(nine.min())),
                                 "random subsets of that size: median best nine": float(np.median(sub)),
                                 "random subsets: 95th percentile": float(np.quantile(sub, 0.95))}
OUT["K3 the CP control"] = K3


# K4
def r_masses(rng):
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2:
                break
        tg += [r2, r1]
    return tg


I, X, lab = DATA["ZERO_FREE_HOLOMORPHIC"]
K4 = {}
for name, dirs, ru, rd in (("DR split (up S~)", ["dR"], "St", "S"), ("menu flipped (up S)", ["F_6", "F_-2", "F_22"], "S", "St")):
    Ls = []
    for d in dirs:
        L9, _J = l9(X[:, I["dirs"].index(d)], ru, rd)
        Ls.append(L9.reshape(-1, 9)[:, :6])
    L6 = np.concatenate(Ls)
    obs = float(np.min(np.sum(((L6 - T6) / SIG[:6]) ** 2, axis=1)))
    shares = []
    for sd in range(1720, 1725):
        rg = random.Random(sd)
        tg = np.log(np.array([r_masses(rg) for _ in range(4000)]))
        hit = 0
        for j in range(0, 4000, 20):
            d2 = (((L6[None, :, :] - tg[j:j + 20, None, :]) / SIG[None, None, :6]) ** 2).sum(axis=2)
            hit += int((d2.min(axis=1) <= obs).sum())
        shares.append(hit / 4000)
    K4[name] = {"rows": int(len(L6)), "observed min chi2_six": obs, "share of random six-target sets as good, seeds 1720-1724": shares}
OUT["K4 the six's chi-square calibration (ZERO_FREE_HOLOMORPHIC's grid)"] = K4
(HERE / "framing_readouts3.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
