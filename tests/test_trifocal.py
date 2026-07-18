"""Trifocal locks — the silver theorem, the convention bridge, 15A8."""
import sympy as sp


def test_silver_delta_relation_exact():
    a = sp.root(2, 4)
    Us2 = (a - 1)/(a + 1)
    assert sp.simplify(Us2 + 1/Us2 - 2*(1 + sp.sqrt(2))**2) == 0


def test_convention_bridge():
    x, u = sp.symbols("x u")
    mine = x**8 - 12*x**6 + 6*x**4 - 12*x**2 + 1
    assert sp.expand(mine.subs(x, sp.sqrt(2)*u)
                     - (16*u**8 - 96*u**6 + 24*u**4 - 24*u**2 + 1)) == 0


def test_15a8_j_match():
    m = sp.symbols("m")
    b2, b4, b6 = 5, 1, 1
    b8 = (b2*b6 - b4**2) // 4
    Delta = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
    assert Delta == -15
    assert sp.Rational((b2**2 - 24*b4)**3, Delta) == sp.Rational(-1, 15)
    q4 = sp.expand((m**2 - 3*m + 1)*(m**2 + m + 1))
    a_, b_, c_, d_, e_ = [q4.coeff(m, k) for k in (4, 3, 2, 1, 0)]
    I = 12*a_*e_ - 3*b_*d_ + c_**2
    J = (72*a_*c_*e_ - 27*a_*d_**2 - 27*b_**2*e_ + 9*b_*c_*d_
         - 2*c_**3)
    assert sp.Rational(1728*4*I**3, 4*I**3 - J**2) == sp.Rational(-1, 15)


def test_branch_locus_bifocal():
    m = sp.symbols("m")
    phi = (1 + sp.sqrt(5))/2
    assert sp.expand((m**2 - 3*m + 1).subs(m, phi**2)) == 0
    om = sp.Rational(-1, 2) + sp.sqrt(3)*sp.I/2
    assert sp.simplify((m**2 + m + 1).subs(m, om)) == 0
