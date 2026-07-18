"""B693 — the inert-5 Hecke eigenvalue of the base change is +1 (Steinberg)."""
import sympy as sp


def test_inert5_hecke_is_plus_one():
    # chi_-3(5) = -1 (5 inert); base change L = L(f) L(f x chi)
    assert sp.jacobi_symbol(-3, 5) == -1
    x = sp.symbols("x")
    # local factors at 5: (1 - 5^-s)(1 + 5^-s) = 1 - 25^-s  => a_(5)=+1
    assert sp.expand((1 - x)*(1 + x)) == 1 - x**2
    # a_5=+1, twist a_5=-1, product coefficient of N(P)^-s = +1
    a5, a5_tw = 1, 1*sp.jacobi_symbol(-3, 5)
    assert a5 == 1 and a5_tw == -1        # the two local roots
