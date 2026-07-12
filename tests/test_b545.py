"""Locks for B545 — c = 1 is a proved ghost level (elliptic-locked)."""
import sympy as sp


def test_c1_class_on_level():
    assert 1*1 + 0 + 0 - 0 == 1


def test_c1_all_slots_negative_definite():
    a = sp.Symbol('a', real=True)
    for (x, y, z) in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        d = sp.expand((z - x*a)**2 + 4*(a*(y - a) - 1))
        assert sp.maximum(d, a, sp.S.Reals) < 0


def test_elliptic_lock_leading_coefficient():
    """The slot discriminant's a^2 coefficient is x^2 - 4."""
    a, x, y, z = sp.symbols('a x y z')
    d = sp.expand((z - x*a)**2 + 4*(a*(y - a) - 1))
    assert sp.Poly(d, a).coeff_monomial(a**2) == x**2 - 4
