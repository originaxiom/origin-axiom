"""B509 locks — the square-time elliptic curve."""
import sympy as sp


def test_elimination():
    s, c = sp.symbols('s c')
    D = sp.discriminant(s**2 + s*(1 - c**2) + (c**2 - 1), s)
    assert sp.expand(D - (c**2 - 1)*(c**2 - 5)) == 0


def test_curve_torsion_by_hand():
    # (0,1) doubles to (1,0) on Y^2 = X^3 - 2X + 1: order 4
    lam = sp.Rational(-2, 2)          # (3*0^2-2)/(2*1)
    x3 = lam**2 - 0 - 0
    y3 = lam*(0 - x3) - 1
    assert (x3, y3) == (1, 0)
    assert 1**3 - 2*1 + 1 == 0        # (1,0) on the curve, 2-torsion
