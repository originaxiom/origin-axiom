"""Locks for B434 -- the Meyerhoff trace field x^4-x-1: disc -283, S4, no quadratic subfield."""
import sympy as sp

x = sp.Symbol('x')
P = x**4 - x - 1

def test_quartic_disc_is_minus_283_prime():
    d = sp.discriminant(P, x)
    assert d == -283 and sp.isprime(283)

def test_irreducible_and_S4_so_no_quadratic_subfield():
    assert sp.Poly(P, x).is_irreducible
    # resolvent cubic of x^4 + px + q (p=-1, q=-1): x^3 - 4qx - p^2 = x^3 + 4x - 1
    R = x**3 + 4*x - 1
    assert sp.Poly(R, x).is_irreducible          # cubic resolvent irreducible
    # disc not a square + resolvent irreducible => Galois S4 => quartic has NO quadratic subfield
    assert not sp.sqrt(sp.Abs(-283)).is_integer
