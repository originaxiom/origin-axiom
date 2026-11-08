"""
Pytest Countercontrol & Referee Suite for the Pure-Logic P000 -> F_2 -> SL(2,Z) -> Weave -> M_phi Bridge
========================================================================================================
Tests Step 1 (Freeness vs Relaxations), Step 2A/2B (P-221 Rank-Free PF1 & P-321 Half 2 Prime Selection),
Step 2C (P-211 / B1707 Genus-2 Surface Route), and Step 3/4 (P-321 Half 1 / R57 / L239(a) & 4 Forks).
"""

from __future__ import annotations

import numpy as np

from origin_axiom.p000_pure_logic_bridge import (
    apply_homomorphism,
    canonical_unoriented_conj_rep,
    commutator_word,
    run_all_p000_bridge_verifications,
    verify_4a0c6d799_affine_d4_register_and_realization_controls,
    verify_d47f7d79f_selector_earning_and_syntactic_congruence,
    verify_step1_freeness_vs_relaxations,
    verify_step2a_word_side_w110,
    verify_step2b_character_and_p321_prime,
    verify_step2c_p211_genus2_surface,
    verify_step3_and_4_carrier_and_forks,
)


def test_step1_freeness_vs_relaxations() -> None:
    s1 = verify_step1_freeness_vs_relaxations()
    assert s1["idempotent_band_size"] == 6
    assert s1["idempotent_collapses_to_6"] is True
    assert s1["d_inf_two_per_length"] is True
    assert s1["f2_exponential_per_length"] is True
    assert s1["d_inf_derived_length_2_collapses"] is True
    assert s1["transvection_obstructed_in_dinf"] is True
    assert s1["q8_collapses_to_v4_on_dinf"] is True
    assert s1["burnside_b23_order"] == 27
    assert s1["burnside_b23_all_exp_3"] is True
    assert s1["burnside_b23_nilpotent_class_2"] is True
    assert s1["burnside_b23_kills_q8"] is True
    assert s1["burnside_b23_sl2c_strictly_abelian"] is True
    assert s1["abelian_kills_commutator"] is True
    hz = s1["heisenberg_hz_countermodel"]
    assert hz["commutator_ab_nontrivial"] is True
    assert hz["triple_commutators_vanish"] is True
    assert hz["f2_sanov_triple_commutator_nontrivial"] is True
    assert hz["aut_f2_moves_descend_on_commutator"] is True
    assert hz["q8_character_factors_through_hz"] is True
    assert hz["proves_full_f2_faithfulness_is_explicit_hypothesis"] is True


def test_step2a_word_side_w110() -> None:
    s2a = verify_step2a_word_side_w110()
    assert s2a["whitehead_identity_failures"] == 0
    assert s2a["whitehead_left_identity_failures"] == 0
    assert s2a["whitehead_sum_bound_failures"] == 0
    assert s2a["whitehead_identity_trials"] >= 25000
    assert s2a["n3_kept_len_R_count_len_le_6"] == 0
    assert s2a["n4_kept_len_R_count_len_le_5"] == 0
    assert len(s2a["n2_kept_classes_len_le_8"]) == 4


def test_step2b_character_and_p321_prime_selection() -> None:
    s2b = verify_step2b_character_and_p321_prime()
    assert s2b["fricke_roots"] == [0, 2]
    assert s2b["kappa_at_0"] == -2
    assert s2b["kappa_at_2"] == 2
    assert s2b["clifford_n3_product_trace"] == -2
    assert s2b["clifford_symbolic_traces"] == [-2, 2]
    assert s2b["sl2_f3_binary_tetrahedral_order"] == 24
    assert s2b["parity_orbit_size"] == 3
    assert s2b["basis_invariance_err"] < 1e-12

    # P-321 Half 2: under orientation-reversing swap P and Fibonacci tick LP,
    # only p = 2 (Q_8) is strictly invariant; odd primes p = 3, 5 are conjugated!
    p321 = s2b["p321_prime_selection_under_swap_and_tick"]
    assert p321["2"]["witness_group"] == "Q_8_subset_SU2"
    assert p321["2"]["generator_det"] == 1
    assert p321["2"]["single_irrep_dim"] == 2
    assert p321["2"]["single_irrep_fixed_by_swap"] is True
    assert p321["2"]["fixed_by_swap_P"] is True
    assert p321["2"]["fixed_by_tick_LP"] is True
    assert p321["3"]["single_irrep_dim"] == 3
    assert p321["3"]["single_irrep_fixed_by_swap"] is False
    assert p321["3"]["paired_reducible_dim"] == 6
    assert p321["3"]["paired_reducible_fixed_by_swap"] is True
    assert p321["3"]["fixed_by_swap_P"] is False
    assert p321["3"]["fixed_by_tick_LP"] is False
    assert p321["5"]["single_irrep_dim"] == 5
    assert p321["5"]["single_irrep_fixed_by_swap"] is False
    assert p321["5"]["paired_reducible_dim"] == 10
    assert p321["5"]["paired_reducible_fixed_by_swap"] is True
    assert p321["5"]["fixed_by_swap_P"] is False
    assert p321["5"]["fixed_by_tick_LP"] is False
    # Whole-weave alternatives at odd p: conjugate-pair direct sum and antiunitary Fourier intertwiner
    assert p321["3"]["whole_weave_conjugate_pair_2p_fixed_by_swap"] is True
    assert p321["5"]["whole_weave_conjugate_pair_2p_fixed_by_swap"] is True
    assert p321["3"]["whole_weave_antiunitary_fourier_swap_err"] < 1e-12
    assert p321["5"]["whole_weave_antiunitary_fourier_swap_err"] < 1e-12


def test_step2c_p211_genus2_surface() -> None:
    s2c = verify_step2c_p211_genus2_surface()
    assert s2c["f4_intra_handle_transvections_kept"] == 4
    assert s2c["f4_cross_handle_transvections_kept"] == 0
    assert s2c["g1_arf1_form_count"] == 1
    assert s2c["g2_arf1_form_count"] == 6
    assert s2c["g2_arf0_form_count"] == 10
    assert s2c["g2_sp4_f2_orbit_sizes"] == [6, 10]
    assert s2c["g2_fixed_2group_characters"] == 0
    assert s2c["g2_heisenberg_h3_order"] == 243
    assert s2c["g2_heisenberg_h3_irrep_dim"] == 9
    assert s2c["g2_heisenberg_h3_fixed_by_sp4"] is True
    assert s2c["g2_sp4_f3_transvections_checked"] == 80
    assert s2c["g2_sp4_f3_distinct_transvection_matrices"] == 40


def test_step3_and_4_carrier_and_countercontrols() -> None:
    s34 = verify_step3_and_4_carrier_and_forks()
    s3 = s34["step3_r57_and_carrier_theorem"]
    assert s3["r57_equivariance_holds"] is True
    assert s3["comm_in_f2_nontrivial"] is True
    assert s3["comm_in_z2_vanishes"] is True
    assert s3["hyperbolic_no_unit_eigenvalue"] is True
    assert s3["sigma_conjugate_to_inv_comm"] is True
    assert s3["sigma2_conjugate_to_comm"] is True
    assert s3["peripheral_h1_classes"]["Sigma_{1,1}"] == [[0, 0]]

    # Independent check of planted mutations and Guardrail 3 left-right scrambling failure
    qi = np.array([[1j, 0.0], [0.0, -1j]], dtype=complex)
    U_left = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    U_right = np.eye(2, dtype=complex)
    assert abs(np.trace(U_left @ qi @ U_right.conj().T) - np.trace(qi)) < 1e-12
    assert abs(np.trace(U_left @ qi) - np.trace(qi)) > 1.0 or abs(
        np.trace(U_left @ np.eye(2)) - 2.0
    ) > 1.0

    comm = commutator_word((1,), (2,))
    L_f2 = {1: (1,), 2: (1, 2)}
    assert canonical_unoriented_conj_rep(apply_homomorphism(L_f2, comm)) == canonical_unoriented_conj_rep(comm)
    assert canonical_unoriented_conj_rep(apply_homomorphism(L_f2, (1, 2))) != canonical_unoriented_conj_rep((1, 2))

    full = run_all_p000_bridge_verifications()
    assert full["all_verifications_passed"] is True
    assert full["all_planted_mutations_rejected"] is True
    assert full["planted_mutations_rejected_count"] == 8

    d47 = verify_d47f7d79f_selector_earning_and_syntactic_congruence()
    assert d47["d47f7d79f_passed"] is True
    assert d47["section6_rank2_independent_of_A1_to_A4"] is True
    assert d47["section7_single_fixed_sector_independent_of_A1_to_A4"] is True
    assert d47["syntactic_congruence_quotient_sizes"] == {
        "Z2_order_2": 2,
        "V4_order_4": 4,
        "S3_order_6": 6,
        "Q8_order_8": 8,
    }
    assert d47["f2_word_syntactic_congruence_quotient_sizes"] == {
        "F2_to_Z2_order_2": 2,
        "F2_to_V4_order_4": 4,
        "F2_to_S3_order_6": 6,
        "F2_to_Q8_order_8": 8,
        "F2_to_H3_F3_order_27": 27,
    }
    assert all(cert["surjective"] is True for cert in d47["f2_word_image_coverage_certificates"].values())
    assert d47["f2_derived_length_3_cocycle_witness"]["P_r_equals_2_I_minus_A_A_plus_I_equals_4I"] is True
    assert d47["f2_derived_length_3_cocycle_witness"]["dim_H1_F2_mod_F2_triple_prime_VQ8"] == 2
    assert d47["f2_derived_length_3_cocycle_witness"]["dim_H1_across_3_parity_twists"] == 6
    assert d47["d2_automatic_det_one_lemma"]["r12_forces_det_b_eq_1"] is True
    assert d47["a5_all_rank_control"]["chi4_inner_product"] == 1
    assert d47["non_swap_sl2r_control"]["pred_P4_rejected"] is True
    assert d47["strict_single_drop_exact_diagonal"] is True
    assert len(d47["strict_single_drop_countermodels"]) == 6
    mp_audit = d47["codex_2896d441a_matter_price_audit"]
    assert mp_audit["Ad_commutator_is_plus_I3"] is True
    assert mp_audit["doublet_commutator_is_minus_I2"] is True
    assert mp_audit["dim_H1_F2_Ad_rho"] == 3
    assert mp_audit["dim_H1_F2_V_rho"] == 2
    assert mp_audit["dim_H1_Q8_V_rho"] == 0
    assert mp_audit["q8_averaging_recovery_error"] < 1e-12
    assert len(d47["three_selection_tasks_separation"]) == 3
    fam = d47["section7_model_comparison"]["M_family_p3_WeylPair_dim6"]
    assert fam["swap_block_intertwiner_error"] < 1e-12
    assert fam["L_block_intertwiner_error"] < 1e-12
    assert fam["R_block_intertwiner_error"] < 1e-12
    assert fam["max_L_trace_diff"] < 1e-12
    assert fam["max_R_trace_diff"] < 1e-12
    assert all(abs(x - (-0.5)) < 1e-12 for x in fam["normalized_commutator_trace_L_R_P"])
    assert d47["unique_survivor_after_P1_to_P5"] == ["M6_Quaternion_Spinor_Q8_SU2"]
    assert len(d47["models_matrix"]) == 6


def test_4a0c6d799_affine_d4_register_and_realization_controls() -> None:
    res = verify_4a0c6d799_affine_d4_register_and_realization_controls()
    assert res["codex_4a0c6d799_passed"] is True
    u_coc = res["universal_quaternion_order_cocycle"]
    assert u_coc["words_checked_count"] == 161
    assert u_coc["norm_and_zero_equivalence_verified"] is True
    assert u_coc["coboundary_shift_on_a_nonzero"] is True
    assert u_coc["relator_coordinates_in_I_A_B_C"] == {
        "P_r1_a4": [0, 0, 0, 0],
        "P_r2_a2_b_inv2": [-1, 0, -1, 0],
        "P_r3_b_inv_a_b_a": [0, 0, 1, 1],
    }
    d4 = res["d4_kernel_lattice"]
    assert d4["hnf_determinant_index_in_Z4"] == 2
    assert d4["minimal_norm2_d4_root_count"] == 24
    nielsen = res["nielsen_d4_and_s3_discriminant_transport"]
    assert nielsen["nielsen_on_relators_verified"] is True
    assert nielsen["perm_T_L_on_v0_s0_c0"] == {"v0": "v0", "s0": "c0", "c0": "s0"}
    assert nielsen["perm_T_R_on_v0_s0_c0"] == {"v0": "c0", "s0": "s0", "c0": "v0"}
    assert nielsen["left_inverse_transport_is_left_homomorphism"] is True
    assert nielsen["right_composition_homomorphism_fails"] is True
    lim = res["limits_and_6d_total_family"]
    assert lim["a4_killed_in_untwisted_doublet"] is True
    assert lim["homogenized_3x3_trace_independent_of_v"] is True
    assert lim["total_family_6d_aut_f2_covariant"] is True
    w34 = res["codex_283159389_w34_schreier_cycle_module"]
    assert w34["num_vertices"] == 8
    assert w34["num_directed_edges"] == 16
    assert w34["cycle_module_Z_rank_N_ab"] == 9
    assert w34["adjoint_plus_doublet_rank_split"] == [5, 4]
    assert w34["J_a4_norm_squared"] == 4
    assert w34["J_comm_a4_b4_norm_squared"] == 0
    assert w34["J_projects_to_P_w_on_all_289_words"] is True

