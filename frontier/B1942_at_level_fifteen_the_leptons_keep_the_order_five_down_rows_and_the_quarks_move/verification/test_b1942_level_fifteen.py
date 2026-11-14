"""B1942's lock: the identity (the lepton twists at an order-15 point are those at an order-5 point) checked exactly on
the 192 points; the kept runs hold E1 to roundoff and E2 well above it at every modulus, and the control is caught."""
import re, pathlib
from fractions import Fraction as Fr
from math import gcd
HERE = pathlib.Path(__file__).resolve().parent


def test_the_identity_exactly():
    pts = [(Fr(i, 15), Fr(j, 15)) for i in range(15) for j in range(15) if 15 // gcd(gcd(i, j), 15) == 15]
    assert len(pts) == 192
    red = lambda x: x - (x.numerator // x.denominator)
    images = {}
    for a, b in pts:
        w = (a, b); v2 = (red(6 * a), red(6 * b))                       # the order-5 point 6w
        assert all(red(5 * c) == 0 for c in v2) and v2 != (0, 0)
        for q, q2 in ((-3, -3), (6, 6)):                               # the lepton twists q w and q (6w) agree mod 1
            assert (red(q * a), red(q * b)) == (red(q2 * v2[0]), red(q2 * v2[1]))
        images[v2] = images.get(v2, 0) + 1
    assert len(images) == 24 and set(images.values()) == {8}           # onto the 24 points of order 5, evenly


def test_the_kept_runs():
    t = (HERE / "level15_run.txt").read_text()
    rows = re.findall(r"E1 lepton\(15\) vs down\(5\): S ([0-9.e+-]+), S~ ([0-9.e+-]+) \| E2 down\(15\) vs down\(5\): S ([0-9.e+-]+), S~ ([0-9.e+-]+)", t)
    assert len(rows) == 3
    for e1s, e1t, e2s, e2t in rows:
        assert float(e1s) < 1e-12 and float(e1t) < 1e-12 and float(e2s) > 0.1 and float(e2t) > 0.1
    assert "CAUGHT" in (HERE / "level15_control_run.txt").read_text()
