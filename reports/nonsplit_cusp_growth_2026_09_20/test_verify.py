"""Exact algebra for the prewritten F03 inequalities and countercontrols."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('nonsplit_growth_controls', Path(__file__).with_name('verify.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_relator_and_horospherical_diagonal():
    assert v.word('aabaBaaBab') == s.eye(2)
    for m in v.flag_matrices():
        assert s.simplify(m.det()) == 1
        assert m[1, 0] == 0
        assert s.simplify(m[0, 0]*s.conjugate(m[0, 0])) == 1


@pytest.mark.parametrize('text,shift', [('AbAA', -1), ('babA', 1)])
def test_actual_peripheral_translation(text, shift):
    m = v.word(text)
    assert m == s.Matrix([[1, shift], [0, 1]])
    z = s.symbols('z')
    assert s.simplify(m[0, 0]**2*z+m[0, 0]*m[0, 1]-z) == shift


def test_target_dilation_does_not_preserve_busemann_height():
    y = s.symbols('y', positive=True)
    assert s.simplify(-s.log(4*y)+s.log(y)) == -s.log(4)
    assert -s.log(4) != 0


def test_marked_base_has_one_cusp():
    import snappy
    M = snappy.Manifold('m010')
    assert M.num_cusps() == 1
    assert M.is_orientable()


def test_laplacian_from_cusp_density():
    r, x, y = s.symbols('r x y', real=True)
    h = s.Matrix([[2, 1], [1, 3]])
    g = s.diag(1, s.exp(-2*r), s.exp(-2*r))
    g[1:3, 1:3] = s.exp(-2*r)*h
    density = s.sqrt(5)*s.exp(-2*r)
    assert s.simplify(g.det()-density**2) == 0
    f = s.Function('f')(r, x, y)
    coords = (r, x, y)
    gi = g.inv()
    lap = sum(s.diff(density*gi[i,j]*s.diff(f,coords[j]),coords[i]) for i in range(3) for j in range(3))/density
    transverse = sum(h.inv()[i,j]*s.diff(f,coords[i+1],coords[j+1]) for i in range(2) for j in range(2))
    assert s.simplify(lap-s.diff(f,r,2)+2*s.diff(f,r)-s.exp(2*r)*transverse) == 0


def test_radial_equation_from_variation():
    r, B, velocity, acceleration, K = s.symbols('r B velocity acceleration K', real=True)
    density = s.exp(-2*r)
    lagrangian = density*(velocity**2+K*s.exp(2*r+2*B))/2
    momentum = s.diff(lagrangian, velocity)
    EL = s.diff(momentum,r)+s.diff(momentum,B)*velocity+s.diff(momentum,velocity)*acceleration-s.diff(lagrangian,B)
    assert s.simplify(EL/density-(acceleration-2*velocity-K*s.exp(2*r+2*B))) == 0


def test_period_norm_is_positive_and_coordinate_invariant():
    h = s.Matrix([[2, 1], [1, 3]])
    p = s.Matrix([-1, 1])
    K = (p.T*h.inv()*p)[0]
    assert K == s.Rational(7, 5)
    S = s.Matrix([[1, 2], [0, 1]])
    h_new, p_new = S.T*h*S, S.T*p
    assert (p_new.T*h_new.inv()*p_new)[0] == K
    assert (s.zeros(2,1).T*h.inv()*s.zeros(2,1))[0] == 0


def test_periodic_fluctuation_energy_has_no_cross_term():
    x, y, a, b = s.symbols('x y a b', real=True)
    H = s.Matrix([[2, 1], [1, 3]]).inv()
    z = -x+y+a*s.sin(2*s.pi*x)+b*s.cos(2*s.pi*y)
    dz = s.Matrix([s.diff(z,x),s.diff(z,y)])
    energy = s.integrate(s.expand((dz.T*H*dz)[0]),(x,0,1),(y,0,1))
    expected = s.Rational(7,5)+2*s.pi**2*(a*a*H[0,0]+b*b*H[1,1])
    assert s.simplify(energy-expected) == 0


def test_flux_derivative_and_integrated_mean_bound():
    r, r0, A, Q0 = s.symbols('r r0 A Q0', positive=True)
    B0 = s.symbols('B0',real=True)
    B = s.Function('B')(r)
    flux = A*s.exp(-2*r)*s.diff(B,r)
    assert s.simplify(s.diff(flux,r)-A*s.exp(-2*r)*(s.diff(B,r,2)-2*s.diff(B,r))) == 0
    lower = B0+Q0*(s.exp(2*r)-s.exp(2*r0))/(2*A)
    assert s.simplify(s.diff(lower,r)-Q0*s.exp(2*r)/A) == 0
    assert s.simplify(lower.subs(r,r0)-B0) == 0
    assert s.limit(s.exp(-2*r)*lower,r,s.oo) == Q0/(2*A)


def test_physical_angular_covector_scaling():
    r, bx, by = s.symbols('r bx by',real=True)
    h = s.Matrix([[2,1],[1,3]])
    covector = s.Matrix([bx,by])
    physical = (covector.T*(s.exp(-2*r)*h).inv()*covector)[0]
    reference = (covector.T*h.inv()*covector)[0]
    assert s.simplify(physical-s.exp(2*r)*reference) == 0


def test_ode_multiplier_identity_and_wrong_coefficient():
    r, kappa, p = s.symbols('r kappa p', positive=True)
    u = s.Function('u')(r)
    first = s.diff(u,r)**2-2*kappa*s.exp(p*u)/p
    correct = 2*s.diff(u,r)*(s.diff(u,r,2)-kappa*s.exp(p*u))
    assert s.simplify(s.diff(first,r)-correct) == 0
    wrong = s.diff(u,r)**2-kappa*s.exp(p*u)/p
    assert s.simplify(s.diff(wrong,r)-correct) != 0


def test_finite_time_comparison_solution():
    t = s.symbols('t',real=True)
    kappa, p = s.symbols('kappa p',positive=True)
    u0 = s.symbols('u0',real=True)
    u = v.comparison_solution(t,kappa,p,u0)
    assert s.simplify(s.diff(u,t,2)-kappa*s.exp(p*u)) == 0
    assert s.simplify(u.subs(t,0)-u0) == 0
    assert s.simplify(s.diff(u,t).subs(t,0)) == 0
    rate = s.sqrt(kappa*p/2)*s.exp(p*u0/2)
    T = s.pi*s.exp(-p*u0/2)/s.sqrt(2*kappa*p)
    assert s.simplify(rate*T) == s.pi/2


def test_time_bound_primitive():
    t = s.symbols('t',real=True)
    assert s.simplify(s.diff(s.asin(t),t)-1/s.sqrt(1-t*t)) == 0
    assert s.asin(1)-s.asin(0) == s.pi/2


def test_positive_local_cusp_has_opposite_outward_flux():
    r, K, A = s.symbols('r K A',positive=True)
    B = -r+s.log(2/K)/2
    assert v.radial_residual(B,r,K) == 0
    flux = A*s.exp(-2*r)*s.diff(B,r)
    assert s.simplify(flux+A*s.exp(-2*r)) == 0
    assert s.simplify(s.diff(flux,r)-2*A*s.exp(-2*r)) == 0


def test_wrong_cusp_profile_fails():
    r, K = s.symbols('r K',positive=True)
    wrong = r+s.log(2/K)/2
    assert s.simplify(v.radial_residual(wrong,r,K).subs(r,0)) == -4


def test_zero_period_local_radial_growth_control():
    r, c = s.symbols('r c',positive=True)
    B = c*s.exp(2*r)
    assert v.radial_residual(B,r,0) == 0
    assert s.limit(B,r,s.oo) == s.oo


def test_smooth_weighted_slice_countercontrol():
    x = s.symbols('x',real=True)
    w, b, z = v.slice_control(x)
    assert s.simplify(z.subs(x,x+1)-z) == 1
    assert s.simplify(s.diff(z,x)-w) == 0
    energy = s.simplify(s.exp(2*b)*s.diff(z,x)**2)
    assert s.simplify(energy-w) == 0
    assert s.integrate(energy,(x,0,1)) == 1
    factorization = s.Rational(9,10)*((1+s.cos(2*s.pi*x)/3)**2+(s.sin(2*s.pi*x)/3)**2)
    assert s.trigsimp(factorization-w) == 0
    # The zero logarithmic mean of the nonvanishing analytic factor is
    # proved by its convergent Fourier series in PROOF, not this assertion.
    assert s.Rational(10,9) > 1


def test_generic_dimension_dependent_linearization():
    r, K, d, eps = s.symbols('r K d eps', positive=True)
    delta = s.Function('delta')(r)
    local = -r+s.log((d-1)/K)/2
    residual = v.radial_residual(local+eps*delta,r,K,d)
    linear = s.simplify(s.diff(residual,eps).subs(eps,0))
    assert s.simplify(linear-(s.diff(delta,r,2)-(d-1)*s.diff(delta,r)-2*(d-1)*delta)) == 0
    lam = s.symbols('lam')
    polynomial = lam*lam-(d-1)*lam-2*(d-1)
    assert set(s.solve(polynomial.subs(d,3),lam)) == {1+s.sqrt(5),1-s.sqrt(5)}
    assert set(s.solve(polynomial.subs(d,2),lam)) == {2,-1}
