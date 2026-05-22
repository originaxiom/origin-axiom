"""P3 — L + R is exactly a normalized 1D zero-field Ising transfer matrix."""

import sympy as sp

from origin_axiom.algebra import L, R
from origin_axiom.statistics import correlation_length, ising_transfer_matrix, K_ISING


def test_L_plus_R():
    assert L + R == sp.Matrix([[2, 1], [1, 2]])


def test_ising_transfer_matrix_equals_L_plus_R_at_K_ising():
    assert sp.simplify(ising_transfer_matrix(K_ISING) - (L + R)) == sp.zeros(2, 2)


def test_L_plus_R_eigenvalues_are_three_and_one():
    assert set((L + R).eigenvals().keys()) == {3, 1}


def test_correlation_length_is_one_over_log_three():
    assert sp.simplify(correlation_length(K_ISING) - 1 / sp.log(3)) == 0
