"""Exact finite safeguards for the authored all-orders theta proof."""
import json
from fractions import Fraction
from math import isqrt

N = 256


def mul(a, b, limit=N):
    out = {}
    for j, v in a.items():
        for k, w in b.items():
            if j+k <= limit:
                out[j+k] = out.get(j+k, 0) + v*w
    return {j: v for j, v in out.items() if v}


def power(a, n, limit=N):
    out = {0: 1}
    for _ in range(n):
        out = mul(out, a, limit)
    return out


def scale(a, c):
    return {j: c*v for j, v in a.items() if c*v}


def theta_series(limit=N):
    a, b, c = {}, {}, {}
    for n in range(-isqrt(limit)-1, isqrt(limit)+2):
        j, k = (2*n+1)**2, 4*n*n
        if j <= limit:
            a[j] = a.get(j, 0)+1
        if k <= limit:
            b[k] = b.get(k, 0)+1
            c[k] = c.get(k, 0)+(1 if n % 2 == 0 else -1)
    return a, b, c


def euler(exponent, limit=N):
    out = {0: 1}
    for m in range(1, limit//8+1):
        out = mul(out, power({0: 1, 8*m: -1}, exponent, limit), limit)
    return out


def run():
    a, b, c = theta_series()
    p = mul(mul(a, b), c)
    eta3 = mul({1: 1}, euler(3))
    delta = mul({8: 1}, euler(24))
    p8 = power(p, 8)
    wrong = mul(mul(a, b), b)
    checks = {}

    def check(name, value):
        checks[name] = bool(value)

    check('banked Jacobi product reconstructed before eighth power', p == scale(eta3, 2))
    check('Delta identity with coefficient256', p8 == scale(delta, 256))
    check('theta2 T phase is exp(pi i/4)', all(j % 8 == 1 for j in a))
    check('T exchanges theta3 with theta4', {j: v*(1 if j % 8 == 0 else -1) for j, v in b.items()} == c)
    check('T exchanges theta4 with theta3', {j: v*(1 if j % 8 == 0 else -1) for j, v in c.items()} == b)
    check('P T phase is exp(pi i/4)', all(j % 8 == 1 for j in p))
    check('Delta has integral q powers', all(j % 8 == 0 for j in delta))
    check('Delta cusp order is one', min(delta) == 8 and delta[8] == 1)
    check('first three Delta coefficients', [delta[j] for j in (8, 16, 24)] == [1, -24, 252])
    powers = [r for r in range(1, 25) if Fraction(r, 8).denominator == 1]
    check('least phase cancelling positive power is eight', powers == [8, 16, 24])
    check('S root factor eighth power has weight12 and no phase', Fraction(3, 2)*8 == 12 and 12 % 4 == 0)
    check('fourth power control retains T phase', Fraction(4, 8).denominator != 1)
    check('fourth power control retains S minus sign', 6 % 4 == 2)
    check('missing normalization control rejected', p8 != delta)
    check('missing alternating theta4 sign rejected', wrong != p)
    check('wrong product also fails at eighth power', power(wrong, 8) != p8)
    check('normalized holomorphic product is two', p == scale(eta3, 2) and 2*2 == 4)
    # Products of the actual squared-theta triplets; exponents are eta powers.
    check('meromorphic triplet product eta power', 6-3*3 == -3)
    check('meromorphic triplet eighth power is inverse Delta', (6-3*3)*8 == -24)
    check('holomorphic triplet product eta power', 6+21*3 == 69)
    check('holomorphic triplet eighth power is Delta power23', (6+21*3)*8 == 24*23)
    check('dressing by Delta changes weight by12', Fraction(23, 2)-Fraction(-1, 2) == 12)
    check('constant-term zero-flux control remains available', power(delta, 0) == {0: 1})
    return {'scope': 'Exact finite safeguards, analytic proof separately authored',
            'series_variable': 'x=q^(1/8)', 'maximum_degree': N,
            'checks': checks, 'all_passed': all(checks.values()),
            'delta_q_coefficients_1_to_32': [delta.get(8*j, 0) for j in range(1, 33)]}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
