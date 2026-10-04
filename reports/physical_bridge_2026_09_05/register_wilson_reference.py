"""R90 separate finite-field Haar and Fraction moment reference; no native import."""
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json

LABELS = ('1', '5', 'bar5', '10', 'bar10', '24')


@lru_cache(None)
def grid_gram():
    p, order = 53, 13
    root = next(x for x in range(2, p) if pow(x, order, p) == 1)
    vals = [pow(root, k, p) for k in range(order)]
    gram = [[0] * 6 for _ in range(6)]
    for exps in product(range(order), repeat=4):
        zs = [vals[e] for e in (*exps, -sum(exps) % order)]
        inv = [pow(z, p - 2, p) for z in zs]
        den = 1
        for i in range(5):
            for j in range(i + 1, 5):
                den = den * (zs[i] - zs[j]) * (inv[i] - inv[j]) % p
        if not den:
            continue
        a, b = sum(zs) % p, sum(inv) % p
        c = (a * a - sum(z * z for z in zs)) * pow(2, p - 2, p) % p
        d = (b * b - sum(z * z for z in inv)) * pow(2, p - 2, p) % p
        f = [1, a, b, c, d, (a * b - 1) % p]
        fc = [1, b, a, d, c, f[5]]
        for i in range(6):
            for j in range(6):
                gram[i][j] = (gram[i][j] + den * f[i] * fc[j]) % p
    norm = pow(120 * order ** 4 % p, p - 2, p)
    return [[n * norm % p for n in row] for row in gram]


def moments(h, degree, conjugate_five=True):
    if len(h) != 5 or sum(h) != 0:
        raise ValueError('Invalid Cartan')
    # Ordered exterior-basis coefficients, independently of Dynkin weights.
    total = sum((h[i] + h[j]) ** degree for i in range(5) for j in range(i))
    return total + sum((-z if conjugate_five else z) ** degree for z in h)


def cyclic_odd(block, order=7):
    c = [0] * order
    for i in range(5):
        for j in range(i):
            e = block[i] + block[j]
            c[e % order] += 1
            c[-e % order] -= 1
        c[-block[i] % order] += 1
        c[block[i] % order] -= 1
    # Independent high-degree polynomial subtraction by the monic Phi7.
    work = c[:]
    for j in range(6, len(work)):
        coefficient = work[j]
        for k in range(7):
            work[j - 6 + k] -= coefficient
    return tuple(work[:6])


@lru_cache(None)
def audit():
    checks = {}
    gram = grid_gram()
    for i, a in enumerate(LABELS):
        for j, b in enumerate(LABELS):
            checks['grid_haar_' + a + '_' + b] = gram[i][j] == int(i == j)
    for q in product((-1, 0, 1), repeat=4):
        h = [Fraction(z) for z in (*q, -sum(q))]
        name = '_'.join(str(z) for z in q)
        p2, p3, p5 = (sum(z ** n for z in h) for n in (2, 3, 5))
        checks['linear_' + name] = moments(h, 1) == 0
        checks['cubic_' + name] = moments(h, 3) == 0
        checks['quintic_' + name] = moments(h, 5) == 10 * p2 * p3 - 12 * p5
        checks['anomalous_' + name] = moments(h, 3, False) == 2 * p3
    block = (1, 1, 1, 1, -4)
    expected = (-4, -8, 2, -9, 1, -10)
    checks['block_fifth240'] = moments(block, 5) == 240
    checks['dual_block_fifth_minus240'] = moments(tuple(-z for z in block), 5) == -240
    checks['cyclic_fixture'] = cyclic_odd(block) == expected
    checks['cyclic_reverse'] = cyclic_odd(tuple(-z for z in block)) == tuple(-z for z in expected)
    checks['special_holonomy_can_be_blind'] = cyclic_odd((0, 0, 0, 0, 0)) == (0,) * 6
    # Vector coordinates in the independently projected character basis.
    R, dual, balanced = (0, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0), (0, 2, 2, 2, 2, 0)
    for name, vector, sign in (('R', R, 1), ('dual', dual, -1), ('paired', balanced, 0)):
        for label, a, b, value in (('10', 3, 4, sign), ('5', 1, 2, -sign)):
            got = sum(vector[i] * (gram[i][a] - gram[i][b]) for i in range(6)) % 53
            checks['grid_register_' + name + '_' + label] = got == value % 53
    if any(type(v) is not bool for v in checks.values()):
        raise TypeError('Ungrounded reference predicate')
    return {'checks': checks, 'passed': sum(checks.values()), 'total': len(checks),
            'torus_order': 13, 'finite_field_prime': 53, 'grid_points': 13 ** 4,
            'no_constant_term_alias_bound': 12, 'characteristic_zero_certificate': False,
            'non_author_review': False, 'physics_derived': False}


if __name__ == '__main__':
    out = audit()
    print(json.dumps({k: v for k, v in out.items() if k != 'checks'}, sort_keys=True))
    failed = [k for k, v in out['checks'].items() if not v]
    if failed:
        print(json.dumps({'failed': failed}))
    raise SystemExit(0 if not failed else 1)
