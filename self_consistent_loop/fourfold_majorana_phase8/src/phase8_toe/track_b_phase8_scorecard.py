"""Gate P8-5 (Track B): Explicitly Priced Empirical Comparison Boundary & 34-Observable
Non-Dimensionalized Joint Ledger for Phase 8 (`v10_e8_weave` -> 24 / 24 SM Tier 1+2).

Isolated strictly from all Track-A (`0 of 19`) modules per Guardrails 1 & 5.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root

mp.mp.dps = 50

PDG_24: Dict[str, float] = {
    "sin2_thetaW_MZ_MSbar": 0.23121,
    "MW_over_vEW": 80.3692 / 246.21965,
    "MZ_over_vEW": 91.1876 / 246.21965,
    "mH_over_vEW": 125.25 / 246.21965,
    "mH_over_MW": 125.25 / 80.3692,
    "m_t_over_vEW": 171.7 / 246.21965,
    "mt_over_mb": 171.7 / 2.89,
    "mb_over_mtau": 2.89 / 1.74617,
    "mc_over_mt": 0.619 / 171.7,
    "mu_over_mc": 0.00127 / 0.619,
    "ms_over_mb": 0.055 / 2.89,
    "md_over_ms": 0.00290 / 0.055,
    "mmu_over_mtau": 0.102718 / 1.74617,
    "me_over_mmu": 0.00048657 / 0.102718,
    "V_us": 0.22500,
    "V_cb": 0.04182,
    "V_ub": 0.003732,
    "abs_J_q": 3.12e-5,
    "sin2_theta12": 0.307,
    "sin2_theta23": 0.546,
    "sin2_theta13": 0.02203,
    "abs_J_lep_max": 0.033,
    "delta_m21_sq_over_delta_m31_sq": 7.41e-5 / 2.511e-3,
    "mnu3_over_vEW": 5.011e-11 / 246.21965,
}


def _classify_tier(pred: float, obs: float) -> Tuple[float, float, str]:
    frac_err = (pred - obs) / obs
    l10 = math.log10(max(pred, 1e-300) / obs)
    al = abs(l10)
    if al <= 0.15:
        tier = "Tier_1_Precision_Hit"
    elif al <= 0.50:
        tier = "Tier_2_Structural_O1_Hit"
    else:
        tier = "Tier_3_Quantitative_Tension_or_Miss"
    return frac_err, l10, tier


def _random_haar_u(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    q = q * (d / np.abs(d))
    return q / (np.linalg.det(q) ** (1.0 / n))


def _rhs76(_t: float, y: np.ndarray) -> np.ndarray:
    g = y[0:3]
    Yu = (y[3:12] + 1j * y[12:21]).reshape(3, 3)
    Yd = (y[21:30] + 1j * y[30:39]).reshape(3, 3)
    Ye = (y[39:48] + 1j * y[48:57]).reshape(3, 3)
    lam = float(y[57])
    knu = (y[58:67] + 1j * y[67:76]).reshape(3, 3)
    g1, g2, g3 = g
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    c1 = 1.0 / (16.0 * math.pi * math.pi)
    c2 = c1 * c1
    Hu, Hd, He = Yu @ Yu.conj().T, Yd @ Yd.conj().T, Ye @ Ye.conj().T
    tu, td, te = float(np.real(np.trace(Hu))), float(np.real(np.trace(Hd))), float(np.real(np.trace(He)))
    T = 3.0 * tu + 3.0 * td + te
    B2 = np.array([[3.98, 2.7, 8.8], [0.9, 35.0 / 6.0, 12.0], [1.1, 4.5, -26.0]])
    Cy = np.array([[1.7, 0.5, 1.5], [1.5, 1.5, 0.5], [2.0, 2.0, 0.0]])
    dg = c1 * np.array([4.1, -19.0 / 6.0, -7.0]) * (g**3) + c2 * (g**3) * (B2 @ np.array([g12, g22, g32]) - Cy @ np.array([tu, td, te]))
    tu2, td2, te2, tud = (
        float(np.real(np.trace(Hu @ Hu))),
        float(np.real(np.trace(Hd @ Hd))),
        float(np.real(np.trace(He @ He))),
        float(np.real(np.trace(Hu @ Hd))),
    )
    chi2 = -2.25 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.5 * tud
    y2g = (
        ((85.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * tu
        + ((25.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * td
        + ((75.0 / 8.0) * g12 + (15.0 / 8.0) * g22) * te
    )
    dYu = c1 * ((1.5 * (Hu - Hd) + (T - 0.85 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ Yu) + c2 * (
        1.5 * (Hu @ Hu) - Hu @ Hd - 0.25 * (Hd @ Hu) + 2.75 * (Hd @ Hd) - 2.25 * T * Hu - 12.0 * lam * Hu
        + (chi2 + y2g + 6.0 * (lam**2) + (1187.0 / 600.0) * (g12**2) - 0.45 * g12 * g22 + (19.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (223.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * Hu - (43.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * Hd
    ) @ Yu
    dYd = c1 * ((1.5 * (Hd - Hu) + (T - 0.25 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ Yd) + c2 * (
        1.5 * (Hd @ Hd) - Hd @ Hu - 0.25 * (Hu @ Hd) + 2.75 * (Hu @ Hu) - 2.25 * T * Hd - 12.0 * lam * Hd
        + (chi2 + y2g + 6.0 * (lam**2) - (127.0 / 600.0) * (g12**2) - 1.35 * g12 * g22 + (31.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (187.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * Hd - (79.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * Hu
    ) @ Yd
    dYe = c1 * ((1.5 * He + (T - 2.25 * g12 - 2.25 * g22) * np.eye(3)) @ Ye) + c2 * (
        1.5 * (He @ He) - 2.25 * T * He - 12.0 * lam * He
        + (chi2 + y2g + 6.0 * (lam**2) + (1371.0 / 200.0) * (g12**2) + 1.35 * g12 * g22 - 5.75 * (g22**2)) * np.eye(3)
        + (387.0 / 80.0 * g12 + 135.0 / 16.0 * g22) * He
    ) @ Ye
    gp2 = 0.6 * g12
    dlam = c1 * (24.0 * (lam**2) + lam * (4.0 * T - 9.0 * g22 - 3.0 * gp2) - 2.0 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.125 * (g22**2) + 0.75 * g22 * gp2 + 0.375 * (gp2**2)) + c2 * (
        -312.0 * (lam**3) - 144.0 * (lam**2) * tu + 36.0 * (lam**2) * (3.0 * g22 + gp2) - 3.0 * lam * (tu**2)
        + lam * tu * (80.0 * g32 + 22.5 * g22 + (85.0 / 6.0) * gp2) - 32.0 * g32 * (tu**2) - (8.0 / 3.0) * gp2 * (tu**2) + 30.0 * (tu**3)
    )
    dknu = c1 * (-1.5 * (He @ knu + knu @ He.T) + (-3.0 * g22 + 4.0 * lam + 2.0 * T) * knu)
    return np.concatenate(
        [dg.real, dYu.real.ravel(), dYu.imag.ravel(), dYd.real.ravel(), dYd.imag.ravel(), dYe.real.ravel(), dYe.imag.ravel(), [float(dlam)], dknu.real.ravel(), dknu.imag.ravel()]
    )


def run_gate_p8_5_track_b_scorecard(
    g1: Dict[str, Any],
    g2_raw: Dict[str, Any],
    g3: Dict[str, Any],
    g4: Dict[str, Any],
) -> Dict[str, Any]:
    mp.mp.dps = 50
    Y_weave = g2_raw["_Y_weave"]
    K_v10_unit = g2_raw["_K_v10_e8_unit"]
    K_diluted_unit = g2_raw["_K_diluted_unit"]
    K_pos_plant = g2_raw["_K_pos_plant"]
    mrs = float(g2_raw["mrs"])

    reg_i, reg_h = 0.5 * math.log(2.0 * math.pi), 0.5 * math.log(2.0)
    T_i, T_h = [0.8, 6.0, 5.0], [8.2, 3.0, 4.0]
    rsh_g = [(-1.0 / (8.0 * math.pi**2)) * (-3.5 * T_i[i] * reg_i - 3.5 * T_h[i] * reg_h) for i in range(3)]
    d_sh = [rsh_g[i] - rsh_g[2] for i in range(3)]

    def shoot_k(K_u: np.ndarray, au: float, lr: float, basis_mats: Optional[List[np.ndarray]] = None) -> Tuple[float, float, Dict[str, float]]:
        Yur, Ydr, Yer, Ynur = Y_weave
        ig3 = au / (4.0 * math.pi)
        guv = np.sqrt(1.0 / np.array([ig3 + d_sh[0], ig3 + d_sh[1], ig3 + d_sh[2]]))
        gb = float(np.mean(guv))
        sf = gb / float(np.max(np.linalg.svd(Yur, compute_uv=False)))
        Yu0, Yd0, Ye0, Ynu0 = Yur * sf, Ydr * sf, Yer * sf, Ynur * sf
        ynt = float(np.max(np.linalg.svd(Ynu0, compute_uv=False)))
        knu0 = ((ynt**2) / mrs) * K_u.copy()
        lam0 = ((gb**2) / 8.0) * ((0.1272571765 * math.sqrt((1.0 / au) / 0.04)) ** 2)
        if basis_mats is not None:
            UQ, Uu, Ud, UL, Ue = basis_mats
            Yu0, Yd0, Ye0, knu0 = UQ @ Yu0 @ Uu.conj().T, UQ @ Yd0 @ Ud.conj().T, UL @ Ye0 @ Ue.conj().T, UL @ knu0 @ UL.T
        y0 = np.concatenate([guv.real, Yu0.real.ravel(), Yu0.imag.ravel(), Yd0.real.ravel(), Yd0.imag.ravel(), Ye0.real.ravel(), Ye0.imag.ravel(), [lam0], knu0.real.ravel(), knu0.imag.ravel()])
        sol = solve_ivp(_rhs76, (0.0, -lr), y0, method="DOP853", rtol=1e-11, atol=1e-13)
        yf = sol.y[:, -1]
        g1_v, g2_v, g3_v = yf[0:3]
        Yu = (yf[3:12] + 1j * yf[12:21]).reshape(3, 3)
        Yd = (yf[21:30] + 1j * yf[30:39]).reshape(3, 3)
        Ye = (yf[39:48] + 1j * yf[48:57]).reshape(3, 3)
        lam = float(yf[57])
        knu = 0.5 * ((yf[58:67] + 1j * yf[67:76]).reshape(3, 3) + (yf[58:67] + 1j * yf[67:76]).reshape(3, 3).T)
        aem = (4.0 * math.pi) * (1.0 / (0.6 * g1_v * g1_v) + 1.0 / (g2_v * g2_v))
        a3 = (g3_v * g3_v) / (4.0 * math.pi)
        Wu, su_d, _ = np.linalg.svd(Yu)
        Wd, sd_d, _ = np.linalg.svd(Yd)
        We, se_d, _ = np.linalg.svd(Ye)
        Wnu, snu_d, _ = np.linalg.svd(knu)
        Wu_a, su = Wu[:, ::-1], su_d[::-1]
        Wd_a, sd = Wd[:, ::-1], sd_d[::-1]
        We_a, se = We[:, ::-1], se_d[::-1]
        Wnu_a, snu = Wnu[:, ::-1], snu_d[::-1]
        Vc = Wu_a.conj().T @ Wd_a
        aVc = np.abs(Vc)
        Jq = abs(float(np.imag(Vc[0, 1] * Vc[1, 2] * np.conj(Vc[0, 2]) * np.conj(Vc[1, 1]))))
        Up = We_a.conj().T @ Wnu_a
        aUp = np.abs(Up)
        s13_sq = float(aUp[0, 2] ** 2)
        c13_sq = max(1.0 - s13_sq, 1e-15)
        MW_v = 0.5 * g2_v
        mH_v = math.sqrt(2.0 * max(lam, 0.0))
        return aem, a3, {
            "sin2_thetaW_MZ_MSbar": (0.6 * g1_v * g1_v) / (g2_v * g2_v + 0.6 * g1_v * g1_v),
            "MW_over_vEW": MW_v,
            "MZ_over_vEW": 0.5 * math.sqrt(g2_v * g2_v + 0.6 * g1_v * g1_v),
            "mH_over_vEW": mH_v,
            "mH_over_MW": mH_v / MW_v,
            "m_t_over_vEW": float(su[2] / math.sqrt(2.0)),
            "mt_over_mb": float(su[2] / sd[2]),
            "mb_over_mtau": float(sd[2] / se[2]),
            "mc_over_mt": float(su[1] / su[2]),
            "mu_over_mc": float(su[0] / su[1]),
            "ms_over_mb": float(sd[1] / sd[2]),
            "md_over_ms": float(sd[0] / sd[1]),
            "mmu_over_mtau": float(se[1] / se[2]),
            "me_over_mmu": float(se[0] / se[1]),
            "V_us": float(aVc[0, 1]),
            "V_cb": float(aVc[1, 2]),
            "V_ub": float(aVc[0, 2]),
            "abs_J_q": Jq,
            "sin2_theta12": float((aUp[0, 1] ** 2) / c13_sq),
            "sin2_theta23": float((aUp[1, 2] ** 2) / c13_sq),
            "sin2_theta13": s13_sq,
            "abs_J_lep_max": abs(float(np.imag(Up[0, 1] * Up[1, 2] * np.conj(Up[0, 2]) * np.conj(Up[1, 1])))),
            "delta_m21_sq_over_delta_m31_sq": float((snu[1] ** 2 - snu[0] ** 2) / (snu[2] ** 2 - snu[0] ** 2)),
            "mnu3_over_vEW": 0.5 * math.exp(-lr) * float(snu[2]),
        }

    sr = root(
        lambda x: np.array([shoot_k(K_v10_unit, x[0], x[1])[0] - 127.951, (shoot_k(K_v10_unit, x[0], x[1])[1] - 0.1179) * 500.0]),
        np.array([41.988, 29.680]),
        method="hybr",
        tol=1e-11,
    )
    au_v10, lr_v10 = float(sr.x[0]), float(sr.x[1])
    _, _, pred_v10 = shoot_k(K_v10_unit, au_v10, lr_v10)
    _, _, pred_diluted = shoot_k(K_diluted_unit, au_v10, lr_v10)
    _, _, pred_pos_plant = shoot_k(K_pos_plant, au_v10, lr_v10)

    rng_h = np.random.default_rng(20261126)
    haar_max = 0.0
    vec_ref = np.array([pred_v10[k] for k in sorted(PDG_24)])
    for _ in range(10):
        _, _, pr = shoot_k(K_v10_unit, au_v10, lr_v10, [_random_haar_u(3, rng_h) for _ in range(5)])
        vr = np.array([pr[k] for k in sorted(PDG_24)])
        haar_max = max(haar_max, float(np.max(np.abs(vr - vec_ref) / np.maximum(np.abs(vec_ref), 1.0))))

    tiers_v10 = {"Tier_1_Precision_Hit": 0, "Tier_2_Structural_O1_Hit": 0, "Tier_3_Quantitative_Tension_or_Miss": 0}
    rows_v10 = {}
    for k, obs_v in PDG_24.items():
        fe, l10, tr = _classify_tier(pred_v10[k], obs_v)
        tiers_v10[tr] += 1
        rows_v10[k] = {"observed": obs_v, "v10_e8_weave_predicted": pred_v10[k], "fractional_err": fe, "log10_ratio": l10, "tier": tr}

    # Early-Universe Isocurvature Shootout Comparison (priced theta_i = 0.06052 from Omega_a h^2 = 0.120, A_s = 2.10e-9):
    theta_i_dm = 0.06052
    as_obs = 2.10e-9

    def beta_from_ratio(hi_over_2pifa: float) -> Tuple[float, float]:
        p_iso = ((2.0 / theta_i_dm) * hi_over_2pifa) ** 2
        return p_iso / (p_iso + as_obs), p_iso

    b1a = g1["branch_1A_large_radius_track_a"]
    b1b = g1["branch_1B_small_radius_self_dual_track_a"]
    b1bsd = b1b["casimir_scale_self_dual_plateau_1B_SD"]
    pf1 = g1["planted_fault_signals"]

    beta_1ai, _ = beta_from_ratio(b1a["branch_1Ai_H_I_over_2pi_feff"])
    beta_1aii, _ = beta_from_ratio(b1a["branch_1Aii_H_I_over_2pi_fMI"])
    beta_1bi_m7, _ = beta_from_ratio(b1b["high_scale_M7_4_at_R_sd_H_I_over_2pi_fa"])
    beta_1bsd, piso_1bsd = beta_from_ratio(b1bsd["H_I_over_2pi_fa_sd"])
    beta_wrong_weyl_plant, _ = beta_from_ratio(pf1["wrong_positive_weyl_H_I_over_2pi_fa"])

    as_fe, as_l10, as_tier = _classify_tier(b1bsd["A_s_predicted"], as_obs)
    ns_fe, ns_l10, ns_tier = _classify_tier(b1bsd["ns_exact"], 0.9649)
    agut_fe, agut_l10, agut_tier = _classify_tier(g4["track_a_alpha_GUT_inv_at_2Lc"], au_v10)

    tbbn_mpl = 4.0e-3 / 2.43536e18
    treh_rad_mpl = [r["ratio_to_MPl_red"] for r in g4["track_a_ten_scale_hierarchy_over_MPl_red"] if r["scale"] == "T_reh_radion"][0]
    bp_r8_log10 = g3["theorem_P8_3_critical_del_pezzo_rank"]["fano_transition_r8_P1_x_dP8"]["log10_bp_step_at_R_flux_max"]

    input_ledger = {
        "dimensionful_unit_anchor_count": 1,
        "track_a_zero_input_module_empirical_floats": 0,
        "track_b_priced_continuous_inputs": {
            "count": 3,
            "names": ["alpha_EM_inv_MZ", "alpha_s_MZ", "theta_i_axion_misalignment"],
        },
        "priced_empirical_comparison_ratios": ["T_BBN_over_MPl", "rho_Lambda_over_MPl4", "Omega_a_h2"],
        "unpriced_multi_anchor_violation_plant_excess_anchors": 2,
    }

    passed = bool(
        tiers_v10["Tier_1_Precision_Hit"] == 12
        and tiers_v10["Tier_2_Structural_O1_Hit"] == 12
        and tiers_v10["Tier_3_Quantitative_Tension_or_Miss"] == 0
        and haar_max < 1.0e-11
        and beta_1ai > 0.999
        and beta_1aii > 0.999
        and beta_1bi_m7 > 0.99
        and beta_1bsd < 0.038
        and beta_wrong_weyl_plant > 0.999
        and as_tier == "Tier_1_Precision_Hit"
        and ns_tier == "Tier_1_Precision_Hit"
        and b1bsd["r_exact"] < 0.036
        and agut_tier == "Tier_1_Precision_Hit"
        and treh_rad_mpl > tbbn_mpl
        and bp_r8_log10 <= -105.0
    )
    assert passed, "Gate P8-5 Track-B assertion failed"

    return {
        "gate_p8_5_passed": passed,
        "v10_e8_weave_calibration": {
            "alpha_GUT_inv": au_v10,
            "ln_MKK_MZ": lr_v10,
            "haar_10trial_SU3x5_max_err": haar_max,
        },
        "v10_e8_weave_tier_summary": tiers_v10,
        "v10_e8_weave_24_rows": rows_v10,
        "clause_P8_C2_sheet_coherence_disclosure": {
            "base_singlet_coherent_sin2_theta13": pred_v10["sin2_theta13"],
            "base_singlet_coherent_abs_J_lep": pred_v10["abs_J_lep_max"],
            "sheet_diluted_0p2_sin2_theta13": pred_diluted["sin2_theta13"],
            "sheet_diluted_0p2_abs_J_lep": pred_diluted["abs_J_lep_max"],
            "wrong_positive_torsion_sin2_theta13_plant": pred_pos_plant["sin2_theta13"],
            "wrong_positive_torsion_sin2_theta12_plant": pred_pos_plant["sin2_theta12"],
        },
        "isocurvature_shootout_comparison": {
            "planck_beta_iso_upper_bound": 0.038,
            "bicep_keck_r_upper_bound": 0.036,
            "priced_theta_i_for_Omega_a_h2_0p120": theta_i_dm,
            "branch_1Ai_11d_gauss_bonnet_beta_iso": beta_1ai,
            "branch_1Aii_horava_witten_wall_beta_iso": beta_1aii,
            "branch_1Bi_high_scale_M7_4_at_R_sd_beta_iso": beta_1bi_m7,
            "branch_1B_SD_casimir_self_dual": {
                "P_iso": piso_1bsd,
                "beta_iso_predicted": beta_1bsd,
                "A_s_observed": as_obs,
                "A_s_predicted": b1bsd["A_s_predicted"],
                "A_s_fractional_err": as_fe,
                "A_s_log10_ratio": as_l10,
                "A_s_tier": as_tier,
                "ns_observed": 0.9649,
                "ns_predicted": b1bsd["ns_exact"],
                "ns_prompt_gauge_reheated": b1bsd["prompt_gauge_reheated_ns_exact"],
                "ns_fractional_err": ns_fe,
                "ns_tier": ns_tier,
                "r_predicted": b1bsd["r_exact"],
            },
            "wrong_positive_weyl_beta_iso_plant": beta_wrong_weyl_plant,
            "clause_P8_C1_isocurvature_verdict": (
                "Large-radius 11D Gauss-Bonnet and 10D Horava-Witten wall mixing both fail (beta_iso > 0.9999), "
                "and high-scale V_0 = M_7^4 fails even at R_sd = M_7^-1 (beta_iso = 0.9966); the UV self-dual "
                "Casimir-scale cusp-cap plateau (1B-SD: R_sd * M_7 = 1, V_0 = |V_Cas|, mu = M_7) achieves "
                "beta_iso = 0.00784 < 0.038 and A_s = 2.63e-9 (Tier 1) with zero fitted couplings."
            ),
        },
        "gravity_and_scale_comparison": {
            "alpha_GUT_inv_2Lc_vs_calibrated": {
                "track_a_2Lc": g4["track_a_alpha_GUT_inv_at_2Lc"],
                "calibrated_v10": au_v10,
                "fractional_err": agut_fe,
                "log10_ratio": agut_l10,
                "tier": agut_tier,
            },
            "T_reh_radion_exceeds_T_BBN": bool(treh_rad_mpl > tbbn_mpl),
            "T_BBN_over_MPl_red": tbbn_mpl,
            "cy4_P1_x_dP8_bp_log10_step": bp_r8_log10,
        },
        "non_dimensionalized_input_ledger": input_ledger,
        "serialized_uv_yukawas_and_majorana": {
            "au_v10": au_v10,
            "lr_v10": lr_v10,
            "mrs": mrs,
            "Y_weave_real": [Y.real.tolist() for Y in Y_weave],
            "Y_weave_imag": [Y.imag.tolist() for Y in Y_weave],
            "K_v10_real": K_v10_unit.real.tolist(),
            "K_v10_imag": K_v10_unit.imag.tolist(),
        },
    }
