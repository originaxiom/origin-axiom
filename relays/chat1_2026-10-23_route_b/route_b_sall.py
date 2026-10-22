#!/usr/bin/env python3
"""POST HOC, labelled (written after route_b_readings was read; committed before its own run): route (b) in the reading
S for every sector, at that reading's own best census points.
Why: of the two readings in which up and down share the Higgs's section (Pati-Salam's bidoublet gives H_u and H_d one
section), route (b) was tested only with S~ (where the -3 does not act).  With S for every sector, the down quarks and
leptons see h itself, as in the split reading where the -3 acts; but route_b_scan's base points were chosen with S~ and
the up sector fails there with S.  So here the base points are the distinct base points among the sealed census's ten
best six-rows in the reading S for every sector with the by-hand Clebsch 3 (as route_b_scan chose its points with S~).
The scan is route_b_scan's (directions, kappa grid, horocycles), with the Clebsch -3 and the Clebsch-1 control.
Summaries as route_b_readings.py, plus the baseline (rho = 1e-4) per base point.
    python3 -B route_b_sall.py      # writes route_b_sall.json and route_b_sall_run.txt"""
import contextlib, hashlib, importlib.util, io, json, math, random, subprocess, pathlib
from fractions import Fraction as Fr
import numpy as np
from scipy.spatial import cKDTree

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
SEL = HERE.parent / "chat1_2026-10-22_selection_map"
_spec = importlib.util.spec_from_file_location("rbs", HERE / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)
B, tic = rbs.B, rbs.tic


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


# the base points: the census's ten best six-rows with S for every sector and the by-hand Clebsch 3
LINES = [(float(Fr(a)), float(Fr(b))) for (_t, a, b) in tic.LINES]
cand = []
for l in (SEL / "two_ingredients_census.jsonl").read_text().splitlines():
    r = json.loads(l)
    for hor in ("L_max", "L_2"):
        x = np.log(np.maximum(np.array(r[f"up|{hor}|S"] + r[f"down|{hor}|S"] + r[f"lep|{hor}|S"], dtype=float), 1e-300))
        x[4] += math.log(3); x[5] -= math.log(3)
        cand.append((float(np.max(np.abs(x - T6))), r["Re_tau"], r["Im_tau"], r["line"]))
cand.sort()
BASE, seen = [], set()
for w, re_t, im_t, k in cand[:10]:
    key = (re_t, im_t, k)
    if key not in seen:
        seen.add(key); BASE.append((re_t, im_t) + LINES[k])
OUT["base points (Re, Im, a, b)"] = BASE
say(f"base points: {BASE}")

data = {c: np.zeros((len(BASE), len(rbs.CANDS), len(rbs.RHO), len(rbs.PHI), len(rbs.HORS), 10)) for c in (-3, 1)}
for ib, (re_t, im_t, a, b) in enumerate(BASE):
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
                kap = rho * np.exp(1j * phi) * n1
                for c in (-3, 1):
                    Sq, Sl = S1 + kap * Ss, S1 + c * kap * Ss
                    for ih, which in enumerate(rbs.HORS):
                        Yu = B.coupling(Sq, M[("up", which)]); Yd = B.coupling(Sq, M[("down", which)]); Yl = B.coupling(Sl, M[("lep", which)])
                        o = []
                        for Y in (Yu, Yd, Yl):
                            s = np.linalg.svd(Y, compute_uv=False); o += [s[1] / s[0], s[2] / s[0]]
                        data[c][ib, ic, ir, ip, ih] = o + tic.ckm_left(Yu, Yd)
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


def where(i):
    b, c, r, p, h = i
    return {"base": BASE[b], "cand": rbs.CANDS[c], "rho": rbs.RHO[r], "phi_deg": 15 * int(p), "hor": rbs.HORS[h]}


for c, X in data.items():
    L = np.log(np.maximum(X[..., :9], 1e-300))
    six = np.max(np.abs(L[..., :6] - T6), axis=-1); nine = np.max(np.abs(L - T9), axis=-1)
    R2 = np.exp(L[..., 4] - L[..., 2]); R1 = np.exp(L[..., 3] - L[..., 5]); D = R2 * R1
    res = {}
    for key, arr, mask in (("best six", six, None), ("best nine", nine, None), ("D-matched best six", six, np.abs(D - P094) <= 3 * SIG),
                           ("GJ-ratio best six", six, (R2 >= 2) & (R2 <= 4.5) & (R1 >= 2) & (R1 <= 4.5))):
        a_ = np.where(mask, arr, np.inf) if mask is not None else arr
        i = np.unravel_index(np.argmin(a_), a_.shape)
        res[key] = None if not np.isfinite(a_[i]) else {"value": math.exp(a_[i]), "rows": int(mask.sum()) if mask is not None else int(arr.size),
                                                        "where": where(i), "D": float(D[i]), "R2": float(R2[i]), "R1": float(R1[i]),
                                                        "six": math.exp(six[i]), "nine": math.exp(nine[i]), "J": float(X[i][9]),
                                                        "model_over_measured": np.exp(L[i] - T9).round(3).tolist()}
    rows = L.reshape(-1, 9)
    q6, _ = cKDTree(rows[:, :6]).query(d6, k=1, p=np.inf); q9, _ = cKDTree(rows).query(d9, k=1, p=np.inf)
    res["six random as good"] = float(np.mean(q6 <= np.min(six) + 1e-12)); res["nine random as good"] = float(np.mean(q9 <= np.min(nine) + 1e-12))
    res["per base: baseline six (rho 1e-4), best six, best nine"] = [[BASE[b], float(np.exp(np.min(six[b, :, 0]))), float(np.exp(np.min(six[b]))),
                                                                     float(np.exp(np.min(nine[b])))] for b in range(len(BASE))]
    OUT[f"Clebsch {c}"] = res
    b6, b9, dm, gj = res["best six"], res["best nine"], res["D-matched best six"], res["GJ-ratio best six"]
    say(f"route (b), S for every sector, second direction Clebsch {c}: best six {b6['value']:.3f} (R2 {b6['R2']:.2f}, R1 {b6['R1']:.2f}, "
        f"D {b6['D']:.2f}; nine there {b6['nine']:.2f}) at {b6['where']}; best nine {b9['value']:.3f} (D {b9['D']:.2f}, R2 {b9['R2']:.2f}, "
        f"R1 {b9['R1']:.2f}); D-matched " + (f"{dm['rows']} rows, best six {dm['value']:.3f} (nine {dm['nine']:.2f})" if dm else "none")
        + "; GJ-ratio " + (f"{gj['rows']} rows, best six {gj['value']:.3f} (nine {gj['nine']:.2f})" if gj else "none")
        + f"; random as good six {res['six random as good']:.4f}, nine {res['nine random as good']:.4f}")
    say("   per base (baseline / best six / best nine): " + "; ".join(f"{p[0]}: {p[1]:.2f} / {p[2]:.2f} / {p[3]:.2f}" for p in res["per base: baseline six (rho 1e-4), best six, best nine"]))
(HERE / "route_b_sall.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "route_b_sall_run.txt").write_text("\n".join(LOG) + "\n")
