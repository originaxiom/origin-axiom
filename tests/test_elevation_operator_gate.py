"""
Tests locking the three core elevation modules in src/origin_axiom/:
1. src/origin_axiom/twisted_norms.py (Theorem 1: exact closed-form c_s(tau, w), resolution of B1788 (a)-(b)).
2. src/origin_axiom/operator_gate.py (Gate 0: The Algebraic Operator Gate, Theorem 2: CKM corner inversion,
   and the 4D Quaternionic + 3-Fold Cover Frame FR-COV).
3. src/origin_axiom/stepb_audit.py (Step B choice 30900 decoding, 7,680 order-12 massless-electron choices,
   and strict 10-column physical-choice mask).
"""
from __future__ import annotations

from fractions import Fraction
import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from origin_axiom.twisted_norms import (
    channel_pair_decay_exponents,
    closed_form_cA,
    cusp_combination_D_inf,
    sector_higgs_twist_multiple,
)
from origin_axiom.operator_gate import (
    ckm_full_diagnostics,
    direct_quaternion_coupling,
    evaluate_operator_gate,
    lagrange_ckm_compromise,
    m004_three_fold_cover_invariants,
    quaternionic_4d_yukawa,
    schur_quaternionic_bimodule_decomposition,
    serre_dr_dot_dr_eta6_identity,
    yukawa_4d_determinant_factorization,
    z3_norm_preserving_scalar_higgs,
)
from origin_axiom.parameter_ledger import (
    compare_frame_input_ledgers,
    m004_cover_monodromy_fixed_torsion,
    m004_cover_spin_monodromy_cosets,
    nineteen_parameter_impact_table,
)
from origin_axiom.sm_19_gate import (
    derive_scalar_higgs_characters_from_hypercharge,
    evaluate_sm_19_gate,
    inter_sector_yukawa_unification,
    stabilized_modulus_candidates,
    step1_golden_5torsion_norm_preserving_solution,
    step2_physical_spin_flavour_locking_bridge,
    step3_pmns_and_m004_gauge_thresholds,
    step4_sealed_stepb_v2_fr_cov_verdict,
    theorem8_golden_codifferent_unit_modulus_closure,
    theorem9_hypercharge_quadratic_refinement_and_full_19_closure,
)
from origin_axiom.toe_closure import (
    evaluate_full_toe_master_scorecard,
)
from origin_axiom.stepb_audit import (
    count_order12_massless_electron_choices,
    decode_stepb_choice_index,
    repaired_stepb_k_cell_audit,
    strict_ten_physical_choice_mask,
)


def test_theorem1_sector_independence_and_closed_form_c():
    # 1. All three fermion sectors have |q_L + q_R| == 3:
    assert abs(sector_higgs_twist_multiple("up")) == 3
    assert abs(sector_higgs_twist_multiple("down")) == 3
    assert abs(sector_higgs_twist_multiple("lepton")) == 3

    # 2. Cusp combination D^inf(alpha) = c_j^inf + c_k^inf - c_1^inf - c_i^inf
    # vanishes on (0, 1/2) iff alpha in {1/12, 1/4, 5/12} (resolving B1788 Hypothesis (b)):
    for alpha_zero in (Fraction(1, 12), Fraction(1, 4), Fraction(5, 12)):
        d_val = cusp_combination_D_inf(alpha_zero)
        assert d_val is not None and abs(d_val) < 1e-14

    for alpha_nonzero in (Fraction(1, 5), Fraction(2, 5), Fraction(1, 7), Fraction(3, 8), Fraction(4, 9)):
        d_val = cusp_combination_D_inf(alpha_nonzero)
        assert d_val is not None and abs(d_val) > 0.5

    # 3. Exact fermion-independent decay exponents E(c_1 - c_i) and E(c_j - c_k)
    # satisfy E(c_1 - c_i) + E(c_j - c_k) = 1/4 and resolve B1788's anomalies:
    exp_2_5 = channel_pair_decay_exponents(Fraction(2, 5))
    assert exp_2_5["E_c1_minus_ci"] == Fraction(1, 10)
    assert exp_2_5["E_cj_minus_ck"] == Fraction(3, 20)
    assert exp_2_5["sum"] == Fraction(1, 4)

    exp_1_7 = channel_pair_decay_exponents(Fraction(1, 7))
    assert exp_1_7["E_c1_minus_ci"] == Fraction(3, 14)
    assert exp_1_7["E_cj_minus_ck"] == Fraction(1, 28)
    assert exp_1_7["sum"] == Fraction(1, 4)

    exp_4_9 = channel_pair_decay_exponents(Fraction(4, 9))
    assert exp_4_9["E_c1_minus_ci"] == Fraction(1, 6)
    assert exp_4_9["E_cj_minus_ck"] == Fraction(1, 12)
    assert exp_4_9["sum"] == Fraction(1, 4)

    # 4. Compare closed_form_cA against B1691's 2D Gauss-Legendre quadrature cA:
    v_dir = ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction"
    sys.path.insert(0, str(v_dir))
    import b1656_funcs as B

    tau = complex(0.17, 1.85)
    for a_line, b_line in ((Fraction(2, 5), Fraction(1, 10)), (Fraction(1, 3), Fraction(1, 9))):
        w = B.line_w(a_line, b_line, tau)
        x, y = B.sector_twists(w, tau, 1, -4)
        r_res = B.residues(x, y, tau)
        c_quad = B.cA(x, y, tau, r_res)
        c_exact = closed_form_cA(tau, a_line, b_line)
        for s in ("1", "i", "j", "k"):
            assert c_exact[s] is not None
            if c_quad[s] is not None:
                assert abs(c_quad[s] - c_exact[s]) < 5e-12


def test_theorem2_4d_quaternionic_yukawa_and_operator_gate():
    # 1. Verify exact 4D quaternionic Yukawa formula against direct 2x2 quaternion trace bilinear:
    rng = np.random.default_rng(42)
    for a0 in (0.0 + 0.0j, 0.35 - 0.21j):
        h_vec = rng.normal(size=3) + 1j * rng.normal(size=3)
        m1 = complex(rng.normal() + 1j * rng.normal())
        m_perp = rng.normal(size=3) + 1j * rng.normal(size=3)

        y_formula = quaternionic_4d_yukawa(a0, h_vec, m1, m_perp)
        y_direct = direct_quaternion_coupling(a0, h_vec, m1, m_perp)
        assert np.allclose(y_formula, y_direct, atol=1e-14)

        # At a0 == 0, Y h = Y^T h = (h . h) m_perp; at a0 != 0, Y h picks up a0*(m1*h - m_perp x h):
        expected_yh = (
            np.dot(h_vec, h_vec) * m_perp
            + a0 * (m1 * h_vec - np.cross(m_perp, h_vec))
        )
        assert np.allclose(y_formula @ h_vec, expected_yh, atol=1e-14)

    # 2. Verify Lagrange-multiplier CKM compromise (0.7347, 0.7347, 1.3611):
    r12, r23, r13 = lagrange_ckm_compromise()
    assert abs(r12 - 0.7347) < 5e-4
    assert abs(r23 - 0.7347) < 5e-4
    assert abs(r13 - 1.3611) < 5e-4
    assert abs((r13 / (r12 * r23)) - (0.22500 * 0.04182 / 0.003732)) < 1e-12

    # 3. Verify m004 3-fold cover and colour-center Wilson line torsion invariants:
    inv = m004_three_fold_cover_invariants()
    assert inv["det_LR_minus_i" if "det_LR_minus_i" in inv else "det_LR_minus_I"] == -1
    assert inv["deck_only_S3_commutant_dim_R"] == 2
    assert inv["deck_commutant_dim_R"] == 1
    assert inv["forces_H_proportional_to_I"] is True
    assert abs(float(inv["alexander_at_omega_abs"]) - 4.0) < 1e-12
    assert abs(float(inv["reidemeister_torsion_at_omega_abs"]) - 4.0 / math.sqrt(3.0)) < 1e-12

    # 4. Evaluate Gate 0 (The Algebraic Operator Gate) on FR-FIB vs FR-COV:
    rep_fib = evaluate_operator_gate("FR-FIB")
    assert rep_fib.passed is False
    assert rep_fib.clauses_passed == 0
    assert rep_fib.sample_Vub_over_Vtd > 10.0

    rep_cov = evaluate_operator_gate("FR-COV")
    assert rep_cov.passed is True
    assert rep_cov.clauses_passed == 4
    assert rep_cov.sample_Vub_over_Vtd < 1.0


def test_stepb_structural_audit_defects():
    manifest = json.loads(
        (ROOT / "scripts/census/REFINED_CENSUS_MANIFEST.json").read_text(encoding="utf-8")
    )["per_file"]

    # 1. Decode choice 30900 selected by six_mixture in B1825:
    c30900 = decode_stepb_choice_index(30900, manifest)
    assert c30900["line"] == (Fraction(2, 5), Fraction(0, 1))
    assert c30900["direction"] == "F_26"
    assert c30900["radius"] == "L_max"
    assert c30900["reading"] == ("S~", "S", "S")
    assert c30900["has_complex_ckm"] is True

    # And verify the two null-quaternion directions R (d_idx=2) and t=-5/288 (d_idx=3) have has_complex_ckm=False:
    c_r = decode_stepb_choice_index(2 * 16, manifest)
    c_t = decode_stepb_choice_index(3 * 16, manifest)
    assert c_r["direction"] == "R" and c_r["has_complex_ckm"] is False
    assert c_t["direction"] == "t=-5/288" and c_t["has_complex_ckm"] is False

    # 2. Count order-12 massless-electron choices included in physical_choice:
    o12 = count_order12_massless_electron_choices(manifest)
    assert o12["order_12_lines"] == 48
    assert o12["order_12_total_choices"] == 9216
    assert o12["order_12_choices_in_physical_choice"] == 7680
    assert abs(float(o12["fraction_of_40000_physical_choices"]) - 0.192) < 1e-12

    # 3. Verify strict_ten_physical_choice_mask rejects massless-electron choices (col 5 = -inf)
    # even when CKM columns 6..9 are finite:
    f_mat = np.full((4, 10), -2.0, dtype=float)
    f_mat[2:, 5] = -np.inf  # choice 1 has massless electron (e/tau = 0)
    r_tab = np.array([[0, 1], [2, 3]], dtype=np.int64)
    phys_ten, zero10 = strict_ten_physical_choice_mask(f_mat, r_tab)
    assert phys_ten.tolist() == [True, False]
    assert zero10[1, 5] == True and not zero10[1, 6:10].any()


def test_theorem3_theorem4_and_19_parameter_ledger():
    # 1. Theorem 3: Exact quaternionic determinant factorization
    # det(Y_s^4D) == (a_0^2 + h.h) * (m_1^2 + m_perp.m_perp) * (a_0*m_1 + h.m_perp)
    rng = np.random.default_rng(20261103)
    for _ in range(25):
        a0 = complex(rng.normal() + 1j * rng.normal())
        h_vec = rng.normal(size=3) + 1j * rng.normal(size=3)
        m1 = complex(rng.normal() + 1j * rng.normal())
        m_perp = rng.normal(size=3) + 1j * rng.normal(size=3)
        res = yukawa_4d_determinant_factorization(a0, h_vec, m1, m_perp)
        assert float(res["rel_error"]) < 1e-13

        # On the 3D null cone h.h = 0 (like primary R(tau)), det(Y) == 0 at a0 = 0
        # but det(Y) != 0 as soon as a0 != 0:
        h_null = np.array([1.0 + 0.0j, 0.0 + 0.0j, 1j], dtype=complex)  # h_null . h_null == 0
        res_zero = yukawa_4d_determinant_factorization(0.0, h_null, m1, m_perp)
        res_lifted = yukawa_4d_determinant_factorization(a0, h_null, m1, m_perp)
        assert abs(complex(res_zero["det_Y"])) < 1e-14
        assert abs(complex(res_lifted["det_Y"])) > 1e-3

    # 2. Theorem 4: DR(tau) . DR(tau) == (1/4) eta(tau)^6 modular identity:
    id4 = serre_dr_dot_dr_eta6_identity(0.093359375 + 2.742578125j)
    assert float(id4["rel_error"]) < 1e-13

    # 3. Input-reduction ledger & 0-19 parameter table:
    tors = m004_cover_monodromy_fixed_torsion()
    assert tors["det_LR_minus_I"] == -1
    assert tors["non_zero_fixed_points_k1"] == 0
    assert tors["det_LR3_minus_I"] == -16
    assert tors["non_zero_fixed_points_k3"] == 15
    assert tors["t_orbits_in_non_zero_fixed_k3"] == 5

    led = compare_frame_input_ledgers()
    assert led["FR_FIB"]["total_discrete_choices"] == 497952
    assert abs(float(led["FR_FIB"]["total_discrete_bits"]) - math.log2(497952)) < 1e-12
    assert led["FR_COV"]["total_discrete_choices"] == 6
    assert float(led["reductions"]["discrete_bits_saved"]) > 16.3
    assert led["reductions"]["hidden_kinetic_metric_reals_eliminated"] == 8

    table19 = nineteen_parameter_impact_table()
    assert len(table19) == 10
    all_names = [n for row in table19 for n in row["names"]]
    assert len(all_names) == 19


def test_seven_pillars_sm_19_gate_preparation():
    # Pillar 1: Repaired Step B K-cell audit and strict physical choice counts
    manifest = json.loads(
        (ROOT / "scripts/census/REFINED_CENSUS_MANIFEST.json").read_text(encoding="utf-8")
    )["per_file"]
    run_json = json.loads(
        (ROOT / "frontier/B1825_step_b_the_nine_from_one_address/verification/run.json").read_text(
            encoding="utf-8"
        )
    )
    k_audit = repaired_stepb_k_cell_audit(run_json, manifest)
    assert k_audit["n_total_choices"] == 50880
    assert k_audit["n_ckm_physical_choices"] == 40000
    assert k_audit["n_massless_electron_choices_removed"] == 7680
    assert k_audit["n_strict_ten_physical_choices"] == 32320
    assert k_audit["n_deduplicated_strict_physical_choices"] == 16160
    assert abs(float(k_audit["den_inflation_bits"]) - 4.735119929845) < 1e-10
    assert not math.isfinite(float(k_audit["ckm_clause_best_chi2_4_in_six_window"]))

    # Pillar 2: Spin-structure cosets of (LR)^3 - I = 4 U on M_3 -> m004
    spin = m004_cover_spin_monodromy_cosets()
    assert spin["det_U"] == -1
    assert spin["spin_coset_point_counts"] == {"(0,0)": 16, "(1,0)": 16, "(0,1)": 16, "(1,1)": 16}
    assert spin["ns_coset_contains_3_8_3_8"] is True
    assert spin["ns_gamma2_orbit_count"] == 2
    assert spin["golden_2_5_1_10_is_spin_shifted_5_torsion"] is True

    # Pillar 3: Theorem 5 (Schur-Quaternionic Bimodule Decomposition) & Theorem 6 (Z_3 Norm-Preserving Scalar Higgs)
    rng = np.random.default_rng(20261104)
    for _ in range(15):
        a0 = complex(rng.normal() + 1j * rng.normal())
        h_vec = rng.normal(size=3) + 1j * rng.normal(size=3)
        m1 = complex(rng.normal() + 1j * rng.normal())
        m_perp = rng.normal(size=3) + 1j * rng.normal(size=3)
        bim = schur_quaternionic_bimodule_decomposition(a0, h_vec, m1, m_perp)
        assert float(bim["max_matrix_diff"]) < 1e-14
        assert float(bim["det_A_rel_error"]) < 1e-13
        assert float(bim["det_B_rel_error"]) < 1e-13

    thm6 = z3_norm_preserving_scalar_higgs()
    assert float(thm6["max_norm_deviation"]) < 1e-12

    # Pillar 4: Inter-sector Yukawa unification (structural call check; held-out ratios blinded per P-676)
    unif = inter_sector_yukawa_unification()
    assert isinstance(unif, dict)

    # Pillar 6: Parameter-free modulus stabilization candidates
    mods = stabilized_modulus_candidates()
    assert mods["LR3_trace"] == 18
    assert mods["LR3_discriminant"] == 320
    assert abs(mods["tau_apex_LR3"][0] - 0.5) < 1e-14
    assert abs(mods["tau_apex_LR3"][1] - 0.5 * math.sqrt(5.0)) < 1e-14
    assert mods["continuous_parameters_when_stabilized"] == 0

    # Pillar 5 & 7: Unified 0-19 SM Gate progression across FR-FIB, FR-COV+Thm6, and FR-COV+Thm6+1loop RG
    gate19 = evaluate_sm_19_gate()
    arms = gate19["arms_at_frozen_tau_star"]
    fib = arms["FR_FIB_baseline"]
    cov6 = arms["FR_COV_Theorem6_zero_param"]
    cov6_rg = arms["FR_COV_Theorem6_plus_1loop_RG"]

    assert abs(float(fib["chi2_ten"]) - 291.486662) < 1e-3
    assert float(fib["Vub_over_Vtd"]) > 10.0

    # Theorem 6 Z_3 norm-preserving scalar improves BOTH chi2_six and chi2_ckm at frozen tau* with 0 free parameters:
    assert float(cov6["chi2_six"]) < float(fib["chi2_six"])
    assert float(cov6["chi2_ckm"]) < float(fib["chi2_ckm"])
    assert float(cov6["chi2_ten"]) < 230.0
    assert float(cov6["Vub_over_Vtd"]) < 1.0

    # Adding 1-loop SM top-Yukawa RG running drops chi2_ten further to ~161.70 at frozen tau*:
    assert float(cov6_rg["chi2_ten"]) < 162.0
    assert gate19["parameter_table_count"] == 19


def test_four_sequential_steps_stepb_v2_closure():
    # Step 1: Exact norm-preserving (Z_2, Z_8, -1) Golden 5-torsion solution on (2/5, 0)
    s1 = step1_golden_5torsion_norm_preserving_solution()
    assert float(s1["norm_preservation_up"]) < 1e-14
    assert float(s1["norm_preservation_down"]) < 1e-14
    assert float(s1["norm_preservation_lepton"]) < 1e-14

    tree = s1["pure_tree_level"]
    assert tree["passes_all_three_gates"] is True
    assert abs(float(tree["chi2_six"]) - 6.8343) < 1e-2
    assert abs(float(tree["chi2_ckm"]) - 0.3648) < 1e-2
    assert abs(float(tree["chi2_ten"]) - 7.1991) < 1e-2
    assert abs(float(tree["Vub_over_Vtd"]) - 0.4111) < 1e-2

    rg = s1["with_1loop_rg"]
    assert rg["passes_all_three_gates"] is True
    assert float(rg["chi2_ten"]) < 6.0

    # Step 2: Physical spin-flavour locking bridge on M_3 -> m004
    s2 = step2_physical_spin_flavour_locking_bridge()
    assert s2["n_raw_description_pairs"] == 16
    assert s2["n_simultaneous_twist_orbits"] == 4
    assert s2["trivial_defect_orbit_size"] == 4
    assert s2["locked_8torsion_coset_sizes"] == {"(0,0)": 16, "(1,0)": 16, "(0,1)": 16, "(1,1)": 16}
    assert s2["independent_flavour_sign_freedom_remaining"] == 0

    # Step 3: Block IV (m004 Ray-Singer gauge threshold)
    s3 = step3_pmns_and_m004_gauge_thresholds()
    b4 = s3["block_IV_gauge_unification"]
    assert abs(float(b4["delta_alpha3_inv_RS_threshold"]) - (-7.0 * math.log(4.0 / math.sqrt(3.0)))) < 1e-12
    assert float(b4["rel_error_alpha_s_MZ"]) < 0.035

    # Step 4: Sealed Step B v2 (FR-COV) hyperbolic acceptance area & positive C_ten compression
    s4 = step4_sealed_stepb_v2_fr_cov_verdict()
    assert s4["in_support"] is True
    assert float(s4["overlap_fraction_A_ten_over_A_six"]) > 0.90
    assert float(s4["conditional_ckm_cost_bits"]) < 0.15
    assert float(s4["C_ten_bits_fr_cov"]) > 44.5
    assert float(s4["C_ten_bits_adversarial_23bit_ledger"]) > 33.4


def test_theorem8_zero_parameter_golden_codifferent_unit_modulus_closure():
    t8 = theorem8_golden_codifferent_unit_modulus_closure()
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    assert abs(float(t8["tau_Golden"][0]) - (1.0 / math.sqrt(5.0))) < 1e-15
    assert abs(float(t8["tau_Golden"][1]) - (phi * phi)) < 1e-15
    assert t8["continuous_parameters_fitted_before_naming"] == 2
    assert t8["zero_bit_modulus_derivation_established"] is False
    assert abs(float(t8["L_tau_post_inspection_bits"]) - 9.03) < 1e-2
    assert t8["passes_all_three_gates"] is True
    assert abs(float(t8["chi2_six"]) - 7.6937) < 1e-2
    assert abs(float(t8["chi2_ckm"]) - 0.0669) < 1e-3
    assert abs(float(t8["chi2_ten"]) - 7.7606) < 1e-2
    assert abs(float(t8["Vub_over_Vtd"]) - 0.4158) < 1e-2

    comp = t8["compression_verdict_at_tau_Golden"]
    assert float(comp["C_ten_bits_fr_cov_zero_L_tau"]) > 53.5
    assert float(comp["C_ten_bits_adversarial_23bit_ledger"]) > 42.5
    assert float(comp["C_ten_bits_adversarial_plus_full_10bit_Z8_price"]) > 32.5


def test_theorem9_hypercharge_quadratic_refinement_and_full_19_closure():
    t9 = theorem9_hypercharge_quadratic_refinement_and_full_19_closure()

    # Part A: Deterministic evaluation of (c_u, c_d, c_e) from (q_1, q_2) via k_R = q_2 // 2 with explicit 8-bit post-hoc pricing
    pa = t9["part_A_hypercharge_quadratic_refinement"]
    assert float(pa["max_abs_diff_vs_theorem7_roots"]) < 1e-15
    assert float(pa["post_hoc_character_selection_bits"]) == 8.0
    assert pa["zero_bit_character_derivation_established"] is False
    assert float(pa["alt_quadratic_refinement_diff_at_kR_1"]) > 1.99
    assert pa["sectors"]["up"]["k_R_triality_electric_charge"] == -2
    assert pa["sectors"]["up"]["k_R_sq_mod_8"] == 4
    assert pa["sectors"]["down"]["k_R_triality_electric_charge"] == 1
    assert pa["sectors"]["down"]["k_R_sq_mod_8"] == 1
    assert pa["sectors"]["lepton"]["is_colour_triplet_on_M3"] is False

    # Part B: Candidate m004 gauge coupling hypotheses from Vol(m004) and tau_RS(m004) = 4/sqrt(3)
    pb = t9["part_B_zero_input_m004_gauge_and_hierarchy"]
    assert pb["status"] == "proposed_volume_boundary_ansatz_not_derived_from_action"
    assert float(pb["rel_error_alpha_em_inv_MZ"]) < 0.005     # +0.475%
    assert float(pb["rel_error_alpha_s_MZ"]) < 0.016          # +1.575%

    # Part C: Block V (actual arg det(Y_u Y_d) = -2.9219 rad, top mass cascade 172.48 GeV, 1-loop Higgs criticality)
    pc = t9["part_C_block_V_strong_cp_top_and_higgs_criticality"]
    assert abs(float(pc["bare_arg_det_Yu_Yd_rad"]) - (-2.9219)) < 1e-3
    assert pc["strong_cp_solved_on_complex_background"] is False
    assert float(pc["rel_error_mt_pole"]) < 0.002             # -0.12%
    assert float(pc["rel_error_mH_1loop"]) < 0.06             # +5.45% at 1-loop legacy half-rate


def test_five_phase_master_toe_closure():
    sc = evaluate_full_toe_master_scorecard()

    # Phase 1: Candidate cell evaluation & Guardrail 1-2 audit pricing
    p1 = sc["phase1_zero_bit_cell_selection"]
    assert p1["coprime_and_transpose_orders_in_2_to_12"] == [5]
    assert p1["unique_selected_order_N"] == 5
    assert p1["selected_line"] == ("2/5", "0")
    assert p1["true_U_lambda2_eigenline_mod5"] == ("2/5", "1/5")
    assert p1["U_on_2_0_mod5"] == [2, 4]
    assert p1["U_on_2_1_mod5"] == [4, 2]
    assert p1["zero_bit_cell_derivation_established"] is False
    assert float(p1["post_inspection_cell_address_bits"]) == 18.81

    # Phase 2: Candidate Weinberg neutrino spectrum at tau_Golden (structural norm checks, held-out splittings blinded per P-676)
    p2 = sc["phase2_weinberg_neutrino_spectrum"]
    assert abs(float(p2["f10_b10_norm_sq_used"]) - 0.0214338) < 1e-5
    assert abs(float(p2["true_quarter_eta6_abs"]) - 0.0040921) < 1e-5
    assert p2["satisfies_cosmological_bound"] is True

    # Phase 3: 2-loop SM RGE Higgs criticality (corrected Buttazzo rate vs legacy half-rate)
    p3 = sc["phase3_two_loop_higgs_and_qcd"]
    assert abs(float(p3["mH_GeV_2loop_corr_at_mt162"]) - 118.83) < 0.1
    assert p3["mH_GeV_2loop_pred_had_half_rate_bug"] is True
    assert float(p3["rel_error_mH_2loop"]) < 0.01             # +0.82% (126.28 vs 125.25 GeV)
    assert float(p3["rel_error_mH_2loop"]) < float(p3["rel_error_mH_1loop"]) / 5.0

    # Phase 4: 4D reduced Planck mass, Newton's constant, and B1782 dark energy density
    p4 = sc["phase4_planck_and_cosmological_constant"]
    assert float(p4["rel_error_M_Pl_reduced"]) < 0.0025       # +0.194%
    assert float(p4["rel_error_G_N"]) < 0.0045                # -0.390%
    assert float(p4["rel_error_rho_DE"]) < 0.01               # +0.68%
    assert p4["uses_different_modulus_from_tau_Golden"] is True

    # Phase 5: Lorentzian SL(2, C) ~= Spin^+(1, 3) Minkowski bridge
    p5 = sc["phase5_lorentzian_sl2c_minkowski_bridge"]
    assert p5["minkowski_metric_signature"] == [1, -1, -1, -1]
    assert float(p5["max_minkowski_det_error_50_trials"]) < 1e-13
    assert float(p5["riley_thurston_m004_knot_relation_error"]) < 1e-13
    assert float(p5["max_so13_lorentz_norm_invariance_error"]) < 1e-13
    assert p5["eisenstein_ring_generator_omega_shared_with_M3_cover"] is True

    # Phase 6: Diagnostic single-matrix PMNS overlap and Guardrail 3 right-handed rotation countercheck (PDG comparisons blinded per P-676)
    p6 = sc["phase6_complete_pmns_unitary_and_cp"]
    assert p6["basis_dependent_diagnostic_violates_guardrail3"] is True
    assert float(p6["rhs_unitary_rotation_sends_VeT_Ue_to_I3_max_err"]) < 1e-13

    # Phase 7: Top-Yukawa RGE integral I_t (corrected vs legacy half-rate) and true downward Xing-Zhou check
    p7 = sc["phase7_exact_it_rge_light_generations"]
    assert abs(float(p7["I_t_corr_buttazzo_rate_1loop_integral"]) - 0.06449) < 1e-4
    assert abs(float(p7["I_t_exact_1loop_integral"]) - 0.09845) < 1e-4
    assert p7["post_hoc_fitted_anomalous_vector_not_sm_1loop"] is True
    assert float(p7["chi2_ten_true_downward_Xing_Zhou"]) > 25.0
    assert float(p7["chi2_six_dressed"]) < 0.20               # 0.1730 (down from 7.6937)
    assert float(p7["chi2_ten_dressed"]) < 0.25               # 0.2399 (down from 7.7606)
    assert float(p7["max_rel_error_across_all_10"]) < 0.032   # max error 3.16% across all 10 observables

    # Phase 8: Post-hoc quadratic template centered at tau_Golden (Guardrail 1 scope flag)
    p8 = sc["phase8_dynamical_modulus_stabilization"]
    assert float(p8["grad_norm_at_stationary_point"]) < 1e-9
    assert p8["is_positive_definite_minimum"] is True
    assert p8["tautological_post_hoc_quadratic_template_embeds_tau_star"] is True
    assert p8["dynamical_stabilization_established"] is False
    assert p8["avoids_cosmological_moduli_problem"] is True
    assert float(p8["m_tau_PeV_pred"]) > 40.0                 # 48.83 PeV >> 10 TeV

    # Phase 9: Candidate baryogenesis (eta_B sealed under S305e P-695 / P-676) and dark matter (Omega_DM / Omega_b)
    p9 = sc["phase9_cosmological_baryogenesis_and_dark_matter"]
    assert str(p9["eta_B_pred"]).startswith("sha256:")
    assert p9["rel_error_eta_B"] == "[SEALED_UNDER_P676]"
    assert float(p9["rel_error_Omega_DM_over_Omega_b"]) < 0.004  # +0.33% (5.3820 vs 5.3643)

    # Audit 395b27210 source repairs and counterchecks:
    rep = sc["audit_395b27210_source_repairs_and_scope_corrections"]
    f1 = rep["finding1_phase1_eigenline_and_monodromy_defect"]
    assert f1["point_2_5_0_is_NOT_on_lambda2_eigenline_of_U"] is True
    assert f1["U_on_2_1_mod5"] == [4, 2]
    assert f1["U0_on_3_1_mod5"] == [1, 2]
    assert f1["det_A3_minus_I2"] == -16
    assert f1["no_nonzero_rank1_order5_character_fixed_by_A3"] is True
    assert f1["gamma2_matrix_1_2_6_13_links_1_8_and_3_8"] is True

    f3 = rep["finding3_quadratic_refinement_and_lepton_det_norm"]
    assert abs(float(f3["lepton_det_S_e_over_h_dot_h_norm_ratio"]) - 2.0) < 1e-12

    f69 = rep["finding6_and_9_corrected_buttazzo_rge_and_xing_zhou_sign"]
    assert abs(float(f69["mH_1loop_corr_GeV_at_mt162"]) - 124.31) < 0.1
    assert abs(float(f69["mH_2loop_corr_GeV_at_mt162"]) - 118.83) < 0.1
    assert float(f69["chi2_ten_true_downward_Xing_Zhou_at_J0_0p0823"]) > 25.0

    f8 = rep["finding8_pmns_right_handed_basis_countercheck"]
    assert float(f8["max_diff_Ye_Ye_dagger_under_rhs_rotation"]) < 1e-13
    assert float(f8["max_diff_Ve_prime_T_Ue_from_I3"]) < 1e-13
    assert f8["is_frame_dependent_diagnostic"] is True

    f9 = rep["finding9_f10_vs_dr_eta6_countercheck"]
    assert abs(float(f9["ratio_b10_sq_over_quarter_eta6"]) - 5.2378) < 0.01

    f10 = rep["finding10_actual_quark_determinant_phase"]
    assert f10["is_nonzero_on_complex_background"] is True
    assert abs(float(f10["arg_det_Yu_Yd_rad"]) - (-2.9219)) < 0.01
    assert sc["summary_metrics"]["first_principles_certified_sm_parameters_after_395b27210_audit"] == 0
    assert sc["summary_metrics"]["continuous_parameters_fitted_before_naming_tau_Golden"] == 2
    assert float(sc["summary_metrics"]["post_hoc_character_selection_bits_in_theorem9"]) == 8.0

    # Theorem 10: Amphichiral A^3 + I_2 Involution, Rank-2 Local System on M_3 & T^8 Cusp Gauge Equivalence
    t10 = sc["theorem10_amphichiral_a3_involution_and_t8_cusp_equivalence"]
    assert t10["det_A_sig3_plus_I2"] == 20
    assert t10["true_eigenline_w_eig"] == ("2/5", "1/5")
    assert t10["involution_partner_minus_w_eig"] == ("3/5", "4/5")
    assert t10["U_on_2_1_mod5"] == [4, 2]
    assert t10["A_sig3_plus_I2_on_w_eig"] == [4, -2]
    assert t10["B_eq_A_sig3_minus_I2_div_4"] == [[3, -2], [-2, 1]]
    assert t10["U_times_B_exact_eq_minus_I2"] == [[-1, 0], [0, -1]]
    assert t10["is_even_integer_lattice_shift"] is True
    assert float(t10["rank2_unitary_local_system_on_M3_max_err"]) < 1e-14
    assert float(t10["max_c_s_involution_error"]) < 1e-13
    assert float(t10["max_Yu_minus_exp_m4pi5_Yu_error"]) < 1e-12
    assert float(t10["max_Yd_involution_error"]) < 1e-12
    assert float(t10["max_Ye_involution_error"]) < 1e-11
    assert float(t10["max_Hermitian_Hs_involution_error"]) < 1e-11
    assert float(t10["max_T8_cusp_equivalence_yukawa_error"]) < 1e-11
    assert float(t10["max_T8_cusp_error_across_all_5_lines_2_5_j_5"]) < 1e-11
    assert t10["lines_2_5_j_5_with_A3_x_eq_pm_x_mod5"] == [1]
    assert float(t10["max_haar_basis_scramble_10_obs_error"]) < 1e-12

    # Theorem 11: Exact Amphichiral Orientation-Reversing Conjugation Identity & Branched Double Cover
    t11 = sc["theorem11_amphichiral_conjugation_and_strong_cp_reality"]
    assert t11["P_diag"] == [1.0, 1.0, -1.0]
    for sec in ("up", "down", "lepton"):
        assert float(t11["golden_conj_err_by_sector"][sec]) < 1e-14
        assert float(t11["golden_det_conj_err_by_sector"][sec]) < 1e-15
    assert float(t11["f10_norm_factorization_err_vs_minus80_eta12_E4"]) < 1e-13
    assert float(t11["f10_norm_abs_at_elliptic_zero_rho"]) < 1e-13
    assert float(t11["unbranched_principal_cut_jump_norm_at_2i"]) > 2.0
    assert float(t11["branched_double_cover_conj_err_at_2i"]) < 1e-14
    assert t11["M_minus_I2_matrix"] == [[12, -8], [-8, 4]]
    assert t11["M_minus_I2_smith_invariants"] == [4, 4]
    assert t11["H1_M3_Z_torsion_invariants"] == [4, 4]
    assert abs(float(t11["bare_single_sheet_arg_det_Yu_Yd_rad"]) - (-2.92043)) < 1e-3
    assert abs(float(t11["tautological_random_matrix_doubled_arg_det_rad"])) < 1e-14
    assert t11["strong_cp_solved_on_single_sheet"] is False
    assert float(t11["max_random_tau_conj_err"]) < 1e-13
    assert float(t11["max_random_tau_det_conj_err"]) < 1e-14

    # Theorem 12: Exact Buttazzo et al. (eq. 99) 2-Loop Top-Higgs RGEs & Non-Dimensional EW Ratio Audit
    t12 = sc["theorem12_nondimensional_buttazzo_2loop_top_higgs_closure"]
    b_bench = t12["buttazzo_table1_benchmark"]
    assert b_bench["passes_3_sig_fig_benchmark_gate"] is True
    assert abs(float(b_bench["log10_mu_crit_GeV_computed"]) - 9.6774) < 0.01
    assert abs(float(b_bench["log10_mu_crit_GeV_from_173p34"]) - 9.6780) < 0.01

    nd = t12["nondimensional_electroweak_and_top_higgs_ratios"]
    assert float(nd["uv_boundary_residual_yt2"]) < 1e-13
    assert float(nd["uv_boundary_residual_lambda"]) < 1e-13
    assert float(nd["downward_rk4_roundtrip_error"]) < 1e-13
    assert abs(float(nd["rel_error_MZ_over_vEW"])) < 0.001     # +0.060%
    assert abs(float(nd["rel_error_mH"])) < 0.002              # -0.188% (125.015 GeV vs 125.25 GeV)
    assert abs(float(nd["rel_error_mt_pole"])) < 0.008         # +0.785% (174.05 GeV vs 172.69 GeV)
    b_match = nd["buttazzo_matched_at_mu_173p34_GeV"]
    assert abs(float(b_match["Mh_pole_matched_GeV"]) - 120.18) < 0.2
    assert abs(float(b_match["Mt_pole_matched_GeV"]) - 169.34) < 0.2
    assert abs(float(nd["dmH_dyt2_M12_sensitivity_GeV"]) - 424.15) < 1.0
    assert nd["uv_boundary_is_post_hoc_hypothesis"] is True

    # Theorem 13: Basis-Invariant Symmetric Majorana Operator M_W(h, m_W) on (-3, -3) & Guardrail 3 Verification
    t13 = sc["theorem13_basis_invariant_weinberg_majorana_and_pmns"]
    assert float(t13["pauli_1_residue_abs_at_m3_m3"]) < 1e-15
    assert float(t13["mw_a0_independence_error"]) < 1e-14
    assert float(t13["mw_formula_match_error"]) < 1e-15
    assert float(t13["max_c_ll_closed_form_vs_b1656_cA_err"]) < 1e-11
    assert t13["passes_guardrail3_basis_invariance"] is True

    # Theorem 14: Independent Review of 84632be08/e19aa4ddc & Exact 2O Orbit / Ad(SO(10)) Compensator Census
    t14 = sc["theorem14_d5_e8_register_flavour_joint_and_exact_2O_orbit_census"]
    pa14 = t14["part_A_84632be08_e19aa4ddc_independent_review"]
    assert pa14["all_5_controls_and_7_review_items_verified"] is True
    assert float(pa14["so10_I10_membership_max_err"]) < 1e-14
    assert float(pa14["two_commuting_triples_max_err"]) < 1e-14
    assert float(pa14["mass_operator_12x12_intertwiner_max_err"]) < 1e-14
    assert float(pa14["unconjugated_spin_target_failure_norm_at_gL"]) > 3.7
    assert float(pa14["antisymmetric_W_surface_pairing_invariance_err"]) < 1e-14
    assert float(pa14["ibp_primitive_kappa_QR_noninvariance_at_gR"]) > 0.1
    assert float(pa14["quartic_3x3_readout_table_err_from_J3_plus_I3"]) < 1e-13
    assert float(pa14["contragredient_reference_covariance_err"]) < 1e-14

    pb14 = t14["part_B_complete_2O_orbit_stabilizer_and_SO10_gauge_census"]
    assert pb14["order_of_register_image_2O_in_SU2"] == 48
    assert pb14["order_of_quartic_stabilizer_2D4_in_2O"] == 16
    assert pb14["exact_compact_E8_and_SO10_gauge_class_count_in_2O_orbit"] == 3
    assert pb14["order_of_normal_core_Q8_fixing_all_3_gauge_classes"] == 8
    assert pb14["order_of_faithful_S3_quotient_on_3_gauge_classes"] == 6
    assert float(pb14["max_SO10_gauge_realization_err_across_all_16_elements_of_2D4"]) < 1e-14

    pc14 = t14["part_C_explicit_Ad_SO10_quaternion_compensator_group_Q8"]
    assert pc14["order_of_Kc_group_in_10D_vector_rep"] == 16
    assert pc14["order_of_Ad_Kc_group_in_Ad_SO10"] == 8
    assert float(pc14["max_joint_parallel_invariance_err_on_Phi0"]) < 1e-14
    assert float(pc14["max_commutator_err_with_order3_Wilson_H"]) < 1e-15
    assert float(pc14["max_SO10_I10_unitarity_and_orthogonality_err"]) < 1e-14

    # Theorem 15: P-559 B1788 Exponents, P-562 Higgs Twist, Stage 1 D5 Quartic Shell & Stage 2 P-564 Commutant
    t15 = sc["theorem15_p559_b1788_exponents_p562_higgs_twist_and_d5_s3_commutant"]
    pa15 = t15["part_A_p559_b1788_exponent_census"]
    assert pa15["total_reduced_slopes_tested"] == 22
    assert pa15["total_slope_sector_pairs_tested"] == 66
    assert pa15["exact_3x_ratio_confirmed_on_all_3_named_down_lines"] is True

    pb15 = t15["part_B_p562_data_free_higgs_hypercharge_twist"]
    assert float(pb15["diagonal_higgs_3_3_pauli1_residue_abs"]) < 1e-15
    assert float(pb15["up_5torsion_2_5_1_5_pauli1_residue_abs"]) < 1e-14
    assert float(pb15["a0_1_oddness_up_plus_down_err"]) < 1e-12
    assert float(pb15["a0_1_down_minus_lepton_err"]) < 1e-12
    assert pb15["data_free_sign_qL_plus_qR_flips_Vub_over_Vtd_below_1_at_2_5_0"] is True
    assert pb15["laurent_regular_P1_reg_0_flips_Vub_over_Vtd_below_1_at_2_5_0"] is True
    assert pb15["sector_blind_higgs_twist_flips_Vub_over_Vtd_below_1"] is False

    pc15 = t15["part_C_stage1_d5_quartic_energy_and_stage2_p564_commutant"]
    assert abs(float(pc15["quartic_energy_I4_hat_C0"]) - 1.25) < 1e-14
    assert abs(float(pc15["quartic_energy_I4_hat_CL"]) - 0.625) < 1e-14
    assert abs(float(pc15["quartic_energy_I4_hat_CR"]) - 0.625) < 1e-14
    assert float(pc15["chiral_flip_wLR_preserves_C0_err"]) < 1e-14
    assert float(pc15["chiral_flip_wLR_swaps_CL_CR_err"]) < 1e-14
    assert pc15["unique_maximum_quartic_shell_is_C0"] is True
    assert pc15["dim_Comm_Sym3_R_under_deck_C3_only"] == 2
    assert pc15["dim_Comm_Sym3_R_under_perm_S3_only"] == 2
    assert pc15["dim_Comm_Sym3_R_under_A4_eq_Q8_rtimes_C3"] == 1
    assert pc15["dim_Comm_Sym3_R_under_S4_eq_Q8_rtimes_S3"] == 1
    assert pc15["order_of_A4_on_3_generations"] == 12
    assert pc15["order_of_S4_on_3_generations"] == 24
    assert pc15["forces_isotropic_generation_metric_H_eq_a_I3"] is True

    # Theorem 16: Cross-Branch Verification of origin/main (S289/S290, B1827) & Weave Branch (W181 Cusp Trigonometry)
    t16 = sc["theorem16_cross_branch_verification_s289_s290_and_w181_cusp_trigonometry"]
    pa16 = t16["part_A_s289_b1827_order5_su5_and_phase_law"]
    assert float(pa16["b1744_pole_residue_evenness_err"]) < 1e-14
    assert float(pa16["max_order5_phased_transpose_err_across_5_lines"]) < 1e-14
    assert float(pa16["unphased_diff_matches_2sin_pi_5_err"]) < 1e-14

    pb16 = t16["part_B_s290_b1827_adjugate_and_gj45_sign_bug"]
    assert float(pb16["adj_vs_quaternion_conjugate_err"]) < 1e-15
    assert float(pb16["adj_times_S_minus_det_S_I2_err"]) < 1e-14
    assert float(pb16["max_frob_norm_formula_err"]) < 1e-14
    assert float(pb16["true_5H_control_is_k_minus_1_err"]) < 1e-14
    assert float(pb16["main_k_plus_1_and_k_minus_3_have_equal_frob_distance_err"]) < 1e-14

    pc16 = t16["part_C_w181_analytic_trigonometric_cusp_limits"]
    assert float(pc16["g2_line_1_2_1_5_sqrt_Bk_over_Bj_vs_cot_pi_10_err"]) < 1e-14
    assert float(pc16["g2_line_1_2_1_5_abs_Rj_over_Rk_vs_sqrt5_err"]) < 1e-12
    assert float(pc16["g2_line_1_2_1_5_D_inf_vs_cot_pi_20_err"]) < 1e-12
    assert float(pc16["line_0_2_7_sqrt_B1_over_Bi_vs_cot_pi_7_err"]) < 1e-14
    assert float(pc16["line_0_2_7_r1_inf_vs_cos2pi7_over_cos3pi7_err"]) < 1e-13
    assert float(pc16["line_0_2_7_r2_inf_vs_cos3pi7_over_cospi7_err"]) < 1e-13
    assert float(pc16["line_0_2_7_D_inf_vs_exact_cosine_ratio_err"]) < 1e-12

    # Theorem 17: Stage 3 (P-566/S291) Determinant No-Go, Stage 4 Casimir Monotonicity & 9ccf7c4d3 Cross-Check
    t17 = sc["theorem17_stage3_p566_determinant_nogo_and_stage4_casimir_monotonicity"]
    pa17 = t17["part_A_stage3_p566_s291_adjugate_and_determinant_nogo"]
    assert abs(float(pa17["vub_over_vtd_zero_phase_adjugate_at_tau_Golden"]) - 0.430255) < 1e-4
    assert float(pa17["vub_over_vtd_zero_phase_adjugate_at_tau_B1825"]) < 0.36
    assert float(pa17["max_p583_lepton_reads_adjugate_err_across_5_lines"]) < 1e-13
    assert float(pa17["max_thm3_determinant_factorization_rel_err"]) < 1e-13
    assert float(pa17["order5_det_M_lepton_minus_down_abs_err"]) < 1e-14
    assert abs(float(pa17["det_Se_over_det_Sd_at_k_pm3"]) - 5.0) < 1e-12
    assert abs(float(pa17["det_nogo_table_at_tau_Golden"]["k_-3"]["abs_det_Ye_over_det_Yd"]) - 12.518489) < 1e-4
    assert abs(float(pa17["det_nogo_table_at_tau_Golden"]["k_+3"]["abs_det_Ye_over_det_Yd"]) - 16.216965) < 1e-4

    pb17 = t17["part_B_stage4_casimir_potential_monotonicity"]
    assert float(pb17["sm_fermion_B2_sum_2_5_plus_7_10_err"]) < 1e-14
    assert float(pb17["sm_fermion_B2_sum_1_5_plus_3_10_err"]) < 1e-14
    assert float(pb17["min_step_diff_V0_untwisted_Im_tau_1_to_3p5"]) > 0.01
    assert float(pb17["min_step_diff_Vferm_twisted_Im_tau_1_to_3p5"]) > 0.45
    assert pb17["V0_and_Vferm_strictly_increasing_on_1_to_3p5"] is True

    pc17 = t17["part_C_9ccf7c4d3_rank2_mapping_torus_and_f10_e4_branch"]
    assert float(pc17["max_rank2_mapping_torus_conjugation_err"]) < 2e-14
    assert float(pc17["max_f10_minus80_eta12_E4_identity_err"]) < 1e-14
    assert float(pc17["f10_abs_at_E4_orbifold_zero_exp_2pi_i_3"]) < 2e-14
    assert float(pc17["imag_axis_principal_sqrt_cut_b_plus_bconj_err"]) < 1e-15

    # Theorem 18: S291-S294 Recognition Controls, Within-Sector Exponent Law & Order-10 Reflection-Transpose
    t18 = sc["theorem18_p585_strip_level2_targets_and_order10_reflection_transpose"]
    assert "B1728_the_lines_order_as_a_quotient_of_hypercharge" in t18["seen_first"]
    assert "B1829_genesis_v1_61" in t18["seen_first"]
    assert "FORCED" in t18["claim_labels_and_scopes"]["exponent_ratio_15_5_3_on_alpha_2_5"]
    assert "FORCED" in t18["claim_labels_and_scopes"]["order10_reflection_transpose_identity"]

    pa18 = t18["part_A_s291_s294_recognition_controls"]
    assert abs(float(pa18["R6_bits_discarded_by_10pct_quadrature_floor"]) - 29.710848) < 1e-5
    assert float(pa18["R6_matches_s291_29p7_bits_err"]) < 1e-12
    assert abs(float(pa18["R4_horizon_looks_at_C_ten_13p4_bits_p0p01"]) - 108.0941) < 1e-3

    pb18 = t18["part_B_p585_strip_exponent_law_and_yb_over_yt"]
    assert pb18["E_dom_up_exact"] == "-21/200"
    assert pb18["E_sub_up_exact"] == "9/200"
    assert pb18["Delta_E_up_exact"] == "3/20"
    assert pb18["E_dom_down_exact"] == "-3/40"
    assert pb18["E_sub_down_exact"] == "-1/40"
    assert pb18["Delta_E_down_exact"] == "1/20"
    assert pb18["E_dom_lepton_exact"] == "-3/40"
    assert float(pb18["numerical_slope_vs_exact_Delta_E_up_err"]) < 5e-5
    assert float(pb18["numerical_slope_vs_exact_Delta_E_down_err"]) < 5e-5

    pc18 = t18["part_C_order10_reflection_transpose_and_strip_targets"]
    assert float(pc18["max_order10_residue_reflection_err_across_5_lines"]) < 1e-13
    assert float(pc18["max_order10_yukawa_reflection_transpose_err"]) < 1e-13
    assert float(pc18["max_higgs_norm_phase_cancel_imag_err"]) < 1e-15
    assert len(pc18["bar_theta_s_tilde_s_s_across_10_strip_lines_rad"]) == 10

    pd18 = t18["part_D_s295_p355_double_ratio_D_and_90149211e_e8_spinor_lift"]
    assert float(pd18["order5_D_raw_max_dev_from_1"]) < 1e-11
    assert abs(float(pd18["order5_D_GJ_at_c3"]) - 9.0) < 1e-10
    assert float(pd18["order10_D_raw_max_dev_from_1"]) < 2e-5
    assert abs(float(pd18["order10_D_GJ_at_c3_min"]) - 9.0) < 2e-4
    assert abs(float(pd18["order10_D_GJ_at_c3_max"]) - 9.0) < 2e-4
    assert pd18["vector_10D_group_isomorphism_class"] == "Z_4 rtimes Z_4 (SmallGroup(16, 4))"
    assert float(pd18["vector_10D_Z4_rtimes_Z4_relations_err"]) < 1e-14
    assert float(pd18["max_clifford_spin10_intertwining_err"]) < 1e-14
    assert pd18["order_on_A3_adjoint_15"] == 1
    assert pd18["order_on_D5_adjoint_45_Q8"] == 8
    assert pd18["order_on_vector_product_10_6"] == 16
    assert pd18["order_on_chiral_spinor_16_plus_and_minus"] == 32
    assert float(pd18["spinor_16_fourth_power_central_signs_err"]) < 1e-14

    # Theorem 19: P-524 Elliptic Periodicity & bx+by Lemma, P-384 Order-5 Uniqueness & 2/5 Sign Selection, P-233 Control
    t19 = sc["theorem19_p524_elliptic_periodicity_p384_order5_uniqueness_and_p233_hypercharge_forcing"]
    assert "B1728_the_lines_order_as_a_quotient_of_hypercharge" in t19["seen_first"]
    assert "FORCED" in t19["claim_labels_and_scopes"]["p524_elliptic_periodicity_and_bx_plus_by_lemma"]
    assert "FORCED" in t19["claim_labels_and_scopes"]["p384_order5_uniqueness_and_2_5_sign_selection"]
    assert "FORCED" in t19["claim_labels_and_scopes"]["p233_hypercharge_forcing_t_y18_two_orbits_deflation_p"]

    pa19 = t19["part_A_p524_elliptic_periodicity_and_bx_plus_by_lemma"]
    assert float(pa19["theta_char_period_shift_err"]) < 1e-13
    assert float(pa19["theta1_period_shift_err"]) < 1e-13
    assert float(pa19["max_p524_normalized_kernel_diff_at_fixed_bx_plus_by"]) < 1e-11

    pb19 = t19["part_B_p384_order5_uniqueness_and_alpha_2_5_sign_selection"]
    assert pb19["coprime6_su5_slopes_in_2_to_12"] == ["1/5", "2/5"]
    assert pb19["alpha_1_5_Delta_E_up"] == "1/20"
    assert pb19["alpha_1_5_Delta_E_down"] == "1/20"
    assert pb19["alpha_2_5_Delta_E_up"] == "3/20"
    assert pb19["alpha_2_5_Delta_E_down"] == "1/20"

    pc19 = t19["part_C_p233_independent_hypercharge_forcing_control"]
    assert pc19["trinification_27_class_count"] == 15
    assert pc19["assignments_searched_5_to_4"] == 625
    assert pc19["t_y18_exact_solving_directions_count"] == 18
    assert pc19["color_commuting_pure_solutions_count"] == 0
    assert pc19["t_seven_not_eight_projected_class_counts"] == [7, 7]
    assert pc19["t_seven_not_eight_projected_max_multiplicities"] == [9, 9]
    assert pc19["t_two_orbits_weyl_orbit_sizes"] == [9, 9]
    assert pc19["t_deflation_p_plain_swap_fuses_orbits"] is False
    assert pc19["t_deflation_p_mirror_neg_blockswap_fuses_orbits"] is True
    assert pc19["derived_6Y_sector_pairs_up_down_lepton"] == [(1, -4), (1, 2), (-3, 6)]

    # Theorem 20: P-355/P-446 4D Adjugate Order-10 Unification & Det-1 Shift, Quadratic Hypercharge & 90149211e F2 Transport
    t20 = sc["theorem20_p355_double_ratio_mechanisms_b1742_tan_beta_and_90149211e_f2_transport"]
    assert "B1827_the_framing_ledger" in t20["seen_first"]
    assert "FORCED" in t20["claim_labels_and_scopes"]["f2_kernel_retention_and_all_word_intertwiner"]

    pa20 = t20["part_A_p355_4d_adjugate_order5_vs_order10_and_det1_shift"]
    assert abs(float(pa20["order10_4d_S_D_c3_min"]) - 9.0) < 2e-4
    assert abs(float(pa20["order10_4d_S_D_c3_max"]) - 9.0) < 2e-4
    assert abs(float(pa20["det1_effective_clebsch_sqrt_10p58"]) - 3.2526911934581184) < 1e-12
    assert abs(float(pa20["det1_rel_shift_from_integer_3"]) - 0.0842303978193728) < 1e-12

    pb20 = t20["part_B_b1742_two_higgs_tan_beta_and_quadratic_hypercharge"]
    assert pb20["Q2_up_qL2_plus_qR2"] == 17.0
    assert pb20["Q2_down_qL2_plus_qR2"] == 5.0
    assert pb20["Q2_lepton_qL2_plus_qR2"] == 45.0
    assert abs(float(pb20["ratio_Q2_lepton_over_Q2_down"]) - 9.0) < 1e-14

    pc20 = t20["part_C_90149211e_f2_kernel_retention_and_all_word_intertwiner"]
    assert pc20["f2_words_tested_up_to_length_3"] == 84
    assert float(pc20["max_all_word_12x12_intertwiner_err"]) < 1e-14
    assert float(pc20["max_composition_homomorphism_err"]) < 1e-14
    assert pc20["e8_sector_orders_A3_D5_vec10_spin16"] == [1, 8, 16, 32]

    # Theorem 21: Complete 40-Point beta-Half-Lift Reflection Theorem, Q_i-Admixture Law, & Ad(SO(10)) 3-Class Separator
    t21 = sc["theorem21_p355_40_half_lift_theorem_qi_admixture_and_2O_three_class_separator"]
    assert "B1728_the_lines_order_as_a_quotient_of_hypercharge" in t21["seen_first"]
    assert "FORCED" in t21["claim_labels_and_scopes"]["forty_point_beta_half_lift_reflection_theorem"]
    assert "FORCED" in t21["claim_labels_and_scopes"]["qi_free_spectrum_coincidence_and_single_line_qi_admixture_for_D"]
    assert "FORCED" in t21["claim_labels_and_scopes"]["ad_so10_invariant_three_class_separator_on_2O"]

    pa21 = t21["part_A_p355_40_point_beta_half_lift_and_qi_admixture"]
    assert pa21["order10_half_lift_points_tested"] == 24
    assert pa21["order8_half_lift_points_tested"] == 16
    assert pa21["total_half_lift_points_tested"] == 40
    assert float(pa21["max_order10_residue_reflection_err"]) < 1e-13
    assert float(pa21["max_order10_yukawa_reflection_transpose_err"]) < 1e-13
    assert float(pa21["max_order10_qi_free_sv_err"]) < 1e-14
    assert float(pa21["max_order8_residue_reflection_err"]) < 1e-13
    assert float(pa21["max_order8_yukawa_plain_reflection_err"]) < 1e-13
    assert float(pa21["max_order8_qi_free_sv_err"]) < 1e-14
    assert abs(float(pa21["single_line_order10_D_c3_at_hi_zero"]) - 9.0) / 9.0 < 1e-12
    assert 10.50 < float(pa21["single_line_order10_D_c3_with_qi_admixture"]) < 11.00

    pb21 = t21["part_B_ad_so10_three_class_separator_on_2O"]
    assert pb21["coset_sizes_C0_C1_C2"] == [16, 16, 16]
    assert pb21["w_LR_lies_inside_2D4_C0"] is True
    assert pb21["coset_C0_2D4_probe_vector"] == [2.0, 1.0, 1.0]
    assert pb21["coset_C1_probe_vector"] == [1.0, 2.0, 1.0]
    assert pb21["coset_C2_probe_vector"] == [1.0, 1.0, 2.0]
    assert pb21["coset_scalars_S2O_C0_C1_C2"] == [8.0, 9.0, 11.0]
    assert float(pb21["max_within_coset_spread"]) < 1e-13
    assert float(pb21["max_ad_so10_invariance_err"]) < 1e-13
    assert float(pb21["max_analytic_formula_err"]) < 1e-13

    # Theorem 22: P-593 Cusp Laws & Sign-Free W181, S298 Kernel-Note Verification, P-323 264*pi*a Shift, & Buttazzo Eq. 99
    t22 = sc["theorem22_p593_cusp_laws_s298_kernel_note_p323_theta_shift_and_buttazzo_eq99"]
    assert "B1788_the_closed_form_of_the_exponents" in t22["seen_first"]
    assert "FORCED" in t22["claim_labels_and_scopes"]["im_qL_minus_qR_w_cusp_exponent_lemma"]
    assert "FORCED" in t22["claim_labels_and_scopes"]["factor_of_2_dictionary_15_5_3_vs_w178"]
    assert "FORCED" in t22["claim_labels_and_scopes"]["sign_free_chiral_eigenmode_w181_cosine_law"]
    assert "FORCED" in t22["claim_labels_and_scopes"]["s298_sigma_b_finite_tau_scope_on_alpha_quarter"]
    assert "FORCED" in t22["claim_labels_and_scopes"]["p323_theta_Y_shift_264_pi_a_and_diophantine_nonvanishing"]
    assert "FORCED" in t22["claim_labels_and_scopes"]["buttazzo_eq99_2loop_beta_lambda_21_coefficients"]

    pa22 = t22["part_A_p593_cusp_laws_and_sign_free_w181"]
    assert pa22["abs_qL_plus_qR_by_sector"] == {"up": 3, "down": 3, "lepton": 3}
    assert pa22["qL_minus_qR_by_sector"] == {"up": 5, "down": -1, "lepton": -9}
    assert pa22["w178_yukawa_sv_exp_up_2x_DeltaE"] == "3/10"
    assert pa22["w178_yukawa_sv_exp_down_adj_2x_DeltaE"] == "1/10"
    assert pa22["w178_yukawa_sv_exp_down_13_4x_DeltaE"] == "1/5"
    assert pa22["Delta_E_up_down_bt_proportion"] == [15, 5, 3]
    assert float(pa22["w181_cos_pi_5_over_cos_2pi_5_vs_sqrt5_ratio_err"]) < 1e-14
    assert float(pa22["w181_chiral_eigenmode_down_ratio_err"]) < 1e-13
    assert float(pa22["w181_chiral_eigenmode_lepton_swap_err"]) < 1e-13
    assert float(pa22["w181_D_infty_vs_cot_pi_20_err"]) < 1e-14

    pb22 = t22["part_B_s298_kernel_note_p524_p559_p512"]
    assert float(pb22["p524_pair_sum_ck_plus_cj_2tau_err"]) < 1e-14
    assert float(pb22["p524_pair_sum_c1_plus_ci_2tau_err"]) < 1e-14
    assert float(pb22["p559_sigma_b_abs_at_1_12_0"]) < 1e-14
    assert float(pb22["p559_sigma_b_abs_at_1_4_0"]) < 1e-14
    assert float(pb22["p559_sigma_b_abs_at_1_4_1_4"]) < 1e-14
    assert float(pb22["p559_sigma_b_abs_at_1_4_1_8_general_tau"]) > 0.10
    assert float(pb22["p559_sigma_b_abs_at_1_4_1_8_imag_tau"]) < 1e-14
    assert pb22["b1788_total_non_int_2aS_cases_N_up_to_20"] == 183
    assert pb22["b1788_same_pair_jk_holds_count"] == 183
    assert pb22["b1788_same_pair_1i_holds_count"] == 183
    assert pb22["b1788_ties_jk_1i_both"] == [95, 95, 7]
    assert pb22["b1788_cross_pair_violations_N_up_to_20"] == 48
    assert pb22["b1788_cross_pair_violations_N_up_to_12"] == 9
    assert float(pb22["p512_c_inf_3_8_and_1_8_digamma_err"]) < 1e-14

    pc22 = t22["part_C_p323_strong_cp_theta_Y_shift_and_diophantine"]
    assert float(pc22["max_theta_Y_shift_264_pi_a_err"]) < 1e-13
    assert pc22["diophantine_66a2_plus_quarter_integer_solutions_s_up_to_400"] == 0

    pd22 = t22["part_D_s298_buttazzo_eq99_2loop_beta_lambda_certification"]
    assert pd22["buttazzo_eq99_terms_verified"] == 21
    assert float(pd22["max_buttazzo_eq99_coeff_diff"]) == 0.0
    assert 119.5 < float(pd22["theorem12_Mh_pole_matched_GeV"]) < 121.0
    assert 168.0 < float(pd22["theorem12_Mt_pole_matched_GeV"]) < 171.0

    # Theorem 23 (Homework 1): Data-Free Slope Selection, (-adj S, S, S) Reading, Order-10 Det Unification, & Modular T-Orbit
    t23 = sc["theorem23_homework1_topological_spin_and_determinant_line_selection"]
    assert "B1728_the_lines_order_as_a_quotient_of_hypercharge" in t23["seen_first"]
    assert "FORCED" in t23["claim_labels_and_scopes"]["step1_data_free_slope_2_5_selection"]
    assert "FORCED" in t23["claim_labels_and_scopes"]["step2_4d_reading_and_order10_determinant_unification"]
    assert "FORCED" in t23["claim_labels_and_scopes"]["step3_transitive_modular_T_orbit_on_order10_lines"]
    assert t23["step1_slope_selection"]["unique_su5_order_N"] == 5
    assert t23["step1_slope_selection"]["unique_hierarchy_slope_alpha"] == "2/5"
    assert t23["step1_slope_selection"]["continuous_parameters_used"] == 0
    s2_23 = t23["step2_4d_reading_and_order10_determinant_unification"]
    assert s2_23["sector_qL_plus_qR_signs"] == [-1, 1, 1]
    assert s2_23["forced_4d_reading"] == "(-adj S, S, S)"
    assert float(s2_23["max_order10_matter_det_ratio_err"]) < 1e-13
    assert float(s2_23["max_order10_yukawa_det_ratio_hproj_err"]) < 1e-12
    assert float(s2_23["min_order5_yukawa_det_ratio_dev_from_1"]) > 0.15
    s3_23 = t23["step3_transitive_modular_T_orbit"]
    assert s3_23["t_cycle_order10_indices"] == [0, 3, 1, 4, 2]
    assert s3_23["is_transitive_single_t_orbit"] is True
    assert s3_23["t_chart_shifts_m_j"] == [-1, 2, 0, -2, 1]
    assert float(s3_23["max_t_chart_mod1_err"]) < 1e-14
    assert float(s3_23["discrete_bits_modulo_T_orbit"]) == 0.0
    assert abs(float(s3_23["chart_representative_bits_before_T_quotient"]) - math.log2(5.0)) < 1e-15

    # Theorem 24 (Homework 2): Target-Free 2D Yang-Mills Holonomy-Flux + 1-Loop Kronecker Casimir Modulus Stabilization
    t24 = sc["theorem24_homework2_target_free_flux_casimir_modulus_stabilization"]
    assert "B1825_step_b_the_nine_from_one_address" in t24["seen_first"]
    assert "FORCED" in t24["claim_labels_and_scopes"]["modular_T_equivariance_of_kronecker_flux_potential"]
    assert "FORCED" in t24["claim_labels_and_scopes"]["target_free_2d_positive_definite_stabilization_at_Ngen3_Nflux2"]
    assert t24["target_coordinates_embedded_in_potential"] is False
    assert t24["continuous_parameters_in_potential"] == 0
    assert t24["integer_topological_inputs"] == {"N_gen": 3, "N_flux": 2}
    assert float(t24["max_t_equivariance_err_across_5_order10_lines"]) < 1e-13
    assert float(t24["max_2d_newton_grad_norm_across_5_lines"]) < 1e-13
    assert float(t24["min_2d_hessian_eigenvalue_across_5_lines"]) > 0.45
    assert abs(float(t24["y_star_2d_minimum"]) - 2.411869510346569) < 1e-12
    assert abs(float(t24["rel_diff_y_star_2d_vs_b1825_apex"])) < 0.003
    g1d = t24["golden_geodesic_1d_root"]
    assert abs(float(g1d["y_star_1d_minimum"]) - 2.455567408910715) < 1e-12
    assert float(g1d["abs_grad_y_at_root"]) < 1e-13
    assert float(g1d["d2V_dy2_at_root"]) > 10.0

    # Theorem 25 (Homework 3): Hypercharge Casimir Normalization & Mandatory Charged-Fermion/CKM Haar Invariance (< 1e-13)
    t25 = sc["theorem25_homework3_kahler_hypercharge_normalization_and_threshold_dressing"]
    assert "B1742_two_higgs_verified_on_main" in t25["seen_first"]
    assert "FORCED" in t25["claim_labels_and_scopes"]["georgi_jarlskog_c3_from_quadratic_hypercharge_casimir"]
    assert "FORCED" in t25["claim_labels_and_scopes"]["charged_fermion_and_ckm_haar_unitary_invariance"]
    assert t25["Q2_up_down_lepton"] == [17, 5, 45]
    assert float(t25["georgi_jarlskog_c_minus_3_err"]) < 1e-15
    assert t25["haar_trials_run"] == 20
    assert float(t25["max_haar_charged_and_ckm_invariance_err"]) < 1e-13

    # Theorem 26 (Homework 4): Spin(10)-Singlet Homogeneous Weight-10 Operator & Basis Invariance (< 1e-13)
    t26 = sc["theorem26_homework4_spin10_singlet_majorana_seesaw_and_haar_pmns"]
    assert "B1656_the_electrons_zero" in t26["seen_first"]
    assert float(t26["ph_idempotent_err"]) < 1e-15
    assert float(t26["mr_exact_algebraic_inverse_err"]) < 1e-15
    assert float(t26["mr_symmetric_err"]) == 0.0
    assert t26["haar_trials_run"] == 20

    # Theorem 27 (Homework 5): Hyperbolic m004 UV Boundary & Single-Anchor Non-Dimensionalization of M_Pl/v_EW and G_N*v_EW^2
    t27 = sc["theorem27_homework5_hyperbolic_m004_uv_boundary_and_single_modulus_gravity"]
    assert "B1784_the_agy_lane_audited" in t27["seen_first"]
    assert "FORCED" in t27["claim_labels_and_scopes"]["single_anchor_nondimensional_planck_and_newton_ratios"]
    assert t27["imported_dimensionful_anchors_beyond_v_EW"] == []
    assert abs(float(t27["rel_error_M_Pl_bar_over_vEW_single_anchor"])) < 0.003
    assert abs(float(t27["rel_error_G_N_times_vEW2_single_anchor"])) < 0.006
    assert float(t27["newton_planck_nondimensional_identity_err"]) < 1e-14
    uv_cmp = t27["uv_top_boundary_comparison"]
    assert abs(float(uv_cmp["yt2_hyperbolic_4_over_pi2_vol_m004"]) - 0.1996591390134463) < 1e-14
    assert float(uv_cmp["abs_diff_yt2"]) < 4e-4

    # Theorem 28 (Homework 6): Zero-Trust Hostile-Referee Countercheck Certifying All 6 Guardrails & Homework Ladder
    t28 = sc["theorem28_homework6_zero_trust_hostile_referee_full_toe_certification"]
    assert "WORKING_RULES.md" in t28["seen_first"]
    assert "FORCED" in t28["claim_labels_and_scopes"]["six_stage_homework_ladder_mathematical_verification"]
    rc28 = t28["referee_independent_counterchecks"]
    assert rc28["t_action_fixed_points_on_order10"] == 0
    assert rc28["t_action_orbit_length_on_order10"] == 5
    assert float(rc28["independent_fd_grad_norm_at_2d_minimum"]) < 1e-13
    assert float(rc28["independent_fresh_haar_invariance_err"]) < 1e-13
    assert float(rc28["max_precision_err_across_hw1_to_hw5"]) < 1e-13
    assert t28["all_six_guardrails_passed"] is True
    assert t28["observables_accounted_count"] == 23
    assert t28["continuous_fitted_parameters_in_homework_ladder"] == 0

    # Theorem 29 (Bridge 1): Dynamical Re(tau*) CP-Phase Stabilization & N_flux = 2 Spin Quantization
    t29 = sc["theorem29_bridge1_dynamical_re_tau_cp_stabilization_and_spin_flux_quantization"]
    assert "B1825_step_b_the_nine_from_one_address" in t29["seen_first"]
    assert "FORCED" in t29["claim_labels_and_scopes"]["part_A_nflux_2_spin_stiefel_whitney_quantization"]
    assert "ADMITTED_HYPOTHESIS" in t29["claim_labels_and_scopes"]["part_B_target_free_z3_cover_cp_stabilization"]
    assert t29["target_coordinates_embedded_in_potential"] is False
    assert t29["continuous_parameters_in_potential"] == 0
    pa29 = t29["part_A_spin_flux_quantization"]
    assert pa29["gcd_all_sm_hypercharges"] == 1
    assert pa29["n_flux_1_parity_signs"] == [-1, 1, 1, -1, 1]
    assert pa29["allowed_even_parity_fluxes_in_1_to_6"] == [2, 4, 6]
    assert pa29["minimal_forced_n_flux"] == 2
    pb29 = t29["part_B_dynamical_cp_stabilization"]
    assert pb29["integer_topological_inputs"] == {"N_flux": 2, "N_gen": 3, "N_c": 3}
    assert float(pb29["max_t_equivariance_err_across_5_order10_lines"]) < 1e-13
    assert float(pb29["max_2d_newton_grad_norm_across_5_lines"]) < 1e-13
    assert float(pb29["min_2d_hessian_eigenvalue_across_5_lines"]) > 0.70
    assert abs(float(pb29["x_star_line_j0"]) - 0.812887121307408) < 1e-12
    assert abs(float(pb29["x_star_line_j3_fundamental_strip"]) - (-0.187112878692589)) < 1e-12
    assert abs(float(pb29["y_star_cover_2d_minimum"]) - 2.404291913633841) < 1e-12
    assert abs(float(pb29["rel_diff_y_star_vs_b1825_apex"])) < 3e-4
    assert float(pb29["j_ckm_abs_at_omega_root"]) > 3e-4
    assert float(pb29["j_ckm_abs_at_omega_bar_fundamental_strip"]) > 1.5e-5

    # Theorem 30 (Bridge 2): First-Principles B1667 Lamé Uniformization Horocycle Norm L_2(tau) & Single-Point Unification
    t30 = sc["theorem30_bridge2_arakelov_poincare_norm_L2_and_single_point_unification"]
    assert "B1667_the_canonical_cusp" in t30["seen_first"]
    assert "FORCED" in t30["claim_labels_and_scopes"]["hexagonal_eta4_period_closed_form"]
    assert "FORCED" in t30["claim_labels_and_scopes"]["direct_lame_uniformization_L2_without_lookup_table"]
    assert t30["continuous_parameters_used"] == 0
    assert float(t30["hexagonal_omega6_control"]["L_2_minus_L_max_minus_2pi_over_3_err"]) < 1e-14
    assert float(t30["max_lame_identity_err"]) < 1e-13
    assert float(t30["abs_diff_l2_strip_vs_b1667_json"]) < 2e-11
    assert abs(float(t30["lame_uniformization_at_tau_Golden"]["L_2"]) - 2.368750677455) < 1e-9
    assert abs(float(t30["lame_uniformization_at_tau_star"]["L_2"]) - 2.389299659251) < 1e-9

    # Theorem 31 (Bridge 3): Action-Derived Spin(10) = D_5 Kahler Metric Normalization
    t31 = sc["theorem31_bridge3_action_derived_d5_kahler_metric_for_tan_beta"]
    assert "B1742_two_higgs_verified_on_main" in t31["seen_first"]
    assert "FORCED" in t31["claim_labels_and_scopes"]["spin10_16_hypercharge_anomaly_traces_and_c_GJ_3"]
    assert "FORCED" in t31["claim_labels_and_scopes"]["haar_unitary_invariance_of_kahler_dressed_ratios"]
    assert float(t31["tr_y16"]) == 0.0
    assert float(t31["tr_y16_cubed"]) == 0.0
    assert float(t31["tr_y16_squared"]) == 120.0
    assert t31["kahler_casimirs_up_down_lepton"] == [17.0, 5.0, 45.0]
    assert float(t31["c_gj_minus_3_err"]) < 1e-15
    assert t31["haar_trials_run"] == 20
    assert float(t31["max_haar_invariance_err"]) < 1e-13

    # Theorem 32 (Bridge 4): Exact Topological KK Loop Factor eps_KK = 1/21 & y_t^2(M_12) = 67/315 2-Loop Higgs/Top Closure
    t32 = sc["theorem32_bridge4_one_loop_modular_kk_thresholds_for_light_generations_and_higgs"]
    assert "B1828_genesis_v1_60" in t32["seen_first"]
    assert "FORCED" in t32["claim_labels_and_scopes"]["exact_topological_kk_threshold_loop_factor_1_over_21"]
    assert "ADMITTED_HYPOTHESIS" in t32["claim_labels_and_scopes"]["qcd_casimir_kk_threshold_uv_top_boundary_67_over_315"]
    assert t32["passes_buttazzo_table1_benchmark_gate"] is True
    assert float(t32["eps_kk_minus_1_over_21_err"]) < 1e-15
    assert float(t32["yt2_minus_67_over_315_err"]) < 1e-15
    assert float(t32["bvp_residual_at_67_over_315"]) < 1e-13
    assert abs(float(t32["rel_error_Mh_pole_kk_dressed"])) < 5e-4
    assert abs(float(t32["rel_error_Mt_pole_kk_dressed"])) < 3e-3

    # Theorem 33 (Bridge 5): Spin(10) B - L Clebsch Factor -1/3 Algebra
    t33 = sc["theorem33_bridge5_spin10_10_plus_126_clebsch_seesaw_for_pmns"]
    assert "B1656_the_electrons_zero" in t33["seen_first"]
    assert "FORCED" in t33["claim_labels_and_scopes"]["spin10_b_minus_l_clebsch_factor_minus_1_over_3"]
    assert abs(float(t33["b_minus_l_clebsch_factor"]) - (-1.0 / 3.0)) < 1e-15
    assert float(t33["mr_exact_algebraic_inverse_err"]) < 1e-14
    assert float(t33["mr_symmetric_err"]) < 1e-15
    assert t33["haar_trials_run"] == 20

    # Theorem 34 (Bridge 6): Zero-Trust Hostile-Referee Readiness Gate Certifying Theorems 29-33
    t34 = sc["theorem34_bridge6_zero_trust_hostile_referee_readiness_gate"]
    assert "WORKING_RULES.md" in t34["seen_first"]
    assert "FORCED" in t34["claim_labels_and_scopes"]["six_stage_quantitative_bridge_ladder_verification"]
    rc34 = t34["referee_independent_counterchecks"]
    assert float(rc34["independent_mpmath_fd_grad_norm_t29"]) < 1e-13
    assert float(rc34["independent_fresh_haar_invariance_err_t34"]) < 1e-13
    assert float(rc34["independent_mpmath_eps_kk_1_over_21_err"]) < 1e-15
    assert float(rc34["independent_mpmath_yt2_67_over_315_err"]) < 1e-15
    assert float(rc34["max_precision_err_across_bridges_1_to_5"]) < 1e-13
    assert t34["all_six_guardrails_passed"] is True
    assert t34["continuous_fitted_parameters_in_bridge_ladder"] == 0

    # Theorem 35 (Stage 3.1): B1832 S299b Banked Theorems & Audit Remediation Verification
    t35 = sc["theorem35_b1832_banked_theorems_and_audit_remediation"]
    assert "B1832_the_agy_lanes_digested" in t35["seen_first"]
    assert "FORCED" in t35["claim_labels_and_scopes"]["t_kernel_sum_twist_and_ri1_analytic_derivative"]
    assert "FORCED" in t35["claim_labels_and_scopes"]["t_residue_theta_products_and_ri_up_two_component_nodal_locus"]
    assert float(t35["max_residue_theta_product_err"]) < 1e-13
    assert float(t35["max_ri1_laurent_derivative_err"]) < 1e-13
    assert float(t35["max_ri_up_nodal_zero_err"]) < 1e-14
    assert float(t35["ri_up_off_nodal_abs"]) > 0.01
    assert float(t35["r1_ll_abs_err"]) < 1e-14
    assert float(t35["max_ll_doubling_err"]) < 1e-13
    assert float(t35["max_fa_norm_polynomial_err_n1_to_6"]) < 1e-14
    assert float(t35["frame_mirror_matrix_err"]) < 1e-14
    assert float(t35["per_sector_unconjugated_control_diff"]) > 0.10

    # Theorem 36 (Stage 3.2): The Higgs Singlet's Law: T-Multiplier exp(i*pi/4) & Admissible sigma(tau; r) = i*r*eta(tau)^3/2
    t36 = sc["theorem36_higgs_singlet_t_multiplier_and_admissible_eta3_law"]
    assert "B1832_the_agy_lanes_digested" in t36["seen_first"]
    assert "FORCED" in t36["claim_labels_and_scopes"]["higgs_singlet_t_multiplier_exp_i_pi_over_4"]
    assert "FORCED" in t36["claim_labels_and_scopes"]["mirror_covariance_and_det_S_1_minus_r2_law"]
    assert "FORCED" in t36["claim_labels_and_scopes"]["apntm_observable_invariance_with_admissible_singlet"]
    assert float(t36["half_eta3_t_multiplier_err"]) < 1e-15
    assert float(t36["h_t_multiplier_err"]) < 1e-15
    assert float(t36["half_eta3_sq_minus_h_dot_h_err"]) < 1e-15
    assert float(t36["sigma_mirror_anti_hermitian_err"]) < 1e-15
    assert float(t36["quadratic_det_factor_1_minus_r2_err"]) < 1e-15
    assert float(t36["max_apntm_observable_invariance_err"]) < 1e-13

    # Theorem 37 (Stage 3.3): Single-Line (-adj S, S, S) Georgi-Jarlskog Determinant Unification & Q_i Admixture at Unified Vacuum
    t37 = sc["theorem37_single_line_qi_singlet_d_and_btau_closure_at_unified_vacuum"]
    assert "B1832_the_agy_lanes_digested" in t37["seen_first"]
    assert "FORCED" in t37["claim_labels_and_scopes"]["order10_det_ye_over_det_yd_unity_for_all_r"]
    assert "ADMITTED_HYPOTHESIS" in t37["claim_labels_and_scopes"]["single_line_qi_admixture_for_D_10p58"]
    assert float(t37["max_det_ye_over_yd_err_across_r"]) < 1e-13
    assert abs(float(t37["d_c3_bare_at_tau_star"]) - 9.0) < 1e-3
    assert 10.45 < float(t37["d_c3_with_qi_admixture_at_tau_star"]) < 10.75
    assert t37["haar_trials_run"] == 20
    assert float(t37["max_haar_invariance_err"]) < 1e-13

    # Theorem 38 (Stage 3.4): The Strong Angle Rule: Exact (A, P, N, T, M) Shift Cocycle, Order-100 Ambiguity, & Counterterm theta_ct
    t38 = sc["theorem38_strong_cp_theta_counterterm_rule_and_fpst_closure"]
    assert "B1831_review_74_the_decadal_review" in t38["seen_first"]
    assert "FORCED" in t38["claim_labels_and_scopes"]["five_generator_theta_Y_shift_cocycle"]
    assert "FORCED" in t38["claim_labels_and_scopes"]["order_100_cyclic_ambiguity_on_a_2_5"]
    assert "ADMITTED_HYPOTHESIS" in t38["claim_labels_and_scopes"]["linear_counterterm_rule_theta_ct_invariance"]
    assert float(t38["max_cocycle_shift_err"]) < 1e-13
    assert t38["n_theta_cyclic_order_on_a_2_5"] == 100
    assert float(t38["max_theta_bar_inv_apntm_err"]) < 1e-13

    # Theorem 39 (Stage 3.5): Complete Single-Anchor Non-Dimensionalized 23-Observable Table at Unified Vacuum & Golden Benchmark
    t39 = sc["theorem39_complete_unified_sm_parameter_derivation_table"]
    assert "B1832_the_agy_lanes_digested" in t39["seen_first"]
    assert t39["main_official_scorecard"] == "0 of 19"
    assert t39["imported_dimensionful_anchors_beyond_v_EW"] == []
    assert t39["continuous_fitted_parameters_in_unified_vacuum"] == 0
    assert t39["total_nondimensional_observables_compiled"] == 23

    # Theorem 40 (Stage 3.6): Zero-Trust Hostile-Referee Gate for B1832 Remediation & Theorems 35-39
    t40 = sc["theorem40_zero_trust_hostile_referee_b1832_and_full_sm_gate"]
    assert "B1832_the_agy_lanes_digested" in t40["seen_first"]
    assert "FORCED" in t40["claim_labels_and_scopes"]["stage3_b1832_and_theorems_35_to_39_verification"]
    rc40 = t40["referee_independent_counterchecks"]
    assert float(rc40["independent_mpmath_t_multiplier_err"]) < 1e-15
    assert float(rc40["independent_mpmath_ct_A_shift_err"]) < 1e-15
    assert float(rc40["independent_mpmath_ct_T_shift_err"]) < 1e-15
    assert float(rc40["independent_fresh_haar_invariance_err_t40"]) < 1e-13
    assert float(rc40["max_precision_err_stage3"]) < 1e-13
    assert t40["all_six_guardrails_passed"] is True

    # Theorem 41 (Stage 4.1): Data-Free P-384 Slope 2/5 Selection via Within-Sector Cusp Non-Degeneracy
    t41 = sc["theorem41_p384_data_free_slope_2_over_5_selection_without_yb_over_yt"]
    assert "B1832_the_agy_lanes_digested" in t41["seen_first"]
    assert "FORCED" in t41["claim_labels_and_scopes"]["exact_3_sector_cusp_degeneracy_at_alpha_1_over_5"]
    assert "FORCED" in t41["claim_labels_and_scopes"]["data_free_p384_slope_2_over_5_uniqueness"]
    assert t41["alpha_1_over_5_cusp_exponents"]["Delta_E_up"] == "1/20"
    assert t41["alpha_1_over_5_cusp_exponents"]["Delta_E_down"] == "1/20"
    assert t41["alpha_1_over_5_cusp_exponents"]["Delta_E_lepton"] == "1/20"
    assert t41["alpha_1_over_5_cusp_exponents"]["Delta_E_up_minus_down"] == "0"
    assert t41["alpha_2_over_5_cusp_exponents"]["Delta_E_up"] == "3/20"
    assert t41["alpha_2_over_5_cusp_exponents"]["Delta_E_down"] == "1/20"
    assert t41["alpha_2_over_5_cusp_exponents"]["Delta_E_up_minus_down"] == "1/10"
    assert float(t41["degeneracy_1_over_5_err"]) < 1e-15
    assert float(t41["nondegeneracy_2_over_5_err"]) < 1e-15
    assert float(t41["frac_part_coincidence_1_and_minus4_at_1_over_5_err"]) < 1e-15
    assert t41["data_free_survivors_cusp_nondegenerate"] == ["2/5"]
    assert t41["data_free_survivors_up_steeper_than_down"] == ["2/5"]

    # Theorem 42 (Stage 4.2): Full E_8 / Spin(10) Compensator Lift & Coherent Pin(2) Electromagnetic Phase
    t42 = sc["theorem42_full_e8_spin10_compensator_lift_and_pin2_em_phase"]
    assert "B1832_the_agy_lanes_digested" in t42["seen_first"]
    assert "FORCED" in t42["claim_labels_and_scopes"]["clifford_32d_spin10_compensator_lift"]
    assert "FORCED" in t42["claim_labels_and_scopes"]["pin2_electromagnetic_phase_coherence_across_248d_e8"]
    assert float(t42["clifford_lie_hom_err"]) < 1e-14
    assert float(t42["torus_2x_minus_p_plus_c_err"]) < 1e-15
    assert float(t42["spin10_relations_err"]) < 1e-13
    assert t42["order_g_spin10"] == 32
    assert t42["order_g_so10"] == 16
    assert t42["order_g_pso10"] == 8
    assert t42["dim_e8_total"] == 248
    assert t42["n_zeta_even_120"] == 120
    assert t42["n_zeta_odd_128"] == 128
    assert float(t42["h2_minus_cd5_inv_248_err"]) < 1e-14
    assert float(t42["tilde_a2_minus_p_248_err"]) < 1e-14
    assert float(t42["tilde_a4_minus_id_248_err"]) < 1e-14
    assert float(t42["pin2_q8_coherence_err"]) < 1e-13

    # Theorem 43 (Stage 4.3): Resolution of chat1's 06401ef07 Singlet Hierarchy Flattening via Perturbative KK / Natural eta^3/2 Scaling
    t43 = sc["theorem43_chat1_singlet_hierarchy_flattening_and_perturbative_kk_singlet_scaling"]
    assert "B1832_the_agy_lanes_digested" in t43["seen_first"]
    assert "FORCED" in t43["claim_labels_and_scopes"]["chat1_06401ef07_singlet_hierarchy_flattening_diagnosis"]
    assert "ADMITTED_HYPOTHESIS" in t43["claim_labels_and_scopes"]["perturbative_order5_singlet_scaling_r_1_over_5_in_dr"]
    assert "FORCED" in t43["claim_labels_and_scopes"]["unit_eta3_singlet_scaling_r_1_in_f10_at_tau_star"]
    dr43 = t43["dr_regime_at_tau_10"]
    assert float(dr43["r_0_null_cone"]["ratio_a0_over_half_eta3"]) > 8.5
    assert float(dr43["r_abs_a0_chat1_flattening"]["mc_over_mt"]) > 0.25
    assert float(dr43["r_abs_a0_chat1_flattening"]["ms_over_mb_c3"]) > 0.45
    assert float(dr43["r_1_over_5_perturbative"]["mc_over_mt"]) < float(dr43["r_1_over_5_perturbative"]["ms_over_mb_bare"]) < 0.01
    assert abs(float(dr43["r_1_over_5_perturbative"]["ms_over_mb_c3"]) - 0.01888) < 3e-4
    assert float(dr43["r_1_over_5_perturbative"]["V_ub_over_V_td"]) < 0.85
    assert float(dr43["r_1_over_5_perturbative"]["J_CKM_abs"]) > 2e-4
    f10_43 = t43["f10_regime_at_tau_star"]
    assert float(f10_43["r_1_unit_eta3"]["mc_over_mt"]) < float(f10_43["r_1_unit_eta3"]["ms_over_mb_bare"]) < 0.025
    assert abs(float(f10_43["r_1_unit_eta3"]["V_ub_over_V_td"]) - 0.4473) < 0.02
    assert float(f10_43["r_1_unit_eta3"]["J_CKM_abs"]) > 5e-5
    assert t43["haar_trials_run"] == 20
    assert float(t43["max_haar_invariance_err"]) < 1e-13

    # Theorem 44 (Stage 4.4): Simultaneous 10 Charged-Fermion + 4 CKM Closure at M_Z in Both F_10 and DR Regimes
    t44 = sc["theorem44_simultaneous_charged_fermion_and_ckm_mz_closure_f10_and_dr"]
    assert "B1832_the_agy_lanes_digested" in t44["seen_first"]
    assert "ADMITTED_HYPOTHESIS" in t44["claim_labels_and_scopes"]["downward_xing_zhou_rge_running_from_m12_to_mz"]
    assert "ADMITTED_HYPOTHESIS" in t44["claim_labels_and_scopes"]["simultaneous_charged_fermion_and_ckm_mz_closure"]
    assert abs(float(t44["downward_rge_integral_It_corr"]) - 0.0644930315) < 1e-12
    assert 10.45 < float(t44["f10_unified_vacuum_tau_star_at_MZ"]["D_c3_with_qi_admixture"]) < 10.75
    assert float(t44["f10_unified_vacuum_tau_star_at_MZ"]["V_ub_over_V_td_MZ"]) < 0.50
    assert t44["haar_trials_run"] == 20
    assert float(t44["max_haar_invariance_err"]) < 1e-13

    # Theorem 45 (Stage 4.5): Complete 19 SM + 4 Gravity Scorecard at M_Z & Explicit Two-Column Unearned-Input Ledger
    t45 = sc["theorem45_complete_19_sm_plus_4_gravity_scorecard_and_unearned_inputs_ledger"]
    assert "B1832_the_agy_lanes_digested" in t45["seen_first"]
    assert t45["main_official_scorecard"] == "0 of 19"
    assert t45["imported_dimensionful_anchors_beyond_v_EW"] == []
    assert t45["total_observables_in_scorecard"] == 23
    ul45 = t45["unearned_inputs_ledger"]
    assert ul45["num_forced_theorems"] == 12
    assert ul45["num_admitted_hypothesis_bridges"] == 7
    assert float(ul45["total_unearned_discrete_bits_in_column1"]) == 0.0
    assert int(ul45["total_unearned_continuous_params_in_column1"]) == 0
    assert float(ul45["total_unearned_discrete_bits_in_column2"]) > 8.0
    assert int(ul45["total_unearned_continuous_params_in_column2"]) == 1

    # Theorem 46 (Stage 4.6): Zero-Trust Hostile-Referee Gate for Theorems 41-45
    t46 = sc["theorem46_zero_trust_hostile_referee_full_sm_two_column_gate"]
    assert "B1832_the_agy_lanes_digested" in t46["seen_first"]
    assert "FORCED" in t46["claim_labels_and_scopes"]["stage4_theorems_41_to_45_verification"]
    assert "FORCED" in t46["claim_labels_and_scopes"]["two_column_transparency_and_working_rules_gate"]
    rc46 = t46["referee_independent_counterchecks"]
    assert float(rc46["independent_mpmath_t41_cusp_err"]) < 1e-15
    assert float(rc46["independent_mpmath_t42_em_phase_err"]) < 1e-15
    assert float(rc46["independent_fresh_haar_invariance_err_t46"]) < 1e-13
    assert float(rc46["max_precision_err_stage4"]) < 1e-13
    assert t46["all_six_guardrails_passed"] is True

    # Theorem 47 (Stage 5.1): Zero-Continuous-Parameter Rational Q_i Admixture (1/42 and 1/45) for HYP-05
    t47 = sc["theorem47_hyp05_zero_continuous_param_kk_casimir_qi_admixture"]
    assert "B1832_the_agy_lanes_digested" in t47["seen_first"]
    assert "FORCED" in t47["claim_labels_and_scopes"]["exact_rational_kk_and_casimir_qi_scales"]
    assert t47["continuous_parameters_used"] == 0
    assert float(t47["rational_identity_err"]) == 0.0
    assert abs(float(t47["at_delta_i_kk_1_over_42"]["delta_i"]) - (1.0 / 42.0)) < 1e-15
    assert abs(float(t47["at_delta_i_kk_1_over_42"]["rel_error_D_vs_10p58"])) < 0.006
    assert float(t47["at_delta_i_kk_1_over_42"]["half_lift_qi_flipped_det_ratio_minus_1_err"]) < 1e-13
    assert abs(float(t47["at_delta_i_casimir_1_over_45"]["delta_i"]) - (1.0 / 45.0)) < 1e-15
    assert abs(float(t47["at_delta_i_casimir_1_over_45"]["rel_error_D_vs_10p58"])) < 0.006
    assert float(t47["at_delta_i_casimir_1_over_45"]["half_lift_qi_flipped_det_ratio_minus_1_err"]) < 1e-13
    assert abs(float(t47["at_delta_i_midpoint_29_over_1260"]["rel_error_D_vs_10p58"])) < 1e-4
    assert t47["haar_trials_run"] == 20
    assert float(t47["max_haar_invariance_err"]) < 1e-13

    # Theorem 48 (Stage 5.2): Z_3 Galois Character Projectors on M_3 for HYP-01 & HYP-02
    t48 = sc["theorem48_hyp01_hyp02_galois_z3_character_projector_and_kahler_trace"]
    assert "B1832_the_agy_lanes_digested" in t48["seen_first"]
    assert "FORCED" in t48["claim_labels_and_scopes"]["z3_galois_character_projectors_on_m3"]
    assert float(t48["z3_projector_err"]) < 1e-15
    assert float(t48["rho_branch_trace_err"]) < 1e-15
    assert float(t48["rho_branch_eigs_err"]) < 1e-15
    assert float(t48["tr_y16_squared"]) == 120.0
    assert float(t48["tr_down_single_sheet"]) == 5.0
    assert t48["haar_trials_run"] == 20
    assert float(t48["max_haar_invariance_err"]) < 1e-13

    # Theorem 49 (Stage 5.3): Explicit SU(3)_c Gell-Mann Casimir 4/3 & su(4)_C Pati-Salam B-L Ratio -1/3 for HYP-03 & HYP-04
    t49 = sc["theorem49_hyp03_hyp04_kk_casimir_matching_and_spin10_126_clebsch_algebra"]
    assert "B1832_the_agy_lanes_digested" in t49["seen_first"]
    assert "FORCED" in t49["claim_labels_and_scopes"]["su3_gell_mann_casimir_and_kk_quadrature_67_over_315"]
    assert "FORCED" in t49["claim_labels_and_scopes"]["su4_pati_salam_b_minus_l_clebsch_minus_third"]
    assert float(t49["su3_casimir_matrix_err"]) < 1e-15
    assert float(t49["su3_killing_orth_err"]) < 1e-15
    assert float(t49["yt2_quad_minus_67_over_315_err"]) < 1e-15
    assert float(t49["tr_b_minus_l_err"]) < 1e-15
    assert float(t49["clebsch_minus_third_err"]) < 1e-15
    assert t49["haar_trials_run"] == 20
    assert float(t49["max_haar_invariance_err"]) < 1e-13

    # Theorem 50 (Stage 5.4): Quillen Anomaly C_QCD = 66 => 264*pi & First-Principles Clausen/Trigamma Vol(m004) for HYP-06 & HYP-07
    t50 = sc["theorem50_hyp06_hyp07_aps_eta_strong_cp_counterterm_and_m004_clausen_gravity"]
    assert "B1832_the_agy_lanes_digested" in t50["seen_first"]
    assert "FORCED" in t50["claim_labels_and_scopes"]["quillen_determinant_line_anomaly_264_pi_and_132_pi"]
    assert "FORCED" in t50["claim_labels_and_scopes"]["first_principles_clausen_trigamma_volume_of_m004"]
    assert t50["c_qcd_anomaly_66"] == 66
    assert t50["coeff_a_shift_264"] == 264
    assert t50["coeff_t_shift_132"] == 132
    assert float(t50["quillen_coeff_err"]) == 0.0
    assert abs(float(t50["vol_m004_from_polylog"]) - 2.0298832128193072) < 1e-15
    assert abs(float(t50["vol_m004_from_trigamma"]) - 2.0298832128193072) < 1e-15
    assert float(t50["vol_m004_clausen_err"]) < 1e-15
    assert float(t50["vol_m004_trigamma_err"]) < 1e-15

    # Theorem 51 (Stage 5.5): Updated Two-Column Ledger with 16 FORCED Theorems and ZERO Continuous Parameters
    t51 = sc["theorem51_updated_two_column_ledger_zero_continuous_parameters"]
    assert "B1832_the_agy_lanes_digested" in t51["seen_first"]
    assert t51["main_official_scorecard"] == "0 of 19"
    assert t51["imported_dimensionful_anchors_beyond_v_EW"] == []
    assert t51["total_observables_in_scorecard"] == 23
    ul51 = t51["unearned_inputs_ledger"]
    assert ul51["num_forced_theorems"] == 16
    assert ul51["num_admitted_hypothesis_bridges"] == 7
    assert float(ul51["total_unearned_discrete_bits_in_column1"]) == 0.0
    assert int(ul51["total_unearned_continuous_params_in_column1"]) == 0
    assert int(ul51["total_unearned_continuous_params_in_column2"]) == 0

    # Theorem 52 (Stage 5.6): Zero-Trust Hostile-Referee Gate for Theorems 47-51
    t52 = sc["theorem52_zero_trust_hostile_referee_bridge_promotion_gate"]
    assert "B1832_the_agy_lanes_digested" in t52["seen_first"]
    assert "FORCED" in t52["claim_labels_and_scopes"]["stage5_theorems_47_to_51_verification"]
    assert "FORCED" in t52["claim_labels_and_scopes"]["zero_continuous_parameter_two_column_gate"]
    rc52 = t52["referee_independent_counterchecks"]
    assert float(rc52["independent_mpmath_vol_m004_err"]) < 1e-15
    assert float(rc52["independent_mpmath_z3_orth_err"]) < 1e-15
    assert float(rc52["independent_fresh_haar_invariance_err_t52"]) < 1e-13
    assert float(rc52["max_precision_err_stage5"]) < 1e-13
    assert t52["all_six_guardrails_passed"] is True

    # Theorem 53 (Stage 6.1): S300/S300b P-661 Borrowed-Joints Scaffold & P-662 Provenance Clean-Sweep
    t53 = sc["theorem53_p661_borrowed_joints_scaffold_and_p662_provenance_clean_sweep"]
    assert "B1830_the_register_triaged" in t53["seen_first"]
    assert "FORCED" in t53["claim_labels_and_scopes"]["p662_100_percent_provenance_resolution"]
    assert "FORCED" in t53["claim_labels_and_scopes"]["p661_borrowed_joints_scaffold_and_p418_vector"]
    assert int(t53["missing_or_invented_citations_count"]) == 0
    assert int(t53["total_observables_in_p418_vector"]) == 23
    assert int(t53["total_borrowed_continuous_parameters"]) == 0
    assert int(t53["unique_borrowed_discrete_joints_count"]) == 7

    # Theorem 54 (Stage 6.2): S300 P-638 Charged-Lepton Left Diagonalizer U_e^L Control on Order-5 and Order-10 Lines
    t54 = sc["theorem54_p638_charged_lepton_ue_and_pmns_second_held_out_target"]
    assert "B1830_the_register_triaged" in t54["seen_first"]
    assert "FORCED" in t54["claim_labels_and_scopes"]["order5_uel_equals_udr_conj_control"]
    assert "FORCED" in t54["claim_labels_and_scopes"]["order10_uel_equals_di_udr_conj_half_lift"]
    assert float(t54["max_order5_uel_vs_udr_conj_err"]) < 1e-13
    assert float(t54["max_order10_uel_vs_di_udr_conj_err"]) < 1e-13
    assert t54["haar_trials_run"] == 20
    assert float(t54["max_haar_invariance_err"]) < 1e-13

    # Theorem 55 (Stage 6.3): S300 P-639 The Mirror in Matter & P-637 Two-Channel 1-Loop Radiative Lift of D
    t55 = sc["theorem55_p639_mirror_in_matter_and_p637_one_loop_radiative_lift"]
    assert "B1830_the_register_triaged" in t55["seen_first"]
    assert "FORCED" in t55["claim_labels_and_scopes"]["p639_mirror_and_mod5_transposition_sector_pairing"]
    assert "ADMITTED_HYPOTHESIS" in t55["claim_labels_and_scopes"]["p637_two_channel_rational_mean_29_over_1260_for_d"]
    assert t55["up_is_mod5_self_transpose"] is True
    assert t55["down_lepton_are_mod5_transposes"] is True
    assert t55["unique_negative_sum_sector"] == ["up"]
    assert float(t55["max_b1821_mirror_hermitian_err"]) < 1e-13
    assert float(t55["rational_mean_29_over_1260_err"]) == 0.0
    assert float(t55["sigma_deviation_from_pdg_10p58"]) < 0.01

    # Theorem 56 (Stage 6.4): S300 P-636 Deriving the 3 from Minimal Hyperbolic Trace |2 - tr| = 3, FK7 Deck Count, & FK11 Curvature
    t56 = sc["theorem56_p636_deriving_the_three_from_minimal_hyperbolic_trace_and_fk11"]
    assert "B1830_the_register_triaged" in t56["seen_first"]
    assert "FORCED" in t56["claim_labels_and_scopes"]["p636_minimal_hyperbolic_trace_5_and_lefschetz_3"]
    assert "FORCED" in t56["claim_labels_and_scopes"]["fk7_deck_gauged_1_vs_kept_3_and_fk11_curvature"]
    assert int(t56["tr_l3r"]) == 5
    assert int(t56["lefschetz_count_l3r"]) == 3
    assert int(t56["minimal_prime_gt2_lefschetz"]) == 3
    assert int(t56["minimal_prime_gt2_trace"]) == 5
    assert float(t56["lefschetz_formula_err_across_36_words"]) == 0.0
    assert int(t56["fk7_deck_gauged_dim"]) == 1
    assert int(t56["fk7_deck_kept_dim"]) == 3
    assert float(t56["spin_curvature_flux_k_half"]) == -0.5
    assert float(t56["lichnerowicz_shift"]) == 0.5
    assert float(t56["fk11_gauss_bonnet_err"]) == 0.0

    # Theorem 57 (Stage 6.5): S300 P-629 / P-630 / P-631 / P-633 Critical Weave Switch c_crit = 6*pi*h & 2-Loop Fiber Vacuum Arrest
    t57 = sc["theorem57_p629_p630_p631_p633_critical_weave_switch_and_two_loop_fiber_potential"]
    assert "B1830_the_register_triaged" in t57["seen_first"]
    assert "FORCED" in t57["claim_labels_and_scopes"]["p633_critical_weave_switch_6pi_vol_m004"]
    assert "FORCED" in t57["claim_labels_and_scopes"]["p630_tricritical_ising_dimensions_match_b1788_exponents"]
    assert "FORCED" in t57["claim_labels_and_scopes"]["p631_one_loop_eisenstein_runaway_vs_holonomy_casimir_arrest"]
    assert abs(float(t57["c_crit_6pi_vol_m004"]) - 38.2623971342303) < 1e-12
    assert float(t57["c_crit_ratio_err"]) < 1e-15
    assert float(t57["tricritical_exponent_err"]) == 0.0
    assert float(t57["golden_eigenvalue_err"]) < 1e-15
    assert t57["one_loop_always_runs_to_cusp"] is True

    # Theorem 58 (Stage 6.6): Zero-Trust Hostile-Referee Gate for Theorems 53-57 & Full S300/S300b Certification
    t58 = sc["theorem58_zero_trust_hostile_referee_stage6_s300_gate"]
    assert "B1830_the_register_triaged" in t58["seen_first"]
    assert "FORCED" in t58["claim_labels_and_scopes"]["stage6_theorems_53_to_57_verification"]
    assert "FORCED" in t58["claim_labels_and_scopes"]["p661_p662_s300_s300b_readiness_gate"]
    rc58 = t58["referee_independent_counterchecks"]
    assert float(rc58["independent_mpmath_c_crit_err"]) < 1e-13
    assert float(rc58["independent_mpmath_golden_trace_err"]) < 1e-15
    assert float(rc58["independent_fresh_haar_invariance_err_t58"]) < 1e-13
    assert float(rc58["max_precision_err_stage6"]) < 1e-13
    assert t58["all_six_guardrails_passed"] is True

    # Theorem 59 (Stage 7.1): S300c P-663 Cheapest Scoreboard Conversions B08 (B1667 L_2) & B47 (Reidemeister Torsion)
    t59 = sc["theorem59_p663_b1667_l2_and_reidemeister_torsion_conversions"]
    assert "B1667_the_canonical_cusp" in t59["seen_first"]
    assert "FORCED" in t59["claim_labels_and_scopes"]["b08_to_f4_exact_b1667_l2_conversion"]
    assert "FORCED" in t59["claim_labels_and_scopes"]["b47_fox_free_calculus_reidemeister_torsion"]
    assert "plain_english_elaboration" in t59
    assert int(t59["lookup_table_points_used"]) == 0
    assert float(t59["b1667_json_strip_agreement_err"]) < 2e-11
    assert float(t59["fox_fundamental_identity_err"]) < 1e-14
    assert float(t59["max_alexander_poly_err"]) < 1e-14
    assert float(t59["tau_rs_abelian_err"]) < 1e-14
    assert float(t59["tau_rs_adjoint_err"]) < 1e-14
    assert abs(float(t59["w_ad_at_minus1"]) - (-14.0)) < 1e-14
    assert abs(float(t59["w_ad_slope_at_1"]) - 3.0) < 1e-14

    # Theorem 60 (Stage 7.2): Analytic Term-by-Term q-Series Proof of B1834 Joint F7 Mirror Identity
    t60 = sc["theorem60_analytic_q_series_proof_of_f7_mirror_identity"]
    assert "B1821_the_frames_mirror_symmetry_in_re_tau" in t60["seen_first"]
    assert "FORCED" in t60["claim_labels_and_scopes"]["term_by_term_theta_q_series_mirror_conjugation"]
    assert "FORCED" in t60["claim_labels_and_scopes"]["quaternionic_channel_parity_and_f7_matrix_proof"]
    assert "plain_english_elaboration" in t60
    assert float(t60["max_single_term_q_series_err"]) < 1e-14
    assert float(t60["max_t1_term_err"]) < 1e-14
    assert float(t60["max_quat_matrix_parity_err"]) < 1e-14
    assert float(t60["max_channel_residue_parity_err"]) < 1e-14
    assert float(t60["max_algebraic_3x3_f7_err"]) < 1e-13

    # Theorem 61 (Stage 7.3): S300c P-664 Self-Contained Gauge-to-Yukawa Cascade Eliminating Measured Inputs & Refuted Legacy Keys
    t61 = sc["theorem61_p664_self_contained_gauge_to_yukawa_cascade_zero_measured_inputs"]
    assert "B1830_the_register_triaged" in t61["seen_first"]
    assert "FORCED" in t61["claim_labels_and_scopes"]["p664_self_contained_cascade_zero_measured_couplings"]
    assert "ADMITTED_HYPOTHESIS" in t61["claim_labels_and_scopes"]["single_uv_scale_m12_reading_and_ode_itop"]
    assert "plain_english_elaboration" in t61
    assert int(t61["imported_measured_couplings_count"]) == 0
    assert t61["imported_dimensionful_anchors_beyond_v_EW"] == []
    assert float(t61["uv_bvp_residual"]) < 1e-13
    assert int(t61["eliminated_b1834_joints_count"]) == 13
    assert t61["haar_trials_run"] == 20
    assert float(t61["max_haar_invariance_err"]) < 1e-13

    # Theorem 62 (Stage 7.4): S300 P-632 Instability Spectrum, P-634 Angle A Cuspidal Cohomology, & P-635 Flat Q_8 Bundle dim H^1 = 0
    t62 = sc["theorem62_s300_p632_instability_spectrum_p634_cuspidal_cohomology_and_p635_h1_q8"]
    assert "B1830_the_register_triaged" in t62["seen_first"]
    assert "FORCED" in t62["claim_labels_and_scopes"]["p632_one_loop_eisenstein_saddle_instability"]
    assert "FORCED" in t62["claim_labels_and_scopes"]["p634_cuspidal_cohomology_on_punctured_torus"]
    assert "FORCED" in t62["claim_labels_and_scopes"]["p635_flat_q8_bundle_cohomological_rigidity_h1_zero"]
    assert "plain_english_elaboration" in t62
    assert t62["one_loop_is_saddle_instability"] is True
    assert float(t62["commutator_minus_t6_err"]) == 0.0
    assert t62["parabolic_cuspidal_cohomology_dims"] == {1: 2, 2: 4, 3: 6}
    assert float(t62["d1_d0_chain_complex_err"]) < 1e-15
    assert int(t62["rank_d0_coboundary"]) == 3
    assert int(t62["rank_d1_cocycle"]) == 3
    assert int(t62["dim_h0_ad_q8"]) == 0
    assert int(t62["dim_z1_ad_q8"]) == 3
    assert int(t62["dim_b1_ad_q8"]) == 3
    assert int(t62["dim_h1_ad_q8"]) == 0
    assert int(t62["continuous_q8_bundle_moduli"]) == 0

    # Theorem 63 (Stage 7.5): B1834 Frame B Borrowed-Joint Reduction Audit
    t63 = sc["theorem63_b1834_frame_b_borrowed_joint_reduction_audit"]
    assert "B1830_the_register_triaged" in t63["seen_first"]
    assert "FORCED" in t63["claim_labels_and_scopes"]["b1834_measured_refuted_and_unknown_joints_eliminated"]
    assert "ADMITTED_HYPOTHESIS" in t63["claim_labels_and_scopes"]["seven_admitted_hypothesis_bridges_remaining"]
    assert "plain_english_elaboration" in t63
    assert int(t63["b1834_at_18c607040_counts"]["total_borrowed_joints"]) == 45
    assert int(t63["stage7_resolved_joints_count"]) == 15
    assert int(t63["stage7_after_counts"]["MEASURED-INPUT"]) == 0
    assert int(t63["stage7_after_counts"]["REFUTED"]) == 0
    assert int(t63["stage7_after_counts"]["UNKNOWN"]) == 0
    assert int(t63["stage7_after_counts"]["FORCED-CLAIMED"]) == 0
    assert int(t63["stage7_after_counts"]["FITTED_CONTINUOUS"]) == 0
    assert int(t63["stage7_after_counts"]["ADMITTED_HYPOTHESIS_DISCRETE_BRIDGES"]) == 7
    assert int(t63["stage7_after_counts"]["FORCED_THEOREMS_IN_COLUMN1"]) == 24

    # Theorem 64 (Stage 7.6): Zero-Trust Hostile-Referee Gate for Theorems 59-63 & Full S300c B1834 Certification
    t64 = sc["theorem64_zero_trust_hostile_referee_stage7_b1834_gate"]
    assert "B1830_the_register_triaged" in t64["seen_first"]
    assert "FORCED" in t64["claim_labels_and_scopes"]["stage7_theorems_59_to_63_verification"]
    assert "FORCED" in t64["claim_labels_and_scopes"]["b1834_p663_p664_s300c_readiness_gate"]
    assert "plain_english_elaboration" in t64
    rc64 = t64["referee_independent_counterchecks"]
    assert float(rc64["independent_mpmath_torsion_err"]) < 1e-25
    assert float(rc64["independent_mpmath_vs_t59_err"]) < 1e-15
    assert float(rc64["independent_mpmath_f7_theta1_err"]) < 1e-25
    assert float(rc64["independent_fresh_haar_invariance_err_t64"]) < 1e-13
    assert float(rc64["max_precision_err_stage7"]) < 1e-13
    assert t64["all_six_guardrails_passed"] is True

    # Theorem 65 (Stage 8.1): Foundational Pillar 1 - 2D Slice Inside 3D Mapping Torus & |b_3| Complex Chern-Simons Unification
    t65 = sc["theorem65_pillar1_slice_bulk_mapping_torus_and_b3_complex_chern_simons_unification"]
    assert "B1830_the_register_triaged" in t65["seen_first"]
    assert "FORCED" in t65["claim_labels_and_scopes"]["mapping_torus_slice_bulk_structure"]
    assert "FORCED" in t65["claim_labels_and_scopes"]["qcd_single_b3_complex_chern_simons_unification"]
    assert "FORCED" in t65["claim_labels_and_scopes"]["p667_l248_arithmetic_atom_identity"]
    assert "plain_english_elaboration" in t65
    assert int(t65["tr_a_m004"]) == 3
    assert int(t65["lefschetz_a_m004"]) == 1
    assert int(t65["tr_a_m3"]) == 18
    assert int(t65["lefschetz_a_m3"]) == 16
    assert float(t65["monodromy_eig_err"]) < 1e-14
    assert int(t65["abs_b3_qcd"]) == 7
    assert float(t65["qcd_single_b3_identity_err"]) < 1e-14
    assert float(t65["atom_real_shift_err"]) < 1e-14
    assert float(t65["atom_imag_vol_err"]) < 1e-14

    # Theorem 66 (Stage 8.2): Foundational Pillar 2 - Single-Higgs Fermion Kahler Equivalence
    t66 = sc["theorem66_pillar2_one_higgs_fermion_kahler_equivalence_eliminating_two_higgs_ansatz"]
    assert "B1742_two_higgs_verified_on_main" in t66["seen_first"]
    assert "FORCED" in t66["claim_labels_and_scopes"]["haar_unitary_invariance_of_1hdm_kahler_yukawas"]
    assert "plain_english_elaboration" in t66
    assert int(t66["extra_higgs_doublets_beyond_sm"]) == 0
    assert float(t66["z_d_inv_kahler_5"]) == 5.0
    assert float(t66["one_higgs_vs_two_higgs_err"]) < 1e-14
    assert t66["haar_trials_run"] == 20
    assert float(t66["max_haar_invariance_err"]) < 1e-13

    # Theorem 67 (Stage 8.3): Foundational Pillar 3 - Spectral Faithfulness Principle vs chat1's Steepness Map & P-625
    t67 = sc["theorem67_pillar3_spectral_faithfulness_and_chat1_steepness_map_audit"]
    assert "B1788_the_closed_form_of_the_exponents" in t67["seen_first"]
    assert "FORCED" in t67["claim_labels_and_scopes"]["chat1_steepness_map_condition_norm4a_gt_third"]
    assert "FORCED" in t67["claim_labels_and_scopes"]["spectral_faithfulness_mod5_orbit_separation_selects_2_over_5"]
    assert "plain_english_elaboration" in t67
    assert int(t67["slopes_tested_s_up_to_25"]) > 80
    assert float(t67["chat1_steepness_formula_err"]) == 0.0
    assert float(t67["max_gap_quarter_err"]) == 0.0
    assert t67["alpha_1_5_is_spectrally_faithful"] is False
    assert t67["alpha_2_5_is_spectrally_faithful"] is True
    assert t67["spectrally_faithful_n5_slopes"] == ["2/5"]

    # Theorem 68 (Stage 8.4): S300d/e/f B1835 Planted Divisibility Relations & Channel Exponents
    t68 = sc["theorem68_s300f_b1835_planted_quark_lepton_relations_and_dirac_r_ratio"]
    assert "B1728_the_lines_order_as_a_quotient_of_hypercharge" in t68["seen_first"]
    assert "FORCED" in t68["claim_labels_and_scopes"]["b1835_planted_order_div6_and_div4_quark_lepton_relations"]
    assert "plain_english_elaboration" in t68
    assert float(t68["div6_max_nu_lep_prop_err"]) < 1e-13
    assert float(t68["non_div6_min_nu_lep_dev"]) > 0.01
    assert float(t68["div4_max_quark_lepton_prop_err"]) < 1e-13
    assert float(t68["non_div4_min_quark_lepton_dev"]) > 0.02
    assert float(t68["dirac_nu_exponent_err"]) < 1e-15
    assert float(t68["dirac_nu_gap_err"]) < 1e-15
    assert t68["haar_trials_run"] == 20

    # Theorem 69 (Stage 8.5): P-667 Regular-Tetrahedral Family Atom & Compression of 7 Bridges into 4 Irreducible Pillar Bridges
    t69 = sc["theorem69_p667_l248_arithmetic_atom_and_3_pillar_bridge_compression"]
    assert "B1830_the_register_triaged" in t69["seen_first"]
    assert "FORCED" in t69["claim_labels_and_scopes"]["p667_tetrahedral_family_atom_m004_m003_m3"]
    assert "ADMITTED_HYPOTHESIS" in t69["claim_labels_and_scopes"]["three_pillar_bridge_compression_to_4_irreducible_bridges"]
    assert "plain_english_elaboration" in t69
    assert float(t69["tetrahedral_family_atom_err"]) < 1e-15
    assert t69["m004_is_amphichiral"] is True
    assert t69["m003_is_amphichiral"] is False
    assert int(t69["num_forced_theorems_in_column1"]) == 28
    assert int(t69["num_irreducible_pillar_bridges_in_column2"]) == 4
    assert int(t69["total_unearned_continuous_params_in_column2"]) == 0
    assert abs(float(t69["total_unearned_discrete_bits_in_column2"]) - 6.0) < 1e-15

    # Theorem 70 (Stage 8.6): Zero-Trust Hostile-Referee Gate for Theorems 65-69 & 3-Pillar Foundational Certification
    t70 = sc["theorem70_zero_trust_hostile_referee_stage8_foundational_and_b1835_gate"]
    assert "B1830_the_register_triaged" in t70["seen_first"]
    assert "FORCED" in t70["claim_labels_and_scopes"]["stage8_theorems_65_to_69_verification"]
    assert "FORCED" in t70["claim_labels_and_scopes"]["three_pillar_foundational_and_b1835_readiness_gate"]
    assert "plain_english_elaboration" in t70
    rc70 = t70["referee_independent_counterchecks"]
    assert float(rc70["independent_mpmath_atom_real_err"]) < 1e-25
    assert float(rc70["independent_mpmath_atom_imag_err"]) < 1e-25
    assert float(rc70["independent_mpmath_qcd_b3_err"]) < 1e-25
    assert float(rc70["independent_fresh_haar_invariance_err_t70"]) < 1e-13
    assert float(rc70["max_precision_err_stage8"]) < 1e-13
    assert t70["all_six_guardrails_passed"] is True

    # Theorem 71 (Stage 9.1): Rebuttal of All 7 Wrongful/Stale Refutations & Exact Theorem 21 All-Orders Transpose Reflection Law
    t71 = sc["theorem71_rebuttal_of_seven_wrongful_or_stale_refutations_and_t21_all_orders_determinant_law"]
    assert "B1832_the_agy_lanes_digested" in t71["seen_first"]
    assert "FORCED" in t71["claim_labels_and_scopes"]["t21_all_orders_transpose_reflection_and_sigma10_even_law"]
    assert "FORCED" in t71["claim_labels_and_scopes"]["rebuttal_of_all_seven_wrongful_or_stale_refutations"]
    assert "plain_english_elaboration" in t71
    assert float(t71["residue_reflection_err"]) < 1e-13
    assert float(t71["max_transpose_reflection_err"]) < 1e-12
    assert float(t71["max_reflected_sv_err"]) < 1e-12
    assert float(t71["max_reflected_det_err"]) < 1e-12
    assert float(t71["max_qi_free_all_orders_err"]) < 1e-12
    assert float(t71["max_sigma10_even_product_err"]) < 1e-12
    assert int(t71["seven_rebuttals_count"]) == 7

    # Theorem 72 (Stage 9.2): chat1 S300f Doublet Index Projective Reading-Distance & Non-Holomorphic Conjugate I-35 Survival
    t72 = sc["theorem72_chat1_doublet_index_reading_distance_and_nonholomorphic_conjugate_i35"]
    assert "B1790_the_reading_not_derived_in_the_frame" in t72["seen_first"]
    assert "FORCED" in t72["claim_labels_and_scopes"]["chat1_projective_reading_distance_identity"]
    assert "FORCED" in t72["claim_labels_and_scopes"]["nonholomorphic_conjugate_higgs_i35_survival"]
    assert "plain_english_elaboration" in t72
    assert float(t72["unit_orth_err"]) < 1e-15
    assert float(t72["pseudoreal_err"]) < 1e-15
    assert float(t72["max_reading_distance_err"]) < 1e-13
    assert abs(float(t72["holomorphic_twist_flip_shift"]) - 0.40) < 1e-15
    assert float(t72["rho_f10_at_tau_star"]) < 0.04
    assert float(t72["reading_separation_fraction_f10"]) > 0.97
    assert float(t72["nonholomorphic_conjugate_n_invariance_err"]) == 0.0

    # Theorem 73 (Stage 9.3): chat1 S300f Density Higgs Closed-Form Area Integral & Cauchy-Pompeiu Proof
    t73 = sc["theorem73_chat1_density_higgs_exact_area_integral_eliminating_puncture_cut"]
    assert "B1651_where_a_higgs_can_couple" in t73["seen_first"]
    assert "FORCED" in t73["claim_labels_and_scopes"]["dolbeault_cauchy_pompeiu_density_higgs_integral"]
    assert "FORCED" in t73["claim_labels_and_scopes"]["cut_free_2d_area_integration_without_disk_excision"]
    assert "plain_english_elaboration" in t73
    assert int(t73["quadrature_nodes_per_axis"]) == 48
    assert int(t73["channels_and_modes_verified"]) == 12
    assert float(t73["max_density_integral_rel_err"]) < 1e-13
    assert t73["requires_punctured_disk_cutoff"] is False

    # Theorem 74 (Stage 9.4): physical-bridge 646492da1 Fredholm Index Cancellation & Quaternionic SU(2)_L Weak Chirality
    t74 = sc["theorem74_physical_bridge_dolbeault_fredholm_index_and_quaternionic_weak_chirality"]
    assert "B1651_where_a_higgs_can_couple" in t74["seen_first"]
    assert "FORCED" in t74["claim_labels_and_scopes"]["physical_bridge_dolbeault_fredholm_index_zero"]
    assert "FORCED" in t74["claim_labels_and_scopes"]["quaternionic_su2L_weak_chirality_completion"]
    assert "plain_english_elaboration" in t74
    assert float(t74["fredholm_index_cancellation_err"]) == 0.0
    assert int(t74["old_parent_control_at_beta1"]) == 1
    assert abs(float(t74["su2L_casimir_left"]) - 0.75) < 1e-15
    assert float(t74["su2L_casimir_right"]) == 0.0
    assert abs(float(t74["weak_chiral_asymmetry"]) - 1.0) < 1e-15

    # Theorem 75 (Stage 9.5): origin/main S300d P-666 Serre Derivative DR vs F_10 Null-Cone Unification
    t75 = sc["theorem75_s300d_p666_serre_derivative_dr_and_f10_null_cone_unification"]
    assert "B1691_the_exponents_at_the_two_fixed_points" in t75["seen_first"]
    assert "FORCED" in t75["claim_labels_and_scopes"]["jacobi_null_cone_perturbation_law_dr_and_f10"]
    assert "FORCED" in t75["claim_labels_and_scopes"]["dr_and_f10_shared_half_lift_covariance"]
    assert "plain_english_elaboration" in t75
    assert float(t75["r_null_err"]) < 1e-25
    assert float(t75["dr_dot_dr_err"]) < 1e-14
    assert float(t75["rho_dr_at_tau_star"]) < 0.04
    assert float(t75["rho_f10_at_tau_star"]) < 0.04
    assert float(t75["dr_half_lift_err"]) < 1e-12
    assert float(t75["f10_half_lift_err"]) < 1e-12

    # Theorem 76 (Stage 9.6): Zero-Trust Hostile-Referee Gate for Theorems 71-75 & Cross-Seat Synthesis
    t76 = sc["theorem76_zero_trust_hostile_referee_stage9_cross_seat_synthesis_gate"]
    assert "B1832_the_agy_lanes_digested" in t76["seen_first"]
    assert "FORCED" in t76["claim_labels_and_scopes"]["stage9_theorems_71_to_75_verification"]
    assert "FORCED" in t76["claim_labels_and_scopes"]["cross_seat_synthesis_and_rebuttal_gate"]
    assert "plain_english_elaboration" in t76
    rc76 = t76["referee_independent_counterchecks"]
    assert float(rc76["independent_mpmath_reading_dist_err"]) < 1e-25
    assert float(rc76["independent_fresh_haar_invariance_err_t76"]) < 1e-12
    assert float(rc76["max_precision_err_stage9"]) < 1e-12
    assert t76["all_six_guardrails_passed"] is True

    # Theorem 77 (Stage 10.1): Rebuttals of B1836 S301 Misreadings on B08 Exact 2D L_2, Spin(10)->SO(10)->PSO(10) Tower, and c29b
    t77 = sc["theorem77_b1836_s301_rebuttals_b08_exact_l2_proof_and_spin10_so10_pso10_tower"]
    assert "B1667_the_canonical_cusp" in t77["seen_first"]
    assert "MATH" in t77["claim_labels_and_scopes"]["b08_exact_2d_l2_already_solved_in_t30_t59"]
    assert "MATH" in t77["claim_labels_and_scopes"]["spin10_so10_pso10_covering_group_tower_32_16_8"]
    assert "plain_english_elaboration" in t77
    assert float(t77["b08_l2_golden_vs_b1836_c2_err"]) < 2e-11
    assert float(t77["b08_l2_star_vs_b1836_c30b_err"]) < 1e-8
    assert float(t77["omega6_l2_minus_lmax_2pi3_err"]) < 1e-11
    assert int(t77["spin10_group_order"]) == 32
    assert int(t77["spin10_center_order"]) == 8
    assert int(t77["spin10_commutator_order"]) == 2
    assert int(t77["so10_group_order"]) == 16
    assert int(t77["so10_center_order"]) == 4
    assert int(t77["ker_spin10_to_so10_order"]) == 2
    assert int(t77["pso10_q8_quotient_order"]) == 8
    assert float(t77["spin10_to_so10_homomorphism_err"]) == 0.0

    # Theorem 78 (Stage 10.2): Banked B1836 S301 Refinements (T-FRAME-MIRROR 16 Basis Pairs, Riley SL(2,C) Torsion, Bianchi E_{k,k})
    t78 = sc["theorem78_b1836_t_frame_mirror_step2_parities_riley_sl2_torsion_and_explicit_cuspidal_cohomology"]
    assert "B1821_the_frames_mirror_symmetry_in_re_tau" in t78["seen_first"]
    assert "FORCED-BY-MAIN" in t78["claim_labels_and_scopes"]["t_frame_mirror_step2_and_16_basis_pairs"]
    assert "FORCED-BY-MAIN" in t78["claim_labels_and_scopes"]["b47_torsion_and_riley_sl2_polynomial"]
    assert "plain_english_elaboration" in t78
    assert int(t78["basis_pair_violations_with_channel_signs"]) == 0
    assert int(t78["basis_pair_violations_without_channel_signs"]) == 8
    assert float(t78["riley_sl2_torsion_err"]) < 1e-14
    assert t78["m004_bianchi_h1_dims_k0_to_3"] == [1, 1, 1, 1]
    assert t78["m004_bianchi_h1_cusp_dims_k0_to_3"] == [0, 0, 0, 0]
    assert int(t78["dim_h1_parabolic_ad_q8"]) == 0

    # Theorem 79 (Stage 10.3): P-676 Framework Authority, B1834 S301c 44-Joint Scoreboard Vocabulary, & P-585/P-638 Blinding Gate
    t79 = sc["theorem79_p676_authority_compliance_scoreboard_vocabulary_and_held_out_blinding_gate"]
    assert "GENESIS.md" in t79["seen_first"]
    assert "MATH" in t79["claim_labels_and_scopes"]["p676_framework_authority_and_scoreboard_vocabulary"]
    assert "MATH" in t79["claim_labels_and_scopes"]["p676_p624_held_out_target_blinding_gate"]
    assert "plain_english_elaboration" in t79
    assert int(t79["s301c_scoreboard_state"]["frame_b_complete_picture_borrowed_joints_at_s301c"]) == 44
    assert int(t79["unsealed_p585_p638_test_assertions_count"]) == 0
    assert t79["sample_p624_sha256_seal_valid"] is True

    # Theorem 80 (Stage 10.4): Zero-Trust Hostile-Referee Gate for Stage 10 & Module-Wide Non-Literal Guardrail Audit
    t80 = sc["theorem80_zero_trust_hostile_referee_stage10_and_all_referees_independent_upgrade"]
    assert "GENESIS.md" in t80["seen_first"]
    assert "MATH" in t80["claim_labels_and_scopes"]["stage10_theorems_77_to_79_verification"]
    assert "MATH" in t80["claim_labels_and_scopes"]["zero_literal_guardrail_flags_across_entire_module"]
    assert "plain_english_elaboration" in t80
    rc80 = t80["referee_independent_counterchecks"]
    assert float(rc80["independent_mpmath_riley_torsion_err"]) < 1e-25
    assert float(rc80["independent_mpmath_step2_offdiag_err"]) < 1e-25
    assert float(rc80["independent_fresh_haar_invariance_err_t80"]) < 1e-13
    assert int(rc80["literal_true_in_any_guardrail_compliance_block"]) == 0
    assert t80["all_six_guardrails_passed"] is True

    # Theorem 81 (Stage 11.1): Spectral Hurwitz-Epstein Zeta Renormalization of A07/A09 Small-Cut Norm Addressing P-421
    t81 = sc["theorem81_zagier_rankin_selberg_spectral_zeta_renormalization_of_a07_small_cut_norm"]
    assert "B1654_the_norm_of_the_boundary_class" in t81["seen_first"]
    assert "MATH" in t81["claim_labels_and_scopes"]["spectral_hurwitz_epstein_zeta_derivation_of_small_cut_norm"]
    assert "MATH" in t81["claim_labels_and_scopes"]["p421_a07_a09_geometric_ground"]
    assert "plain_english_elaboration" in t81
    assert float(t81["max_spectral_zeta_vs_closed_form_cA_err"]) < 1e-14
    assert float(t81["spectral_zeta_o_exp_minus_2L_coeff"]) == 0.0
    assert float(t81["hard_disk_o_exp_minus_2L_at_l2"]) > 0.05

    # Theorem 82 (Stage 11.2): Hecke-Regularized Cross-Kernel Principal Value & W147 20-Line Density Higgs Pairing (chat1 9a6847e7f)
    t82 = sc["theorem82_hecke_regularized_cross_kernel_principal_value_and_w147_density_higgs_pairing"]
    assert "B1651_where_a_higgs_can_couple" in t82["seen_first"]
    assert "MATH" in t82["claim_labels_and_scopes"]["cross_kernel_weierstrass_pv_and_hecke_modular_covariance"]
    assert "MATH" in t82["claim_labels_and_scopes"]["w147_density_higgs_pairing_and_a05_scope"]
    assert "plain_english_elaboration" in t82
    assert float(t82["elliptic_product_wp_identity_err"]) < 1e-25
    assert float(t82["pv_closed_forms_agreement_err"]) < 1e-25
    assert float(t82["hecke_pv_modular_s_covariance_err"]) < 1e-25
    assert float(t82["hard_disk_s_covariance_violation"]) > 5.0
    assert int(t82["total_census_lines_count"]) == 256
    assert int(t82["w147_p3_exception_lines_count"]) == 20
    assert int(t82["non_exception_census_lines_count"]) == 236

    # Theorem 83 (Stage 11.3): P-670 Exact theta_2 Branch Restoration & Analytical Bernoulli Supertrace Theorem for B1836 c29b
    t83 = sc["theorem83_p670_exact_theta2_branch_restoration_and_c29b_bernoulli_supertrace_theorem"]
    assert "B1667_the_canonical_cusp" in t83["seen_first"]
    assert "MATH" in t83["claim_labels_and_scopes"]["p670_exact_theta2_sheet_restoration_across_all_re_tau"]
    assert "MATH" in t83["claim_labels_and_scopes"]["c29b_analytical_bernoulli_supertrace_theorem"]
    assert "plain_english_elaboration" in t83
    assert float(t83["p670_sheet_factor_formula_err"]) < 1e-25
    assert float(t83["p670_restored_series_err"]) < 1e-25
    assert float(t83["p670_repaired_t_step_across_cut_err"]) < 1e-25
    assert t83["sm_per_gen_bernoulli_sum_at_2_5"] == "-7/10"
    assert t83["sm_per_gen_bernoulli_sum_at_1_5"] == "-3/10"
    assert abs(float(t83["dy_analytical_plus_at_y12"]) - 12.64637779) < 1e-6
    assert abs(float(t83["dy_analytical_minus_at_y12"]) - (-13.74300050)) < 1e-6
    assert float(t83["c29b_table_plus_rounding_err"]) < 1e-12
    assert float(t83["c29b_table_minus_rounding_err"]) < 1e-12

    # Theorem 84 (Stage 11.4): Zero-Trust Hostile-Referee Gate for Stage 11 & P-676 Total Compliance
    t84 = sc["theorem84_zero_trust_hostile_referee_stage11_and_p676_total_compliance_gate"]
    assert "GENESIS.md" in t84["seen_first"]
    assert "MATH" in t84["claim_labels_and_scopes"]["stage11_theorems_81_to_83_verification"]
    assert "MATH" in t84["claim_labels_and_scopes"]["p421_p670_c29b_and_chat1_density_higgs_synthesis"]
    assert "plain_english_elaboration" in t84
    rc84 = t84["referee_independent_counterchecks"]
    assert float(rc84["independent_mpmath_hurwitz_err"]) < 1e-25
    assert float(rc84["independent_mpmath_p670_err"]) < 1e-25
    assert float(rc84["independent_fresh_haar_invariance_err_t84"]) < 1e-13
    assert float(rc84["max_precision_err_stage11"]) < 1e-13
    assert t84["all_six_guardrails_passed"] is True

    # Theorem 85 (Stage 12.1): B1837 c2 Complete Banked m004 Torsion Dictionary, S304 D4 Spin(10)->PSO(10)=Q_8 Lift, & P-683 Single-Source L_2
    t85 = sc["theorem85_b1837_c2_banked_m004_torsion_dictionary_and_s304_d4_spin10_q8_lift"]
    assert "B1667_the_canonical_cusp" in t85["seen_first"]
    assert "FORCED-BY-MAIN" in t85["claim_labels_and_scopes"]["b1837_c2_exact_adjoint_wada_laurent_polynomial"]
    assert "FORCED-BY-MAIN" in t85["claim_labels_and_scopes"]["s304_d4_spin10_to_pso10_q8_kernel_lift"]
    assert "MATH" in t85["claim_labels_and_scopes"]["p683_single_source_l2_and_zero_np_interp"]
    assert "plain_english_elaboration" in t85
    assert float(t85["wada_laurent_circle_err"]) < 1e-13
    assert float(t85["w_ad_omega_6sqrt3_err"]) < 1e-13
    assert float(t85["w_ad_minus1_14_err"]) < 1e-13
    assert float(t85["w_ad_longitude_3_err"]) < 1e-11
    assert float(t85["w_ab_4_over_sqrt3_err"]) < 1e-14
    assert t85["w_sl2_holonomy_tuple"] == (2, 5, 6)
    assert float(t85["riley_sl2_rel_err"]) < 1e-14
    assert t85["withdrawn_4_minus_2sqrt3"] is True
    assert t85["withdrawn_m003_chirality"] is True
    assert t85["orders_quotient_2_0_d4"] == {1: 1, 2: 5, 4: 2}
    assert t85["orders_quotient_2_2_q8"] == {1: 1, 2: 1, 4: 6}
    assert float(t85["single_source_l2_err"]) < 1e-13
    assert int(t85["np_interp_call_count_in_toe_closure"]) == 0

    # Theorem 86 (Stage 12.2): B1837 c1 Order-10 First-Order Sigma_10 Jacobian & S303 P-682 11-Order Dictionary
    t86 = sc["theorem86_b1837_c1_first_order_sigma10_jacobian_and_s303_p682_eleven_order_dictionary"]
    assert "B1728_the_lines_order_as_a_quotient_of_hypercharge" in t86["seen_first"]
    assert "FORCED-BY-MAIN" in t86["claim_labels_and_scopes"]["b1837_c1_order10_transpose_and_first_order_sigma10_jacobian"]
    assert "FORCED-BY-MAIN" in t86["claim_labels_and_scopes"]["s303_p682_eleven_order_proportionality_dictionary"]
    assert "plain_english_elaboration" in t86
    assert float(t86["max_b1837_c1_transpose_err"]) < 1e-13
    assert float(t86["max_frechet_jacobian_err"]) < 1e-7
    assert float(t86["max_doubling_ratio_err"]) < 1e-6
    assert float(t86["max_sigma10_even_det_err"]) < 1e-11
    assert t86["orders_11_verified"] == [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 30]
    assert float(t86["p682_worst_predicted_hold_err"]) < 1e-13
    assert float(t86["p682_least_unpredicted_fail_dev"]) > 0.02
    assert int(t86["p682_unpredicted_holds_count"]) == 0

    # Theorem 87 (Stage 12.3): S304 B1838 Inradius Bound, D1 Channel Horocycle Split, & D2/chat1 20ece78d5 Radius Scaling
    t87 = sc["theorem87_s304_b1838_inradius_bound_channel_horocycle_split_and_chat1_20ece78d5_radius_scaling"]
    assert "B1654_the_norm_of_the_boundary_class" in t87["seen_first"]
    assert "FORCED-BY-MAIN" in t87["claim_labels_and_scopes"]["s304_hurwitz_minimal_subtraction_degeneracy"]
    assert "FORCED-BY-MAIN" in t87["claim_labels_and_scopes"]["s304_inradius_bound_and_d1_channel_horocycle_split"]
    assert "FORCED-BY-MAIN" in t87["claim_labels_and_scopes"]["s304_d2_and_chat1_20ece78d5_scaled_radius_s_covariance"]
    assert "plain_english_elaboration" in t87
    assert float(t87["l_ms_channel_spread_err"]) < 1e-14
    assert float(t87["max_cusp_area_law_err"]) < 1e-14
    assert float(t87["min_exp_minus_lmax"]) > 0.5005
    assert float(t87["delta_l_split_jk_minus_1i"]) < 0.0
    assert float(t87["scaled_eps_s_covariance_err"]) < 1e-28
    assert float(t87["fixed_eps_s_covariance_violation"]) > 0.05
    assert float(t87["rho_anomaly_zero_err"]) < 1e-15

    # Theorem 88 (Stage 12.4): Complete P-683 & P-684 Compliance Resolution & Zero-Trust Stage 12 Referee Gate
    t88 = sc["theorem88_p684_complete_compliance_resolution_and_zero_trust_stage12_referee_gate"]
    assert "GENESIS.md" in t88["seen_first"]
    assert "MATH" in t88["claim_labels_and_scopes"]["stage12_theorems_85_to_87_verification"]
    assert "MATH" in t88["claim_labels_and_scopes"]["p683_and_p684_complete_compliance_gate"]
    assert "plain_english_elaboration" in t88
    assert int(t88["p684_unsealed_test_assertions_count"]) == 0
    assert int(t88["p684_unsealed_relay_lines_count"]) == 0
    assert t88["p684_positive_control_scanner_verified"] is True
    assert int(t88["p683_np_interp_call_count"]) == 0
    rc88 = t88["referee_independent_counterchecks"]
    assert float(rc88["independent_mpmath_w_ad_err"]) < 1e-30
    assert float(rc88["independent_mpmath_cusp_area_err"]) < 1e-30
    assert float(rc88["independent_fresh_haar_invariance_err_t88"]) < 1e-13
    assert float(rc88["max_precision_err_stage12"]) < 1e-6
    assert t88["all_six_guardrails_passed"] is True

    # Theorem 89 (Stage 13.1): Analytic Proof of B1839's Control C1 Higgs-Twist Norm Law & 170-Class Partition of 266 Lines
    t89 = sc["theorem89_b1839_higgs_twist_norm_law_and_170_class_partition_theorem"]
    assert "B1839_the_end_card" in t89["seen_first"]
    assert "FORCED-BY-MAIN" in t89["claim_labels_and_scopes"]["b1839_c1_four_sector_horoball_norm_identity"]
    assert "MATH" in t89["claim_labels_and_scopes"]["b1713_266_lines_to_170_higgs_twist_classes_theorem"]
    assert "plain_english_elaboration" in t89
    assert int(t89["total_lines_count"]) == 266
    assert int(t89["higgs_twist_classes_count"]) == 170
    assert t89["class_size_distribution"] == {1: 156, 5: 4, 9: 10}
    assert t89["t_shift_bijection_verified"] is True
    assert float(t89["frobenius_al2_be2_err"]) < 1e-14
    assert float(t89["frobenius_odd_max_err"]) < 1e-14
    assert float(t89["max_horocycle_inversion_err"]) < 1e-12
    assert float(t89["max_four_sector_horoball_norm_err"]) < 1e-12
    assert float(t89["within_class_rel_err"]) < 1e-12
    assert float(t89["between_class_abs_diff"]) > 0.5

    # Theorem 90 (Stage 13.2): Liouville Second-Laurent Identity & Completed-Square Horoball Asymptotics to O(e^{-6 L_h})
    t90 = sc["theorem90_b1839_completed_square_horoball_asymptotics_and_lame_accessory_coupling"]
    assert "B1839_the_end_card" in t90["seen_first"]
    assert "MATH" in t90["claim_labels_and_scopes"]["liouville_second_laurent_identity_a1_from_a0_and_wp"]
    assert "MATH" in t90["claim_labels_and_scopes"]["completed_square_horoball_norm_asymptotics_to_o_exp_minus_6Lh"]
    assert "plain_english_elaboration" in t90
    assert float(t90["liouville_a1_identity_err"]) < 1e-11
    assert float(t90["rem_o4_at_delta_3"]) < 1e-9
    assert float(t90["rem_o4_at_delta_4"]) < 5e-11
    assert float(t90["o4_improvement_factor_at_delta_3"]) > 400.0
    assert float(t90["min_crossing_delta"]) > 0.14
    assert float(t90["max_crossing_delta"]) < 0.32

    # Theorem 91 (Stage 13.3): S305a P-665 Data-Free Takagi Basis Invariance & 3-Fold Cover M_3 -> m004 Wada Factorization
    t91 = sc["theorem91_s305a_p665_basis_invariant_seesaw_spectrum_and_m3_cover_wada_factorization"]
    assert "B1837_agy_stages_8_9_and_the_density_higgs" in t91["seen_first"]
    assert "FORCED-BY-MAIN" in t91["claim_labels_and_scopes"]["s305a_p665_data_free_takagi_invariance_vs_rhs_overlap"]
    assert "MATH" in t91["claim_labels_and_scopes"]["m3_cover_wada_polynomial_chebyshev_factorization"]
    assert "plain_english_elaboration" in t91
    assert float(t91["max_takagi_sv_haar_err"]) < 1e-13
    assert float(t91["max_lr_overlap_rhs_variation"]) > 0.1
    assert float(t91["max_m3_w_ad_factorization_err"]) < 1e-12
    assert float(t91["max_m3_w_sl2_factorization_err"]) < 1e-12
    assert abs(float(t91["m3_ad_nontrivial_sheet_prod_108"]) - 108.0) < 1e-12
    assert abs(float(t91["m3_ad_full_three_sheet_prod_324"]) - 324.0) < 1e-12
    assert abs(float(t91["m3_sl2_prod_at_t1_50"]) - 50.0) < 1e-12
    assert abs(float(t91["m3_sl2_prod_at_tminus1_54"]) - 54.0) < 1e-12

    # Theorem 92 (Stage 13.4): Zero-Trust Hostile-Referee Gate for Stage 13, B1839 Horoball Laws, and P-684 Salted Seal
    t92 = sc["theorem92_zero_trust_hostile_referee_stage13_b1839_and_s305a_gate"]
    assert "B1839_the_end_card" in t92["seen_first"]
    assert "MATH" in t92["claim_labels_and_scopes"]["stage13_theorems_89_to_91_verification"]
    assert "MATH" in t92["claim_labels_and_scopes"]["p684_salted_hiding_and_binding_seal_verification"]
    assert "plain_english_elaboration" in t92
    assert t92["seal_is_salted_and_hiding"] is True
    rc92 = t92["referee_independent_counterchecks"]
    assert float(rc92["independent_mpmath_m3_wada_err"]) < 1e-30
    assert float(rc92["independent_fresh_haar_invariance_err_t92"]) < 1e-13
    assert float(rc92["max_precision_err_stage13"]) < 1e-9
    assert t92["all_six_guardrails_passed"] is True

    # Theorem 93 (Stage 14.1): P-663 / P-689 Direct B1667 L_2 Conversion B08 & Exact Contour-Free Two-Twist B1656 Laurent Theorem
    t93 = sc["theorem93_p663_b08_direct_b1667_l2_conversion_and_exact_two_twist_b1656_laurent_theorem"]
    assert "B1840_the_principled_ends" in t93["seen_first"]
    assert "FORCED-BY-MAIN" in t93["claim_labels_and_scopes"]["p663_p689_b08_direct_b1667_runtime_l2_conversion"]
    assert "MATH" in t93["claim_labels_and_scopes"]["exact_contour_free_two_twist_b1656_laurent_theorem"]
    assert "plain_english_elaboration" in t93
    assert float(t93["max_b1667_im_trace_err"]) < 1e-12
    assert float(t93["max_abs_diff_c_vs_b1667_solver"]) < 1e-12
    assert float(t93["max_abs_diff_l2_vs_b1667_runtime"]) < 2e-11
    assert int(t93["legacy_l2_literals_remaining_count"]) == 0
    assert t93["b08_joint_converted_across_16_rows"] is True
    assert float(t93["max_two_twist_R_err"]) < 1e-14
    assert float(t93["max_two_twist_a0_err"]) < 1e-12
    assert float(t93["max_two_twist_a1_err"]) < 1e-12

    # Theorem 94 (Stage 14.2): B1840 Principled Ends E_1..E_5 Registration & B1667 Weierstrass Half-Period O(e^{-4 L_h}) Law
    t94 = sc["theorem94_b1840_principled_ends_e1_to_e5_and_b1667_weierstrass_half_period_o4_law"]
    assert "B1840_the_principled_ends" in t94["seen_first"]
    assert "MATH" in t94["claim_labels_and_scopes"]["b1840_principled_ends_e1_to_e5_registration"]
    assert "MATH" in t94["claim_labels_and_scopes"]["b1667_weierstrass_half_period_o4_horoball_law"]
    assert "plain_english_elaboration" in t94
    assert len(t94["principled_ends_table"]) == 5
    assert float(t94["e4_incircle_tangency_err"]) < 1e-12
    assert t94["e4_strictly_inside_incircle_at_zero"] is True
    assert float(t94["weierstrass_sum_zero_err"]) < 1e-14
    assert float(t94["max_b1667_a1_half_period_err"]) < 1e-12
    assert float(t94["rel_o4_errs_by_r"][2]) < 1e-8

    # Theorem 95 (Stage 14.3): P-686 S3 GAP1 Functional Independence Proof & Complete 13-Order Unification Dictionary
    t95 = sc["theorem95_p686_s3_gap1_independence_proof_and_complete_13_order_unification_dictionary"]
    assert "B1840_the_principled_ends" in t95["seen_first"]
    assert "MATH" in t95["claim_labels_and_scopes"]["p686_s3_gap1_condition4_functional_independence"]
    assert "FORCED-BY-MAIN" in t95["claim_labels_and_scopes"]["complete_13_order_two_sided_unification_dictionary"]
    assert "plain_english_elaboration" in t95
    assert t95["disjoint_hypercharge_and_colour_sectors"] is True
    assert int(t95["jacobian_rank"]) == 2
    assert float(t95["abs_det_jacobian"]) > 0.1
    assert float(t95["off_diagonal_decoupling_err"]) < 1e-12
    assert int(t95["shared_tau_jacobian_rank"]) == 2
    assert float(t95["shared_tau_abs_det_jacobian"]) > 4.0
    assert t95["orders_13_tested"] == [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 30]
    assert float(t95["n7_lep_up_transpose_err"]) < 1e-14
    assert float(t95["n9_lep_symmetric_err"]) < 1e-14
    assert float(t95["worst_predicted_hold_err"]) < 1e-14
    assert float(t95["least_unpredicted_fail_dev"]) > 0.02
    assert int(t95["unpredicted_holds_count"]) == 0

    # Theorem 96 (Stage 14.4): Zero-Trust Hostile-Referee Gate for Stage 14 & Semantic AST Data-Flow P-684 Blinding Scanner
    t96 = sc["theorem96_zero_trust_stage14_referee_and_ast_semantic_p684_blinding_gate"]
    assert "B1840_the_principled_ends" in t96["seen_first"]
    assert "MATH" in t96["claim_labels_and_scopes"]["stage14_theorems_93_to_95_verification"]
    assert "MATH" in t96["claim_labels_and_scopes"]["ast_semantic_p684_blinding_gate_with_positive_control"]
    assert "plain_english_elaboration" in t96
    assert int(t96["ast_semantic_flagged_assertions_count"]) == 0
    assert t96["positive_control_caught_indirect_leak"] is True
    rc96 = t96["referee_independent_counterchecks"]
    assert float(rc96["independent_mpmath_stage14_err"]) < 1e-30
    assert float(rc96["independent_fresh_haar_invariance_err_t96"]) < 1e-13
    assert float(rc96["max_precision_err_stage14"]) < 2e-11
    assert t96["all_six_guardrails_passed"] is True

    # Theorem 97 (Stage 15.1): Liouville Elliptic Uniqueness Lemma L1 for Higgs-Twist Law & B1840 E_4 Universal Area-4 Horocycle
    t97 = sc["theorem97_liouville_uniqueness_higgs_twist_law_and_b1840_e4_universal_area4_horocycle"]
    assert "B1840_the_principled_ends" in t97["seen_first"]
    assert "FORCED-BY-MAIN" in t97["claim_labels_and_scopes"]["liouville_uniqueness_lemma_l1_for_higgs_twist_law"]
    assert "FORCED-BY-MAIN" in t97["claim_labels_and_scopes"]["b1840_e4_universal_area4_fuchsian_horocycle"]
    assert "plain_english_elaboration" in t97
    assert float(t97["max_liouville_elliptic_periodicity_err"]) < 1e-13
    assert float(t97["max_liouville_quotient_unity_err"]) < 1e-13
    assert float(t97["mismatched_sum_quotient_variation"]) > 0.5
    assert float(t97["min_a_cusp_across_54_pts"]) >= 4.0
    assert float(t97["max_e4_delta_identity_err"]) < 1e-14
    assert t97["e4_overlaps_single_horocycle_crossing_band"] is True

    # Theorem 98 (Stage 15.2): Single-Trajectory UV-to-IR Modular RG Flow & KK Threshold Cancellation of Downward Xing-Zhou I_t
    t98 = sc["theorem98_single_trajectory_uv_ir_modular_rg_flow_and_kk_threshold_xing_zhou_closure"]
    assert "B1788_the_closed_form_of_the_exponents" in t98["seen_first"]
    assert "MATH" in t98["claim_labels_and_scopes"]["single_trajectory_uv_ir_modular_rg_flow"]
    assert "MATH" in t98["claim_labels_and_scopes"]["kk_modular_threshold_xing_zhou_cancellation"]
    assert "plain_english_elaboration" in t98
    assert str(t98["im_tau_uv_strip_endpoint"]).startswith("sha256:")
    assert float(t98["uv_ir_modular_ode_roundtrip_err"]) < 1e-13
    assert float(t98["kk_xing_zhou_up_cancellation_err"]) < 1e-14

    # Theorem 99 (Stage 15.3): S305d P-693 One-Higgs Reading-Triple Law & SU(2)_L-Invariant M_3 Cover Trace
    t99 = sc["theorem99_p693_one_higgs_reading_triple_and_su2l_invariant_m3_cover_self_energy_trace"]
    assert "B1839_the_end_card" in t99["seen_first"]
    assert "FORCED-BY-MAIN" in t99["claim_labels_and_scopes"]["s305d_p693_one_higgs_reading_triple_law"]
    assert "MATH" in t99["claim_labels_and_scopes"]["su2l_invariant_m3_cover_self_energy_trace_and_c_gj"]
    assert "plain_english_elaboration" in t99
    assert t99["one_higgs_reading_triple"] == ["S~", "S", "S"]
    assert t99["p693_reading_rule_verified"] is True
    assert int(t99["tr_m3_hypercharge_total"]) == 402
    assert int(t99["q2_down_exact"]) == 5
    assert int(t99["c_gj_exact"]) == 3
    assert float(t99["max_su2l_doublet_commutator_err"]) < 1e-15

    # Theorem 100 (Stage 15.4): Unique Parameter-Free 1-Loop Bulk+Boundary Radiative h_i Lift Eliminating the 1/42 vs 1/45 Menu
    t100 = sc["theorem100_unique_one_loop_sigma10_breaking_radiative_hi_lift_eliminating_rational_menu"]
    assert "B1656_the_electrons_zero" in t100["seen_first"]
    assert "MATH" in t100["claim_labels_and_scopes"]["aps_bulk_boundary_unique_29_over_1260_radiative_lift"]
    assert "plain_english_elaboration" in t100
    assert t100["delta_unique_1loop_fraction"] == "29/1260"
    assert float(t100["exact_fraction_err"]) == 0.0
    assert int(t100["discrete_menu_choices_remaining"]) == 0
    assert int(t100["continuous_parameters_used"]) == 0
    assert float(t100["max_haar_invariance_err"]) < 1e-13

    # Theorem 101 (Stage 15.5): Parameter-Free Spin(10) 10_S (+) 126_bar_S Clebsch Seesaw Lock & Two-Tier SM-vs-Gravity Firewall
    t101 = sc["theorem101_spin10_10_plus_126_clebsch_seesaw_lock_and_two_tier_sm_gravity_separation"]
    assert "B1799_the_neutrinos_self_pairing_at_the_canonical_end" in t101["seen_first"]
    assert "MATH" in t101["claim_labels_and_scopes"]["spin10_10_plus_126_clebsch_seesaw_lock"]
    assert "MATH" in t101["claim_labels_and_scopes"]["two_tier_sm_vs_chern_simons_gravity_firewall"]
    assert "plain_english_elaboration" in t101
    assert t101["spin10_tensor_decomp_verified"] is True
    assert t101["xi_clebsch_lock_fraction"] == "1/5"
    assert float(t101["clebsch_b_minus_l_err"]) < 1e-15
    assert int(t101["adjustable_seesaw_parameters_count"]) == 0
    assert float(t101["seesaw_symmetry_err"]) < 1e-15
    assert float(t101["max_seesaw_haar_err"]) < 1e-13
    assert int(t101["tier1_core_sm_count"]) == 19
    assert int(t101["tier2_chern_simons_gravity_count"]) == 4
    assert int(t101["tier1_gravity_contamination_count"]) == 0
    assert t101["tier2_feeds_into_tier1"] is False

    # Theorem 102 (Stage 15.6): Zero-Trust Hostile Referee Gate for Stage 15, Theorem 59 W_Ad(-1)=-14 Fix, Openable Commitment, & Full-Repo AST Blinding Scanner
    t102 = sc["theorem102_zero_trust_stage15_referee_and_full_repo_ast_openable_commitment_gate"]
    assert "B1840_the_principled_ends" in t102["seen_first"]
    assert "MATH" in t102["claim_labels_and_scopes"]["stage15_theorems_97_to_101_and_t59_w_ad_verification"]
    assert "MATH" in t102["claim_labels_and_scopes"]["p692_openable_commitment_and_full_repo_ast_blinding_gate"]
    assert "plain_english_elaboration" in t102
    assert t102["t59_in_place_w_ad_repaired"] is True
    assert float(t102["t59_w_ad_minus1_err"]) < 1e-14
    assert t102["commitment_is_hiding_and_openable"] is True
    assert int(t102["python_files_ast_scanned_count"]) >= 15
    assert int(t102["full_repo_flagged_assertions_count"]) == 0
    assert int(t102["full_repo_flagged_relay_lines_count"]) == 0
    assert t102["positive_control_caught_indirect_leak"] is True
    rc102 = t102["referee_independent_counterchecks"]
    assert float(rc102["independent_mpmath_stage15_err"]) < 1e-30
    assert float(rc102["independent_fresh_haar_invariance_err_t102"]) < 1e-13
    assert float(rc102["max_precision_err_stage15"]) < 1e-12
    assert t102["all_six_guardrails_passed"] is True

    # Theorem 103 (Stage 16.1): P-694 Milne-Thurston 3+1D Expanding Spacetime Clock & Dynamical T-NORM Isotropy
    t103 = sc["theorem103_p694_milne_thurston_3plus1d_spacetime_clock_and_dynamical_tnorm_isotropy"]
    assert "B1822_t_norm_on_the_frames_matter" in t103["seen_first"]
    assert "MATH" in t103["claim_labels_and_scopes"]["p694_milne_thurston_3plus1d_expanding_spacetime_from_sl2c_branch_density"]
    assert "MATH" in t103["claim_labels_and_scopes"]["b1822_p693_n4_dynamical_markov_relaxation_to_isotropic_tnorm"]
    assert "plain_english_elaboration" in t103
    assert float(t103["single_state_det_null_err"]) < 1e-15
    assert abs(float(t103["tau_clock_step1"]) - 3.0) < 1e-14
    assert float(t103["wronskian_det_identity_err"]) < 1e-14
    assert float(t103["max_sl2c_lorentz_invariance_err"]) < 1e-13
    assert t103["clock_strictly_increasing"] is True
    assert float(t103["sympy_robertson_walker_metric_err"]) == 0.0
    assert int(t103["g96_group_order"]) == 96
    assert float(t103["max_g96_unitarity_err"]) < 1e-14
    assert int(t103["unit_eigenvalue_multiplicity"]) == 1
    assert float(t103["traceless_spectral_radius_err"]) < 1e-14
    assert float(t103["tnorm_step40_isotropy_err"]) < 1e-11
    assert int(t103["eliminated_tnorm_continuous_params"]) == 8

    # Theorem 104 (Stage 16.2): Direct G_192 Peter-Weyl 12D Gauge Orthogonality & Frustrated Plaquette Curvature
    t104 = sc["theorem104_direct_g192_peter_weyl_12d_gauge_orthogonality_and_plaquette_curvature"]
    assert "B1822_t_norm_on_the_frames_matter" in t104["seen_first"]
    assert "MATH" in t104["claim_labels_and_scopes"]["gap6_f_mc_direct_g192_peter_weyl_12d_sm_gauge_orthogonality"]
    assert "MATH" in t104["claim_labels_and_scopes"]["non_vanishing_frustrated_plaquette_yang_mills_curvature"]
    assert "plain_english_elaboration" in t104
    assert int(t104["g192_group_order"]) == 192
    assert int(t104["g768_full_group_order"]) == 768
    assert float(t104["plaquette_su3_norm_err"]) < 1e-14
    assert float(t104["plaquette_su2_norm_err"]) < 1e-14
    assert float(t104["max_trace_orthonormality_err"]) < 1e-15
    assert int(t104["peter_weyl_lie_algebra_rank"]) == 12
    assert float(t104["max_off_diag_killing_err"]) < 1e-14
    assert float(t104["su3_mean_stiffness_err"]) < 1e-14
    assert float(t104["su2_stiffness_err"]) < 1e-14
    assert float(t104["u1_stiffness_err"]) < 1e-14
    assert float(t104["bare_weak_ratio_err"]) < 1e-14

    # Theorem 105 (Stage 16.3): Tensor-Product Separation of 4_parity = 3_c (+) 1_l from Pillowcase Flavour & B915 Pati-Salam Scale
    t105 = sc["theorem105_pati_salam_4parity_colour_lepton_vs_pillowcase_flavour_tensor_separation"]
    assert "B1617_the_weave_at_tau_omega" in t105["seen_first"]
    assert "B915_the_crossing" in t105["seen_first"]
    assert "MATH" in t105["claim_labels_and_scopes"]["b1617_b1618_tensor_product_resolution_4parity_colour_lepton_vs_pillowcase_flavour"]
    assert "HYPOTHESIS" in t105["claim_labels_and_scopes"]["b915_two_loop_rge_benchmark_and_pati_salam_4_to_3_plus_1_matching_scale"]
    assert "plain_english_elaboration" in t105
    assert float(t105["jacobi_null_cone_err"]) < 1e-14
    assert t105["flavour_3_generations_distinct"] is True
    assert float(t105["max_gauge_flavour_commutator_err"]) < 1e-14
    assert float(t105["max_8fold_gauge_degeneracy_spread"]) < 1e-14
    assert float(t105["max_haar_scrambling_err"]) < 1e-12
    assert float(t105["b915_literature_benchmark_rel_err"]) < 0.005
    assert float(t105["pati_salam_matching_residual"]) < 1e-12
    assert int(t105["priced_pati_salam_threshold_continuous_params"]) == 1

    # Theorem 106 (Stage 16.4): P-694 Spontaneous Horizon Freeze-Out, Blind Transfer Census, & Stage 16 Referee Gate
    t106 = sc["theorem106_p694_spontaneous_horizon_freezeout_blind_transfer_census_and_stage16_referee_gate"]
    assert "B1840_the_principled_ends" in t106["seen_first"]
    assert "MATH" in t106["claim_labels_and_scopes"]["p694_spontaneous_horizon_freezeout_on_symmetric_sl2z_walks"]
    assert "MATH" in t106["claim_labels_and_scopes"]["exhaustive_blind_transfer_operator_census_and_stage16_referee_gate"]
    assert "plain_english_elaboration" in t106
    assert abs(float(t106["ensemble_mean_chiral_rate"])) < 0.02
    assert float(t106["horizon_freezeout_fraction"]) > 0.95
    assert float(t106["spontaneous_branch_separation"]) > 0.45
    assert int(t106["k2_total_operators"]) == 21
    assert int(t106["k2_nondegenerate_count"]) == 8
    assert float(t106["honest_k2_selection_bits"]) == 1.0
    assert int(t106["k3_total_operators"]) == 35
    assert int(t106["k3_nondegenerate_count"]) == 24
    assert float(t106["honest_k3_selection_bits"]) == 3.0
    assert int(t106["flagged_ast_assertions"]) == 0
    rc106 = t106["referee_independent_counterchecks"]
    assert float(rc106["independent_mpmath_stage16_err"]) < 1e-30
    assert float(rc106["independent_fresh_haar_invariance_err_t106"]) < 1e-13
    assert float(rc106["max_precision_err_stage16"]) < 1e-11
    assert t106["all_six_guardrails_passed"] is True

    # Theorem 107 (Stage 17.1): 1-Loop Modular pi-Cancellation Theorem & Algebraic Q(sqrt(3)) RG Shifts
    t107 = sc["theorem107_loop_modular_pi_cancellation_and_exact_algebraic_rg_shifts"]
    assert "B1696_tau_is_the_cusp_shape" in t107["seen_first"]
    assert "MATH" in t107["claim_labels_and_scopes"]["one_loop_modular_pi_cancellation_theorem"]
    assert "MATH" in t107["claim_labels_and_scopes"]["root_field_q_sqrt3_algebraicity_of_1loop_shifts"]
    assert "plain_english_elaboration" in t107
    assert float(t107["sympy_1loop_pi_cancellation_residual"]) == 0.0
    assert t107["pi_absent_at_1loop"] is True
    assert t107["two_loop_retains_one_inverse_pi"] is True
    assert float(t107["cusp_quarter_equals_im_omega_err"]) == 0.0
    assert t107["algebraic_shifts_verified"] is True
    assert float(t107["max_num_vs_sym_err"]) < 1e-14
    assert int(t107["selection_bits"]) == 0

    # Theorem 108 (Stage 17.2): Exact Electroweak Scale Cancellation in alpha_EM^{-1}(IR) - alpha_3^{-1}(mu_EW)
    t108 = sc["theorem108_exact_electroweak_scale_cancellation_in_em_minus_qcd_running"]
    assert "B1684_w59_on_main" in t108["seen_first"]
    assert "MATH" in t108["claim_labels_and_scopes"]["exact_bosonic_ew_and_qcd_beta_equality_at_ng3"]
    assert "MATH" in t108["claim_labels_and_scopes"]["exact_ln_mu_ew_cancellation_in_em_minus_qcd_running"]
    assert "plain_english_elaboration" in t108
    assert t108["unique_to_three_generations_for_nh1"] is True
    assert float(t108["bosonic_equals_qcd_at_ng3_err"]) == 0.0
    assert float(t108["em_minus_qcd_equals_qed_err"]) == 0.0
    assert float(t108["ln_mu_ew_derivative_err"]) == 0.0
    assert t108["ln_mu_ew_completely_cancelled"] is True
    assert float(t108["symbolic_formula_match_err"]) == 0.0
    assert int(t108["selection_bits"]) == 0

    # Theorem 109 (Stage 17.3): Exact Fermion & Higgs Cancellation in Pati-Salam 5*b_1 - 3*b_2 - 2*b_3 = 44
    t109 = sc["theorem109_exact_fermion_and_higgs_cancellation_in_pati_salam_beta_combination"]
    assert "B1601_the_common_point_is_the_geometry_mod_3" in t109["seen_first"]
    assert "MATH" in t109["claim_labels_and_scopes"]["exact_fermion_and_higgs_cancellation_in_pati_salam_beta"]
    assert "MATH" in t109["claim_labels_and_scopes"]["algebraic_1loop_pati_salam_invariant"]
    assert "plain_english_elaboration" in t109
    assert float(t109["fermion_coeff"]) == 0.0
    assert float(t109["higgs_coeff"]) == 0.0
    assert float(t109["su2_ym_contribution"]) == 22.0
    assert float(t109["su3_ym_contribution"]) == 22.0
    assert float(t109["b_ps_exact_value"]) == 44.0
    assert float(t109["pure_ym_equipartition_err"]) == 0.0
    assert float(t109["l_ps_pi_cancellation_err"]) == 0.0
    assert int(t109["selection_bits"]) == 0

    # Theorem 110 (Stage 17.4): Direct Pushback on S305f, Shared-Parameter GAP1 Proof, Unmasked RGE Proof, & Stage 17 Gate
    t110 = sc["theorem110_s305f_pushback_shared_parameter_gap1_proof_and_stage17_referee_gate"]
    assert "B1684_w59_on_main" in t110["seen_first"]
    assert "MATH" in t110["claim_labels_and_scopes"]["s305f_pushback1_shared_parameter_gap1_jacobian_proof"]
    assert "MATH" in t110["claim_labels_and_scopes"]["s305f_pushback2_unstructured_random_matrix_1loop_sm_yt_cancellation"]
    assert "FORCED-BY-MAIN" in t110["claim_labels_and_scopes"]["s305f_pushback3_p697_p698_and_law_map_verification"]
    assert "plain_english_elaboration" in t110
    assert int(t110["shared_tau_jacobian_rank"]) == 2
    assert float(t110["shared_tau_abs_det_jacobian"]) > 4.0
    assert float(t110["mpmath_shared_tau_det_agreement_err"]) < 1e-5
    assert float(t110["unstructured_random_matrix_yt_ratio_invariance_err"]) < 1e-8
    assert t110["durable_git_info_salt_present"] is True
    assert t110["p698_b08_solver_independent_closed"] is True
    assert int(t110["orders_13_count"]) == 13
    assert float(t110["haar_err_110"]) < 1e-13
    assert t110["all_six_guardrails_passed"] is True

    # Theorem 111 (Stage 18.1): Closed-Form SL(2, Z) 3x3 Generation Covariance, Level-4 S_4 Homomorphism, & Order-12 CRT Split
    t111 = sc["theorem111_closed_form_sl2z_generation_covariance_level4_s4_and_order12_crt_split"]
    assert "B1724_the_readings_covariance" in t111["seen_first"]
    assert "MATH" in t111["claim_labels_and_scopes"]["closed_form_sl2z_3x3_generation_covariance_theorem"]
    assert "MATH" in t111["claim_labels_and_scopes"]["level4_psl2_z4_s4_generation_group_and_order12_crt_independence"]
    assert "plain_english_elaboration" in t111
    assert float(t111["bilinear_tensor_identity_err"]) < 1e-14
    assert float(t111["max_entrywise_t_err"]) < 1e-12
    assert float(t111["max_entrywise_s_err"]) < 1e-12
    assert float(t111["max_s_weight_one_scale_err"]) < 1e-12
    assert float(t111["max_pseudoscalar_s_sign_err"]) < 1e-13
    assert int(t111["sl2_z6_order"]) == 144
    assert int(t111["sl2_z12_order"]) == 1152
    assert t111["crt_6_bijection"] is True
    assert t111["crt_12_bijection"] is True
    assert t111["level4_s4_homomorphism_verified"] is True
    assert int(t111["s4_group_order"]) == 24
    assert int(t111["selection_bits"]) == 0

    # Theorem 112 (Stage 18.2): Exact j vs k Theta-Block Interference Law, T-Duality Swap N_j <-> N_k, & B1839 norms.npz Audit
    t112 = sc["theorem112_exact_j_k_theta_interference_law_t_duality_swap_and_b1839_norms_audit"]
    assert "B1839_the_end_card" in t112["seen_first"]
    assert "MATH" in t112["claim_labels_and_scopes"]["exact_jk_theta_block_interference_and_t_duality_swap_law"]
    assert "FORCED-BY-MAIN" in t112["claim_labels_and_scopes"]["b1838_absolute_level_offsets_and_b1839_norms_npz_verification"]
    assert "plain_english_elaboration" in t112
    assert t112["offsets_recorded_correctly"] is True
    assert float(t112["rk_over_rj_minus_i_err"]) < 1e-13
    assert float(t112["cross_term_formula_err"]) < 1e-12
    assert float(t112["t_duality_jk_swap_rel_err"]) < 1e-11
    assert float(t112["generic_line_jk_rel_split"]) > 1e-3
    assert float(t112["symmetric_line_jk_rel_split"]) < 1e-12
    assert list(t112["b1839_norms_shape"]) == [223, 170, 22, 4]
    assert t112["b1839_norms_sha_verified"] is True
    assert int(t112["selection_bits"]) == 0

    # Theorem 113 (Stage 18.3): P-699 Hostile Referee Audit of B1841 & Independent Third-Opinion Check of B1839 norms.npz
    t113 = sc["theorem113_p699_hostile_referee_audit_of_b1841_and_b1839_independent_third_opinion"]
    assert "B1841_the_principled_ends_card" in t113["seen_first"]
    assert "FORCED-BY-MAIN" in t113["claim_labels_and_scopes"]["p699_pre_run_hostile_referee_audit_of_b1841"]
    assert "FORCED-BY-MAIN" in t113["claim_labels_and_scopes"]["independent_third_opinion_verification_of_b1839_norms_npz"]
    assert "plain_english_elaboration" in t113
    assert int(t113["apex_count_audited"]) == 223
    assert t113["strict_ordering_all_223"] is True
    assert float(t113["min_gap_e1_e4"]) > 1.0
    assert float(t113["min_gap_e4_e2"]) > 0.04
    assert float(t113["min_gap_e2_e3"]) > 0.035
    assert t113["all_b1841_hashes_verified"] is True
    assert int(t113["b1841_total_priced_rows"]) == 237272
    assert float(t113["max_third_opinion_rel_err"]) < 1e-12
    assert t113["b1839_c1_holds"] is True
    assert t113["b1839_c2_holds"] is True
    assert int(t113["selection_bits"]) == 0

    # Theorem 114 (Stage 18.4): P-688/P-699 Audit of B1842 Closure Instruments, C-T Vacuity Defect Fix, Owed nu Control, & Stage 18 Gate
    t114 = sc["theorem114_p688_p699_b1842_closure_instruments_audit_ct_defect_fix_and_stage18_gate"]
    assert "B1842_the_closure_instruments" in t114["seen_first"]
    assert "FORCED-BY-MAIN" in t114["claim_labels_and_scopes"]["b1842_controls_exact_ct_vacuity_defect_and_r_gen_t_fix"]
    assert "FORCED-BY-MAIN" in t114["claim_labels_and_scopes"]["p688_dirac_neutrino_higgs_twist_class_constancy_and_p611_budgets"]
    assert "plain_english_elaboration" in t114
    assert t114["ct_interior_points_collapse_to_same_tau"] is True
    assert float(t114["unpermuted_ct_boundary_rel_err"]) > 0.20
    assert float(t114["permuted_ct_boundary_rel_err"]) < 1e-11
    assert float(t114["nu_higgs_twist_class_constancy_err"]) < 1e-12
    assert float(t114["cx_max_rel_err"]) < 1e-9
    assert float(t114["cx_max_inv_err"]) < 1e-11
    assert float(t114["p611_budget_nats_ybyt"]) > 4.0
    assert float(t114["p611_budget_nats_r"]) > 3.5
    assert float(t114["haar_err_114"]) < 1e-13
    assert t114["all_six_guardrails_passed"] is True


























