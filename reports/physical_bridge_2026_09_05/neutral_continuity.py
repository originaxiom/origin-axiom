"""R52 finite controls only: no global PDE or parameter derivative solver."""
from functools import lru_cache
from pathlib import Path
import importlib.util
import json
import sympy as s


def zero(value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(s.simplify(x) == 0 for x in entries)


@lru_cache(None)
def barrier_controls():
    r, k = s.symbols('r k', real=True, nonzero=True)
    a = s.Rational(3, 4)
    g = s.Matrix([[5*a/4, 0, a*k], [0, a*s.exp(-2*r)/2, 0], [a*k, 0, 4*a*k*k]])
    gi, rho = g.inv(), s.exp(-r)
    lap = lambda f: s.simplify(s.diff(rho*gi[0, 0]*s.diff(f, r), r)/rho)
    K, h, C = s.symbols('K h C', positive=True)
    w = C+a*K*h*r
    f = C+a*K*h*r/2
    return {
        'geometric_laplacian_height_negative': zero(lap(r)+1/a),
        'volume_weight': zero(g.det()-2*a**3*k*k*rho**2),
        'linear_supersolution': zero(lap(w)+K*h),
        'positive_comparison_example': zero(lap(f-w)-K*h/2),
        'wrong_sign_rejected': not zero(lap(C-a*K*h*r)+K*h),
        'half_slope_fails_worst_source': s.simplify(-K*h-lap(C+a*K*h*r/2)).is_negative is True,
    }


def weighted_moment(degree, rate, p):
    """Integral r^degree exp(p*rate*r) exp(-r) from 0 to infinity."""
    if not isinstance(degree, int) or degree < 0:
        raise ValueError('nonnegative integer degree required')
    margin = 1-s.sympify(p)*s.sympify(rate)
    if margin.is_positive:
        return s.factorial(degree)/margin**(degree+1)
    if margin.is_nonpositive:
        return s.oo
    raise ValueError('undecided integrability margin')


@lru_cache(None)
def envelope_controls():
    r = s.symbols('r', nonnegative=True)
    cases = [(0, s.Rational(1, 8), 4), (2, s.Rational(1, 12), 4),
             (4, s.Rational(1, 3), 2)]
    direct = [zero(s.integrate(r**d*s.exp(-(1-p*v)*r), (r, 0, s.oo))-weighted_moment(d, v, p))
              for d, v, p in cases]
    return {
        'independent_improper_integrals': all(direct),
        'strict_L4_margin_finite': weighted_moment(8, s.Rational(1, 8), 4).is_finite is True,
        'endpoint_diverges': weighted_moment(0, s.Rational(1, 4), 4) == s.oo,
        'endpoint_polynomial_diverges': weighted_moment(8, s.Rational(1, 4), 4) == s.oo,
        'L2_does_not_imply_L4': weighted_moment(0, s.Rational(1, 3), 2) == 3 and
            weighted_moment(0, s.Rational(1, 3), 4) == s.oo,
        'linear_growth_is_integrable': weighted_moment(4, 0, 4) == 24,
    }


def sylvester(S, rhs):
    n = S.rows
    op = s.kronecker_product(S, s.eye(n))+s.kronecker_product(s.eye(n), S.T)
    return (op.inv()*rhs.reshape(n*n, 1)).reshape(n, n)


@lru_cache(None)
def matrix_controls():
    t = s.symbols('t', real=True)
    S, X, Y = s.Matrix([[2, 1], [1, 1]]), s.Matrix([[1, 2], [2, -1]]), s.Matrix([[0, 3], [3, 2]])
    curve = S+t*X+t*t*Y/2
    K = curve*curve
    kp, kpp = K.diff(t).subs(t, 0), K.diff(t, 2).subs(t, 0)
    xp = sylvester(S, kp)
    ypp = sylvester(S, kpp-2*xp*xp)
    Q = s.Matrix([[1, 2], [0, 1]])
    H0 = Q.T*Q
    B = Q.inv()*S*Q
    Hq = B.T*H0*B
    H = Q.T*s.diag(s.exp(t), s.exp(-t))*Q
    bad = s.eye(2)+t*X  # positive on a small interval, not harmonic
    return {
        'noncommuting_example': not zero(S*X-X*S),
        'first_sylvester_derivative': xp == X,
        'second_sylvester_derivative': ypp == Y,
        'commuting_shortcut_rejected': not zero(S*(S.inv()*kp/2)+(S.inv()*kp/2)*S-kp),
        'missing_quadratic_term_rejected': sylvester(S, kpp) != Y,
        'positive_isometry': H0.det() == Hq.det() == B.det() == 1 and Hq[0, 0] > 0 and S[0, 0] > 0,
        'self_adjoint_and_squared': zero(B.T*H0-H0*B) and zero(B*B-H0.inv()*Hq),
        'not_Euclidean_square_root': not zero(B*B-Hq),
        'matrix_harmonic_equation_geodesic': zero(H.diff(t, 2)-H.diff(t)*H.inv()*H.diff(t)),
        'positive_nonharmonic_control': not zero((bad.diff(t, 2)-bad.diff(t)*bad.inv()*bad.diff(t)).subs(t, 0)),
    }


@lru_cache(None)
def transport_controls():
    x, y = s.symbols('x y', real=True)
    U = s.Matrix([[1, y], [0, 1]])
    B = U.T*s.diag(s.exp(x), s.exp(-x))*U
    bi, D = B.inv(), s.diag(1, -1)
    def curvature(sign):
        cx = B*D*bi+sign*B.diff(x)*bi
        cy = 2*B*D*bi+sign*B.diff(y)*bi
        return cy.diff(x)-cx.diff(y)+cx*cy-cy*cx
    return {
        'positive_det_one_transport': zero(B.det()-1) and B[0, 0].is_positive is True,
        'transported_connection_flat': zero(curvature(-1)),
        'wrong_transport_sign_rejected': not zero(curvature(1).subs({x:0, y:1})),
    }


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(None)
def parent_character_data():
    affine = load('r52_affine_input', 'affine_background.py')
    parent = load('r52_parent_input', 'parent_cusp.py')
    q = s.symbols('q', positive=True)
    word = 'nMNmmNMn'
    lam = affine.word(word, affine.generators(q))
    t4, dual = s.trace(lam), s.trace(lam.inv())
    t6 = s.trace(parent.group_action('6', lam))
    total = s.factor(45+(t4*dual-1)+10*t6+16*(t4+dual))
    weights = parent.direct_root_weights()
    root_trace = sum(mult*q**weight for weight, mult in weights.items())
    expected = 54+48*(q+1/q)+30*(q*q+q**-2)+16*(q**3+q**-3)+3*(q**4+q**-4)
    bracket = 48+60*(q+1/q)+48*(q*q+1+q**-2)+12*(q**3+q+q**-1+q**-3)
    return q, lam, t4, dual, t6, total, weights, root_trace, expected, bracket, word


@lru_cache(None)
def parent_controls():
    q, lam, t4, dual, t6, total, weights, roots, expected, bracket, word = parent_character_data()
    return {
        'literal_longitude_determinant': zero(lam.det()-1),
        'literal_defining_trace': zero(t4-3*q-q**-3),
        'literal_dual_trace': zero(dual-3/q-q**3),
        'actual_exterior_trace': zero(t6-3*(q*q+q**-2)),
        'literal_parent_character': zero(total-expected),
        'independent_root_character': zero(total-roots) and sum(weights.values()) == 248,
        'reciprocal_symmetry': zero(total.subs(q, 1/q)-total),
        'strict_monotonicity_factor': zero(q*s.diff(total, q)-(q-1/q)*bracket) and
            all(c > 0 for c in s.Poly(s.expand(q**3*bracket), q).all_coeffs()),
        'omitting_dual_sector_rejected': not zero(total-16*dual-expected),
        'central_twist_trivial_on_longitude': sum(1 if c.islower() else -1 for c in word) == 0,
    }


def controls():
    return dict(barrier=barrier_controls(), envelope=envelope_controls(),
                matrix=matrix_controls(), transport=transport_controls(), parent=parent_controls())


if __name__ == '__main__':
    groups = {name:{k:bool(v) for k,v in group.items()} for name,group in controls().items()}
    values = [v for group in groups.values() for v in group.values()]
    print(json.dumps(dict(checks=groups, passed=sum(values), total=len(values),
        all_checks_pass=all(values), global_PDE_numerically_solved=False,
        global_analytic_proof_machine_verified=False, parameter_derivative_established=False,
        physical_chirality_derived=False), indent=2))
    raise SystemExit(0 if all(values) else 1)
