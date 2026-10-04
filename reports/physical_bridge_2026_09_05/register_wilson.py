"""R90 exact character registers in the existing supplied gauge model."""
import ast
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'parent_gluing_character.py'
SOURCE_SHA = '2d01c892b75acac30355aefed48af400e9e4376510c02033811d7d9c2048a0c9'
LABELS = ('1', '5', 'bar5', '10', 'bar10', '24')
ZERO = (0, 0, 0, 0)


@lru_cache(None)
def retained():
    raw = SOURCE.read_bytes()
    if sha256(raw).hexdigest() != SOURCE_SHA:
        raise RuntimeError('Changed retained root source')
    tree = ast.parse(raw, filename=str(SOURCE))
    names = {'roots', 'simple', 'reps', 'roster', 'root_weights'}
    body = [n for n in tree.body if
            isinstance(n, ast.FunctionDef) and n.name in names or
            isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and
                                              t.id == 'BRANCHES' for t in n.targets)]
    if {n.name for n in body if isinstance(n, ast.FunctionDef)} != names:
        raise RuntimeError('Missing retained root primitives')
    ns = {'Counter': Counter, 'combinations': combinations, 'product': product}
    exec(compile(ast.Module(body=body, type_ignores=[]), str(SOURCE), 'exec'), ns)
    return ns


def clean(poly):
    return Counter({w: n for w, n in poly.items() if n})


def sum_chars(*terms):
    out = Counter()
    for factor, term in terms:
        for w, n in term.items():
            out[w] += factor * n
    return clean(out)


def conjugate(poly):
    return Counter({tuple(-x for x in w): n for w, n in poly.items()})


def char(label):
    # z5=(z1*z2*z3*z4)^-1; transform retained Dynkin weights literally.
    out = Counter()
    for w in retained()['reps']()[label]:
        out[tuple(sum(w[i:]) for i in range(4))] += 1
    return out


def multiply(a, b):
    out = Counter()
    for u, c in a.items():
        for v, d in b.items():
            out[tuple(x + y for x, y in zip(u, v))] += c * d
    return clean(out)


@lru_cache(None)
def weyl_density():
    delta = Counter()
    for perm in permutations(range(5)):
        sign = (-1) ** sum(perm[i] > perm[j] for i, j in combinations(range(5), 2))
        delta[tuple(perm[i] - perm[4] for i in range(4))] += sign
    return multiply(delta, conjugate(delta))


def haar(a, b):
    # integral chi_a conjugate(chi_b): genuine integer constant term.
    density = weyl_density()
    numerator = sum(c * d * density.get(tuple(y - x for x, y in zip(u, v)), 0)
                    for u, c in a.items() for v, d in b.items())
    return Fraction(numerator, 120)


def probe(label):
    c = char(label)
    return sum_chars((1, c), (-1, conjugate(c)))


def moment(poly, hs, degree):
    if len(hs) != 5 or sp.expand(sum(hs)) != 0:
        raise ValueError('A traceless five-coordinate Cartan is required')
    values = (hs[0], hs[1], hs[2], hs[3])
    # poly is already in determinant-one eigenvalue coordinates.
    return sp.expand(sum(n * sum(w[i] * values[i] for i in range(4)) ** degree
                         for w, n in poly.items()))


def seventh(poly, hs=(1, 1, 1, 1, -4)):
    if len(hs) != 5 or sum(hs) != 0:
        raise ValueError('Invalid unitary determinant-one fixture')
    coefficients = [0] * 7
    for w, n in poly.items():
        coefficients[sum(w[i] * hs[i] for i in range(4)) % 7] += n
    # Phi7 is monic with all coefficients one.
    return tuple(coefficients[i] - coefficients[6] for i in range(6))


@lru_cache(None)
def audit():
    checks = {}

    def check(name, result):
        if type(result) is not bool:
            raise TypeError('Ungrounded predicate: ' + name)
        if name in checks:
            raise ValueError('Duplicate predicate: ' + name)
        checks[name] = result

    r = retained()
    actual = r['root_weights']()
    simples = r['simple']()
    check('actual240_roots', len(r['roots']()) == 240)
    check('full248_roster', actual == r['roster']() and sum(actual.values()) == 248)
    wrong = r['BRANCHES'][:4] + (('5', '10'), ('bar5', 'bar10'))
    check('wrong_bar_roster_rejected', sum(r['roster'](wrong).values()) == 248 and
          r['roster'](wrong) != actual)
    check('a4_factors_commute', all(sum(x * y for x, y in zip(a, b)) == 0
                                 for a in simples[:4] for b in simples[4:]))
    check('parent_adjoint_duality_even', actual == conjugate(actual))
    kernel = [(a, b) for a, b in product(range(5), repeat=2)
              if all(sum((i + 1) * (a * w[i] + b * w[i + 4])
                         for i in range(4)) % 5 == 0 for w in actual)]
    check('center_kernel_actual', kernel == [(j, -2 * j % 5) for j in range(5)])
    check('individual_su5_faithful', all((a == 0) == (b == 0) for a, b in kernel))
    cs = {l: char(l) for l in LABELS}
    check('haar_density_normalized', haar(cs['1'], cs['1']) == 1)
    for a, b in product(LABELS, repeat=2):
        check('haar_gram_' + a + '_' + b, haar(cs[a], cs[b]) == int(a == b))
    R = sum_chars((1, cs['10']), (1, cs['bar5']))
    dual = conjugate(R)
    balanced = sum_chars((2, R), (2, dual))
    for label, expected in (('10', 1), ('5', -1)):
        check('chiral_register_' + label, haar(R, probe(label)) == expected)
        check('dual_register_' + label, haar(dual, probe(label)) == -expected)
        check('paired_register_' + label, haar(balanced, probe(label)) == 0)
    check('paired_matter_retained', sum(balanced.values()) == 60)
    odd = sum_chars((1, R), (-1, dual))
    check('odd_character_not_zero', bool(odd))
    check('duality_negates_odd', conjugate(odd) == sum_chars((-1, odd)))
    check('balanced_odd_identically_zero', not sum_chars((1, balanced), (-1, conjugate(balanced))))
    q = sp.symbols('h1:5')
    hs = (*q, -sum(q))
    p2, p3, p5 = (sum(h ** j for h in hs) for j in (2, 3, 5))
    m1, m3, m5 = (moment(R, hs, n) for n in (1, 3, 5))
    check('linear_trace_universal_zero', m1 == 0)
    check('cubic_anomaly_universal_zero', m3 == 0)
    check('quintic_universal_identity', sp.expand(m5 - 10 * p2 * p3 + 12 * p5) == 0)
    check('quintic_universal_not_zero', m5 != 0)
    anomalous = sum_chars((1, cs['10']), (1, cs['5']))
    check('anomalous_control_cubic', sp.expand(moment(anomalous, hs, 3) - 2 * p3) == 0)
    check('anomalous_control_not_zero', moment(anomalous, hs, 3) != 0)
    block = (1, 1, 1, 1, -4)
    check('block_quintic240', moment(R, block, 5) == 240)
    check('block_odd_quintic480', moment(odd, block, 5) == 480)
    check('odd_taylor_coefficient4i', Fraction(int(moment(odd, block, 5)), 120) == 4)
    for n in (1, 3, 5, 7, 9):
        check('balanced_odd_moment_' + str(n), moment(balanced, hs, n) == 0)
    fixture = (-4, -8, 2, -9, 1, -10)
    check('unitary_seventh_fixture', seventh(odd) == fixture)
    check('unitary_seventh_nonzero', any(seventh(odd)))
    check('reversed_unitary_fixture', seventh(odd, tuple(-x for x in block)) == tuple(-x for x in fixture))
    x, y, t = sp.symbols('x y t', real=True)
    amplitude = 2 * x * y
    check('two_odd_slots_joint_even', amplitude.subs({x: -x, y: -y}, simultaneous=True) == amplitude)
    check('fixed_probe_hears_linearly', sp.diff(amplitude, x) == 2 * y)
    check('both_scaled_quadratic', amplitude.subs({x: t, y: t}, simultaneous=True) == 2 * t ** 2)
    for n, value in ((1, m1), (3, m3), (5, m5)):
        check('fixed_gauge_character_structure_variation_' + str(n), sp.diff(value, t) == 0)
    return {'checks': checks, 'passed': sum(checks.values()), 'total': len(checks),
            'seventh_odd_coefficients': list(seventh(odd)), 'haar_10_register': str(haar(R, probe('10'))),
            'haar_5_register': str(haar(R, probe('5'))), 'block_fifth_moment': int(moment(R, block, 5)),
            'physical_chirality_derived': False, 'source_generated': False,
            'quantum_measure_derived': False, 'full_goal_achieved': False}


def main():
    out = audit()
    for name, value in out['checks'].items():
        print(json.dumps({'check': name, 'pass': value}, sort_keys=True))
    print(json.dumps({k: v for k, v in out.items() if k != 'checks'}, sort_keys=True))
    return 0 if out['passed'] == out['total'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
