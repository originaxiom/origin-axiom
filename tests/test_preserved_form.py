"""P6 — A preserves a non-degenerate Lorentzian phase-space form G.

NOTE: G is a form on (q, p) phase space, NOT a spacetime metric
(see GOVERNANCE.md sec. 8).
"""

import sympy as sp

from origin_axiom.algebra import A, G, L, preserves_form, quadratic_form, R
from origin_axiom.constants import PHI


def test_A_preserves_G():
    assert preserves_form(A, G)


def test_G_is_nondegenerate_with_lorentzian_signature():
    assert G.det() == -5  # non-degenerate
    evs = list(G.eigenvals().keys())
    assert len(evs) == 2
    assert any(e > 0 for e in evs) and any(e < 0 for e in evs)  # signature (1,1)


def test_L_and_R_alone_do_not_preserve_G():
    # Individually the boundary half-moves preserve only degenerate forms.
    assert not preserves_form(L, G)
    assert not preserves_form(R, G)
    assert preserves_form(L, sp.Matrix([[0, 0], [0, 1]]))  # momentum only
    assert preserves_form(R, sp.Matrix([[1, 0], [0, 0]]))  # position only


def test_null_directions_of_G_are_the_phi_eigenvectors_of_A():
    v = sp.Matrix([PHI, 1])  # the phi^2-eigenvector of A
    assert sp.simplify(A * v - PHI**2 * v) == sp.zeros(2, 1)
    assert quadratic_form(G, v) == 0  # ... and it is G-null


def test_P13_log_A_shape_and_G_are_isospectral():
    # P13 — elementary corollary of P11 + P6: H_LOG_A (the shape of log A,
    # i.e. log A rescaled) and the preserved form G are both symmetric and
    # traceless with det -5, hence share the spectrum {+sqrt5, -sqrt5}.
    from origin_axiom.algebra import H_LOG_A

    assert H_LOG_A.det() == -5 and G.det() == -5
    assert set(H_LOG_A.eigenvals()) == set(G.eigenvals())
