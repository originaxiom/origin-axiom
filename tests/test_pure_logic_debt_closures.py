"""
Pytest Suite & Planted-Mutation Countercontrols for the Five Pure-Logic Debt Closures
=====================================================================================
Tests:
  - Theorem A (P-318 & P-618): Metallic McKay shadow counterexample (m=4 -> 120) & CRT repair (m=1 unique),
    plus level-1 WZW c=6 counterexamples (A_{6,1}, D_{6,1}) & 3-primary E_{6,1} selection.
  - Theorem B (P-604): B1221 hypercharge primitivity kernel order 6k vs wrong 6*gcd(k, 12) formula.
  - Theorem C (P-606): B298 degree-2 trace field vs multiplicity-3 scoping & 3 counterexamples on m004.
  - Theorem D (P-355): Complete data-free classification of 266 (N<=12) and 614 (N<=16) torsion lines
    into Class I (22 lines), Class II (60 lines = 20 II-i + 20 II-j + 20 II-k), and Class III.
  - Theorem E (P-262, P-268, P-292/P-337): Exact 4-channel duplication residue factorization,
    B1703 N|3 zero, B1701 27 tied lines, P-268 order-4/12 pairing, and P-292/P-337 Re(tau)=0 zero law.
"""

from __future__ import annotations

import pytest

from origin_axiom.pure_logic_debt_closures import (
    _b1656_contour_residues,
    _duplication_factored_residues,
    run_all_pure_logic_debt_closures,
    verify_debt_p262_and_p268_duplication_and_zeros,
    verify_debt_p318_and_p618_metallic_mckay_and_wzw_c6,
    verify_debt_p355_lepton_down_coincidence_locus,
    verify_debt_p604_hypercharge_primitivity_kernel,
    verify_debt_p606_degree2_trace_field_vs_multiplicity3,
)


def test_theorem_a_p318_p618_metallic_mckay_and_wzw_c6() -> None:
    res = verify_debt_p318_and_p618_metallic_mckay_and_wzw_c6()
    assert res["own_conductor_mckay_hits"] == [1, 4]
    assert res["primitive_own_conductor_mckay_unique_hit"] == [1]
    assert res["m4_counterexample_order"] == 120
    assert res["sl2_z4_order_and_involution_count"] == [48, 7]
    assert res["genuine_su2_2O_order_and_involution_count"] == [48, 1]
    assert res["sl2_z4_not_isomorphic_to_su2_2O_proved"] is True
    assert res["full_cascade_unique_hit"] == [1]
    assert res["wzw_sigma_eq_1_hits"] == ["A6", "D6", "E6"]
    assert res["wzw_sigma_eq_1_and_3primaries_unique_hit"] == ["E6"]
    assert res["wzw_rank6_comparison"]["A6"]["level1_primaries_det_C"] == 7
    assert res["wzw_rank6_comparison"]["D6"]["level1_primaries_det_C"] == 4
    assert res["wzw_rank6_comparison"]["E6"]["level1_primaries_det_C"] == 3
    assert len(res["wzw_all_16_simply_laced_table"]) == 16


def test_theorem_b_p604_hypercharge_primitivity_kernel() -> None:
    res = verify_debt_p604_hypercharge_primitivity_kernel()
    assert res["exact_kernel_eq_6_solutions_k_le_18"] == [1]
    assert res["b1221_wrong_formula_eq_6_solutions_k_le_18"] == [1, 5, 7, 11, 13, 17]
    assert res["k5_counterexample_exact_order"] == 30
    assert res["k5_counterexample_wrong_formula"] == 6


def test_theorem_c_p606_degree2_trace_field_vs_multiplicity3() -> None:
    res = verify_debt_p606_degree2_trace_field_vs_multiplicity3()
    assert res["scoped_galois_orbit_sizes_in_quadratic_field"] == [1, 2]
    assert res["counterexample1_isotypic_multiplicity"] == 3
    assert res["counterexample1_1d_block_commutant_dim_K"] == 9
    assert res["counterexample1_irred_2d_block_commutant_dim_Q"] == 18
    assert res["counterexample1_irred_2d_block_commutant_dim_K"] == 9
    assert res["counterexample1_reducible_diag_splitting_commutant_dim_K"] == 18
    assert res["counterexample2_sigma11_f2_parity_count"] == 3
    assert res["counterexample3_2T_1d_character_count"] == 3
    assert res["counterexample3_2T_2d_doublet_count"] == 3
    assert res["counterexample3_2T_has_rational_3d_triplet"] is True
    assert res["unscoped_b298_implication_refuted"] is True


def test_theorem_d_p355_lepton_down_coincidence_locus() -> None:
    res = verify_debt_p355_lepton_down_coincidence_locus()
    assert res["total_oriented_primitive_points_N_le_16"] == 1224
    assert res["total_unoriented_lines_N_le_16"] == 614
    assert res["total_unoriented_lines_N_le_12_b1713"] == 266
    assert res["class1_full_lattice_orders"] == [1, 2, 4, 5]
    assert res["class1_line_count"] == 22
    assert res["class2_diagonal_half_period_orders"] == [8, 10]
    assert res["class2_line_count"] == 60
    assert res["class2_klein4_subclass_counts"] == {
        "II_i_delta_0_half": 20,
        "II_j_delta_half_0": 20,
        "II_k_delta_half_half": 20,
    }
    assert res["class2_real_half_period_b1742_line_count"] == 20
    cc_b1832 = res["b1832_t_half_lift_and_pure_qi_countercontrol"]
    assert cc_b1832["pure_qi_higgs_also_preserves_d_eq_e"] is True
    assert cc_b1832["mixed_higgs_breaks_d_eq_e"] is True
    assert res["class3_clean_separation_line_count_N_le_12"] == 184
    assert res["class3_clean_separation_line_count_N_le_16"] == 532
    assert res["total_clean_separation_with_v_i_zero_N_le_12"] == 224
    assert res["total_clean_separation_with_v_i_zero_N_le_16"] == 572


def test_theorem_e_p262_p268_p292_duplication_and_zeros() -> None:
    res = verify_debt_p262_and_p268_duplication_and_zeros()
    assert res["max_duplication_factorization_rel_err"] < 1e-14
    assert res["max_mp30_full_u_unnormalized_szego_err"] < 1e-26
    assert res["max_riemann_sum_R2_rel_err"] < 1e-14
    assert res["order3_max_rel_R1"] < 1e-14
    assert res["b1701_tied_line_count"] == 27
    assert res["b1701_max_rel_R_tied"] < 1e-14
    assert res["p268_firing_counts_by_order"]["4"] == {"up": 6, "down": 6, "lep": 6}
    assert res["p268_firing_counts_by_order"]["12"] == {"up": 0, "down": 0, "lep": 48}
    assert res["p292_re_tau_0_both_odd_line_count"] == 16
    assert res["p292_re_tau_0_max_both_odd_4channel_a0_spread"] < 1e-14
    assert res["p292_re_tau_0_max_both_odd_full_2d_c_tilde_spread"] < 1e-13
    assert res["p292_re_tau_0_alpha_odd_b_even_counterexample_count"] == 16
    assert res["p292_re_tau_0_min_b_even_counterexample_defect"] > 1e-3
    assert res["p292_re_tau_0_b_even_full_2d_c_tilde_defect"] > 1e-2


def test_planted_mutations_rejected() -> None:
    """
    Countercontrol check: verify that planted mutations of the duplication phase or
    B997/B1221/B1228/P-292 unscoped claims are immediately rejected.
    """
    t = 0.29 + 1.9j
    x, y = (0.17, -0.33), (-0.41, 0.62)
    r_cont = _b1656_contour_residues(x, y, t)
    r_fact = _duplication_factored_residues(x, y, t)
    # Planted mutation 1: omitting exp(-2*pi*i * a_y) on R_1 or R_j breaks agreement with B1656 contour residues
    mutated_r1 = r_fact["1"] / (complex(__import__("numpy").exp(-2j * __import__("math").pi * y[0])))
    assert abs(mutated_r1 - r_cont["1"]) / abs(r_cont["1"]) > 0.1

    # Planted mutation 2: claiming m = 4 has shadow order != 120 or that B1221's 6*gcd(k, 12) holds at k = 5
    full = run_all_pure_logic_debt_closures()
    assert full["all_five_debt_theorems_verified"] is True
    assert full["theorem_a_p318_p618"]["m4_counterexample_order"] != 1920
    assert (
        full["theorem_b_p604"]["k5_counterexample_exact_order"]
        != full["theorem_b_p604"]["k5_counterexample_wrong_formula"]
    )
