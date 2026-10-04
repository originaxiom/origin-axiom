"""Separately authored R92 eight-point permutations; no native import or manifold claim."""
import itertools
import json
import sys


def affine_from_vertices(images):
    origin = images[0]
    columns = [images[i] ^ origin for i in (1, 2, 3)]
    return tuple(origin ^ (columns[0] if x & 1 else 0) ^
                 (columns[1] if x & 2 else 0) ^ (columns[2] if x & 4 else 0)
                 for x in range(8))


def product(g, h):
    return tuple(g[0][h[0][x]] for x in range(8)), g[1] ^ h[1]


def group(generators):
    found = {(tuple(range(8)), 0)}
    while True:
        expanded = found | {product(g, h) for g in generators for h in found}
        if expanded == found:
            return found
        found = expanded


def additive(vectors):
    result = {0}
    for x in vectors:
        result |= {y ^ x for y in tuple(result)}
    return result


def parity(perm):
    return sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))) % 2


def evaluate():
    checks = []
    def check(value):
        checks.append(bool(value))
    p = (affine_from_vertices((0, 2, 4, 1)), 0)
    q = (affine_from_vertices((1, 0, 4, 2)), 0)
    r = (tuple(x ^ 7 for x in range(8)), 1)
    h = group((p, q)); g = group((p, q, r))
    check(len(h) == 12); check(len(g) == 24)
    preserving = {f[0][0] for f in g if not f[1]}
    reversing = {f[0][0] for f in g if f[1]}
    check(preserving == {0, 1, 2, 4}); check(reversing == {3, 5, 6, 7})
    check(additive(preserving) == set(range(8)))
    check(0 not in reversing and 0 in {7 ^ x for x in additive(preserving)})
    check(product(p, q)[0][0] == 2 and (p[0][0] ^ q[0][0]) == 1)
    check(all(parity([ (0, 1, 2, 4).index(f[0][x]) for x in (0, 1, 2, 4)]) == 0 for f in h))
    check(product(r, p) == product(p, r)); check(product(r, q) == product(q, r))
    for left in g:
        for right in g:
            pr = product(left, right)
            check(pr in g)
            check(pr[0][0] == left[0][right[0][0]])
            # Left linear part applied to right defect: A_l b_r = T_l(b_r)+b_l.
            check(pr[0][0] == left[0][0] ^ (left[0][right[0][0]] ^ left[0][0]))
    for f in g:
        for x in range(8):
            a_x = f[0][x] ^ f[0][0]
            check((f[0][x] == x) == ((x ^ a_x) == f[0][0]))
            if f[1]:
                check(f[0][x] != x)
    for u in range(8):
        orbit = {f[0][u] ^ u for f in h}
        reverse = {f[0][u] ^ u for f in g if f[1]}
        check(0 not in reverse); check(additive(orbit) == set(range(8)))
    linear_maps = {affine_from_vertices((0, a, b, c))
                   for a, b, c in itertools.product(range(8), repeat=3)}
    gl = {f for f in linear_maps if len(set(f)) == 8}
    agl = {tuple(f[x] ^ b for x in range(8)) for f in gl for b in range(8)}
    check(len(gl) == 168); check(len(agl) == 1344)
    check(all(f[0] in agl for f in g))
    t1, t2 = (tuple(x ^ 1 for x in range(8)), 0), (tuple(x ^ 2 for x in range(8)), 0)
    translate_swap = group((t1, t2, (tuple(x ^ 4 for x in range(8)), 1)))
    translate_fix = group((t1, t2, (t1[0], 1)))
    swap12 = (affine_from_vertices((0, 2, 1, 4)), 0)
    nontrivial = group((t1, t2, swap12, (tuple(x ^ 4 for x in range(8)), 1)))
    for population, fix in ((translate_swap, False), (translate_fix, True), (nontrivial, False)):
        k = {f[0][0] for f in population if not f[1]}
        rev = {f[0][0] for f in population if f[1]}
        check(k == additive(k)); check((0 in rev) == fix)
        check((0 in {min(rev) ^ x for x in additive(k)}) == fix)
    check(len(nontrivial) == 16)
    check(any(f[0][0] == 0 and f[0] != tuple(range(8)) for f in nontrivial if not f[1]))
    check(0 not in {1} and any(f[1] and f[0][0] == 0 for f in translate_fix))
    # Integer columns, independently from the native matrix product.
    def s(v): return (-v[1], v[0])
    def negative_s(v): return (v[1], -v[0])
    def t(v): return (-v[1], v[0] - v[1])
    for basis in ((1, 0), (0, 1)):
        neg = tuple(-x for x in basis)
        check(s(s(basis)) == neg); check(negative_s(negative_s(basis)) == neg)
        check(s(s(s(s(basis)))) == basis); check(t(t(t(basis))) == basis)
    return dict(total=len(checks), passed=sum(checks), failed=len(checks)-sum(checks),
                linear_maps=168, affine_maps=1344, actual_manifold_table_recomputed=False,
                physical_goal_achieved=False, non_author_acceptance=False)


if __name__ == '__main__':
    result = evaluate()
    print(json.dumps(result, sort_keys=True))
    sys.exit(bool(result['failed']))
