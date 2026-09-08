"""R20: source-symmetry compatibility, keeping the global parent explicit.

Run normally for numerical geometry controls; use sage -python with
--verified for certified canonical geometry. No orbifold projection.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path
import sys
import time

import sympy as sp

SPEC = importlib.util.spec_from_file_location('r20_holonomy_spectrum', Path(__file__).with_name('holonomy_spectrum.py'))
hs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hs)


def key_matrix(A):
    return tuple(map(int, A))


def matrix_order(A, limit=48):
    P = sp.eye(A.rows)
    for n in range(1, limit+1):
        P = P*A
        if P == sp.eye(A.rows):
            return n
    raise ValueError('not finite order within the declared bound')


def reduce_word(word):
    stack = []
    for c in word:
        if stack and stack[-1] == c.swapcase():
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)


def inverse_word(word):
    return ''.join(c.swapcase() for c in word[::-1])


def substitute(word, images=('B', 'aB')):
    m = dict(zip('ab', images))
    m.update({c.upper(): inverse_word(m[c]) for c in 'ab'})
    return reduce_word(''.join(m[c] for c in word))


def cyclic_reduce(word):
    w = reduce_word(word)
    while len(w) > 1 and w[0] == w[-1].swapcase():
        w = w[1:-1]
    return w


def word_map_control(images=('B', 'aB')):
    rel = cyclic_reduce(hs.RELATOR)
    image = cyclic_reduce(substitute(rel, images))
    relator_ok = len(image) == len(rel) and any(image in w+w for w in (rel, inverse_word(rel)))
    third = [substitute(substitute(substitute(c, images), images), images) for c in 'ab']
    A = sp.Matrix([[w.count(c)-w.count(c.upper()) for w in images] for c in 'ab'])
    return dict(images=list(images), relator_cyclic_image=image,
                relator_preserved=relator_ok, third_power=third, h1_matrix=A.tolist())


def iso_data(iso):
    return (tuple(map(int, iso.cusp_images())),
            tuple(sp.Matrix([[int(M[i, j]) for j in range(2)] for i in range(2)]) for M in iso.cusp_maps()))


def compose(s, t):
    """s after t; columns carry images of the source cusp basis."""
    ps, ms = s
    pt, mt = t
    return tuple(ps[pt[c]] for c in range(len(pt))), tuple(ms[pt[c]]*mt[c] for c in range(len(pt)))


def inverse_iso(s):
    p, m = s
    inv = tuple(p.index(c) for c in range(len(p)))
    return inv, tuple(m[inv[c]].inv() for c in range(len(p)))


def h1_action(peripherals, iso):
    p, m = iso
    B = [sp.Matrix(x) for x in peripherals]
    A = B[p[0]]*m[0]*B[0].inv()
    if any(v.is_Integer is not True for v in A) or abs(A.det()) != 1:
        raise ValueError('peripheral action does not descend integrally and unimodularly')
    if any(A*B[c] != B[p[c]]*m[c] for c in range(len(p))):
        raise ValueError('the second cusp does not give the same action')
    return A


def geometry(verified=False, bits=100):
    import snappy
    Q = snappy.Manifold('m202')
    pi = Q.fundamental_group()
    assert list(pi.generators()) == ['a', 'b'] and list(pi.relators()) == [hs.RELATOR]
    words = [list(pair) for pair in pi.peripheral_curves()]
    B = [sp.Matrix([[w.count(c)-w.count(c.upper()) for w in pair] for c in 'ab']) for pair in words]
    K = Q.canonical_retriangulation(verified=verified, interval_bits_precs=[bits],
                                   exact_bits_prec_and_degrees=[(bits, 10), (1000, 20)])
    bridges = Q.isomorphisms_to(K)
    if not bridges:
        raise ValueError('no explicit original-to-canonical combinatorial basis bridge')
    J = iso_data(bridges[0])
    rows = []
    for s in K.isomorphisms_to(K):
        iso = compose(inverse_iso(J), compose(iso_data(s), J))
        A = h1_action(B, iso)
        rows.append(dict(cusp_images=list(iso[0]), cusp_maps=[M.tolist() for M in iso[1]],
                         h1_matrix=A.tolist(), h1_order=matrix_order(A),
                         orientation=int(iso[1][0].det())))
    rows.sort(key=lambda r: tuple(sum(r['h1_matrix'], [])))
    actions = [sp.Matrix(r['h1_matrix']) for r in rows]
    keys = {key_matrix(A) for A in actions}
    assert len(keys) == len(rows) == 12
    assert all(key_matrix(A*C) in keys for A in actions for C in actions)
    assert all(r['orientation'] == 1 for r in rows)
    c3 = [A for A in actions if matrix_order(A) == 3]
    assert len(c3) == 2
    subgroup = {key_matrix(sp.eye(2)), *map(key_matrix, c3)}
    assert all(key_matrix(A*C*A.inv()) in subgroup for A in actions for C in c3)
    word = word_map_control()
    assert word['relator_preserved'] and word['third_power'] == ['a', 'b']
    assert key_matrix(sp.Matrix(word['h1_matrix'])) in subgroup
    control = snappy.Manifold('m004').canonical_retriangulation(
        verified=verified, interval_bits_precs=[bits], exact_bits_prec_and_degrees=[(bits, 10), (1000, 20)])
    control_order = len(control.isomorphisms_to(control))
    assert control_order == 8 and control_order % 3 != 0
    return dict(verified=verified, requested_bits=bits, version=snappy.version(),
                original_isosig=Q.triangulation_isosig(), canonical_isosig=K.triangulation_isosig(),
                canonical_finite_vertices=bool(K.has_finite_vertices()),
                basis_bridge=dict(cusp_images=list(J[0]), cusp_maps=[M.tolist() for M in J[1]]),
                peripheral_words=words, peripheral_columns=[x.tolist() for x in B],
                isometries=rows, faithful_h1_action=True, c3_normal=True,
                exact_word_control=word, m004_symmetry_count=control_order)


def mod_vector(v, period=1):
    return tuple(sp.simplify(x-period*sp.floor(x/period)) for x in v)


def invariant(A, h, period=1):
    return all((x/period).is_Integer is True for x in (A.T-sp.eye(2))*sp.Matrix(h))


def fixed_characters(A, period=1):
    A = sp.Matrix(A)
    if any(v.is_Integer is not True for v in A) or abs(A.det()) != 1:
        raise ValueError('integral unimodular action required')
    d = abs(int((A-sp.eye(2)).det()))
    if not d:
        raise ValueError('fixed locus has a continuous part; not a finite enumeration')
    p = sp.Rational(period)
    if p <= 0:
        raise ValueError('positive circle period required')
    rows = [(p*i/d, p*j/d) for i, j in itertools.product(range(d), repeat=2)]
    points = [h for h in rows if invariant(A, h, p)]
    assert len(points) == d
    return points


def character(h):
    return tuple(sp.simplify(sp.expand_complex(sp.exp(2*sp.pi*sp.I*x))) for x in h)


def parent_lifts(A, h):
    rows = []
    for i, j in itertools.product(range(3), repeat=2):
        lift = mod_vector(sp.Matrix(h)+sp.Matrix([i, j]), 3)
        defect = (A.T-sp.eye(2))*sp.Matrix(lift)
        rows.append(dict(h=list(lift), central_defect_mod_three=list(mod_vector(defect, 3)),
                         invariant_parent=invariant(A, lift, 3),
                         invariant_adjoint=invariant(A, lift, 1)))
    assert len({tuple(r['h']) for r in rows}) == 9
    return rows


def analysis_of_actions(actions):
    actions = sorted([sp.Matrix(A) for A in actions], key=key_matrix)
    C3 = next(A for A in actions if matrix_order(A) == 3)
    C6 = next(A for A in actions if matrix_order(A) == 6)
    x, y = hs.X, hs.Y
    norm = hs.identities()['polynomial']/(x*y)
    polynomial_checks = []
    for A in actions:
        images = (x**A[0, 0]*y**A[1, 0], x**A[0, 1]*y**A[1, 1])
        polynomial_checks.append(sp.cancel(norm.subs(dict(zip((x, y), images)), simultaneous=True)-norm) == 0)
    assert all(polynomial_checks)
    points = fixed_characters(C3)
    rows = []
    for h in points:
        orbit = {mod_vector(A.T*sp.Matrix(h)) for A in actions}
        stab = [A for A in actions if invariant(A, h)]
        lifts = parent_lifts(C3, h)
        rows.append(dict(h=list(h), character=list(character(h)),
                         cohomology=hs.cochains(*character(h)), orbit=[list(p) for p in sorted(orbit)],
                         stabilizer_size=len(stab), stabilizer_orders=dict(Counter(matrix_order(A) for A in stab)),
                         parent_lifts=lifts))
    p3 = [dict(h=list(h), adjoint_h=list(mod_vector(h)), invariant_parent=invariant(C3, h, 3))
          for h in fixed_characters(C3, 3)]
    old = (sp.Rational(1, 2), sp.Integer(0))
    C = hs.e6_cartan()
    u = C.inv()[:, 0]
    roots, weights = hs.weyl_orbit(C, sp.eye(6)[:, 0]), hs.weyl_orbit(C, u)
    root_phases = {sp.Rational(v[0]) % 1 for v in roots}
    fundamental_phases = {sp.Rational(v[0]) % 1 for v in weights}
    assert root_phases == {0} and fundamental_phases == {sp.Rational(1, 3)}
    return dict(c3_matrix=C3.tolist(), c6_matrix=C6.tolist(), c3_fixed=rows,
                c6_fixed=[list(h) for h in fixed_characters(C6)],
                full_group_fixed=[list(h) for h in points if all(invariant(A, h) for A in actions)],
                simply_connected_c3_fixed=p3,
                old_order_two=dict(h=list(old), c3_invariant=invariant(C3, old),
                                   orbit=[list(p) for p in sorted({mod_vector(A.T*sp.Matrix(old)) for A in actions})]),
                polynomial_invariance=polynomial_checks,
                parent=dict(u=list(u), coroot_period=sp.ilcm(*[v.q for v in u]),
                            adjoint_period=1, central_root_phases=list(root_phases),
                            central_fundamental_phases=list(fundamental_phases)),
                physical_selection=False, orbifold_projection_performed=False)


@lru_cache(maxsize=1)
def numerical_control():
    g = geometry()
    return dict(geometry=g, algebra=analysis_of_actions([r['h1_matrix'] for r in g['isometries']]))


def run(verified=False):
    start = time.monotonic()
    geometric = [geometry(verified, bits) for bits in ((100, 212) if verified else (100,))]
    sets = [{tuple(sum(r['h1_matrix'], [])) for r in g['isometries']} for g in geometric]
    assert all(s == sets[0] for s in sets)
    return dict(scope='prescribed scalar-holonomy source model; global forms explicit',
                geometry=geometric, algebra=analysis_of_actions([r['h1_matrix'] for r in geometric[0]['isometries']]),
                runtime_seconds=time.monotonic()-start)


if __name__ == '__main__':
    certified = '--verified' in sys.argv
    if certified:
        import sage.all  # Activate certified SnapPy before importing it in geometry.
    print(json.dumps(run(certified), default=str, indent=2, sort_keys=True), flush=True)
