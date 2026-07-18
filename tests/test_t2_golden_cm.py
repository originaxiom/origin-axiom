"""T2 golden CM confirmation — t_golden algebraic degree 12, norm 5^30."""
import sympy as sp


def test_golden_t_minpoly_via_modular_equation():
    t, J = sp.symbols("t J")
    jmin = J**2 - 2835810000*J + 6549518250000        # banked H_-48 (T1)
    rel = (t**2 + 250*t + 3125)**3 - J*t**5            # j = (t^2+250t+3125)^3/t^5
    res = sp.resultant(rel, jmin, J)
    P = sp.Poly(res, t)
    assert P.degree() == 12
    assert P.is_irreducible
    assert P.all_coeffs()[-1] == 5**30                # pure hearing-prime norm
