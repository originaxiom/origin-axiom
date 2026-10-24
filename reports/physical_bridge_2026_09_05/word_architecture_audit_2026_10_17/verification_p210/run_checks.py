"""P210 wrapper: infrastructure only until genuine strict admission.

The frozen runner retains its runtime, command, output and custody gates.
Synthetic fixture success is not permission to run the scientific module.
"""
from hashlib import sha256
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUNNER_SHA256 = "1cc1c9e299be3f85df41d066b2673c2c62b33e83ad978603f769cf04fd8adbf0"
EXPECTED = (
    "SymmetricResponseChecks.test_actual_symmetric_coupling_keeps_transpose_and_wrong_input",
    "SymmetricResponseChecks.test_full_q8_commutant_and_nonscalar_family_freedom",
    "SymmetricResponseChecks.test_four_cayley_planes_and_nonnull_wrong_graph",
    "SymmetricResponseChecks.test_all_eight_graded_family_involutions_and_conditional_indices",
    "SymmetricResponseChecks.test_null_graph_does_not_automatically_preserve_gamma",
    "SymmetricResponseChecks.test_48_state_covariances_and_frozen_state_rejection",
    "SymmetricResponseChecks.test_18_projector_paths_keep_opposite_limits_and_endpoint",
    "SymmetricResponseChecks.test_tail_clifford_green_grading_and_wrong_commuting_symbol",
    "SymmetricResponseChecks.test_both_decaying_slots_scalar_controls_and_zero_threshold",
    "SymmetricResponseChecks.test_actual_cusp_conjugation_and_retained_bump_normalization",
)


def main():
    source = HERE.parent / "verification_v3" / "run_checks.py"
    if sha256(source.read_bytes()).hexdigest() != RUNNER_SHA256:
        raise ValueError("Frozen infrastructure source hash differs; refuse import")
    spec = importlib.util.spec_from_file_location("p210_runner_infrastructure", source)
    infrastructure = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(infrastructure)
    infrastructure.HERE = HERE
    infrastructure.ENTRY = Path(__file__).resolve().relative_to(infrastructure.ROOT).as_posix()
    infrastructure.EXPECTED = EXPECTED
    return infrastructure.main()


if __name__ == "__main__":
    raise SystemExit(main())
