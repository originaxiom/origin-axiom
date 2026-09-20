"""F04 load-bearing identities and discriminating countercontrols."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('full_flag_controls', Path(__file__).with_name('verify.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_exact_representation_and_unit_modulus_flag_characters():
    assert v.word('aabaBaaBab') == s.eye(4)
    for matrix in v.generators():
        assert matrix.is_upper
        for diagonal in matrix.diagonal():
            assert s.simplify(s.expand_complex(diagonal*s.conjugate(diagonal))) == 1
        assert s.simplify(s.expand_complex(matrix.det()*s.conjugate(matrix.det()))) == 1


def test_regular_unipotent_flag_is_the_standard_flag():
    b = v.generators()[1]
    powers = [v.clean((b-s.eye(4))**r) for r in range(1, 5)]
    assert [matrix.rank() for matrix in powers] == [3, 2, 1, 0]
    for r, matrix in enumerate(powers, 1):
        assert matrix[:, :r] == s.zeros(4, r)
        assert len(matrix.nullspace()) == r


@pytest.mark.parametrize('text,sign', [('AbAA', -1), ('babA', 1)])
def test_actual_normalized_peripheral_exponentials(text, sign):
    j = v.jordan_generator()
    assert j**4 == s.zeros(4)
    assert v.word(text) == v.nil_exp(sign*j)
    assert v.nil_exp(j)*v.nil_exp(-j) == s.eye(4)


def test_leading_principal_determinants_are_metric_flag_coordinates():
    n, _, d, _ = v.generic_cholesky_data()
    h = v.clean(n.conjugate().T*d*n)
    assert h == h.conjugate().T
    assert h.det() == 1
    assert all(d[i, i] > 0 for i in range(4))
    for r in range(1, 5):
        assert s.simplify(h[:r, :r].det()) == s.prod(d[i, i] for i in range(r))
    # Induced rank-two Cholesky ratios would require D11=D22^3.
    assert d[0, 0] != d[1, 1]**3


@pytest.mark.parametrize('generator_index', [0, 1])
def test_full_generator_equivariance_and_flag_determinants(generator_index):
    n, _, d, _ = v.generic_cholesky_data()
    h = v.clean(n.conjugate().T*d*n)
    matrix = v.generators()[generator_index]
    inverse = v.clean(matrix.inv())
    delta = s.diag(*matrix.diagonal())
    transformed_n = v.clean(delta*n*inverse)
    transformed_h = v.clean(inverse.conjugate().T*h*inverse)
    assert transformed_n.is_upper
    assert list(transformed_n.diagonal()) == [1, 1, 1, 1]
    assert v.clean(transformed_h-transformed_n.conjugate().T*d*transformed_n) == s.zeros(4)
    for r in range(1, 5):
        assert s.simplify(s.expand_complex(transformed_h[:r, :r].det()-h[:r, :r].det())) == 0


def test_simple_root_additive_periods_allow_all_other_coordinates():
    variables = s.symbols('n12 n13 n14 n23 n24 n34')
    n = s.eye(4)
    for indices, variable in zip(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)), variables):
        n[indices] = variable
    j = v.jordan_generator()
    for sign in (-1, 1):
        transformed = n*v.nil_exp(sign*j)
        for i in range(3):
            assert s.expand(transformed[i, i+1]-n[i, i+1]) == sign*j[i, i+1]
    dn = s.zeros(4)
    for i in range(4):
        for k in range(i+1, 4):
            dn[i, k] = s.Symbol(f'dn{i}{k}')
    theta = dn*n.inv()
    for i in range(3):
        assert theta[i, i+1] == dn[i, i+1]


def test_full_trace_metric_in_six_complex_root_directions():
    d_values = s.symbols('d1:5', positive=True)
    diagonal_velocities = s.symbols('v1:5', real=True)
    d = s.diag(*d_values)
    theta = s.zeros(4)
    for i in range(4):
        for j in range(i+1, 4):
            re, im = s.symbols(f'x{i}{j} y{i}{j}', real=True)
            theta[i, j] = re+s.I*im
    current = s.diag(*diagonal_velocities)+d.inv()*theta.conjugate().T*d+theta
    direct = s.trace(current*current)
    expected = v.root_metric(d, diagonal_velocities, theta)
    assert s.simplify(s.expand(direct-expected)) == 0


def test_nontrivial_cholesky_coordinates_require_right_maurer_cartan():
    n, dn, d, dt = v.generic_cholesky_data()
    dd = d*s.diag(*dt)
    h = n.conjugate().T*d*n
    dh = dn.conjugate().T*d*n+n.conjugate().T*dd*n+n.conjugate().T*d*dn
    current = v.clean(h.inv()*dh)
    exact = s.simplify(s.expand_complex(s.trace(current*current)))
    right_value = v.root_metric(d, dt, dn*n.inv())
    wrong_value = v.root_metric(d, dt, n.inv()*dn)
    assert exact == right_value
    assert exact > 0
    assert exact != wrong_value
    assert s.trace(current) == 0


def test_harmonic_central_normalization_current_and_trace_split():
    r = s.symbols('r', real=True)
    w = s.Function('w')(r)
    q = s.Function('q')(r)
    j = v.jordan_generator()
    n = v.nil_exp(r*j)
    d = s.diag(s.exp(q), s.exp(-q), 1, 1)
    normalized = n.T*d*n
    h = s.exp(w/4)*normalized
    normalized_inverse = v.nil_exp(-r*j)*d.inv()*v.nil_exp(-r*j.T)
    current = (s.exp(-w/4)*normalized_inverse*h.diff(r)).applyfunc(s.simplify)
    normalized_current = (normalized_inverse*normalized.diff(r)).applyfunc(s.simplify)
    assert (current-normalized_current-s.diff(w, r)*s.eye(4)/4).applyfunc(s.simplify) == s.zeros(4)
    assert s.simplify(s.trace(normalized_current)) == 0
    assert s.simplify(s.trace(current*current)-s.trace(normalized_current*normalized_current)-s.diff(w, r)**2/4) == 0
    # The differential identity works for arbitrary w; harmonicity is used
    # analytically in PROOF to make the divergence of its central term zero.
    assert s.simplify(h.det()-s.exp(w)) == 0


def test_euler_derivatives_and_positive_flag_sources():
    t, roots, potential = v.root_potential()
    sources = [s.diff(potential, coordinate) for coordinate in t]
    assert s.simplify(sum(sources)) == 0
    flags = []
    for r in range(1, 4):
        expected = sum(s.exp(t[i]-t[j])*coefficient
                       for (i, j), coefficient in roots.items() if i < r <= j)
        assert s.simplify(sum(sources[:r])-expected) == 0
        flags.append(expected)
    weighted = sum((j-i)*s.exp(t[i]-t[j])*coefficient
                   for (i, j), coefficient in roots.items())
    assert s.simplify(sum(flags)-weighted) == 0
    assert s.simplify(sum(flags)-potential) != 0  # higher roots count more than once


def test_diagonal_variation_uses_correct_laplacian_sign():
    r = s.symbols('r', real=True)
    t, _, potential = v.root_potential()
    velocities = s.symbols('v1:5', real=True)
    accelerations = s.symbols('a1:5', real=True)
    density = s.exp(-2*r)
    lagrangian = density*(sum(x*x for x in velocities)/2+potential)
    for i in range(4):
        momentum = s.diff(lagrangian, velocities[i])
        el = s.diff(momentum, r)+sum(s.diff(momentum, velocities[j])*accelerations[j] for j in range(4))-s.diff(lagrangian, t[i])
        assert s.simplify(el/density-(accelerations[i]-2*velocities[i]-s.diff(potential, t[i]))) == 0


def test_cartan_inverse_and_weighted_am_gm_constants():
    c = s.Matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    weights = c.inv()*s.ones(3, 1)
    assert weights == s.Matrix([s.Rational(3, 2), 2, s.Rational(3, 2)])
    assert sum(weights) == 5
    b = s.Matrix(s.symbols('b1:4', real=True))
    assert s.expand((weights.T*c*b)[0]-sum(b)) == 0
    alpha = weights/5
    coefficients = [3, 4, 3]
    assert [coefficients[i]/alpha[i] for i in range(3)] == [10, 10, 10]
    # z_i=10 log x_i turns the weighted exponential inequality into an
    # exact homogeneous polynomial inequality. These are controls; the
    # all-positive-input statement is convexity of exp in PROOF.
    for x, expected_gap in [((1, 1, 1), 0), ((2, 2, 2), 0), ((2, 1, 1), 2999)]:
        gap = sum(coefficients[i]*x[i]**10 for i in range(3))-10*x[0]**3*x[1]**4*x[2]**3
        assert gap == expected_gap


def test_peripheral_energy_constants_and_coordinate_change():
    h0 = s.Matrix([[2, 1], [1, 3]])
    period = s.Matrix([1, -1])
    k = (period.T*h0.inv()*period)[0]
    assert k == s.Rational(7, 5)
    assert [coefficient*k for coefficient in (3, 4, 3)] == [s.Rational(21, 5), s.Rational(28, 5), s.Rational(21, 5)]
    change = s.Matrix([[1, 2], [0, 1]])
    h_new, p_new = change.T*h0*change, change.T*period
    assert (p_new.T*h_new.inv()*p_new)[0] == k


def test_full_matrix_local_cusp_tension_and_wrong_profile():
    r, k = s.symbols('r k', positive=True)
    assert v.local_cusp_tension(r, k) == s.zeros(4)
    wrong = v.local_cusp_tension(r, k, slope=1)
    assert wrong.subs({r: 0, k: 2}) != s.zeros(4)


def test_local_flag_sources_and_exact_scalar_inequality_equality():
    r, k = s.symbols('r k', positive=True)
    b = -r+s.log(2/k)/2
    flag = [3*b, 4*b, 3*b]
    sources = [6, 8, 6]
    for height, source in zip(flag, sources):
        assert s.simplify(s.diff(height, r, 2)-2*s.diff(height, r)-source) == 0
    total = sum(flag)
    lhs = s.diff(total, r, 2)-2*s.diff(total, r)
    rhs = 10*k*s.exp(2*r+total/5)
    assert s.simplify(lhs-rhs) == 0
    assert lhs == 20
    assert s.diff(total, r) == -10


def test_local_inner_boundary_is_essential_for_positive_bulk():
    r, radius, area = s.symbols('r R A', positive=True)
    bulk = s.integrate(20*area*s.exp(-2*r), (r, 0, radius))
    inner, outer = 10*area, -10*area*s.exp(-2*radius)
    assert s.simplify(bulk-inner-outer) == 0
    assert s.simplify(bulk-outer) == 10*area


def test_zero_period_has_local_diagonal_infinite_growth():
    r = s.symbols('r', real=True)
    t = s.exp(2*r)*s.Matrix([3, 1, -1, -3])
    assert t.diff(r, 2)-2*t.diff(r) == s.zeros(4, 1)
    assert sum(t) == 0
    # N constant means every theta_ij=0. The solution is local on the cusp,
    # not a source-free global extension over the compact core.


def test_root_covector_norm_and_central_independence():
    velocities = s.Matrix(s.symbols('v1:5', real=True))
    for i in range(3):
        root = s.zeros(4, 1)
        root[i], root[i+1] = 1, -1
        assert (root.T*root)[0] == 2
        assert (root.T*s.ones(4, 1))[0] == 0
        delta = (root.T*velocities)[0]
        remainder = 2*(velocities.T*velocities)[0]-delta**2
        expected = (velocities[i]+velocities[i+1])**2+2*sum(velocities[j]**2 for j in range(4) if j not in (i, i+1))
        assert s.expand(remainder-expected) == 0
