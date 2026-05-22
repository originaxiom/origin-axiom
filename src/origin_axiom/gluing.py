"""
Variational boundary-to-bulk gluing identity. Locks claim P7 of ``CLAIMS.md``.

The hyperbolic bulk action ``S_A`` is the on-shell gluing of the two parabolic
boundary half-move generating functions::

    S_A(q, Q) = ext_{m,s} [ S_L(m, Q) - F_R(q, s) + m*s ]

where ``m*s`` is the canonical corner term. This is an exact model-level
variational identity, not a derivation of physical dynamics.
"""

import sympy as sp


def S_A(q, Q):
    """Type-I generating function of the bulk sector ``A``."""
    return q**2 - q * Q + sp.Rational(1, 2) * Q**2


def S_L(m, Q):
    """Type-I generating function of the ``L`` boundary half-move."""
    return sp.Rational(1, 2) * (Q - m) ** 2


def F_R(q, s):
    """Type-II generating function of the ``R`` boundary half-move."""
    return q * s - sp.Rational(1, 2) * q**2


def gluing_functional(q, m, s, Q):
    """The gluing functional ``W = S_L(m,Q) - F_R(q,s) + m*s``."""
    return S_L(m, Q) - F_R(q, s) + m * s


def on_shell_gluing(q, Q):
    """
    Extremize the gluing functional ``W`` over the intermediate data ``(m, s)``
    and return the resulting on-shell expression in ``(q, Q)``.
    """
    m, s = sp.symbols("m_int s_int", real=True)
    W = gluing_functional(q, m, s, Q)
    solution = sp.solve([sp.diff(W, m), sp.diff(W, s)], [m, s], dict=True)[0]
    return sp.expand(W.subs(solution))
