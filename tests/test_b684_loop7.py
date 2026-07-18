"""B684 loop-7 locks — G3 dark cell + S2 det-products."""
import sympy as sp


def test_g3_dark_cell_1785():
    x = sp.symbols("x")
    r = sp.sqrt(5 + 2*sp.sqrt(3) - 2*sp.sqrt(2) - sp.sqrt(6))
    P = x**8 - 20*x**6 + 98*x**4 - 172*x**2 + 97
    assert sp.simplify(P.subs(x, r)) == 0
    assert abs(float(r) - 1.7849887247846656) < 1e-12


def test_s2_detproduct_distinct():
    L = lambda n: int(sp.lucas(n))
    tr = [int(sp.prod([2 - L(4*k) for k in range(1, e+1)])) for e in (1, 4, 5)]
    assert tr[0] == -5 and len(set(tr)) == 3         # golden conductor, distinct
