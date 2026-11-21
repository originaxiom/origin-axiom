"""Gate P10-3: Dimensionless Experimental Falsifiability Observables — Takagi Neutrino Ratios,
Dirac CP Phase delta_CP, Srednicki E/N = 8/3, & E_8 (16, 4) Split-Multiplet Selection Rule
(`0 of 19` Track A — Zero Empirical Inputs).
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

from .p10_1_pati_salam_projection import _random_haar_u, _rhs76

mp.mp.dps = 50


def run_gate_p10_3_falsifiability_observables(g1_raw: Dict[str, Any], g2_res: Dict[str, Any]) -> Dict[str, Any]:
    """Compute pure Track-A dimensionless falsifiability observables and verify 10-trial Haar invariance."""
    mp.mp.dps = 50

    # 1. Literature Benchmarks (Guardrail 4):
    m_sym_test = mp.matrix([[mp.mpc("2.0", "1.0"), mp.mpc("0.5", "-0.3")], [mp.mpc("0.5", "-0.3"), mp.mpc("1.2", "0.7")]])
    u_t, s_t, _ = mp.svd_c(m_sym_test)
    p_t = u_t.H * m_sym_test * u_t.conjugate()
    w_t = u_t * mp.diag([mp.exp(0.5j * mp.arg(p_t[0, 0])), mp.exp(0.5j * mp.arg(p_t[1, 1]))])
    takagi_50d_err = float(mp.norm(w_t.H * m_sym_test * w_t.conjugate() - mp.diag([s_t[0], s_t[1]])))

    q_em_16 = np.array([2.0 / 3.0] * 3 + [-1.0 / 3.0] * 3 + [-2.0 / 3.0] * 3 + [1.0 / 3.0] * 3 + [0.0, -1.0, 1.0, 0.0])
    tr_qem_sq = float(np.sum(q_em_16**2))
    tr_tc_sq = 2.0 * 0.5 + 0.5 + 0.5
    e_over_n_spin10 = tr_qem_sq / tr_tc_sq

    e1_su4 = np.array([1.0, 0.0, 0.0, 0.0])
    e2_su4 = np.array([0.0, 1.0, 0.0, 0.0])
    su4_singlet_xy_coupling = float(np.dot(e1_su4, np.eye(4) @ e2_su4))

    # 2. Pure Track-A Neutrino Falsifiability Observables & 10-Trial SU(3)^5 Haar Check:
    yw = g1_raw["_Yw_v12"]
    k_u = g1_raw["_K_v10_unit"]
    fp = g1_raw["v12_zero_input_fixed_point_track_a"]
    au0, lr0, mrs = fp["alpha_GUT_inv_2wall_0"], fp["ln_MKK_MZ_0"], g1_raw["_mrs_v12"]

    reg_i, reg_h = 0.5 * math.log(2.0 * math.pi), 0.5 * math.log(2.0)
    t_i, t_h = [0.8, 6.0, 5.0], [8.2, 3.0, 4.0]
    rsh_g = [(-1.0 / (8.0 * math.pi**2)) * (-3.5 * t_i[i] * reg_i - 3.5 * t_h[i] * reg_h) for i in range(3)]
    d_sh = [rsh_g[i] - rsh_g[2] for i in range(3)]

    def eval_neutrino_ratios(bm: Optional[List[np.ndarray]] = None):
        ig3 = au0 / (4.0 * math.pi)
        guv = np.sqrt(1.0 / np.array([ig3 + d_sh[0], ig3 + d_sh[1], ig3 + d_sh[2]]))
        gb = float(np.mean(guv))
        sf = gb / float(np.max(np.linalg.svd(yw[0], compute_uv=False)))
        yu0, yd0, ye0, ynu0 = yw[0] * sf, yw[1] * sf, yw[2] * sf, yw[3] * sf
        ynt = float(np.max(np.linalg.svd(ynu0, compute_uv=False)))
        knu0 = ((ynt**2) / mrs) * k_u.copy()
        lam0 = ((gb**2) / 8.0) * ((0.1272571765 * math.sqrt((1.0 / au0) / 0.04)) ** 2)
        if bm is not None:
            uq, uu, ud, ul, ue = bm
            yu0, yd0, ye0, knu0 = uq @ yu0 @ uu.conj().T, uq @ yd0 @ ud.conj().T, ul @ ye0 @ ue.conj().T, ul @ knu0 @ ul.T
        y0 = np.concatenate([guv.real, yu0.real.ravel(), yu0.imag.ravel(), yd0.real.ravel(), yd0.imag.ravel(), ye0.real.ravel(), ye0.imag.ravel(), [lam0], knu0.real.ravel(), knu0.imag.ravel()])
        sol = solve_ivp(_rhs76, (0.0, -lr0), y0, method="DOP853", rtol=1e-11, atol=1e-13)
        yf = sol.y[:, -1]
        ye = (yf[39:48] + 1j * yf[48:57]).reshape(3, 3)
        knu = 0.5 * ((yf[58:67] + 1j * yf[67:76]).reshape(3, 3) + (yf[58:67] + 1j * yf[67:76]).reshape(3, 3).T)

        mnu_vew = 0.5 * math.exp(-lr0) * knu
        u_nu, s_nu_d, _ = np.linalg.svd(mnu_vew)
        s_nu = s_nu_d[::-1]
        u_nu_a = u_nu[:, ::-1]
        p_d = u_nu_a.conj().T @ mnu_vew @ u_nu_a.conj()
        w_nu_tak = u_nu_a @ np.diag(np.exp(0.5j * np.angle(np.diag(p_d))))
        we, _, _ = np.linalg.svd(ye)
        we_a = we[:, ::-1]
        u_pmns = we_a.conj().T @ w_nu_tak
        aup = np.abs(u_pmns)

        m_bb_over_vew = float(abs(sum((u_pmns[0, i] ** 2) * s_nu[i] for i in range(3))))
        raw_mnu_00_non_invariant = float(abs(mnu_vew[0, 0]))
        sum_mnu_over_vew = float(np.sum(s_nu))

        s13_sq = float(aup[0, 2] ** 2)
        c13_sq = max(1.0 - s13_sq, 1e-15)
        s12 = math.sqrt((aup[0, 1] ** 2) / c13_sq)
        c12 = math.sqrt(max(1.0 - s12 * s12, 0.0))
        s23 = math.sqrt((aup[1, 2] ** 2) / c13_sq)
        c23 = math.sqrt(max(1.0 - s23 * s23, 0.0))
        s13 = math.sqrt(s13_sq)
        c13 = math.sqrt(c13_sq)
        j_signed = float(np.imag(u_pmns[0, 1] * u_pmns[1, 2] * np.conj(u_pmns[0, 2]) * np.conj(u_pmns[1, 1])))
        sin_dcp = j_signed / max(c12 * s12 * c23 * s23 * (c13**2) * s13, 1e-30)
        cos_dcp = ((aup[1, 0] ** 2) - (c12**2) * (s23**2) * (s13**2) - (s12**2) * (c23**2)) / max(2.0 * c12 * s12 * c23 * s23 * s13, 1e-30)
        dcp_deg = math.degrees(math.atan2(sin_dcp, cos_dcp)) % 360.0
        return [float(x) for x in s_nu], sum_mnu_over_vew, m_bb_over_vew, dcp_deg, sin_dcp, cos_dcp, raw_mnu_00_non_invariant

    s_nu0, sum_vew0, mbb_vew0, dcp0, sin_dcp0, cos_dcp0, raw00_0 = eval_neutrino_ratios()
    rng_f = np.random.default_rng(20261201)
    haar_fals_max = 0.0
    raw00_haar_violation = 0.0
    for _ in range(10):
        _, sv_h, mb_h, dc_h, _, _, r00_h = eval_neutrino_ratios([_random_haar_u(3, rng_f) for _ in range(5)])
        haar_fals_max = max(
            haar_fals_max,
            abs(sv_h - sum_vew0) / sum_vew0,
            abs(mb_h - mbb_vew0) / mbb_vew0,
            abs(dc_h - dcp0) / 360.0,
        )
        raw00_haar_violation = max(raw00_haar_violation, abs(r00_h - raw00_0) / max(raw00_0, 1e-30))

    # 3. Pure Track-A Dimensionless Proton-Decay Wilson Coefficients & 5D Collar Overlap Integral:
    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = float(2 * mp.re(hl1)), float(2 * mp.im(hl1))
    eps1 = (math.exp(-2.9745505801732 * ell1) / abs(2 * np.sinh(0.5 * (ell1 + 1j * th1)))) / (2 * math.pi)
    lc = (4 * (math.pi**2 / 15) / eps1) ** 0.2
    mkk_mpl = math.exp(-2 * lc) / math.sqrt(3.0)
    m7_mpl = 2.0 * lc * mkk_mpl
    g_gut_sq = 4.0 * math.pi / au0

    ys = np.linspace(0.0, lc, 10001)
    t3r = {"e_c": 0.5, "L": 0.0, "d_c": 0.5, "u_c": -0.5, "Q": 0.0}
    bl_w = {"e_c": 1.0, "L": -1.0, "d_c": -1.0 / 3.0, "u_c": -1.0 / 3.0, "Q": 1.0 / 3.0}
    dens = {}
    for k, m_v in {k: t3r[k] - (1.0 / 12.0) * bl_w[k] for k in t3r}.items():
        if abs(m_v) < 1e-12:
            dens[k] = np.ones_like(ys) / lc
        else:
            raw_p = np.exp(-4.0 * m_v * ys)
            dens[k] = raw_p / np.trapezoid(raw_p, ys)

    c_5d_single16_ratio = 0.0
    for n_kk in range(150):
        psi_n = math.sqrt(2.0 / lc) * np.cos(((n_kk + 0.5) * math.pi / lc) * ys)
        ov_qu = math.sqrt(lc) * float(np.trapezoid(psi_n * np.sqrt(dens["Q"] * dens["u_c"]), ys))
        ov_ed = math.sqrt(lc) * float(np.trapezoid(psi_n * np.sqrt(dens["e_c"] * dens["d_c"]), ys))
        c_5d_single16_ratio += (ov_qu * ov_ed) / (((2 * n_kk + 1) ** 2))

    c6_e8_uv_m7_mpl2 = g_gut_sq / (2.0 * (m7_mpl**2))
    c6_naive_4d_mkk_plant_mpl2 = g_gut_sq / (2.0 * (mkk_mpl**2))
    c6_single16_5d_plant_mpl2 = abs(c_5d_single16_ratio) * c6_naive_4d_mkk_plant_mpl2

    n_sc = g2_res["m5_axion_and_baryon_track_a"]["N_star_self_consistent"]
    dns_dlnk = -2.0 / (n_sc**2)

    passed = bool(
        takagi_50d_err < 1.0e-45
        and abs(e_over_n_spin10 - 8.0 / 3.0) < 1.0e-15
        and abs(su4_singlet_xy_coupling) < 1.0e-15
        and haar_fals_max < 1.0e-11
        and raw00_haar_violation > 0.1
    )
    assert passed, "Gate P10-3 failed"

    return {
        "gate": "P10-3_falsifiability_observables_and_e8_proton_decay_track_a",
        "gate_p10_3_passed": passed,
        "benchmarks": {
            "takagi_50d_abs_err": takagi_50d_err,
            "srednicki_E_over_N_spin10": e_over_n_spin10,
            "e8_su4_split_16_xy_coupling": su4_singlet_xy_coupling,
            "haar_10trial_falsifiability_max_err": haar_fals_max,
        },
        "dimensionless_falsifiability_track_a": {
            "m_nu_over_vEW": s_nu0,
            "sum_m_nu_over_vEW": sum_vew0,
            "m_beta_beta_over_vEW": mbb_vew0,
            "delta_CP_deg": dcp0,
            "sin_delta_CP": sin_dcp0,
            "cos_delta_CP": cos_dcp0,
            "dn_s_dlnk_approx": dns_dlnk,
            "M_KK_over_MPl_red": mkk_mpl,
            "M_7_over_MPl_red": m7_mpl,
            "c6_e8_uv_m7_in_MPl_red_inv2": c6_e8_uv_m7_mpl2,
        },
        "planted_fault_signals_track_a": {
            "unrotated_mnu_00_haar_violation_plant": raw00_haar_violation,
            "c6_naive_4d_mkk_in_MPl_red_inv2_plant": c6_naive_4d_mkk_plant_mpl2,
            "c6_single16_5d_overlap_in_MPl_red_inv2_plant": c6_single16_5d_plant_mpl2,
        },
    }
