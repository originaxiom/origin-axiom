"""Exact local node transport, not a total-space metric or particle calculation."""
import json
import sympy as s


def simp(x):
    return s.simplify(s.expand_complex(x))


def clean(m):
    return m.applyfunc(simp)


def zero(m):
    return all(simp(x) == 0 for x in m)


def coefficient():
    a0 = s.diag(s.I, -s.I)
    b0 = s.Matrix([[0, 1], [-1, 0]])
    a = s.diag(-a0, a0, -a0)
    b = s.diag(b0, -b0, -b0)
    p13 = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    t = s.kronecker_product(p13, (s.eye(2)+a0)/s.sqrt(2))
    return a, b, t


def joint_basis():
    e = s.eye(6)
    return s.Matrix.hstack((e[:, 0]+e[:, 4])/s.sqrt(2),
                           (e[:, 1]+e[:, 5])/s.sqrt(2),
                           (e[:, 0]-e[:, 4])/s.sqrt(2),
                           (e[:, 1]-e[:, 5])/s.sqrt(2), e[:, 2], e[:, 3])


def eighth_exponent(value):
    zeta = (1+s.I)/s.sqrt(2)
    choices = [j for j in range(8) if simp(value-zeta**j) == 0]
    if len(choices) != 1:
        raise ValueError('not a unique eighth root')
    return choices[0]


def inverse_minus_identity(u):
    eye = s.eye(u.rows)
    if not zero(u**4+eye):
        raise ValueError('fourth-power hypothesis fails')
    return clean(-(eye+u+u**2+u**3)/2)


def complex_matrices(u, v):
    if not zero(u*v-v*u):
        raise ValueError('a local torus requires commuting transports')
    p, q = u-s.eye(u.rows), v-s.eye(v.rows)
    return s.Matrix.vstack(p, q), s.Matrix.hstack(-q, p)


def betti(u, v):
    d0, d1 = complex_matrices(u, v)
    r0, r1, n = d0.rank(), d1.rank(), u.rows
    return n-r0, 2*n-r0-r1, n-r1


def run():
    checks, rows = {}, []
    def check(name, condition):
        checks[name] = bool(condition)
    a, b, t = coefficient()
    eye = s.eye(6)
    check('actual unitary coefficient', zero(a.H*a-eye) and zero(b.H*b-eye) and zero(t.H*t-eye))
    check('actual L fixes a', zero(t*a*t.H-a))
    check('actual L sends b to ab', zero(t*b*t.H-a*b))
    check('actual marked puncture minus identity', zero(a*b*a.H*b.H+eye))
    check('vanishing cycle fourth power', zero(a**4-eye))
    check('cusp move fourth power minus identity', zero(t**4+eye))
    check('vanishing circle is acyclic', (a-eye).rank() == 6)
    basis = joint_basis()
    da, dt = clean(basis.H*a*basis), clean(basis.H*t*basis)
    check('joint basis is unitary', zero(basis.H*basis-eye))
    check('actual joint diagonalization', da.is_diagonal() and dt.is_diagonal())
    phase_a = [eighth_exponent(da[j, j]) for j in range(6)]
    phase_t = [eighth_exponent(dt[j, j]) for j in range(6)]
    zeta = (1+s.I)/s.sqrt(2)
    for k in range(4):
        check(f'framing {k} primitive integer basis', s.Matrix([[k+1, k], [1, 1]]).det() == 1)
        for lift in (1, -1):
            u0, v0 = clean(lift*a**(k+1)*t), clean(lift*a**k*t)
            check(f'{k} {lift} vanishing cycle recovered', zero(u0*v0.H-a))
            check(f'{k} {lift} framing period four', zero(lift*a**(k+4)*t-v0))
            for sx in (1, -1):
                for sy in (1, -1):
                    label = f'k{k} lift{lift} spin{sx},{sy}'
                    u, v = sx*u0, sy*v0
                    check(label+' commute', zero(u*v-v*u))
                    check(label+' fourth powers', zero(u**4+eye) and zero(v**4+eye))
                    pinv = inverse_minus_identity(u)
                    check(label+' polynomial inverse', zero((u-eye)*pinv-eye) and zero(pinv*(u-eye)-eye))
                    d0, d1 = complex_matrices(u, v)
                    h1 = s.Matrix.hstack(pinv, s.zeros(6))
                    h2 = s.Matrix.vstack(s.zeros(6), pinv)
                    check(label+' complex', zero(d1*d0))
                    check(label+' contraction all degrees', zero(h1*d0-eye) and zero(d0*h1+h2*d1-s.eye(12)) and zero(d1*h2-eye))
                    px = [((k+1)*j+l+(4 if lift*sx < 0 else 0)) % 8 for j, l in zip(phase_a, phase_t)]
                    py = [(k*j+l+(4 if lift*sy < 0 else 0)) % 8 for j, l in zip(phase_a, phase_t)]
                    check(label+' spectral route agrees', zero(basis.H*u*basis-s.diag(*[zeta**j for j in px])) and
                          zero(basis.H*v*basis-s.diag(*[zeta**j for j in py])))
                    check(label+' no invariant branch vector', all(j % 2 == 1 for j in px+py))
                    min_sq = min(s.Rational(min(j, 8-j)**2+min(l, 8-l)**2, 64) for j, l in zip(px, py))
                    check(label+' flat link Fourier bound', min_sq >= s.Rational(1, 32))
                    check(label+' power cover trivializes', zero(u**8-eye) and zero(v**8-eye))
                    check(label+' deck projection required', zero(sum((u**j for j in range(8)), s.zeros(6))/8))
                    rows.append({'framing_mod_four': k, 'lift': lift, 'spin': [sx, sy],
                                 'joint_numerators_over_eight': list(zip(px, py)),
                                 'flat_link_minimum_squared_frequency': str(min_sq)})
    check('trivial coefficient positive control', betti(eye, eye) == (6, 12, 6))
    check('invariant summand positive control', betti(s.diag(1, -1), s.diag(1, -1)) == (1, 2, 1))
    check('actual local rank control', betti(a*t, t) == (0, 0, 0))
    check('dropping T changes local spectrum', not zero(a**4+eye) and not zero(eye**4+eye))
    n = s.Symbol('n', integer=True)
    x, y = s.symbols('x y', positive=True)
    # The divisor statement is all-integer; the constant phase simplification is a guard.
    check('integer cusp twist has trivial local phase', s.simplify(s.exp(2*s.pi*s.I*n)) == 1)
    check('q twist changes both logarithmic orders', s.simplify(x*s.diff((x*y)**n, x)/(x*y)**n) == n and
          s.simplify(y*s.diff((x*y)**n, y)/(x*y)**n) == n)
    return {'all_passed': all(checks.values()), 'checks': checks, 'rows': rows,
            'scope': 'local coefficient contraction and flat-link comparison, not a total-space Fredholm index'}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
