#!/usr/bin/env python3
"""POST HOC, labelled (written after route_b_readout was read; committed before its own run): four checks on route
(b)'s exploration.
  1. Calibration, as main calibrates (B1725) and as the sealed census did (two_ingredients_compare.py): random targets
     from main's generator (random.Random(1720); 4 000 six-targets, then 4 000 nine-targets), each fitted with the same
     rows; the fraction that fit at least as well as the data (Chebyshev distance in log, by a k-d tree).  Menus:
       (a) Clebsch -3, reading S~ for every sector, every direction;   (b) the same, direction h3 only;
       (c) Clebsch -3, the split reading (up S~; down and leptons S), every direction;
       (d) the Clebsch-1 control (route_b_clebsch1_control.npz), reading S~, every direction.
     Caveat written before the run: the base points were chosen as the sealed census's best six-rows, i.e. on the data,
     so these fractions favour the data; a large fraction is robust, a small one is not.
  2. The control: Clebsch -3 against Clebsch 1 (reading S~), the same summaries as route_b_readout.py.
  3. The best rows in detail (model over measured, D, J): Clebsch -3 with S~ (best six, best nine, best D-matched six),
     and the split reading's best six.
  4. Refinement with kappa continuous (Nelder-Mead in log10 rho and phi, from the grid point), Clebsch -3, reading S~:
     the six from the five best distinct (base point, direction, horocycle) triples, the nine from the three best.
    python3 -B route_b_posthoc.py      # writes route_b_posthoc.json and route_b_posthoc_run.txt"""
import contextlib, hashlib, importlib.util, io, json, math, random, subprocess, pathlib
import numpy as np
from scipy.optimize import minimize
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
IDX = json.loads((HERE / "route_b_scan_index.json").read_text())
X = np.load(HERE / "route_b_scan.npz")["data"]                       # base, cand, rho, phi, hor, model, field
XC = np.load(HERE / "route_b_clebsch1_control.npz")["data"]          # base, cand, rho, phi, hor, field (S~ only)
L3 = np.log(np.maximum(X[..., 0, :9], 1e-300))                       # Clebsch -3, S~
LM = np.log(np.maximum(X[..., 1, :9], 1e-300))                       # Clebsch -3, split reading
L1 = np.log(np.maximum(XC[..., :9], 1e-300))                         # Clebsch 1, S~
NAMES = ["m_c/m_t", "m_u/m_t", "m_s/m_b", "m_d/m_b", "m_mu/m_tau", "m_e/m_tau", "|V_us|", "|V_cb|", "|V_ub|"]
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


def where(i):
    b, c, r, p, h = i
    return {"base": IDX["base"][b], "cand": IDX["cands"][c], "rho": IDX["rho"][r], "phi_deg": IDX["phi_deg"][p], "hor": IDX["hors"][h]}


def stats(Lx):
    six = np.max(np.abs(Lx[..., :6] - T6), axis=-1); nine = np.max(np.abs(Lx - T9), axis=-1)
    D = np.exp((Lx[..., 4] - Lx[..., 2]) + (Lx[..., 3] - Lx[..., 5]))
    R2 = np.exp(Lx[..., 4] - Lx[..., 2]); R1 = np.exp(Lx[..., 3] - Lx[..., 5])
    return six, nine, D, R2, R1


def argbest(a, mask=None):
    a = np.where(mask, a, np.inf) if mask is not None else a
    i = np.unravel_index(np.argmin(a), a.shape)
    return float(np.exp(a[i])) if np.isfinite(a[i]) else None, tuple(int(k) for k in i)


# 1. calibration
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
d6 = np.log(np.array([r_masses() for _ in range(N)]))
d9 = np.log(np.array([r_masses() + r_ckm() for _ in range(N)]))
OUT["calibration"] = {}
for label, Lx in (("(a) Clebsch -3, S~, every direction", L3), ("(b) Clebsch -3, S~, h3 only", L3[:, 1:2]),
                  ("(c) Clebsch -3, split reading, every direction", LM), ("(d) Clebsch 1 control, S~, every direction", L1)):
    rows = Lx.reshape(-1, 9)
    w6 = float(np.min(np.max(np.abs(rows[:, :6] - T6), axis=1))); w9 = float(np.min(np.max(np.abs(rows - T9), axis=1)))
    q6, _ = cKDTree(rows[:, :6]).query(d6, k=1, p=np.inf); q9, _ = cKDTree(rows).query(d9, k=1, p=np.inf)
    f6 = float(np.mean(q6 <= w6 + 1e-12)); f9 = float(np.mean(q9 <= w9 + 1e-12))
    say(f"1. calibration {label}, {rows.shape[0]} rows: six {math.exp(w6):.3f} (random as good {f6:.4f}); "
        f"nine {math.exp(w9):.3f} (random as good {f9:.4f})")
    OUT["calibration"][label] = {"rows": int(rows.shape[0]), "six": math.exp(w6), "six_random_as_good": f6,
                                 "nine": math.exp(w9), "nine_random_as_good": f9}

# 2. the control: Clebsch -3 against Clebsch 1, reading S~
OUT["control"] = {}
for label, Lx in (("Clebsch -3", L3), ("Clebsch 1", L1)):
    six, nine, D, R2, R1 = stats(Lx)
    dm = np.abs(D - P094) <= 3 * SIG; gj = (R2 >= 2) & (R2 <= 4.5) & (R1 >= 2) & (R1 <= 4.5)
    w6, i6 = argbest(six); w9, i9 = argbest(nine); wd, idd = argbest(six, dm); wg, ig = argbest(six, gj)
    per = []
    for b in range(Lx.shape[0]):
        pb = argbest(six[b])[0]; pd = argbest(six[b], dm[b])[0]; pn = argbest(nine[b])[0]
        per.append({"base": IDX["base"][b], "best_six": pb, "best_nine": pn, "best_six_D_matched": pd})
    say(f"2. {label} (S~): best six {w6:.3f} (D {D[i6]:.2f}); best nine {w9:.3f}; D-matched rows {int(dm.sum())}, best six there "
        f"{('%.3f' % wd) if wd else 'none'}; GJ-ratio rows {int(gj.sum())}, best six there {('%.3f' % wg) if wg else 'none'}")
    say("   per base point, best six / best nine / best D-matched six: " + "; ".join(
        f"{p['base']}: {p['best_six']:.2f} / {p['best_nine']:.2f} / {('%.2f' % p['best_six_D_matched']) if p['best_six_D_matched'] else '-'}" for p in per))
    OUT["control"][label] = {"best_six": [w6, where(i6), float(D[i6])], "best_nine": [w9, where(i9)], "n_D_matched": int(dm.sum()),
                             "best_six_D_matched": [wd, where(idd)] if wd else None, "n_GJ_rows": int(gj.sum()),
                             "best_six_GJ_rows": [wg, where(ig)] if wg else None, "per_base": per}

# 3. the best rows in detail
OUT["detail"] = {}
six3, nine3, D3, _, _ = stats(L3); sixM, nineM, DM, _, _ = stats(LM)
for label, arr, Lx, Dx, Xr, mask in (("S~, best six", six3, L3, D3, X[..., 0, :], None), ("S~, best nine", nine3, L3, D3, X[..., 0, :], None),
                                     ("S~, best D-matched six", six3, L3, D3, X[..., 0, :], np.abs(D3 - P094) <= 3 * SIG),
                                     ("split reading, best six", sixM, LM, DM, X[..., 1, :], None)):
    val, i = argbest(arr, mask)
    mm = np.exp(Lx[i] - T9)
    say(f"3. {label}: {val:.3f} at {where(i)}; D {Dx[i]:.2f}; J {Xr[i][9]:.1e}; model/measured "
        + ", ".join(f"{n} {x:.2f}" for n, x in zip(NAMES, mm)))
    OUT["detail"][label] = {"value": val, "where": where(i), "D": float(Dx[i]), "J": float(Xr[i][9]), "model_over_measured": dict(zip(NAMES, mm.tolist()))}

# 4. refinement with kappa continuous (Clebsch -3, reading S~)
_spec = importlib.util.spec_from_file_location("rbs", HERE / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)
cacheM, OUT["refinement"] = {}, []


def setup(b, c):
    re_t, im_t, a_, b_ = IDX["base"][b]
    if b not in cacheM:
        cacheM[b] = rbs.channels(re_t, im_t, a_, b_)
    v1, v2, v3 = rbs.at(rbs.H1, re_t, im_t), rbs.at(rbs.H2, re_t, im_t), rbs.at(rbs.H3, re_t, im_t)
    u2, u3 = v2 / np.linalg.norm(v2), v3 / np.linalg.norm(v3)
    dirs = {"h2": u2, "h3": u3}
    for ang in (0, 90, 180, 270):
        dirs[f"c{ang}"] = (u2 + np.exp(1j * math.radians(ang)) * u3) / math.sqrt(2)
    return cacheM[b], rbs.S_of(v1), np.linalg.norm(v1), rbs.S_of(dirs[IDX["cands"][c]])


for target, arr, nfield, k in (("six", six3, 6, 5), ("nine", nine3, 9, 3)):
    order, seen = np.argsort(arr, axis=None), []
    for f in order:
        i = np.unravel_index(f, arr.shape)
        if (i[0], i[1], i[4]) in [(s[0], s[1], s[4]) for s in seen]:
            continue
        seen.append(i)
        if len(seen) == k:
            break
    for i in seen:
        M, S1, n1, Ss = setup(i[0], i[1]); hor = IDX["hors"][i[4]]; T = T9[:nfield]

        def obj(p):
            kap = 10 ** p[0] * np.exp(1j * p[1]) * n1
            o = np.log(np.maximum(np.array(rbs.outputs(M, hor, S1 + kap * Ss, S1 - 3 * kap * Ss, "St_all")[:nfield]), 1e-300))
            return float(np.max(np.abs(o - T)))

        p0 = [math.log10(IDX["rho"][i[2]]), math.radians(IDX["phi_deg"][i[3]])]
        res = minimize(obj, p0, method="Nelder-Mead", options={"xatol": 1e-7, "fatol": 1e-10, "maxiter": 4000})
        kap = 10 ** res.x[0] * np.exp(1j * res.x[1]) * n1
        o = np.array(rbs.outputs(M, hor, S1 + kap * Ss, S1 - 3 * kap * Ss, "St_all"))
        Dv = (o[4] / o[2]) * (o[3] / o[5])
        say(f"4. {target}: from {where(i)}: grid {math.exp(arr[i]):.3f} -> continuous {math.exp(res.fun):.3f} at rho {10 ** res.x[0]:.4g}, "
            f"phi {math.degrees(res.x[1]) % 360:.1f}; D there {Dv:.2f}")
        OUT["refinement"].append({"target": target, "from": where(i), "grid": math.exp(arr[i]), "continuous": math.exp(res.fun),
                                  "rho": 10 ** res.x[0], "phi_deg": math.degrees(res.x[1]) % 360, "D": Dv})
(HERE / "route_b_posthoc.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "route_b_posthoc_run.txt").write_text("\n".join(LOG) + "\n")
