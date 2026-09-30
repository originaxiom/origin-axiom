"""R63 full local cone symbol and separated graph tests, not a particle census."""
from functools import lru_cache
import importlib.util
from pathlib import Path
import json
import sympy as s


def local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cd = local('r63_metric_forms', 'charged_domain.py')
r62 = local('r63_link_data', 'cone_interaction.py')
LINK = ((), (1,), (2,), (1, 2))
ORDER = LINK + tuple((0,)+b for b in LINK)
DEGREES = [len(b) for b in ORDER]
P = s.diag(0, 1, 1, 2)
M = P-s.eye(4)
GAMMA = s.BlockMatrix([[s.zeros(4), -s.eye(4)], [s.eye(4), s.zeros(4)]]).as_explicit()


def clean(x):
    if isinstance(x, s.MatrixBase):
        return x.applyfunc(lambda y: s.simplify(s.expand_complex(y)))
    return s.simplify(s.expand_complex(x))


def zero(x):
    return clean(x) == (s.zeros(*x.shape) if isinstance(x, s.MatrixBase) else 0)


def norm(x):
    return clean(s.trace(x.H*x))


def wedge_matrix(z):
    return s.Matrix([[0, 0, 0, 0], [z[0], 0, 0, 0],
                     [z[1], 0, 0, 0], [0, -z[1], z[0], 0]])


def operators(z, sigma):
    e = wedge_matrix(z)
    a = e.H
    L = e+a
    d = s.BlockMatrix([[e, s.zeros(4)], [sigma*s.eye(4)+M, -e]]).as_explicit()
    adj = s.BlockMatrix([[a, -sigma*s.eye(4)+M], [s.zeros(4), -a]]).as_explicit()
    A = s.BlockMatrix([[M, -L], [-L, -M]]).as_explicit()
    return d, adj, A


@lru_cache(maxsize=1)
def metric_controls():
    r, x, y = cd.COORDS
    sigma, k1, k2, p1, p2, q1, q2 = s.symbols('sigma k1 k2 p1 p2 q1 q2', real=True)
    phase = r**sigma*s.exp(s.I*(k1*x+k2*y))
    C = {(1,): p1+s.I*q1, (2,): p2+s.I*q2}
    Cbar = {b: s.conjugate(v) for b, v in C.items()}
    metric = cd.MetricForms((1, r, r))
    weights = [r**(len(b)-1) for b in LINK]*2
    direct_d, direct_adj, wrong = s.zeros(8), s.zeros(8), s.zeros(8)
    for j, basis in enumerate(ORDER):
        form = {basis: phase*weights[j]}
        outputs = (metric.dq(form, C), metric.deltaq(form, Cbar), metric.deltaq(form, C))
        for matrix, output in zip((direct_d, direct_adj, wrong), outputs):
            for i, target in enumerate(ORDER):
                matrix[i, j] = cd.simplify(output.get(target, 0)*r/(phase*weights[i]))
    z = s.Matrix([p1+s.I*(q1+k1), p2+s.I*(q2+k2)])
    d, adj, A = operators(z, sigma)
    checks = dict(operator_from_metric=zero(direct_d+direct_adj-GAMMA*(sigma*s.eye(8)+A)),
                  differential_from_metric=zero(direct_d-d), adjoint_from_metric=zero(direct_adj-adj),
                  wrong_complex_adjoint_rejected=not zero(wrong-direct_adj),
                  shifted_d_nilpotent=zero(d.subs(sigma, sigma-1)*d),
                  shifted_adjoint_nilpotent=zero(adj.subs(sigma, sigma-1)*adj),
                  hodge_involution=all(metric.star(metric.star({b: 1})) == {b: 1} for b in ORDER),
                  normalized_measure=all(s.simplify(metric.volume*weights[j]**2/metric.basis_length(b)**2)==1
                                         for j, b in enumerate(ORDER)))
    return dict(checks=checks, d=direct_d, adjoint=direct_adj)


@lru_cache(maxsize=1)
def spectrum_controls():
    p1, p2, q1, q2, t = s.symbols('p1 p2 q1 q2 t', real=True)
    z = s.Matrix([p1+s.I*q1, p2+s.I*q2])
    lam = clean((z.H*z)[0])
    _, _, A = operators(z, 0)
    L = wedge_matrix(z)+wedge_matrix(z).H
    poly = s.factor(A.charpoly(t).as_expr())
    expected = s.expand(((t**2-lam)**2-t**2)**2)
    _, _, neutral = operators(s.zeros(2, 1), 0)
    wrong = s.BlockMatrix([[P, -L], [-L, -P]]).as_explicit()
    zc = s.Matrix([1+s.I, 2-s.I])
    length = s.sqrt(7)
    U = s.Matrix.hstack(zc, s.Matrix([-s.conjugate(zc[1]), s.conjugate(zc[0])]))/length
    exterior_U = s.diag(1, 1, 1, U.det())
    exterior_U[1:3, 1:3] = U
    Rc = s.diag(exterior_U, exterior_U)
    _, _, Ac = operators(zc, 0)
    _, _, An = operators(s.Matrix([length, 0]), 0)
    checks = dict(link_square=zero(L*L-lam*s.eye(4)), angular_hermitian=zero(A-A.H),
                  gamma_skew_unitary=zero(GAMMA.H+GAMMA) and zero(GAMMA*GAMMA+s.eye(8)),
                  green_anticommutation=zero(GAMMA*A+A*GAMMA),
                  characteristic_polynomial=s.expand(poly-expected)==0,
                  wrong_density_shift_rejected=s.expand(wrong.charpoly(t).as_expr()-expected)!=0,
                  neutral_spectrum=neutral.eigenvals()=={-1: 2, 0: 4, 1: 2},
                  complex_unitary_reduction=zero(Rc.H*Rc-s.eye(8)) and zero(Rc.H*Ac*Rc-An))
    return dict(checks=checks, polynomial=poly, lambda_value=lam)


def eigenvalues(lam):
    lam = s.sympify(lam)
    if not lam.is_number or not lam.is_real or lam.has(s.Float) or lam < 0:
        raise ValueError('nonnegative exact scalar required')
    nu = s.sqrt(lam+s.Rational(1, 4))
    return [sign*nu+shift for sign in (-1, 1) for shift in (-s.Rational(1, 2), s.Rational(1, 2)) for _ in range(2)]


@lru_cache(maxsize=1)
def threshold_controls():
    eps, r = s.symbols('epsilon r', positive=True)
    values = (s.Integer(0), s.Rational(5, 16), s.Rational(3, 4), s.Integer(2))
    counts = [sum(bool(-s.Rational(1, 2)<x<s.Rational(1, 2)) for x in eigenvalues(lam)) for lam in values]
    cap = lambda p: 1/s.integrate(r**(-2*p), (r, eps, 1))
    n, ell, c = s.symbols('n ell c', positive=True)
    checks = dict(critical_counts=counts==[4, 4, 0, 0],
                  endpoint_slow_log=zero(s.integrate(1/r, (r, eps, 1))+s.log(eps)),
                  endpoint_fast_capacity_zero=s.limit(cap(s.Rational(1, 2)), eps, 0, dir='+')==0,
                  critical_fast_cutoff_cost=s.limit(cap(s.Rational(1, 4)), eps, 0, dir='+')==s.Rational(1, 2),
                  scale_changes_window=sum(bool(-s.Rational(1, 2)<x<s.Rational(1, 2)) for x in eigenvalues(s.Rational(2, 4)))==4,
                  no_uniform_gap=s.limit(c*(ell/n)**2/ell**2, n, s.oo)==0)
    return dict(checks=checks, lambda_values=values, critical_counts=counts)


@lru_cache(maxsize=2)
def fourier_controls(kind):
    H, w = r62.link(kind)
    a, b = s.symbols('a b', real=True)
    m, n = s.symbols('m n', integer=True)
    C = w*(a+s.I*b)
    u = C.applyfunc(lambda x: s.re(s.expand_complex(x)))
    v = C.applyfunc(lambda x: s.im(s.expand_complex(x)))
    k = 2*s.pi*s.Matrix([m, n])
    pairing = lambda x: clean((x.T*H*x)[0])
    lam = clean(pairing(k+v)+pairing(u))
    c = clean((w.H*H*w)[0])
    integer_form = m*m+n*n if kind=='square' else m*m+n*n-m*n
    minimum = s.Integer(1) if kind=='square' else 2/s.sqrt(3)
    decomposition = m*m+n*n if kind=='square' else (m*m+n*n+(m-n)**2)/2
    checks = dict(helicity_equal_norm=zero(pairing(u)-pairing(v)),
                  completed_square=zero(lam-2*pairing(v+k/2)-pairing(k)/2),
                  zero_fourier=zero(lam.subs({m: 0, n: 0})-c*(a*a+b*b)),
                  gram_positive=bool(H.det()>0 and H[0, 0]>0),
                  integer_bound_decomposition=zero(integer_form-decomposition) and zero(pairing(s.Matrix([m, n]))-minimum*integer_form),
                  minimum_attained=zero(pairing(s.Matrix([1, 0]))-minimum),
                  bound_above_window=bool(2*s.pi**2*minimum>s.Rational(3, 4)),
                  holonomy_ratio_nonreal=not zero(s.im(s.expand_complex(w[0]/w[1]))),
                  charge_fourier_pairing=zero(lam-lam.xreplace({a: -a, b: -b, m: -m, n: -n})))
    return dict(checks=checks, lambda_value=lam, c=c, nonzero_fourier_lower_bound=2*s.pi**2*minimum)


@lru_cache(maxsize=1)
def koszul_controls():
    p1, p2, q1, q2 = s.symbols('p1 p2 q1 q2', real=True)
    z = s.Matrix([p1+s.I*q1, p2+s.I*q2])
    e = wedge_matrix(z)
    lam = clean((z.H*z)[0])
    return dict(checks=dict(contracting_homotopy=zero(e*e.H+e.H*e-lam*s.eye(4)),
                            differential_nilpotent=zero(e*e),
                            zero_coefficient_not_contractible=wedge_matrix(s.zeros(2, 1))==s.zeros(4) and s.zeros(4)!=s.eye(4)))


@lru_cache(maxsize=1)
def mode_controls():
    eta = s.Symbol('eta', positive=True)
    root = s.sqrt(eta*(eta+1))
    z = s.Matrix([root, 0])
    definitions = dict(fast1=(eta, {1: root, 4: eta}, (1,)),
                       fast2=(eta, {3: eta, 6: root}, (2,)),
                       slowEven=(-eta, {0: root, 5: -eta-1}, (0, 2)),
                       slowOdd=(-eta, {2: eta+1, 7: -root}, (1, 3)))
    vectors, rows, checks = {}, {}, {}
    for name, (power, components, degrees) in definitions.items():
        v = s.zeros(8, 1)
        for index, value in components.items():
            v[index] = value
        vectors[name] = v
        d, adj, A = operators(z, power)
        du, adju = clean(d*v), clean(adj*v)
        checks[name+'_Q_zero'] = zero(du+adju)
        checks[name+'_indicial_eigenvalue'] = zero(A*v+power*v)
        checks[name+'_total_degrees'] = tuple(sorted(set(DEGREES[i] for i in components)))==degrees
        if name.startswith('fast'):
            checks[name+'_separate_residuals'] = zero(du) and zero(adju)
        else:
            checks[name+'_separate_residuals'] = not zero(du) and zero(du+adju) and zero(norm(du)-eta*(eta+1)**2*(2*eta+1))
        rows[name] = dict(power=power, vector=v, d=du, adjoint=adju, d_norm_coefficient=norm(du))
    fast = s.Matrix.hstack(vectors['fast1'], vectors['fast2'])
    slow = s.Matrix.hstack(vectors['slowEven'], vectors['slowOdd'])
    pairing = clean(fast.H*GAMMA*slow)
    checks['fast_plane_current_zero'] = zero(fast.H*GAMMA*fast) and fast.rank()==2
    checks['fast_slow_pairing_nondegenerate'] = not zero(pairing.det())
    primitive = s.eye(8)[:, 0]
    checks['fast1_local_primitive'] = zero(operators(z, eta+1)[0]*primitive-vectors['fast1'])
    eps, r = s.symbols('epsilon r', positive=True)
    checks['slow_separate_norm_diverges'] = s.limit(s.integrate(r**(-s.Rational(5, 2)), (r, eps, 1)), eps, 0, dir='+')==s.oo
    checks['fast_coordinate_trace_vanishes'] = s.limit(r**eta, r, 0, dir='+')==0
    return dict(checks=checks, rows=rows, green_pairing=pairing)


@lru_cache(maxsize=1)
def radial_gauge_controls():
    r = s.Symbol('r', positive=True)
    n = s.Symbol('n', integer=True, positive=True)
    B = s.diag(s.I, -s.I)
    X = s.diag(1+s.I, -1-s.I)
    g = s.diag(s.exp(s.I*s.log(r)), s.exp(-s.I*s.log(r)))
    e = s.Matrix([[0, 1], [0, 0]])
    checks = dict(unitary=zero(g.H*g-s.eye(2)),
                  radial_removed=zero(g*(B/r)*g.H-g.diff(r)*g.H),
                  tangent_unchanged=zero(g*X*g.H-X),
                  root_norm_preserved=zero(norm(g*e*g.H)-norm(e)),
                  distinct_apex_subsequences=clean(g[0, 0].subs(r, s.exp(-2*s.pi*n)))==1 and clean(g[0, 0].subs(r, s.exp(-2*s.pi*n-s.pi)))==-1)
    return dict(checks=checks)


def serial(x):
    if isinstance(x, s.MatrixBase):
        return [[str(v) for v in row] for row in x.tolist()]
    if isinstance(x, s.Basic):
        return str(x)
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [serial(v) for v in x]
    return x


def run():
    groups = dict(metric=metric_controls(), spectrum=spectrum_controls(), thresholds=threshold_controls(),
                  square=fourier_controls('square'), hexagonal=fourier_controls('hexagonal'),
                  koszul=koszul_controls(), modes=mode_controls(), radial_gauge=radial_gauge_controls())
    checks = {name+'_'+key: bool(value) for name, group in groups.items() for key, value in group['checks'].items()}
    return serial(dict(scope='Local normal-background cone spectrum and separated graph test, not a physical particle census',
                       checks=checks, all_checks_pass=all(checks.values()), groups=groups))


if __name__ == '__main__':
    data = run()
    print(json.dumps(data, indent=2))
    raise SystemExit(0 if data['all_checks_pass'] else 1)
