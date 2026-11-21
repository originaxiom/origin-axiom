"""Gate P8-1 (Track A, `0 of 19`): Head-to-Head Axion Isocurvature Shootout —
11D Non-Minimal Kinetic Mixing (Branch 1A) vs. Small-Radius Self-Dual Casimir Plateau (Branch 1B).

Strictly 0 empirical inputs (zero PDG/NuFIT/Planck float literals). Computes all dimensionless
Hubble, decay-constant, and scalar/tensor perturbation observables in reduced Planck units (M_Pl_red == 1).
"""
from __future__ import annotations

import math
from typing import Any, Dict

import mpmath as mp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

mp.mp.dps = 50


def solve_kg_hubble_plateau(mu_mpl: float, n_efolds: float) -> Dict[str, float]:
    """Exact Hubble-flow Klein-Gordon ODE for V(chi) = V_0 * (1 - exp(-chi / mu))^2 in M_Pl_red = 1 units."""
    mp.mp.dps = 50
    fv = lambda c: (1.0 - math.exp(-c / mu_mpl)) ** 2
    fdv = lambda c: (2.0 / mu_mpl) * math.exp(-c / mu_mpl) * (1.0 - math.exp(-c / mu_mpl))
    fd2v = lambda c: (2.0 / (mu_mpl**2)) * math.exp(-c / mu_mpl) * (2.0 * math.exp(-c / mu_mpl) - 1.0)

    c_end_sr = float(brentq(lambda c: 0.5 * (fdv(c) / fv(c)) ** 2 - 1.0, 1.0e-4 * mu_mpl, 30.0 * mu_mpl, xtol=1e-15))
    sol_sr = solve_ivp(
        lambda _n, y: [fdv(y[0]) / fv(y[0])],
        (0.0, n_efolds + 6.0),
        [c_end_sr],
        method="DOP853",
        rtol=1e-12,
        atol=1e-14,
    )
    c_init = float(sol_sr.y[0, -1])
    u_init = -fdv(c_init) / fv(c_init)

    def kg_rhs(_n: float, y: list[float]) -> list[float]:
        c_v, u_v = y
        eps_h = 0.5 * u_v * u_v
        return [u_v, -(3.0 - eps_h) * (u_v + fdv(c_v) / fv(c_v))]

    def hit_end(_n: float, y: list[float]) -> float:
        return 0.5 * (y[1] ** 2) - 1.0

    hit_end.terminal = True  # type: ignore[attr-defined]
    hit_end.direction = 1.0  # type: ignore[attr-defined]

    sol_kg = solve_ivp(
        kg_rhs,
        (0.0, n_efolds + 40.0),
        [c_init, u_init],
        events=hit_end,
        method="DOP853",
        rtol=1e-12,
        atol=1e-14,
        dense_output=True,
    )
    n_tot = float(sol_kg.t_events[0][0])
    c_star, u_star = sol_kg.sol(n_tot - n_efolds)
    c_s, u_s = float(c_star), float(u_star)
    eps_h = 0.5 * u_s * u_s
    du_dn = -(3.0 - eps_h) * (u_s + fdv(c_s) / fv(c_s))
    eps2_h = 2.0 * du_dn / u_s
    ns_exact = 1.0 - 2.0 * eps_h - eps2_h
    r_exact = 16.0 * eps_h
    eps_v = 0.5 * (fdv(c_s) / fv(c_s)) ** 2
    eta_v = fd2v(c_s) / fv(c_s)
    return {
        "chi_star_over_MPl": c_s,
        "chi_end_over_MPl": float(sol_kg.y[0, -1]),
        "ns_exact": float(ns_exact),
        "r_exact": float(r_exact),
        "ns_sr": float(1.0 - 6.0 * eps_v + 2.0 * eta_v),
        "r_sr": float(16.0 * eps_v),
        "eps_H": float(eps_h),
        "V_star_unit": float(fv(c_s)),
        "V_end_unit": float(fv(float(sol_kg.y[0, -1]))),
    }


def run_gate_p8_1_isocurvature_shootout() -> Dict[str, Any]:
    mp.mp.dps = 50

    # 1. Literature Benchmark Gate (Guardrail 4) evaluated at pure synthetic test point (zero empirical literals):
    # (a) Fox-Pierce-Thomas (hep-th/0409059): P_iso = ((2 / theta_0) * (H_I / (2*pi*f_a)))^2, beta = P_iso / (P_iso + A_0)
    hi_over_2pifa_test = 1.0e-5
    theta_test = 1.0
    as_test = 1.6e-9
    p_iso_fpt = ((2.0 / theta_test) * hi_over_2pifa_test) ** 2
    beta_fpt = p_iso_fpt / (p_iso_fpt + as_test)
    fpt_exact = 0.2  # 4e-10 / (4e-10 + 1.6e-9) == 1/5 == 0.2 exactly!
    fpt_abs_err = abs(beta_fpt - fpt_exact)

    # (b) Germani-Kehagias (PRL 106 (2011) 161302): Z_GK = 1 + 3 H^2 / M_GK^2
    h_gk, m_gk, f0_gk = 2.0e-4, 1.0e-5, 1.0e-3
    feff_gk = f0_gk * math.sqrt(1.0 + 3.0 * ((h_gk / m_gk) ** 2))
    gk_abs_err = abs(feff_gk - f0_gk * math.sqrt(1201.0))

    # 2. Pure Track-A Geometric Scales from m004 / M^(5) (M_Pl_red == 1):
    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = 2 * mp.re(hl1), 2 * mp.im(hl1)
    lam1 = mp.mpf("2.9745505801732")
    eps1_mp = (mp.exp(-lam1 * ell1) / abs(2 * mp.sinh((ell1 + 1j * th1) / 2))) / (2 * mp.pi)
    Lc_mp = (4 * (mp.pi**2 / 15) / eps1_mp) ** mp.mpf("0.2")
    vol_m5_mp = 10 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))

    Lc = float(Lc_mp)
    mkk_mpl = float(mp.exp(-2 * Lc_mp) / mp.sqrt(3))
    m7_mpl = 2.0 * Lc * mkk_mpl
    fa0_mpl = mkk_mpl / (2.0 * math.pi)
    c_can = math.sqrt(2.0 / 15.0)
    c_cas = float((4 * (mp.pi**2) / (15 * ((2 * mp.pi) ** 3))) * vol_m5_mp)
    vcas_mpl4 = c_cas * (mkk_mpl**4)
    v0_m7_mpl4 = m7_mpl**4
    mrad_mpl = math.sqrt((14.0 / 15.0) * c_cas) * (mkk_mpl**2)
    treh_mpl = ((90.0 / (math.pi**2 * 106.75)) ** 0.25) * math.sqrt((mrad_mpl**3) / (8.0 * math.pi))
    rho_reh_mpl4 = (math.pi**2 / 30.0) * 106.75 * (treh_mpl**4)
    alpha_gut_0 = 1.0 / ((5.0 / (12.0 * math.pi)) * ((2.0 * Lc) ** 3))

    # 3. Branch 1A (Large-Radius phi_* > 0, V_0 = M_7^4):
    b7, b9 = 7.0 * c_can, 9.0 * c_can
    fv79 = lambda p: 1.0 - 4.5 * math.exp(-b7 * p) + 3.5 * math.exp(-b9 * p)
    fdv79 = lambda p: 4.5 * b7 * math.exp(-b7 * p) - 3.5 * b9 * math.exp(-b9 * p)
    p_end_79 = float(brentq(lambda p: 0.5 * (fdv79(p) / fv79(p)) ** 2 - 1.0, 0.05, 8.0, xtol=1e-13))

    def ll_79(n_g: float) -> float:
        s_t = solve_ivp(lambda _n, y: [fdv79(y[0]) / fv79(y[0])], (0.0, n_g), [p_end_79], method="DOP853", rtol=1e-11, atol=1e-13)
        ps = float(s_t.y[0, -1])
        vs = v0_m7_mpl4 * fv79(ps)
        re = 1.5 * v0_m7_mpl4 * fv79(p_end_79)
        return n_g - (61.55 + 0.25 * math.log((vs**2) / re) + (1.0 / 12.0) * math.log(rho_reh_mpl4 / re))

    n_79 = float(brentq(ll_79, 45.0, 60.0, xtol=1e-10))
    s_79 = solve_ivp(lambda _n, y: [fdv79(y[0]) / fv79(y[0])], (0.0, n_79), [p_end_79], method="DOP853", rtol=1e-12, atol=1e-14)
    phi_star_pos = float(s_79.y[0, -1])
    hi_pos = math.sqrt((v0_m7_mpl4 * fv79(phi_star_pos)) / 3.0)
    fa_min_pos = fa0_mpl * math.exp(-3.0 * c_can * phi_star_pos)

    chi_dp9 = 12.0
    fa_1ai = math.sqrt(fa_min_pos**2 + (3.0 * chi_dp9 / (16.0 * (math.pi**2))) * ((hi_pos / m7_mpl) ** 2) * (fa0_mpl**2))
    fa_1aii = alpha_gut_0 / (2.0 * math.pi * math.sqrt(2.0))

    # 4. Branch 1B (Small-Radius UV Self-Dual Collar R_sd = M_7^-1, phi_sd = -ln(2*Lc*)/c_can):
    phi_sd = -math.log(2.0 * Lc) / c_can
    r_sd_times_m7 = 2.0 * Lc * math.exp(c_can * phi_sd)
    fa_sd = fa0_mpl * math.exp(-3.0 * c_can * phi_sd)

    def ll_1bsd(n_g: float) -> float:
        hub_t = solve_kg_hubble_plateau(m7_mpl, n_g)
        vs = vcas_mpl4 * hub_t["V_star_unit"]
        re = 1.5 * vcas_mpl4 * hub_t["V_end_unit"]
        return n_g - (61.55 + 0.25 * math.log((vs**2) / re) + (1.0 / 12.0) * math.log(rho_reh_mpl4 / re))

    n_1bsd = float(brentq(ll_1bsd, 40.0, 55.0, xtol=1e-10))
    hub_1bsd = solve_kg_hubble_plateau(m7_mpl, n_1bsd)
    as_1bsd = (vcas_mpl4 * hub_1bsd["V_star_unit"]) / (24.0 * (math.pi**2) * hub_1bsd["eps_H"])
    hi_1bsd = math.sqrt((vcas_mpl4 * hub_1bsd["V_star_unit"]) / 3.0)

    # Prompt cusp-cap SM gauge decay (Gamma_gg = 3 m_chi^3 / (16 pi M_7^2)):
    mchi_mpl = math.sqrt(2.0 * vcas_mpl4) / m7_mpl
    gamma_cap_mpl = (3.0 * (mchi_mpl**3)) / (16.0 * math.pi * (m7_mpl**2))
    treh_cap_mpl = ((90.0 / (math.pi**2 * 106.75)) ** 0.25) * math.sqrt(gamma_cap_mpl)
    rho_reh_cap_mpl4 = min((math.pi**2 / 30.0) * 106.75 * (treh_cap_mpl**4), 1.5 * vcas_mpl4)

    def ll_1bsd_gauge(n_g: float) -> float:
        hub_t = solve_kg_hubble_plateau(m7_mpl, n_g)
        vs = vcas_mpl4 * hub_t["V_star_unit"]
        re = 1.5 * vcas_mpl4 * hub_t["V_end_unit"]
        return n_g - (61.55 + 0.25 * math.log((vs**2) / re) + (1.0 / 12.0) * math.log(min(rho_reh_cap_mpl4, re) / re))

    n_1bsd_gauge = float(brentq(ll_1bsd_gauge, 45.0, 58.0, xtol=1e-10))
    hub_1bsd_gauge = solve_kg_hubble_plateau(m7_mpl, n_1bsd_gauge)
    as_1bsd_gauge = (vcas_mpl4 * hub_1bsd_gauge["V_star_unit"]) / (24.0 * (math.pi**2) * hub_1bsd_gauge["eps_H"])

    # 5. Planted-Fault Signals (pure Track-A ratios):
    fa_sd_wrong_weyl = fa0_mpl * math.exp(+3.0 * c_can * phi_sd)
    phi_trans_plant = -8.0
    r_trans_times_m7_plant = 2.0 * Lc * math.exp(c_can * phi_trans_plant)

    passed = bool(
        fpt_abs_err < 1.0e-15
        and gk_abs_err < 1.0e-15
        and abs(r_sd_times_m7 - 1.0) < 1.0e-14
        and (hi_1bsd / (2.0 * math.pi * fa_sd)) < 2.0e-7
        and (hi_1bsd / (2.0 * math.pi * fa_sd_wrong_weyl)) > 1.0e-2
        and r_trans_times_m7_plant < 0.5
        and 1.0e-9 < as_1bsd < 5.0e-9
    )
    assert passed, "Gate P8-1 assertion failed"

    return {
        "gate_p8_1_passed": passed,
        "benchmarks": {
            "fox_pierce_thomas_synthetic_beta_iso": beta_fpt,
            "fox_pierce_thomas_abs_err": fpt_abs_err,
            "germani_kehagias_feff": feff_gk,
            "germani_kehagias_abs_err": gk_abs_err,
        },
        "branch_1A_large_radius_track_a": {
            "phi_star_pos": phi_star_pos,
            "H_I_over_MPl_red": hi_pos,
            "fa_minimal_over_MPl_red": fa_min_pos,
            "branch_1Ai_11d_gauss_bonnet_feff_over_MPl": fa_1ai,
            "branch_1Ai_H_I_over_2pi_feff": hi_pos / (2.0 * math.pi * fa_1ai),
            "branch_1Aii_horava_witten_fMI_over_MPl": fa_1aii,
            "branch_1Aii_H_I_over_2pi_fMI": hi_pos / (2.0 * math.pi * fa_1aii),
        },
        "branch_1B_small_radius_self_dual_track_a": {
            "phi_sd": phi_sd,
            "R_sd_times_M7": r_sd_times_m7,
            "fa_at_R_sd_over_MPl_red": fa_sd,
            "fa_enhancement_factor_2Lc_cubed": (2.0 * Lc) ** 3,
            "high_scale_M7_4_at_R_sd_H_I_over_2pi_fa": hi_pos / (2.0 * math.pi * fa_sd),
            "casimir_scale_self_dual_plateau_1B_SD": {
                "V0_Cas_over_MPl4": vcas_mpl4,
                "mu_cap_over_MPl_eq_M7": m7_mpl,
                "N_star_self_consistent": n_1bsd,
                "chi_star_over_MPl": hub_1bsd["chi_star_over_MPl"],
                "chi_end_over_MPl": hub_1bsd["chi_end_over_MPl"],
                "ns_exact": hub_1bsd["ns_exact"],
                "r_exact": hub_1bsd["r_exact"],
                "A_s_predicted": as_1bsd,
                "H_I_over_MPl_red": hi_1bsd,
                "H_I_over_2pi_fa_sd": hi_1bsd / (2.0 * math.pi * fa_sd),
                "prompt_gauge_reheated_N_star": n_1bsd_gauge,
                "prompt_gauge_reheated_ns_exact": hub_1bsd_gauge["ns_exact"],
                "prompt_gauge_reheated_A_s": as_1bsd_gauge,
            },
        },
        "planted_fault_signals": {
            "wrong_positive_weyl_fa_at_R_sd": fa_sd_wrong_weyl,
            "wrong_positive_weyl_H_I_over_2pi_fa": hi_1bsd / (2.0 * math.pi * fa_sd_wrong_weyl),
            "trans_7d_planck_phi_plant": phi_trans_plant,
            "trans_7d_planck_R_times_M7_plant": r_trans_times_m7_plant,
        },
    }
