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


def test_tone_character_identification():
    """The pentagon voice IS the golden character table (exact, with
    multiplicities)."""
    import sympy as sp
    from collections import Counter
    phi = (1 + sp.sqrt(5)) / 2
    cls = [(1, 2), (1, -2), (30, 0), (20, -1), (20, 1),
           (12, 1 / phi), (12, -phi), (12, -1 / phi), (12, phi)]
    tone_mult = Counter()
    for sz, ch in cls:
        tone_mult[sp.nsimplify(sp.Abs(ch) / 2)] += sz * 3
    banked = {0: 90, sp.nsimplify(1 / (2 * phi)): 72,
              sp.Rational(1, 2): 120, sp.nsimplify(phi / 2): 72, 1: 6}
    assert len(tone_mult) == 5
    for k, v in banked.items():
        assert tone_mult[k] == v
    assert sp.simplify(sum(sz * ch**2 for sz, ch in cls) / 120) == 1


def test_refutations_exact():
    import sympy as sp
    odd = {4, 8}
    for m in (1, 4, 5):
        assert ((m in odd) == ((12 - m) in odd))   # SAME parity: refutes
    As = sp.Matrix([[5, 2], [2, 1]])
    assert (As + sp.eye(2)).det() == 8             # silver: 8, not 7


def test_q_area_universal_factor_2():
    """Q-AREA verdict lock: the silver chain defect = 2*conj(Y), NOT
    4*conj(Y) (the area law is refuted; the factor 2 is universal).
    Fraction-level: binds silver_Y_L.json to q_area_output.txt, and the
    defect is s-free (lives in Q(i) — the subfield law)."""
    import json
    import os
    from fractions import Fraction as Fr
    p = os.path.join(os.path.dirname(__file__), "..", "frontier",
                     "B649_silver_holonomy", "silver_Y_L.json")
    dY = json.load(open(p))
    out = {  # (re0, im0) of the defect, from q_area_output.txt
        "023": (Fr(-1, 401287500), Fr(523, 134832600000)),
        "134": (Fr("-182020734169560425939/"
                   "43356451579910974689993768960000000"),
                Fr("233965040169927275431/"
                   "130069354739732924069981306880000000")),
    }
    for key, (dre, dim_) in out.items():
        Y = [Fr(x) for x in dY[key]]
        # defect = 2*conj(Y): re = 2*Y_re, im = -2*Y_im, coordinatewise
        assert dre == 2 * Y[0] and dim_ == -2 * Y[4]
        assert dre != 4 * Y[0]                     # the area law fails
        assert Y[1] == Y[2] == Y[3] == 0           # s-free: Q(i)
        assert Y[5] == Y[6] == Y[7] == 0
