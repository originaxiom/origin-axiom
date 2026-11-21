"""Gate P9-2: Two-Wall Contino-Pilo S^1/Z_2 Threshold (-ln pi) & Zero-Input Gauge/Hierarchy
Fixed Point (`0 of 19` Track A — Zero Empirical Inputs).

Enforces Guardrails 1, 2, 3, 4, 5:
  - 50-digit Zeta/Hurwitz benchmark for 2 * ((1/2) ln pi) = ln pi across both collar boundaries (y = 0, y = Lc*).
  - Zero shooting against empirical PDG couplings: solves pure internal fixed point
    ln(M_KK / M_Z)_0 = (15/2)*Lc* - ln(M_Z^pred / v_EW) at alpha_GUT_2wall^-1 = 42.10164.
  - Mandatory 10-trial dynamic SU(3)^5 Haar unitary basis scrambling (< 1e-11) on all 24 pure Track-A SM ratios.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

mp.mp.dps = 50


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


def run_gate_p9_2_zero_input_couplings(g1_raw: Dict[str, Any]) -> Dict[str, Any]:
    """Solve pure Track-A zero-input gauge couplings, hierarchy ratios, and 24 SM ratios (0 empirical inputs)."""
    mp.mp.dps = 50
    yw_v11 = g1_raw["_Yw_v11"]
    k_u = g1_raw["_K_v10_unit"]
    mrs_v11 = g1_raw["_mrs_v11"]

    # 1. 50-Digit Zeta/Hurwitz Benchmark for the 2-Wall Contino-Pilo Threshold (Guardrail 4):
    zeta_p0 = mp.diff(mp.zeta, mp.mpf(0))
    hurwitz_p0_half = mp.diff(lambda s: mp.zeta(s, mp.mpf("0.5")), mp.mpf(0))
    one_wall_cp = (-zeta_p0) - (-hurwitz_p0_half)
    two_wall_cp = 2 * one_wall_cp
    two_wall_err_50d = float(abs(two_wall_cp - mp.log(mp.pi)))

    # 2. Pure Track-A Zero-Anchor Scales & 2-Wall Threshold Coupling:
    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = 2 * mp.re(hl1), 2 * mp.im(hl1)
    lam1 = mp.mpf("2.9745505801732")
    eps1_mp = (mp.exp(-lam1 * ell1) / abs(2 * mp.sinh((ell1 + 1j * th1) / 2))) / (2 * mp.pi)
    lc_mp = (4 * (mp.pi**2 / 15) / eps1_mp) ** mp.mpf("0.2")
    vol_m5_mp = 10 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))

    lc = float(lc_mp)
    agut_inv_bulk = float((9 * vol_m5_mp * ((2 * lc_mp) ** 3)) / (30 * (mp.pi**3)))
    agut_inv_2wall = float(mp.mpf(str(agut_inv_bulk)) - two_wall_cp)
    agut_inv_wrong_plus_plant = float(mp.mpf(str(agut_inv_bulk)) + two_wall_cp)

    ln_mpl_mkk_adams = float(2 * lc_mp + mp.log(3) / 2)
    ln_mkk_vew_hosotani = float(mp.mpf("7.5") * lc_mp)
    ln_mpl_vew_0 = ln_mpl_mkk_adams + ln_mkk_vew_hosotani
    vew_over_mpl_0 = float(mp.exp(-mp.mpf("9.5") * lc_mp) / mp.sqrt(3))
    unwarped_vew_over_mpl_plant = float(mp.exp(-4 * lc_mp) / mp.sqrt(3))

    reg_i, reg_h = 0.5 * math.log(2.0 * math.pi), 0.5 * math.log(2.0)
    t_i, t_h = [0.8, 6.0, 5.0], [8.2, 3.0, 4.0]
    rsh_g = [(-1.0 / (8.0 * math.pi**2)) * (-3.5 * t_i[i] * reg_i - 3.5 * t_h[i] * reg_h) for i in range(3)]
    d_sh = [rsh_g[i] - rsh_g[2] for i in range(3)]

    def eval_zero_input_rge(
        au_val: float,
        y_list: List[np.ndarray],
        mrs_val: float,
        basis_mats: Optional[List[np.ndarray]] = None,
    ) -> Tuple[float, Dict[str, float], Dict[str, float]]:
        def rge_at(lr_val: float, bm=None):
            yur, ydr, yer, ynur = y_list
            ig3 = au_val / (4.0 * math.pi)
            guv = np.sqrt(1.0 / np.array([ig3 + d_sh[0], ig3 + d_sh[1], ig3 + d_sh[2]]))
            gb = float(np.mean(guv))
            sf = gb / float(np.max(np.linalg.svd(yur, compute_uv=False)))
            yu0, yd0, ye0, ynu0 = yur * sf, ydr * sf, yer * sf, ynur * sf
            ynt = float(np.max(np.linalg.svd(ynu0, compute_uv=False)))
            knu0 = ((ynt**2) / mrs_val) * k_u.copy()
            lam0 = ((gb**2) / 8.0) * ((0.1272571765 * math.sqrt((1.0 / au_val) / 0.04)) ** 2)
            yt_uv = float(np.max(np.linalg.svd(yu0, compute_uv=False)))
            if bm is not None:
                uq, uu, ud, ul, ue = bm
                yu0, yd0, ye0, knu0 = uq @ yu0 @ uu.conj().T, uq @ yd0 @ ud.conj().T, ul @ ye0 @ ue.conj().T, ul @ knu0 @ ul.T
            y0 = np.concatenate([guv.real, yu0.real.ravel(), yu0.imag.ravel(), yd0.real.ravel(), yd0.imag.ravel(), ye0.real.ravel(), ye0.imag.ravel(), [lam0], knu0.real.ravel(), knu0.imag.ravel()])
            sol = solve_ivp(_rhs76, (0.0, -lr_val), y0, method="DOP853", rtol=1e-11, atol=1e-13)
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
            mw_v = 0.5 * g2_v
            mh_v = math.sqrt(2.0 * max(lam, 0.0))
            mz_v = 0.5 * math.sqrt(g2_v * g2_v + 0.6 * g1_v * g1_v)
            aem_inv = (4.0 * math.pi) * (1.0 / (0.6 * g1_v * g1_v) + 1.0 / (g2_v * g2_v))
            a3 = (g3_v * g3_v) / (4.0 * math.pi)
            aux = {
                "alpha_EM_inv_MZ_pred": aem_inv,
                "alpha_s_MZ_pred": a3,
                "g2_uv": float(guv[1]),
                "g2_ir": float(g2_v),
                "yt_uv": yt_uv,
                "yt_ir": float(su[2]),
            }
            sm24 = {
                "sin2_thetaW_MZ_MSbar": (0.6 * g1_v * g1_v) / (g2_v * g2_v + 0.6 * g1_v * g1_v),
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
                "mnu3_over_vEW": 0.5 * math.exp(-lr_val) * float(snu[2]),
            }
            return mz_v, sm24, aux

        lr_fp = float(brentq(lambda l: l - (7.5 * lc - math.log(rge_at(l)[0])), 27.0, 32.0, xtol=1e-12))
        _, sm24_res, aux_res = rge_at(lr_fp, basis_mats)
        return lr_fp, sm24_res, aux_res

    lr_0, sm24_0, aux_0 = eval_zero_input_rge(agut_inv_2wall, yw_v11, mrs_v11)
    ln_mpl_mz_0 = ln_mpl_mkk_adams + lr_0

    # Mandatory 10-trial dynamic SU(3)^5 Haar unitary basis scrambling (< 1e-11, Guardrail 3):
    keys_sorted = sorted(sm24_0.keys())
    vec_ref = np.array([sm24_0[k] for k in keys_sorted])
    rng_h = np.random.default_rng(20261129)
    haar_max = 0.0
    for _ in range(10):
        _, pr_h, _ = eval_zero_input_rge(agut_inv_2wall, yw_v11, mrs_v11, [_random_haar_u(3, rng_h) for _ in range(5)])
        vr = np.array([pr_h[k] for k in keys_sorted])
        haar_max = max(haar_max, float(np.max(np.abs(vr - vec_ref) / np.maximum(np.abs(vec_ref), 1.0))))

    # Pure Track-A planted-fault reference signals:
    _, _, aux_plus_plant = eval_zero_input_rge(agut_inv_wrong_plus_plant, yw_v11, mrs_v11)
    _, sm_sym_up_plant, _ = eval_zero_input_rge(agut_inv_2wall, *g1_raw["_Yw_sym_up_plant"])
    _, sm_pos_flux_plant, _ = eval_zero_input_rge(agut_inv_2wall, *g1_raw["_Yw_pos_flux_plant"])
    _, sm_lhs_wlp_plant, _ = eval_zero_input_rge(agut_inv_2wall, *g1_raw["_Yw_lhs_wlp_plant"])

    hosotani_uv = 2.25 * (aux_0["g2_uv"] ** 2) - 3.0 * (aux_0["yt_uv"] ** 2)
    hosotani_ir = 2.25 * (aux_0["g2_ir"] ** 2) - 3.0 * (aux_0["yt_ir"] ** 2)
    hosotani_no_top_plant = 2.25 * (aux_0["g2_uv"] ** 2)

    passed = bool(
        two_wall_err_50d < 1.0e-40
        and haar_max < 1.0e-11
        and hosotani_uv < 0.0
        and hosotani_ir < 0.0
        and hosotani_no_top_plant > 0.0
    )
    assert passed, "Gate P9-2 failed"

    return {
        "gate": "P9-2_two_wall_contino_pilo_and_zero_input_couplings",
        "gate_p9_2_passed": passed,
        "two_wall_contino_pilo_benchmark": {
            "one_wall_half_ln_pi": float(one_wall_cp),
            "two_wall_ln_pi": float(two_wall_cp),
            "abs_err_50d": two_wall_err_50d,
        },
        "zero_input_fixed_point_track_a": {
            "alpha_GUT_inv_bulk_0": agut_inv_bulk,
            "alpha_GUT_inv_2wall_0": agut_inv_2wall,
            "ln_MKK_MZ_0": lr_0,
            "alpha_EM_inv_MZ_pred": aux_0["alpha_EM_inv_MZ_pred"],
            "alpha_s_MZ_pred": aux_0["alpha_s_MZ_pred"],
            "vEW_over_MPl_red_pred": vew_over_mpl_0,
            "ln_MPl_red_over_vEW_pred": ln_mpl_vew_0,
            "ln_MPl_red_over_MZ_pred": ln_mpl_mz_0,
            "haar_10trial_SU3x5_max_err": haar_max,
        },
        "sm24_zero_input_predictions_track_a": sm24_0,
        "hosotani_ewsb_check": {
            "uv_coeff_with_top": hosotani_uv,
            "ir_coeff_with_top": hosotani_ir,
            "uv_coeff_without_top_plant": hosotani_no_top_plant,
        },
        "planted_fault_signals_track_a": {
            "wrong_plus_ln_pi_alpha_s_plant": aux_plus_plant["alpha_s_MZ_pred"],
            "wrong_plus_ln_pi_alpha_em_inv_plant": aux_plus_plant["alpha_EM_inv_MZ_pred"],
            "unwarped_vew_over_MPl_plant": unwarped_vew_over_mpl_plant,
            "wrong_sym_up_45_mu_over_mc_plant": sm_sym_up_plant["mu_over_mc"],
            "wrong_positive_dP8_flux_mb_over_mtau_plant": sm_pos_flux_plant["mb_over_mtau"],
            "wrong_lhs_wlp_scaling_abs_J_q_plant": sm_lhs_wlp_plant["abs_J_q"],
            "wrong_lhs_wlp_scaling_V_cb_plant": sm_lhs_wlp_plant["V_cb"],
        },
    }
