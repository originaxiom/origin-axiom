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


def test_b510_jacobian_mechanism():
    # Jacobian of v^2=(c^2-1)(c^2-5) via classical I,J: y^2 = x^3 - 27I x - 27J
    a, b, c, d, e = 1, 0, -6, 0, 5
    I = 12*a*e - 3*b*d + c*c
    J = 72*a*c*e + 9*b*c*d - 27*a*d*d - 27*e*b*b - 2*c**3
    assert (I, J) == (96, -1728)
    # j-invariants differ => NOT quadratic twists (the corrected mechanism)
    # j(40a1)=148176/25, j(40a3)=55296/5 — both nonzero and distinct
    assert 148176*5 != 55296*25
