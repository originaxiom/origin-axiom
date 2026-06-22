"""B192 -- SL(n>=3) higher-rank Lyapunov spectra (V185; CORRECTED 2026-06-23). Fast locks.

The original "parity law" (symmetric iff n even, special to metallic, realizing V29) is REFUTED: it was an
artifact of cherry-picked energies + a rigged dense-Gaussian control. On a fair broad energy grid the pattern
inverts (n=4 asymmetric, n=3 symmetric, n=6 not symmetric), and a random potential in the same companion matches
metallic -- so the approximate +-symmetry is a generic reciprocal-pair transfer-matrix property, not a law and not
metallic-special. Only D1 (sum=0) + B166's exact V29 obstruction survive. Full version in sln_higher_rank.py.
"""
import numpy as np

rng = np.random.default_rng(7)
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
def _metallic(n, Es, k=12):
    w = _fib(k)
    return _asym(np.mean([_spec([_Mn(n, E, 1.0 if c == "a" else 0.0) for c in w]) for E in Es], axis=0))


def test_spectrum_sums_to_zero():
    for n in (3, 4, 5):
        g = np.mean([_spec([_Mn(n, E, 1.0 if c == "a" else 0.0) for c in _fib(12)]) for E in (1.3, 2.1, -1.7)], axis=0)
        assert abs(g.sum()) < 1e-9                  # D1: SL(n), det=1


def test_parity_law_refuted_energy_artifact():
    cherry = [1.3, 2.1, -1.7]; fair = list(np.linspace(-3.5, 3.5, 15))
    # the "even-symmetric" n=4 at cherry energies INVERTS on a fair grid -> no parity law
    assert _metallic(4, cherry) < 0.02          # cherry: looks symmetric
    assert _metallic(4, fair) > 0.2             # fair: asymmetric (inverts)
    assert _metallic(6, fair) > 0.2             # n=6 (even) NOT symmetric on the fair grid


def test_symmetry_not_special_to_metallic():
    fair = list(np.linspace(-3.5, 3.5, 15)); L = 500
    V = rng.uniform(0, 1.0, L)
    randpot4 = _asym(np.mean([_spec([_Mn(4, E, v) for v in V]) for E in fair], axis=0))
    assert abs(randpot4 - _metallic(4, fair)) < 0.06   # random potential matches metallic -> not special
