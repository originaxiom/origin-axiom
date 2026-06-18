"""B171 -- the heterogeneous metallic quasicrystal (Phase 0; V165). Fast locks.

The decisive Phase-0 facts: (B3) the rank-3 gap-label set is DENSE -> chance-hit rises with
label-sum, so only small labels are credible; (B4) the cross-session '0.611 combination gap'
is at the LARGE label (3,-3) (sum 6), hence not statistically credible; and a small woven chain
INHERITS a golden +-1 ladder gap (the 'bilingual' baseline). The full N=8000 sweep lives in
het_quasicrystal.py (too heavy for the suite).
"""
import numpy as np


def _alpha(m):
    return 1.0 / ((m + (m * m + 4) ** 0.5) / 2)


def _labels(ag, as_, L):
    return np.array(sorted({(n1 * ag + n2 * as_) % 1.0
                            for n1 in range(-L - 1, L + 2)
                            for n2 in range(-L - 1, L + 2)
                            if 0 < abs(n1) + abs(n2) <= L}))


def _null(ag, as_, L, tol=1.2e-3, R=60000, seed=0):
    v = _labels(ag, as_, L)
    x = np.random.default_rng(seed).uniform(0, 1, R)
    j = np.searchsorted(v, x) % len(v)
    d1 = np.abs(x - v[j]); d2 = np.abs(x - v[(j - 1) % len(v)])
    dd = np.minimum(np.minimum(d1, d2), 1 - np.maximum(d1, d2))
    return (dd < tol).mean()


def test_density_trap_null_rises_with_label_sum():
    ag, as_ = _alpha(1), _alpha(2)
    rates = [_null(ag, as_, L) for L in (1, 2, 3, 4, 6)]
    assert all(b > a for a, b in zip(rates, rates[1:]))   # monotone increasing => density trap real
    assert rates[2] < 0.07 and rates[4] > 0.15            # sum<=3 low-null window; sum<=6 dense


def test_combination_0611_is_genuinely_large_label():
    ag, as_ = _alpha(1), _alpha(2)
    comb = (3 * ag - 3 * as_) % 1.0                       # the (3,-3) value ~ 0.611457
    assert abs(comb - 0.611457) < 1e-5
    # resolvably distinct from any SMALL label (nearest is golden (1,0)=0.618, ~6.6e-3 away,
    # >> finite-size resolution ~1.2e-3) => a genuinely large-sum (=6) label, hence not null-credible
    small = _labels(ag, as_, 3)
    d = np.min(np.minimum(np.abs(small - comb), 1 - np.abs(small - comb)))
    assert d > 3e-3                                       # not a mislabeled small-label value
    assert _null(ag, as_, 6) > 3 * _null(ag, as_, 2)     # sum-6 deep in the density floor (uncertified)


def test_small_woven_chain_inherits_a_golden_ladder_gap():
    ag, as_, lam, th, N = _alpha(1), _alpha(2), 1.5, 0.1357, 1400
    def V(a, theta):
        n = np.arange(1, N + 1)
        return (((n * a + theta) % 1.0) >= 1.0 - a).astype(float)
    Vw = lam * V(ag, th) + lam * V(as_, th + 0.27)
    H = np.diag(Vw) + np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)
    e = np.sort(np.linalg.eigvalsh(H))
    d = np.diff(e); i = int(np.argmax(d)); ids = (i + 1) / N
    # the single widest gap sits at a golden +-1 ladder label (IDS ~ 0.382 or 0.618)
    assert min(abs(ids - 0.381966), abs(ids - 0.618034)) < 5e-3
