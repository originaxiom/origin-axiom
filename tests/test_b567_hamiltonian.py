"""B567 — the Hamiltonian handoff verdict locks.

The claimed six pi/3-spaced levels at level 15 are IMPOSSIBLE: rho(A1) has forced
projective order 20 (= ord of A1 in SL(2,Z/15)); verified constructively for the
standard Weil rep at levels 15 and 165 (11 and 20 distinct eigenvalues, not 6).

Corrected 2026-11-10 (B1862; the advisor seat's audit, E13, reproduced on main): this lock asserted 21 distinct
eigenvalues at level 165. It clustered the sorted angles on the line, so the eigenvalue at angle +-pi, which np.angle
returns on both sides of its branch cut, was counted twice -- and only on some machines, so the lock failed elsewhere.
Projective order 20 allows at most 20. The count is now made on the circle: each eigenvalue is placed on the lattice
of 20th roots of the constant U^20 is a multiple of."""
import numpy as np


def _weil_A1(N):
    zeta = np.exp(2j * np.pi / N)
    s = (N + 1) // 2
    T = np.diag([zeta ** ((s * x * x) % N) for x in range(N)])
    S = np.array([[zeta ** ((x * y) % N) for y in range(N)] for x in range(N)]) / np.sqrt(N)
    L = S @ np.linalg.inv(T) @ np.linalg.inv(S)
    return T @ L


def _distinct_and_order(N, kmax=60):
    """(number of distinct eigenvalues, projective order, their multiplicities), counted on the circle"""
    U = _weil_A1(N)
    order = None
    Uk = np.eye(N)
    for k in range(1, kmax + 1):
        Uk = Uk @ U
        if abs(Uk[0, 0]) > 1e-9 and np.linalg.norm(Uk / Uk[0, 0] - np.eye(N)) < 1e-6:
            order = k
            break
    assert order is not None
    # U^order = c * 1, so every eigenvalue is c^(1/order) times an order-th root of unity: place each on that lattice
    base = Uk[0, 0] ** (1.0 / order)
    ev = np.linalg.eigvals(U)
    idx = np.round(np.angle(ev / base) / (2 * np.pi / order)).astype(int) % order
    assert np.max(np.abs(ev - base * np.exp(2j * np.pi * idx / order))) < 1e-6        # every eigenvalue is on the lattice
    mult = sorted(np.bincount(idx, minlength=order)[np.bincount(idx, minlength=order) > 0].tolist(), reverse=True)
    return len(mult), order, mult


def test_a1_matrix_orders():
    A = np.array([[2, 1], [1, 1]])
    assert (np.linalg.matrix_power(A, 2) % 3 == (2 * np.eye(2)) % 3).all()   # A^2 = -I mod 3
    assert (np.linalg.matrix_power(A, 5) % 5 == (4 * np.eye(2)) % 5).all()   # A^5 = -I mod 5
    # => ord(A1) in SL(2,Z/15) = lcm(4,10) = 20; pi/3 spacing would force order 6: 6 ∤ 20, 6 ∤ 40.
    assert 20 % 6 != 0 and 40 % 6 != 0


def test_level15_spectrum_refutes_six_levels():
    n, order, mult = _distinct_and_order(15)
    assert order == 20                      # forced projective order
    assert n == 11 and n != 6               # NOT six pi/3-spaced levels
    assert mult == [2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1] and sum(mult) == 15


def test_level165_spectrum_refutes_28_27():
    n, order, mult = _distinct_and_order(165)
    assert order == 20                      # lcm(4,10,5)
    assert n <= order                       # at most `order` distinct eigenvalues: 21 was never possible
    assert n == 20 and n != 6               # NOT six levels with mult 28/27
    assert mult == [12, 12, 12, 12, 11, 11, 10, 10, 10, 10, 7, 7, 7, 6, 6, 5, 5, 4, 4, 4] and sum(mult) == 165
    assert 28 not in mult and 27 not in mult
