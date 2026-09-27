"""R51 finite controls, NOT a nonlinear PDE solver or analytic proof verifier."""
from functools import lru_cache
from pathlib import Path
import importlib.util
import json
import sympy as s


def zero(value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(s.simplify(x) == 0 for x in entries)


@lru_cache(None)
def energy_controls():
    R, R0 = s.symbols('R R0', positive=True)
    dk, db = s.symbols('dk db', real=True)
    D, P = s.diag(1, -3, 1, 1), s.zeros(4)
    P[0, 3] = 1
    a = dk*D+db*P/R
    density = s.trace(a.T*a)*R**(-s.Rational(3, 2))
    tail = 24*dk**2/s.sqrt(R0)+s.Rational(2, 5)*db**2/R0**s.Rational(5, 2)
    return {
        'trace_norm': zero(s.trace(a.T*a)-12*dk**2-db**2/R**2),
        'improper_integral': zero(s.integrate(density, (R, R0, s.oo))-tail),
        'lower_limit_derivative': zero(s.diff(tail, R0)+density.subs(R, R0)),
        'old_hyperbolic_log_diverges': s.integrate(1/R, (R, R0, s.oo)) == s.oo,
        'quadratic_energy_majorant': zero(2*dk**2+2*db**2-(dk+db)**2-(dk-db)**2),
    }


def hardy_integrals(poly):
    r = s.symbols('r', real=True)
    f = sum(s.sympify(c)*r**j for j, c in enumerate(poly))
    moment = lambda expr: sum(c*s.factorial(power[0]) for power, c in s.Poly(s.expand(expr), r).terms())
    return moment(f**2), moment(s.diff(f, r)**2), f.subs(r, 0)**2


def hardy_controls():
    r = s.symbols('r', real=True)
    f = s.Function('f')(r)
    identity = s.diff(f**2*s.exp(-r), r)+f**2*s.exp(-r)-2*f*s.diff(f, r)*s.exp(-r)
    examples = [(1,), (0, 1), (1, -2, 3), (0, 0, 0, 1)]
    inequalities = [I <= 2*B+4*J for I, J, B in map(hardy_integrals, examples)]
    I, J, B = hardy_integrals((1,))
    return {
        'integration_by_parts_identity': zero(identity),
        'anchored_polynomial_controls': all(bool(x) for x in inequalities),
        'dropping_boundary_term_rejected': I > 4*J and B == 1,
        'unbounded_linear_function_is_L2': hardy_integrals((0, 1))[0] == 2,
    }


@lru_cache(None)
def model_controls():
    r, k = s.symbols('r k', real=True, nonzero=True)
    a = s.Rational(3, 4)
    g = s.Matrix([[5*a/4, 0, a*k], [0, a*s.exp(-2*r)/2, 0], [a*k, 0, 4*a*k*k]])
    gi = g.inv()
    weight = s.exp(-r)
    delta = lambda cov: s.simplify(-s.diff(weight*(gi*cov)[0], r)/weight)
    dt, dr = s.Matrix([0, 0, 1]), s.Matrix([1, 0, 0])
    sigma_prime = -1/(4*k)
    alpha = dt-sigma_prime*dr
    return {
        'volume_weight': zero(g.det()-2*a**3*k*k*s.exp(-2*r)),
        'radial_ray_bounded_length': g[0, 0] == 5*a/4,
        'dt_bounded_norm': zero(gi[2, 2]-5/(16*a*k*k)),
        'delta_dt': zero(delta(dt)+1/(4*a*k)),
        'laplacian_r': zero(delta(dr)-1/a),
        'corrected_tangent_coclosed': zero(delta(alpha)),
        'wrong_sign_rejected': not zero(delta(dt+sigma_prime*dr)),
        'dropping_radial_term_rejected': not zero(delta(dt)),
        'correction_is_dv': alpha == s.Matrix([1/(4*k), 0, 1]),
    }


def commutant_dimension(gens):
    n = gens[0].rows
    units = []
    for a in range(n):
        for b in range(n):
            E = s.zeros(n)
            E[a, b] = 1
            units.append(E)
    columns = [s.Matrix.vstack(*((E*g-g*E).reshape(n*n, 1) for g in gens)) for E in units]
    return n*n-s.Matrix.hstack(*columns).rank()


@lru_cache(None)
def algebra_controls():
    # Nondiagonal positive determinant-one metric; no Euclidean substitution.
    U = s.Matrix([[1, 2, 0, 1], [0, 1, 1, 0], [0, 0, 1, 3], [0, 0, 0, 1]])
    H = U.T*s.diag(2, 3, 5, s.Rational(1, 30))*U
    hi = H.inv()
    equalities = []
    for a in range(4):
        for b in range(4):
            E = s.zeros(4)
            E[a, b] = 1
            equalities.append(zero(s.trace(hi*E.T*H*E)-H[a, a]*hi[b, b]))
    T, N = s.diag(2, s.Rational(1, 2)), s.Matrix([[1, 1], [0, 1]])
    t = s.symbols('t', positive=True)
    escaping = s.diag(t, 1/t)
    norm_N = s.trace(escaping.inv()*N.T*escaping*N)
    norm_T = s.trace(escaping.inv()*T.T*escaping*T)
    return {
        'positive_metric_determinant_one': H.det() == 1 and all(H[:j, :j].det() > 0 for j in range(1, 5)),
        'matrix_unit_identity': all(equalities),
        'sum_identity': zero(sum(H[a, a]*hi[b, b] for a in range(4) for b in range(4))-s.trace(H)*s.trace(hi)),
        'triangular_scalar_commutant': commutant_dimension((T, N)) == 1,
        'triangular_not_full_algebra': s.Matrix.hstack(*(x.reshape(4, 1) for x in (s.eye(2), T, N, T*N))).rank() == 3,
        'bounded_generators_despite_escape': zero(norm_N-2-t*t) and norm_T == s.Rational(17, 4),
        'escaping_inverse_unbounded': s.limit(escaping[1, 1], t, 0, dir='+') == s.oo,
    }


@lru_cache(None)
def word_controls():
    path = Path(__file__).with_name('affine_background.py')
    spec = importlib.util.spec_from_file_location('r51_affine_input', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    words = ('', 'm', 'n', 'mm', 'nm', 'mn', 'nn', 'nmm', 'mnm', 'nnm', 'mmn', 'nmn', 'mnn', 'mnmm', 'nnmm', 'nnmn')
    out = {}
    for q in (s.Rational(2), s.Rational(1, 2), s.Rational(3), s.Rational(1, 3)):
        gens = module.generators(q)
        columns = [module.word(word, gens).reshape(16, 1) for word in words]
        out['full_word_span_at_'+str(q)] = s.Matrix.hstack(*columns).rank() == 16
    return out


def controls():
    return dict(energy=energy_controls(), hardy=hardy_controls(),
                model=model_controls(), algebra=algebra_controls(), words=word_controls())


if __name__ == '__main__':
    groups = {name: {k: bool(v) for k, v in group.items()} for name, group in controls().items()}
    values = [v for group in groups.values() for v in group.values()]
    print(json.dumps(dict(checks=groups, passed=sum(values), total=len(values),
                         all_checks_pass=all(values), global_PDE_numerically_solved=False,
                         global_analytic_proof_machine_verified=False,
                         strong_X_branch_proved=False, physical_chirality_derived=False), indent=2))
    raise SystemExit(0 if all(values) else 1)
