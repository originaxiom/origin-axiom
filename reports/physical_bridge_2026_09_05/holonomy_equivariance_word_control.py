"""R20 post-failure control: exact word maps plus a certified upper count."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sys
import time

import sympy as sp

SPEC = importlib.util.spec_from_file_location('r20_original_equivariance', Path(__file__).with_name('holonomy_equivariance.py'))
he = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(he)

R = ('b', 'bA')
S = ('a', 'aB')
R_INV = ('Ba', 'a')
S_INV = ('a', 'Ba')
ID = ('a', 'b')


def compose_words(f, g):
    return tuple(he.substitute(w, f) for w in g)


def preserves_relator(images):
    rel = he.cyclic_reduce(he.hs.RELATOR)
    v = he.cyclic_reduce(he.substitute(rel, images))
    return len(v) == len(rel) and any(v in w+w for w in (rel, he.inverse_word(rel)))


def word_actions():
    checks = []
    for label, f, inv in (('r', R, R_INV), ('s', S, S_INV)):
        good = compose_words(f, inv) == compose_words(inv, f) == ID
        rel = preserves_relator(f) and preserves_relator(inv)
        assert good and rel
        checks.append(dict(label=label, images=list(f), inverse=list(inv),
                           two_sided_free_inverse=good, relator_preserved=rel))
    rows = []
    power = ID
    for k in range(6):
        for e in (0, 1):
            images = compose_words(power, S if e else ID)
            A = sp.Matrix([[w.count(c)-w.count(c.upper()) for w in images] for c in 'ab'])
            assert preserves_relator(images)
            rows.append(dict(k=k, e=e, images=list(images), h1_matrix=A.tolist(), relator_preserved=True))
        power = compose_words(R, power)
    matrices = [sp.Matrix(r['h1_matrix']) for r in rows]
    keys = set(map(he.key_matrix, matrices))
    assert len(keys) == 12 and all(he.key_matrix(A*B) in keys for A in matrices for B in matrices)
    return dict(generators=checks, outer_class_lower_bound=len(keys), actions=rows)


def cusp_order(s):
    identity = (tuple(range(len(s[0]))), tuple(sp.eye(2) for _ in s[0]))
    cur = identity
    for n in range(1, 49):
        cur = he.compose(s, cur)
        if cur == identity:
            return n
    raise ValueError('cusp action did not close')


def control_geometry(verified=False, bits=100):
    import snappy
    Q = snappy.Manifold('m202')
    pi = Q.fundamental_group()
    assert list(pi.generators()) == ['a', 'b'] and list(pi.relators()) == [he.hs.RELATOR]
    exact = word_actions()
    keys = {tuple(sum(r['h1_matrix'], [])) for r in exact['actions']}
    K = Q.canonical_retriangulation(verified=verified, interval_bits_precs=[bits],
                                   exact_bits_prec_and_degrees=[(bits, 10), (1000, 20)])
    canonical = [he.iso_data(s) for s in K.isomorphisms_to(K)]
    assert len(canonical) == exact['outer_class_lower_bound'] == 12
    descriptors = {(p, tuple(tuple(M) for M in m)) for p, m in canonical}
    assert len(descriptors) == 12  # cusp-action order is now faithful
    assert all(M.det() == 1 for _, ms in canonical for M in ms)
    c3 = [s for s in canonical if cusp_order(s) == 3]
    assert len(c3) == 2
    c3_rows = []
    for p, maps in c3:
        assert p == (0, 1)
        fixed = [abs(int((M-sp.eye(2)).det())) for M in maps]
        assert fixed == [3, 3]
        c3_rows.append(dict(cusp_images=list(p), cusp_maps=[M.tolist() for M in maps], fixed_points=fixed))
    per = [list(pair) for pair in pi.peripheral_curves()]
    B = [sp.Matrix([[w.count(c)-w.count(c.upper()) for w in pair] for c in 'ab']) for pair in per]
    numerical = []
    for iso in Q.symmetry_group().isometries():
        p, maps = he.iso_data(iso)
        A = he.h1_action(B, (p, maps))
        numerical.append(dict(cusp_images=list(p), cusp_maps=[M.tolist() for M in maps], h1_matrix=A.tolist()))
    assert {tuple(sum(r['h1_matrix'], [])) for r in numerical} == keys
    control = snappy.Manifold('m004').canonical_retriangulation(
        verified=verified, interval_bits_precs=[bits], exact_bits_prec_and_degrees=[(bits, 10), (1000, 20)])
    count = len(control.isomorphisms_to(control))
    assert count == 8
    return dict(verified=verified, requested_bits=bits, version=snappy.version(),
                original_isosig=Q.triangulation_isosig(), canonical_isosig=K.triangulation_isosig(),
                original_tetrahedra=Q.num_tetrahedra(), canonical_tetrahedra=K.num_tetrahedra(),
                canonical_finite_vertices=bool(K.has_finite_vertices()),
                direct_combinatorial_bridges=len(Q.isomorphisms_to(K)),
                canonical_symmetry_upper_bound=len(canonical), exact_word_actions=exact,
                lower_equals_upper=True, canonical_orientations_all_positive=True,
                canonical_c3_cusps=c3_rows, m004_symmetry_count=count,
                numerical_peripheral_control=dict(grade='numerical enumeration; exact integral descent; not separately interval-certified',
                    peripheral_columns=[M.tolist() for M in B], isometries=numerical))


@lru_cache(maxsize=1)
def algebra():
    return he.analysis_of_actions([r['h1_matrix'] for r in word_actions()['actions']])


def run(verified=False):
    start = time.monotonic()
    g = [control_geometry(verified, bits) for bits in ((100, 212) if verified else (100,))]
    assert all(v['exact_word_actions'] == g[0]['exact_word_actions'] for v in g)
    return dict(scope='same R20 scientific target; post-failure exact word-map control',
                geometry=g, algebra=algebra(), runtime_seconds=time.monotonic()-start)


if __name__ == '__main__':
    verified = '--verified' in sys.argv
    if verified:
        import sage.all
    print(json.dumps(run(verified), default=str, indent=2, sort_keys=True), flush=True)
