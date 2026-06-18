"""B176 -- the golden privilege, with controls (V170). Fast locks (single theta, small N).

The decisive facts: golden(m=1) is the Hurwitz-extremal most-irrational metallic mean; in the woven
cosine chain the golden satellite ladder strongly dominates the silver one (golden privilege); but the
ordering does NOT continue -- silver and bronze ladders are comparable (golden stands alone, not a
monotone irrationality order). The theta-averaged 2-model sweep lives in golden_privilege.py.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

phi = (1 + 5**0.5) / 2
A = {'golden': 1/phi, 'silver': 2**0.5 - 1, 'bronze': (13**0.5 - 3)/2}


def _cos(N, a, th):
    n = np.arange(1, N + 1); return np.cos(2 * np.pi * (a * n + th))


def _wat(a1, a2, t, N, th1=0.137, th2=0.413, lam=1.0):
    V = lam * _cos(N, a1, th1) + lam * _cos(N, a2, th2)
    e = np.sort(eigvalsh_tridiagonal(V, np.ones(N - 1)))
    d = np.diff(e); ids = np.arange(1, N) / N
    m = np.abs(ids - (t % 1.0)) < 0.003
    return d[m].max() if m.any() else 0.0


def _ladders(aA, aB, N):
    As = sum(_wat(aA, aB, (1 + k) * aA + k * aB, N) for k in (1, 2, 3))
    Bs = sum(_wat(aA, aB, k * aA + (1 + k) * aB, N) for k in (1, 2, 3))
    return As, Bs


def test_hurwitz_irrationality_ordering():
    h = [1 / (m * m + 4) ** 0.5 for m in (1, 2, 3)]      # golden, silver, bronze
    assert h[0] > h[1] > h[2]                             # golden most irrational (1/sqrt5)


def test_golden_dominates_silver():
    As, Bs = _ladders(A['golden'], A['silver'], 6000)
    assert As / max(Bs, 1e-9) > 2.0                      # golden satellite ladder dominates -> golden privileged


def test_ordering_breaks_below_golden():
    As, Bs = _ladders(A['silver'], A['bronze'], 6000)
    assert 0.4 < As / max(Bs, 1e-9) < 2.5                # silver ~ bronze: comparable, NOT a monotone order
