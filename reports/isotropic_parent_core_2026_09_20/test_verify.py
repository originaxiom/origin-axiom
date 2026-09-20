"""F06 controls include metric, boundary, whole-matrix and operator counterexamples."""
import importlib.util
from itertools import combinations
from pathlib import Path
import sympy as s

spec = importlib.util.spec_from_file_location('isotropic_parent_core', Path(__file__).with_name('verify.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_parent_charge_and_full_isotropic_current():
    ns = m.nilpotents()
    assert all(m.U*n-n*m.U == 4*n for n in ns)
    assert all(p*q-q*p == s.zeros(4) for p, q in combinations(ns, 2))
    assert sum((n*n.T-n.T*n for n in ns), s.zeros(4)) == m.U
    alpha = m.a/s.sqrt(m.v)*s.eye(3)
    assert alpha.H*alpha/m.v**2 == m.a**2/m.v**3*s.eye(3)


def test_flatness_is_full_matrix_and_holds_before_the_PDE():
    assert m.flatness(m.connection()) == (s.zeros(4),)*3
    assert all(s.trace(c) == 0 for c in m.connection())


def test_entire_moment_equation_not_just_its_central_projection():
    expected = (s.trace(m.ddv)+4*m.a**2)/(4*m.v**3)*m.U
    assert m.clean(m.moment(m.connection())-expected) == s.zeros(4)
    assert m.clean(m.moment(m.connection()).subs(m.ddv[2, 2], -4*m.a**2-m.ddv[0, 0]-m.ddv[1, 1])) == s.zeros(4)


def test_rank_two_central_retuning_keeps_a_nonzero_su3_residual():
    residual = m.moment(m.connection(count=2))
    residual = m.clean(residual.subs(m.ddv[2, 2], -8*m.a**2/3-m.ddv[0, 0]-m.ddv[1, 1]))
    expected = m.a**2/(3*m.v**3)*s.diag(0, -1, -1, 2)
    assert residual == expected and residual != s.zeros(4)
    assert s.trace(residual*m.U) == 0


def test_dual_solution_reverses_source_sign_without_changing_metric():
    c = m.connection()
    dual = tuple(-matrix.T for matrix in c)
    assert m.flatness(dual) == (s.zeros(4),)*3
    assert m.clean(m.moment(dual)+m.moment(c).T) == s.zeros(4)
    assert all(s.trace(((x+x.H)/2)**2) == s.trace(((y+y.H)/2)**2) for x, y in zip(c, dual))


def test_constant_v_requires_zero_amplitude_and_is_not_a_false_positive():
    constant = {**dict.fromkeys(m.dv, 0), **dict.fromkeys(m.ddv_symbols, 0)}
    residual = m.moment(m.connection()).subs(constant)
    assert residual == m.a**2/m.v**3*m.U
    assert residual.subs(m.a, 0) == s.zeros(4)


def test_christoffel_ricci_tensor_and_scalar_are_derived():
    gradient = s.Matrix(m.dv)
    expected = -m.ddv/m.v+2*gradient*gradient.T/m.v**2-s.trace(m.ddv)/m.v*s.eye(3)
    assert m.clean(m.ricci()-expected) == s.zeros(3)
    scalar = s.trace(m.ricci())/m.v**2
    assert m.clean(scalar+4*s.trace(m.ddv)/m.v**3-2*(gradient.T*gradient)[0]/m.v**4) == 0


def test_hyperbolic_metric_control_has_negative_curvature_but_fails_moment():
    z = s.symbols('z', positive=True)
    jets = {m.v: 1/z, m.dv[0]: 0, m.dv[1]: 0, m.dv[2]: -1/z**2,
            **dict.fromkeys(m.ddv_symbols, 0), m.ddv[2, 2]: 2/z**3}
    assert m.clean((s.trace(m.ricci())/m.v**2).subs(jets)) == -6
    assert m.clean(m.moment(m.connection()).subs(jets)) == (s.Rational(1, 2)+m.a**2*z**3)*m.U


def test_higgs_tensor_norm_and_curvature_sign_with_correct_trace():
    gradient = s.Matrix(m.dv)
    tensor = 3*gradient*gradient.T/(16*m.v**2)+m.a**2/(2*m.v)*s.eye(3)
    assert m.clean(m.higgs_tensor()-tensor) == s.zeros(3)
    pde = {m.ddv[2, 2]: -4*m.a**2-m.ddv[0, 0]-m.ddv[1, 1]}
    scalar = m.clean((s.trace(m.ricci())/m.v**2).subs(pde))
    norm = m.clean(s.trace(tensor)/m.v**2)
    assert m.clean(scalar-s.Rational(32, 3)*norm) == 0
    assert m.clean(scalar-16*m.a**2/m.v**3-2*(gradient.T*gradient)[0]/m.v**4) == 0


def test_full_einstein_comparison_has_a_hessian_obligation_not_just_trace():
    delta = s.trace(m.ddv)
    difference = m.ricci()-s.Rational(32, 3)*m.higgs_tensor()
    expected = -m.ddv/m.v-(delta+s.Rational(16, 3)*m.a**2)/m.v*s.eye(3)
    assert m.clean(difference-expected) == s.zeros(3)
    spherical = {m.ddv[i, j]: -s.Rational(4, 3)*m.a**2 if i == j else 0
                 for i in range(3) for j in range(i, 3)}
    assert m.clean(difference.subs(spherical)) == s.zeros(3)


def test_harmonic_quadratic_change_keeps_BPS_but_fails_einstein_tensor():
    e = s.symbols('epsilon', nonzero=True, real=True)
    jets = {m.ddv[0, 0]: -4*m.a**2/3+2*e, m.ddv[1, 1]: -4*m.a**2/3-2*e,
            m.ddv[2, 2]: -4*m.a**2/3, m.ddv[0, 1]: 0, m.ddv[0, 2]: 0, m.ddv[1, 2]: 0}
    assert m.clean(m.moment(m.connection()).subs(jets)) == s.zeros(4)
    defect = m.clean((m.ricci()-s.Rational(32, 3)*m.higgs_tensor()).subs(jets))
    assert defect == s.diag(-2*e/m.v, 2*e/m.v, 0) and defect != s.zeros(3)


def test_einstein_action_trace_really_implies_the_tensor_equation_in_3d():
    curvature, energy, k = s.symbols('curvature energy k')
    trace_equation = curvature-s.Rational(3, 2)*curvature-k*(energy-s.Rational(3, 2)*energy)
    assert s.solve(trace_equation, curvature) == [k*energy]


def test_explicit_ball_PDE_and_finite_boundary_distance():
    x, y, z = s.symbols('x y z', real=True)
    c, r, radius = s.symbols('c r radius', positive=True)
    vv = c-s.Rational(2, 3)*m.a**2*(x*x+y*y+z*z)
    assert sum(s.diff(vv, t, 2) for t in (x, y, z)) == -4*m.a**2
    radial = s.Rational(2, 3)*m.a**2*(radius**2-r**2)
    distance = s.integrate(radial, (r, 0, radius))
    assert distance == s.Rational(4, 9)*m.a**2*radius**3
    assert distance == s.Rational(2, 3)*(s.Rational(2, 3)*m.a**2*radius**2)*radius
    assert radial.subs(r, radius) == 0


def test_maximal_ball_Higgs_norm_diverges_logarithmically_not_finitely():
    r, radius = s.symbols('r radius', positive=True)
    vv = s.Rational(2, 3)*m.a**2*(radius**2-r**2)
    density = 4*s.pi*r**2*(m.a**4*r**2/(3*vv)+3*m.a**2/2)
    assert s.limit((radius-r)*density, r, radius, dir='-') == s.pi*m.a**2*radius**3
    assert s.limit(density, r, 0) == 0


def test_boundary_flux_is_retained_and_balances_volume_source():
    r, r0, c = s.symbols('r r0 c', positive=True)
    vv = c-s.Rational(2, 3)*m.a**2*r**2
    boundary = s.simplify(4*s.pi*r**2*s.diff(vv, r)/8)
    volume = s.integrate(-m.a**2/2*4*s.pi*r**2, (r, 0, r0))
    assert boundary.subs(r, r0) == volume == -2*s.pi*m.a**2*r0**3/3
    assert volume != 0


def test_center_algebraic_operator_has_exact_kernel_but_is_not_the_full_Laplacian():
    h = m.center_h(1)
    lam = s.symbols('lam')
    assert h == h.H
    assert s.factor(h.charpoly(lam).as_expr()-lam**5*(lam-s.Rational(1, 2))**6*(lam-s.Rational(3, 4))) == 0
    assert len(h.nullspace()) == 5
    b11, b22, b12, b13, b23 = s.symbols('b11 b22 b12 b13 b23')
    b = s.Matrix([[b11, b12, b13], [b12, b22, b23], [b13, b23, -b11-b22]])
    u = s.Matrix([value for i in range(3) for value in [0, *list(b.row(i))]])
    assert h*u == s.zeros(12, 1)
    assert m.center_h(0) == s.diag(s.Rational(3, 4), *([s.Rational(1, 4)]*3))


def test_nonparallel_higgs_blocks_the_homogeneous_gap_inference():
    derivatives = m.covariant_higgs_derivatives()
    center = [m.clean(matrix.subs(m.center_substitution())) for matrix in derivatives]
    assert any(matrix != s.zeros(4) for matrix in center)
    assert sum((center[3*i+i] for i in range(3)), s.zeros(4)) == s.zeros(4)
    ns = m.nilpotents()
    s0, s1 = (ns[0]+ns[0].T)/2, (ns[1]+ns[1].T)/2
    assert s0*s1-s1*s0 != s.zeros(4)
