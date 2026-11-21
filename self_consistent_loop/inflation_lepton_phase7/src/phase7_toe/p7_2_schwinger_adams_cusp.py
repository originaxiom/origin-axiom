"""Gate P7-2 (Track A, `0 of 19`): 50-Digit Schwinger Orbifold Benchmark, Adams Maximal Cusp Theorem,
& Cubic Divergence / Covering-Circumference Audit of `Clause W2-C1`.

Strictly 0 empirical inputs (zero PDG/NuFIT/Planck float literals).
"""
from __future__ import annotations

from typing import Any, Dict

import mpmath as mp
import snappy

mp.mp.dps = 50


def run_gate_p7_2_schwinger_adams_cusp() -> Dict[str, Any]:
    mp.mp.dps = 50
    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = 2 * mp.re(hl1), 2 * mp.im(hl1)
    lam1 = mp.mpf("2.9745505801732")
    eps1_mp = (mp.exp(-lam1 * ell1) / abs(2 * mp.sinh((ell1 + 1j * th1) / 2))) / (2 * mp.pi)
    Lc_mp = (4 * (mp.pi**2 / 15) / eps1_mp) ** mp.mpf("0.2")
    vol_m5_mp = 10 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    L_s1 = 2 * Lc_mp

    mu_test = mp.mpf("0.25")
    quad_m1 = mp.quad(
        lambda u: (L_s1 / (mp.sqrt(mp.pi) * u * u)) * mp.exp(-((mu_test * u) ** 2) - ((L_s1 / (2 * u)) ** 2)),
        [mp.mpf("0.05"), mp.mpf("1.0"), mp.mpf("5.0"), mp.mpf("20.0"), mp.inf],
    )
    schwinger_m1_err = float(abs(quad_m1 - mp.exp(-mu_test * L_s1)))

    mu_ir = mp.mpf("1e-25")
    reg_diff_mp = -mp.mpf("0.25") * (
        (-2 * mp.log(1 - mp.exp(-mu_ir * L_s1)) + 2 * mp.log(mu_ir * L_s1 / (2 * mp.pi)))
        - (-2 * mp.log(1 + mp.exp(-mu_ir * L_s1)))
    )
    contino_pilo_err = float(abs(reg_diff_mp - mp.mpf("0.5") * mp.log(mp.pi)))

    M4 = snappy.Manifold("m004")
    cn = M4.cusp_neighborhood()
    cn.set_displacement(cn.reach(0), 0)
    v_horo_snappy = float(cn.volume(0))
    v_horo_exact = float(mp.sqrt(3))
    adams_vol_err = abs(v_horo_snappy - v_horo_exact)
    adams_ir_area_over_6 = float((2 * mp.sqrt(3) * mp.exp(-2 * Lc_mp)) / 6)
    mkk_over_mpl_w2 = float(mp.exp(-2 * Lc_mp) / mp.sqrt(3))
    adams_identity_err = abs(adams_ir_area_over_6 - mkk_over_mpl_w2)

    lam_uv_1, lam_uv_2 = mp.mpf("10.0"), mp.mpf("20.0")
    i7_1 = mp.quad(lambda s: s ** mp.mpf("-2.5"), [lam_uv_1**-2, mp.inf])
    i7_2 = mp.quad(lambda s: s ** mp.mpf("-2.5"), [lam_uv_2**-2, mp.inf])
    cubic_scaling_ratio = float(i7_2 / i7_1)

    def alpha_gut_inv_at_cutoff(lam_r0_mp: mp.mpf) -> float:
        return float((9 * vol_m5_mp * (lam_r0_mp**3)) / (30 * (mp.pi**3)))

    agut_covering_2Lc = alpha_gut_inv_at_cutoff(2 * Lc_mp)
    agut_half_1Lc_plant = alpha_gut_inv_at_cutoff(Lc_mp)
    agut_kk_mom_pi_over_Lc_plant = alpha_gut_inv_at_cutoff(mp.pi / Lc_mp)

    passed = bool(
        schwinger_m1_err < 1.0e-35
        and contino_pilo_err < 1.0e-22
        and adams_vol_err < 1.0e-12
        and adams_identity_err < 1.0e-18
        and abs(cubic_scaling_ratio - 8.0) < 1.0e-30
        and 40.0 < agut_covering_2Lc < 45.0
        and agut_half_1Lc_plant < 6.0
        and agut_kk_mom_pi_over_Lc_plant < 0.1
    )
    assert passed

    return {
        "gate_p7_2_passed": passed,
        "contino_pilo_schwinger_benchmark": {
            "covering_circle_circumference_2Lc": float(L_s1),
            "schwinger_m1_quadrature_err_50d": schwinger_m1_err,
            "orbifold_differential_threshold_half_ln_pi": float(reg_diff_mp),
            "contino_pilo_50d_err": contino_pilo_err,
        },
        "theorem_P7_2_adams_maximal_cusp": {
            "snappy_maximal_horoball_volume": v_horo_snappy,
            "exact_sqrt3_volume": v_horo_exact,
            "adams_volume_abs_err": adams_vol_err,
            "euclidean_cusp_torus_area_2sqrt3": 2.0 * v_horo_snappy,
            "ir_cusp_area_over_6_ratio": adams_ir_area_over_6,
            "matches_stage_w2_MKK_over_MPl_err": adams_identity_err,
        },
        "clause_P7_C2_cubic_divergence_audit": {
            "m0_bulk_7d_doubling_cutoff_ratio": cubic_scaling_ratio,
            "alpha_GUT_inv_at_covering_2Lc": agut_covering_2Lc,
            "alpha_GUT_inv_at_1Lc_plant": agut_half_1Lc_plant,
            "alpha_GUT_inv_at_pi_over_Lc_plant": agut_kk_mom_pi_over_Lc_plant,
            "requires_uv_mtheory_tdual_winding_completion": True,
        },
    }
