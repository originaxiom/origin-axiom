"""B567 — the Hamiltonian handoff verdict locks.

The claimed six pi/3-spaced levels at level 15 are IMPOSSIBLE: rho(A1) has forced
projective order 20 (= ord of A1 in SL(2,Z/15)); verified constructively for the
standard Weil rep at levels 15 and 165 (11 and 21 distinct eigenvalues, not 6)."""
import numpy as np


def _weil_A1(N):
    zeta = np.exp(2j * np.pi / N)
    s = (N + 1) // 2
    T = np.diag([zeta ** ((s * x * x) % N) for x in range(N)])
    S = np.array([[zeta ** ((x * y) % N) for y in range(N)] for x in range(N)]) / np.sqrt(N)
    L = S @ np.linalg.inv(T) @ np.linalg.inv(S)
    return T @ L


def _distinct_and_order(N, kmax=60):
    U = _weil_A1(N)
    ang = np.sort(np.angle(np.linalg.eigvals(U)))
    clusters = []
    for a in ang:
        if clusters and abs(a - clusters[-1][0]) < 1e-6:
            clusters[-1][1] += 1
        else:
            clusters.append([a, 1])
    order = None
    Uk = np.eye(N)
    for k in range(1, kmax + 1):
        Uk = Uk @ U
        if abs(Uk[0, 0]) > 1e-9 and np.linalg.norm(Uk / Uk[0, 0] - np.eye(N)) < 1e-6:
            order = k
            break
    return len(clusters), order


def test_a1_matrix_orders():
    A = np.array([[2, 1], [1, 1]])
    assert (np.linalg.matrix_power(A, 2) % 3 == (2 * np.eye(2)) % 3).all()   # A^2 = -I mod 3
    assert (np.linalg.matrix_power(A, 5) % 5 == (4 * np.eye(2)) % 5).all()   # A^5 = -I mod 5
    # => ord(A1) in SL(2,Z/15) = lcm(4,10) = 20; pi/3 spacing would force order 6: 6 ∤ 20, 6 ∤ 40.
    assert 20 % 6 != 0 and 40 % 6 != 0


def test_level15_spectrum_refutes_six_levels():
    n, order = _distinct_and_order(15)
    assert order == 20                      # forced projective order
    assert n == 11 and n != 6               # NOT six pi/3-spaced levels


def test_level165_spectrum_refutes_28_27():
    n, order = _distinct_and_order(165)
    assert order == 20                      # lcm(4,10,5)
    assert n == 21 and n != 6               # NOT six levels with mult 28/27
