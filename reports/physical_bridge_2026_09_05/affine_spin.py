"""R92 exact supplied affine fixtures; no manifold, spin selection or physics claim."""
import itertools
import json
import sys
from dataclasses import dataclass


def add(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def mv(a, x):
    return tuple(sum(c * d for c, d in zip(row, x)) % 2 for row in a)


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(a))) % 2
                       for j in range(len(a))) for i in range(len(a)))


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def points(n):
    return tuple(itertools.product((0, 1), repeat=n))


@dataclass(frozen=True)
class Affine:
    a: tuple
    b: tuple
    reverse: int = 0

    def __call__(self, x):
        return add(mv(self.a, x), self.b)


def compose(g, h):
    """Left map g after h, including the separate orientation tag."""
    return Affine(mm(g.a, h.a), add(g.b, mv(g.a, h.b)), g.reverse ^ h.reverse)


def closure(generators):
    n = len(generators[0].b)
    unit = Affine(identity(n), (0,) * n)
    found, queue = {unit}, [unit]
    for h in queue:
        for g in generators:
            gh = compose(g, h)
            if gh not in found:
                found.add(gh)
                queue.append(gh)
    return found


def span(vectors):
    vectors = tuple(vectors)
    out = {(0,) * len(vectors[0])}
    for v in vectors:
        out |= {add(x, v) for x in tuple(out)}
    return out


def fixed_equation(g):
    """Solve (I+A)x=b over F2 by elimination, not point-action enumeration."""
    n = len(g.b)
    rows = [[g.a[i][j] ^ int(i == j) for j in range(n)] + [g.b[i]]
            for i in range(n)]
    pivots, k = [], 0
    for col in range(n):
        pivot = next((j for j in range(k, n) if rows[j][col]), None)
        if pivot is None:
            continue
        rows[k], rows[pivot] = rows[pivot], rows[k]
        for j in range(n):
            if j != k and rows[j][col]:
                rows[j] = [a ^ b for a, b in zip(rows[j], rows[k])]
        pivots.append(col)
        k += 1
    if any(not any(row[:n]) and row[n] for row in rows):
        return set()
    free = [i for i in range(n) if i not in pivots]
    out = set()
    for values in points(len(free)):
        x = [0] * n
        for col, value in zip(free, values):
            x[col] = value
        for j, col in enumerate(pivots):
            x[col] = rows[j][n] ^ (sum(rows[j][i] * x[i] for i in free) % 2)
        out.add(tuple(x))
    return out


def rebase(g, u):
    return Affine(g.a, add(g.b, add(mv(g.a, u), u)), g.reverse)


def fixtures():
    i = identity(3)
    p = Affine(((0, 0, 1), (1, 0, 0), (0, 1, 0)), (0, 0, 0))
    q = Affine(((1, 1, 1), (0, 0, 1), (0, 1, 0)), (1, 0, 0))
    r = Affine(i, (1, 1, 1), 1)
    t1, t2 = Affine(i, (1, 0, 0)), Affine(i, (0, 1, 0))
    swap12 = Affine(((0, 1, 0), (1, 0, 0), (0, 0, 1)), (0, 0, 0))
    return {
        'tetrahedral': (p, q, r),
        'translation_swap': (t1, t2, Affine(i, (0, 0, 1), 1)),
        'translation_fix': (t1, t2, Affine(i, (1, 0, 0), 1)),
        'nontrivial_subgroup_orbit': (t1, t2, swap12, Affine(i, (0, 0, 1), 1)),
    }


def orbit_data(group):
    preserving = {g.b for g in group if not g.reverse}
    reversing = {g.b for g in group if g.reverse}
    zero = (0,) * len(next(iter(group)).b)
    k = span(preserving)
    first = min(reversing)
    shortcut = {add(first, x) for x in k}
    return dict(preserving=preserving, reversing=reversing, additive_span=k,
                true_fix=zero in reversing, shortcut_fix=zero in shortcut)


def imul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
                 for i in range(2))


def evaluate():
    checks, rows = {}, {}
    v = points(3)
    unit = Affine(identity(3), (0, 0, 0))
    groups = {name: closure(gens) for name, gens in fixtures().items()}
    for name, group in groups.items():
        data = orbit_data(group)
        checks[name + '_bijections'] = all(set(g(x) for x in v) == set(v) for g in group)
        checks[name + '_closed'] = all(compose(g, h) in group for g in group for h in group)
        checks[name + '_inverses'] = all(any(compose(g, h) == unit == compose(h, g)
                                           for h in group) for g in group)
        checks[name + '_composition_on_all_points'] = all(
            compose(g, h)(x) == g(h(x)) for g in group for h in group for x in v)
        checks[name + '_fixed_equation'] = all(
            fixed_equation(g) == {x for x in v if g(x) == x} for g in group)
        checks[name + '_rebase_all_points'] = all(
            rebase(g, u)(x) == add(g(add(x, u)), u)
            for g in group for u in v for x in v)
        rows[name] = dict(group_order=len(group), preserving_elements=sum(not g.reverse for g in group),
                          preserving_orbit=sorted(data['preserving']),
                          reversing_orbit=sorted(data['reversing']),
                          additive_span=sorted(data['additive_span']),
                          true_fix=data['true_fix'], shortcut_fix=data['shortcut_fix'])
    tetra = groups['tetrahedral']; td = orbit_data(tetra)
    s = {(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)}
    checks['tetrahedral_order24_preserving12'] = len(tetra) == 24 and sum(not g.reverse for g in tetra) == 12
    checks['tetrahedral_actual_orbit_is_tetrahedron'] = td['preserving'] == s
    checks['tetrahedral_orbit_not_additive'] = (1, 1, 0) not in td['preserving'] and (1, 1, 0) in td['additive_span']
    checks['tetrahedral_span_all_eight'] = td['additive_span'] == set(v)
    checks['tetrahedral_false_fix_reproduced'] = not td['true_fix'] and td['shortcut_fix']
    p, q, r = fixtures()['tetrahedral']
    checks['untwisted_product_rejected'] = compose(p, q).b == (0, 1, 0) != add(p.b, q.b)
    checks['reverser_commutes'] = compose(r, p) == compose(p, r) and compose(r, q) == compose(q, r)
    checks['tetrahedral_no_reversing_fixed_point'] = all(not fixed_equation(g) for g in tetra if g.reverse)
    checks['tetrahedral_false_fix_at_all_origins'] = all(
        not orbit_data({rebase(g, u) for g in tetra})['true_fix'] and
        orbit_data({rebase(g, u) for g in tetra})['shortcut_fix'] for u in v)
    for name, expected in [('translation_swap', False), ('translation_fix', True),
                           ('nontrivial_subgroup_orbit', False)]:
        data = orbit_data(groups[name])
        checks[name + '_correct_coset'] = data['true_fix'] == data['shortcut_fix'] == expected
        checks[name + '_orbit_equals_subgroup'] = data['preserving'] == data['additive_span']
    checks['nontrivial_linear_action_not_a_general_kill'] = any(
        g.a != identity(3) for g in groups['nontrivial_subgroup_orbit'] if not g.reverse)
    bounded = {unit, fixtures()['translation_fix'][-1]}
    checks['bounded_sample_false_swap'] = not orbit_data(bounded)['shortcut_fix'] and orbit_data(groups['translation_fix'])['true_fix']
    plus, minus = ((1, 0), (0, 1)), ((-1, 0), (0, -1))
    z2, z3 = ((0, -1), (1, 0)), ((0, -1), (1, -1))
    neg_z2 = tuple(tuple(-a for a in row) for row in z2)
    checks['PSL_order_two_nontrivial'] = z2 not in (plus, minus) and imul(z2, z2) == minus
    checks['both_order_two_lifts_have_order_four'] = all(
        imul(a, a) == minus and imul(imul(a, a), imul(a, a)) == plus for a in (z2, neg_z2))
    checks['no_section_on_order_two_subgroup'] = not any(imul(a, a) == plus for a in (z2, neg_z2))
    checks['order_three_has_homomorphic_lift'] = z3 not in (plus, minus) and imul(z3, z3) not in (plus, minus) and imul(imul(z3, z3), z3) == plus
    return dict(checks=checks, fixtures=rows, actual_manifold_table_recomputed=False,
                physical_chirality_derived=False, generated_spin_selection_derived=False,
                physical_goal_achieved=False, non_author_acceptance=False)


if __name__ == '__main__':
    result = evaluate()
    for name, passed in result['checks'].items():
        print(json.dumps(dict(check=name, passed=bool(passed)), sort_keys=True))
    failed = [name for name, passed in result['checks'].items() if not passed]
    total = len(result['checks'])
    result.pop('checks')
    print(json.dumps(dict(result, total=total, failed=failed), sort_keys=True))
    sys.exit(bool(failed))
