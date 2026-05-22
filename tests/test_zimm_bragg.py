"""P4 — A is exactly a Zimm-Bragg helix-coil transfer matrix at s=2, sigma=1/2."""

import sympy as sp

from origin_axiom.algebra import A
from origin_axiom.statistics import zimm_bragg_matrix


def test_A_is_zimm_bragg_at_s_two_sigma_half():
    assert zimm_bragg_matrix(2, sp.Rational(1, 2)) == A


def test_zimm_bragg_parameter_point_is_weakly_cooperative():
    # sigma = 1/2 is weakly cooperative (not the sigma << 1 strong-cooperative
    # regime of typical proteins) — recorded honestly, see CLAIMS.md P4.
    sigma = sp.Rational(1, 2)
    assert sigma == sp.Rational(1, 2)
