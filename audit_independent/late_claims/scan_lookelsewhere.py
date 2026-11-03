"""Look-elsewhere scans on the agy seat's FR-COV 'Golden' cell (frozen commit dfe4c6f90).

T1  tau map: chi2 over B1825's full tau domain (Re in [-1/2,1/2], Im in [1,4]) on agy's cell
    ((2/5,0), F_10, L_2, S~S~S~, Theorem-7 characters); hyperbolic-measure pass fraction.
T2  how many 'natural' closed-form tau candidates land in the pass region.
T3  scalar-Higgs character scan: (1+c_u^2), (1+c_d^2) over 8th roots of unity, both sqrt branches,
    c_e over 8th roots of unity: how many pass at their best tau / at tau_Golden.
"""
from __future__ import annotations

import itertools
import json
import math
import time

import numpy as np

from agy_eval import (
    CD7, CE7, CU7, PHI, TAU_FIT_TREE, TAU_GOLDEN, chi2, l2_of, matter, observables, passes,
)

OUT = {}

# ---------------- T1: tau map ----------------
t0 = time.time()
re_g = np.linspace(-0.5, 0.5, 101)
im_g = np.linspace(1.0, 4.0, 121)
chi = np.full((len(im_g), len(re_g), 3), np.nan)
mats_cache = {}
for i, y in enumerate(im_g):
    for j, x in enumerate(re_g):
        tau = complex(x, y)
        try:
            mats = matter(tau, 0.4, "0", l2_of(y), n_terms=10, dps=15, n_pts=48)
            mats_cache[(i, j)] = mats
            raw = observables(tau, mats=mats)
            s, c, t, _ = chi2(raw)
            chi[i, j] = (s, c, t)
        except Exception as e:  # noqa: BLE001
            pass
dx = re_g[1] - re_g[0]
dy = im_g[1] - im_g[0]
w = (dx * dy) / (im_g[:, None] ** 2) * np.ones((1, len(re_g)))
ok = np.isfinite(chi[..., 2])
pass_mask = ok & (chi[..., 0] <= 16.811893829770927) & (chi[..., 1] <= 15.086272469388987) & (chi[..., 2] <= 23.209251158954356)
mu_dom = float(np.sum(w[ok]))
mu_pass = float(np.sum(w[pass_mask]))
imin = np.unravel_index(np.nanargmin(chi[..., 2]), chi[..., 2].shape)
OUT["T1_tau_map"] = {
    "grid": [len(re_g), len(im_g)],
    "domain": "Re[-0.5,0.5] x Im[1,4] (B1825 domain)",
    "n_points_finite": int(ok.sum()),
    "n_points_pass": int(pass_mask.sum()),
    "hyperbolic_pass_fraction": mu_pass / mu_dom,
    "bits_L_tau_honest": -math.log2(mu_pass / mu_dom) if mu_pass > 0 else None,
    "grid_min_chi2_ten": float(chi[imin][2]),
    "grid_argmin_tau": [float(re_g[imin[1]]), float(im_g[imin[0]])],
    "pass_bbox_re": [float(re_g[np.where(pass_mask.any(0))[0].min()]), float(re_g[np.where(pass_mask.any(0))[0].max()])] if pass_mask.any() else None,
    "pass_bbox_im": [float(im_g[np.where(pass_mask.any(1))[0].min()]), float(im_g[np.where(pass_mask.any(1))[0].max()])] if pass_mask.any() else None,
    "secs": time.time() - t0,
}
np.savez_compressed("t1_tau_map.npz", re=re_g, im=im_g, chi=chi, pass_mask=pass_mask)
print(json.dumps(OUT["T1_tau_map"], indent=1))

# ---------------- T2: natural closed-form tau candidates ----------------
s5 = 5 ** 0.5
re_c = {"0": 0.0, "1/2": 0.5, "-1/2": -0.5, "1/sqrt5": 1 / s5, "-1/sqrt5": -1 / s5, "1/phi": 1 / PHI, "1/phi^2": 1 / PHI ** 2,
        "-1/phi^2": -1 / PHI ** 2, "2/5": 0.4, "-2/5": -0.4, "1/5": 0.2, "-1/5": -0.2, "1/3": 1 / 3, "-1/3": -1 / 3, "1/4": 0.25, "-1/4": -0.25,
        "3/8": 0.375, "1/sqrt3": 1 / 3 ** 0.5, "1/e": 1 / math.e, "1/pi": 1 / math.pi, "phi-1": PHI - 1, "sqrt5-2": s5 - 2, "3/7": 3 / 7, "1/sqrt7": 1 / 7 ** 0.5}
im_c = {"phi": PHI, "phi^2": PHI ** 2, "phi^3/2": PHI ** 3 / 2, "sqrt5": s5, "sqrt7": 7 ** 0.5, "sqrt6": 6 ** 0.5, "sqrt8": 8 ** 0.5, "e": math.e,
        "pi-1/2": math.pi - 0.5, "5/2": 2.5, "8/3": 8 / 3, "3": 3.0, "2": 2.0, "sqrt3*3/2": 1.5 * 3 ** 0.5, "Vol(m004)": 2.0298832128193072,
        "4/sqrt3*2": 8 / 3 ** 0.5 / 1.0 if False else 2 * 4 / 3 ** 0.5 / 2, "(1+sqrt5)": 1 + s5, "pi/phi+.. no": math.pi / PHI * 1.0, "2*phi-1/2": 2 * PHI - 0.5,
        "sqrt(5)+1/2": s5 + 0.5, "4*sqrt14/5": 4 * 14 ** 0.5 / 5, "sqrt(84)/3": 84 ** 0.5 / 3, "11/4": 2.75, "phi+1": PHI + 1, "3*phi/2+.. ": 1.5 * PHI + 0.2}
cands = []
for (rn, rv), (inn, iv) in itertools.product(re_c.items(), im_c.items()):
    if not (1.0 <= iv <= 4.0):
        continue
    tau = complex(rv, iv)
    raw = observables(tau)
    s, c, t, _ = chi2(raw)
    cands.append({"re": rn, "im": inn, "tau": [rv, iv], "chi2": [s, c, t], "pass": passes(s, c, t)})
n_pass = sum(c["pass"] for c in cands)
OUT["T2_natural_tau_candidates"] = {
    "n_candidates": len(cands),
    "n_pass": n_pass,
    "passing": [(c["re"], c["im"], round(c["chi2"][2], 3)) for c in cands if c["pass"]],
}
print(json.dumps(OUT["T2_natural_tau_candidates"], indent=1))

# ---------------- T3: scalar-Higgs character scan ----------------
roots8 = [np.exp(2j * math.pi * k / 8) for k in range(8)]


def c_from_target(chi_t, branch):
    c = np.sqrt(chi_t - 1.0 + 0j)
    return -c if branch == 0 else c


combos = []
for ku, bu, kd, bd, ke in itertools.product(range(8), range(2), range(8), range(2), range(8)):
    combos.append((ku, bu, kd, bd, ke))
cu_arr = {(k, b): c_from_target(roots8[k], b) for k in range(8) for b in range(2)}
ce_arr = {k: roots8[k] for k in range(8)}

# reference: agy's Theorem-7 choice index
ref = None
for (k, b), v in cu_arr.items():
    if abs(v - CU7) < 1e-12:
        ref_u = (k, b)
for (k, b), v in cu_arr.items():
    if abs(v - CD7) < 1e-12:
        ref_d = (k, b)
ref_e = [k for k, v in ce_arr.items() if abs(v - CE7) < 1e-12][0]
OUT["T3_reference_index"] = {"u": ref_u, "d": ref_d, "e": ref_e}

# coarse tau grid (subsample of T1) for best-tau search
sub_i = list(range(0, len(im_g), 3))
sub_j = list(range(0, len(re_g), 3))
from origin_axiom.sm_19_gate import _f10_st_and_scalar  # noqa: E402
from origin_axiom.operator_gate import ckm_full_diagnostics, quaternionic_4d_yukawa  # noqa: E402
from origin_axiom.sm_19_gate import C3_SHIFTED_TARGETS_10, SIGMA_LOG_10  # noqa: E402

t0 = time.time()
best = {}
golden_mats = matter(TAU_GOLDEN, 0.4, "0", l2_of(TAU_GOLDEN.imag), n_terms=14, dps=20, n_pts=64)
pts = [(i, j) for i in sub_i for j in sub_j if (i, j) in mats_cache] + [("G", "G")]
for (i, j) in pts:
    if i == "G":
        tau = TAU_GOLDEN
        mats = golden_mats
    else:
        tau = complex(re_g[j], im_g[i])
        mats = mats_cache[(i, j)]
    h_st, b_st = _f10_st_and_scalar(tau)
    # up / down / lepton yukawas per character
    yu = {key: quaternionic_4d_yukawa(v * b_st, h_st, *mats["up"]) for key, v in cu_arr.items()}
    yd = {key: quaternionic_4d_yukawa(v * b_st, h_st, *mats["down"]) for key, v in cu_arr.items()}
    lep = {}
    for k, v in ce_arr.items():
        se = np.sort(np.linalg.svd(quaternionic_4d_yukawa(v * b_st, h_st, *mats["lepton"]), compute_uv=False))
        lep[k] = (se[1] / se[2], se[0] / se[2])
    for keyu in cu_arr:
        for keyd in cu_arr:
            try:
                d = ckm_full_diagnostics(yu[keyu], yd[keyd])
            except Exception:  # noqa: BLE001
                continue
            q = np.array([d["up_ratios"][1], d["up_ratios"][0], d["down_ratios"][1], d["down_ratios"][0], d["V_us"], d["V_cb"], d["V_ub"], d["abs_J"]])
            for ke, (r1, r0) in lep.items():
                raw = np.array([q[0], q[1], q[2], q[3], r1, r0, q[4], q[5], q[6], q[7]])
                with np.errstate(divide="ignore", invalid="ignore"):
                    z = (np.log(raw) - np.log(C3_SHIFTED_TARGETS_10)) / SIGMA_LOG_10
                if not np.all(np.isfinite(z)):
                    continue
                six = float(np.sum(z[:6] ** 2)); ckm = float(np.sum(z[6:] ** 2)); ten = six + ckm
                key = (keyu, keyd, ke)
                if i == "G":
                    best.setdefault(key, {})["golden"] = (six, ckm, ten)
                else:
                    cur = best.setdefault(key, {}).get("best")
                    if cur is None or ten < cur[2]:
                        best[key]["best"] = (six, ckm, ten, float(tau.real), float(tau.imag))

n_total = len(best)
n_pass_best = sum(1 for v in best.values() if "best" in v and passes(*v["best"][:3]))
n_pass_golden = sum(1 for v in best.values() if "golden" in v and passes(*v["golden"]))
ranked = sorted(((v["best"][2], k) for k, v in best.items() if "best" in v))
ref_key = (ref_u, ref_d, ref_e)
ref_rank = [k for _, k in ranked].index(ref_key) + 1 if ref_key in [k for _, k in ranked] else None
OUT["T3_character_scan"] = {
    "n_character_combos": n_total,
    "tau_grid_points": len(pts) - 1,
    "n_pass_at_best_grid_tau": n_pass_best,
    "n_pass_at_tau_golden": n_pass_golden,
    "theorem7_choice_rank_by_best_chi2_ten": ref_rank,
    "theorem7_choice_best": best[ref_key].get("best"),
    "top10": [(round(t, 3), str(k), best[k]["best"][3:]) for t, k in ranked[:10]],
    "secs": time.time() - t0,
}
print(json.dumps(OUT["T3_character_scan"], indent=1))
json.dump(OUT, open("scan_results.json", "w"), indent=1, default=str)
