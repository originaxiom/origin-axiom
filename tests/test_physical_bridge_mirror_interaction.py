"""R33 exact controls. Passing these does NOT establish a quantum gap."""
import importlib.util
import itertools
from pathlib import Path

import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/mirror_interaction.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_mirror_interaction', PATH)
mi = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mi)


def test_clifford_charge_conjugation_and_actual_chiral_blocks():
    a = mi.algebra_controls()
    for key in ('hermitian_gamma', 'clifford', 'C_antisymmetric', 'C_unitary',
                'charge_conjugation', 'chirality_square', 'chirality_odd', 'yukawa_even'):
        assert a[key]
    for row in a['sectors'].values():
        assert row['dimension'] == 16 and row['symmetric']
        assert row['real_mass_identity'] and row['ward_all'] and row['ward_equations'] == 450


def test_weight_map_matches_actual_parent_not_just_dimension():
    g = mi.global_controls()
    for key in ('cartan_matched', 'psi_matches_positive', 'chi_matches_negative',
                'scalar_vector_weights', 'all_H_weights_integral', 'locking_weight_pairs'):
        assert g[key]
    assert g['charges'] == dict(psi=[1], chi=[-1], S=[2], Phi=4)
    # Switching D5 chiralities without conjugating the weights must fail.
    a = mi.clifford_data()['sectors']
    assert set(a[1]['weights']).isdisjoint(set(a[-1]['weights']))
    assert {tuple(-x for x in w) for w in a[1]['weights']} == set(a[-1]['weights'])
    assert g['scalar_charge_two_singlet_rejected']


def test_both_mirror_and_ordinary_yukawas_are_allowed():
    c = mi.global_controls()['monomial_charges']
    assert [c[k] for k in ('mirror_yukawa', 'ordinary_yukawa', 'phase_lock', 'dirac_pair')] == [0, 0, 0, 0]
    assert c['wrong_yukawa'] == 4 and c['neutral_vector_mirror'] == -2
    assert all(mi.algebra_controls()['sectors'][s]['ward_all'] for s in (1, -1))


def test_anomaly_does_not_disappear_by_discarding_mirrors():
    g = mi.global_controls()
    assert g['vectorlike_anomaly'] == 0
    assert g['full_H_light_anomaly'] != 0
    assert sp.expand(g['full_H_light_anomaly']+g['full_H_mirror_anomaly']) == 0
    assert g['pure_D5_cubic'] == g['pure_D5_linear'] == 0
    assert mi.ac.anomaly_controls()['factorization']


@pytest.mark.parametrize('sign', (1, -1))
def test_real_mass_identity_as_polynomial_coefficients(sign):
    yy = mi.clifford_data()['sectors'][sign]['yukawa']
    for a in range(10):
        for b in range(a, 10):
            assert yy[a].H*yy[b]+yy[b].H*yy[a] == 2*int(a == b)*sp.eye(16)
    assert yy[0].H != yy[0]  # Singular values, not Hermitian eigenvalues.
    mutant = yy.copy()
    mutant[0] = sp.zeros(16)
    assert mutant[0].H*mutant[0] != sp.eye(16)


@pytest.mark.parametrize('sign', (1, -1))
def test_full_45_generator_yukawa_not_only_cartan(sign):
    d = mi.clifford_data()['sectors'][sign]
    for (a, b), T in d['generators'].items():
        for c, yy in enumerate(d['yukawa']):
            assert T.T*yy+yy*T == int(c == a)*d['yukawa'][b]-int(c == b)*d['yukawa'][a]
    # A nonscalar distortion breaks a non-Cartan Ward identity.
    T = d['generators'][(0, 2)]
    bad = 2*d['yukawa'][0]
    assert T.T*bad+bad*T != d['yukawa'][2]


@pytest.mark.parametrize('sign', (1, -1))
def test_nonzero_complex_null_vector_has_eight_massless_components(sign):
    S = sp.Matrix([1, sp.I]+[0]*8)
    m = mi.mass_matrix(S, sign)
    assert (S.H*S)[0] == 2 and (S.T*S)[0] == 0
    assert m.rank() == 8
    assert (m.H*m).eigenvals() == {0: 8, 4: 8}
    row = mi.gap_controls()['sectors'][sign]
    assert row['complex_polynomial'] and row['complex_trace'] == 0
    a, b, c = sp.symbols('a b c', real=True)
    assert row['complex_discriminant'] == 4*a*a*b*b


@pytest.mark.parametrize('sign', (1, -1))
def test_real_rotated_and_collinear_complex_vectors_are_full_rank(sign):
    for S in ([sp.Rational(3, 5), sp.Rational(4, 5)]+[0]*8,
              [1+sp.I, 2+2*sp.I]+[0]*8):
        s = sp.Matrix(S)
        m = mi.mass_matrix(s, sign)
        assert mi.clean(m.H*m) == (s.H*s)[0]*sp.eye(16)


def test_phase_lock_stationary_point_hessian_and_broken_generators():
    d = mi.locking_controls()
    assert d['gradient'] == [0]*20 and d['hessian_matches']
    f, kappa, lam, v = sp.symbols('f kappa lambda v', positive=True)
    assert list(d['hessian'].diagonal()) == [2*lam*v*v]+[0]*9+[4*kappa*f]*10
    assert (d['real_target_dimension'], d['broken_vector_generators'], d['unbroken_vector_generators']) == (9, 9, 36)
    # Turning off locking makes all ten imaginary directions flat here.
    assert all(d['hessian'][j, j].subs(kappa, 0) == 0 for j in range(10, 20))


def test_charged_real_structure_is_gauge_covariant_and_requires_nonzero_phi():
    p = mi.phase_controls()
    assert p['involution'] and p['H_covariant'] and p['omitted_Phi_fails']
    n = sp.Matrix([1, 2]+[0]*8)
    z = (3+4*sp.I)/5
    assert mi.real_structure(mi.clean(z*z), z*n) == z*n
    with pytest.raises(ValueError):
        mi.real_structure(0, n)
    with pytest.raises(ValueError):
        mi.real_structure(2, n)


def test_fixed_condensate_and_dirac_mixing_do_not_leave_chiral_zero_modes():
    d = mi.gap_controls()['fixed_condensate_control']
    assert d['symmetric'] and d['rank'] == 32 and d['squared_mass_polynomial']
    assert d['squared_mass_trace'] == 16*17
    mu, M, e = sp.symbols('mu M e', real=True)
    assert d['two_by_two_charpoly'] == e**2-M*e-mu**2
    assert d['schur_mass'] == -mu**2/M
    # The decoupled control DOES have a light kernel; finite mixing removes it.
    yy = mi.clifford_data()['sectors'][-1]['yukawa'][0]
    decoupled = sp.diag(sp.zeros(16), 3*yy)
    assert decoupled.nullspace() and decoupled.rank() == 16


def test_inherited_c3_does_not_allow_one_nonzero_invariant_phi_on_all_arcs():
    p = mi.phase_controls()
    assert p['c3_Phi_invariant_arcs'] == [1, 1, 1]
    assert p['c3_charge12_natural_invariant_arcs'] == 3
    assert p['c3_coupling_phase_identities']
    # Independent flavour phases CAN compensate each arc: an added choice.
    assert all((4*j-j) % 3 == 0 for j in range(3))


@pytest.mark.parametrize('bad', ([0]*9, [0]*11, [0.5]+[0]*9))
def test_reject_wrong_dimension_or_inexact_mass_input(bad):
    with pytest.raises(ValueError):
        mi.mass_matrix(bad)


def test_reject_untyped_chiral_sign():
    with pytest.raises(ValueError):
        mi.mass_matrix([1]+[0]*9, 0)
