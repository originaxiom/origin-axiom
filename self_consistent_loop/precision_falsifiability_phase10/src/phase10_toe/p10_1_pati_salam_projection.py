"""Gate P10-1: Pati-Salam SU(2)_R x U(1)_{B-L} -> U(1)_Y Projection cos(theta_R) = sqrt(3/5)
on `v12_dP8_ps` & RG-Quasi-Invariance Audit (`0 of 19` Track A — Zero Empirical Inputs).
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

mp.mp.dps = 50
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _random_haar_u(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    q = q * (d / np.abs(d))
    return q / (np.linalg.det(q) ** (1.0 / n))


def _rhs76(_t: float, y: np.ndarray) -> np.ndarray:
    g = y[0:3]
    yu = (y[3:12] + 1j * y[12:21]).reshape(3, 3)
    yd = (y[21:30] + 1j * y[30:39]).reshape(3, 3)
    ye = (y[39:48] + 1j * y[48:57]).reshape(3, 3)
    lam = float(y[57])
    knu = (y[58:67] + 1j * y[67:76]).reshape(3, 3)
    g1, g2, g3 = g
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    c1 = 1.0 / (16.0 * math.pi * math.pi)
    c2 = c1 * c1
    hu, hd, he = yu @ yu.conj().T, yd @ yd.conj().T, ye @ ye.conj().T
    tu, td, te = float(np.real(np.trace(hu))), float(np.real(np.trace(hd))), float(np.real(np.trace(he)))
    tr_tot = 3.0 * tu + 3.0 * td + te
    b2 = np.array([[3.98, 2.7, 8.8], [0.9, 35.0 / 6.0, 12.0], [1.1, 4.5, -26.0]])
    cy = np.array([[1.7, 0.5, 1.5], [1.5, 1.5, 0.5], [2.0, 2.0, 0.0]])
    dg = c1 * np.array([4.1, -19.0 / 6.0, -7.0]) * (g**3) + c2 * (g**3) * (b2 @ np.array([g12, g22, g32]) - cy @ np.array([tu, td, te]))
    tu2, td2, te2, tud = (
        float(np.real(np.trace(hu @ hu))),
        float(np.real(np.trace(hd @ hd))),
        float(np.real(np.trace(he @ he))),
        float(np.real(np.trace(hu @ hd))),
    )
    chi2 = -2.25 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.5 * tud
    y2g = (
        ((85.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * tu
        + ((25.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * td
        + ((75.0 / 8.0) * g12 + (15.0 / 8.0) * g22) * te
    )
    dyu = c1 * ((1.5 * (hu - hd) + (tr_tot - 0.85 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ yu) + c2 * (
        1.5 * (hu @ hu) - hu @ hd - 0.25 * (hd @ hu) + 2.75 * (hd @ hd) - 2.25 * tr_tot * hu - 12.0 * lam * hu
        + (chi2 + y2g + 6.0 * (lam**2) + (1187.0 / 600.0) * (g12**2) - 0.45 * g12 * g22 + (19.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (223.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * hu - (43.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * hd
    ) @ yu
    dyd = c1 * ((1.5 * (hd - hu) + (tr_tot - 0.25 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ yd) + c2 * (
        1.5 * (hd @ hd) - hd @ hu - 0.25 * (hu @ hd) + 2.75 * (hu @ hu) - 2.25 * tr_tot * hd - 12.0 * lam * hd
        + (chi2 + y2g + 6.0 * (lam**2) - (127.0 / 600.0) * (g12**2) - 1.35 * g12 * g22 + (31.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (187.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * hd - (79.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * hu
    ) @ yd
    dye = c1 * ((1.5 * he + (tr_tot - 2.25 * g12 - 2.25 * g22) * np.eye(3)) @ ye) + c2 * (
        1.5 * (he @ he) - 2.25 * tr_tot * he - 12.0 * lam * he
        + (chi2 + y2g + 6.0 * (lam**2) + (1371.0 / 200.0) * (g12**2) + 1.35 * g12 * g22 - 5.75 * (g22**2)) * np.eye(3)
        + (387.0 / 80.0 * g12 + 135.0 / 16.0 * g22) * he
    ) @ ye
    gp2 = 0.6 * g12
    dlam = c1 * (24.0 * (lam**2) + lam * (4.0 * tr_tot - 9.0 * g22 - 3.0 * gp2) - 2.0 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.125 * (g22**2) + 0.75 * g22 * gp2 + 0.375 * (gp2**2)) + c2 * (
        -312.0 * (lam**3) - 144.0 * (lam**2) * tu + 36.0 * (lam**2) * (3.0 * g22 + gp2) - 3.0 * lam * (tu**2)
        + lam * tu * (80.0 * g32 + 22.5 * g22 + (85.0 / 6.0) * gp2) - 32.0 * g32 * (tu**2) - (8.0 / 3.0) * gp2 * (tu**2) + 30.0 * (tu**3)
    )
    dknu = c1 * (-1.5 * (he @ knu + knu @ he.T) + (-3.0 * g22 + 4.0 * lam + 2.0 * tr_tot) * knu)
    return np.concatenate([dg.real, dyu.real.ravel(), dyu.imag.ravel(), dyd.real.ravel(), dyd.imag.ravel(), dye.real.ravel(), dye.imag.ravel(), [float(dlam)], dknu.real.ravel(), dknu.imag.ravel()])


def run_gate_p10_1_pati_salam_projection() -> Dict[str, Any]:
    """Construct pure Track-A v12_dP8_ps operators and solve zero-input RGEs (0 empirical inputs)."""
    mp.mp.dps = 50
    p9 = json.loads((PROJECT_ROOT.parent / "zero_input_precision_phase9" / "outputs" / "phase9_results.json").read_text(encoding="utf-8"))
    ser = p9["gate_p9_5_track_b_scorecard"]["serialized_v11_operators"]

    # 1. Explicit 16x16 Spin(10) Matrix Trace Benchmark (Guardrails 2 & 4):
    t3r_diag = np.array([0.0] * 6 + [-0.5] * 3 + [0.5] * 3 + [0.0] * 2 + [0.5] + [-0.5])
    half_bl_diag = np.array([1.0 / 6.0] * 6 + [-1.0 / 6.0] * 3 + [-1.0 / 6.0] * 3 + [-0.5] * 2 + [0.5] + [0.5])
    t3r_16 = np.diag(t3r_diag)
    hbl_16 = np.diag(half_bl_diag)
    y_16 = t3r_16 + hbl_16

    tr_t3r_sq = float(np.trace(t3r_16 @ t3r_16))
    tr_hbl_sq = float(np.trace(hbl_16 @ hbl_16))
    tr_orth = float(np.trace(t3r_16 @ hbl_16))
    tr_y_sq = float(np.trace(y_16 @ y_16))
    tr_t3r_y = float(np.trace(t3r_16 @ y_16))
    cos_theta_r = math.sqrt(tr_t3r_y / tr_y_sq)
    sin_theta_r_plant = math.sqrt(1.0 - tr_t3r_y / tr_y_sq)

    ym_v11 = [np.array(r) + 1j * np.array(im) for r, im in zip(ser["Ym_m004_real"], ser["Ym_m004_imag"])]
    yw_v11 = [np.array(r) + 1j * np.array(im) for r, im in zip(ser["Yw_weave_real"], ser["Yw_weave_imag"])]
    k_u = np.array(ser["K_v10_real"]) + 1j * np.array(ser["K_v10_imag"])
    au0 = ser["au_0"]
    mrs = ser["mrs_v11"]

    ym_v12 = [ym_v11[0], ym_v11[1] * cos_theta_r, ym_v11[2] * cos_theta_r, ym_v11[3]]
    yw_v12 = [yw_v11[0], yw_v11[1] * cos_theta_r, yw_v11[2] * cos_theta_r, yw_v11[3]]
    yw_wrong_sin_plant = [yw_v11[0], yw_v11[1] * sin_theta_r_plant, yw_v11[2] * sin_theta_r_plant, yw_v11[3]]
    yw_wrong_inv_cos_plant = [yw_v11[0], yw_v11[1] / cos_theta_r, yw_v11[2] / cos_theta_r, yw_v11[3]]

    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = float(2 * mp.re(hl1)), float(2 * mp.im(hl1))
    eps1 = (math.exp(-2.9745505801732 * ell1) / abs(2 * np.sinh(0.5 * (ell1 + 1j * th1)))) / (2 * math.pi)
    lc = (4 * (math.pi**2 / 15) / eps1) ** 0.2
    ln_mpl_mkk_adams = 2.0 * lc + 0.5 * math.log(3.0)
    vew_over_mpl_0 = math.exp(-9.5 * lc) / math.sqrt(3.0)

    reg_i, reg_h = 0.5 * math.log(2.0 * math.pi), 0.5 * math.log(2.0)
    t_i, t_h = [0.8, 6.0, 5.0], [8.2, 3.0, 4.0]
    rsh_g = [(-1.0 / (8.0 * math.pi**2)) * (-3.5 * t_i[i] * reg_i - 3.5 * t_h[i] * reg_h) for i in range(3)]
    d_sh = [rsh_g[i] - rsh_g[2] for i in range(3)]

    def eval_zero_input(y_list: List[np.ndarray], bm: Optional[List[np.ndarray]] = None) -> Tuple[float, Dict[str, float], Dict[str, float]]:
        def rge_at(lr_v: float, b_m=None):
            ig3 = au0 / (4.0 * math.pi)
            guv = np.sqrt(1.0 / np.array([ig3 + d_sh[0], ig3 + d_sh[1], ig3 + d_sh[2]]))
            gb = float(np.mean(guv))
            sf = gb / float(np.max(np.linalg.svd(y_list[0], compute_uv=False)))
            yu0, yd0, ye0, ynu0 = y_list[0] * sf, y_list[1] * sf, y_list[2] * sf, y_list[3] * sf
            ynt = float(np.max(np.linalg.svd(ynu0, compute_uv=False)))
            knu0 = ((ynt**2) / mrs) * k_u.copy()
            lam0 = ((gb**2) / 8.0) * ((0.1272571765 * math.sqrt((1.0 / au0) / 0.04)) ** 2)
            if b_m is not None:
                uq, uu, ud, ul, ue = b_m
                yu0, yd0, ye0, knu0 = uq @ yu0 @ uu.conj().T, uq @ yd0 @ ud.conj().T, ul @ ye0 @ ue.conj().T, ul @ knu0 @ ul.T
            y0 = np.concatenate([guv.real, yu0.real.ravel(), yu0.imag.ravel(), yd0.real.ravel(), yd0.imag.ravel(), ye0.real.ravel(), ye0.imag.ravel(), [lam0], knu0.real.ravel(), knu0.imag.ravel()])
            sol = solve_ivp(_rhs76, (0.0, -lr_v), y0, method="DOP853", rtol=1e-11, atol=1e-13)
            yf = sol.y[:, -1]
            g1_v, g2_v, g3_v = yf[0:3]
            yu = (yf[3:12] + 1j * yf[12:21]).reshape(3, 3)
            yd = (yf[21:30] + 1j * yf[30:39]).reshape(3, 3)
            ye = (yf[39:48] + 1j * yf[48:57]).reshape(3, 3)
            lam = float(yf[57])
            knu = 0.5 * ((yf[58:67] + 1j * yf[67:76]).reshape(3, 3) + (yf[58:67] + 1j * yf[67:76]).reshape(3, 3).T)
            wu, su_d, _ = np.linalg.svd(yu)
            wd, sd_d, _ = np.linalg.svd(yd)
            we, se_d, _ = np.linalg.svd(ye)
            wnu, snu_d, _ = np.linalg.svd(knu)
            wu_a, su = wu[:, ::-1], su_d[::-1]
            wd_a, sd = wd[:, ::-1], sd_d[::-1]
            we_a, se = we[:, ::-1], se_d[::-1]
            wnu_a, snu = wnu[:, ::-1], snu_d[::-1]
            vc = wu_a.conj().T @ wd_a
            avc = np.abs(vc)
            jq = abs(float(np.imag(vc[0, 1] * vc[1, 2] * np.conj(vc[0, 2]) * np.conj(vc[1, 1]))))
            up = we_a.conj().T @ wnu_a
            aup = np.abs(up)
            s13_sq = float(aup[0, 2] ** 2)
            c13_sq = max(1.0 - s13_sq, 1e-15)
            mw_v = float(0.5 * g2_v)
            mh_v = math.sqrt(2.0 * max(lam, 0.0))
            mz_v = float(0.5 * math.sqrt(g2_v * g2_v + 0.6 * g1_v * g1_v))
            aem_inv = float((4.0 * math.pi) * (1.0 / (0.6 * g1_v * g1_v) + 1.0 / (g2_v * g2_v)))
            a3 = float((g3_v * g3_v) / (4.0 * math.pi))
            aux = {"alpha_EM_inv_MZ_pred": aem_inv, "alpha_s_MZ_pred": a3}
            return mz_v, {
                "sin2_thetaW_MZ_MSbar": float((0.6 * g1_v * g1_v) / (g2_v * g2_v + 0.6 * g1_v * g1_v)),
                "MW_over_vEW": mw_v,
                "MZ_over_vEW": mz_v,
                "mH_over_vEW": mh_v,
                "mH_over_MW": mh_v / mw_v,
                "m_t_over_vEW": float(su[2] / math.sqrt(2.0)),
                "mt_over_mb": float(su[2] / sd[2]),
                "mb_over_mtau": float(sd[2] / se[2]),
                "mc_over_mt": float(su[1] / su[2]),
                "mu_over_mc": float(su[0] / su[1]),
                "ms_over_mb": float(sd[1] / sd[2]),
                "md_over_ms": float(sd[0] / sd[1]),
                "mmu_over_mtau": float(se[1] / se[2]),
                "me_over_mmu": float(se[0] / se[1]),
                "V_us": float(avc[0, 1]),
                "V_cb": float(avc[1, 2]),
                "V_ub": float(avc[0, 2]),
                "abs_J_q": jq,
                "sin2_theta12": float((aup[0, 1] ** 2) / c13_sq),
                "sin2_theta23": float((aup[1, 2] ** 2) / c13_sq),
                "sin2_theta13": s13_sq,
                "abs_J_lep_max": abs(float(np.imag(up[0, 1] * up[1, 2] * np.conj(up[0, 2]) * np.conj(up[1, 1])))),
                "delta_m21_sq_over_delta_m31_sq": float((snu[1] ** 2 - snu[0] ** 2) / (snu[2] ** 2 - snu[0] ** 2)),
                "mnu3_over_vEW": 0.5 * math.exp(-lr_v) * float(snu[2]),
            }, aux

        lr_fp = float(brentq(lambda l: l - (7.5 * lc - math.log(rge_at(l)[0])), 27.0, 32.0, xtol=1e-12))
        _, pr, aux = rge_at(lr_fp, bm)
        return lr_fp, pr, aux

    lr_v12, pred_v12, aux_v12 = eval_zero_input(yw_v12)
    _, pred_sin_plant, _ = eval_zero_input(yw_wrong_sin_plant)
    _, pred_inv_cos_plant, _ = eval_zero_input(yw_wrong_inv_cos_plant)

    wu_uv, _, _ = np.linalg.svd(yw_v12[0])
    wd_uv, sd_uv_d, _ = np.linalg.svd(yw_v12[1])
    _, se_uv_d, _ = np.linalg.svd(yw_v12[2])
    sd_uv = sd_uv_d[::-1]
    se_uv = se_uv_d[::-1]
    vc_uv = wu_uv[:, ::-1].conj().T @ wd_uv[:, ::-1]
    jq_uv = abs(float(np.imag(vc_uv[0, 1] * vc_uv[1, 2] * np.conj(vc_uv[0, 2]) * np.conj(vc_uv[1, 1]))))
    uv_vals = {
        "ms_over_mb": float(sd_uv[1] / sd_uv[2]),
        "mmu_over_mtau": float(se_uv[1] / se_uv[2]),
        "V_cb": float(abs(vc_uv[1, 2])),
        "V_ub": float(abs(vc_uv[0, 2])),
        "abs_J_q": jq_uv,
    }
    max_rg_drift_dex = max(abs(math.log10(pred_v12[k] / uv_vals[k])) for k in uv_vals)

    rng_h = np.random.default_rng(20261130)
    keys_s = sorted(pred_v12.keys())
    v_ref = np.array([pred_v12[k] for k in keys_s])
    haar_max = 0.0
    for _ in range(10):
        _, pr_h, _ = eval_zero_input(yw_v12, [_random_haar_u(3, rng_h) for _ in range(5)])
        vr = np.array([pr_h[k] for k in keys_s])
        haar_max = max(haar_max, float(np.max(np.abs(vr - v_ref) / np.maximum(np.abs(v_ref), 1.0))))

    passed = bool(
        abs(tr_t3r_sq - 2.0) < 1e-15
        and abs(tr_y_sq - 10.0 / 3.0) < 1e-15
        and abs(tr_orth) < 1e-15
        and abs(cos_theta_r - math.sqrt(0.6)) < 1e-15
        and haar_max < 1.0e-11
        and max_rg_drift_dex < 0.15
    )
    assert passed, "Gate P10-1 failed"

    return {
        "gate": "P10-1_pati_salam_electroweak_projection_and_rg_quasi_invariance",
        "gate_p10_1_passed": passed,
        "spin10_16plet_trace_benchmarks": {
            "tr_T3R_sq": tr_t3r_sq,
            "tr_half_BL_sq": tr_hbl_sq,
            "tr_T3R_dot_half_BL": tr_orth,
            "tr_Y_sq": tr_y_sq,
            "cos_theta_R_sqrt_3_over_5": cos_theta_r,
        },
        "v12_zero_input_fixed_point_track_a": {
            "alpha_GUT_inv_2wall_0": au0,
            "ln_MKK_MZ_0": lr_v12,
            "alpha_EM_inv_MZ_pred": aux_v12["alpha_EM_inv_MZ_pred"],
            "alpha_s_MZ_pred": aux_v12["alpha_s_MZ_pred"],
            "vEW_over_MPl_red_pred": vew_over_mpl_0,
            "ln_MPl_red_over_MZ_pred": ln_mpl_mkk_adams + lr_v12,
            "haar_10trial_SU3x5_max_err": haar_max,
            "remaining_tier2_max_rg_drift_dex": max_rg_drift_dex,
        },
        "sm24_v12_zero_input_predictions_track_a": pred_v12,
        "planted_fault_signals_track_a": {
            "wrong_inverse_cos_mt_over_mb_plant": pred_inv_cos_plant["mt_over_mb"],
            "wrong_sin_theta_R_mt_over_mb_plant": pred_sin_plant["mt_over_mb"],
        },
        "_Ym_v12": ym_v12,
        "_Yw_v12": yw_v12,
        "_K_v10_unit": k_u,
        "_mrs_v12": mrs,
        "_overtones": ser["overtones"],
    }
