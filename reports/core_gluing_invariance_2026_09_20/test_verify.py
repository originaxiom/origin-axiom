"""F07 tests distinguish preserved kernels, changed spectra, and changed ends/holonomy."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('core_gluing_invariance', Path(__file__).with_name('verify.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_reference_complex_and_contraction_are_nonvacuous():
    d = m.acyclic_complex()
    k = d.H
    assert d != s.zeros(4) and d*d == s.zeros(4) and k*k == s.zeros(4)
    assert d*k+k*d == s.eye(4)
    assert m.laplacian(d, s.eye(4)) == s.eye(4)
    assert d.rank() == 2 and d.nullspace() != []


def test_nondiagonal_complex_metric_has_exact_equivalence_constants():
    g = m.metric()
    assert g == g.H and g.is_positive_definite
    assert g.eigenvals() == {9: 1, 4: 1, 1: 1, s.Rational(1, 4): 1}
    assert (g-s.eye(4)/4).is_positive_semidefinite
    assert (9*s.eye(4)-g).is_positive_semidefinite


def test_new_adjoint_and_laplacian_use_the_new_metric():
    d, g = m.acyclic_complex(), m.metric()
    star = m.adjoint(d, g)
    assert g*star == d.H*g
    assert star != d.H
    lap = m.laplacian(d, g)
    assert g*lap == lap.H*g
    assert lap != s.eye(4)
    lam = s.symbols('lambda')
    expected = (lam-s.Rational(2, 9))**2*(lam-s.Rational(1, 8))**2
    assert s.factor(lap.charpoly(lam).as_expr()-expected) == 0
    assert lap.det() != 0


def test_same_homotopy_remains_bounded_and_gap_bound_holds():
    d, g = m.acyclic_complex(), m.metric()
    k = d.H
    assert d*k+k*d == s.eye(4)
    assert (36*g-k.H*g*k).is_positive_semidefinite
    assert (g*m.laplacian(d, g)-g/36).is_positive_semidefinite


def test_new_orthogonality_not_old_orthogonality_controls_the_proof():
    d, g = m.acyclic_complex(), m.metric()
    exact = s.Matrix.hstack(*d.columnspace())
    star = m.adjoint(d, g)
    coexact = s.Matrix.hstack(*star.columnspace())
    assert exact.H*g*coexact == s.zeros(2)
    assert exact.H*coexact != s.zeros(2)
    assert s.Matrix.hstack(exact, coexact).rank() == 4
    assert star*coexact == s.zeros(4, 2)


def test_metric_family_saturates_the_bound_without_a_finite_zero():
    t = s.symbols('t', positive=True)
    d = s.Matrix([[0, 0], [1, 0]])
    g = s.diag(t**2, 1)
    lap = m.laplacian(d, g)
    assert lap == s.eye(2)/t**2
    assert lap.det() == t**-4
    assert s.limit(lap[0, 0], t, s.oo) == 0
    # For t>=1, m=1 and M=t^2. Equivalence is not uniform in t.
    assert s.simplify(lap[0, 0]-1/t**2) == 0


def test_bounded_nonunitary_chain_map_is_not_fixed_norm_dirac_conjugacy():
    d = m.acyclic_complex()
    t = s.diag(2, s.Matrix([[1, s.I], [0, 3]]), s.Rational(1, 2))
    new_d = m.chain_change(d, t)
    new_k = m.chain_change(d.H, t)
    assert new_d*new_d == s.zeros(4)
    assert new_d*new_k+new_k*new_d == s.eye(4)
    new_q = new_d+new_d.H
    assert new_q != t.inv()*(d+d.H)*t
    assert new_q.det() != 0


def test_changing_the_differential_can_create_zeros_without_a_chain_isomorphism():
    d = m.acyclic_complex()
    changed = s.zeros(4)
    assert changed*changed == s.zeros(4)
    assert m.laplacian(changed, s.eye(4)) == s.zeros(4)
    assert changed.rank() != d.rank()
    assert changed*d.H+d.H*changed != s.eye(4)


def test_nonflat_differential_is_outside_the_comparison():
    epsilon = s.symbols('epsilon', nonzero=True)
    d = m.acyclic_complex()
    d[2, 0] = epsilon
    assert (d*d)[3, 0] == epsilon and d*d != s.zeros(4)


def test_circle_holonomy_control_changes_the_entire_two_degree_kernel():
    n = s.symbols('n', integer=True)
    alpha = s.symbols('alpha', real=True)
    q = m.circle_dirac(n, alpha)
    assert q == q.H and q*q == (n+alpha)**2*s.eye(2)
    assert m.circle_dirac(0, 0) == s.zeros(2)
    assert m.circle_dirac(0, s.Rational(1, 2))**2 == s.eye(2)/4
    assert m.circle_dirac(-1, s.Rational(1, 2))**2 == s.eye(2)/4
    assert s.expand(4*(n+s.Rational(1, 2))**2-(2*n+1)**2) == 0
    assert s.exp(2*s.pi*s.I*s.Rational(1, 2)) == -1
    assert s.exp(2*s.pi*s.I*0) == 1


def test_nonperiodic_circle_gauge_cannot_be_used_as_a_bounded_global_chain_map():
    theta = s.symbols('theta', real=True)
    transport = s.exp(s.I*theta/2)
    assert s.diff(transport, theta) == s.I*transport/2
    assert transport.subs(theta, 2*s.pi) == -transport.subs(theta, 0)


def test_unbounded_end_gauge_preserves_ordinary_flatness_but_not_L2_kernel():
    x = s.symbols('x', real=True)
    u = s.Function('u')(x)
    gauge = s.exp(x*x/2-x)
    transported = (s.diff(gauge*u, x)+gauge*u)/gauge
    assert s.simplify(transported-s.diff(u, x)-x*u) == 0
    assert s.limit(gauge, x, s.oo) == s.oo
    gaussian = s.exp(-x*x/2)
    assert s.simplify(s.diff(gaussian, x)+x*gaussian) == 0
    assert s.integrate(gaussian**2, (x, -s.oo, s.oo)) == s.sqrt(s.pi)
    old_d = s.diff(u, x)+u
    old_laplacian = -s.diff(old_d, x)+old_d
    assert s.simplify(old_laplacian+s.diff(u, x, 2)-u) == 0
    new_d = s.diff(u, x)+x*u
    new_laplacian = -s.diff(new_d, x)+x*new_d
    assert s.simplify(new_laplacian+s.diff(u, x, 2)-(x*x-1)*u) == 0


@pytest.mark.parametrize('degree', [0, 1, 2, 3])
def test_form_norm_comparison_includes_volume_and_degree(degree):
    b, c = s.symbols('b c', positive=True)
    weights = m.form_norm_density(b*b*s.eye(3), c*c, degree)
    assert all(s.simplify(weight-c**2*b**(3-2*degree)) == 0 for weight in weights)


def test_degreewise_metric_scaling_is_not_only_the_fiber_metric():
    lengths = (2, 3, 5)
    g = s.diag(*(length**2 for length in lengths))
    assert m.form_norm_density(g, 1, 0) == (30,)
    assert m.form_norm_density(g, 1, 1) == (s.Rational(15, 2), s.Rational(10, 3), s.Rational(6, 5))
    assert m.form_norm_density(g, 1, 3) == (s.Rational(1, 30),)
