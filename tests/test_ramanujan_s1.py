"""S1 lock — the silver octic's delta relation (exact closed form)."""
import sympy as sp


def test_silver_octic_closed_form():
    x = sp.symbols("x")
    s2 = sp.sqrt(2)
    M = (6 + 4*s2 - sp.sqrt((6 + 4*s2)**2 - 4)) / 2
    mpoly = sp.minimal_polynomial(sp.sqrt(M/2), x)
    assert sp.expand(mpoly - (16*x**8 - 96*x**6 + 24*x**4
                              - 24*x**2 + 1)) == 0
    assert sp.Poly(mpoly, x).is_irreducible
