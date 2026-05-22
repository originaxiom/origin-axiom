"""P12 — the figure-eight gluing equation factorization."""

import sympy as sp

from origin_axiom.topology import gluing_equation_factorization


def test_gluing_equation_factors_into_eisenstein_times_golden():
    _z, lhs, eisenstein, golden = gluing_equation_factorization()
    assert sp.expand(lhs - eisenstein * golden) == 0


def test_discriminants_are_minus_three_and_five():
    z, _lhs, eisenstein, golden = gluing_equation_factorization()
    assert sp.discriminant(eisenstein, z) == -3   # Eisenstein quadratic
    assert sp.discriminant(golden, z) == 5        # golden quadratic
