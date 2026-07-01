"""B326 — congruence-torsion result (Chat-2 handoff, verified). sympy-only; no SnapPy needed."""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

t = sp.symbols('t')
Delta = t**2 - 3*t + 1


def test_two_arithmetic_ends_in_one_polynomial():
    # sqrt(5) end = discriminant; sqrt(-3) end = reduction mod 4 = Phi_3.
    assert sp.discriminant(Delta, t) == 5
    assert [int(c) % 4 for c in sp.Poly(Delta, t).all_coeffs()] == [1, 1, 1]


def test_torsion_is_Z4_squared_and_order_16():
    w = sp.exp(2 * sp.pi * sp.I / 3)
    order = sp.nsimplify(sp.simplify(Delta.subs(t, w) * Delta.subs(t, w**2)))
    assert order == 16

    def vec(poly):
        c = sp.Poly(sp.rem(poly, Delta, t), t).all_coeffs()
        c = [0] * (2 - len(c)) + list(c)
        return sp.Matrix([c[1], c[0]])

    sub = sp.Matrix.hstack(vec(t**3 - 1), vec(t * (t**3 - 1)))
    assert smith_normal_form(sub.T) == sp.diag(4, 4)          # (Z/4)^2


def test_deck_z3_acts_irreducibly_with_Phi3():
    Comp = sp.Matrix([[0, -1], [1, 3]])                       # mult-by-t on Z[t]/(Delta)
    char_mod4 = [int(c) % 4 for c in sp.Poly(Comp.charpoly(t).as_expr(), t).all_coeffs()]
    assert char_mod4 == [1, 1, 1]                              # Phi_3 mod 4
    assert (Comp**3).applyfunc(lambda x: x % 4) == sp.eye(2)   # order 3
    # irreducible action: no eigenvector mod 2 (Phi_3 is the irreducible F_2 quadratic)
    assert [x for x in range(2) if (x * x + x + 1) % 2 == 0] == []
    assert [x for x in range(4) if (x * x + x + 1) % 4 == 0] == []
