"""
Möbius action of A on the upper half-plane H, generating vector field,
and the derived potential.

Locks claims P15 (Möbius generating vector field) and P16 (derived potential).

Everything in this module is exact algebra about A — a direct consequence of
P11's exact form of ``log(A)``. No physical interpretation here; the field-
theoretic lift (kinetic term, dimensionality, particle reading) lives in
``frontier/B6_*`` through ``frontier/B9_*`` as logged observations, not claims.
"""

import sympy as sp

from origin_axiom.algebra import A
from origin_axiom.constants import PHI, PHI_SQ

# --- The variable on the upper half-plane ---------------------------------
tau = sp.symbols("tau")

# --- Derived coupling constant --------------------------------------------
# KAPPA = 2 * log(phi^2) / sqrt(5) = 4 * log(phi) / sqrt(5).
# This is twice the P11 prefactor ``log(phi^2)/sqrt(5)`` of ``log(A)`` — the
# factor of 2 comes from b = c = 2 * (P11 prefactor) in the Möbius generator
# formula v(tau) = b + (a-d) * tau - c * tau^2.
KAPPA = 2 * sp.log(PHI_SQ) / sp.sqrt(5)


def mobius_map(M, var=tau):
    """Action of a 2x2 SL(2) matrix ``M`` on ``H`` as a Möbius transformation.

    ``M = [[a,b],[c,d]]`` acts as ``var -> (a*var + b) / (c*var + d)``.
    """
    return (M[0, 0] * var + M[0, 1]) / (M[1, 0] * var + M[1, 1])


def A_mobius_fixed_points():
    """Exact fixed points of A acting on H as a Möbius transformation.

    Returns ``[phi, -1/phi]``: solving ``(2*tau + 1)/(tau + 1) = tau`` gives
    ``tau^2 - tau - 1 = 0``, whose roots are exactly ``phi`` and ``-1/phi``.
    """
    f = mobius_map(A)
    sols = sp.solve(sp.together(f - tau), tau)
    return sols


# --- P15: the Möbius generating vector field ------------------------------
# v(tau) = b + (a - d) * tau - c * tau^2, where a, b, c, d are the entries of
# log(A). With log(A) = (log(phi^2)/sqrt(5)) * [[1, 2], [2, -1]] (P11):
#   a = -d = log(phi^2)/sqrt(5)
#   b = c = 2 * log(phi^2)/sqrt(5)
# so v(tau) = 2*kappa_half + 2*kappa_half * tau - 2*kappa_half * tau^2
#           = -2*kappa_half * (tau^2 - tau - 1)
#           = -KAPPA * (tau^2 - tau - 1).
def vector_field(var=tau):
    """The Möbius generating vector field of A on H. Returns ``-KAPPA*(var^2 - var - 1)``."""
    return -KAPPA * (var**2 - var - 1)


def vector_field_from_logA():
    """Alternative derivation: ``b + (a - d)*tau - c*tau^2`` from log(A) entries.

    Returned in expanded form. Used by tests to confirm both forms agree symbolically.
    """
    from origin_axiom.algebra import H_LOG_A
    logA = (sp.log(PHI_SQ) / sp.sqrt(5)) * H_LOG_A
    a, b, c, d = logA[0, 0], logA[0, 1], logA[1, 0], logA[1, 1]
    return sp.expand(b + (a - d) * tau - c * tau**2)


# --- P16: the derived potential -------------------------------------------
# V is the antiderivative of -v = KAPPA*(tau^2 - tau - 1):
#   V(tau) = KAPPA * (tau^3/3 - tau^2/2 - tau).
def potential(var=tau):
    """The derived potential whose gradient flow is ``v``: ``V(var) = KAPPA*(var^3/3 - var^2/2 - var)``."""
    return KAPPA * (var**3 / sp.Integer(3) - var**2 / sp.Integer(2) - var)


def potential_derivative(var=tau):
    """``V'(var) = KAPPA*(var^2 - var - 1)``. Same polynomial as ``-v(var)``."""
    return KAPPA * (var**2 - var - 1)


def potential_second_derivative(var=tau):
    """``V''(var) = KAPPA*(2*var - 1)``."""
    return KAPPA * (2 * var - 1)


def mass_squared():
    """``V''(phi) = KAPPA * sqrt(5)``. The minimum at ``phi`` has positive curvature."""
    return KAPPA * sp.sqrt(5)
