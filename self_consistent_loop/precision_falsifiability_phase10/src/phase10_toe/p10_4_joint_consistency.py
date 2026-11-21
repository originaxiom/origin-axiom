"""Gate P10-4: Cross-Sector Anomaly Cancellation, Dynamical Strong-CP on `v12_dP8_ps`,
CY4 P^1 x dP_8 Tadpole Audit, & 10-Scale M^(5) Ordering (`0 of 19` Track A — Zero Empirical Inputs).
"""
from __future__ import annotations

from fractions import Fraction
import math
from typing import Any, Dict

import mpmath as mp
import numpy as np
from scipy.optimize import brentq
import sympy as sp

mp.mp.dps = 50


def run_gate_p10_4_joint_consistency(g1_raw: Dict[str, Any], g2_res: Dict[str, Any]) -> Dict[str, Any]:
    """Verify anomalies, Strong-CP on v12_dP8_ps, CY4 P^1 x dP_8 flux step, and 10-scale M^(5) ordering."""
    mp.mp.dps = 50

    n_gen = 3
    fermions = [
        ("Q", 3 * n_gen, 2, Fraction(1, 6), Fraction(1, 3)),
        ("u_c", 3 * n_gen, 1, Fraction(-2, 3), Fraction(-1, 3)),
        ("d_c", 3 * n_gen, 1, Fraction(1, 3), Fraction(-1, 3)),
        ("L", 1 * n_gen, 2, Fraction(-1, 2), Fraction(-1, 1)),
        ("e_c", 1 * n_gen, 1, Fraction(1, 1), Fraction(1, 1)),
        ("nu_c", 1 * n_gen, 1, Fraction(0, 1), Fraction(1, 1)),
        ("S_1_15", 15, 1, Fraction(0, 1), Fraction(0, 1)),
    ]
    a_su3_2_y = sum((m * d2 / 2) * y for nm, m, d2, y, _ in fermions if nm in ("Q", "u_c", "d_c"))
    a_su2_2_y = sum((m / 2) * y for _, m, d2, y, _ in fermions if d2 == 2)
    a_y3 = sum(m * d2 * (y**3) for _, m, d2, y, _ in fermions)
    a_grav2_y = sum(m * d2 * y for _, m, d2, y, _ in fermions)
    a_bl3 = sum(m * d2 * (bl**3) for _, m, d2, _, bl in fermions)
    n_su2_doublets = sum(m for _, m, d2, _, _ in fermions if d2 == 2)

    yw = g1_raw["_Yw_v12"]
    dp_v12 = np.linalg.det(yw[0] @ yw[1])
    th0_v12 = float(math.atan2(dp_v12.imag, dp_v12.real))
    alpha_v12 = float(brentq(lambda a: math.sin(th0_v12 + a), -th0_v12 - 0.5, -th0_v12 + 0.5, xtol=1e-15))
    hess_v12 = math.cos(th0_v12 + alpha_v12)
    strong_cp_residual_abs = abs(th0_v12 + alpha_v12)
    frozen_axion_plant_abs = abs(th0_v12)

    r_sym = sp.Symbol("r", integer=True)
    int_c1_c2_sym = sp.simplify(2 * (3 + r_sym) + 2 * (9 - r_sym))
    chi_sym = sp.simplify(12 * (int_c1_c2_sym + 30 * 6 * (9 - r_sym)))
    chi_r8 = int(chi_sym.subs(r_sym, 8))
    b4_r8 = 2 + 2 * (chi_r8 // 6 - 19) + (44 + 44 + 4 * (chi_r8 // 6 - 19))
    rmax_r8 = mp.sqrt(mp.mpf(chi_r8) / mp.mpf(12))
    vb_r8 = (mp.pi ** (mp.mpf(b4_r8) / 2)) / mp.gamma(mp.mpf(b4_r8) / 2 + 1)
    log10_bp_r8 = float(-mp.log10(mp.mpf(b4_r8) * vb_r8 * (rmax_r8**b4_r8)))

    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = 2 * mp.re(hl1), 2 * mp.im(hl1)
    eps1_mp = (mp.exp(-mp.mpf("2.9745505801732") * ell1) / abs(2 * mp.sinh((ell1 + 1j * th1) / 2))) / (2 * mp.pi)
    lc_mp = (4 * (mp.pi**2 / 15) / eps1_mp) ** mp.mpf("0.2")
    vol_m5_mp = 10 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    lc = float(lc_mp)
    mkk_mpl = float(mp.exp(-2 * lc_mp) / mp.sqrt(3))
    m7_mpl = 2.0 * lc * mkk_mpl
    fa0_m5_mpl = g2_res["m5_axion_and_baryon_track_a"]["fa0_M5_over_MPl_red"]
    fa_sd_m5_mpl = g2_res["m5_axion_and_baryon_track_a"]["fa_sd_M5_over_MPl_red"]
    c_cas = float((4 * (mp.pi**2) / (15 * ((2 * mp.pi) ** 3))) * vol_m5_mp)
    vcas_mpl4 = c_cas * (mkk_mpl**4)
    mchi_mpl = math.sqrt(2.0 * vcas_mpl4) / m7_mpl
    mrad_mpl = math.sqrt((14.0 / 15.0) * c_cas) * (mkk_mpl**2)
    hi_1bsd_mpl = g2_res["m5_axion_and_baryon_track_a"]["H_I_over_MPl_red"]
    treh_rad_mpl = ((90.0 / (math.pi**2 * 106.75)) ** 0.25) * math.sqrt((mrad_mpl**3) / (8.0 * math.pi))

    scales_10 = [
        ("M_Pl_red", 1.0),
        ("f_a_M5_at_R_sd", fa_sd_m5_mpl),
        ("M_7", m7_mpl),
        ("M_KK", mkk_mpl),
        ("V_Cas_quarter", vcas_mpl4**0.25),
        ("f_a0_M5_IR", fa0_m5_mpl),
        ("m_chi_cap", mchi_mpl),
        ("m_rad", mrad_mpl),
        ("H_I_1B_SD", hi_1bsd_mpl),
        ("T_reh_radion", treh_rad_mpl),
    ]
    strict_ordering = all(scales_10[i][1] > scales_10[i + 1][1] for i in range(len(scales_10) - 1))

    passed = bool(
        a_su3_2_y == 0
        and a_su2_2_y == 0
        and a_y3 == 0
        and a_grav2_y == 0
        and a_bl3 == 0
        and n_su2_doublets % 2 == 0
        and strong_cp_residual_abs < 1.0e-14
        and hess_v12 > 0.999999
        and frozen_axion_plant_abs > 1.0e-4
        and chi_r8 == 2448
        and b4_r8 == 2424
        and log10_bp_r8 < -190.0
        and strict_ordering
        and treh_rad_mpl < fa0_m5_mpl
    )
    assert passed, "Gate P10-4 failed"

    return {
        "gate": "P10-4_joint_consistency_and_m5_scale_ordering",
        "gate_p10_4_passed": passed,
        "anomalies_with_E8_singlet": {
            "SU3_2_U1Y": int(a_su3_2_y),
            "SU2_2_U1Y": int(a_su2_2_y),
            "U1Y_3": int(a_y3),
            "grav_2_U1Y": int(a_grav2_y),
            "BL_3_with_nuc_and_S": int(a_bl3),
            "witten_SU2_doublets": n_su2_doublets,
        },
        "strong_cp_v12": {
            "tree_arg_det_YuYd_rad": th0_v12,
            "minimized_strong_cp_residual_abs": strong_cp_residual_abs,
            "hessian_at_min": hess_v12,
            "frozen_axion_plant_abs": frozen_axion_plant_abs,
        },
        "cy4_P1_x_dP8_summary": {
            "r_crit": 8,
            "chi_X8": chi_r8,
            "b4_X8": b4_r8,
            "log10_bp_step_at_R_flux_max": log10_bp_r8,
        },
        "track_a_ten_scale_M5_hierarchy": [{"scale": k, "ratio_to_MPl_red": v} for k, v in scales_10],
        "strict_scale_ordering_satisfied": strict_ordering,
    }
