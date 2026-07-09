"""B478 — the +j asymmetry IS the clock translation (exact, proved). Full recompute.

Locks the operator identity Par · D(m,c) · Par = D(m,c) · Z^{cm} at level 15
(D(m,c) = diag(zeta^{c·m·j(j-1)/2}), Z = diag(zeta^j) the clock) two ways:
exactly in the exponents mod 15 (the two-line proof), and numerically as in
plusj_verify.py. Plus the trace-invisibility corollary (tr Z^{cm} = 0).
"""
import numpy as np

N = 15
CS = (1, 14, 2, 4)
MS = (1, 2, 3)


def test_exponent_identity_exact():
    """The proof, verbatim in Z/15: conjugating by Par sends entry j to (-j)%N, and
    c·m·(-j)(-j-1)/2 = c·m·j(j-1)/2 + c·m·j (mod 15) — D's entry times Z^{cm}'s."""
    for c in CS:
        for m in MS:
            for j in range(N):
                k = (-j) % N
                lhs = (c * m * (k * (k - 1) // 2)) % N
                rhs = (c * m * (j * (j - 1) // 2) + c * m * j) % N
                assert lhs == rhs, (c, m, j)


def test_operator_identity_numeric():
    """The plusj_verify.py battery: ||Par D Par - D Z^{cm}|| < 1e-12 for c in
    {1,14,2,4}, m in {1,2,3}."""
    z = np.exp(2j * np.pi / N)
    Par = np.zeros((N, N), complex)
    for j in range(N):
        Par[(-j) % N, j] = 1
    Z = np.diag([z ** j for j in range(N)])
    assert np.allclose(Par @ Par, np.eye(N))
    for c in CS:
        for m in MS:
            D = np.diag([z ** ((c * m * (j * (j - 1) // 2)) % N) for j in range(N)])
            lhs = Par @ D @ Par
            rhs = D @ np.linalg.matrix_power(Z, (c * m) % N)
            assert np.max(np.abs(lhs - rhs)) < 1e-12, (c, m)


def test_translation_is_trace_invisible():
    """The FINDINGS corollary: the defect Z^{cm} is traceless for every (c,m) probed
    (cm not divisible by 15), so trace invariants cannot see the two-world defect —
    consistent with the B466/B472 world-independence of all trace data."""
    z = np.exp(2j * np.pi / N)
    for c in CS:
        for m in MS:
            assert (c * m) % N != 0
            tr = sum(z ** ((c * m * j) % N) for j in range(N))
            assert abs(tr) < 1e-12, (c, m)
