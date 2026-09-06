"""R11: exact founding-ratio action, with a distinct commuting family component.

Independent implementation of the icosian construction used by the
SM-derivation seat's B1270 (945e091d). No upstream code is imported.
All fixed dimensions below refer to ROOT SPACE, not the full Lie algebra.
"""
import argparse
from collections import Counter, deque
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import itertools as it
import json
from pathlib import Path
import subprocess
import time

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

ONE = (F(1),) + (F(0),) * 7
ZERO = (F(0),) * 8
ID5 = (1, 0, 0, 1)
R5, L5 = (1, 1, 0, 1), (1, 0, 1, 1)
ROOT = Path(__file__).resolve().parents[2]
SOURCE_REFS = {
    "87a2eb3dbc757c6b621a407e20b87e5203208ee3": [
        "frontier/B1275_e8_family_verified/verification/e8_family.py"],
    "945e091db226fc871a174e63adb907f05e461815": [
        "frontier/B1270_e6_from_the_two_faces/verification/e6_from_the_two_faces.py",
        "frontier/B1271_the_chain_all_the_way/ADDENDUM_2026-09-06_prior_art_and_the_generation_index.md"],
}


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, c):
    return tuple(c * x for x in a)


def q5mul(a, b):
    return (a[0]*b[0] + 5*a[1]*b[1], a[0]*b[1] + a[1]*b[0])


@lru_cache(maxsize=None)
def qmul(a, b):
    aa, bb = [a[i:i+2] for i in range(0, 8, 2)], [b[i:i+2] for i in range(0, 8, 2)]
    rows = (((0, 0, 1), (1, 1, -1), (2, 2, -1), (3, 3, -1)),
            ((0, 1, 1), (1, 0, 1), (2, 3, 1), (3, 2, -1)),
            ((0, 2, 1), (1, 3, -1), (2, 0, 1), (3, 1, 1)),
            ((0, 3, 1), (1, 2, 1), (2, 1, -1), (3, 0, 1)))
    out = []
    for row in rows:
        terms = [scale(q5mul(aa[i], bb[j]), s) for i, j, s in row]
        out.extend(sum(t[k] for t in terms) for k in range(2))
    return tuple(out)


def conj(a):
    return a[:2] + tuple(-x for x in a[2:])


def bil(a, b):
    return 2*sum(a[i]*b[i] + 5*a[i+1]*b[i+1]
                 + a[i]*b[i+1] + a[i+1]*b[i] for i in range(0, 8, 2))


def metric():
    return sp.diag(*([sp.Matrix([[2, 2], [2, 10]])]*4))


def matrix_of(fun):
    return sp.Matrix.hstack(*(sp.Matrix(fun(tuple(F(i == j) for i in range(8))))
                              for j in range(8)))


def operator(matrix):
    rows = [[(j, F(v)) for j, v in enumerate(row) if v]
            for row in matrix.tolist()]
    return lambda v: tuple(sum((c*v[j] for j, c in row), F(0)) for row in rows)


def reflection(a):
    if bil(a, a) != 2:
        raise ValueError("reflection requires a norm-two root")
    return sp.eye(8) - sp.Matrix(a)*(sp.Matrix(a).T*metric())


@lru_cache(maxsize=1)
def units():
    out = set()
    for i in range(4):
        for s in (-1, 1):
            out.add(tuple(F(s if j == 2*i else 0) for j in range(8)))
    for signs in it.product((-1, 1), repeat=4):
        out.add(tuple(v for s in signs for v in (F(s, 2), F(0))))
    base = ((F(1, 4), F(1, 4)), (F(1, 2), F(0)),
            (F(-1, 4), F(1, 4)), (F(0), F(0)))
    for perm in it.permutations(range(4)):
        if sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4)) % 2:
            continue
        for signs in it.product((-1, 1), repeat=3):
            coords = [None]*4
            for k in range(4):
                coords[perm[k]] = scale(base[k], signs[k] if k < 3 else 1)
            out.add(tuple(v for pair in coords for v in pair))
    return tuple(sorted(out))


def roots():
    invphi = (F(-1, 2), F(1, 2))
    scaled = [tuple(v for j in range(0, 8, 2) for v in q5mul(invphi, u[j:j+2]))
              for u in units()]
    return tuple(sorted(set(units()) | set(scaled)))


def integerize(coords, denominator=None):
    den = denominator or sp.ilcm(*(v.q for v in coords))
    scaled = coords*den
    if any(v.q != 1 for v in scaled):
        raise ValueError("non-integral scaled coordinates; truncation forbidden")
    return scaled, int(den)


def lattice_check(rr):
    if len(rr) != 240 or len(set(rr)) != 240 or any(bil(r, r) != 2 for r in rr):
        raise ValueError("240 distinct norm-two roots required")
    rs = set(rr)
    pairs = Counter()
    for a in rr:
        for b in rr:
            z = bil(a, b)
            if z.denominator != 1 or add(b, scale(a, -z)) not in rs:
                raise ValueError("integral root reflections do not close")
            pairs[int(z)] += 1
    coords = sp.Matrix(rr)
    ints, den = integerize(coords)
    basis = hermite_normal_form(ints.T)/den
    gram = basis.T*metric()*basis
    assert basis.shape == (8, 8) and gram.det() == 1
    assert all(v.q == 1 for v in gram) and all(gram[i, i] % 2 == 0 for i in range(8))
    try:
        integerize(coords, 2)
    except ValueError:
        rejected = True
    else:
        rejected = False
    return {"denominator": den, "gram_determinant": int(gram.det()),
            "basis_columns": basis.tolist(), "gram": gram.tolist(),
            "root_pairing_census": dict(pairs), "scale_two_rejected": rejected}


def mul5(a, b):
    x, y, z, t = a
    p, q, r, s = b
    return ((x*p+y*r) % 5, (x*q+y*s) % 5, (z*p+t*r) % 5, (z*q+t*s) % 5)


def group_data():
    uu = units()
    ui = {u: i for i, u in enumerate(uu)}
    table = tuple(tuple(ui[qmul(a, b)] for b in uu) for a in uu)
    assert len(table) == 120
    assert all(qmul(u, conj(u)) == ONE for u in uu)
    identity = ui[ONE]
    orders = []
    for j in range(120):
        x = identity
        for n in range(1, 121):
            x = table[x][j]
            if x == identity:
                orders.append(n)
                break
        else:
            raise AssertionError("unit order exceeds finite group bound")
    return table, orders, identity


def marked_map(table, identity, r, l):
    mapping, queue = {ID5: identity}, deque([ID5])
    while queue:
        a = queue.popleft()
        for b, j in ((R5, r), (L5, l)):
            ab, image = mul5(a, b), table[mapping[a]][j]
            if ab in mapping:
                if mapping[ab] != image:
                    return None
            else:
                mapping[ab] = image
                queue.append(ab)
    return mapping if len(mapping) == len(set(mapping.values())) == 120 else None


def founding_map(table, orders, identity):
    candidates = [j for j, n in enumerate(orders) if n == 5]
    witness = None
    for r, l in it.product(candidates, repeat=2):
        witness = marked_map(table, identity, r, l)
        if witness is not None:
            break
    assert witness is not None
    assert marked_map(table, identity, candidates[0], candidates[0]) is None
    for a, b in it.product(witness, repeat=2):
        assert witness[mul5(a, b)] == table[witness[a]][witness[b]]
    g5 = tuple(-x % 5 for x in mul5(R5, (1, 0, 4, 1)))
    assert g5 != ID5 and mul5(mul5(g5, g5), g5) == ID5
    return units()[witness[g5]], {
        "generator_images": [units()[r], units()[l]], "g5": g5,
        "g_unit_index": witness[g5], "all_product_checks": 14400,
        "invalid_equal_generator_assignment_rejected": True,
        "map": [[a, witness[a]] for a in sorted(witness)]}


def positive(v):
    return next(x for x in v if x) > 0


def simples(perp):
    pos = {r for r in perp if positive(r)}
    return sorted(r for r in pos if not any(add(r, scale(s, -1)) in pos for s in pos))


def weyl_word(matrix, simple, perp):
    """Right descent to the identity, then independently multiply the reversed word."""
    current, word = matrix, []
    inversions = sum(not positive(operator(current)(r)) for r in perp if positive(r))
    while True:
        fn = operator(current)
        candidates = [i for i, a in enumerate(simple) if not positive(fn(a))]
        if not candidates:
            break
        i = candidates[0]
        current = current*reflection(simple[i])
        word.append(i)
        new = sum(not positive(operator(current)(r)) for r in perp if positive(r))
        assert new == inversions - 1 and len(word) <= 36
        inversions = new
    # A remaining diagram automorphism would fail this, not be called a Weyl word.
    assert current == sp.eye(8)
    rebuilt = sp.eye(8)
    for i in reversed(word):
        rebuilt = rebuilt*reflection(simple[i])
    assert rebuilt == matrix
    return list(reversed(word))


def family_action_passes(matrix, g, rr):
    fn = operator(matrix)
    perp = [r for r in rr if bil(r, ONE) == bil(r, g) == 0]
    return (matrix**3 == sp.eye(8) and matrix != sp.eye(8)
            and fn(ONE) == g and fn(g) == qmul(g, g)
            and all(fn(r) == r for r in perp)
            and {fn(r) for r in rr} == set(rr))


def cycle_lengths(permutation):
    seen, lengths = set(), []
    for v in permutation:
        if v in seen:
            continue
        x, cycle = v, []
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = permutation[x]
        assert x == v
        lengths.append(len(cycle))
    return dict(Counter(lengths))


def action_row(g, rr, detailed=False):
    eye, B = sp.eye(8), metric()
    L = matrix_of(lambda v: qmul(g, v))
    W = reflection(ONE)*reflection(g)
    U = L*W**2
    A = sp.Matrix.hstack(sp.Matrix(ONE), sp.Matrix(g))
    PA = A*(A.T*B*A).inv()*A.T*B
    assert W == eye+(L-eye)*PA
    assert L*W == W*L and L == U*W
    assert all(M**3 == eye and M.T*B*M == B for M in (L, W, U))
    assert A.T*B*A == sp.Matrix([[2, -1], [-1, 2]])
    assert add(add(qmul(g, g), g), ONE) == ZERO
    functions = {name: operator(M) for name, M in (("L", L), ("W", W), ("U", U))}
    assert all({fn(r) for r in rr} == set(rr) for fn in functions.values())
    perp = [r for r in rr if bil(r, ONE) == bil(r, g) == 0]
    assert len(perp) == 72
    simple = simples(perp)
    C = sp.Matrix([[bil(a, b) for b in simple] for a in simple])
    assert C.shape == (6, 6) and C.det() == 3
    assert sorted(sum(x == -1 for x in C.row(i)) for i in range(6)) == [1, 1, 1, 2, 2, 3]
    S = sp.Matrix.hstack(*(sp.Matrix(r) for r in simple))
    left_inverse = (S.T*B*S).inv()*S.T*B
    root_coords = [left_inverse*sp.Matrix(r) for r in perp]
    assert all(all(x.q == 1 for x in c) and S*c == sp.Matrix(r)
               for c, r in zip(root_coords, perp))
    word = weyl_word(U, simple, perp)
    cls = lambda r: (bil(r, ONE), bil(r, g))
    byclass = {}
    for r in rr:
        byclass.setdefault(cls(r), []).append(r)
    keys = sorted(k for k, members in byclass.items() if len(members) == 27)
    assert len(keys) == 6
    class_perms = {}
    for name, fn in functions.items():
        perm = {}
        for k in keys:
            images = {cls(fn(r)) for r in byclass[k]}
            assert len(images) == 1
            perm[k] = images.pop()
        class_perms[name] = perm
    assert class_perms["L"] == class_perms["W"]
    assert all(k == v for k, v in class_perms["U"].items())
    assert cycle_lengths(class_perms["W"]) == {3: 2}
    x = sp.Symbol("x")
    char = {name: sp.Poly(M.charpoly(x).as_expr(), x).all_coeffs()
            for name, M in (("L", L), ("W", W), ("U", U))}
    assert sp.Poly.from_list(char["L"], x).as_expr() == sp.expand((x*x+x+1)**4)
    assert sp.Poly.from_list(char["W"], x).as_expr() == sp.expand((x-1)**6*(x*x+x+1))
    assert sp.Poly.from_list(char["U"], x).as_expr() == sp.expand((x-1)**2*(x*x+x+1)**3)
    flags = {name: family_action_passes(M, g, rr) for name, M in (("L", L), ("W", W))}
    assert flags == {"L": False, "W": True}
    aroots = [ONE, g, qmul(g, g)]
    aroots += [scale(a, -1) for a in aroots]
    assert all(add(a, b) not in set(rr) for a in aroots for b in perp)
    row = {"g": g, "cartan": C.tolist(), "simple_roots": simple,
           "E6_reflection_word_for_U": word, "charpoly_coefficients": char,
           "root_space_fixed_dimensions": {name: 8-(M-eye).rank()
                for name, M in (("L", L), ("W", W), ("U", U))},
           "E6_fixed_roots": {name: sum(fn(r) == r for r in perp)
                               for name, fn in functions.items()},
           "E6_root_cycles": {name: cycle_lengths({r: fn(r) for r in perp})
                              for name, fn in functions.items()},
           "family_action_predicate": flags, "class_cycles": {3: 2},
           "mixed_E6_A2_root_sum_checks": len(aroots)*len(perp)}
    if detailed:
        row.update({"matrices": {name: M.tolist() for name, M in (("L", L), ("W", W), ("U", U))},
                    "class_permutations": {name: [[k, v] for k, v in perm.items()]
                        for name, perm in class_perms.items()},
                    "E6_roots": perp, "root_classes": [[k, members] for k, members in byclass.items()]})
    return row, (L, W, U)


def source_receipts():
    out = []
    for ref, paths in SOURCE_REFS.items():
        full = subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, text=True).strip()
        for path in paths:
            blob = subprocess.check_output(["git", "show", f"{full}:{path}"], cwd=ROOT)
            out.append({"commit": full, "path": path, "sha256": hashlib.sha256(blob).hexdigest()})
    return out


def run():
    started = time.monotonic()
    rr, uu = roots(), units()
    lattice = lattice_check(rr)
    assert lattice["scale_two_rejected"]
    table, orders, identity = group_data()
    assert Counter(orders) == {1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24}
    g, iso = founding_map(table, orders, identity)
    gs = [u for u, n in zip(uu, orders) if n == 3]
    rows, operators = [], {}
    for gg in gs:
        row, matrices = action_row(gg, rr, detailed=(gg == g))
        rows.append(row)
        operators[gg] = matrices
    planes = {tuple(sorted((gg, qmul(gg, gg)))) for gg in gs}
    assert len(planes) == 10
    for gg in gs:
        assert operators[qmul(gg, gg)][1] == operators[gg][1]**2
    covariant = 0
    for a in uu:
        Q = matrix_of(lambda v: qmul(qmul(a, v), conj(a)))
        Qi = metric().inv()*Q.T*metric()
        assert Q*Qi == sp.eye(8)
        for gg in gs:
            image = qmul(qmul(a, gg), conj(a))
            assert Q*operators[gg][1]*Qi == operators[image][1]
            covariant += 1
    i4 = next(u for u, n in zip(uu, orders) if n == 4)
    control_count = sum(bil(r, ONE) == bil(r, i4) == 0 for r in rr)
    assert control_count != 72
    n1 = sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    n2 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    n = n1*n2
    assert n**3 == sp.eye(3) and n.T*n == sp.eye(3) and n.det() == 1
    assert (n-sp.eye(3)).rank() == 2
    return {"scope": "exact root-space action; not a physical family count or a TOE",
            "source_receipts": source_receipts(), "lattice": lattice,
            "unit_order_census": dict(Counter(orders)), "marked_isomorphism": iso,
            "founding_g": g, "all_twenty_actions": rows,
            "unoriented_Eisenstein_planes": len(planes),
            "unit_conjugation_covariance_checks": covariant,
            "inverse_orientation_checks": len(gs),
            "order_four_complement_control": control_count,
            "SU3_order_three_representative": n.tolist(),
            "runtime_seconds": time.monotonic()-started}


def json_default(value):
    if isinstance(value, (F, sp.Rational)):
        return int(value) if value.denominator == 1 else str(value)
    raise TypeError(f"not serializable: {type(value)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = run()
    blob = json.dumps(result, default=json_default, indent=2, sort_keys=True)+"\n"
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(blob)
    print(json.dumps({"actions": len(result["all_twenty_actions"]),
                      "lattice_det": result["lattice"]["gram_determinant"],
                      "covariance_checks": result["unit_conjugation_covariance_checks"],
                      "runtime_seconds": result["runtime_seconds"]}))


if __name__ == "__main__":
    main()
