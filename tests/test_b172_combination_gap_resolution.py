"""B172 -- the combination gap, resolved (Phase 1; V166). Fast locks.

The decisive Phase-1 facts: the Sturm/pivot count matches the dense solver; the candidate IDS 0.6114613
is NOT any single-frequency (inherited-ladder) value (so a gap there requires BOTH frequencies =
interaction-born); and a small woven chain has a real gap near 0.611 whose IDS is far closer to the
combination label (3,-3) than to any single-frequency label. The full high-N sweep + 3-pair seed-robust
scan live in combination_gap.py.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal


def _alpha(m):
    return 1.0 / ((m + (m * m + 4) ** 0.5) / 2)


def _woven_diag(N, terms):
    n = np.arange(1, N + 1)
    d = np.zeros(N)
    for lam, a, th in terms:
        d += lam * ((((n * a + th) % 1.0) >= 1.0 - a).astype(float))
    return d


def _count_below(d, E):
    q = d[0] - E
    cnt = 1 if q < 0.0 else 0
    for k in range(1, d.shape[0]):
        q = (d[k] - E) - 1.0 / (q if q != 0.0 else -1e-300)
        if q < 0.0:
            cnt += 1
    return cnt


def _nearest_single_freq(ids, a1, a2, nmax=14):
    best = 1.0
    for n in range(1, nmax + 1):
        for v in ((n * a1) % 1.0, (-n * a1) % 1.0, (n * a2) % 1.0, (-n * a2) % 1.0):
            best = min(best, abs(ids - v), 1 - abs(ids - v))
    return best


def test_sturm_count_matches_dense():
    ag, as_ = _alpha(1), _alpha(2)
    d = _woven_diag(400, [(1.5, ag, 0.1357), (1.5, as_, 0.4057)])
    e = np.sort(eigvalsh_tridiagonal(d, np.ones(399)))
    for E in (-1.0, 0.5, 1.7, 3.5):
        assert _count_below(d, E) == int((e < E).sum())


def test_0611_is_a_combination_not_single_frequency():
    ag, as_ = _alpha(1), _alpha(2)
    comb = (3 * ag - 3 * as_) % 1.0                       # (3,-3) = 0.6114613, both coeffs nonzero
    assert abs(comb - 0.6114613) < 1e-6
    # the nearest LOW-order (|n|<=14) single-frequency value is ~3.8e-3 away (silver (0,-13); the prominent
    # golden (1,0) ladder is 6.6e-3) => 0.611 is NOT a low-order ladder value => needs BOTH frequencies.
    # (high-order single-freq labels are dense, so the meaningful comparison is bounded-order, as here.)
    assert _nearest_single_freq(comb, ag, as_, nmax=14) > 3e-3   # interaction-born combination label


def test_woven_chain_has_real_combination_gap_near_0611():
    ag, as_, lam = _alpha(1), _alpha(2), 1.5
    N = 4000
    d = _woven_diag(N, [(lam, ag, 0.1357), (lam, as_, 0.4057)])
    e = np.sort(eigvalsh_tridiagonal(d, np.ones(N - 1)))
    dd = np.diff(e)
    # widest gap with IDS in [0.602, 0.616] (excludes the 0.618 golden ladder gap)
    cand = [(i, (i + 1) / N, dd[i]) for i in range(N - 1) if 0.602 < (i + 1) / N < 0.616 and dd[i] > 0.03]
    i, ids, w = max(cand, key=lambda t: t[2])
    comb = (3 * ag - 3 * as_) % 1.0
    assert w > 0.05                                       # a real, wide gap
    assert abs(ids - comb) < 1e-3                         # IDS at the combination label (3,-3)
    assert abs(ids - comb) < _nearest_single_freq(ids, ag, as_) / 5   # far closer to (3,-3) than any ladder
