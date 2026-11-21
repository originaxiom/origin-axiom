"""Gate P7-4 (Track A, `0 of 19`): Symbolic Radion-BBN Vacuum-Energy Identity,
Degenerate Type-I Seesaw Clash, & Kunneth Bousso-Polchinski G_4-Flux Lattice Audit.

Strictly 0 empirical inputs (zero PDG/NuFIT/Planck float literals).
"""
from __future__ import annotations

from typing import Any, Dict

import mpmath as mp
import numpy as np
import snappy
import sympy as sp

mp.mp.dps = 50


def run_gate_p7_4_nogo_and_bp_flux(Ynu_weave: np.ndarray) -> Dict[str, Any]:
    mp.mp.dps = 50
    x_s, A_s, B_s, Mpl_s = sp.symbols("x A B M_Pl", positive=True)
    V_bulk_expr = -A_s * (x_s**-7) + B_s * (x_s**-9)
    B_sol = sp.solve(sp.diff(V_bulk_expr, x_s).subs(x_s, 1), B_s)[0]
    V_min_val = sp.simplify(V_bulk_expr.subs({B_s: B_sol, x_s: 1}))
    d2V_min_val = sp.simplify(sp.diff(V_bulk_expr, x_s, 2).subs({B_s: B_sol, x_s: 1}))
    mrad_sq_15_4 = sp.simplify(d2V_min_val / (2 * sp.Rational(15, 4) * (Mpl_s**2)))
    ratio_vbulk_to_mpl2_mrad2 = sp.simplify(abs(V_min_val) / ((Mpl_s**2) * mrad_sq_15_4))

    s_ynu = np.linalg.svd(Ynu_weave, compute_uv=False)
    s_kappa_deg = np.linalg.svd(Ynu_weave @ Ynu_weave.T, compute_uv=False)[::-1]
    dm21_over_dm31_deg_plant = float((s_kappa_deg[1] ** 2 - s_kappa_deg[0] ** 2) / (s_kappa_deg[2] ** 2 - s_kappa_deg[0] ** 2))

    M_base = snappy.Manifold("m004")
    M5_cov = [c for c in M_base.covers(5) if "irregular" in c.cover_info()["type"]][0]
    b1_m004 = M_base.homology().betti_number()
    b1_m5 = M5_cov.homology().betti_number()
    torsion_m5 = [int(x) for x in M5_cov.homology().elementary_divisors() if x > 0]
    J_m004_dp9 = 1 + b1_m004 * 10
    J_m5_dp9 = 1 + b1_m5 * 10

    def bp_min_fractional_step(J_cycles: int, R_flux: float = 3.0) -> float:
        vol_ball = (mp.pi ** (mp.mpf(J_cycles) / 2)) / mp.gamma(mp.mpf(J_cycles) / 2 + 1)
        surf_sphere = mp.mpf(J_cycles) * vol_ball * (mp.mpf(str(R_flux)) ** (J_cycles - 1))
        return float(1 / (surf_sphere * mp.mpf(str(R_flux))))

    bp_step_j11 = bp_min_fractional_step(J_m004_dp9, 3.0)
    bp_step_j21 = bp_min_fractional_step(J_m5_dp9, 3.0)
    global_min_step_R3 = min(bp_min_fractional_step(J_t, 3.0) for J_t in range(1, 200))
    J_min_for_1e105_R10 = next(J_t for J_t in range(22, 600) if bp_min_fractional_step(J_t, 10.0) <= 1.0e-105)

    passed = bool(
        ratio_vbulk_to_mpl2_mrad2 == sp.Rational(5, 42)
        and dm21_over_dm31_deg_plant < 1.0e-8
        and J_m004_dp9 == 11
        and J_m5_dp9 == 21
        and torsion_m5 == [2]
        and bp_step_j21 > 1.0e-12
        and global_min_step_R3 > 1.0e-15
        and J_min_for_1e105_R10 > 100
    )
    assert passed

    return {
        "gate_p7_4_passed": passed,
        "exact_symbolic_Vbulk_over_MPl2_mrad2": str(ratio_vbulk_to_mpl2_mrad2),
        "degenerate_type1_seesaw_clash": {
            "Ynu_singular_ratios": [float(x / s_ynu[0]) for x in s_ynu],
            "degenerate_MR_dm21_sq_over_dm31_sq": dm21_over_dm31_deg_plant,
            "degenerate_4d_type1_ruled_out": bool(dm21_over_dm31_deg_plant < 1.0e-8),
        },
        "bousso_polchinski_flux_lattice_audit": {
            "b1_m004": int(b1_m004),
            "b1_M5_cover": int(b1_m5),
            "M5_torsion_divisors": torsion_m5,
            "J_4cycles_m004_x_dP9": int(J_m004_dp9),
            "J_4cycles_M5_x_dP9": int(J_m5_dp9),
            "bp_fractional_step_J11_R3": bp_step_j11,
            "bp_fractional_step_J21_R3": bp_step_j21,
            "global_min_step_all_J_at_R3": global_min_step_R3,
            "min_J_required_for_1e105_at_R10": int(J_min_for_1e105_R10),
        },
    }
