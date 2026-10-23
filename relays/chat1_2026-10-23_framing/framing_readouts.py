#!/usr/bin/env python3
"""POST HOC read-outs for the framing note, labelled (written after every output they read had been read; committed
before their own run).  Not tests; they bound two statements the note makes.
  F1  CP across the day's four stored scans (the zero-free census, ZERO_FREE_HOLOMORPHIC, TICK_LINE_HIGGS, RIGID_TAU's
      family A), for the menu read S, the menu read S~, main's DR read S~ in every sector, and main's DR in its split
      reading (up S~, down and leptons S), all with c = 3: the largest |J| over all rows; the share of rows with
      |J| >= 3.08e-5 / 3; the largest |J| among rows whose nine is within 3 and within 5; and the best nine among rows
      whose |J| is within a factor 3 of 3.08e-5.
  F2  the scale, an estimate: one-loop Standard Model running of the nine targets from M_Z to 2e16 GeV (rg_ratios.py's
      equations, extended: ln(y_c/y_t) and ln(y_u/y_t) run with -3/2 (y_t^2 - y_b^2), the down ratios with +3/2 (y_t^2 -
      y_b^2), the lepton ratios with -3/2 y_tau^2, |V_cb| and |V_ub| with +3/2 (y_t^2 + y_b^2), |V_us| fixed; the
      light Yukawas and mixing in the leading terms neglected), and PRECISION_BAR's chi-square minima over all rows
      against the M_Z targets and against the run ones, per model and scan.
    python3 -B framing_readouts.py      # writes framing_readouts.json"""
import hashlib, json, math, subprocess, pathlib
import numpy as np
from scipy.integrate import solve_ivp

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
OUT = {}

# F2's running (rg_ratios.py's equations and inputs, with the exponents integrated)
MZ = 91.1876; vv = 246.0 / math.sqrt(2)
G0 = [math.sqrt(5 / 3) * 0.3578, 0.6517, 1.2177]


def rhs(t, Y):
    g1, g2, g3, yt, yb, ytau, e1, e2, e3 = Y
    k = 1 / (16 * math.pi ** 2)
    T = 3 * yt ** 2 + 3 * yb ** 2 + ytau ** 2
    dyt = k * yt * (1.5 * (yt ** 2 - yb ** 2) + T - (17 / 20 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2))
    dyb = k * yb * (1.5 * (yb ** 2 - yt ** 2) + T - (1 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2))
    dytau = k * ytau * (1.5 * ytau ** 2 + T - (9 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2))
    return [k * 41 / 10 * g1 ** 3, k * (-19 / 6) * g2 ** 3, k * (-7) * g3 ** 3, dyt, dyb, dytau,
            k * 1.5 * (yt ** 2 - yb ** 2), k * 1.5 * (yt ** 2 + yb ** 2), k * 1.5 * ytau ** 2]


sol = solve_ivp(rhs, [0, math.log(2e16 / MZ)], G0 + [v["t"] / vv, v["b"] / vv, v["tau"] / vv, 0.0, 0.0, 0.0], rtol=1e-10, atol=1e-13)
E1, E2, E3 = sol.y[6, -1], sol.y[7, -1], sol.y[8, -1]
SHIFT = np.array([-E1, -E1, +E1, +E1, -E3, -E3, 0.0, +E2, +E2])     # ln(target at 2e16 GeV / target at M_Z)
T9H = T9 + SHIFT
OUT["F2 the running, M_Z to 2e16 GeV (one loop, SM, estimate)"] = {
    "factors on the nine targets": np.exp(SHIFT).round(4).tolist(), "J factor": float(math.exp(2 * E2)),
    "order": ["m_c/m_t", "m_u/m_t", "m_s/m_b", "m_d/m_b", "m_mu/m_tau", "m_e/m_tau", "|V_us|", "|V_cb|", "|V_ub|"]}

SCANS = {
    "zero-free census": (R / "chat1_2026-10-23_zero_free_frame" / "zero_free_census_index.json", R / "chat1_2026-10-23_zero_free_frame" / "zero_free_census.npz", None),
    "ZERO_FREE_HOLOMORPHIC": (R / "chat1_2026-10-23_zero_free_frame" / "zero_free_holomorphic_index.json", R / "chat1_2026-10-23_zero_free_frame" / "zero_free_holomorphic.npz", None),
    "TICK_LINE_HIGGS": (R / "chat1_2026-10-23_tick_line" / "tick_line_index.json", R / "chat1_2026-10-23_tick_line" / "tick_line.npz", None),
    "RIGID_TAU family A": (R / "chat1_2026-10-23_rigid_tau" / "rigid_tau_index.json", R / "chat1_2026-10-23_rigid_tau" / "rigid_tau.npz", "A"),
}
SEC = {"S": (0, 4, 8), "St": (2, 6, 10)}
CKMI = {("S", "S"): 12, ("S", "St"): 16, ("St", "S"): 20, ("St", "St"): 24}
MODELS = {"menu, S": (["F_6", "F_-2", "F_22"], "S", "S"), "menu, S~": (["F_6", "F_-2", "F_22"], "St", "St"),
          "DR, S~": (["dR"], "St", "St"), "DR, split (up S~)": (["dR"], "St", "S")}


def rows(X, dirs_all, dirs, ru, rd, c=3.0):
    Ls, Js = [], []
    for d in dirs:
        Y = X[:, dirs_all.index(d)]
        iu, idn, il = SEC[ru][0], SEC[rd][1], SEC[rd][2]
        L = np.concatenate([Y[..., iu:iu + 2], Y[..., idn:idn + 2], Y[..., il:il + 2]], axis=-1) * math.log(10)
        L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
        k = CKMI[(ru, rd)]
        Ls.append(np.concatenate([L, np.log(np.maximum(Y[..., k:k + 3], 1e-300))], axis=-1).reshape(-1, 9))
        Js.append(Y[..., k + 3].reshape(-1))
    return np.concatenate(Ls), np.concatenate(Js)


for scan, (ip, dp, fam) in SCANS.items():
    I = json.loads(ip.read_text()); X = np.load(dp)["data"].astype(np.float64)
    if fam:
        X = X[[k for k, p in enumerate(I["points"]) if p[0] == fam]]
    res = {}
    for name, (dirs, ru, rd) in MODELS.items():
        L9, J = rows(X, I["dirs"], dirs, ru, rd)
        aJ = np.abs(J)
        nine = np.max(np.abs(L9 - T9), axis=1)
        okJ = (aJ >= JPDG / 3) & (aJ <= 3 * JPDG)
        chi6 = np.sum(((L9[:, :6] - T6) / SIG[:6]) ** 2, axis=1); chi9 = np.sum(((L9 - T9) / SIG) ** 2, axis=1)
        chi6h = np.sum(((L9[:, :6] - T9H[:6]) / SIG[:6]) ** 2, axis=1); chi9h = np.sum(((L9 - T9H) / SIG) ** 2, axis=1)
        nineh = np.max(np.abs(L9 - T9H), axis=1); sixh = np.max(np.abs(L9[:, :6] - T9H[:6]), axis=1)
        r = {"rows": int(len(J)), "max |J|": float(aJ.max()), "share with |J| >= JPDG/3": float(np.mean(aJ >= JPDG / 3)),
             "best nine": float(math.exp(nine.min()))}
        for cut in (3.0, 5.0):
            g = nine <= math.log(cut)
            r[f"rows with nine <= {cut}"] = int(g.sum())
            r[f"max |J| among them ({cut})"] = float(aJ[g].max()) if g.any() else None
        r["rows with |J| within a factor 3 of 3.08e-5"] = int(okJ.sum())
        r["best nine among them"] = float(math.exp(nine[okJ].min())) if okJ.any() else None
        r["min chi2_six, M_Z targets"] = float(chi6.min()); r["min chi2_nine, M_Z targets"] = float(chi9.min())
        r["min chi2_six, 2e16 GeV targets (SM)"] = float(chi6h.min()); r["min chi2_nine, 2e16 GeV targets (SM)"] = float(chi9h.min())
        r["best six, 2e16 GeV targets"] = float(math.exp(sixh.min())); r["best nine, 2e16 GeV targets"] = float(math.exp(nineh.min()))
        res[name] = r
    OUT[f"F1 and F2: {scan}"] = res
    del X
(HERE / "framing_readouts.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
