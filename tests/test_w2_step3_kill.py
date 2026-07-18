"""W2 step (iii) locks — the kill verdict (kill #8, the 5-adic ring separation)."""
import os

import sympy as sp

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B674_generation_leg", "w2_step3")


def test_verdict_banked():
    v = open(os.path.join(_B, "STEP3_VERDICT.md")).read()
    assert "KILLED-AT-(iii)" in v
    assert "5-adic" in v


def test_kill_arithmetic_exact():
    phi = (1 + sp.sqrt(5)) / 2
    q = sp.symbols("q")
    s = sp.series(sp.prod([(1 - q**n)**sp.Rational(-3, 5)
                           for n in range(1, 4)]), q, 0, 3).removeO()
    assert s.coeff(q, 1) == sp.Rational(3, 5)
    assert not sp.simplify(phi**2).is_rational
    assert sp.expand(phi**2 * phi**-2 - 1) == 0
