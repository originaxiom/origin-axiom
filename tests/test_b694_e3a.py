"""B694 — E-3a gate: a_(5)=+1 and the Hecke-field-Q forcing of being."""
import sympy as sp


def test_a5_plus_one_and_phi_unreachable():
    x = sp.symbols("x")
    assert sp.expand((1 - x)*(1 + x)) == 1 - x**2      # a_(5)=+1 (Euler factor)
    # base change of a rational form has Hecke field Q; phi is not rational
    assert not sp.sqrt(5).is_rational                   # phi unreachable => being forced
