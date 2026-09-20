"""Frozen F08 predictions and controls, including global-map and cusp distinctions."""
import importlib.util
from pathlib import Path
from itertools import combinations
import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('f08', Path(__file__).with_name('verify.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_unitary_basis_and_actual_real_lorentz_connection():
    u, j = m.basis(), m.lorentz_j()
    assert m.clean(u.H*u-s.eye(4)) == s.zeros(4)
    assert j.H*j == s.eye(4) and j.det() == -1
    assert all(m.clean(c-c.conjugate()) == s.zeros(4) for c in m.connection())
    assert all(m.clean(c.T*j+j*c) == s.zeros(4) for c in m.connection())
    assert all(s.trace(c) == 0 for c in m.connection())


def test_full_flatness_and_moment_not_only_a_central_projection():
    assert all(r == s.zeros(4) for r in m.flat_residual(m.connection()))
    assert m.moment(m.connection()) == s.zeros(4)
    a, psi = m.split()
    assert any(r != s.zeros(4) for r in m.flat_residual(a))
    assert m.clean(psi[0]*psi[1]-psi[1]*psi[0]) != s.zeros(4)


def test_higgs_scale_is_not_a_free_flat_BPS_parameter():
    t = s.symbols('t', real=True)
    a, psi = m.split()
    residuals = m.flat_residual(m.scaled_connection(t))
    for (i, j), residual in zip(combinations(range(3), 2), residuals):
        assert m.clean(residual-(t*t-1)*(psi[i]*psi[j]-psi[j]*psi[i])) == s.zeros(4)
    assert residuals[0].subs(t, 0) != s.zeros(4)
    assert m.moment(m.scaled_connection(t)) == s.zeros(4)


def test_hermitian_triple_and_finite_volume_background_norm():
    a, psi = m.split()
    assert all(m.clean(m.z*p-b) == s.zeros(4) for p, b in zip(psi, m.boosts()))
    assert sum(s.trace(b*b) for b in m.boosts()) == 6
    z0 = s.symbols('z0', positive=True)
    assert s.integrate(6/m.z**3, (m.z, z0, s.oo)) == 3/z0**2


def test_actual_compact_connection_is_the_coframe_Levi_Civita_connection():
    a, _ = m.split()
    for old, omega in zip(a, m.coframe_connection()):
        assert m.clean(old-s.diag(s.zeros(1), omega)) == s.zeros(4)
    assert all(r == s.zeros(4) for r in m.parallel_residual())


def test_no_extra_gauge_generators_in_four_six_or_fifteen():
    boosts = m.boosts()
    assert s.Matrix.vstack(*boosts).rank() == 4
    exterior = [m.f05.exterior_lie(b) for b in boosts]
    assert s.Matrix.vstack(*exterior).rank() == 6
    eq = m.commutant_equations()
    assert eq.rank() == 15
    identity = s.Matrix(list(s.eye(4)))
    assert eq*identity == s.zeros(eq.rows, 1)
    trace_row = s.Matrix([[int(i//4 == i%4) for i in range(16)]])
    assert eq.col_join(trace_row).rank() == 16


@pytest.mark.parametrize('degree', [0, 3])
def test_scalar_and_top_algebraic_terms_are_strictly_positive(degree):
    assert m.bochner(degree) == s.diag(3, 1, 1, 1)


@pytest.mark.parametrize('degree', [1, 2])
def test_middle_algebraic_terms_have_the_declared_kernel_not_the_Sym3_gap(degree):
    h = m.bochner(degree)
    lam = s.symbols('lam')
    assert h == h.H
    assert s.factor(h.charpoly(lam).as_expr()-lam**5*(lam-2)**3*(lam-3)**4) == 0
    assert len(h.nullspace()) == 5


def test_F06_kernel_join_is_an_explicit_operator_identity():
    assert m.bochner(1) == 4*m.f06.center_h(1)
    assert m.bochner(0) == 4*m.f06.center_h(0)


def test_full_complex_component_norm_and_tensor_kernel():
    rr, ii = s.symbols('r0:12', real=True), s.symbols('i0:12', real=True)
    values = [r+s.I*i for r, i in zip(rr, ii)]
    t, b = values[:3], s.Matrix(3, 3, values[3:])
    u = s.Matrix([value for i in range(3) for value in [t[i], *list(b.row(i))]])
    expected = abs(s.trace(b))**2+3*sum(abs(v)**2 for v in t)
    expected += sum(abs(b[i, j]-b[j, i])**2 for i, j in combinations(range(3), 2))
    assert s.simplify(s.expand_complex((u.H*m.bochner(1)*u)[0]-expected)) == 0
    aa, bb, cc, dd, ee = s.symbols('aa bb cc dd ee')
    b0 = s.Matrix([[aa, cc, dd], [cc, bb, ee], [dd, ee, -aa-bb]])
    u0 = s.Matrix([value for i in range(3) for value in [0, *list(b0.row(i))]])
    assert m.t_matrix(1)*u0 == s.zeros(12, 1)
    assert m.t_matrix(0).H*u0 == s.zeros(4, 1)


def test_exact_global_representation_relator_and_changed_holonomy():
    a0, b0 = m.f05.geometric_matrices()
    a, b = m.balanced_group(a0), m.balanced_group(b0)
    assert m.f05.word('aaabABBAb', (a, b)) == s.eye(4)
    assert m.clean(m.balanced_group(a0*b0)-a*b) == s.zeros(4)
    assert m.balanced_group(-a0) == a
    assert s.simplify(a.det()-1) == 0 and s.simplify(b.det()-1) == 0
    assert s.simplify(s.trace(b)-4) == 0
    assert s.simplify(s.trace(b)-s.trace(m.f05.symmetric_cube(b0))) != 0


def test_global_linear_dual_map_is_not_the_positive_kinetic_metric():
    j = m.lorentz_j()
    for g in map(m.balanced_group, m.f05.geometric_matrices()):
        assert m.clean(g.T*j*g-j) == s.zeros(4)
        assert m.clean(j*g-g.inv().T*j) == s.zeros(4)
        assert g != s.eye(4)
    assert not j.is_positive_definite
    assert s.eye(4).is_positive_definite


def test_fourth_root_twist_breaks_linear_self_duality_but_not_antiunitary_pairing():
    a0, b0 = m.f05.geometric_matrices()
    a, b, j = m.balanced_group(a0), s.I*m.balanced_group(b0), m.lorentz_j()
    assert m.f05.word('aaabABBAb', (a, b)) == s.eye(4)
    assert s.simplify(b.det()-1) == 0
    assert s.simplify(s.trace(b)-s.trace(b.inv().T)) == 8*s.I
    assert m.clean(j*b-b.inv().T*j) != s.zeros(4)
    for g in (a, b):
        assert m.clean(j*g.conjugate()-g.inv().T*j) == s.zeros(4)
    assert j.H*j == s.eye(4) and j*j.conjugate() == s.eye(4)


def test_particular_pairing_has_an_explicit_SL4_countercontrol():
    j = m.lorentz_j()
    u = s.diag(3, -1, -1, -1)
    assert s.trace(u) == 0
    assert u.T*j+j*u != s.zeros(4)
    # A nonunitary scalar twist also defeats the antiunitary transport rule.
    _, g0 = m.f05.geometric_matrices()
    g = 2*m.balanced_group(g0)
    assert m.clean(j*g.conjugate()-g.inv().T*j) != s.zeros(4)
    assert g.det() == 16  # Outside the specified SL4 central twist as well.


def test_cusp_equations_force_the_full_zero_Fourier_form():
    f, g, h, p, q = [s.Function(name)(m.z) for name in ('f', 'g', 'h', 'p', 'q')]
    b = s.Matrix([[f, h, p], [h, g, q], [p, q, -f-g]])
    residual = m.cusp_codazzi(b)
    assert s.simplify(residual[0]+q) == 0
    assert s.simplify(residual[1]-p) == 0
    reduced = [s.simplify(value.subs({p: 0, q: 0})) for value in residual]
    conditions = {s.diff(f, m.z): (2*f+g)/m.z,
                  s.diff(g, m.z): (f+2*g)/m.z,
                  s.diff(h, m.z): h/m.z}
    assert all(s.simplify(value.subs(conditions)) == 0 for value in reduced)
    # Recover, not only satisfy, all three independent ODEs.
    assert s.simplify(reduced[3]-(2*f+g-m.z*s.diff(f, m.z))) == 0
    assert s.simplify(reduced[4]-(h-m.z*s.diff(h, m.z))) == 0
    assert s.simplify(reduced[7]-(f+2*g-m.z*s.diff(g, m.z))) == 0


def test_zero_Fourier_Codazzi_solutions_and_their_actual_norm():
    c, d, e = s.symbols('c d e', real=True)
    b = m.cusp_solution(c, d, e)
    assert s.trace(b) == 0 and b == b.T
    assert all(value == 0 for value in m.cusp_codazzi(b))
    density = s.simplify(s.trace(b.H*b)/m.z**3)
    expected = s.Rational(3, 2)*c*c*m.z**3+(d*d/2+2*e*e)/m.z
    assert s.simplify(density-expected) == 0
    z0, z1 = s.symbols('z0 z1', positive=True)
    for values in ({c: 1, d: 0, e: 0}, {c: 0, d: 1, e: 0}, {c: 0, d: 0, e: 1}):
        integral = s.integrate(density.subs(values), (m.z, z0, z1))
        assert s.limit(integral, z1, s.oo) == s.oo


def test_pointwise_tensor_kernel_does_not_impose_Codazzi():
    b = s.diag(1, -1, 0)
    u = s.Matrix([value for i in range(3) for value in [0, *list(b.row(i))]])
    assert m.bochner(1)*u == s.zeros(12, 1)
    assert any(value != 0 for value in m.cusp_codazzi(b))
