"""Bind six sealed controls to the unchanged strict/custody infrastructure."""
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUNNER_SHA256 = "1cc1c9e299be3f85df41d066b2673c2c62b33e83ad978603f769cf04fd8adbf0"
EXPECTED = (
    'GaugeResponseControls.test_01_weights_outward_flux_and_retained_moment_source',
    'GaugeResponseControls.test_02_poisson_equations_and_both_norm_branches',
    'GaugeResponseControls.test_03_green_divided_differences_and_response_norms',
    'GaugeResponseControls.test_04_static_shell_schur_and_both_riccati_laws',
    'GaugeResponseControls.test_05_cubic_power_overlap_and_nonabelian_colour_vertex',
    'GaugeResponseControls.test_06_curvature_finite_norm_and_remote_sector_control',
)


def main():
    source = (HERE.parents[1] / "word_architecture_audit_2026_10_17"
              / "verification_v3" / "run_checks.py")
    if sha256(source.read_bytes()).hexdigest() != RUNNER_SHA256:
        raise ValueError("Frozen infrastructure source hash differs; refuse import")
    spec = spec_from_file_location("gauge_response_runner_infrastructure", source)
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
