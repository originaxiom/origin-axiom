"""P15 — Möbius generating vector field of A on H.

The Möbius action of ``A = [[2,1],[1,1]]`` on the upper half-plane H,
``tau -> (2*tau+1)/(tau+1)``, has fixed points ``phi`` and ``-1/phi``. Its
one-parameter generating vector field, computed from ``log(A)`` (P11), is
``v(tau) = -KAPPA*(tau^2 - tau - 1)`` with ``KAPPA = 2*log(phi^2)/sqrt(5)``.

Pure algebra — direct consequence of P1 and P11. No physical interpretation.
"""

import sympy as sp

from origin_axiom.algebra import A
from origin_axiom.constants import PHI, PHI_SQ
from origin_axiom.mobius import (
    KAPPA,
    A_mobius_fixed_points,
    mobius_map,
    tau,
    vector_field,
    vector_field_from_logA,
)


def test_mobius_action_form():
    """A acts on H as ``tau -> (2*tau + 1)/(tau + 1)``."""
    f = mobius_map(A)
    expected = (2 * tau + 1) / (tau + 1)
    assert sp.simplify(f - expected) == 0


def test_fixed_points_are_phi_and_minus_one_over_phi():
    """``f(tau) = tau`` collapses to ``tau^2 - tau - 1 = 0``, roots phi and -1/phi."""
    fps = A_mobius_fixed_points()
    assert sp.simplify(PHI - max(fps, key=lambda r: float(r))) == 0
    assert sp.simplify(-1 / PHI - min(fps, key=lambda r: float(r))) == 0


def test_vector_field_factored_form():
    """``v(tau) = -KAPPA * (tau^2 - tau - 1)`` exactly."""
    v = vector_field()
    expected = -KAPPA * (tau**2 - tau - 1)
    assert sp.simplify(v - expected) == 0


def test_vector_field_matches_logA_derivation():
    """The two derivations of v(tau) agree symbolically.

    Form 1: ``b + (a-d)*tau - c*tau^2`` from entries of log(A).
    Form 2: ``-KAPPA * (tau^2 - tau - 1)``.
    """
    v1 = vector_field_from_logA()
    v2 = vector_field()
    assert sp.expand(v1 - v2) == 0


def test_vector_field_vanishes_at_phi():
    """``v(phi) = 0`` since ``phi^2 - phi - 1 = 0``. Fixed-point of the flow."""
    assert sp.simplify(vector_field(PHI)) == 0


def test_vector_field_vanishes_at_minus_one_over_phi():
    """``v(-1/phi) = 0``. The other (repelling) fixed point."""
    assert sp.simplify(vector_field(-1 / PHI)) == 0


def test_vector_field_at_zero_equals_kappa():
    """``v(0) = -KAPPA*(0 - 0 - 1) = KAPPA``. Zero is NOT a fixed point."""
    assert sp.simplify(vector_field(0) - KAPPA) == 0


def test_kappa_is_twice_p11_prefactor():
    """``KAPPA = 2 * log(phi^2)/sqrt(5)``. The factor of 2 comes from b = c = 2*(P11 prefactor)."""
    expected = 2 * sp.log(PHI_SQ) / sp.sqrt(5)
    assert sp.simplify(KAPPA - expected) == 0


def test_kappa_numerical_value():
    """Numerical anchor for downstream frontier work."""
    assert abs(float(KAPPA) - 0.86081788) < 1e-7
