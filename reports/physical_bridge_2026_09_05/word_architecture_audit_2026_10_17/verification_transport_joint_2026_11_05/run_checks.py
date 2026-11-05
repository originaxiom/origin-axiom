"""Bind the declared joint packet to the frozen prospective/custody runner."""
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUNNER_SHA256 = "1cc1c9e299be3f85df41d066b2673c2c62b33e83ad978603f769cf04fd8adbf0"
EXPECTED = (
    'TransportEndChecks.test_full_root_central_phases_and_electromagnetic_lattice',
    'TransportEndChecks.test_actual_clifford_lift_of_d5_compensators',
    'TransportEndChecks.test_faithful_compensator_group_and_quotient_kernels',
    'TransportEndChecks.test_full_pin2_correction_and_retained_gauge_sectors',
    'TransportEndChecks.test_continuous_stabilizer_and_phase_constraint',
    'TransportEndChecks.test_based_and_all_word_holonomy_covariance',
    'TransportEndChecks.test_stationary_gluing_and_full_peripheral_table',
    'TransportEndChecks.test_actual_centralizer_mass_and_escaping_channel',
    'GeometricSpinSectorChecks.test_geometric_spin_pullback_and_based_group_scope',
    'GeometricSpinSectorChecks.test_complete_curve_mass_and_action_transport',
    'GeometricSpinSectorChecks.test_all_slot_half_root_coercivity',
    'GeometricSpinSectorChecks.test_periodic_and_cover_parity_controls',
    'GeometricSpinSectorChecks.test_bounded_end_split_and_four_slot_index_cancellation',
)


def main():
    source = HERE.parent / "verification_v3" / "run_checks.py"
    if sha256(source.read_bytes()).hexdigest() != RUNNER_SHA256:
        raise ValueError("Frozen infrastructure source hash differs; refuse import")
    spec = spec_from_file_location("joint_transport_runner_infrastructure", source)
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load frozen runner infrastructure")
    infrastructure = module_from_spec(spec)
    spec.loader.exec_module(infrastructure)
    infrastructure.HERE = HERE
    infrastructure.ENTRY = Path(__file__).resolve().relative_to(infrastructure.ROOT).as_posix()
    infrastructure.EXPECTED = EXPECTED
    return infrastructure.main()


if __name__ == "__main__":
    raise SystemExit(main())
