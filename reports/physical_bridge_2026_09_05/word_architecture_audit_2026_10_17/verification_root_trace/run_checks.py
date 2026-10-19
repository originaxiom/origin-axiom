"""Reuse the pinned admission/custody runner without changing frozen v3.

Only infrastructure is imported here. Scientific checks.py is imported
by the reused runner only after real strict prospective admission.
"""
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = (
    "RootTraceChecks.test_actual_quaternion_group_and_central_sign",
    "RootTraceChecks.test_based_fourth_power_retains_inverse_hidden_by_quaternion_image",
    "RootTraceChecks.test_root_period_maps_and_noncommuting_control",
    "RootTraceChecks.test_modular_maps_normalize_actual_cover_lattice",
    "RootTraceChecks.test_joint_minus_period_marking_obeys_actual_based_conjugations",
    "RootTraceChecks.test_modular_central_relations_keep_branch_lemma_explicit",
    "RootTraceChecks.test_combined_line_and_epsilon_compensation",
    "RootTraceChecks.test_trace_sequence_has_two_nonzero_charts_and_zero_control",
    "RootTraceChecks.test_residue_pullback_keeps_ramification_and_derivative_factor",
    "RootTraceChecks.test_cover_regular_scalar_form_and_spin_are_different_types",
    "RootTraceChecks.test_coordinate_domains_both_kernels_via_independent_intersections",
    "RootTraceChecks.test_special_theta_domains_and_rank_jump_are_not_generic_sampling",
    "RootTraceChecks.test_actual_cauchy_and_extreme_domains_preserve_green_form",
    "RootTraceChecks.test_full_doublet_quartet_projection_retains_both_pieces",
    "RootTraceChecks.test_flat_transport_removes_only_constant_sector_ratio",
    "RootTraceChecks.test_all_critical_residue_ranks_keep_same_holonomy_but_change_degree",
    "RootTraceChecks.test_smooth_traceless_cap_has_curvature_without_determinant_flux",
    "RootTraceChecks.test_trace_flux_energy_bound_and_traceless_countercontrol",
)


def main():
    source = HERE.parent / "verification_v3" / "run_checks.py"
    spec = importlib.util.spec_from_file_location("root_trace_runner_infrastructure", source)
    infrastructure = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(infrastructure)
    # Explicitly rebind only the existing runner's experiment parameters.
    # Its admission, exact-command/output checks and custody policy are unchanged.
    infrastructure.HERE = HERE
    infrastructure.ENTRY = Path(__file__).resolve().relative_to(infrastructure.ROOT).as_posix()
    infrastructure.EXPECTED = EXPECTED
    return infrastructure.main()


if __name__ == "__main__":
    raise SystemExit(main())
