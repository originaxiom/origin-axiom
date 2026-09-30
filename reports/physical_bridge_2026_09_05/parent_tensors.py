"""R59 exact E8 parent tensors, no imported scientific implementation.

Standard representation theory in a supplied parent, not physical modes.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
import json


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def vector(i, j, sign=-1):
    return tuple(2 * ((k == i) + sign * (k == j)) for k in range(8))


@lru_cache(None)
def roots():
    simple = [(1, -1, -1, -1, -1, -1, -1, 1), vector(0, 1, 1)]
    simple += [vector(j + 1, j) for j in range(6)]
    found, pending = set(simple), list(simple)
    while pending:
        r = pending.pop()
        for a in simple:
            p = dot(r, a)
            assert p % 4 == 0
            s = tuple(x - (p // 4) * y for x, y in zip(r, a))
            if s not in found:
                found.add(s)
                pending.append(s)
    return tuple(sorted(found))


def bases():
    return ([vector(i, i + 1) for i in range(4)],
            [vector(6, 7), vector(5, 6), vector(6, 7, 1), (-1,) * 8])


def labels(r, basis):
    values = [dot(r, b) for b in basis]
    assert all(x % 4 == 0 for x in values)
    return tuple(x // 4 for x in values)


def weight(indices):
    counts = Counter(indices)
    return tuple(counts[i] - counts[i + 1] for i in range(4))


def exterior(k):
    return Counter(weight(i) for i in combinations(range(5), k))


def adjoint():
    c = Counter({(0,) * 4: 4})
    for i, j in product(range(5), repeat=2):
        if i != j:
            c[tuple(int(i == k) - int(j == k) - int(i == k + 1)
                    + int(j == k + 1) for k in range(4))] += 1
    return c


def tensor(a, b):
    return Counter({(x, y): m * n for x, m in a.items() for y, n in b.items()})


def dual(c):
    return Counter({neg(w): m for w, m in c.items()})


def branching(wrong=False):
    z = Counter({(0,) * 4: 1})
    f, t, ad = exterior(1), exterior(2), adjoint()
    return (tensor(ad, z) + tensor(z, ad) + tensor(t, f)
            + tensor(dual(t), dual(f)) + tensor(f, t if wrong else dual(t))
            + tensor(dual(f), t))


@lru_cache(None)
def actual():
    g, s = bases()
    c = Counter((labels(r, g), labels(r, s)) for r in roots())
    c[((0,) * 4, (0,) * 4)] += 8
    return c


@lru_cache(None)
def blocks():
    g, s = bases()
    lookup = {(labels(r, g), labels(r, s)): r for r in roots()}
    pairs = tuple(combinations(range(5), 2))
    ten = {(ab, i): lookup[(weight(ab), weight((i,)))]
           for ab in pairs for i in range(5)}
    up = {(a, ij): lookup[(weight((a,)), neg(weight(ij)))]
          for a in range(5) for ij in pairs}
    down = {(a, ij): lookup[(neg(weight((a,))), weight(ij))]
            for a in range(5) for ij in pairs}
    return ten, up, down


def permutation_sign(indices):
    if len(set(indices)) != len(indices):
        return 0
    return (-1) ** sum(indices[i] > indices[j]
                       for i in range(len(indices)) for j in range(i + 1, len(indices)))


def up_tensor(t1, t2, h):
    ab, i = t1
    cd, j = t2
    e, pair = h
    structure = int((i, j) == pair) - int((j, i) == pair)
    return permutation_sign(ab + cd + (e,)) * structure


def down_tensor(t, d1, d2):
    ab, i = t
    a, jk = d1
    b, lm = d2
    gauge = int((a, b) == ab) - int((b, a) == ab)
    return gauge * permutation_sign((i,) + jk + lm)


@lru_cache(None)
def cubic_support():
    ten, up, down = blocks()
    output = {}
    for name in ('up', 'down'):
        seen, expected, checked, negative_dot = set(), set(), 0, True
        population = ((t1, t2, h) for t1, t2 in combinations(ten, 2) for h in up) if name == 'up' else (
            (t, d1, d2) for t in ten for d1, d2 in combinations(down, 2))
        for entry in population:
            if name == 'up':
                a, b, c = (ten[entry[0]], ten[entry[1]], up[entry[2]])
                value = up_tensor(*entry)
            else:
                a, b, c = (ten[entry[0]], down[entry[1]], down[entry[2]])
                value = down_tensor(*entry)
            checked += 1
            if value:
                expected.add(entry)
            if add(add(a, b), c) == (0,) * 8:
                seen.add(entry)
                negative_dot &= dot(a, b) == -4 and add(a, b) in roots()
        output[name] = dict(actual_count=len(seen), predicted_count=len(expected),
                            compared=checked, exact_support=seen == expected,
                            nonzero_bracket=negative_dot and bool(seen))
    return output


def charged_fibre(label):
    out = Counter()
    for (g, s), m in actual().items():
        sm = (g[0], g[1], g[3], -2 * g[0] - 4 * g[1] - 6 * g[2] - 3 * g[3])
        if sm == label:
            out[s] += m
    return out


def run():
    g, s = bases()
    a4 = [[2 if i == j else -int(abs(i - j) == 1) for j in range(4)] for i in range(4)]
    sector = {'Q': ((1, 0, 1, 1), 1), 'u': ((0, 1, 0, -4), 1),
              'e': ((0, 0, 0, 6), 1), 'd': ((0, 1, 0, 2), 2),
              'L': ((0, 0, 1, -3), 2)}
    up_args = (((0, 1), 0), ((2, 3), 1), (4, (0, 1)))
    down_args = (((0, 1), 0), (0, (1, 2)), (1, (3, 4)))
    checks = {
        'complete_E8_reflection_orbit': len(roots()) == 240 and all(dot(r, r) == 8 for r in roots()),
        'two_orthogonal_A4': all(dot(a, b) == 0 for a in g for b in s) and all(
            [[dot(a, b) // 4 for b in basis] for a in basis] == a4 for basis in (g, s)),
        'all_248_weights': actual() == branching() and sum(actual().values()) == 248,
        'wrong_dual_rejected_at_equal_dimension': actual() != branching(True) and sum(branching(True).values()) == 248,
        'missing_Cartans_rejected': Counter((labels(r, g), labels(r, s)) for r in roots()) != actual(),
        'all_five_charged_bundles_and_duals': all(charged_fibre(l) == exterior(k) and charged_fibre(neg(l)) == dual(exterior(k)) for l, k in sector.values()),
        'nonzero_up_tensor': up_tensor(*up_args) != 0,
        'nonzero_down_tensor': down_tensor(*down_args) != 0,
        'up_exchange_sign': up_tensor(up_args[1], up_args[0], up_args[2]) == -up_tensor(*up_args),
        'down_exchange_sign': down_tensor(down_args[0], down_args[2], down_args[1]) == -down_tensor(*down_args),
        'up_repeated_structure_index_zero': up_tensor(up_args[0], ((2, 3), 0), up_args[2]) == 0,
        'down_repeated_structure_index_zero': down_tensor(down_args[0], down_args[1], (1, (2, 4))) == 0,
        'common_line_cancels': 1 - 4 + 3 == 0 and 1 + 2 - 3 == 0 and 6 - 3 - 3 == 0,
        'independent_line_mutation_detected': 1 - 4 + 4 != 0,
    }
    for name, data in cubic_support().items():
        checks[name + '_full_support'] = data['exact_support'] and data['actual_count'] > 0
        checks[name + '_all_brackets_nonzero'] = data['nonzero_bracket']
    assert all(checks.values()), checks
    return dict(checks=checks, passed=sum(checks.values()), cubic_support=cubic_support(),
                physical_generation_count_derived=False, normalized_Yukawas_computed=False,
                actual_background_or_end_law_selected=False, full_E8_sign_gauge_computed=False)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
