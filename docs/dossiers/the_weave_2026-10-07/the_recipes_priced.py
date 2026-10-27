#!/usr/bin/env python3
"""W161 — the plan's stage 1, second part: the agy branch's ten Higgs recipes (B1762) on this seat's own code, the
whole menu priced, and held out at the strip's 38 rows (the rule: W161_RULE.md, committed and pushed before this
script).  It runs once, from the repository root.

The recipes are B1762's definitions, rebuilt on W158's basis couplings (S reading for every sector, the leptons with
H_d, c = 3, B1757's nine2).  B1762's and B1757's JSON files are read from the agy branch's head by their git blobs, for
K1 and the read-outs only.

  K0  the pins and the rows; the up Gram's 1 + 2 block and Sigma_lep = P Sigma_down P at B1757's four points
  K1  B1762 reproduced: 40 (recipe, point) chi2_nine and |J| to 1e-5 relative
  K2  the menu priced: the data's least chi2_nine over the 40 under both nulls (seeds 1849-1868)
  K3  held out: no recipe below 21.67 at any of the 38 rows
  R   read-outs

    python3 -B docs/dossiers/the_weave_2026-10-07/the_recipes_priced.py
"""
import contextlib
import io
import json
import math
import platform
import sys
import time
import traceback
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from scipy.spatial import cKDTree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_two_special_higgs as W58      # noqa: E402  (W158: basis couplings, rows, pins; W157, W152 under it)
    import the_higgs_orbit_pair as W59       # noqa: E402  (W159: the forced group's action on directions)
W57, T8, T42 = W58.W57, W58.T8, W58.T42

REV = W58.REV
FILES, PIN = W58.FILES, W58.PIN
V49, V53 = W58.V49, W58.V53
AGY = "05e6caabf"
J62 = "frontier/B1762_zero_parameter_two_doublet_law_and_ten_observables/verification/zero_param_two_doublets.json"
J57 = "frontier/B1757_step_twos_free_doublets_at_the_strip/verification/free_doublets.json"
OUT = HERE / "the_recipes_priced.json"
SEEDS = tuple(range(1849, 1869))
BAR6, BAR9 = 16.75, 21.67
LN3 = math.log(3)
J_PDG, J_SIG = 3.08e-5, 0.15e-5
LINE0 = (Fr(2, 5), Fr(1, 10))
POINTS = [(0.3145, 3.0345), (0.333333, 3.055050), (0.3145, 3.10), (0.3145, 2.95)]
NAMES = ["B0_single_higgs_vdr", "B1_unboosted_hu_hd_p1", "L1_decoupled_block_hd", "L1_boost_p1", "L1p_boost_pnat",
         "L2_anomalous_up_p1", "L2p_anomalous_up_pnat", "L3_schur_im_p1", "L3p_schur_im_pnat", "L4p_schur_rot_pnat"]
P_E1 = np.diag([-1.0, 1.0, 1.0])
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


# ============================================================================================ B1762's definitions
def gauge_h1(v):
    v = np.asarray(v, dtype=complex)
    v = v / np.linalg.norm(v)
    return v * np.exp(-1j * np.angle(v[1]))


def mat_pow_herm(H, p):
    ev, U = np.linalg.eigh(H)
    return (U * (ev ** p)) @ U.conj().T


def grams(B):
    out = {}
    for sec in T8.SECTS:
        bY = B[sec]["S"]
        S = np.array([[np.trace(bY[c].conj().T @ bY[d]) for d in range(3)] for c in range(3)])
        out[sec] = S / np.trace(S).real
    return out


def recipes(B, tau):
    """the ten (H_u, H_d) of B1762, from the Grams and the record's DR at tau"""
    Sg = grams(B)
    Su, Sd = Sg["up"], Sg["down"]
    DR = np.array(T8.higgs_DR(tau))
    dr, drc = gauge_h1(DR), gauge_h1(np.conj(DR))
    v = np.array([0.0 + 0.0j, drc[1], drc[2]])
    delta = 0.5 * float(np.real(Su[0, 0]))
    p = 1.0 + delta
    hd1 = gauge_h1(np.linalg.inv(np.conj(Sd)) @ v)
    hdp = gauge_h1(mat_pow_herm(np.conj(Sd), -p) @ v)
    e1 = np.conj(-(Sd[0, 1] * dr[1] + Sd[0, 2] * dr[2]) / Sd[0, 0])
    hd12 = np.linalg.inv(np.conj(Sd[1:, 1:])) @ v[1:]
    hdd = gauge_h1(np.array([e1, hd12[0], hd12[1]]))
    boost = float(np.real(np.vdot(v, Su @ v))) / float(np.real(Su[0, 0]))
    z0 = boost * (-dr[0])
    z2 = z0 * np.exp(1j * delta)
    z3 = complex(z0.real, abs(e1))
    z4 = z0 * np.exp(2j * abs(e1))

    def hu(z):
        return gauge_h1([z, drc[1], drc[2]])

    pairs = [(drc, drc), (drc, hd1), (hu(z0), hdd), (hu(z0), hd1), (hu(z0), hdp), (hu(z2), hd1), (hu(z2), hdp),
             (hu(z3), hd1), (hu(z3), hdp), (hu(z4), hdp)]
    info = {"boost": boost, "delta": delta, "p": p, "|e1|": float(abs(e1)),
            "up off-block": float(np.linalg.norm([Su[0, 1], Su[0, 2], Su[1, 0], Su[2, 0]]) / np.linalg.norm(Su)),
            "lep parity": float(np.linalg.norm(Sg["lep"] - P_E1 @ Sd @ P_E1) / np.linalg.norm(Sd))}
    return pairs, info, hd1, hdp


def nine_of(B, hu, hd, t9, s9):
    """B1757's nine2 on W158's basis: up from H_u, down and leptons from H_d, S reading, c = 3; and J"""
    Y = {"up": W58.Y_of(B, "up", "S", hu), "down": W58.Y_of(B, "down", "S", hd), "lep": W58.Y_of(B, "lep", "S", hd)}
    six = []
    for s in T8.SECTS:
        sv = np.maximum(np.linalg.svd(Y[s], compute_uv=False), 1e-300)
        six += [math.log(sv[1] / sv[0]), math.log(sv[2] / sv[0])]
    six = np.array(six) + np.array([0, 0, 0, 0, LN3, -LN3])
    Uu, _ = W58.lefts(Y["up"])
    Ud, _ = W58.lefts(Y["down"])
    v = W58.ckm_from(Uu, Ud)
    f = np.concatenate([six, np.log(np.maximum(v[:3], 1e-300))])
    pulls = (f - t9) / s9
    return f, pulls, v[3]


def fs(u, w):
    return W58.fs_angle(np.asarray(u, dtype=complex), np.asarray(w, dtype=complex))


# ============================================================================================ main
def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W161", "rule": "W161_RULE.md", "status": "one run", "rev": REV, "agy": AGY,
           "python": sys.version.split()[0], "numpy": np.__version__, "machine": platform.machine()}
    try:
        run(root, out)
    except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
        out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out.get("cells"), indent=1))
    if "run_failed" in out:
        print("run failed")


def run(root, out):
    files = {p: T8.git_bytes(root, REV, p) for p in FILES}
    out["pins"] = {p: T8.sha256(files[p]) == h for p, h in PIN.items()}
    b62 = T8.git_bytes(root, AGY, J62)
    b57 = T8.git_bytes(root, AGY, J57)
    out["agy files (sha256)"] = {J62: T8.sha256(b62), J57: T8.sha256(b57)}
    d62 = json.loads(b62.decode("utf-8"))
    d57 = [r for r in json.loads(b57.decode("utf-8")) if r["hor"] == "L_max"]
    t6, t9 = T8.targets(files)
    sg = T42.sigma(files)
    s9 = np.concatenate([sg, T42.sigma_ckm(files)])
    W93, W89 = T8.own_modules(root)
    col = T8.L_column(files)
    L = T8.own_lines()
    kline = L.index(LINE0)
    G = W59.group()
    # ---------------------------------------------------------------- K0, K1 and the menu at B1757's four points
    k0 = {"up off-block max": 0.0, "lep parity max": 0.0}
    k1 = {"worst chi2_nine relative": 0.0, "worst |J| relative": 0.0, "pairs compared": 0, "failing": []}
    stored = {(round(r["tau"][0], 6), round(r["tau"][1], 6)): r for r in d62["strip_records"]}
    feats, meta, per_point = [], [], []
    for (x, y) in POINTS:
        tau = complex(x, y)
        B = W58.basis(W93, W89, col, L[kline], x, y, "L_max")
        pairs, info, hd1, hdp = recipes(B, tau)
        k0["up off-block max"] = max(k0["up off-block max"], info["up off-block"])
        k0["lep parity max"] = max(k0["lep parity max"], info["lep parity"])
        ref = stored.get((round(x, 6), round(y, 6)))
        rows = {}
        for name, (hu, hd) in zip(NAMES, pairs):
            f, pulls, J = nine_of(B, hu, hd, t9, s9)
            c9 = float((pulls ** 2).sum())
            rows[name] = {"chi2_nine": c9, "chi2_six": float((pulls[:6] ** 2).sum()),
                          "CKM part": float((pulls[6:] ** 2).sum()), "J": J, "pull J": (abs(J) - J_PDG) / J_SIG,
                          "model over measured": np.exp(f - t9).tolist()}
            feats.append(f / s9)
            meta.append(((x, y), name))
            if ref is not None:
                rv = ref["laws"][name]
                e9 = abs(c9 / rv["chi2_nine_MZ"] - 1)
                eJ = abs(abs(J) / rv["abs_J_CKM"] - 1)
                k1["worst chi2_nine relative"] = max(k1["worst chi2_nine relative"], e9)
                k1["worst |J| relative"] = max(k1["worst |J| relative"], eJ)
                k1["pairs compared"] += 1
                if e9 > 1e-5 or eJ > 1e-5:
                    k1["failing"].append([x, y, name, c9, rv["chi2_nine_MZ"]])
        # read-outs at this point: the inverse Gram against B1757's fit, and W159's orbit
        fit = next((r for r in d57 if abs(r["tau"][0] - x) < 1e-6 and abs(r["tau"][1] - y) < 1e-6), None)
        DR = np.array(T8.higgs_DR(tau))
        imgs = [W59.act(g, DR) for g in G]
        rd = {"tau": [x, y], "recipe numbers": info, "recipes": rows,
              "hd_1 to DR's orbit, least angle (deg)": min(fs(hd1, h) for h in imgs)}
        if fit is not None:
            Hu = np.array([complex(a, b) for a, b in fit["H_u"]])
            Hd = np.array([complex(a, b) for a, b in fit["H_d"]])
            rd["B1757 chi2_nine"] = fit["chi2_nine"]
            rd["hd_1 to B1757's H_d (deg)"] = fs(hd1, Hd)
            rd["hd_p to B1757's H_d (deg)"] = fs(hdp, Hd)
            rd["B1757's H_d to DR's orbit, least angle (deg)"] = min(fs(Hd, h) for h in imgs)
            rd["B1757's H_u to DR's orbit, least angle (deg)"] = min(fs(Hu, h) for h in imgs)
        per_point.append(rd)
    out["K0"] = {"pins": out["pins"], **k0}
    out["K1"] = k1
    out["the four points"] = per_point
    X = np.array(feats)
    c2 = ((X - t9 / s9) ** 2).sum(1)
    i0 = int(np.argmin(c2))
    obs = float(c2[i0])
    out["the data's least over the 40"] = {"chi2_nine": obs, "point": list(meta[i0][0]), "recipe": meta[i0][1]}
    # ---------------------------------------------------------------- K2, the nulls
    tree = cKDTree(X)
    fa, fb = [], []
    for s in SEEDS:
        _six, nine = T8.own_draws(s, T8.NTARGET)
        N = np.array(nine)
        Ta = np.concatenate([np.tile(t6, (len(N), 1)), N[:, 6:9]], axis=1) / s9
        Tb = N / s9
        da = tree.query(Ta, k=1)[0] ** 2
        db = tree.query(Tb, k=1)[0] ** 2
        fa.append(float(np.mean(da <= obs + 1e-9)))
        fb.append(float(np.mean(db <= obs + 1e-9)))
    out["K2"] = {"null (a), the data's six with random mixings: fraction_mean": float(np.mean(fa)),
                 "null (b), random nines: fraction_mean": float(np.mean(fb)), "per seed (a)": fa, "per seed (b)": fb}
    # ---------------------------------------------------------------- K3, the 38 rows held out
    rows_all = []
    for name, path in (("B1749", V49), ("B1753", V53)):
        rows = T8.census_rows(files[path + "/census.jsonl"])
        _arr, lab, best, _arg = W57.below_rows(rows, t6, sg)
        for i in range(len(best)):
            if best[i] < BAR6:
                k, x, y, hor = lab[i]
                rows_all.append((name, k, x, y, hor))
    out["rows"] = len(rows_all)
    held = {n: [] for n in NAMES}
    jp = {n: [] for n in NAMES}
    below = []
    for (name, k, x, y, hor) in rows_all:
        tau = complex(x, y)
        B = W58.basis(W93, W89, col, L[k], x, y, hor)
        pairs, _info, _h1, _hp = recipes(B, tau)
        for rn, (hu, hd) in zip(NAMES, pairs):
            _f, pulls, J = nine_of(B, hu, hd, t9, s9)
            c9 = float((pulls ** 2).sum())
            held[rn].append(c9)
            jp[rn].append((abs(J) - J_PDG) / J_SIG)
            if c9 < BAR9:
                below.append([name, k, x, y, hor, rn, c9])
    out["K3"] = {"rows below 21.67": below,
                 "per recipe": {n: {"least": float(min(held[n])), "median": float(np.median(held[n])),
                                    "J pull range": [float(min(jp[n])), float(max(jp[n]))]} for n in NAMES}}
    out["cells"] = {
        "K0": bool(out["rows"] == 38 and all(out["pins"].values()) and k0["up off-block max"] < 1e-12
                   and k0["lep parity max"] < 1e-12),
        "K1": bool(k1["pairs compared"] == 40 and not k1["failing"]),
        "K2": bool(np.mean(fa) <= 0.01 and np.mean(fb) <= 0.01),
        "K3": bool(not below)}


if __name__ == "__main__":
    main()
