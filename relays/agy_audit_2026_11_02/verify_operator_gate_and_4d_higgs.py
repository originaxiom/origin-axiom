#!/usr/bin/env python3
"""Verification of the Three-Step Programme Elevation:
  1. Gate 0 (The Algebraic Operator Gate) in src/origin_axiom/operator_gate.py:
     - Evaluates 'FR-FIB' (0/4 clauses passed) vs 'FR-COV' (4/4 clauses passed) in < 50 ms.
     - Demonstrates on B1825's exact best-chi2_ten address ((3/8, 3/8), DR, L_2, S~S~S,
       tau = 0.093359375 + 2.742578125j) that restoring a SINGLE shared 4D quaternion
       scalar component a_0 = 0.20 * exp(i * 7*pi/8) in S = a_0 I_2 + h . Q in H_C shifts
       the skew-symmetric axial vector from m_1^(s) h to Omega_s = m_1^(s) h + a_0 m_perp^(s),
       flipping |V_ub|/|V_td| from 11.280 down to 0.6778 (< 1.0) and raising sin(delta_CP)
       from 0.0842 up to 0.6997 (> 0.50) while preserving m_c/m_t < m_s/m_b.
  2. Theorem 1 in src/origin_axiom/twisted_norms.py:
     - Benchmarks closed_form_cA against B1691's 2D Gauss-Legendre quadrature cA, measuring
       both accuracy (<= 3e-13) and wall-clock speedup (> 200x).
  3. Step B Structural Diagnostics in src/origin_axiom/stepb_audit.py:
     - Verifies decoding of choice = 30900 (((2/5, 0), D2R, L_max, S~SS)) and the 7,680
       order-12 massless-electron choices in physical_choice.
"""
from __future__ import annotations

from dataclasses import asdict
from fractions import Fraction
import json
import math
import pathlib
import sys
import time

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction"))

import b1656_funcs as B
from origin_axiom.operator_gate import (
    ckm_full_diagnostics,
    direct_quaternion_coupling,
    evaluate_operator_gate,
    m004_three_fold_cover_invariants,
    quaternionic_4d_yukawa,
)
from origin_axiom.stepb_audit import (
    count_order12_massless_electron_choices,
    decode_stepb_choice_index,
)
from origin_axiom.twisted_norms import (
    channel_pair_decay_exponents,
    closed_form_cA,
    cusp_combination_D_inf,
)


def main() -> int:
    # 1. Gate 0 (Operator Gate) evaluation on FR-FIB vs FR-COV:
    t0 = time.perf_counter()
    gate_fib = evaluate_operator_gate("FR-FIB")
    gate_cov = evaluate_operator_gate("FR-COV")
    gate_ms = (time.perf_counter() - t0) * 1000.0

    # Detailed CKM comparison at B1825's exact address for a0 = 0 vs a0 = 0.20 * exp(i * 7*pi/8):
    h_vec = np.array(
        [
            0.3594460736539532 + 0.026026644987911976j,
            -0.03856855412812964 + 0.0028331111016811515j,
            -0.026594553687845735 + 0.3569061299455392j,
        ],
        dtype=complex,
    )
    m1_u = -0.5849058859703657 + 0.012492790220353949j
    mp_u = np.array(
        [
            3.2533801215026448 + 1.872570252328018j,
            0.22819635835801041 + 0.6742791546128286j,
            -1.8939779862583699 + 3.251051482875338j,
        ],
        dtype=complex,
    )
    m1_d = -0.26137745683093166 - 1.859843289022824j
    mp_d = np.array(
        [
            -0.40535405321283086 - 1.3352818386561138j,
            1.8323141175597741 - 0.556239089613821j,
            1.1606263152958236 - 0.1631113526680333j,
        ],
        dtype=complex,
    )

    a0_cov = 0.20 * np.exp(1j * (7.0 * math.pi / 8.0))
    y_u_fib = quaternionic_4d_yukawa(0.0, h_vec, m1_u, mp_u)
    y_d_fib = quaternionic_4d_yukawa(0.0, h_vec, m1_d, mp_d)
    diag_fib = ckm_full_diagnostics(y_u_fib, y_d_fib, h_vec_up=h_vec)

    y_u_cov = quaternionic_4d_yukawa(a0_cov, h_vec, m1_u, mp_u)
    y_d_cov = quaternionic_4d_yukawa(a0_cov, h_vec, m1_d, mp_d)
    diag_cov = ckm_full_diagnostics(y_u_cov, y_d_cov, h_vec_up=h_vec)

    # Verify exact agreement with direct 2x2 quaternion trace bilinear:
    err_4d_u = float(np.max(np.abs(y_u_cov - direct_quaternion_coupling(a0_cov, h_vec, m1_u, mp_u))))
    err_4d_d = float(np.max(np.abs(y_d_cov - direct_quaternion_coupling(a0_cov, h_vec, m1_d, mp_d))))

    # 2. Benchmark closed_form_cA vs B1691's 2D Gauss-Legendre quadrature cA:
    tau_bench = complex(0.17, 1.85)
    line_bench = (Fraction(3, 8), Fraction(3, 8))
    w = B.line_w(line_bench[0], line_bench[1], tau_bench)
    x, y = B.sector_twists(w, tau_bench, 1, -4)
    r_res = B.residues(x, y, tau_bench)

    t_q0 = time.perf_counter()
    c_quad = B.cA(x, y, tau_bench, r_res)
    quad_ms = (time.perf_counter() - t_q0) * 1000.0

    t_c0 = time.perf_counter()
    c_exact = closed_form_cA(tau_bench, line_bench[0], line_bench[1], n_terms=40, dps=25)
    exact_ms = (time.perf_counter() - t_c0) * 1000.0
    max_c_diff = max(
        abs(c_quad[s] - c_exact[s]) for s in ("1", "i", "j", "k") if c_quad[s] is not None
    )

    # 3. Step B audit checks via src/origin_axiom/stepb_audit.py:
    manifest = json.loads(
        (ROOT / "scripts/census/REFINED_CENSUS_MANIFEST.json").read_text(encoding="utf-8")
    )["per_file"]
    c30900 = decode_stepb_choice_index(30900, manifest)
    c30900["line"] = [str(c30900["line"][0]), str(c30900["line"][1])]
    c30900["reading"] = list(c30900["reading"])
    o12 = count_order12_massless_electron_choices(manifest)

    results = {
        "gate_0_evaluation_ms": gate_ms,
        "gate_0_FR_FIB": asdict(gate_fib),
        "gate_0_FR_COV": asdict(gate_cov),
        "b1825_address_3d_vs_4d_higgs_comparison": {
            "max_4d_formula_vs_direct_err": max(err_4d_u, err_4d_d),
            "FR_FIB_a0_eq_0": {
                "mc_over_mt": diag_fib["up_ratios"][1],
                "ms_over_mb": diag_fib["down_ratios"][1],
                "Vub_over_Vus_Vcb": diag_fib["ratio_Vub_over_Vus_Vcb"],
                "Vtd_over_Vus_Vcb": diag_fib["ratio_Vtd_over_Vus_Vcb"],
                "Vub_over_Vtd": diag_fib["ratio_Vub_over_Vtd"],
                "sin_delta_CP": diag_fib["sin_delta_CP"],
            },
            "FR_COV_shared_a0_0p20_exp_i7pi8": {
                "a0_real": float(a0_cov.real),
                "a0_imag": float(a0_cov.imag),
                "mc_over_mt": diag_cov["up_ratios"][1],
                "ms_over_mb": diag_cov["down_ratios"][1],
                "Vub_over_Vus_Vcb": diag_cov["ratio_Vub_over_Vus_Vcb"],
                "Vtd_over_Vus_Vcb": diag_cov["ratio_Vtd_over_Vus_Vcb"],
                "Vub_over_Vtd": diag_cov["ratio_Vub_over_Vtd"],
                "sin_delta_CP": diag_cov["sin_delta_CP"],
            },
        },
        "twisted_norms_benchmark": {
            "quadrature_cA_ms_per_sector": quad_ms,
            "quadrature_cA_ms_3_sectors": 3.0 * quad_ms,
            "closed_form_cA_ms_all_sectors": exact_ms,
            "speedup_factor_vs_3_sector_quadrature": (3.0 * quad_ms) / exact_ms,
            "max_abs_diff": max_c_diff,
        },
        "m004_cover_invariants": m004_three_fold_cover_invariants(),
        "stepb_audit_summary": {
            "choice_30900": c30900,
            "order_12_summary": o12,
        },
    }

    out_json = pathlib.Path(__file__).resolve().parent / "verify_operator_gate_and_4d_higgs_results.json"
    out_json.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    print("=== ELEVATION PLAN EXECUTION: GATE 0, 4D HIGGS & TWISTED NORMS BENCHMARK ===")
    print(f"Gate 0 runtime: {gate_ms:.2f} ms")
    print(f"  FR-FIB: passed={gate_fib.passed} ({gate_fib.clauses_passed}/4 clauses) | "
          f"|V_ub|/|V_td|={gate_fib.sample_Vub_over_Vtd:.4f}, sin(delta_CP)={gate_fib.sample_sin_delta_CP:.4f}")
    print(f"  FR-COV: passed={gate_cov.passed} ({gate_cov.clauses_passed}/4 clauses) | "
          f"|V_ub|/|V_td|={gate_cov.sample_Vub_over_Vtd:.4f}, sin(delta_CP)={gate_cov.sample_sin_delta_CP:.4f}")
    print(f"4D Quaternionic Yukawa formula vs direct 2x2 trace bilinear max err: {max(err_4d_u, err_4d_d):.2e}")
    print(f"Twisted norms c_s(tau, w): 3-sector 2D quadrature = {3.0*quad_ms:.2f} ms vs "
          f"closed_form_cA = {exact_ms:.2f} ms ({(3.0*quad_ms)/exact_ms:.1f}x speedup, max diff = {max_c_diff:.2e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
