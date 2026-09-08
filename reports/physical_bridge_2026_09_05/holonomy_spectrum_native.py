"""R19 independent native Alexander/interval and exact-field controls.

Run with sage -python; no source-line or physical-operator certification.
"""
import json
import time

import sage.all as sa  # Activate SnapPy's certified interval mode first.
import snappy


def normalized_support(terms):
    terms = {tuple(map(int, e)): sa.QQ(c) for e, c in terms.items() if c}
    shift = tuple(min(e[i] for e in terms) for i in range(2))
    moved = {tuple(e[i]-shift[i] for i in range(2)): c for e, c in terms.items()}
    sign = 1 if moved[min(moved)] > 0 else -1
    return {e: sign*c for e, c in moved.items()}


def run():
    start = time.monotonic()
    Q = snappy.Manifold('m202')
    pi = Q.fundamental_group()
    assert list(pi.generators()) == ['a', 'b']
    assert list(pi.relators()) == ['aabbAbAABBaB']
    poly = Q.alexander_polynomial()
    terms = poly.dict()
    expected = {(2, 1): 1, (2, 0): 1, (1, 2): 1, (1, 1): 1,
                (1, 0): 1, (0, 2): 1, (0, 1): 1}
    matches = []
    for swap in (False, True):
        for sa1 in (-1, 1):
            for sa2 in (-1, 1):
                transformed = {}
                for e, c in terms.items():
                    e = tuple(e)[::-1] if swap else tuple(e)
                    transformed[(sa1*e[0], sa2*e[1])] = c
                if normalized_support(transformed) == normalized_support(expected):
                    matches.append(dict(swap=swap, generator_signs=[sa1, sa2]))
    assert matches
    intervals = []
    for bits in (100, 212):
        ok, shapes = Q.verify_hyperbolicity(bits_prec=bits)
        assert ok and all(z.imag().lower() > 0 for z in shapes)
        intervals.append(dict(bits=bits, verified=bool(ok), shapes=[str(z) for z in shapes]))
    R = sa.PolynomialRing(sa.QQ, 't')
    t = R.gen()
    K = sa.NumberField(2*t*t+3*t+2, 'z')
    z = K.gen()
    exact = []
    for label, x, y in [('trivial', K(1), K(1)), ('order_two', K(-1), K(1)),
                        ('exceptional', z, z), ('dual_exceptional', 1/z, 1/z)]:
        P = x*x*y+x*x+x*y*y+x*y+x+y*y+y
        d0 = sa.matrix(K, 5, 1, [x-1, y-1, 1, 1, 1])
        d1 = sa.matrix(K, 1, 5, [-(y-1)*P/x, (x-1)*P/x, 0, 0, 0])
        assert d1*d0 == sa.zero_matrix(K, 1, 1)
        b = [1-d0.rank(), 5-d0.rank()-d1.rank(), 1-d1.rank(), 0]
        assert b == ([0, 3, 0, 0] if label == 'order_two' else [0, 4, 1, 0])
        exact.append(dict(label=label, polynomial=str(P), ranks=[int(d0.rank()), int(d1.rank())],
                          relative_T=list(map(int, b))))
    assert z*((-sa.QQ(3)/2)-z) == 1  # conjugate roots: product one, discriminant negative
    return dict(sage_version=sa.version(), snappy_version=snappy.version(),
                native_alexander=str(poly), native_variables=list(map(str, poly.parent().gens())),
                matching_basis_changes=matches, interval_hyperbolicity=intervals,
                exact_number_field=str(K), exact_controls=exact,
                runtime_seconds=time.monotonic()-start)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True), flush=True)
