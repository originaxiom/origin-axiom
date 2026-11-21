"""Gate P8-3 (Track A, `0 of 19`): Sethi-Vafa-Witten & Klemm-Lian-Roan-Yau Weierstrass Elliptic
Calabi-Yau Fourfold X_8 -> B_6 Tadpole & Freed-Witten Quantization Audit.

Strictly 0 empirical inputs (zero PDG/NuFIT/Planck float literals).
"""
from __future__ import annotations

from typing import Any, Dict, List

import mpmath as mp

mp.mp.dps = 50


def weierstrass_cy4_invariants(
    name: str,
    int_c1_cubed: int,
    int_c1_c2: int,
    h11_base: int,
    c2_plus_c1sq_mod2_nonzero: int,
    h21_base: int = 0,
) -> Dict[str, Any]:
    mp.mp.dps = 50
    chi = 12 * (int_c1_c2 + 30 * int_c1_cubed)
    assert chi % 24 == 0, f"chi={chi} not divisible by 24 for {name}"
    h11 = h11_base + 1
    h21 = h21_base
    h31 = (chi // 6) - 8 - h11 + h21
    h22 = 44 + 4 * h11 + 4 * h31 - 2 * h21
    b4 = 2 + 2 * h31 + h22
    chi_betti = 2 + 2 * h11 - 4 * h21 + b4
    assert chi_betti == chi

    tadpole_budget = chi // 24
    r_flux_max_mp = mp.sqrt(mp.mpf(chi) / mp.mpf(12))
    vol_b = (mp.pi ** (mp.mpf(b4) / 2)) / mp.gamma(mp.mpf(b4) / 2 + 1)
    denom = mp.mpf(b4) * vol_b * (r_flux_max_mp**b4)
    log10_step_at_rmax = float(-mp.log10(denom))

    return {
        "base_B6": name,
        "int_B6_c1_cubed": int_c1_cubed,
        "int_B6_c1_c2": int_c1_c2,
        "chi_X8": chi,
        "chi_betti_identity_err": abs(chi_betti - chi),
        "h11_X8": h11,
        "h21_X8": h21,
        "h31_X8": h31,
        "h22_X8": h22,
        "b4_X8": b4,
        "m2_tadpole_chi_over_24": tadpole_budget,
        "R_flux_max_tadpole_positivity": float(r_flux_max_mp),
        "log10_bp_step_at_R_flux_max": log10_step_at_rmax,
        "clears_1e_minus_105_under_tadpole": bool(log10_step_at_rmax <= -105.0),
        "c2_X8_mod2_residual": c2_plus_c1sq_mod2_nonzero,
        "requires_half_integer_freed_witten_shift": bool(c2_plus_c1sq_mod2_nonzero != 0),
    }


def run_gate_p8_3_cy4_tadpole_bp() -> Dict[str, Any]:
    mp.mp.dps = 50

    bench_p3 = weierstrass_cy4_invariants("P^3", 64, 24, 1, (6 + 16) % 2)
    bench_p1_p2 = weierstrass_cy4_invariants("P^1 x P^2", 54, 24, 2, ((3 + 9) % 2) | (6 % 2))

    family_p1_dpr: List[Dict[str, Any]] = []
    for r_dp in range(9, -1, -1):
        int_c1_sq_dpr = 9 - r_dp
        int_c2_dpr = 3 + r_dp
        int_c1_3_b6 = 6 * int_c1_sq_dpr
        int_c1_c2_b6 = 2 * int_c2_dpr + 2 * int_c1_sq_dpr
        mod2_res = ((int_c2_dpr + int_c1_sq_dpr) % 2) | (6 % 2)
        row = weierstrass_cy4_invariants(f"P^1 x dP_{r_dp}", int_c1_3_b6, int_c1_c2_b6, 2 + r_dp, mod2_res)
        row["del_pezzo_rank_r"] = r_dp
        family_p1_dpr.append(row)

    clearing_ranks = [row["del_pezzo_rank_r"] for row in family_p1_dpr if row["clears_1e_minus_105_under_tadpole"]]
    r_crit = max(clearing_ranks)
    row_r9 = [row for row in family_p1_dpr if row["del_pezzo_rank_r"] == 9][0]
    row_r8 = [row for row in family_p1_dpr if row["del_pezzo_rank_r"] == 8][0]

    r_flux_illegal_plant = 10.0
    n_m2_at_r10_on_dP9_plant = (row_r9["chi_X8"] / 24.0) - 0.5 * (r_flux_illegal_plant**2)
    quadric_q3_plant = weierstrass_cy4_invariants("Q_3_quadric", 54, 24, 1, (4 + 9) % 2)

    passed = bool(
        bench_p3["chi_X8"] == 23328
        and bench_p3["h22_X8"] == 15564
        and bench_p1_p2["chi_X8"] == 19728
        and all(row["int_B6_c1_c2"] == 24 for row in family_p1_dpr)
        and all(not row["requires_half_integer_freed_witten_shift"] for row in family_p1_dpr)
        and row_r9["chi_X8"] == 288
        and row_r9["b4_X8"] == 262
        and row_r9["log10_bp_step_at_R_flux_max"] > -30.0
        and r_crit == 8
        and row_r8["chi_X8"] == 2448
        and row_r8["b4_X8"] == 2424
        and row_r8["log10_bp_step_at_R_flux_max"] < -190.0
        and n_m2_at_r10_on_dP9_plant < -30.0
        and quadric_q3_plant["requires_half_integer_freed_witten_shift"]
    )
    assert passed, "Gate P8-3 assertion failed"

    return {
        "gate_p8_3_passed": passed,
        "benchmarks": {"P3": bench_p3, "P1_x_P2": bench_p1_p2},
        "theorem_P8_3_critical_del_pezzo_rank": {
            "constant_int_c1_c2_across_P1_x_dPr": 24,
            "critical_rank_r_crit": r_crit,
            "parabolic_boundary_r9_P1_x_dP9": row_r9,
            "fano_transition_r8_P1_x_dP8": row_r8,
            "full_P1_x_dPr_sweep": family_p1_dpr,
            "clause_P8_C3_parabolic_tadpole_wall": (
                "Parabolic B_6 = P^1 x dP_9 has b_4 = 262 >= 249, but M2-tadpole positivity N_M2 >= 0 caps "
                "R_flux <= sqrt(24) = 4.90, limiting log10(Delta Lambda_BP / |V_bulk|) to -26.42; one blow-down "
                "to Fano dP_8 (r_crit = 8) raises chi to 2,448 and reaches -192.42 <= -105."
            ),
        },
        "planted_fault_signals": {
            "illegal_R10_on_P1_x_dP9_N_M2_branes": n_m2_at_r10_on_dP9_plant,
            "quadric_Q3_odd_c2_freed_witten_plant": quadric_q3_plant,
        },
    }
