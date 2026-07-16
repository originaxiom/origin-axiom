"""B654 locks — the listening synthesis' exact findings."""
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B654 = os.path.join(HERE, "..", "frontier", "B654_listening_synthesis")


def test_q_period_identity():
    from math import lcm
    divs = [2, 3, 4, 5, 6, 7, 8, 10, 11, 15, 19, 20, 24, 30, 35, 40, 55]
    c = 1
    for d in divs:
        c = lcm(c, d * d)
    N0 = 2**6 * 3**3 * 5**4 * 7**2 * 11**2 * 19**2
    assert N0 == 75 * c
    assert 75 == 3 * 5**2


def test_q_field_shapes_exact():
    import warnings
    warnings.filterwarnings("ignore")
    import snappy
    import mpmath as mp
    mp.mp.dps = 60
    sh = snappy.Manifold("m136").tetrahedra_shapes(part="rect",
                                                   bits_prec=212)
    tgts = [(0.5, 0.5), (1, 1), (1, 1), (0.5, 0.5)]
    for z, (a, b) in zip(sh, tgts):
        zr = mp.mpf(str(z.real()).replace(" E", "e"))
        zi = mp.mpf(str(z.imag()).replace(" E", "e"))
        assert abs(zr - a) < 1e-45 and abs(zi - b) < 1e-45
