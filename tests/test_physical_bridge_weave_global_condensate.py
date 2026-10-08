"""Actual bundle coefficients, full parent weights and common holonomy kernels."""
from pathlib import Path
import importlib.util
import pytest
import sympy as s

PACKET = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_global_condensate_2026_10_08'


def load(name):
    spec = importlib.util.spec_from_file_location('global_condensate_'+name, PACKET/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope='module')
def native():
    return load('probe')


def test_live_native_predicates(native):
    r = native.run()
    assert r['facts'] and all(r['facts'].values())
    assert r['predicates_passed'] == len(r['facts'])


def test_separate_phase_orbit_reference(native):
    r = load('reference').run()
    assert r['predicates'] and all(r['predicates'].values())
    assert r['global_profile'] == native.run()['global_profile']


def test_full_root_transport(native):
    f = native.run()['facts']
    assert f['Weyl_map_takes_old_weak_to_condensate'] and f['Weyl_map_fixes_color']
    assert f['Weyl_map_preserves_all_roots'] and f['transported_A5_chain']


def test_defining_six_is_actual_parent_embedding(native):
    f = native.run()['facts']
    assert f['transported_factors_commute'] and f['fundamental_six_Gram']
    assert f['fundamental_root_differences_faithful'] and f['whole248_roster_not_truncated']


def test_spin_root_gluing_cancels_globally(native):
    f = native.run()['facts']
    assert f['spin_line_transition_cancels_root_transition']
    assert f['space_dependent_connection_transition'] and f['dropped_transition_derivative_detected']
    assert f['four_flat_roots_for_each_extending_spin']


def test_all_global_vacuum_coefficients(native):
    f = native.run()['facts']
    assert f['global_spin_holomorphic_equation'] and f['curvature_connection_coefficient']
    assert f['hyperbolic_moment_globally_zero']


def test_core_orientation_not_arbitrary(native):
    f = native.run()['facts']
    assert f['Gauss_Bonnet_two_ideal_triangles'] and f['spin_peripheral_is_bounding']
    assert f['quarter_phase_sign_from_core_orientation'] and f['wrong_Stokes_sign_detected']


def test_actual_torus_compensator_and_quotient(native):
    f = native.run()['facts']
    assert f['torus_compensator_in_A5'] and f['actual_defining_compensator_phases']
    assert f['shared_SU2_SU6_center_on_every_root']


def test_noncommuting_flat_holonomies_in_SU6(native):
    A, B = native.matrices()
    assert native.zero(native.adj(A)*A-s.eye(6)) and native.zero(native.adj(B)*B-s.eye(6))
    assert native.zero(A.det()-1) and B.det() == 1
    assert not native.zero(A*B-B*A)
    assert native.zero(B**6+s.eye(6))


def test_holonomy_commutator_and_wrong_marking(native):
    f = native.run()['facts']
    assert f['actual_commutator_is_compensator'] and f['inverse_commutator_wrong_marking_detected']
    assert f['unsigned_cycle_control_rejected'] and f['SU6_center_matches_commutator_square']


def test_total_periphery_on_every_root(native):
    f = native.run()['facts']
    assert f['total_peripheral_on_every_root'] and f['compensator_order_four_not_two']
    assert f['omitting_spin_quarter_detected'] and f['wrong_spin_quarter_detected']
    assert f['finite_slice_phase_matches_local_end']


def test_actual_exterior_square_kernel(native):
    A, B = native.matrices()
    assert len(native.fixed(native.compound(A, 2), native.compound(B, 2))) == 1
    assert native.run()['facts']['invariant_skew_form']
    assert native.run()['facts']['skew_form_change_detected']


def test_fundamental_irreducible_does_not_delete_wedge_kernel(native):
    d = native.run()['global_profile']['invariant_dimensions']
    assert d == {'6': 0, '15': 1, '20': 0, '35': 0}
    assert native.run()['facts']['full_generators_not_only_commutator']


def test_exact_orbit_instrument_controls():
    r = load('reference')
    assert r.exterior_invariants(2) == [[(0, 3), (1, 4), (2, 5)]]
    assert len(r.exterior_invariants(2, (0,)*6)) > 1
    assert r.end_invariants() == [[(i, i) for i in range(6)]]


def test_complete_G2_root_system(native):
    f = native.run()['facts']
    assert f['full_unbroken_dimension14'] and f['unbroken_Cartan_exactly_two']
    assert f['all_unbroken_roots_multiplicity_one'] and f['full_G2_root_lengths']
    assert f['G2_Cartan_not_dimension_guess'] and f['full_G2_reflection_closed']


def test_global_energy_norms(native):
    f = native.run()['facts']
    assert f['global_Higgs_norm_finite_positive'] and f['separate_global_energy_terms_balance']


def test_global_core_does_not_delete_end_spectators(native):
    r = native.run()
    assert r['global_profile']['odd_cusp_spectators'] == 54
    assert r['facts']['unchanged_odd_spectators']


def test_actual_gauge_algebra_not_SM(native):
    assert native.run()['facts']['not_the_SM_algebra']
    assert native.run()['global_profile']['unbroken_rank'] == 2


def test_independent_root_set(native):
    exact = {tuple(2*x for x in b) for b in native.roots()}
    assert exact == load('reference').independent_roots()


def test_scope_no_generated_or_physical_completion(native):
    r = native.run()
    for k in ('physical_chiral_SM_derived', 'genesis_selects_background',
              'full_fermion_spectrum_derived', 'Einstein_equations_solved',
              'gapped_4D_reduction_derived', 'global_anomaly_acceptance', 'nonauthor_acceptance'):
        assert r[k] is False
