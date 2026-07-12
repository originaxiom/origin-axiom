"""Locks: the charge tower's arithmetic (closed form, resultant, period-3)."""
import sympy as sp

x, mu = sp.symbols('x mu')
F = sp.Matrix([[1, 1], [1, 0]])


def _T(M):
    return sp.Matrix(sp.BlockMatrix([[M, M], [M*M, M]]))


def test_closed_form_e_n_is_charpoly_at_1():
    M = F
    for _ in range(4):
        assert (sp.eye(M.shape[0]) - M).det() == M.charpoly(x).as_expr().subs(x, 1)
        M = _T(M)


def test_charpoly_resultant_recursion():
    p0 = F.charpoly(x).as_expr()
    R = sp.expand(sp.resultant(sp.Poly(p0.subs(x, mu), mu),
                               sp.Poly(x**2 - 2*mu*x + mu**2 - mu**3, mu)))
    p1 = _T(F).charpoly(x).as_expr()
    assert sp.factor(R) == sp.factor(p1) or sp.factor(-R) == sp.factor(p1)


def test_charge_from_fixed_cubic_resultant():
    g = x**3 - x**2 + 2*x - 1
    M = F
    for _ in range(3):
        cp = M.charpoly(x).as_expr()
        e_next = (sp.eye(_T(M).shape[0]) - _T(M)).det()
        R = sp.resultant(sp.Poly(cp, x), sp.Poly(g, x))
        assert abs(R) == abs(e_next)
        M = _T(M)


def test_11_divides_e_n_period_3():
    """11 | e_n at n = 1, 4 (verified rungs); period 3."""
    M = F
    zeros = []
    for n in range(5):
        if (sp.eye(M.shape[0]) - M).det() % 11 == 0:
            zeros.append(n)
        M = _T(M)
    assert 1 in zeros and 4 in zeros
    assert all((z - 1) % 3 == 0 for z in zeros)
