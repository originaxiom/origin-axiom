"""Live local equations and two root enumerators, not global existence tests."""
from pathlib import Path
import importlib.util
from fractions import Fraction as Q
import pytest

PACKET = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_cusp_condensate_2026_10_08'


def load(name):
    spec = importlib.util.spec_from_file_location('cusp_condensate_'+name, PACKET/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope='module')
def native():
    return load('probe')


def test_live_native_predicates(native):
    result = native.run()
    assert result['facts'] and all(result['facts'].values())
    assert result['predicates_passed'] == len(result['facts'])


def test_separate_reference_profile(native):
    result = load('reference').run()
    assert result['predicates'] and all(result['predicates'].values())
    assert result['end_profile'] == native.run()['end_profile']


def test_two_full_root_enumerations(native):
    assert native.roots() == load('reference').weyl_roots()
    assert len(native.roots()) == 240


def test_nonzero_all_vacuum_residuals(native):
    f = native.run()['facts']
    assert f['general_derivative'] and f['general_curvature'] and f['general_moment']
    assert f['nonzero_branch_fixed'] and f['all_nonzero_background_residuals_zero']


def test_controls_cannot_drop_backreaction(native):
    f = native.run()['facts']
    assert f['wrong_connection_detected'] and f['wrong_amplitude_detected']
    assert f['zero_origin_control'] and f['non_normal_condensate']


def test_curvature_balance_keeps_all_terms(native):
    f = native.run()['facts']
    assert f['spin_and_gauge_covariant_parallel']
    assert f['expanded_curvature_balance'] and f['dropping_curvature_energy_detected']


def test_same_spin_periphery_but_nonflat_holonomy(native):
    f = native.run()['facts']
    assert f['combined_spin_periphery_descends'] and f['slice_holonomy_not_fixed']


def test_finite_end_kinetic_and_graph_norms(native):
    f = native.run()['facts']
    assert f['finite_spin_kinetic_norm'] and f['finite_connection_kinetic_norm']
    assert f['baseline_graph_derivatives_finite'] and f['cusp_graph_cutoff_tail_vanishes']
    assert f['flat_critical_log_control_diverges']


def test_actual_R_hessian_and_unitary_radial_transport(native):
    f = native.run()['facts']
    assert f['R_moment_has_no_quadratic_term'] and f['radial_operator_with_kinetic_transport']
    assert f['radial_kinetic_is_unitary'] and f['mixed_potential_coefficient_from_action']


def test_sl2_scalar_thresholds_and_control(native):
    assert native.threshold(Q(1, 2), Q(1, 2)) == Q(1, 16)
    assert native.threshold(Q(1, 2), -Q(1, 2)) == Q(9, 16)
    assert native.threshold(Q(1), -Q(1)) == Q(5, 4)
    assert native.threshold(Q(0), Q(0)) == 0
    assert native.threshold(Q(1, 2), -Q(1, 2), Q(1, 4)) != Q(9, 16)


def test_polynomial_Gram_changes_adjoint():
    r = load('reference')
    assert r.polynomial_levels(2) == ([Q(1, 4), Q(1), Q(5, 4)], [Q(1), Q(1, 2), Q(1)])


def test_actual_peripheral_identification_not_just_dimensions(native):
    f = native.run()['facts']
    assert f['A5_actual_chain'] and f['A5_color_weak_orthogonal']
    assert f['actual_SU6_center_vector'] and f['actual_periphery_equal_on_every_root']
    assert f['different_torus_element_detected']


def test_gauge_breaking_explicit(native):
    f = native.run()['facts']
    assert f['chosen_root_preserves_color'] and f['chosen_root_breaks_old_weak']


def test_all_odd_root_condensates_bounded_population(native):
    f = native.run()['facts']
    assert f['odd_root_population'] and f['full_adjoint_sl2_decomposition']
    assert f['every_odd_root_same_threshold_histogram'] and f['every_odd_root_has_spectators']


def test_gapless_spectators_not_particles(native):
    profile = native.run()['end_profile']
    assert profile['R_threshold_histogram']['0'] == 54
    assert profile['free_spin_slot_channels'] == 108
    assert native.run()['facts']['spectator_root_brackets_vanish']
    assert native.run()['facts']['deleting_spectators_changes_population']


def test_threshold_sequence_is_form_quotient(native):
    f = native.run()['facts']
    assert f['derivative_cross_is_surface'] and f['Weyl_form_quotient']


def test_nonzero_angular_frequency_confining(native):
    assert native.run()['facts']['nonzero_angular_channel_confining']


def test_no_global_or_physical_promotion(native):
    result = native.run()
    for key in ('global_stationary_background_derived', 'full_fermion_spectrum_derived',
                'gapped_4D_reduction_derived', 'physical_chiral_SM_derived',
                'genesis_selects_condensate', 'global_anomaly_acceptance', 'nonauthor_acceptance'):
        assert result[key] is False
