"""Locks for B437 (C2) -- the golden return + the Lucas-square law."""
import os, sys
import sympy as sp
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B437_child_abelian_book")
sys.path.insert(0, HERE)
import abelian_book as AB


def test_golden_return_exact():
    gt = AB.golden_trace()
    assert sp.simplify(gt - (3 + sp.sqrt(5)/5)) == 0     # in Q(sqrt5): the parent's field returns


def test_lucas_square_law_and_control():
    assert AB.total_torsion(5) == AB.L(5)**2 == 121      # child: 11^2 (11 = apparition prime)
    assert AB.total_torsion(7) == AB.L(7)**2 == 841      # sibling: 29^2 (generic law)
    # the classical identity behind it, for odd p
    for p in (3, 5, 7, 9, 11):
        assert abs(2 - AB.L(2*p)) == AB.L(p)**2


def test_trefoil_control_field_is_numerator_forced():
    # SAME field Q(sqrt5) for the trefoil parent: the field-return is NOT inheritance
    import sympy as sp
    t = sp.Symbol('t')
    Phi5 = sp.Poly(sum(t**k for k in range(5)), t)
    inv_den = sp.invert(sp.Poly((t-1)**2, t), Phi5)
    def gt(D):
        tau = (sp.Poly(D, t) * inv_den) % Phi5
        s4 = sp.Poly(tau.as_expr().subs(t, t**4), t) % Phi5
        h = ((tau + s4) % Phi5).all_coeffs()[::-1]; h += [sp.Integer(0)]*(4-len(h))
        return sp.simplify(h[0] + h[2]*(-1-(-1+sp.sqrt(5))/2))
    tre = gt(t**2 - t + 1)
    assert sp.simplify(tre - (1 - sp.sqrt(5)/5)) == 0      # trefoil: same field, different value
