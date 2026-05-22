"""P7 — the bulk action S_A is the on-shell gluing of the boundary actions."""

import sympy as sp

from origin_axiom.gluing import on_shell_gluing, S_A


def test_on_shell_gluing_reproduces_S_A():
    q, Q = sp.symbols("q Q", real=True)
    assert sp.expand(on_shell_gluing(q, Q) - S_A(q, Q)) == 0


def test_S_A_is_the_expected_generating_function():
    q, Q = sp.symbols("q Q", real=True)
    assert sp.expand(S_A(q, Q) - (q**2 - q * Q + sp.Rational(1, 2) * Q**2)) == 0
