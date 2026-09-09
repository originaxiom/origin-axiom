"""Direct locks for path-local R23; global analytic qualifications are not finite tests."""
import importlib.util
import itertools
from pathlib import Path

import pytest
import sympy as sp

SPEC = importlib.util.spec_from_file_location('r23_test', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/mass_inflow.py')
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def test_actual_prior_differential_has_the_clifford_mass_symbol():
    r = m.actual_symbol()
    assert r['symbol_matches']
    assert r['wrong_codifferential_rejected']


def test_even_form_map_exhibits_two_commuting_clifford_actions():
    r = m.clifford_map()
    assert r['J_unitary'] and r['J_odd'] and r['pair_anticommutators']
    assert r['hermitian'] and r['clifford'] and r['commuting']
    assert r['G_product'] == -sp.I*sp.eye(4)
    assert r['T_product'] == sp.I*sp.eye(4)


def test_unitary_intertwiner_acts_on_every_kinetic_and_mass_matrix():
    r = m.clifford_map()
    assert r['seed_rank'] == 1 and r['unitary']
    for i in range(3):
        assert r['kinetic_map'][i] == -sp.kronecker_product(m.PAULI[i], sp.eye(2))
        assert r['mass_map'][i] == sp.kronecker_product(sp.eye(2), m.PAULI[i])
        assert r['kinetic_map'][i] != r['mass_map'][i]


def test_the_same_map_preserves_the_natural_twisted_rotation_action():
    r = m.clifford_map()
    assert len(r['rotation_matches']) == 3 and all(r['rotation_matches'])
    assert len(r['rotation_actions']) == 18 and all(r['rotation_actions'])


def test_all_morse_signs_have_the_actual_gaussian_zero_mode_and_chirality():
    for signs in itertools.product((-1, 1), repeat=3):
        r = m.morse_control(tuple((i+1)*s for i, s in enumerate(signs)))
        assert r['operator_residual'] == {}
        assert r['degree'] == signs.count(-1)
        assert r['zero_basis'] == [r['basis']]
        assert all(e >= 0 for e in r['ground_energies'])
        assert r['left_minus_right'] == -r['determinant_sign']
        assert r['norm_squared'] > 0
    with pytest.raises(ValueError):
        m.morse_control((1, 0, -1))


def test_harmonic_saddles_and_source_reversal_reverse_local_chirality():
    first, second = m.morse_control((-2, 1, 1)), m.morse_control((2, -1, -1))
    assert sum(first['eigenvalues']) == sum(second['eigenvalues']) == 0
    assert first['degree'] == 1 and second['degree'] == 2
    assert first['left_minus_right'] == 1 and second['left_minus_right'] == -1


def test_charged_reality_gives_one_determinant_not_two_or_a_square_root():
    r = m.reality_control()
    assert all(row['identity'] and row['double_count_rejected'] and row['extra_square_root_rejected'] for row in r['blocks'])
    assert r['real_components_per_charged_pair'] == 2*r['complex_components_in_one_representative']
    assert r['complex_components_in_one_representative'] == 2*r['seven_dimensional_Dirac_size']
    with pytest.raises(ValueError):
        m.pfaffian(sp.eye(2))


def test_berry_line_has_unit_chiral_flux_and_reverses():
    r = m.angular_form()
    theta = next(s for s in r['K_theta_phi'].free_symbols if str(s) == 'theta')
    assert r['projector_identity']
    assert sp.simplify(r['K_theta_phi']+sp.sin(theta)/(4*sp.pi)) == 0
    assert r['sphere_flux'] == -1
    assert sp.simplify(r['reversed']+r['K_theta_phi']) == 0
    assert 2*r['sphere_flux'] != -1


def test_position_dependent_frame_and_curvature_terms_are_not_dropped():
    r = m.angular_form()
    assert sp.simplify(r['frame_covariant']-r['K_theta_phi']) == 0
    assert sp.simplify(r['omitted_connection']-r['K_theta_phi']) != 0
    assert r['constant_projector_curved'] == -1/(2*sp.pi)


def test_odd_superconnection_has_the_same_normalized_flux():
    r = m.superconnection_form()
    assert r['cubic_trace'] == 12*sp.I
    assert r['normalized_coefficient'] == -1/sp.pi**sp.Rational(3, 2)
    assert r['gaussian_integral'] == m.angular_form()['sphere_flux']
    assert r['wrong_ungraded_sign'] != r['normalized_coefficient']


def test_smooth_angular_primitive_retains_its_outer_boundary():
    r = m.superconnection_form()
    assert r['primitive_derivative'] == 0
    assert r['zero_limit'] == 0 and r['infinity_limit'] == 1
    assert r['radial_integral'] == -1
    assert r['radial_integral'] != -r['zero_limit']


def test_anisotropic_linear_mass_controls_match_the_morse_orientation():
    for A in (sp.diag(1, 2, 3), sp.diag(-2, 1, 1), sp.diag(2, -1, -1),
              sp.Matrix([[1, 1, 0], [0, 2, 1], [0, 0, 3]])):
        r = m.linear_flux(A)
        assert abs(r['flux']-r['expected']) < 1e-9
        assert r['numerical_only']
    with pytest.raises(ValueError):
        m.linear_flux(sp.zeros(3))


def test_same_sign_mass_and_reference_regulator_are_discriminating():
    assert m.response_eigenvalues(1, 1) == dict(angular=0, regulator=0)
    assert m.response_eigenvalues(-1, -1) == dict(angular=0, regulator=-2)
    assert m.response_eigenvalues(1, -1) == dict(angular=1, regulator=-1)
    assert m.response_eigenvalues(-1, 1) == dict(angular=-1, regulator=-1)
    assert m.anomaly_forms()['I8'] != 0
    with pytest.raises(ValueError):
        m.response_eigenvalues(0, 1)


def test_descent_sign_is_computed_in_exterior_algebra():
    r = m.descent_sign()
    assert r['correct'] and r['wrong_sign_rejected']
    assert r['dK_I4'] and r['K_dI4']


def test_constant_gauge_zero_mode_keeps_the_actual_three_spinor_anomaly():
    r = m.boundary_balance([1, 1, 1], [1, 1, 1], 1)
    a = m.anomaly_forms()
    assert r['local'] == 3 and r['bulk'] == 0 and r['total'] == 3
    assert sp.expand(r['total']*a['one_I6']-a['three_I6']) == 0
    assert a['three_I6'] != 0
    assert a['one_linear_trace'] == a['one_cubic_trace'] == 16
    assert sp.expand(a['one_I6']+a['conjugate_I6']) == 0
    assert r['fake_total_after_dropping_outer'] != r['total']


def test_compact_support_and_zero_total_controls_really_cancel():
    supported = m.boundary_balance([1, 1, 1], [1, 1, 1], 0)
    assert supported['local'] == 3 and supported['bulk'] == -3 and supported['total'] == 0
    opposite = m.boundary_balance([1, -1], [1, 1], 1)
    assert opposite['total'] == opposite['local'] == opposite['outer'] == 0
    varying = m.boundary_balance([1, -1], [2, 5], 1)
    assert varying['local'] == -3 and varying['bulk'] == 3 and varying['total'] == 0


def test_acyclic_whole_torus_does_not_force_zero_disc_relative_index():
    for z in (sp.I, m.prior.ZETA):
        for k in (1, 2, 3):
            r = m.partition_control(z, k)
            assert r['whole_torus'] == (0, 0, 0)
            assert r['solid_torus'] == (0, 0, 0, 0)
            assert r['disc_relative'] == (0, k, 0, 0)
            assert r['relative_euler'] == -k


def test_annular_and_trivial_character_controls_preserve_the_scope():
    for z in (sp.I, m.prior.ZETA, 1):
        r = m.partition_control(z)
        assert r['essential_annulus_relative'] == (0, 0, 0, 0)
        if z == 1:
            assert r['whole_torus'] == (1, 2, 1)
            assert r['solid_torus'] == (1, 1, 0, 0)
            assert r['disc_relative'] == (0, 1, 0, 0)
    with pytest.raises(ValueError):
        m.betti((1, 1, 1), [sp.eye(1), sp.eye(1)])
