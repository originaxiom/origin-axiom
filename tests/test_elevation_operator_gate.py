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
    evaluate_sm_19_gate,
    inter_sector_yukawa_unification,
    stabilized_modulus_candidates,
    step1_golden_5torsion_norm_preserving_solution,
    step2_physical_spin_flavour_locking_bridge,
    step3_pmns_and_m004_gauge_thresholds,
    step4_sealed_stepb_v2_fr_cov_verdict,
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



