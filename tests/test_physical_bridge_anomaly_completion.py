"""R21's actual weight/lattice/anomaly/mass/holonomy assertions."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SOURCE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/anomaly_completion.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_anomaly_completion', SOURCE)
ac = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ac)


def test_actual_global_subgroup_character_and_saturated_derived_group():
    r = ac.lattice_controls()
    assert r['singlet_character_row'] == sp.Matrix([[4, 3, 5, 6, 4, 2]])
    assert r['character_gcd'] == r['d5_coroot_saturation_index'] == 1
    assert r['d5_root_count'] == 40
    assert all(r['singlet_charges'][str(q)] == (q % 4 == 0) for q in range(-4, 13))


def test_root_datum_map_not_just_matching_dimensions():
    r = ac.lattice_controls()
    assert r['map_integral'] and r['inverse_integral'] and abs(r['map_determinant']) == 1
    assert r['direction_tripled'] and r['d5_roots_preserved'] and r['d5_metric_preserved']
    assert r['pullback_integral'] and r['actual_positive_spinor']
    assert r['pullback_charge_dimensions'] == {-2: 10, 1: 16, 4: 1}
    assert not r['no_swap_same_spinor']
    assert not r['no_swap_integral']


def test_full_anomaly_polynomial_factorization_and_live_mutant():
    r = ac.anomaly_controls()
    assert sp.expand(r['spinor_I6']-r['character']*r['X4']) == 0
    assert r['spinor_I6'] != 0 and r['general_copy_identity']
    assert r['orthonormal_spinor_count'] == 16 and r['independent_D5_identity']
    assert r['wrong_counterterm_nonzero'] and r['missing_singlet_nonzero']
    assert sp.expand(r['spinor_I6']+r['spectator_anomaly']) == 0


def test_integral_counterterm_has_an_explicit_global_pullback():
    r = ac.anomaly_controls()
    assert sp.expand(3*r['Q']-3*r['pullback_Q']+r['character']**2) == 0
    assert r['minimum_quadratic_level'] == 3
    assert r['levels'] == {'1': False, '2': False, '3': True, '6': True}
    assert r['spin_S2xS2_Q'] == sp.Rational(4, 3)
    assert r['spin_S2xS2_X4'] == 4
    assert r['one_copy_formal_X4'].q == r['two_copy_formal_X4'].q == 3
    assert ac.quadratic_level(ac.data()['C']) == 1


@pytest.mark.parametrize('n', [1, 2, 3, 9])
def test_completed_matter_is_anomaly_free_without_forcing_three(n):
    d = ac.data()
    assert ac.anomaly(d['spinor']+d['vector']+d['singlet'], n) == 0
    assert ac.anomaly(d['spinor'], n) != 0
    assert ac.anomaly_controls()['direct_pulled_27_anomaly'] == 0


def test_mass_terms_remove_only_added_real_spin10_representations():
    r = ac.mass_controls()
    assert r['vector_dimension'] == 10 and r['singlet_dimension'] == 1
    assert r['vector_D5_weights_self_dual']
    assert r['vector_mass_weight_cancellation'] and r['singlet_mass_weight_cancellation']
    assert r['spectator_components_for_three'] == 33
    assert r['wrong_mass_charge'] != 0
    assert r['radial_stationary'] == 0 and r['radial_mass_squared'].is_positive
    assert r['gauge_mass_squared'].is_positive
    assert r['vector_mass'].is_positive and r['singlet_mass'].is_positive
    assert not r['charge12_vector_mass_exponent'].is_Integer
    assert not r['charge12_singlet_mass_exponent'].is_Integer


def test_higgs_must_be_checked_on_the_unchanged_holonomy():
    r = ac.holonomy_controls()
    rows = {x['charge']: x for x in r['rows']}
    assert rows[4]['parallel_h0'] == rows[8]['parallel_h0'] == 0
    assert rows[0]['parallel_h0'] == rows[12]['parallel_h0'] == 1
    assert rows[4]['phases'] == rows[1]['phases'] == rows[-2]['phases']
    assert r['coprime'] == 1 and r['smallest_parallel_singlet_charge'] == 12
    assert r['residual_generator_character'] == sp.Rational(4, 3)


def test_residual_z3_anomaly_two_methods_and_completing_controls():
    r = ac.holonomy_controls()
    assert r['eta_single_charge'] == {'0': 0, '1': sp.Rational(1, 9), '2': -sp.Rational(1, 9)}
    assert r['eta_spinor_copies'] == {'1': sp.Rational(7, 9), '2': sp.Rational(5, 9), '3': sp.Rational(1, 3), '9': 0}
    assert r['independent_net_charge_mod9'] == 3
    assert r['eta_three_spinors_inverse'] == sp.Rational(2, 3)
    assert r['vectorlike_eta'] == 0
    assert all(x == 0 for x in r['completed_eta'].values())


def test_invalid_inputs_and_vectorlike_controls_are_not_vacuous():
    with pytest.raises(ValueError):
        ac.singlet_weight(4.0)
    with pytest.raises(ValueError):
        ac.quadratic_level(sp.Matrix([[1, 2], [0, 1]]))
    with pytest.raises(ValueError):
        ac.anomaly(ac.data()['spinor'], 0.5)
    assert ac.anomaly_controls()['vectorlike_anomaly'] == 0
    assert ac.lattice_controls()['scalar_from_cube']
