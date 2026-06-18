"""B175 -- the collective spectrum is two-number predictable (V169). Fast locks (small N).

The decisive facts: prominent woven-chain gaps sit at gap-labeling labels n1*a1+n2*a2 (heights exact);
the order-2 (1,1) combination gap width scales as ~lambda^2 at weak coupling (the perturbative width
law); and that gap OPENS in the smooth cosine model but is ~closed in the metallic Sturmian chain
(openings are potential-dependent, heights are not). The full 2-pair sweep lives in collective_predictivity.py.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

phi = (1 + 5**0.5) / 2
ag, as_ = 1/phi, 2**0.5 - 1


def _cos(N, a, th):
    n = np.arange(1, N + 1); return np.cos(2 * np.pi * (a * n + th))


def _sturm(N, a, th):
    n = np.arange(1, N + 1); return (((n * a + th) % 1.0) >= 1.0 - a).astype(float)


def _width_at(Vfun, lam, target, N, th1=0.137, th2=0.413):
    V = lam * Vfun(N, ag, th1) + lam * Vfun(N, as_, th2)
    e = np.sort(eigvalsh_tridiagonal(V, np.ones(N - 1)))
    d = np.diff(e); ids = np.arange(1, N) / N
    m = np.abs(ids - target) < 0.004
    return d[m].max() if m.any() else 0.0


def _label(n1, n2):
    return (n1 * ag + n2 * as_) % 1.0


def test_heights_match_gap_labels():
    N = 4000
    V = 1.0 * _cos(N, ag, 0.137) + 1.0 * _cos(N, as_, 0.413)
    e = np.sort(eigvalsh_tridiagonal(V, np.ones(N - 1))); d = np.diff(e); ids = np.arange(1, N) / N
    errs = []
    for i in np.argsort(d)[::-1][:6]:
        if d[i] > 0.05:
            t = ids[i]
            best = min(min(abs(t - _label(n1, n2)), 1 - abs(t - _label(n1, n2)))
                       for n1 in range(-6, 7) for n2 in range(-6, 7) if abs(n1) + abs(n2) <= 6)
            errs.append(best)
    assert max(errs) < 3e-3                              # every prominent gap is a gap-label


def test_order2_width_law_weak_coupling():
    N = 5000
    lams = [0.12, 0.20, 0.32]
    t = _label(1, 1)                                     # order-2 combination gap
    ws = np.array([_width_at(_cos, lam, t, N) for lam in lams])
    slope = np.polyfit(np.log(lams), np.log(ws), 1)[0]
    assert 1.5 < slope < 2.5                             # width ~ lambda^2 (order = |n1|+|n2| = 2)


def test_ridge_is_cosine_specific_not_sturmian():
    N = 5000
    t = _label(2, 1)
    w_cos = _width_at(_cos, 1.5, t, N)
    w_stu = _width_at(_sturm, 1.5, t, N)
    assert w_cos > 0.05 and w_stu < 0.03                 # opens in cosine, ~closed in metallic Sturmian
