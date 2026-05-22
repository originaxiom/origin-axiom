"""
Algebra of the minimal record-transfer system.

Locks claims P1, P2, P6 of ``CLAIMS.md``. Matrices are exact integer
``sympy`` matrices; eigenvalues are exact surds.
"""

import sympy as sp

t = sp.symbols("t")

# --- Primitive parabolic record shears (P1) --------------------------------
L = sp.Matrix([[1, 1], [0, 1]])
R = sp.Matrix([[1, 0], [1, 1]])

# First mixed persistent sectors
A = L * R                       # [[2, 1], [1, 1]]  — the persistent bulk sector
A_RL = R * L                    # [[1, 1], [1, 2]]

# --- Fibonacci fusion-count matrix and basis swap (P2) ---------------------
N_TAU = sp.Matrix([[0, 1], [1, 1]])     # fusion-count matrix of tau x tau = 1 + tau
P_SWAP = sp.Matrix([[0, 1], [1, 0]])    # two-state basis swap

# Fibonacci matrix; F_FIB**2 == A
F_FIB = sp.Matrix([[1, 1], [1, 0]])

# --- Non-degenerate Lorentzian phase-space form preserved by A (P6) --------
# Signature (1,1), det = -5. NOTE: this is a phase-space form, NOT spacetime
# (see GOVERNANCE.md sec. 8).
G = sp.Matrix([[-2, 1], [1, 2]])


def char_poly(M):
    """Characteristic polynomial of ``M`` as a sympy expression in ``t``."""
    return sp.factor(M.charpoly(t).as_expr())


def eigenvalues(M):
    """Exact eigenvalues of ``M`` with multiplicities, as a dict."""
    return M.eigenvals()


def is_parabolic(M):
    """True iff ``M`` in SL(2,Z) is parabolic: det 1 and |trace| == 2."""
    return M.det() == 1 and abs(sp.trace(M)) == 2


def preserves_form(M, form):
    """True iff ``M.T * form * M == form`` (``M`` preserves the bilinear form)."""
    return sp.simplify(M.T * form * M - form) == sp.zeros(*form.shape)


def quadratic_form(form, v):
    """Evaluate the scalar ``v.T * form * v``."""
    return sp.simplify((v.T * form * v)[0, 0])
