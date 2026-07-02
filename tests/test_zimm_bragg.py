"""P4 — A is exactly a Zimm-Bragg helix-coil transfer matrix at s=2, sigma=1/2.

Hardened 2026-07-01 (audit): the parameter point (s, sigma) = (2, 1/2) is now
*derived* by solving zimm_bragg_matrix(s, sigma) == A — showing it is the
unique solution — rather than plugged in and echoed back.
"""

import sympy as sp

from origin_axiom.algebra import A
from origin_axiom.statistics import zimm_bragg_matrix


def test_A_is_zimm_bragg_at_s_two_sigma_half():
    assert zimm_bragg_matrix(2, sp.Rational(1, 2)) == A


def test_parameter_point_is_the_unique_solution():
    # Solve the matrix identity for (s, sigma): the Zimm-Bragg point realizing
    # A is forced, not chosen.
    s, sigma = sp.symbols("s sigma")
    eqs = [sp.Eq(zimm_bragg_matrix(s, sigma)[i, j], A[i, j]) for i in range(2) for j in range(2)]
    sols = sp.solve(eqs, [s, sigma], dict=True)
    assert sols == [{s: 2, sigma: sp.Rational(1, 2)}]


def test_zimm_bragg_parameter_point_is_weakly_cooperative():
    # Weakly cooperative means 0 < sigma < 1 but NOT the sigma << 1
    # strong-cooperativity regime of typical proteins — recorded honestly,
    # see CLAIMS.md P4. Derived sigma = 1/2 satisfies exactly that.
    s, sigma = sp.symbols("s sigma")
    eqs = [sp.Eq(zimm_bragg_matrix(s, sigma)[i, j], A[i, j]) for i in range(2) for j in range(2)]
    sol = sp.solve(eqs, [s, sigma], dict=True)[0]
    assert 0 < sol[sigma] < 1          # cooperative (helix nucleation penalized)
    assert not sol[sigma] < sp.Rational(1, 100)   # but only weakly so
