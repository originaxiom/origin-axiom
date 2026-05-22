"""P2 — A is basis-conjugate to the squared Fibonacci fusion-count matrix."""

from origin_axiom.algebra import A, A_RL, F_FIB, N_TAU, P_SWAP


def test_N_tau_squared_equals_RL():
    assert N_TAU**2 == A_RL


def test_A_is_basis_conjugate_to_N_tau_squared():
    assert A == P_SWAP * N_TAU**2 * P_SWAP


def test_A_power_equals_conjugated_N_tau_even_power():
    for n in range(1, 9):
        assert A**n == P_SWAP * N_TAU ** (2 * n) * P_SWAP


def test_fibonacci_matrix_squared_is_A():
    assert F_FIB**2 == A
