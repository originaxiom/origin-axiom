"""First-computation runner for the mathematical entrypoints of upstream stages one to seven and P-753.

Calls the twenty-one mathematical verification entrypoints in src/origin_axiom/ directly
(without re-running the seventeen-file source-scanner loop) and prints exact integer,
rational, and boolean check summaries. Data-free: 0 of 19.
"""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from origin_axiom.p753_register_field_join import run_full_p753_join  # noqa: E402
from origin_axiom.stage1_curved_action_cusp_orbit import (  # noqa: E402
    verify_wp21_curved_action_and_flat_moduli,
    verify_wp22_exact_e8_and_weave_background_orbits,
    verify_wp23_cusp_end_law_and_normalizations,
)
from origin_axiom.stage2_kernel_and_physical_join import (  # noqa: E402
    verify_b1866_zero_handtyped_3branch_pde_join,
    verify_wp31_exact_koszul_homotopy_and_248_parabolic_kernel,
    verify_wp32_exact_cyclotomic_algebra_and_metaplectic_obstruction,
)
from origin_axiom.stage3_carrier_moves_parent_algebra import (  # noqa: E402
    verify_wp12_records_and_punctured_torus,
    verify_wp13_moves_and_ground_theorems,
    verify_wp18_parent_algebra_exhibits_vs_forces,
    verify_wp19_register_deck_and_state_joins,
)
from origin_axiom.stage4_currents_hand_anomalies_theta import (  # noqa: E402
    verify_fl16_strong_cp_theta_bar_theorem,
    verify_wp14_swap_orientation_and_hand_exhaustion,
    verify_wp33_paired_pole_and_cyclic_theta_theorems,
    verify_wp35_anomalies_cusp_inflow_and_non_sm_modes,
)
from origin_axiom.stage5_cubic_overlaps_higgs_dictionary import (  # noqa: E402
    verify_wp17_quantum_number_dictionary_and_up_conjugate,
    verify_wp25_stationary_source_generation_metric_and_lepton_factor,
    verify_wp34_cubic_overlaps_and_value_frame_comparison,
)
from origin_axiom.stage6_closed_loop_scale_rge import (  # noqa: E402
    verify_part6a_kronecker_cusp_end_and_wp41,
    verify_part6b_whole_weave_transfer_and_p845,
    verify_part6c_level5_kashaev_and_2loop_rge,
)
from origin_axiom.stage7_upstream_audit_dag import (  # noqa: E402
    audit_buckingham_pi_guardrail5_ledger,
    build_one_generation_16_sm_generators,
    verify_b1604_flat_counting_dictionary_no_go,
    verify_upstream_epistemic_dag_and_fk_gates,
)


def main() -> None:
    lines: list[str] = []
    say = lines.append
    say("First computation of upstream stages 1 to 7 and P-753 (data-free, 0 of 19)")

    # P-753
    p753 = run_full_p753_join()
    p753_ok = bool(p753.get("all_passed", all(v is not False for v in p753.values())))
    say(f"P-753 register-to-field join: all_checks_hold={p753_ok}")

    # Stage 1
    wp21 = verify_wp21_curved_action_and_flat_moduli()
    wp22 = verify_wp22_exact_e8_and_weave_background_orbits()
    wp23 = verify_wp23_cusp_end_law_and_normalizations()
    s1_ok = bool(
        wp21["s01_flat_fibre_metric_ansatz_eliminated_by_curved_action"]
        and wp21["curved_pv_two_kdag_k_and_hitchin_bps_exact"]
        and wp21["x_flat_curved_1form_conformal_cancellation_exact"]
        and wp21["x_flat_rank2_cartan_real_moduli_dim"] == 12
        and wp21["x_flat_classical_u1_moduli_unobstructed_no_go"]
        and wp22["z4_global_kernel_exact"]
        and wp22["e8_compact_killing_neg60_exact"]
        and wp22["coherent_all_248_dims"]
        and wp23["radial_cusp_threshold_exact"]
        and wp23["curved_hodge_serre_and_spin_holonomy_index_exact"]
        and wp23["v4_haar_scrambling_invariant"]
    )
    say(
        f"Stage 1 (WP-2.1, WP-2.2, WP-2.3): real_cartan_flat_moduli_dim={wp21['x_flat_rank2_cartan_real_moduli_dim']}; "
        f"all_checks_hold={s1_ok}"
    )

    # Stage 2
    wp31 = verify_wp31_exact_koszul_homotopy_and_248_parabolic_kernel()
    wp32 = verify_wp32_exact_cyclotomic_algebra_and_metaplectic_obstruction()
    b1866 = verify_b1866_zero_handtyped_3branch_pde_join(wp32)
    s2_ok = bool(
        wp31["koszul_homotopy_all_5_blocks_exact"]
        and wp31["curved_pde_and_cusp_s5_pole_cutoff_exact"]
        and wp31["parabolic_248_census_verified"]
        and wp32["wp32_algebra_verified"]
        and wp32["universal_s4_sym2_no_go_proven"]
        and wp32["b1879_exchange_doubles_96_to_192_exact"]
        and b1866["eta3_supplies_odd_metaplectic_char_exact"]
        and b1866["b1866_physical_join_resolved_and_verified"]
    )
    say(f"Stage 2 (WP-3.1, WP-3.2, B1866 3-branch join): all_checks_hold={s2_ok}")

    # Stage 3
    wp12 = verify_wp12_records_and_punctured_torus()
    wp13 = verify_wp13_moves_and_ground_theorems()
    wp19 = verify_wp19_register_deck_and_state_joins()
    wp18 = verify_wp18_parent_algebra_exhibits_vs_forces(wp19)
    s3_ok = bool(
        wp12["fricke_cayley_hamilton_engine_verified"]
        and wp12["fk5_abelian_quotient_excluded_by_remainder"]
        and wp13["b1876_h1_h2_nonneg_unimodular_atoms_exact"]
        and wp19["b1879_exchange_192_doubling_and_end_dims_exact"]
        and wp19["contravariant_pullback_functoriality_exact"]
        and wp18["d5_d3_z4_glue_cosets_exact"]
        and wp18["mc_hyp_guardrail5_reconciled"]
    )
    say(f"Stage 3 (WP-1.2, WP-1.3, WP-1.8, WP-1.9): all_checks_hold={s3_ok}")

    # Stage 4
    wp14 = verify_wp14_swap_orientation_and_hand_exhaustion()
    wp33 = verify_wp33_paired_pole_and_cyclic_theta_theorems()
    wp35 = verify_wp35_anomalies_cusp_inflow_and_non_sm_modes()
    fl16 = verify_fl16_strong_cp_theta_bar_theorem()
    s4_ok = bool(
        wp14["r96_g192_orders_and_tau_exch_duality_exact"]
        and wp33["bare_j0_fails_while_theta_lj0_glues_and_pairs_exact"]
        and wp35["sm_16_perturbative_and_witten_anomaly_free"]
        and wp35["e8_6d_gs_quartic_factorization_exact"]
        and wp35["callan_harvey_cusp_inflow_exact"]
        and wp35["d09_roster_68_vs_70_and_non_sm_count_exact"]
        and fl16["haar_su3_and_u3_chiral_anomaly_invariance_verified"]
        and fl16["nelson_barr_det_real_nonzero_jarlskog_witness"]
    )
    say(f"Stage 4 (WP-1.4, WP-3.3, WP-3.5, FL:16): all_checks_hold={s4_ok}")

    # Stage 5
    wp17 = verify_wp17_quantum_number_dictionary_and_up_conjugate()
    wp34 = verify_wp34_cubic_overlaps_and_value_frame_comparison()
    wp25 = verify_wp25_stationary_source_generation_metric_and_lepton_factor()
    s5_ok = bool(
        wp17["wp17_dictionary_and_up_conjugate_verified"]
        and wp34["wp34_cubic_overlap_comparison_verified"]
        and wp25["wp25_source_metric_and_lepton_c_verified"]
    )
    say(f"Stage 5 (WP-1.7, WP-2.5, WP-3.4): all_checks_hold={s5_ok}")

    # Stage 6
    p6a = verify_part6a_kronecker_cusp_end_and_wp41()
    p6b = verify_part6b_whole_weave_transfer_and_p845()
    p6c = verify_part6c_level5_kashaev_and_2loop_rge()
    s6_ok = bool(
        p6a["part6a_kronecker_end_and_wp41_verified"]
        and p6b["part6b_whole_weave_and_p845_verified"]
        and p6c["part6c_level5_kashaev_and_rge_verified"]
    )
    say(f"Stage 6 (WP-1.6, WP-4.1, WP-4.2, WP-4.3): all_checks_hold={s6_ok}")

    # Stage 7 mathematical checks
    p7a = verify_b1604_flat_counting_dictionary_no_go()
    p7b = verify_upstream_epistemic_dag_and_fk_gates()
    su3_16, su2_16, y_16 = build_one_generation_16_sm_generators()
    anom_y3 = sum(y_16[i, i] ** 3 for i in range(16))
    anom_y1 = sum(y_16[i, i] for i in range(16))
    ledger = [("anchor_v", 1, 1, 0)] + [(f"ratio_{k}", 0, 0, 0) for k in range(19)]
    bp = audit_buckingham_pi_guardrail5_ledger(ledger, priced_imported_ratios=0)
    s7_ok = bool(
        p7a["b1604_flat_counting_no_go_verified"]
        and p7b["dag_and_fk_audit_verified"]
        and sum(p7b["layer_counts"]) == 83
        and len(su3_16) == 8
        and len(su2_16) == 3
        and anom_y3 == 0
        and anom_y1 == 0
        and bp["dimensionless_nullity"] == 19
        and bp["mass_dim_rank"] == 1
        and bp["guardrail5_compliant"]
    )
    say(
        f"Stage 7 (B1604 No-Go, 83-node DAG, Buckingham-Pi): "
        f"dag_nodes={sum(p7b['layer_counts'])}, layer_counts={p7b['layer_counts']}, "
        f"rank={bp['mass_dim_rank']}, nullity={bp['dimensionless_nullity']}; "
        f"all_checks_hold={s7_ok}"
    )

    overall = bool(p753_ok and s1_ok and s2_ok and s3_ok and s4_ok and s5_ok and s6_ok and s7_ok)
    say(f"Overall upstream mathematical suite (0 of 19): all_stages_hold={overall}")
    assert overall
    print("\n".join(lines))


if __name__ == "__main__":
    main()
