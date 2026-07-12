"""Lock: the charge-tower primes are sparse — only 11 divides e_n (n<=6) for p<=79.

e_n = det(I - M_n) where M_0 = Fibonacci matrix and M_{n+1} = [[M,M],[M^2,M]]
(the escalator functor T).  The determinant is taken mod p with a fast numpy
Gaussian elimination so the 128x128 rung stays sub-second (sympy .det() on that
size times out).  See frontier/B556_escalator_tower/FINDINGS.md.
"""
import numpy as np
import sympy as sp

x = sp.Symbol('x')
F = np.array([[1, 1], [1, 0]], dtype=np.int64)


def _T_mod(M, p):
    """One rung of the escalator functor, reduced mod p."""
    M2 = (M @ M) % p
    n = M.shape[0]
    top = np.hstack([M, M])
    bot = np.hstack([M2, M])
    return np.vstack([top, bot]) % p


def _det_mod_p(M, p):
    """det(M) mod p via fraction-free-ish Gaussian elimination over F_p."""
    A = (M % p).astype(np.int64)
    n = A.shape[0]
    det = 1
    for i in range(n):
        nz = np.nonzero(A[i:, i] % p)[0]
        if len(nz) == 0:
            return 0
        piv = i + int(nz[0])
        if piv != i:
            A[[i, piv]] = A[[piv, i]]
            det = (-det) % p
        det = (det * int(A[i, i])) % p
        inv = pow(int(A[i, i]), p - 2, p)
        rows = np.arange(i + 1, n)
        if len(rows):
            f = (A[rows, i] * inv) % p
            A[rows] = (A[rows] - f[:, None] * A[i]) % p
    return int(det % p)


def _appears(p, nmax=7):
    """True if p | e_n for some 0 <= n < nmax (M_n has size 2^(n+1))."""
    M = F
    for _ in range(nmax):
        I = np.eye(M.shape[0], dtype=np.int64)
        if _det_mod_p(I - M, p) == 0:
            return True
        M = _T_mod(M, p)
    return False


def test_only_11_appears_small():
    """Among primes 3..79, only 11 divides some e_n for n<=6 (size<=128)."""
    appearing = {p for p in sp.primerange(3, 80) if _appears(p)}
    assert appearing == {11}


def test_shared_invariants_do_not_predict_appearance():
    """19, 61, 79 share 11's g-type (1,2) and 5-QR, yet don't appear (n<=6)."""
    g = x**3 - x**2 + 2*x - 1

    def gdeg(p):
        return tuple(sorted(int(f.degree())
                            for f, _ in sp.factor_list(sp.Poly(g, x, modulus=p))[1]))

    for p in (11, 19, 61, 79):                       # identical invariants ...
        assert gdeg(p) == (1, 2) and sp.jacobi_symbol(5, p) == 1
    assert _appears(11) and not any(_appears(p) for p in (19, 61, 79))  # ... but only 11 appears
