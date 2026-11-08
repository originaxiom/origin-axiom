"""
Pytest Suite & Planted-Mutation Countercontrols for the Weave Unification Bridge
================================================================================
Tests `src/origin_axiom/weave_unification_bridge.py`:
  - Theorem I (Lead 1 & Joint J1): P-531 commutant dimensions (9 -> 3 -> 1), V_4 deck
    pushforward orthogonality forcing H = I_3, 144-component V_4 character selection rule
    across H = 1 + Im(H), and Joint J1 twist-order parity commutant theorem (2 | N -> dim_R(H) = 2
    vs odd N with gcd(N, 6) = 1 -> dim_R(H) = 1).
  - Theorem II (Lead 2, Lead 3, & WP2): K_1^- twisted 5-torsion kernel, (2/5, 1/5) unique
    1-step LR 3-cycle covariance among B1822's ten (2/5, k/10) lines, exact Golden Ratio
    residue identity |R_k|/||R|| = 1/phi at tau = i, Modular Area-Cutoff Theorem c_tilde_s(tau),
    Gieseking half-period deck 4-cycle on K_1^- \\ {0}, and P-741 Lemma E Dijkstra shortest-path
    margins across subsets S of {2, 3, 4, 5}.
  - Theorem III (Joint J3, WP3, & WP4): P-740 cyclic palindrome involution theorem splitting
    W_k(6) = L^6 R (LR)^k into Tube (Re = 0) and Anti-Apex (Re = 1/2), P-583 holomorphic
    quaternion adjugate identity & B1744 4D factorized determinant theorem, Down-Lepton
    Adjugate Duality on N = 5, and two-locus CKM corner asymmetry under 50-trial Haar unitary
    basis scrambling (Guardrail 3).
  - Theorem IV (Codex Physical-Bridge Joins): 68bbb463f common-source product join E -> S_4 x A_5
    of order 1440 with unique invariant internal density I_4 / 4; c0d19629f Dic_n zero-threshold
    criticality iff n in {2, 8, 10} and min fractional distance 1/10 across all 128 spinor slots
    at n = 5; ae5e48184 complete Dic_5 zero-mode roster (67/69 chiral profiles, 76/78 with gauginos)
    and Gieseking sigma k-pair swap.
  - All 10 Planted-Mutation Countercontrols & Foundational / Whole-Weave Discipline Ledger.
"""

from __future__ import annotations

from origin_axiom.weave_unification_bridge import (
    run_planted_mutation_countercontrols,
    run_weave_unification_crystallization_suite,
    verify_codex_physical_bridge_joins,
    verify_lead1_tnorm_and_j1_parity_commutant,
    verify_lead2_lead3_and_p741_excursion_law,
    verify_p740_palindrome_involutions_and_wp3_wp4,
    verify_wp1_p740_and_joint_j1,
    verify_wp2_p741_charge_law,
    verify_wp3_p583_and_b1744,
    verify_wp4_two_locus_and_localization,
)


def test_theorem1_lead1_and_j1_parity_commutant() -> None:
    t1 = verify_lead1_tnorm_and_j1_parity_commutant()
    assert t1["commutant_dims_9_3_3_1"] == (9, 3, 3, 1)
    assert t1["v4_plus_2T_forces_H_identity"] is True
    assert t1["cover_deck_orthogonality_forces_H_identity"] is True
    assert t1["heisenberg_z3_clock_dims"] == (3, 1)
    assert t1["full_4d_quaternion_144_selection_rule_ok"] is True
    census = t1["joint_j1_parity_census"]
    assert census[5]["dim_R_H"] == 1 and census[5]["has_generation_3cycle"] is True
    assert census[10]["dim_R_H"] == 2 and census[10]["has_generation_3cycle"] is False


def test_theorem2_lead2_lead3_and_p741_excursion_law() -> None:
    t2 = verify_lead2_lead3_and_p741_excursion_law()
    assert len(t2["k1_twisted_5torsion_lines"]) == 5
    assert t2["b1822_ten_lines_lr_3cycle_defects"]["(2/5, 2/10)"] < 1e-14
    assert t2["b1822_ten_lines_lr_3cycle_defects"]["(2/5, 3/10)"] > 0.5
    assert t2["golden_ratio_residue_err"] < 1e-15
    assert t2["ctilde_lr_3cycle_err"] < 1e-5
    assert t2["raw_cA_conformal_shift"] > 1.0
    assert t2["sigma_4cycle_orbit_on_K1_minus"] == [
        ("1/5", "3/5"),
        ("3/5", "4/5"),
        ("4/5", "2/5"),
        ("2/5", "1/5"),
    ]
    assert t2["sigma_residue_3cycle_err"] < 1e-14
    p741 = t2["p741_lemma_e_ledger"]
    assert p741["(5,)"]["single_run_proved_minimal"] is True
    assert abs(float(p741["(5,)"]["margin"]) - 0.182787306) < 1e-6
    assert p741["(3, 4)"]["single_run_proved_minimal"] is False


def test_theorem3_p740_p583_and_two_locus_haar() -> None:
    t3 = verify_p740_palindrome_involutions_and_wp3_wp4()
    assert t3["p740_m004_both_centers_re_half"] is True
    assert t3["p740_W6_splits_tube_re0_and_anti_apex_re_half"] is True
    assert t3["p583_adjugate_identity_max_err"] < 1e-13
    assert t3["b1744_4d_factorized_det_max_err"] < 1e-12
    assert t3["n5_down_lepton_adjugate_sv_err"] < 1e-5
    assert abs(t3["det_preserving_4d_det_ratio"] - 1.0) < 1e-4
    assert t3["two_locus_ckm_corner_asymmetry"] > 0.05
    assert t3["haar_50_trial_max_invariance_err"] < 1e-12
    assert t3["cross_locus_join_scope"] == "CONDITIONAL_TWO_LOCUS_SERRE_AND_ADJUGATE_MODEL_PENDING_3D_BUNDLE_TRANSPORT"


def test_theorem4_codex_physical_bridge_joins() -> None:
    t4 = verify_codex_physical_bridge_joins()
    assert t4["codex_68bbb463f_joint_projective_order"] == 1440
    assert t4["codex_68bbb463f_unique_invariant_density_is_I4_over_4"] is True
    assert t4["codex_c0d19629f_critical_n_list"] == [2, 8, 10]
    assert t4["codex_c0d19629f_n5_min_128_slot_freq_distance"] == "1/10"
    assert t4["codex_c0d19629f_single_lr_trace_obstruction_verified"] is True
    roster = t4["codex_ae5e48184_roster_by_k"]
    assert roster[1]["chiral_profiles"] == 67 and roster[1]["complete_left_zeros_with_gauginos"] == 76
    assert roster[2]["chiral_profiles"] == 69 and roster[2]["complete_left_zeros_with_gauginos"] == 78
    assert t4["codex_ae5e48184_gieseking_sigma_swaps_k_pairs"] is True
    assert t4["dic5_gieseking_swap_scope"] == "CONNECTS_PRIMITIVE_DIC5_HOLONOMY_PAIRS_CONDITIONAL_ON_SPIN_WILSON_DOMAIN_TRANSPORT"


def test_wp1_wp2_wp3_wp4_weave_unification_work_packages() -> None:
    wp1 = verify_wp1_p740_and_joint_j1()
    assert wp1["p740_words_tested"] == 18
    assert wp1["all_p_diag_equal"] is True
    assert wp1["all_dpd_equal"] is True
    assert wp1["all_j_involution"] is True
    assert wp1["all_re_tau_match"] is True
    assert wp1["max_re_tau_error"] < 1e-15
    assert wp1["even_orders_break_H_to_dim2"] is True
    assert wp1["odd_orders_force_H_eq_I3"] is True
    assert wp1["wp1_passed"] is True

    wp2 = verify_wp2_p741_charge_law()
    assert wp2["lemma_b_golden_frame_mismatches"] == 0
    assert wp2["lemma_b_max_rel_err"] < 1e-14
    assert wp2["lemma_c_min_fib_ratio_err"] < 1e-15
    assert wp2["lemma_c_strict_off_2"] is True
    assert wp2["lemma_c_bound_holds_on_200_defects"] is True
    assert wp2["lemma_d_verified"] is True
    assert wp2["all_s_le_10_margins_positive"] is True
    assert wp2["wp2_passed"] is True

    wp3 = verify_wp3_p583_and_b1744()
    assert wp3["v4_nonzero_components_of_144"] == 36
    assert wp3["v4_character_violations"] == 0
    assert wp3["b1656_frame_vs_closed_form_max_rel_err"] < 1e-14
    assert wp3["p583_adjugate_transpose_max_rel_err"] < 1e-14
    assert wp3["b1744_det_identity_max_rel_err"] < 1e-13
    assert wp3["cubic_locus_det_conservation_max_rel_err"] < 1e-12
    assert wp3["wp3_passed"] is True

    wp4 = verify_wp4_two_locus_and_localization()
    assert wp4["max_eta6_quarter_rel_err"] < 1e-30
    assert wp4["k_family_profiles"]["k=1"]["localization_p744"]["scope"] == "1D_TEICHMULLER_SOL_CLOCK_PERIODIC_MODEL_NOT_3D_HYPERBOLIC_PDE_P744"
    assert wp4["single_locus_lock_inequality_holds"] is True
    assert wp4["max_b1646_d3_rel_err"] < 1e-12
    assert wp4["max_b1744_lemma_a_rel_err"] < 1e-12
    assert wp4["single_locus_null_overlap_max_err"] < 1e-12
    assert wp4["max_haar_basis_scramble_err"] < 1e-12
    assert wp4["wp4_passed"] is True


def test_planted_mutations_and_whole_weave_discipline() -> None:
    mutations = run_planted_mutation_countercontrols()
    assert len(mutations) == 10
    assert all(mutations.values())
    suite = run_weave_unification_crystallization_suite()
    assert suite["all_planted_mutations_rejected"] is True
    assert suite["all_work_packages_passed"] is True
    assert suite["data_free_0_of_19"] is True
    disc = suite["foundational_and_whole_weave_discipline"]
    assert disc["non_cancellation_to_matrix_commutator_is_explicit_interpretation"] is True
    assert disc["rank_and_prime_theorems_are_conditional_characterizations_not_unconditional_derivations"] is True
    assert disc["whole_weave_vs_single_fixed_sector_distinction_enforced"] is True
    assert disc["confirmed_sm_parameters"] == "0 of 19"
    cusp = suite["theorem4_codex_physical_bridge_joins"]["codex_b996bc98e_91f4b0aa6_gauge_cusp_response"]
    assert cusp["codex_b996bc98e_passed"] is True
    assert cusp["scalar_and_vector_outward_flux_verified"] is True
    assert cusp["poisson_norms_green_and_riccati_verified"] is True
    assert cusp["static_shell_schur_cut_independence_verified"] is True
    assert cusp["cubic_overlap_from_mode_exponents_verified"] is True
    assert cusp["finding_c1_forbidden_bvv_divergence_guard_verified"] is True
    assert cusp["finding_c1_forged_mode_rejected_by_euler_and_norm_guard"] is True
    assert cusp["colour_so3_triple_bracket_trace"] == -2
    assert cusp["finding_c2_nonabelian_so3_duhamel_holonomy_verified"] is True
    mag = cusp["codex_91f4b0aa6_orthonormal_tail_constant_and_magnetic_saddle_scope"]
    assert mag["orthonormal_tail_amplitude_constant_in_y"] is True
    assert mag["residual_zero_scalar_stiffness_positive"] is True
    assert mag["nonzero_magnetic_flux_charged_eigenvalues"] == {1: -5, 2: -10, 3: -15}
    assert mag["su5_weierstrass_negative_mode_counts_by_n"] == {1: 30, 2: 60, 3: 90}
    sew = cusp["codex_75971c6f7_core_mean_response_and_flux_sewing"]
    assert sew["zero_flux_forces_zero_seam_circulation"] is True
    assert sew["quantized_flux_equalizes_core_and_tail_curvature"] is True
    assert sew["cut_independent_total_area_energy_verified"] is True
    assert sew["unfixed_relative_core_cohomology_rank_per_commuting_gen"] == 2
    assert sew["relative_c0_chain_rank"] == 0

    w3 = suite["weakness3_zero_flux_boundary_source"]
    assert w3["weakness3_zero_flux_source_passed"] is True
    assert w3["scope"] == "CONDITIONAL_TWO_VARIABLE_DISPLACED_SOURCE_MODEL_NOT_PARENT_ACTION_DERIVATION"
    assert w3["symbolic_stationarity_b_star_and_alpha_z_star_verified"] is True
    assert w3["symbolic_hessian_determinant_verified"] is True
    assert w3["benchmark_hessian_det_fraction"] == "52/315"
    assert w3["benchmark_b_star_at_zero_flux_fraction"] == "35/104"
    assert w3["zero_offset_forces_zero_b_star_verified"] is True
    assert w3["opposite_sign_core_tail_curvatures_sum_to_zero"] is True
    assert w3["savvidy_magnetic_shift_at_zero_flux"] == 0

    w4 = suite["weakness4_aps_chiral_index_projection"]
    assert w4["weakness4_aps_chirality_passed"] is True
    assert w4["scope"] == "CONDITIONAL_1D_CALLIAS_DOMAIN_WALL_AND_EXACT_ADJOINT_CONTROL_ON_NATIVE_D4_TRIPLET"
    assert w4["periodic_baseline_ker_L_ker_R_net_index"] == [3, 3, 0]
    assert w4["fixed_h1_h10_same_domain_index_m0_and_wall"] == [1, 1]
    assert w4["asymptotic_sign_glued_indices_pos_neg_kink_antikink"] == [0, 0, 3, -3]
    assert w4["exact_telescoping_hilbert_adjoint_max_err"] < 1e-14
    assert w4["native_d4_triplet_channel_count"] == 3
    assert w4["aps_wall_ker_L_ker_R_net_chiral_index"] == [3, 0, 3]
    assert w4["analytic_sech_zero_mode_spectral_residual"] < 1e-13
    assert w4["max_su3_color_commutator_fro_err"] < 1e-14

    w5 = suite["weakness5_interfiber_propagator_3d_join"]
    assert w5["weakness5_interfiber_propagator_passed"] is True
    assert w5["scope"] == "UPPER_HALF_PLANE_TAU_PARAMETER_TRANSPORT_CONSISTENCY_CONTROL_NOT_3D_HYPERBOLIC_PDE"
    assert w5["geodesic_endpoint_circle_err"] < 1e-13
    assert w5["hyperbolic_distance_closed_vs_quadrature"][2] < 1e-13
    assert w5["Vud_3d_propagator_joined"] > 0.99
    assert w5["Vub_over_Vtd_3d_propagator_joined"] < 1.0
    assert w5["haar_basis_scramble_max_ckm_err"] < 1e-12
    assert w5["haar_basis_scramble_max_jarlskog_err"] < 1e-13

    c09 = suite["codex_09f478c79_dynamic_core_and_period_quartic"]
    assert c09["codex_09f478c79_passed"] is True
    assert c09["scope"] == "FINITE_EXACT_SURROGATES_AND_WARD_CONTROLS_NOT_COMPLETE_SURFACE_PDE_OR_ACTUAL_CORE_SPECTRUM"
    assert c09["control1_nonzero_angular_bessel_tail_verified"] is True
    assert c09["control2_distinct_s0_limits_and_2component_norm_verified"] is True
    assert c09["control3_core_neumann_surrogate_and_symmetry_discriminator_verified"] is True
    assert c09["control4_boundary_ward_null_vector_and_noncommuting_Dc_verified"] is True
    assert c09["control5_longitudinal_vbb_cubic_I_L_vs_I_T_ward_verified"] is True
    assert c09["control6_quartic_nonharmonic_relaxation_verified"] is True
    assert c09["control7_handle_scope_g1_vs_g2_cancellation_verified"] is True

    f69 = suite["frontiers_6_to_9_shape_core_b1856_b1857_weak"]
    assert f69["all_frontiers_6_to_9_passed"] is True
    assert f69["frontier6_ray_singer_shape_torsion"]["frontier6_passed"] is True
    assert f69["frontier6_ray_singer_shape_torsion"]["sl2z_modular_invariance_err"] < 1e-13
    assert f69["frontier7_actual_hyperbolic_core_neumann_spectrum"]["frontier7_passed"] is True
    assert f69["frontier7_actual_hyperbolic_core_neumann_spectrum"]["max_excited_eigenvalue_err"] < 1e-11
    assert f69["frontier8_b1856_weil5_and_b1857_state_readout"]["frontier8_passed"] is True
    assert f69["frontier8_b1856_weil5_and_b1857_state_readout"]["weil5_projective_elements_and_clashes"] == [120, 0]
    assert f69["frontier8_b1856_weil5_and_b1857_state_readout"]["apex_multiplicities_6_21212_21112_2_18_2"] == [1, 1, 2, 2]
    assert f69["frontier9_charged_128_threshold_and_weak_universality"]["frontier9_passed"] is True
    assert f69["frontier9_charged_128_threshold_and_weak_universality"]["zero_flux_charged_128_min_eigenvalue"] > 0.5
    assert f69["frontier9_charged_128_threshold_and_weak_universality"]["same_vs_cross_block_weak_brackets_128_120_cross"] == [0.0, 0.0, 1.0]
    assert f69["frontier9_charged_128_threshold_and_weak_universality"]["s3_triality_weak_commutator_fro_err"] < 1e-14
    assert f69["frontier9_charged_128_threshold_and_weak_universality"]["weak_current_3gen_universality_fro_err"] < 1e-14

    c1e = suite["codex_1eed871f8_four_connection_and_weak_grading"]
    assert c1e["codex_1eed871f8_and_weak_grading_passed"] is True
    assert c1e["scope"] == "BOUNDED_GREEN_CURRENT_GAUSS_QUARTIC_AND_WEAK_GRADING_CONTROLS_NOT_GLOBAL_SM3_COMPLETION"
    assert c1e["control1_green_kernel_and_endpoint_norm_verified"] is True
    assert c1e["control2_conserved_current_and_gauss_response_verified"] is True
    assert c1e["control3_two_triangle_overlap_and_log_cases_verified"] is True
    assert c1e["control3_double_quadrature_err"] < 1e-13
    assert c1e["control4_zero_exchange_and_nonabelian_pair_verified"] is True
    wg = c1e["duty4_e8_grading_and_cross_block_weak_current"]
    assert wg["duty4_passed"] is True
    assert wg["charge_one_roots_in_120_vs_128"] == [0, 32]
    assert wg["zeta_grading_even_120_and_odd_128"] is True
    assert wg["t3_plus_y_equals_q_verified"] is True
    assert wg["d_to_u_cross_block_weak_channel_verified"] is True
    assert wg["centralizer_A3_roots_in_120_vs_128"] == [6, 0]

    wall1 = suite["wall1_nonabelian_period_zero_flux_and_v1_repair"]
    assert wall1["wall1_and_v1_passed"] is True
    w1_p = wall1["wall1_zero_flux_nonabelian_period_stationarity"]
    assert w1_p["wall1_passed"] is True
    assert w1_p["monopole_flux_integer_n"] == 0
    assert w1_p["magnetic_eigenvalue_at_zero_flux"] == 0
    assert w1_p["killing_norm_nonabelian_vs_abelian"] == [1.0, 0.0]
    assert w1_p["relaxed_top_form_curvature_energy_nonabelian"] > 0.0
    assert w1_p["dynamic_core_stationary_x_star_sq"] == "2/3"
    assert w1_p["dynamic_core_minimum_energy_shift"] == "-1/4"
    v1_r = wall1["codex_v1_repair_4slot_physical_mass_gauge_fixing"]
    assert v1_r["v1_repair_passed"] is True
    assert v1_r["imported_4slot_physical_mass_matrix_shape"] == [12, 12]
    assert v1_r["dflat_fflat_11_block_equals_Pv"] is True
    assert v1_r["dflat_fflat_12_block_vanishes"] is True
    assert v1_r["dflat_violation_residual_diag"] == ["4/omega", "-4/omega", "0"]
    assert v1_r["wrong_gaugino_scale_breaks_decoupling"] is True
    assert v1_r["real_pfaffian_weights_Pc_vs_Pv"] == ["1/4", "-3/4"]
    assert v1_r["sm_massless_vector_beta_coefficients"] == [0, -6, -9]

    wall3 = suite["wall3_coupled_half_root_and_pv_weak_eigenmode"]
    assert wall3["wall3_passed"] is True
    c19 = wall3["controls_1_to_9_coupled_half_root_and_centralizer"]
    assert c19["control1_half_root_pairs_and_8_records"] == [64, 8]
    assert c19["control2_koszul_ranks_and_harmonic_cohomology"] == [15, 15, [1, 2, 1]]
    assert c19["control3_homotopy_max_err"] < 1e-12
    assert c19["control4_indicial_roots_and_pole_dim"] == [[-2, 0, 2], 4]
    assert c19["control5_kernel_dim_bare_16_vs_corrected_18"] == [16, 18]
    assert c19["control5_single_sheet_singlet_6_vs_triplet_12"] == [6, 12]
    assert c19["control6_centralizer_A3_15_to_9"] == [15, 9]
    assert c19["control7_source_kernel_9_plus_9_spin_0"] == [9, 9, 0]
    assert c19["control8_unitary_cusp_reduction_verified"] is True
    assert c19["control9_robin_core_continuum_verified"] is True
    pv_w = wall3["chebyshev_pv_eigenmode_and_cross_grading_weak_vertex"]
    assert pv_w["pde_and_vertex_passed"] is True
    assert abs(pv_w["lowest_discrete_eigenvalue_mW_sq_N48_vs_N64"][1] - 36.48214893545666) < 1e-8
    assert pv_w["chebyshev_convergence_err"] < 1e-10
    assert pv_w["cross_grading_weak_coupling_g_eff"] > 0.1
    assert pv_w["haar_basis_scrambling_invariance_err"] < 1e-14

    bvp = suite["coupled_2d_surface_and_3sheet_cover_bvp"]
    assert bvp["coupled_2d_and_3sheet_bvp_passed"] is True
    t1_bvp = bvp["task1_3sheet_d4_cover_vs_single_sheet_wilson"]
    assert t1_bvp["task1_passed"] is True
    assert t1_bvp["bare_pin10_record_counts_sum_16"] == [[2, 2, 2, 2, 2, 2, 2, 2], 16]
    assert t1_bvp["single_sheet_wilson_record_counts_sum_18"] == [[3, 2, 2, 2, 2, 2, 2, 3], 18]
    assert t1_bvp["cover_3sheet_middle_line_counts_per_record"] == [3, 3, 3, 3, 3, 3, 3, 3]
    assert t1_bvp["s3_triality_cover_projector_commutator_err"] == 0.0
    assert t1_bvp["coupled_36x36_4slot_cover_s3_comm_err"] == 0.0
    assert t1_bvp["coupled_36x36_4slot_gaugino_decoupling_err"] < 1e-14
    t2_bvp = bvp["task2_coupled_2d_surface_elliptic_hodge_system"]
    assert t2_bvp["task2_passed"] is True
    assert t2_bvp["discrete_2d_cochain_d1_d0_err"] == 0.0
    assert t2_bvp["coulomb_gauge_div_err_16x16"] < 1e-12
    assert t2_bvp["pointwise_1form_curvature_err_16x16"] < 1e-10
    assert abs(t2_bvp["unrelaxed_vs_relaxed_energy_16x16"][1] - t2_bvp["exact_relaxed_bound_1_over_8pi"]) < 1e-15
    assert t2_bvp["spectral_24x24_and_32x32_energy_errs"][0] < 1e-15
    assert t2_bvp["spectral_24x24_and_32x32_energy_errs"][1] < 1e-15
    t3_bvp = bvp["task3_coupled_4slot_koszul_weak_vertex_and_haar_scrambling"]
    assert t3_bvp["task3_passed"] is True
    assert t3_bvp["g_4slot_grid_convergence_err"] < 1e-11
    assert t3_bvp["haar_50_trial_su2L_u3fam_max_err"] < 1e-13
    assert t3_bvp["non_unitary_negative_control_drift"] > 0.5





