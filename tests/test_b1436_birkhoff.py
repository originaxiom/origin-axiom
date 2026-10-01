"""B1436 lock -- the first Birkhoff coefficient of the monodromy trace map is 16 sqrt(-3)/63.

Live: the coefficient is recomputed in two charts in exact arithmetic, with the controls and the bite.
"""
import importlib.util
import json
import pathlib
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1436_the_first_birkhoff_coefficient" / "verification"


def _mod():
    spec = importlib.util.spec_from_file_location("b1436_birkhoff", V / "birkhoff.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_coefficient_in_two_charts():
    m = _mod()
    target = m.K(0, Fraction(16, 63))
    assert m.chart_XY() == target
    assert m.chart_XZ() == target


def test_the_conjugate_point_the_double_iterate_and_the_form():
    m = _mod()
    a = m.chart_XY()
    assert m.chart_XY(sign=-1) == -a
    assert m.chart_XY(iterate=2) == a + a
    assert m.chart_XY(scale=Fraction(7, 3)) == a / m.K(Fraction(7, 3))


def test_the_controls_bite():
    m = _mod()
    lin = m.first_birkhoff(m.U * m.LAM, m.V * m.LAM.inv(), m.K(1), m.LAM)
    assert lin.iszero()                       # a linear map has no cubic term
    assert m.wrong_leaf() != m.chart_XY()     # the leaf's curvature matters: dropping it changes the number
    assert m.chart_XY() != m.K(0, Fraction(16, 21))   # the test can fail


def test_the_field_arithmetic():
    m = _mod()
    A, B = m.A_, m.B_
    assert A * A == m.K(-3) and B * B == m.K(21)
    z = m.K(1, 2, 3, 4)
    assert z * z.inv() == m.K(1)
    assert m.LAM * m.LAM.inv() == m.K(1) and m.LAM + m.LAM.inv() == m.K(5)


def test_the_record():
    r = json.loads((V / "birkhoff.json").read_text())
    assert r["all_checks"] is True and r["value"] == "16*sqrt(-3)/63"
    assert abs(r["numeric"][1] - 16 * 3 ** 0.5 / 63) < 1e-12 and r["numeric"][0] == 0
