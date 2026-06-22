"""B192 -- SL(n>=3) higher-rank Lyapunov spectrum (V185). Fast locks.

The metallic SL(n) transfer cocycle's full Lyapunov spectrum sums to 0 (SL(n)) and is SYMMETRIC (symplectic)
iff n is EVEN, ASYMMETRIC iff n is ODD -- directly realizing V29 (symplectic form exists iff n even). The even-n
symmetry is SPECIAL to the metallic cocycle (a generic SL(n) is asymmetric for all n). Full version in
sln_higher_rank.py.
"""
import numpy as np


def _Mn(n, E, V):
    if n == 2: return np.array([[E - V, -1.0], [1.0, 0.0]])
    M = np.zeros((n, n)); M[0, 0] = E - V; M[0, 1] = -1.0; M[0, n-1] += (-1.0)**(n-1)
    for i in range(1, n): M[i, i-1] = 1.0
    return M


def _fib(k):
    w = {1: "a", 2: "ab"}
    for j in range(3, k+1): w[j] = w[j-1] + w[j-2]
    return w[k]


def _spec(mats):
    n = mats[0].shape[0]; Q = np.eye(n); s = np.zeros(n)
    for M in mats:
        Q, R = np.linalg.qr(M @ Q); d = np.sign(np.diag(R)); Q = Q*d; R = (R.T*d).T
        s += np.log(np.abs(np.diag(R)) + 1e-300)
    return np.sort(s/len(mats))[::-1]


def _asym(g): return float(np.sum(np.abs(g + g[::-1]))/2)


def _metallic(n, k=12, Es=(1.3, 2.1, -1.7)):
    w = _fib(k)
    return np.mean([_spec([_Mn(n, E, 1.0 if c == "a" else 0.0) for c in w]) for E in Es], axis=0)


def test_spectrum_sums_to_zero_and_parity_symmetry():
    a = {n: _asym(_metallic(n)) for n in (2, 3, 4, 5)}
    for n in (3, 4, 5):
        assert abs(_metallic(n).sum()) < 1e-9        # SL(n): det=1
    assert a[2] < 0.02 and a[4] < 0.02               # even n -> symmetric (symplectic)
    assert a[3] > 0.08 and a[5] > 0.08               # odd n -> asymmetric (non-Hermitian)


def test_even_n_symmetry_is_special_to_metallic():
    rng = np.random.default_rng(0)
    def rnd(n):
        A = rng.standard_normal((n, n)); A /= np.abs(np.linalg.det(A))**(1/n)
        if np.linalg.det(A) < 0: A[0] *= -1
        return A
    ctrl4 = _asym(_spec([rnd(4) for _ in range(250)]))
    assert ctrl4 > 0.3                               # generic SL(4) is asymmetric...
    assert ctrl4 > 10 * _asym(_metallic(4))          # ...unlike the metallic n=4 (symplectic)
