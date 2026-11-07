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


def test_planted_mutations_and_whole_weave_discipline() -> None:
    mutations = run_planted_mutation_countercontrols()
    assert len(mutations) == 10
    assert all(mutations.values())
    suite = run_weave_unification_crystallization_suite()
    assert suite["all_planted_mutations_rejected"] is True
    assert suite["data_free_0_of_19"] is True
    disc = suite["foundational_and_whole_weave_discipline"]
    assert disc["non_cancellation_to_matrix_commutator_is_explicit_interpretation"] is True
    assert disc["rank_and_prime_theorems_are_conditional_characterizations_not_unconditional_derivations"] is True
    assert disc["whole_weave_vs_single_fixed_sector_distinction_enforced"] is True
    assert disc["confirmed_sm_parameters"] == "0 of 19"
