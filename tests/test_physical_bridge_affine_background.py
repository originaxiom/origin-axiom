"""R42 algebraic controls. No finite test certifies the global analytic proof."""
import importlib.util
from itertools import product
from pathlib import Path

import pytest
import sympy as s

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/affine_background.py'
spec = importlib.util.spec_from_file_location('r42_affine', PATH)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


@pytest.mark.parametrize('key', ['symmetric','trace_free','flat_blocks','bianchi',
                                'ricci','ricci_psi','norm_identity','codazzi','moment'])
def test_generic_tensor_identity(key):
    assert m.generic_controls()[key]


def test_cubic_parameterization_spans_seven_tracefree_symmetric_directions():
    c = m.cubic()
    values = [c(i,j,k) for i,j,k in product(range(3),repeat=3)]
    variables = sorted(set().union(*(v.free_symbols for v in values)), key=str)
    assert len(variables) == 7
    assert s.Matrix(values).jacobian(variables).rank() == 7
    assert all(m.clean(sum(c(i,i,k) for i in range(3))) == 0 for k in range(3))
    assert any(v != 0 for v in values)


def test_quartic_parameterization_has_nine_apolar_directions():
    t = m.quartic()
    values = [t(i,j,k,l) for i,j,k,l in product(range(3),repeat=4)]
    variables = sorted(set().union(*(v.free_symbols for v in values)), key=str)
    assert len(variables) == 9
    assert s.Matrix(values).jacobian(variables).rank() == 9
    assert m.divergence(t) == s.zeros(3)


def test_symmetric_without_apolarity_fails_trace_and_moment():
    _, ps = m.blocks(m.tensor({(0,0,0):s.S.One}))
    assert s.trace(ps[0]) == 1
    t = m.tensor({(0,0,0,0):s.S.One})
    assert all(x == 0 for x in m.codazzi(t))
    assert m.divergence(t) == s.diag(1,0,0)


def test_apolar_without_codazzi_does_not_imply_moment():
    c = m.tensor({(0,0,0):s.S.One,(0,1,1):-s.S.One})
    t = lambda i,j,k,l: c(j,k,l) if i==0 else s.S.Zero
    assert all(sum(t(i,j,k,k) for k in range(3)) == 0 for i,j in product(range(3),repeat=2))
    assert any(x != 0 for x in m.codazzi(t))
    assert m.divergence(t) == s.diag(1,-1,0)


def test_quadric_direct_coordinate_flat_and_moment():
    data = m.hyperbolic()
    assert all(a == s.zeros(4) for a in data['flat'])
    assert data['moment'] == s.zeros(4)
    assert data['norm'] == 6


def test_quadric_metric_compatibility_and_wrong_sign_control():
    data = m.hyperbolic()
    assert all(a == s.zeros(4) for a in data['compatible'])
    assert all(a == s.zeros(4) for a in data['self_adjoint'])
    wrong = m.hyperbolic(True)
    assert any(a != s.zeros(4) for a in wrong['flat'])
    assert any(a != s.zeros(4) for a in wrong['self_adjoint'])


def test_simplex_explicit_immersion_volume_and_nonzero_cubic():
    data = m.simplex()
    assert data['frame_det']**2 == 1
    assert all(a == s.zeros(4,1) for a in data['residuals'])
    assert data['cubic_norm'] == 6
    assert data['psi_norm'] == 12


def test_simplex_flat_connection_and_internal_ricci_balance():
    data = m.simplex()
    assert all(a == s.zeros(4) for a in data['commutators'])
    assert all(a == s.zeros(3) for a in data['curvature'].values())
    assert data['psi_norm'] != m.hyperbolic()['norm']


@pytest.mark.parametrize('key', ['relation','unipotent','determinant','commute','characteristic'])
def test_actual_linear_holonomy(key):
    assert m.holonomy()[key]


def test_actual_longitude_pairing_and_torus_formulas():
    data = m.holonomy()
    q = m.Q
    assert m.clean(data['mismatch']+(q-1/q)**3) == 0
    assert m.clean(data['torus_determinant']-(q-1)**3*(q**-3-1)) == 0
    assert data['mismatch'].subs(q,1) == 0
    assert data['mismatch'].subs(q,2) == -s.Rational(27,8)
    assert data['torus_determinant'].subs(q,1) == 0
    assert data['torus_determinant'].subs(q,2) != 0


def test_projective_scalar_rescaling_is_not_the_same_sl4_bundle():
    ell = m.holonomy()['longitude']
    assert m.clean((ell/m.Q).det()) == m.Q**-4
    assert m.clean(ell.det()) == 1


def test_positive_powers_retain_the_same_base_trace_obstruction():
    # Small exact powers are controls; the all-cover argument uses eigenvalues.
    ell = m.holonomy()['longitude'].subs(m.Q,2)
    for degree in (1,2,3):
        expected = -(s.Integer(2)**degree-s.Rational(1,2)**degree)**3
        assert s.trace(ell**degree)-s.trace(ell**(-degree)) == expected
        assert expected != 0
