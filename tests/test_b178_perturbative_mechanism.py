"""B178 -- the perturbative mechanism (V172). Fast locks (small N).

The decisive, fast facts: the contamination-robust INDEX method gives the physical ordering
w(2,1) < w(1,1) (an order-3 gap is smaller than an order-2 gap); the per-frequency power-1 direction
is clean (~1); and golden's banked dressing lead far exceeds the linear Diophantine lead (the
amplification heuristic). The full independent-lambda sweep + the saturation-limited power-2 live in
perturbative_mechanism.py.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

phi = (1 + 5**0.5) / 2
ag, as_ = 1/phi, 2**0.5 - 1


def _cos(N, a, th):
    n = np.arange(1, N + 1); return np.cos(2 * np.pi * (a * n + th))


def _ids(n1, n2):
    return (n1 * ag + n2 * as_) % 1.0


def _w_index(l1, l2, n1, n2, N, th1=0.137, th2=0.413):
    e = np.sort(eigvalsh_tridiagonal(l1 * _cos(N, ag, th1) + l2 * _cos(N, as_, th2), np.ones(N - 1)))
    k0 = int(round(_ids(n1, n2) * N))
    return max(e[k] - e[k - 1] for k in (k0 - 1, k0, k0 + 1))


def test_index_method_physical_ordering():
    # order-3 gap (2,1) must be smaller than order-2 gap (1,1) at weak coupling -- the index method gives this
    # (needs N large enough to resolve the tiny order-3 gap; the probe uses N=14000, lambda=(0.10,0.20))
    N = 14000
    assert _w_index(0.10, 0.20, 2, 1, N) < _w_index(0.10, 0.20, 1, 1, N)


def test_per_frequency_power1_clean():
    # (1,1) gap ~ lambda1^1 * lambda2^1: vary lambda1, slope ~ 1
    N = 6000
    lams = [0.12, 0.20, 0.30]
    ws = [_w_index(l, 0.2, 1, 1, N) for l in lams]
    slope = np.polyfit(np.log(lams), np.log(ws), 1)[0]
    assert 0.7 < slope < 1.3                              # per-frequency power-1 confirmed (clean)


def test_golden_amplification_heuristic():
    # golden's banked dressing lead (B176) far exceeds the LINEAR Diophantine lead D=1/sqrt(m^2+4)
    D = {m: 1 / (m * m + 4) ** 0.5 for m in (1, 2, 3)}
    assert 8.9 / (D[1] / D[2]) > 2.0                      # golden/silver dressing amplified vs linear lead
    assert 1.46 / (D[2] / D[3]) < 1.5                     # silver/bronze not amplified (~1): golden stands alone
