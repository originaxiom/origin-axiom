"""R25 exact controls; no assertion of a selected physical boundary sector."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SPEC = importlib.util.spec_from_file_location('r25_test', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/boundary_wall.py')
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def test_clifford_bridge_calibrates_boundary_sign_to_the_original_operator():
    r = m.chirality_bridge()
    assert r['clifford'] and r['boundary_chirality'] and r['factorization']
    assert all(r['right_internal_matches']) and all(r['r23_kinetic_matches'])
    assert r['normal_positive_rank'] == 4
    assert r['reversed_boundary_sign_rejected']


def test_two_sided_normalizability_selects_one_chirality_only_when_mass_crosses():
    assert m.scalar_crossing(-1, 1)['normalizable_chiralities'] == [1]
    assert m.scalar_crossing(1, -1)['normalizable_chiralities'] == [-1]
    for s in (-1, 1):
        assert m.scalar_crossing(s, s)['normalizable_chiralities'] == []
    with pytest.raises(ValueError):
        m.scalar_crossing(0, 1)


def test_actual_smooth_profile_solves_normal_equation_and_rejects_opposite_sign():
    r = m.smooth_normal()
    assert r['residual'] == 0 and r['opposite_residual'] != 0
    a = sp.Symbol('a', positive=True)
    assert r['right_log_slope'] == -a and r['left_log_slope'] == a
    assert all(x['difference'] == 0 for x in r['integer_integrals'])
    assert [x['integral'] for x in r['integer_integrals']] == [2, sp.Rational(4, 3), sp.Rational(16, 15), sp.Rational(32, 35)]


def test_reference_interpolation_is_not_the_original_traceless_mass():
    r = m.smooth_normal()
    assert r['trace_inside'] == 0 and r['trace_outside'] == 2
    assert r['identity_mass_coefficient'] != 0
    b = m.projected_connection()
    assert b['actual_wall_trace'] == 1+sp.Symbol('u', real=True)
    assert b['wall_inside'] and b['wall_outside']


def test_projected_connection_is_the_actual_negative_eigenline_connection():
    r = m.projected_connection()
    assert r['unit_vector'] == 1 and r['negative_projector'] and r['negative_mass_eigenvector']
    assert r['independent_residual'] == 0 and r['complementary_residual'] == 0
    assert r['omitted_connection_difference'] != 0
    assert r['off_diagonal_derivative_nonzero']
    assert r['flat_sphere_minus_flux'] == 1


@pytest.mark.parametrize('k', [-3, -1, 0, 1, 3])
def test_surface_spin_index_and_reference_flip(k):
    for g in (0, 1, 4, 7):
        for ref in (-1, 1):
            r = m.surface_index(k, g, ref)
            assert r['spin_index'] == -ref*k
            assert r['four_index'] == -k
            assert r['holomorphic_degree'] == -ref*k+g-1
            if g != 1:
                assert r['spin_omission'] != r['spin_index']


def test_sphere_cech_zero_modes_count_flux_not_flux_plus_one():
    for d in range(-4, 5):
        r = m.sphere_sections(d)
        assert r['index'] == d
        assert len(r['h0_monomials']) == max(d, 0)
        assert len(r['h1_laurent_powers']) == max(-d, 0)
    assert m.surface_index(3, 4)['holomorphic_degree'] == 0
    with pytest.raises(ValueError):
        m.surface_index(3, -1)
    with pytest.raises(ValueError):
        m.sphere_sections(sp.Rational(1, 2))


def test_actual_weight_anomaly_is_opposite_full_response_not_just_linear_term():
    r = m.anomaly_join()
    assert r['full_cancellation'] == 0
    assert r['missing_higher_terms'] != 0
    assert r['reduced_residual'] == 0 and r['reversed_reference_residual'] == 0
    assert r['three_spinor_residual'] == 0
    assert r['three_linear'] == 48 and r['three_cubic'] == 48


def test_constant_gauge_bulk_variation_does_not_replace_the_wall_sector():
    r = m.anomaly_join()
    assert r['constant_bulk']['bulk'] == 0
    assert r['constant_bulk']['total'] == 3
    assert r['compact_bulk']['total'] == 0
    assert sp.expand(r['reduced4']) != 0


def test_spatial_overlap_decouples_but_the_constant_gauge_mode_does_not():
    r = m.localization_controls()
    M, R, V, g7 = sp.symbols('M R V g7', positive=True)
    assert r['norm'] == 1
    assert sp.simplify(r['overlap']-(1+M*R)*sp.exp(-M*R)) == 0
    assert r['overlap_limit'] == 0
    assert r['constant_coupling'] == g7/sp.sqrt(V)
    assert r['constant_coupling_R_derivative'] == 0
    assert r['localized_gauge_limit'] == 0 and r['volume_divergence_control'] == 0


def test_cusp_measure_and_finite_lower_endpoint_do_not_erase_charge():
    r = m.localization_controls()
    M, R = sp.symbols('M R', positive=True)
    assert sp.simplify(r['half_norm']-(1-sp.exp(-2*M*R)/2)) == 0
    assert r['normalized_half_norm'] == 1 and r['cusp_measure_cancellation'] == 1
    assert r['local_escape'] == 0
