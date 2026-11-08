"""Bind seven sealed controls to the unchanged strict/custody infrastructure."""
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUNNER_SHA256 = "1cc1c9e299be3f85df41d066b2673c2c62b33e83ad978603f769cf04fd8adbf0"
EXPECTED = (
    "RegisterArchitectureControls.test_01_cover_basis_and_oriented_flow",
    "RegisterArchitectureControls.test_02_lost_order_and_independent_heisenberg_replay",
    "RegisterArchitectureControls.test_03_independent_degree_two_commutators",
    "RegisterArchitectureControls.test_04_higher_order_inverse_and_syllable_guards",
    "RegisterArchitectureControls.test_05_native_transport_in_both_composition_orders",
    "RegisterArchitectureControls.test_06_finite_a5_register_is_not_the_relative_truncation",
    "RegisterArchitectureControls.test_07_finite_inner_lifted_joint_scope_control",
)


def main():
    source = (HERE.parents[1] / "word_architecture_audit_2026_10_17"
              / "verification_v3" / "run_checks.py")
    if sha256(source.read_bytes()).hexdigest() != RUNNER_SHA256:
        raise ValueError("Frozen infrastructure source hash differs; refuse import")
    spec = spec_from_file_location("architecture_runner_infrastructure", source)
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
