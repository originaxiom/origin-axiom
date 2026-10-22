#!/usr/bin/env python3
"""POST HOC, labelled: every number §4 and §5 of THE_SELECTION_MAP.md quote from chat1's exploratory scans, recomputed
from posthoc_scans.json (the committed re-run of those scans), plus the scans' calibrations under main's prior:
  - the Higgs's flavour components at tau = 1/2 + 3.08i (main's B1691 q-series, through two_ingredients_census);
  - fine_scan: main's readings (up S~, down and leptons S) with the Clebsch 3, the best six per (Re tau, line), and the
    Im tau profile of the best;
  - readings_scan: at 1/2 + 3.1i on (2/5, 1/2), maximal horocycle, the CKM moduli for (up, down) readings
    (S~, S), (S~, S~), (S, S), and the up sector's m1/m3 with S against the data;
  - allst_scan: S~ for every sector with the Clebsch 3, the best nine, where, and J;
  - the nine's calibration (main's r_masses + r_ckm, seed 1720, 4 000) on allst_scan's rows, four ways:
      (a) draws as in two_ingredients_compare.py (4 000 six-target sets, then 4 000 nine-target sets);
      (b) draws in main's B1720 order (4 000 six, 4 000 r_ckm, then 4 000 nine);
      (c) the reading's look-elsewhere: data and every random target take the best of the three one-reading-for-all
          models (S, S~ or conjS for every sector);
      (d) every target takes the best of all 27 (up, down, lepton) reading combinations.
Targets: the record's pinned files at main's 3412bf09d.
    python3 -B posthoc_check.py      # writes posthoc_check.json and posthoc_check_run.txt"""
import cmath, hashlib, importlib.util, json, math, random, subprocess, pathlib
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
P = json.loads((HERE / "posthoc_scans.json").read_text())
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


def vec(r, hor, cu, cd, cl, c):
    vals = r[f"up|{hor}|{cu}"] + r[f"down|{hor}|{cd}"] + r[f"lep|{hor}|{cl}"] + r[f"ckm|{hor}|{cu}|{cd}"][:3]
    x = np.log(np.maximum(np.array(vals, dtype=float), 1e-300)); x[4] += math.log(c); x[5] -= math.log(c)
    return x


def w(x, t):
    return float(np.exp(np.max(np.abs(x[:len(t)] - t))))


# the Higgs at 1/2 + 3.08i
spec = importlib.util.spec_from_file_location("tic", HERE / "two_ingredients_census.py")
tic = importlib.util.module_from_spec(spec); spec.loader.exec_module(tic)
av = [complex(tic.te.ev(cc, tic.mp.mpc(0.5, 3.08))) for cc in tic.te.B[1]]
nrm = math.sqrt(sum(abs(a) ** 2 for a in av))
OUT["higgs_at_half_plus_3.08i"] = {"abs": [abs(a) for a in av], "abs_normalised": [abs(a) / nrm for a in av],
                                   "phase_deg": [math.degrees(cmath.phase(a)) for a in av],
                                   "h_dot_h_over_norm2": abs(sum(a * a for a in av)) / nrm ** 2}
say("Higgs at 1/2 + 3.08i (i, j, k): |.| " + ", ".join(f"{x:.3f}" for x in OUT["higgs_at_half_plus_3.08i"]["abs"])
    + " (normalised " + ", ".join(f"{x:.3f}" for x in OUT["higgs_at_half_plus_3.08i"]["abs_normalised"]) + ")"
    + "; phases " + ", ".join(f"{x:.0f}" for x in OUT["higgs_at_half_plus_3.08i"]["phase_deg"])
    + f" deg; |h.h|/|h|^2 = {OUT['higgs_at_half_plus_3.08i']['h_dot_h_over_norm2']:.3f}")

# fine_scan: main's readings with the Clebsch
best = None
for r in P["fine_scan"]:
    for hor in ("L_max", "L_2"):
        x = vec(r, hor, "St", "S", "S", 3); ww = w(x, T6)
        if best is None or ww < best[0]:
            best = (ww, r["tau"], r["line"], hor)
OUT["fine_scan_best_six_main_readings_clebsch"] = best
say(f"fine_scan, main's readings with the Clebsch: best six {best[0]:.3f} at tau {best[1]}, line {best[2]}, {best[3]}")
prof = sorted((r["tau"][1], w(vec(r, best[3], "St", "S", "S", 3), T6)) for r in P["fine_scan"]
              if r["tau"][0] == best[1][0] and r["line"] == best[2])
OUT["fine_scan_profile"] = prof
say("  profile: " + " ".join(f"{a:.2f}:{b:.2f}" for a, b in prof if abs(a - best[1][1]) <= 0.21))
for re_t in (0.0, 0.25, 0.5):
    bb = min((w(vec(r, hor, "St", "S", "S", 3), T6), r["tau"], r["line"], hor) for r in P["fine_scan"] if r["tau"][0] == re_t
             for hor in ("L_max", "L_2"))
    say(f"  best at Re tau = {re_t}: {bb[0]:.3f} at Im {bb[1][1]}, line {bb[2]}, {bb[3]}")
    OUT[f"fine_scan_best_at_Re_{re_t}"] = bb

# readings_scan
r0 = [r for r in P["readings_scan"] if r["tau"] == [0.5, 3.1] and abs(r["line"][1] - 0.5) < 1e-9][0]
ck = {f"{cu}-{cd}": r0[f"ckm|L_max|{cu}|{cd}"][:3] for cu, cd in (("St", "S"), ("St", "St"), ("S", "S"))}
OUT["readings_scan_ckm_half_plus_3.1i_line_2/5_1/2_Lmax"] = ck
say("readings_scan at 1/2 + 3.1i, (2/5, 1/2), L_max: " + "; ".join(f"{k}: " + ", ".join(f"{x:.4f}" for x in val) for k, val in ck.items()))
ratio = r0["up|L_max|S"][1] / (v["u"] / v["t"])
OUT["up_m1_over_m3_with_S_over_data"] = ratio
say(f"  the up sector's m1/m3 with S over the data: {ratio:.0f}")

# allst_scan: S~ for every sector with the Clebsch
rows = P["allst_scan"]
M = {}
for cu in ("S", "St", "conjS"):
    for cd in ("S", "St", "conjS"):
        for cl in ("S", "St", "conjS"):
            M[(cu, cd, cl)] = np.array([vec(r, hor, cu, cd, cl, 3) for r in rows for hor in ("L_max", "L_2")])
lab = [(r["tau"], r["line"], hor, r[f"ckm|{hor}|St|St"][3]) for r in rows for hor in ("L_max", "L_2")]
A = M[("St", "St", "St")]
w9 = np.exp(np.max(np.abs(A - T9), axis=1)); i9 = int(np.argmin(w9))
OUT["allst_best_nine_St_all_clebsch"] = {"best": float(w9[i9]), "at": lab[i9]}
say(f"allst_scan, S~ for every sector with the Clebsch: best nine {w9[i9]:.3f} at {lab[i9][0]}, line {lab[i9][1]}, {lab[i9][2]}, J {lab[i9][3]:.2e}")


def bestw(Ms, t):
    return min(float(np.min(np.exp(np.max(np.abs(Mx - t), axis=1)))) for Mx in Ms)


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


N = 4000
rng = random.Random(1720); [r_masses(rng) for _ in range(N)]
dA = [np.log(np.array(r_masses(rng) + r_ckm(rng))) for _ in range(N)]
rng = random.Random(1720); [r_masses(rng) for _ in range(N)]; [r_ckm(rng) for _ in range(N)]
dB = [np.log(np.array(r_masses(rng) + r_ckm(rng))) for _ in range(N)]
one = [M[(x, x, x)] for x in ("S", "St", "conjS")]
allm = list(M.values())
obs1, obs27 = bestw(one, T9), bestw(allm, T9)
cal = {"a_sealed_order": float(np.mean([bestw([A], d) <= w9[i9] + 1e-12 for d in dA])),
       "b_main_B1720_order": float(np.mean([bestw([A], d) <= w9[i9] + 1e-12 for d in dB])),
       "c_one_reading_for_all_look_elsewhere": float(np.mean([bestw(one, d) <= obs1 + 1e-12 for d in dA])),
       "d_all_27_combinations": float(np.mean([bestw(allm, d) <= obs27 + 1e-12 for d in dA])),
       "data_best_one_reading": obs1, "data_best_27": obs27}
OUT["allst_nine_calibration"] = cal
say("  calibration of the nine (fraction of random targets fitting as well): "
    f"(a) sealed draw order {cal['a_sealed_order']:.4f}; (b) main's order {cal['b_main_B1720_order']:.4f}; "
    f"(c) best of the three one-reading models {cal['c_one_reading_for_all_look_elsewhere']:.4f} (data {obs1:.3f}); "
    f"(d) best of all 27 combinations {cal['d_all_27_combinations']:.4f} (data {obs27:.3f})")
(HERE / "posthoc_check.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "posthoc_check_run.txt").write_text("\n".join(LOG) + "\n")
