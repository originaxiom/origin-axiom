"""R24 direct mathematical locks; global analytic hypotheses remain explicit."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SPEC = importlib.util.spec_from_file_location('r24_test', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/global_mass_flux.py')
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def test_actual_twisted_connection_transports_both_spin_factors():
    r = m.spin_connection_bridge()
    assert r['connection_matches'] and r['antihermitian']
    assert r['mass_on_second_factor']
    assert r['missing_second_factor_rejected'] and r['wrong_spin_sign_rejected']


def test_generic_projector_curvature_equals_negative_secondary_euler_form():
    r = m.angular_identity()
    assert r['unit_identity'] == r['pauli_to_vector_residual'] == r['K_plus_Phi'] == 0
    assert r['projector_identity'] and r['spin_curvature_identity'] and r['tangent_curvature_identity']
    assert r['wrong_angular_sign_rejected'] and r['omitted_curvature_rejected']


def test_generic_mass_reversal_and_flat_stereographic_normalization():
    r = m.angular_identity()
    assert r['reversed_sum'] == r['flat_residual'] == 0
    assert r['flat_stereographic'] != 0


def test_two_coordinate_integrals_give_one_signed_unit_not_two():
    r = m.sphere_control()
    assert r['stereographic_flux'] == r['spherical_flux'] == -1
    assert r['reverse_flux'] == 1 and r['constant_mass_flux'] == 0
    assert 2*r['stereographic_flux'] != -1


def test_hyperbolic_levi_civita_connection_is_torsion_free():
    assert m.hyperbolic_control()['torsion'] == [{}, {}, {}]


def test_actual_horosphere_cancellation_detects_either_omitted_term():
    r = m.hyperbolic_control()
    assert r['K'] == 0
    assert sp.simplify(r['curvature_part']+r['projector_part']) == 0
    assert r['curvature_part'] != 0 and r['projector_part'] != 0
    assert r['omitted_curvature'] != r['K'] and r['omitted_covariant_DP'] != r['K']


def test_corner_crossing_is_transverse_and_tube_to_cap():
    r = m.corner_control()
    assert r['curve_orientation'] and r['positive_normal_derivative']
    assert r['normal_at_crossing'] == 0
    assert r['normal_endpoints'][0].is_negative and r['normal_endpoints'][1].is_positive
    assert r['q_positive_outward_tangent'].is_positive
    assert r['nonzero_normal_plane_norm'].is_positive


def test_reversing_charge_also_reverses_the_incoming_region_boundary():
    r = m.corner_control()
    assert r['q_negative_outward_tangent'] == r['q_positive_outward_tangent']
    assert r['wrong_negative_region_sign'] == -r['q_negative_outward_tangent']
    assert r['wrong_negative_region_sign'].is_negative


def test_general_arc_euler_additivity_keeps_excised_core_distinct():
    for k in (0, 1, 2, 3, 5, 9):
        for q in (-1, 1):
            r = m.topological_prediction(k, q)
            assert r['chi_Q'] == r['chi_C']+r['chi_N']-r['chi_T'] == 0
            assert r['chi_T']+r['chi_E'] == 2*r['chi_C']
            assert r['mass_flux'] == q*k == -r['vector_index']
            if k:
                assert r['unexcised_core_mutant_flux'] != r['mass_flux']
    for args in ((-1, 1), (1, 0), (sp.Rational(3, 2), 1), (True, 1)):
        with pytest.raises(ValueError):
            m.topological_prediction(*args)


def test_independent_cellular_pairs_agree_in_both_charge_sectors():
    for k in range(4):
        r = m.cellular_control(k)
        assert r['chi']['C'] == -k
        assert r['q_positive_flux'] == r['cochain_positive_flux'] == k
        assert r['q_negative_flux'] == r['cochain_negative_flux'] == -k
        for name, betti in r['betti'].items():
            assert sum((-1)**i*b for i, b in enumerate(betti)) == r['chi'][name]
        if k:
            assert r['betti']['relative_T'] == [0, k+1, 1, 0]
            assert r['betti']['relative_E'] == [0, 1, k+1, 0]


def test_changed_resolution_and_height_preserve_full_cohomology():
    coarse, fine = m.cellular_control(3), m.cellular_control(3, 8, 2)
    assert fine['chi'] == coarse['chi']
    assert fine['betti'] == coarse['betti']
    assert fine['q_positive_flux'] == 3 and fine['q_negative_flux'] == -3


def test_ball_constant_and_radial_fields_detect_disc_annulus_confusion():
    rows = m.ball_controls()
    assert [r['actual_flux'] for r in rows] == [0, -1, 1]
    for r in rows:
        assert r['actual_flux'] == r['chi_incoming']-r['chi_core']
    assert rows[0]['actual_flux'] != 0-rows[0]['chi_core']


def test_asymptotic_cap_and_tube_bounds_are_strict_not_fixed_rate_assumptions():
    r = m.cutoff_controls()
    assert r['cap_scaled_lower_bound'].is_positive
    assert r['tube_derivative_lower_bound'] == 1
    assert r['zero_b_negative_c'] == -2
    assert r['fixed_radius_counter_margins'] == [0, -3, -15]


def test_total_mass_flux_matches_actual_three_spinor_anomaly_without_cancelling_it():
    r = m.actual_anomaly_join()
    assert r['boundary_flux'] == 3
    assert sp.expand(r['boundary_I6']-r['previous_three_I6']) == 0
    assert r['linear_trace'] == r['cubic_trace'] == 48
    balance = r['constant_parameter_balance']
    assert balance['bulk'] == 0
    assert balance['local'] == balance['outer'] == balance['total'] == 3
