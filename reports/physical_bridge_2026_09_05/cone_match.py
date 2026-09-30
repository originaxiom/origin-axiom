"""R65 exact necessary peripheral tests, not a global harmonic solver."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent


def local(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


r42 = local('r65_projective_source', 'affine_background.py')
r62 = local('r65_cone_source', 'cone_interaction.py')
T = s.Symbol('t', nonzero=True)


def clean(a):
    return a.applyfunc(s.simplify) if isinstance(a, s.MatrixBase) else s.simplify(a)


def zero(a):
    return clean(a) == (s.zeros(*a.shape) if isinstance(a, s.MatrixBase) else 0)


def inputs():
    return (json.loads((HERE / 'CONE_MATCH_TOPOLOGY.json').read_text()),
            json.loads((HERE / 'CONE_MATCH_SEEDS.json').read_text())['seeds'])


def one(n=5):
    return tuple(range(n)), (0,)*n


def multiply(a, b):
    # Column-image construction, separate from dense matrix multiplication.
    p, v = a
    q, w = b
    outp, outv = [0]*len(p), [0]*len(p)
    for j in range(len(p)):
        mid, dest = q[j], p[q[j]]
        outp[j], outv[dest] = dest, v[dest]+w[mid]
    return tuple(outp), tuple(outv)


def inverse(a):
    p, v = a
    pi = [0]*len(p)
    for j, i in enumerate(p):
        pi[i] = j
    return tuple(pi), tuple(-v[p[j]] for j in range(len(p)))


def word(w, generators):
    result = one(len(generators[0][0]))
    for x in w:
        g = generators[abs(x)-1]
        result = multiply(result, g if x > 0 else inverse(g))
    return result


def matrix(a, t=T):
    p, v = a
    return s.Matrix(len(p), len(p), lambda i, j: t**v[i] if i == p[j] else 0)


def dense_word(w, matrices):
    result = s.eye(matrices[0].rows)
    for x in w:
        g = matrices[abs(x)-1]
        result = clean(result*(g if x > 0 else g.inv()))
    return result


def rewrite(w, degree, start=0):
    vertex, result = start, []
    for x in w:
        target = (vertex+(1 if x > 0 else -1)) % degree
        edge = vertex if x > 0 else target
        label = (1 if edge == degree-1 else 0) if abs(x) == 1 else edge+2
        if label:
            result.append(label if x > 0 else -label)
        vertex = target
    return tuple(result), vertex


def cover(degree):
    data, _ = inputs()
    relations = [rewrite(data['base_relator'], degree, k)[0] for k in range(degree)]
    return relations, (1,), rewrite(data['base_longitude'], degree)[0]


def inclusion():
    base_words = [(1,)*6]+[(1,)*k+(2,)+(-1,)*((k+1) % 6) for k in range(6)]
    return [rewrite(w, 2)[0] for w in base_words]


def order(a, cap=60):
    value = one(len(a[0]))
    for n in range(1, cap+1):
        value = multiply(value, a)
        if value == one(len(a[0])):
            return n
    return None  # A bounded miss is not an infinite-order proof.


@lru_cache(None)
def source_controls():
    data, seeds = inputs()
    rels, mu, ell = cover(2)
    checks = dict(relators=[list(w) for w in rels] == data['M2_relators'],
                  meridian=list(mu) == data['M2_meridian'],
                  longitude=list(ell) == data['M2_longitude'],
                  inclusion=[list(w) for w in inclusion()] == data['M6_generators_in_M2'],
                  seed_population=len(seeds) == 2,
                  words_close=all(rewrite(data['base_relator'], n, k)[1] == k
                                  for n in (2, 6) for k in range(n)),
                  base_relator_abelian_exponent=sum(1 if x > 0 else -1 for x in data['base_relator']) == 0,
                  base_longitude_abelian_exponent=sum(1 if x > 0 else -1 for x in data['base_longitude']) == 0)
    return dict(checks=checks)


@lru_cache(None)
def monomial_controls(number):
    _, seeds = inputs()
    seed = seeds[number]
    down = [(tuple(p), tuple(v)) for p, v in zip(seed['permutations'], seed['exponents'])]
    down_dense = [matrix(a) for a in down]
    up = [word(w, down) for w in inclusion()]
    up_dense = [dense_word(w, down_dense) for w in inclusion()]
    checks = dict(actual_pullback=all(matrix(a) == b for a, b in zip(up, up_dense)))
    rows = {}
    for degree, gens, mats in ((2, down, down_dense), (6, up, up_dense)):
        rels, mu, ell = cover(degree)
        words = rels+[mu, ell]
        prefix = 'M'+str(degree)+'_'
        values = [word(w, gens) for w in words]
        dense = [dense_word(w, mats) for w in words]
        mer, lon = values[-2:]
        mm, ll = dense[-2:]
        checks.update({prefix+'two_routes': all(matrix(a) == b for a, b in zip(values, dense)),
                       prefix+'relators': all(a == one() for a in values[:-2]),
                       prefix+'dense_relators': all(a == s.eye(5) for a in dense[:-2]),
                       prefix+'SL5': all(zero(a.det()-1) for a in mats),
                       prefix+'zero_period_exponents': mer[1] == lon[1] == (0,)*5,
                       prefix+'commuting_pair': zero(mm*ll-ll*mm),
                       prefix+'unitary_pair': zero(mm.H*mm-s.eye(5)) and zero(ll.H*ll-s.eye(5)),
                       prefix+'finite_orders': order(mer) is not None and order(lon) is not None})
        rows['M'+str(degree)] = dict(meridian=mer, longitude=lon,
                                    orders=[order(mer), order(lon)])
    mutated = [(p, v) for p, v in down]
    changed = list(mutated[0][1])
    changed[3], changed[4] = changed[3]+1, changed[4]-1
    mutated[0] = mutated[0][0], tuple(changed)
    bad_mu = matrix(word(cover(2)[1], mutated), 2)
    checks['changed_exponent_rejected'] = not zero(bad_mu.H*bad_mu-s.eye(5))
    checks['changed_exponent_keeps_determinant'] = zero(bad_mu.det()-1)
    return dict(checks=checks, peripheral=rows)


@lru_cache(None)
def period_controls(kind):
    _, w = r62.link(kind)
    u, v, phi1, phi2 = s.symbols('u v phi1 phi2', real=True)
    xi = u+s.I*v
    R = clean(s.Matrix([[s.re(z), -s.im(z)] for z in w]))
    constraints = clean(s.Matrix([s.re(s.expand_complex(z*xi)) for z in w]))
    aa, bb, cc, dd = s.symbols('aa bb cc dd', real=True)
    P = s.Matrix([[aa, bb], [cc, dd]])
    checks = dict(modulus_map=zero(constraints-R*s.Matrix([u, v])),
                  independent_periods=R.det() != 0,
                  unique_zero=R.inv()*s.zeros(2, 1) == s.zeros(2, 1),
                  marking_determinant=zero((P*R).det()-P.det()*R.det()),
                  finite_cover_determinant=zero((s.diag(3, 2)*R).det()-6*R.det()),
                  unitary_phases_do_not_change_moduli=all(
                      zero(s.exp(s.I*p+z*xi)*s.conjugate(s.exp(s.I*p+z*xi))
                           -s.exp(2*s.re(s.expand_complex(z*xi)))) for p, z in zip((phi1, phi2), w)),
                  one_period_shortcut_rejected=zero(s.exp(2*s.pi*s.I*w[1])-1)
                      and not zero(s.re(s.expand_complex(2*s.pi*s.I*w[0]))),
                  real_ratio_control_has_kernel=s.Matrix([[1, 0], [2, 0]]).rank() == 1)
    E = s.Matrix([[0, 1], [0, 0]])
    checks['nilpotent_is_not_normal'] = not zero(E*E.H-E.H*E)
    checks['nilpotent_unit_modulus_control'] = (s.eye(2)+w[0]*E).eigenvals() == {1: 2}
    return dict(checks=checks, real_modulus_matrix=R, determinant=clean(R.det()))


@lru_cache(None)
def projective_controls():
    q = s.Symbol('q', positive=True)
    n = s.Symbol('n', integer=True, positive=True)
    data, _ = inputs()
    m, a = r42.generators(q)
    lon = dense_word(data['base_longitude'], [m, a])
    K = m-s.eye(4)
    L = clean(K-K*K/2)
    powered = s.eye(4)+n*L+n*n*L*L/2
    negative = s.eye(4)-n*L+n*n*L*L/2
    checks = dict(group_relation=zero(dense_word(data['base_relator'], [m, a])-s.eye(4)),
                  commute=zero(m*lon-lon*m),
                  SL4=zero(m.det()-1) and zero(a.det()-1),
                  nilpotent_index_three=zero(K**3) and not zero(K**2),
                  logarithm_cube=zero(L**3) and not zero(L**2),
                  meridian_recovered=zero(m-s.eye(4)-L-L**2/2),
                  power_recurrence=zero(powered.subs(n, n+1)-powered*m),
                  power_inverse=zero(powered*negative-s.eye(4)),
                  power_Jordan_part=zero((powered-s.eye(4))**2-n*n*L*L)
                      and clean((n*n*L*L)[0, 3]) != 0,
                  dual_preserves_Jordan=zero((m.inv().T-s.eye(4))**3)
                      and not zero((m.inv().T-s.eye(4))**2),
                  central_twist_preserves_Jordan=zero((s.I*m-s.I*s.eye(4))**3)
                      and not zero((s.I*m-s.I*s.eye(4))**2))
    return dict(checks=checks, meridian=m, longitude=lon,
                nonzero_power_square_entry=clean((n*n*L*L)[0, 3]))


@lru_cache(None)
def transport_controls():
    r, R, delta, A, ell = s.symbols('r R delta A ell', positive=True)
    H = s.diag(1, -1)
    E = s.Matrix([[0, 1], [0, 0]])
    B = s.I*H
    U = s.diag(s.exp(-s.I*s.log(r/R)), s.exp(s.I*s.log(r/R)))
    power = s.diag(s.sqrt(r), 1/s.sqrt(r))
    logg = s.diag(ell**(-s.Rational(1, 4)), ell**s.Rational(1, 4))
    log_radial = clean(logg.diff(ell)*logg.inv()/r)
    log_tangent = clean(logg*E*logg.inv())
    checks = dict(unitary_leading_transport=zero(U.H*U-s.eye(2)),
                  leading_radial_equation=zero(U.diff(r)+(B/r)*U),
                  remainder_integrable=zero(s.integrate(A*r**(delta-1), (r, 0, R))-A*R**delta/delta),
                  power_erases_Jordan_limit=zero(power*(s.eye(2)+E)*power.inv()-s.eye(2)-r*E),
                  power_radial_not_antihermitian=not zero(-power.diff(r)*power.inv()+(-power.diff(r)*power.inv()).H),
                  power_condition_unbounded=s.limit(1/r, r, 0, dir='+') == s.oo,
                  logarithmic_Jordan=zero(log_tangent-E/s.sqrt(ell)),
                  logarithmic_radial=zero(log_radial+H/(4*r*ell)),
                  logarithmic_flatness=zero(-log_tangent.diff(ell)/r+log_radial*log_tangent-log_tangent*log_radial),
                  logarithmic_limit=all(s.limit(x, ell, s.oo) == 0 for x in log_tangent),
                  logarithmic_condition_unbounded=s.limit(s.sqrt(ell), ell, s.oo) == s.oo,
                  logarithmic_radial_not_integrable=s.limit(s.log(ell), ell, s.oo) == s.oo,
                  logarithmic_not_power_error=s.limit(s.exp(delta*ell)/ell, ell, s.oo) == s.oo,
                  R64_bounded_gauge_limit=(s.cosh(r)*s.eye(2)+s.sinh(r)*(E+E.T)).limit(r, 0) == s.eye(2))
    return dict(checks=checks, integrable_remainder_bound=A*R**delta/delta,
                logarithmic_radial=log_radial, logarithmic_tangent=log_tangent)


@lru_cache(None)
def abelian_controls(kind):
    H, w = r62.link(kind)
    data, _ = inputs()
    integers = (1, 0, -1, 0, 0)
    X = s.diag(*(2*s.pi*s.I*n for n in integers))
    mer = s.diag(*(s.exp(w[0]*X[j, j]) for j in range(5)))
    lon = clean(s.diag(*(s.exp(w[1]*X[j, j]) for j in range(5))))
    c = clean((w.H*H*w)[0])
    m, n = s.symbols('m n', integer=True)
    a, b = s.symbols('a b', real=True)
    C = w*(a+s.I*b)
    u, v = [clean(C.applyfunc(f)) for f in (s.re, s.im)]
    k = 2*s.pi*s.Matrix([m, n])
    pairing = lambda z: clean((z.T*H*z)[0])
    lam = pairing(u)+pairing(v+k)
    minimum = s.S.One if kind == 'square' else 2/s.sqrt(3)
    integer_form = m*m+n*n if kind == 'square' else m*m+n*n-m*n
    zero_root_min = 4*s.pi**2*c
    checks = dict(normal_nonzero=zero(X*X.H-X.H*X) and not zero(X),
                  trace_free=zero(s.trace(X)),
                  longitudinal_log_branch=lon == s.eye(5),
                  global_SL5=zero(mer.det()-1),
                  global_relator=zero(dense_word(data['base_relator'], [mer, mer])-s.eye(5)),
                  actual_longitude=zero(dense_word(data['base_longitude'], [mer, mer])-lon),
                  meridian_nonunitary=not zero(mer.H*mer-s.eye(5)),
                  zero_root_threshold=bool(zero_root_min > s.Rational(3, 4)),
                  all_Fourier_square=zero(lam-2*pairing(v+k/2)-pairing(k)/2),
                  integer_Gram=zero(pairing(s.Matrix([m, n]))-minimum*integer_form),
                  nonzero_Fourier_threshold=bool(2*s.pi**2*minimum > s.Rational(3, 4)),
                  neutral_sectors_retained=any(integers[i] == integers[j] for i in range(5) for j in range(i)),
                  scale_changes_threshold=bool(zero_root_min/10000 < s.Rational(3, 4)))
    return dict(checks=checks, X=X, meridian=mer, longitude=lon,
                zero_root_lower_bound=zero_root_min,
                nonzero_Fourier_lower_bound=2*s.pi**2*minimum)


def serial(value):
    if isinstance(value, s.MatrixBase):
        return [[str(x) for x in row] for row in value.tolist()]
    if isinstance(value, s.Basic):
        return str(value)
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


def run():
    groups = dict(source=source_controls(), monomial0=monomial_controls(0), monomial1=monomial_controls(1),
                  square_periods=period_controls('square'), hex_periods=period_controls('hexagonal'),
                  projective=projective_controls(), transport=transport_controls(),
                  square_abelian=abelian_controls('square'), hex_abelian=abelian_controls('hexagonal'))
    checks = {name+'_'+key: bool(value) for name, group in groups.items() for key, value in group['checks'].items()}
    return serial(dict(scope='Necessary matching of literal cone ends, not global harmonic existence or physical chirality',
                       checks=checks, all_checks_pass=all(checks.values()), groups=groups))


if __name__ == '__main__':
    answer = run()
    print(json.dumps(answer, indent=2))
    raise SystemExit(0 if answer['all_checks_pass'] else 1)
