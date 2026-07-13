"""B570 AP3 — the clock arithmetic. Locks the Pisano/ord(A1) theorem and the
abelian-theater ord-equality + c-mod-24-cancellation facts.

A1 = F^2 = [[2,1],[1,1]], F = [[1,1],[1,0]] (Fibonacci matrix), det F = -1, det A1 = +1.
"""
import numpy as np
from math import gcd


# ---------- Part 1: Pisano-period theorem, two independent methods ----------

def pisano_period_bruteforce(n):
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(0, n * n * 6 + 10):
        a, b = b, (a + b) % n
        if a == 0 and b == 1:
            return i + 1
    raise RuntimeError(f"period not found for n={n}")


def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def pisano_period_crt(n):
    if n == 1:
        return 1
    f = factorize(n)
    val = 1
    for p, k in f.items():
        pp = pisano_period_bruteforce(p) * p ** (k - 1)
        val = val * pp // gcd(val, pp)
    return val


def mat_mul_mod(A, B, n):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % n, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % n],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % n, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % n],
    ]


def mat_order_mod(M, n):
    I = [[1, 0], [0, 1]]
    cur = [row[:] for row in M]
    k = 1
    maxiter = n * n * 20 + 100
    while cur != I:
        cur = mat_mul_mod(cur, M, n)
        k += 1
        if k > maxiter:
            raise RuntimeError(f"order not found n={n}")
    return k


F = [[1, 1], [1, 0]]
A1 = [[2, 1], [1, 1]]

HIGHLIGHT_N = [3, 5, 11, 15, 30, 165]
HIGHLIGHT_EXPECT = {
    3: (8, 4), 5: (20, 10), 11: (10, 5), 15: (40, 20), 30: (120, 60), 165: (40, 20),
}  # N -> (pi(N), ord(A1 mod N))


def test_F_squared_is_A1():
    assert mat_mul_mod(F, F, 10 ** 9) == A1


def test_ord_F_equals_pisano_all_N_le_1000():
    for N in range(2, 1001):
        piN = pisano_period_bruteforce(N)
        ordF = mat_order_mod(F, N)
        assert ordF == piN, (N, ordF, piN)


def test_pisano_crt_matches_bruteforce_all_N_le_1000():
    for N in range(2, 1001):
        assert pisano_period_bruteforce(N) == pisano_period_crt(N)


def test_ord_A1_equals_pi_over_gcd2_all_N_le_1000():
    for N in range(2, 1001):
        piN = pisano_period_bruteforce(N)
        ordA1 = mat_order_mod(A1, N)
        assert ordA1 == piN // gcd(piN, 2), (N, ordA1, piN)


def test_highlight_table():
    for N in HIGHLIGHT_N:
        piN = pisano_period_bruteforce(N)
        ordA1 = mat_order_mod(A1, N)
        exp_pi, exp_ord = HIGHLIGHT_EXPECT[N]
        assert (piN, ordA1) == (exp_pi, exp_ord), (N, piN, ordA1)


# ---------- Part 2: abelian U(1)_N theater, ord equality + c-mod-24 cancellation ----------

def build_theater(N):
    """U(1)_N pointed modular data: Z/N, q(x) = x^2/N mod 1, c = 1 (compact boson)."""
    T = np.zeros((N, N), dtype=complex)
    for x in range(N):
        qx = (x * x) / N
        T[x, x] = np.exp(2j * np.pi * (qx - 1.0 / 24.0))
    S = np.zeros((N, N), dtype=complex)
    for x in range(N):
        for y in range(N):
            S[x, y] = np.exp(-2j * np.pi * 2 * x * y / N) / np.sqrt(N)
    return S, T


def is_gate_consistent(N, tol=1e-8):
    S, T = build_theater(N)
    I = np.eye(N)
    return np.max(np.abs(S @ S.conj().T - I)) < tol


def word_A1_rep(S, T):
    Sinv = np.linalg.inv(S)
    Tinv = np.linalg.inv(T)
    return T @ S @ Tinv @ Sinv


def mat_order_complex(M, tol=1e-6, maxiter=2000):
    n = M.shape[0]
    I = np.eye(n)
    cur = np.eye(n, dtype=complex)
    for k in range(1, maxiter + 1):
        cur = cur @ M
        if np.max(np.abs(cur - I)) < tol:
            return k
    return None


ODD_N_TESTED = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]


def test_gate_separates_odd_even_N_le_24():
    for N in range(1, 25):
        assert is_gate_consistent(N) == (N % 2 == 1), N


def test_theater_Z_is_exactly_plus_one_and_real_for_odd_N():
    for N in ODD_N_TESTED:
        S, T = build_theater(N)
        rep = word_A1_rep(S, T)
        Z = np.trace(rep)
        assert abs(Z - 1.0) < 1e-6, (N, Z)


def test_theater_ord_equals_ord_A1_mod_N_for_odd_N():
    for N in ODD_N_TESTED:
        S, T = build_theater(N)
        rep = word_A1_rep(S, T)
        ord_rep = mat_order_complex(rep)
        if N == 1:
            ord_mod = 1
        else:
            piN = pisano_period_bruteforce(N)
            ord_mod = piN // gcd(piN, 2)
        assert ord_rep == ord_mod, (N, ord_rep, ord_mod)


def test_commutator_word_cancels_overall_T_phase():
    """Algebraic fact: for diagonal T = z*D (any scalar phase z), T S T^-1 S^-1
    is independent of z. This is why the c mod 24 twist drops out of rho(A1)."""
    N = 7
    S, T = build_theater(N)
    for phase in [0.0, 0.37, 1.0, 2.9]:
        z = np.exp(2j * np.pi * phase)
        Tprime = z * T
        rep = word_A1_rep(S, T)
        rep_prime = word_A1_rep(S, Tprime)
        assert np.allclose(rep, rep_prime, atol=1e-9)


def test_word_dependence_under_anomaly():
    """T^2 S T equals T S T^-1 S^-1 as abstract SL(2,Z) matrices (both = A1 exactly),
    but in the (anomalous, lambda != 1) U(1)_N theater rep they differ by a phase —
    the B569 word-dependence lesson, reconfirmed."""
    S_int = np.array([[0, -1], [1, 0]])
    T_int = np.array([[1, 1], [0, 1]])
    Sinv_int = np.linalg.inv(S_int)
    Tinv_int = np.linalg.inv(T_int)
    w1 = T_int @ S_int @ Tinv_int @ Sinv_int
    w2 = T_int @ T_int @ S_int @ T_int
    assert np.allclose(w1, w2)  # same SL(2,Z) element, and it IS A1
    assert np.array_equal(w1.astype(int), np.array(A1))

    N = 7
    S, T = build_theater(N)
    rep_comm = word_A1_rep(S, T)
    rep_T2ST = T @ T @ S @ T
    Z_comm = np.trace(rep_comm)
    Z_T2ST = np.trace(rep_T2ST)
    assert abs(Z_comm - 1.0) < 1e-6
    assert abs(Z_T2ST - 1.0) > 1e-3  # NOT the same value -> word-dependent under anomaly
