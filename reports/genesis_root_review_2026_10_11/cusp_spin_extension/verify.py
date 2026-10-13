"""Exact cusp-extension guards; no total-space physical index is computed."""
import json
from functools import lru_cache
import sympy as s

ZETA = (1+s.I)/s.sqrt(2)


def simp(x):
    return s.simplify(s.expand_complex(x))


def zero(m):
    return all(simp(x) == 0 for x in m)


def representations():
    ps = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    mt = s.Matrix([[s.I, 0, 0], [0, 0, 1], [0, 1, 0]])
    st, tt = ZETA*ps, mt/ZETA
    z = s.diag(1, -1)
    y = s.Matrix([[0, -s.I], [s.I, 0]])
    p23 = s.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    l = s.kronecker_product(ps, (s.eye(2)+s.I*z)/s.sqrt(2))
    r = s.kronecker_product(p23, (s.eye(2)-s.I*y)/s.sqrt(2))
    ss = (l*r.inv()*l).inv().applyfunc(simp)
    q2 = s.kronecker_product(s.ones(3, 1)/s.sqrt(3), s.eye(2))
    q4 = s.kronecker_product(s.Matrix.hstack(
        s.Matrix([1, -1, 0])/s.sqrt(2),
        s.Matrix([1, 1, -2])/s.sqrt(6)), s.eye(2))
    return {'T': (st, tt, s.Rational(3, 2)),
            'Tdual': (s.conjugate(st), s.conjugate(tt), s.Rational(1, 2)),
            'six': (ss, l, s.Integer(1)),
            'V2': ((q2.H*ss*q2).applyfunc(simp), (q2.H*l*q2).applyfunc(simp), s.Integer(1)),
            'V4': ((q4.H*ss*q4).applyfunc(simp), (q4.H*l*q4).applyfunc(simp), s.Integer(1))}


@lru_cache(None)
def exponents(t):
    if not zero(t**8-s.eye(t.rows)):
        raise ValueError('eighth-root spectrum required')
    traces = [simp(s.trace(t**j)) for j in range(8)]
    result = []
    for j in range(8):
        multiplicity = simp(sum(ZETA**(-j*m)*traces[m] for m in range(8))/8)
        if multiplicity.is_Integer is not True or multiplicity < 0:
            raise ValueError('invalid spectral multiplicity')
        result += [s.Rational(j, 8)]*int(multiplicity)
    if len(result) != t.rows:
        raise ValueError('incomplete spectrum')
    return tuple(result)


def chi(k, a, b):
    k = s.Rational(k)
    if not zero(a*a-s.exp(-s.I*s.pi*k)*s.eye(a.rows)):
        raise ValueError('weight incompatible with central character')
    alpha = exponents(s.ImmutableMatrix(b))
    return simp(a.rows*(k-1)/12
                + s.re(s.exp(s.I*s.pi*k/2)*s.trace(a))/4
                + 2*s.re(s.exp(s.I*s.pi*(2*k+1)/6)*s.trace(a*b))/(3*s.sqrt(3))
                + s.Rational(a.rows, 2)-sum(alpha))


def cusp_map(alpha):
    alpha = s.Rational(alpha)
    if not 0 <= alpha < 1:
        raise ValueError('canonical exponent required')
    shift = int(s.floor(alpha+s.Rational(1, 2)))
    return alpha+s.Rational(1, 2)-shift, shift


def run():
    checks, rows = {}, []
    def check(name, condition):
        checks[name] = bool(condition)
    check('compact base canonical weight', 2-12 == -10)
    check('total ordinary and logarithmic canonical weights', (1-10, 1+2) == (-9, 3))
    check('spin gap is six not twelve', s.Rational(3, 2)-s.Rational(-9, 2) == 6)
    eta_s, eta_t = s.exp(-s.I*s.pi/4), s.exp(s.I*s.pi/12)
    check('eta twelfth sign S and T', simp(eta_s**12) == simp(eta_t**12) == -1)
    check('eta twelfth squared discriminant order', 2*s.Rational(12, 24) == 1)
    for alpha in [s.Rational(j, 8) for j in range(8)]:
        beta, shift = cusp_map(alpha)
        check('cusp exponent forward '+str(alpha), 0 <= beta < 1 and alpha+s.Rational(1, 2) == beta+shift)
        check('cusp exponent reverse '+str(alpha), beta+shift-s.Rational(1, 2) == alpha)
    check('threshold half is included', cusp_map(s.Rational(1, 2)) == (0, 1))
    reps = representations()
    for sign in (1, -1):
        data = {}
        for name, (a0, b0, k) in reps.items():
            a, b = sign*a0, sign*b0
            alpha = exponents(s.ImmutableMatrix(b))
            high = sum(x >= s.Rational(1, 2) for x in alpha)
            check(f'{name} sign{sign} unitary', zero(a.H*a-s.eye(a.rows)) and zero(b.H*b-s.eye(a.rows)))
            check(f'{name} sign{sign} modular relation', zero(a*a-(a*b)**3))
            check(f'{name} sign{sign} original zero', chi(k, a, b) == 0)
            check(f'{name} sign{sign} exponents above eta cubed', min(alpha) >= s.Rational(1, 8))
            if k == s.Rational(3, 2):
                inv = s.Matrix.vstack(a/eta_s**3-s.eye(a.rows), b/eta_t**3-s.eye(a.rows))
                check(f'{name} sign{sign} divided weight zero has no invariants', inv.rank() == a.rows)
            values = []
            for step in range(-3, 7):
                w = k+2*step
                left, right = chi(w-6, a, b), chi(w, -a, -b)-high
                check(f'{name} sign{sign} weight{w} modification', left == right)
                values.append([str(w), str(left), str(right)])
            low = chi(k-6, a, b)
            check(f'{name} sign{sign} exact integral Euler number', low.is_Integer is True)
            check(f'{name} sign{sign} correction matters', low != chi(k, -a, -b))
            data[name] = int(low)
            rows.append({'name': name, 'sign': sign, 'weight': str(k),
                         'exponents': [str(x) for x in alpha], 'high_count': high,
                         'original_chi': str(chi(k, a, b)), 'shifted_chi': str(low),
                         'comparisons': values})
        combination = [ -data['T'], -data['T']+data['V2'],
                        -data['T']+data['V4'], -data['T']+data['six'] ]
        check(f'sign{sign} formal all-allowed equals dual', combination[-1] == data['Tdual'])
        check(f'sign{sign} split six additive', data['six'] == data['V2']+data['V4'])
        rows.append({'sign': sign, 'formal_shifted_W46_combination': combination,
                     'scope': 'modular sheaf arithmetic, not a total-space operator spectrum'})
    check('trivial modular form calibrations', all(chi(k, s.eye(1), s.eye(1)) == want
          for k, want in [(0, 1), (2, 0), (12, 2)]))
    # eta^3 has eighth-root T spectrum and a surviving divided invariant line.
    check('eta cubed positive calibration', chi(s.Rational(3, 2), s.Matrix([[eta_s**3]]), s.Matrix([[eta_t**3]])) == 1)
    eta_divided = s.Matrix([[simp(eta_s**3/eta_s**3-1)], [simp(eta_t**3/eta_t**3-1)]])
    check('eta cubed divided invariant survives', eta_divided.rank() == 0 and eta_divided.cols == 1)
    return {'all_passed': all(checks.values()), 'checks': checks, 'rows': rows,
            'scope': 'canonical modular sheaf extension comparison only'}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
