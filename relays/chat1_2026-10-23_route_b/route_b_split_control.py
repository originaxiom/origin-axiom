#!/usr/bin/env python3
"""POST HOC control, labelled (written after route_b_posthoc2 was read; committed before its own run): in the split
reading (up S~; down and leptons S), route (b)'s best six (1.742, with R2 2.28 and R1 3.26) looks Georgi-Jarlskog-like.
Does the -3 do that, or the freedom?  The same scan with the second direction's Clebsch set to 1 in every sector,
in the split reading; summaries as route_b_posthoc.py (best six and nine with D, R2, R1 there; D-matched and
Georgi-Jarlskog-ratio rows; calibration of the six with main's generator).
    python3 -B route_b_split_control.py      # writes route_b_split_control.json and route_b_split_control_run.txt"""
import contextlib, hashlib, importlib.util, io, json, math, random, subprocess, pathlib
import numpy as np
from scipy.spatial import cKDTree

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
_spec = importlib.util.spec_from_file_location("rbs", HERE / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)


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
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


data = np.zeros((len(rbs.BASE), len(rbs.CANDS), len(rbs.RHO), len(rbs.PHI), len(rbs.HORS), 10))
for ib, (re_t, im_t, a, b) in enumerate(rbs.BASE):
    M = rbs.channels(re_t, im_t, a, b)
    v1, v2, v3 = rbs.at(rbs.H1, re_t, im_t), rbs.at(rbs.H2, re_t, im_t), rbs.at(rbs.H3, re_t, im_t)
    n1 = np.linalg.norm(v1)
    u2, u3 = v2 / np.linalg.norm(v2), v3 / np.linalg.norm(v3)
    dirs = {"h2": u2, "h3": u3}
    for ang in (0, 90, 180, 270):
        dirs[f"c{ang}"] = (u2 + np.exp(1j * math.radians(ang)) * u3) / math.sqrt(2)
    S1 = rbs.S_of(v1)
    for ic, cn in enumerate(rbs.CANDS):
        Ss = rbs.S_of(dirs[cn])
        for ir, rho in enumerate(rbs.RHO):
            for ip, phi in enumerate(rbs.PHI):
                Sx = S1 + rho * np.exp(1j * phi) * n1 * Ss
                for ih, which in enumerate(rbs.HORS):
                    data[ib, ic, ir, ip, ih] = rbs.outputs(M, which, Sx, Sx, "main")
L = np.log(np.maximum(data[..., :9], 1e-300))
six = np.max(np.abs(L[..., :6] - T6), axis=-1); nine = np.max(np.abs(L - T9), axis=-1)
R2 = np.exp(L[..., 4] - L[..., 2]); R1 = np.exp(L[..., 3] - L[..., 5]); D = R2 * R1


def where(i):
    b, c, r, p, h = i
    return {"base": rbs.BASE[b], "cand": rbs.CANDS[c], "rho": rbs.RHO[r], "phi_deg": 15 * p, "hor": rbs.HORS[h]}


for label, arr, mask in (("best six", six, None), ("best nine", nine, None),
                         ("best six with D within 3 sigma of P-094", six, np.abs(D - P094) <= 3 * SIG),
                         ("best six with R2 and R1 both in [2, 4.5]", six, (R2 >= 2) & (R2 <= 4.5) & (R1 >= 2) & (R1 <= 4.5))):
    a_ = np.where(mask, arr, np.inf) if mask is not None else arr
    i = np.unravel_index(np.argmin(a_), a_.shape)
    if not np.isfinite(a_[i]):
        say(f"Clebsch 1, split reading, {label}: no such row"); OUT[label] = None; continue
    n = int(mask.sum()) if mask is not None else int(arr.size)
    say(f"Clebsch 1, split reading, {label} ({n} rows): {math.exp(a_[i]):.3f} at {where(i)}; D {D[i]:.2f}, R2 {R2[i]:.2f}, R1 {R1[i]:.2f}; "
        f"nine there {math.exp(nine[i]):.2f}")
    OUT[label] = {"value": math.exp(a_[i]), "rows": n, "where": where(i), "D": float(D[i]), "R2": float(R2[i]), "R1": float(R1[i]),
                  "nine": math.exp(nine[i])}
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


d6 = np.log(np.array([r_masses() for _ in range(4000)]))
rows = L.reshape(-1, 9)[:, :6]
w6 = float(np.min(six))
q6, _ = cKDTree(rows).query(d6, k=1, p=np.inf)
OUT["six_random_as_good"] = float(np.mean(q6 <= w6 + 1e-12))
say(f"Clebsch 1, split reading: six calibration, random as good {OUT['six_random_as_good']:.4f}")
(HERE / "route_b_split_control.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "route_b_split_control_run.txt").write_text("\n".join(LOG) + "\n")
