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
    assert rep_fib.sample_sin_delta_CP < 0.10

    rep_cov = evaluate_operator_gate("FR-COV")
    assert rep_cov.passed is True
    assert rep_cov.clauses_passed == 4
    assert rep_cov.sample_Vub_over_Vtd < 1.0
    assert rep_cov.sample_sin_delta_CP > 0.50


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

    # Pillar 4: Inter-sector Yukawa unification (||R_down||_2 == ||R_lepton||_2 & m_b(M_Z)/m_tau(M_Z))
    unif = inter_sector_yukawa_unification()
    assert float(unif["b_tau_residue_norm_diff"]) < 1e-14
    assert abs(float(unif["uv_yb_over_ytau"]) - 1.005894) < 1e-4
    assert float(unif["rel_error_mb_over_mtau_MZ"]) < 0.01

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
    assert abs(float(tree["sin_delta_CP"]) - 0.9269) < 1e-2
    assert float(tree["b_tau_residue_norm_diff"]) < 1e-14

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

    # Step 3: Block III (PMNS & Weinberg LL (-3, -3) Pauli antisymmetry) and Block IV (m004 Ray-Singer gauge threshold)
    s3 = step3_pmns_and_m004_gauge_thresholds()
    b3 = s3["block_III_pmns"]
    assert float(b3["weinberg_LL_singlet_residue_abs"]) < 1e-15
    assert abs(float(b3["sin2_theta12_pred"]) - 0.3119) < 1e-3
    assert abs(float(b3["Ue2_sq_pred"]) - 0.3030) < 1e-3

    b4 = s3["block_IV_gauge_unification"]
    assert abs(float(b4["delta_alpha3_inv_RS_threshold"]) - (-7.0 * math.log(4.0 / math.sqrt(3.0)))) < 1e-12
    assert float(b4["rel_error_sin2_thetaW_MZ"]) < 0.006
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
    assert abs(float(t8["sin_delta_CP"]) - 0.9288) < 1e-2

    inter = t8["inter_sector_scales"]
    assert float(inter["rel_error_mb_over_mtau"]) < 0.002
    assert float(inter["rel_error_mt_over_mb"]) < 0.001

    pmns = t8["block_III_pmns"]
    assert float(pmns["weinberg_LL_singlet_residue_abs"]) < 1e-15
    assert pmns["is_frame_dependent_rhs_diagnostic_not_physical_pmns"] is True
    assert abs(float(pmns["sin2_theta12_pred"]) - 0.3098) < 1e-3

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
    assert float(pb["rel_error_sin2_thetaW_MZ"]) < 0.002      # +0.155%
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

    # Phase 2: Candidate Weinberg neutrino spectrum at tau_Golden
    p2 = sc["phase2_weinberg_neutrino_spectrum"]
    assert abs(float(p2["f10_b10_norm_sq_used"]) - 0.0214338) < 1e-5
    assert abs(float(p2["true_quarter_eta6_abs"]) - 0.0040921) < 1e-5
    assert float(p2["rel_error_m3_vs_sqrt_dm31"]) < 0.03      # +2.63% (51.43 vs 50.11 meV)
    assert float(p2["rel_error_m2_vs_sqrt_dm21"]) < 0.085     # -8.13% (7.91 vs 8.61 meV)
    assert p2["satisfies_cosmological_bound"] is True
    assert float(p2["sum_mnu_eV_pred"]) < 0.072               # 0.0596 eV < 0.072 eV

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

    # Phase 6: Diagnostic single-matrix PMNS overlap and Guardrail 3 right-handed rotation countercheck
    p6 = sc["phase6_complete_pmns_unitary_and_cp"]
    assert float(p6["rel_error_theta13_lr_deg"]) < 0.03       # 8.79 deg vs 8.54 deg (+2.95%)
    assert float(p6["rel_error_theta23_lr_deg"]) < 0.04       # 50.98 deg vs 49.1 deg (+3.82%)
    assert float(p6["rel_error_delta_CP_PMNS"]) < 0.045       # 205.15 deg vs 197 deg (+4.14%)
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

    # Phase 9: Candidate baryogenesis (eta_B) and dark matter (Omega_DM / Omega_b)
    p9 = sc["phase9_cosmological_baryogenesis_and_dark_matter"]
    assert float(p9["rel_error_eta_B"]) < 0.02                # +1.57% (6.216e-10 vs 6.12e-10)
    assert abs(float(p9["eta_B_pred_with_true_quarter_eta6"]) - 1.1867e-10) < 1e-12
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

    # Theorem 13: Basis-Invariant Symmetric Weinberg Operator M_W(h, m_W) on (-3, -3) & Guardrail 3 Verification
    t13 = sc["theorem13_basis_invariant_weinberg_majorana_and_pmns"]
    assert float(t13["pauli_1_residue_abs_at_m3_m3"]) < 1e-15
    assert float(t13["mw_a0_independence_error"]) < 1e-14
    assert float(t13["mw_formula_match_error"]) < 1e-15
    assert float(t13["max_c_ll_closed_form_vs_b1656_cA_err"]) < 1e-11
    s_ll6 = t13["exact_ll_twist6_weinberg_spectrum"]
    assert abs(float(s_ll6["sin2_theta12"]) - 0.26946) < 1e-4
    assert abs(float(s_ll6["sin2_theta23"]) - 0.03372) < 1e-4
    assert abs(float(s_ll6["sin2_theta13"]) - 0.00118) < 1e-4
    assert abs(float(s_ll6["m2_over_m3"]) - 0.09433) < 1e-4
    assert abs(float(t13["sin2_theta12_weinberg_minimal"]) - 0.27697) < 1e-4
    assert abs(float(t13["sin2_theta13_weinberg_minimal"]) - 0.01393) < 1e-4
    assert t13["passes_guardrail3_basis_invariance"] is True
    assert float(t13["max_haar_unitary_scramble_error_on_pmns"]) < 1e-13
    assert abs(float(t13["modular_seesaw_scale_comparison"]["ratio_quarter_eta6_over_abs_b10_sq"]) - 0.19092) < 1e-3

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

    # Theorem 18: S291-S294 Recognition Controls, P-585 Strip Level-2 Targets, 15:5:3 Exponent Law & Order-10 Reflection-Transpose
    t18 = sc["theorem18_p585_strip_level2_targets_and_order10_reflection_transpose"]
    assert "B1728_the_lines_order_as_a_quotient_of_hypercharge" in t18["seen_first"]
    assert "B1829_the_two_level_bar" in t18["seen_first"]
    assert "FORCED" in t18["claim_labels_and_scopes"]["exponent_ratio_15_5_3_on_alpha_2_5"]
    assert "FORCED" in t18["claim_labels_and_scopes"]["order10_reflection_transpose_identity"]
    assert "EXCLUDED_WITHIN_SCOPE" in t18["claim_labels_and_scopes"]["one_higgs_shared_norm_yb_over_yt_on_strip"]

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
    assert pb18["Delta_E_bt_exact"] == "3/100"
    assert pb18["ratio_Delta_E_bt_over_Delta_E_up"] == "1/5"
    assert pb18["ratio_Delta_E_bt_over_Delta_E_down"] == "3/5"
    assert float(pb18["numerical_slope_vs_exact_Delta_E_bt_err"]) < 1e-5
    assert float(pb18["numerical_slope_vs_exact_Delta_E_up_err"]) < 5e-5
    assert float(pb18["numerical_slope_vs_exact_Delta_E_down_err"]) < 5e-5
    assert 1.07 < float(pb18["one_higgs_yb_over_yt_a0_zero_min_across_strip"]) < 1.09
    assert 1.10 < float(pb18["one_higgs_yb_over_yt_a0_zero_max_across_strip"]) < 1.12
    assert 0.53 < float(pb18["one_higgs_yb_over_yt_4d_adj_min_across_strip"]) < 0.55
    assert 0.57 < float(pb18["one_higgs_yb_over_yt_4d_adj_max_across_strip"]) < 0.59

    pc18 = t18["part_C_order10_reflection_transpose_and_strip_targets"]
    assert float(pc18["max_order10_residue_reflection_err_across_5_lines"]) < 1e-13
    assert float(pc18["max_order10_yukawa_reflection_transpose_err"]) < 1e-13
    assert float(pc18["order5_ytau_over_yb_max_dev_from_1"]) < 1e-13
    assert float(pc18["order10_ytau_over_yb_max_dev_from_1_at_F10"]) < 1e-6
    assert float(pc18["max_higgs_norm_phase_cancel_imag_err"]) < 1e-15
    assert len(pc18["bar_theta_s_tilde_s_s_across_10_strip_lines_rad"]) == 10











