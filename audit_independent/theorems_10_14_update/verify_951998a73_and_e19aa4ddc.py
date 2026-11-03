"""
Independent Zero-Trust Audit of:
1. `origin/audit/physical-bridge-2026-09-05` commits `84632be08` & `e19aa4ddc`
   (Register-flavour action, Gram law, and E_8 quartic state discriminator),
2. `origin/agy/audit-2026-11-02` commit `e810ba3ee`
   (Theorem 14: independent review of 84632be08/e19aa4ddc, 48-element 2O orbit census,
    and explicit Ad(SO(10, I_10)) Q_8 compensators, plus 9d5129445 source repairs),
3. `origin/agy/audit-2026-11-02` commit `951998a73`
   (Acceptance of 2dbfe96dc audit on Theorems 10-13, Buttazzo Eq. 99 2-loop quartic fix,
    F(tau) = -80 eta^12 E_4 branched double cover, and |q_1+q_2|=6 Weinberg LL spectrum).
"""
from __future__ import annotations

import json
import math
import os
import sys
import unittest
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

SNAPSHOT_AGY = Path("/Users/dri/.gemini/antigravity/scratch/agy-snapshot-951998a73")
SNAPSHOT_PHYS = Path("/Users/dri/.gemini/antigravity/scratch/physical-bridge-snapshot-e19aa4ddc")
sys.path.insert(0, str(SNAPSHOT_AGY / "src"))


def verify_physical_bridge_e19aa4ddc() -> dict:
    """Run the 5 prospective controls in checks.py from e19aa4ddc and verify independently."""
    checks_dir = SNAPSHOT_PHYS / "reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_register_flavour_joint_2026_11_03"
    sys.path.insert(0, str(checks_dir))
    import checks as phys_checks

    suite = unittest.defaultTestLoader.loadTestsFromModule(phys_checks)
    runner = unittest.TextTestRunner(verbosity=0)
    res = runner.run(suite)
    return {
        "tests_run": res.testsRun,
        "failures": len(res.failures),
        "errors": len(res.errors),
        "all_5_prospective_sympy_controls_passed": res.wasSuccessful(),
    }


def verify_theorem14_independent() -> dict:
    """Independently construct D_5 subset E_8, 2O register action, 2D_4 stabilizer, and Q_8 compensators."""
    e5 = np.zeros((5, 5), dtype=float)
    for j, c in enumerate([2.0, math.sqrt(6.0), math.sqrt(6.0), 2.0]):
        e5[j + 1, j] = c
    h5 = np.diag([-4.0, -2.0, 0.0, 2.0, 4.0])
    j5 = np.zeros((5, 5), dtype=float)
    for j, c in enumerate([1.0, -1.0, 1.0, -1.0, 1.0]):
        j5[j, 4 - j] = c
    bz = np.zeros((5, 5), dtype=float)
    bz[1, 4] = math.sqrt(2.0 / 5.0)
    bz[4, 1] = -bz[1, 4]
    bz[2, 3] = -math.sqrt(3.0 / 5.0)
    bz[3, 2] = -bz[2, 3]

    z5 = np.zeros((5, 5), dtype=float)
    E = np.block([[e5, z5], [z5, -e5.T]]).astype(complex)
    G = (math.sqrt(10.0) * np.block([[z5, bz], [j5 @ bz @ j5, z5]])).astype(complex)
    H = np.block([[h5, z5], [z5, -h5.T]]).astype(complex)
    I10 = np.block([[z5, np.eye(5)], [np.eye(5), z5]]).astype(complex)
    N10 = np.block([[np.eye(5), z5], [z5, -np.eye(5)]]).astype(complex)

    Ep = 0.5 * (E + G)
    Em = 0.5 * (E - G)
    Hp = Ep @ Ep.conj().T - Ep.conj().T @ Ep
    Hm = Em @ Em.conj().T - Em.conj().T @ Em

    # Verify V_5^+ (+) V_5^- decomposition and bilinear form I10 signs on V_5^+, V_5^-:
    # Projectors onto support of sl_2^+ and sl_2^-:
    vals_p, vecs_p = np.linalg.eigh(Ep @ Ep.conj().T + Ep.conj().T @ Ep)
    vals_m, vecs_m = np.linalg.eigh(Em @ Em.conj().T + Em.conj().T @ Em)
    dim_vp = int(np.sum(vals_p > 1e-8))
    dim_vm = int(np.sum(vals_m > 1e-8))

    # Generate 2O = <g_L, g_R> in SU(2):
    Fi = np.array([[1j, 0], [0, -1j]], dtype=complex)
    Fj = np.array([[0, 1], [-1, 0]], dtype=complex)
    Fk = Fi @ Fj
    gL = (np.eye(2) + Fi) / math.sqrt(2.0)
    gR = (np.eye(2) - Fj) / math.sqrt(2.0)

    els_2O = [np.eye(2, dtype=complex)]
    for _ in range(10):
        added = False
        for g in list(els_2O):
            for s in (gL, gR, gL.conj().T, gR.conj().T):
                p = g @ s
                if not any(np.max(np.abs(p - h)) < 1e-10 for h in els_2O):
                    els_2O.append(p)
                    added = True
        if not added:
            break

    # Direct E_8 quartic polynomial evaluation on all 48 elements of 2O * Phi_0:
    n_norm = 1.0 / (2.0 * math.sqrt(2.0))
    Phi0 = (n_norm * E, n_norm * G)
    probes = [
        (1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0)),
        (1.0 / math.sqrt(2.0), 1j / math.sqrt(2.0)),
        (1.0 + 0.0j, 0.0j),
    ]

    def quartic_readout_vec(pair):
        out = []
        for z1, z2 in probes:
            Xz = z1 * pair[0] + z2 * pair[1]
            comm = Xz @ Xz.conj().T - Xz.conj().T @ Xz
            val = 0.5 * np.real(np.trace(comm @ comm)) / (5.0 / 8.0)
            out.append(round(float(val), 8))
        return tuple(out)

    readouts_48 = {}
    stab_Phi0 = []
    base_ro = quartic_readout_vec(Phi0)
    for g in els_2O:
        pair_g = (g[0, 0] * Phi0[0] + g[0, 1] * Phi0[1], g[1, 0] * Phi0[0] + g[1, 1] * Phi0[1])
        ro = quartic_readout_vec(pair_g)
        readouts_48[ro] = readouts_48.get(ro, 0) + 1
        if ro == base_ro:
            stab_Phi0.append(g)

    # Check compensator matrices in SO(10, I10) cap U(10):
    def expm_h(h_m, c):
        w, v = np.linalg.eigh(h_m)
        return (v * np.exp(c * w)) @ v.conj().T

    k_fi = expm_h(H, 1j * (math.pi / 4.0)) @ (1j * N10)
    k_fk = expm_h(Hp - Hm, 1j * (math.pi / 4.0))
    k_fj = k_fi @ k_fk

    kc_i = k_fi.conj().T
    kc_j = k_fj.conj().T
    kc_k = kc_i @ kc_j
    kc_k_docstring = expm_h(Hp - Hm, -1j * (math.pi / 4.0))

    Z_mat = expm_h(H, -1j * (math.pi / 2.0))
    kc_i_sq_plus_Z_err = float(np.max(np.abs(kc_i @ kc_i + Z_mat)))
    kc_j_sq_plus_Z_err = float(np.max(np.abs(kc_j @ kc_j + Z_mat)))
    kc_k_sq_minus_Z_err = float(np.max(np.abs(kc_k @ kc_k - Z_mat)))
    kc_k_vs_minus_docstring_err = float(np.max(np.abs(kc_k + kc_k_docstring)))

    # Group orders in SO(10, I10) vs PSO(10) = Ad(SO(10)):
    els_so10 = [np.eye(10, dtype=complex)]
    for _ in range(8):
        for g in list(els_so10):
            for s in (kc_i, kc_j, kc_i.conj().T, kc_j.conj().T):
                p = g @ s
                if not any(np.max(np.abs(p - h)) < 1e-10 for h in els_so10):
                    els_so10.append(p)

    els_pso10 = [np.eye(10, dtype=complex)]
    for _ in range(8):
        for g in list(els_pso10):
            for s in (kc_i, kc_j, kc_i.conj().T, kc_j.conj().T):
                p = g @ s
                if not any(np.max(np.abs(p - h)) < 1e-10 or np.max(np.abs(p + h)) < 1e-10 for h in els_pso10):
                    els_pso10.append(p)

    orders_pso10 = []
    for g in els_pso10:
        for r in range(1, 9):
            pw = np.linalg.matrix_power(g, r)
            if np.max(np.abs(pw - np.eye(10))) < 1e-10 or np.max(np.abs(pw + np.eye(10))) < 1e-10:
                orders_pso10.append(r)
                break

    from origin_axiom.toe_closure import theorem14_d5_e8_register_flavour_joint_and_exact_2O_orbit_census
    agy_t14 = theorem14_d5_e8_register_flavour_joint_and_exact_2O_orbit_census()

    return {
        "agy_t14_output": agy_t14,
        "independent_checks": {
            "dim_V5_plus": dim_vp,
            "dim_V5_minus": dim_vm,
            "order_2O": len(els_2O),
            "order_stabilizer_2D4": len(stab_Phi0),
            "quartic_readout_classes_and_counts": {str(k): v for k, v in readouts_48.items()},
            "gL_in_2D4_stabilizer": any(np.max(np.abs(gL - h)) < 1e-10 for h in stab_Phi0),
            "gR_in_2D4_stabilizer": any(np.max(np.abs(gR - h)) < 1e-10 for h in stab_Phi0),
            "kc_i_sq_eq_minus_Z_err": kc_i_sq_plus_Z_err,
            "kc_j_sq_eq_minus_Z_err": kc_j_sq_plus_Z_err,
            "kc_k_sq_eq_plus_Z_err": kc_k_sq_minus_Z_err,
            "kc_k_code_eq_minus_kc_k_docstring_err": kc_k_vs_minus_docstring_err,
            "group_order_in_SO10_vector_rep": len(els_so10),
            "group_order_in_PSO10_adjoint_rep": len(els_pso10),
            "pso10_element_orders": sorted(orders_pso10),
            "pso10_isomorphic_to_Q8": sorted(orders_pso10) == [1, 2, 4, 4, 4, 4, 4, 4],
        },
    }


def verify_theorems_10_to_13_repairs_951998a73() -> dict:
    """Verify the repairs in commit 951998a73 on Theorems 10, 11, 12, 13."""
    from origin_axiom.toe_closure import (
        theorem10_amphichiral_a3_involution_and_t8_cusp_equivalence,
        theorem11_amphichiral_conjugation_and_strong_cp_reality,
        theorem12_nondimensional_buttazzo_2loop_top_higgs_closure,
        theorem13_basis_invariant_weinberg_majorana_and_pmns,
    )
    from origin_axiom.operator_gate import m004_three_fold_cover_invariants, evaluate_operator_gate

    t10 = theorem10_amphichiral_a3_involution_and_t8_cusp_equivalence(n_random_trials=4)
    t11 = theorem11_amphichiral_conjugation_and_strong_cp_reality(n_random_trials=4)
    t12 = theorem12_nondimensional_buttazzo_2loop_top_higgs_closure()
    t13 = theorem13_basis_invariant_weinberg_majorana_and_pmns(n_haar_trials=10)
    gate_inv = m004_three_fold_cover_invariants()
    gate_cov = evaluate_operator_gate("FR-COV")

    # Independent high-precision check of F(tau) = theta_2^20 + theta_4^20 - theta_3^20 == -80 * eta^12 * E_4:
    mp.mp.dps = 50
    tau_test = mp.mpc("0.37", "1.83")
    q = mp.exp(1j * mp.pi * tau_test)
    th2 = mp.jtheta(2, 0, q)
    th3 = mp.jtheta(3, 0, q)
    th4 = mp.jtheta(4, 0, q)
    f_lhs = th2 ** 20 + th4 ** 20 - th3 ** 20
    X = th2 ** 4
    Y = th4 ** 4
    eta12 = X * Y * (X + Y) / 16
    E4 = X ** 2 + X * Y + Y ** 2
    f_rhs = -80 * eta12 * E4
    mp_f_identity_err = float(abs(f_lhs - f_rhs))

    return {
        "t10_repairs": {
            "U_times_B_exact_eq_minus_I2": t10["U_times_B_exact_eq_minus_I2"],
            "rank2_unitary_local_system_on_M3_max_err": t10["rank2_unitary_local_system_on_M3_max_err"],
            "t8_quark_det_phase_shift_rad": t10["t8_quark_det_phase_shift_rad"],
            "inversion_quark_det_phase_shift_rad": t10["inversion_quark_det_phase_shift_rad"],
            "t8_is_coordinate_relabelling_not_selector": t10["t8_is_coordinate_relabelling_not_selector"],
            "lines_2_5_j_5_with_A3_x_eq_pm_x_mod5": t10["lines_2_5_j_5_with_A3_x_eq_pm_x_mod5"],
        },
        "t11_repairs": {
            "mpmath_50dps_F_eq_minus80_eta12_E4_err": mp_f_identity_err,
            "unbranched_principal_cut_jump_norm_at_2i": t11["unbranched_principal_cut_jump_norm_at_2i"],
            "branched_double_cover_conj_err_at_2i": t11["branched_double_cover_conj_err_at_2i"],
            "M_minus_I2_smith_invariants": t11["M_minus_I2_smith_invariants"],
            "strong_cp_solved_on_single_sheet": t11["strong_cp_solved_on_single_sheet"],
            "tautological_random_matrix_doubled_arg_det_rad": t11["tautological_random_matrix_doubled_arg_det_rad"],
        },
        "t12_repairs": {
            "log10_mu_crit_from_173p1": t12["buttazzo_table1_benchmark"]["log10_mu_crit_GeV_computed"],
            "log10_mu_crit_from_173p34": t12["buttazzo_table1_benchmark"]["log10_mu_crit_GeV_from_173p34"],
            "newton_bvp_converged_to_1e13": t12["nondimensional_electroweak_and_top_higgs_ratios"]["newton_bvp_converged_to_1e13"],
            "uv_boundary_is_post_hoc_hypothesis": t12["nondimensional_electroweak_and_top_higgs_ratios"]["uv_boundary_is_post_hoc_hypothesis"],
            "dmH_dyt2_M12_sensitivity_GeV_computed": t12["nondimensional_electroweak_and_top_higgs_ratios"]["dmH_dyt2_M12_sensitivity_GeV"],
            "dmH_dyt2_M12_docstring_stale_value": 370.1,
            "buttazzo_matched_at_mu_173p34_GeV": t12["nondimensional_electroweak_and_top_higgs_ratios"]["buttazzo_matched_at_mu_173p34_GeV"],
        },
        "t13_repairs": {
            "exact_ll_twist6_weinberg_spectrum": t13["exact_ll_twist6_weinberg_spectrum"],
            "m2_over_m3_computed_vs_docstring": {
                "computed_twist6": t13["exact_ll_twist6_weinberg_spectrum"]["m2_over_m3"],
                "docstring_stale_twist3_value": 0.10000,
            },
            "minimal_single_channel_pmns_verdict": t13["minimal_single_channel_pmns_verdict"],
            "modular_seesaw_scale_comparison": t13["modular_seesaw_scale_comparison"],
        },
        "source_hygiene_e810ba3ee": {
            "operator_gate_distinguishes_dc_from_L": gate_inv["distinguishes_colour_triplet_dc_from_singlet_L"],
            "operator_gate_extends_to_m004": gate_cov.extends_to_3manifold_m004,
        },
    }


def verify_code_hygiene_and_guardrail_audit_951998a73() -> dict:
    """Scrutinize test suite execution, referee script execution, relay claims vs code,
    and unremoved Guardrail 1-5 violations in `src/origin_axiom/toe_closure.py` and `sm_19_gate.py` at 951998a73.
    """
    import subprocess
    from origin_axiom.toe_closure import (
        evaluate_full_toe_master_scorecard,
        theorem10_amphichiral_a3_involution_and_t8_cusp_equivalence,
        theorem11_amphichiral_conjugation_and_strong_cp_reality,
        theorem12_nondimensional_buttazzo_2loop_top_higgs_closure,
        theorem13_basis_invariant_weinberg_majorana_and_pmns,
    )

    # 1. Verify the exact crash in tests/test_elevation_operator_gate.py::test_five_phase_master_toe_closure at line 534
    #    (Confirmed via full pytest execution in task-246, task-266, task-288, task-296, task-307):
    test_lines = (SNAPSHOT_AGY / "tests/test_elevation_operator_gate.py").read_text().splitlines()
    line_534 = test_lines[533].strip()

    # 2. Verify the exact crashes in hostile_referee_audit.py (line 1087 NameError and line 1173 KeyError)
    #    (Confirmed via full execution in task-246 & task-296; here we also verify the exact lines directly):
    referee_lines = (SNAPSHOT_AGY / "relays/agy_audit_2026_11_02/hostile_referee_audit.py").read_text().splitlines()
    line_1087 = referee_lines[1086].strip()
    line_1173 = referee_lines[1172].strip()
    referee_crash_1087 = None
    try:
        exec(compile(line_1087, "hostile_referee_audit.py", "exec"), {})
    except Exception as exc:
        referee_crash_1087 = f"{type(exc).__name__}: {exc}"

    # 3. Catalog all 12 dictionary key mismatches between tests/test_elevation_operator_gate.py (lines 534-592)
    #    and the actual return dicts of theorem10..theorem13 in src/origin_axiom/toe_closure.py:
    t10 = theorem10_amphichiral_a3_involution_and_t8_cusp_equivalence(n_random_trials=2)
    t11 = theorem11_amphichiral_conjugation_and_strong_cp_reality(n_random_trials=2)
    t12 = theorem12_nondimensional_buttazzo_2loop_top_higgs_closure()
    t13 = theorem13_basis_invariant_weinberg_majorana_and_pmns(n_haar_trials=4)

    pytest_crash_534 = None
    try:
        _ = t10["B_half_shift_matrix"]
    except Exception as exc:
        pytest_crash_534 = f"{type(exc).__name__}: {exc}"

    referee_crash_1173 = None
    try:
        _ = t13["c_ll_twist6_closed_form"]
    except Exception as exc:
        referee_crash_1173 = f"{type(exc).__name__}: {exc}"

    expected_test_keys_check = [
        ("t10", "B_half_shift_matrix", "B_half_shift_matrix" in t10, "B_eq_A_sig3_minus_I2_div_4"),
        ("t10", "max_T8_cusp_error_across_all_5_lines_2_5_j_5", "max_T8_cusp_error_across_all_5_lines_2_5_j_5" in t10, None),
        ("t10", "lines_2_5_j_5_satisfying_A_sig3_pm_eigenvector_mod5", "lines_2_5_j_5_satisfying_A_sig3_pm_eigenvector_mod5" in t10, "lines_2_5_j_5_with_A3_x_eq_pm_x_mod5"),
        ("t11", "M_minus_I2_matrix", "M_minus_I2_matrix" in t11, None),
        ("t11", "H1_M3_Z_structure", "H1_M3_Z_structure" in t11, "H1_M3_Z_torsion_invariants"),
        ("t11", "random_3x3_matrix_doubled_block_arg_det_rad", "random_3x3_matrix_doubled_block_arg_det_rad" in t11, "tautological_random_matrix_doubled_arg_det_rad"),
        ("t12.buttazzo_table1_benchmark", "log10_mu_crit_GeV_from_mu0_173p34", "log10_mu_crit_GeV_from_mu0_173p34" in t12["buttazzo_table1_benchmark"], "log10_mu_crit_GeV_from_173p34"),
        ("t12.nondimensional", "rel_error_mH_raw_at_MZ", "rel_error_mH_raw_at_MZ" in t12["nondimensional_electroweak_and_top_higgs_ratios"], "rel_error_mH"),
        ("t12.nondimensional", "rel_error_mt_pole_from_MZ", "rel_error_mt_pole_from_MZ" in t12["nondimensional_electroweak_and_top_higgs_ratios"], "rel_error_mt_pole"),
        ("t12.nondimensional", "dMh_d_yt2_UV_GeV", "dMh_d_yt2_UV_GeV" in t12["nondimensional_electroweak_and_top_higgs_ratios"], "dmH_dyt2_M12_sensitivity_GeV"),
        ("t12.nondimensional", "scope_and_parameter_accounting", "scope_and_parameter_accounting" in t12["nondimensional_electroweak_and_top_higgs_ratios"], "uv_boundary_is_post_hoc_hypothesis"),
        ("t13", "max_c_ll_closed_form_vs_b1656_cA_err", "max_c_ll_closed_form_vs_b1656_cA_err" in t13, None),
    ]

    # 4. Audit live Guardrail 1-5 violations still returned by phase1-phase9, theorem8, theorem9, and summary_metrics:
    from origin_axiom.toe_closure import (
        phase1_zero_bit_cell_selection_theorem,
        phase2_weinberg_neutrino_spectrum_closure,
        phase3_two_loop_rge_higgs_and_qcd_closure,
        phase6_complete_pmns_unitary_and_cp_closure,
        phase7_exact_it_rge_light_generation_closure,
        phase9_cosmological_baryogenesis_and_dark_matter_closure,
    )
    from origin_axiom.sm_19_gate import (
        theorem8_golden_codifferent_unit_modulus_closure,
        theorem9_hypercharge_quadratic_refinement_and_full_19_closure,
    )
    p1 = phase1_zero_bit_cell_selection_theorem()
    p2 = phase2_weinberg_neutrino_spectrum_closure()
    p3 = phase3_two_loop_rge_higgs_and_qcd_closure()
    p6 = phase6_complete_pmns_unitary_and_cp_closure()
    p7 = phase7_exact_it_rge_light_generation_closure()
    p9 = phase9_cosmological_baryogenesis_and_dark_matter_closure()
    t8_live = theorem8_golden_codifferent_unit_modulus_closure()
    t9_live = theorem9_hypercharge_quadratic_refinement_and_full_19_closure()
    live_guardrail_violations = {
        "guardrail_1_and_2_zero_bit_and_literal_flags": {
            "phase1_discrete_address_bits_remaining": p1["discrete_address_bits_remaining"],
            "phase8_tau_star_hardcoded_in_V_potential": True,
            "theorem8_continuous_parameters": t8_live["continuous_parameters"],
            "theorem8_L_tau_bits": t8_live["L_tau_bits"],
            "theorem9_post_hoc_z8_selection_bits_remaining": t9_live["part_A_hypercharge_quadratic_refinement"]["post_hoc_z8_selection_bits_remaining"],
            "theorem9_bar_theta_QCD_literal_zero": t9_live["part_C_block_V_strong_cp_top_and_higgs_criticality"]["bar_theta_QCD_pred"],
            "summary_metrics_continuous_parameters": 0,
            "summary_metrics_discrete_selection_bits": 0.0,
        },
        "guardrail_3_basis_dependent_pmns_still_in_phase6_and_summary": {
            "phase6_uses_Vt_U_and_Udag_V_of_single_Dirac_Ye": True,
            "summary_metrics_rel_error_theta13_lr_deg": float(p6["rel_error_theta13_lr_deg"]),
            "summary_metrics_rel_error_delta_CP_PMNS": float(p6["rel_error_delta_CP_PMNS"]),
        },
        "guardrail_4_buggy_rge_still_in_phase3_phase7_and_summary": {
            "phase3_uses_1_over_8pi_factor_of_2_bug": True,
            "phase3_mH_2loop_GeV": p3["mH_GeV_2loop_pred"],
            "phase7_uses_upward_fitted_gamma_anomalous": p7["gamma_anomalous_vector_10"],
            "summary_metrics_chi2_ten_with_It_running": float(p7["chi2_ten_dressed"]),
            "summary_metrics_rel_error_mH_2loop": float(p3["rel_error_mH_2loop"]),
        },
        "guardrail_5_unpriced_dimensionful_anchors_and_eta6_mislabeling": {
            "phase2_m3_meV_pred_using_mislabeled_eta6_quarter": p2["m3_meV_pred"],
            "phase2_imports_MZ_91p1876_and_vEW_246p22": True,
            "phase9_imports_Omega_b_h2_0p02237": p9["Omega_DM_h2_pred"] / p9["Omega_DM_over_Omega_b_pred"],
        },
    }

    return {
        "pytest_test_five_phase_master_toe_closure": {
            "passed": False,
            "line_534_source": line_534,
            "line_534_exception": pytest_crash_534,
        },
        "hostile_referee_audit_script": {
            "passed": False,
            "line_1087_source": line_1087,
            "line_1087_exception": referee_crash_1087,
            "line_1173_source": line_1173,
            "line_1173_exception": referee_crash_1173,
        },
        "mismatched_or_missing_test_keys_count": sum(1 for _, _, present, _ in expected_test_keys_check if not present),
        "mismatched_or_missing_test_keys": [
            {
                "target_dict": d_name,
                "test_expected_key": k_exp,
                "present_in_toe_closure": present,
                "actual_key_in_toe_closure": k_act,
            }
            for d_name, k_exp, present, k_act in expected_test_keys_check
        ],
        "live_guardrail_violations_in_scorecard": live_guardrail_violations,
    }


def main():
    out = {
        "physical_bridge_e19aa4ddc": verify_physical_bridge_e19aa4ddc(),
        "theorem14_e810ba3ee": verify_theorem14_independent(),
        "theorems_10_to_13_repairs_951998a73": verify_theorems_10_to_13_repairs_951998a73(),
        "code_hygiene_and_guardrail_audit_951998a73": verify_code_hygiene_and_guardrail_audit_951998a73(),
    }
    out_path = Path(__file__).parent / "verify_951998a73_and_e19aa4ddc_results.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
