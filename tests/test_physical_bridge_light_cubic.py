"""R56 finite tensor/normalization tests; not independent PDE acceptance."""
from pathlib import Path
import importlib.util

path = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/light_cubic.py'
spec = importlib.util.spec_from_file_location('test_r56_cubic', path)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_actual_parent_weight_population_and_unique_pairing():
    row = v.representation()
    assert all(row['checks'].values())
    assert row['candidate_monomials'] == 6545
    assert row['zero_weight_monomials'] == {'SSS': 1, 'SQT': 16}
    assert row['commutant_dimension'] == 1


def test_pairing_requires_all_generators_not_only_weights():
    checks = v.representation()['checks']
    assert checks['literal_dual_Ward_all']
    assert checks['noninvariant_pairing_rejected']
    assert checks['generator_graph_connected']


def test_graded_primitive_and_its_mutations():
    assert all(v.neutral_controls().values())


def test_zero_integral_is_not_pointwise_zero():
    checks = v.neutral_controls()
    assert checks['cube_not_free_algebra_zero']
    assert checks['noncommuting_pointwise_trace_cube']


def test_cutoff_illustration_keeps_strict_endpoint():
    checks = v.neutral_controls()
    assert checks['scalar_tail_control_decays']
    assert checks['uncontrolled_endpoint_not_integrable']


def test_profile_phase_and_positive_metric_normalization():
    assert all(v.normalization_controls().values())


def test_oblique_coordinates_cannot_change_physical_magnitude():
    checks = v.normalization_controls()
    assert checks['oblique_pairing_metric_spectrum_preserved']
    assert checks['ordinary_oblique_spectrum_wrong']
    assert checks['changed_tensor_not_hidden_by_metric']


def test_formal_tensor_pairs_both_charged_sides():
    checks = v.normalization_controls()
    assert checks['formal_pairing_rank_sixteen']
    assert checks['formal_charged_hessian_rank_thirty_two']
    assert checks['formal_mass_zero_at_origin']


def test_pure_neutral_cubic_mutation_is_visible():
    checks = v.normalization_controls()
    assert checks['no_pure_neutral_cubic_in_polynomial']
    assert checks['mutation_pure_neutral_detected']


def test_finite_controls_do_not_promote_evidence_grade():
    out = v.report()
    assert out['all_checks_pass']
    assert not out['global_analytic_proof_machine_verified']
    assert not out['numerical_physical_coupling_computed']
    assert not out['full_EFT_or_nearby_pole_mass_derived']
    assert not out['physical_chirality_derived']
