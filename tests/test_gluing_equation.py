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


def test_is_the_snappy_edge_equation_under_reciprocal_shape_change():
    """P12 identification (self-audit 2026-06-16): z^2(z-1)^2=1 IS SnapPy's figure-eight edge equation,
    not merely an algebraic factorization. SnapPy's gluing_equations() for 4_1 give, at w=z, the edge
    polynomial p(z) = z^4 - z^2 + 2z - 1 = (z^2-z+1)(z^2+z-1) (verified against SnapPy in audit/lab).
    The repo's lhs = z^2(z-1)^2 - 1 is exactly the RECIPROCAL of p (the z->1/z cross-ratio shape change):
    lhs(z) == -z^4 * p(1/z). This proves the topological identification (roots are exact reciprocals),
    not just the discriminants. Sympy-only (no SnapPy needed at test time)."""
    z, lhs, _e, _g = gluing_equation_factorization()
    snappy_edge = z**4 - z**2 + 2*z - 1                    # SnapPy 4_1 edge eq at w=z (verified)
    assert sp.factor(snappy_edge) == sp.factor((z**2 - z + 1) * (z**2 + z - 1))
    assert sp.expand(lhs - (-z**4 * snappy_edge.subs(z, 1/z))) == 0   # lhs == -z^4 p(1/z): reciprocal
    # the Eisenstein (complete-structure) factor is identical in both coordinates:
    assert sp.rem(snappy_edge, z**2 - z + 1, z) == 0
