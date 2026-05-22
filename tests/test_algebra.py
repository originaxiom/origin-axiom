"""P1 — primitive parabolic shears and the trace-3 persistent sector."""

import sympy as sp

from origin_axiom.algebra import A, char_poly, eigenvalues, is_parabolic, L, R, t
from origin_axiom.constants import PHI_SQ


def test_L_and_R_are_parabolic_shears():
    assert is_parabolic(L) and is_parabolic(R)
    assert sp.trace(L) == 2 and sp.trace(R) == 2
    assert L.det() == 1 and R.det() == 1


def test_A_equals_L_times_R():
    assert A == sp.Matrix([[2, 1], [1, 1]])


def test_A_trace_and_determinant():
    assert sp.trace(A) == 3
    assert A.det() == 1


def test_A_characteristic_polynomial():
    assert sp.expand(char_poly(A) - (t**2 - 3 * t + 1)) == 0


def test_A_eigenvalues_are_phi_squared_and_its_inverse():
    evs = eigenvalues(A)
    assert len(evs) == 2 and all(mult == 1 for mult in evs.values())
    keys = list(evs.keys())
    assert any(sp.simplify(k - PHI_SQ) == 0 for k in keys)
    assert any(sp.simplify(k - 1 / PHI_SQ) == 0 for k in keys)
