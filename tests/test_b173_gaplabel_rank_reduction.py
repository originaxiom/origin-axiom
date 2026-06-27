"""B173 -- the gap-labeling reduction (Phase 2; V167). Fast locks.

The arithmetic backbone of the reduction: golden+silver give a rank-3 frequency module (no integer
relation), confirming the L16 formula (distinct fields -> rank 3); the same-field control (golden
m=1 & m=4, both Q(√5)) IS dependent (-1+2α_1-α_4=0) -> rank caps at 2; and the product α_g·α_s is a
genuine 4th direction (theorem-excluded for a 1D single shift). The cited reduction itself lives in
gaplabel_rank.py / FINDINGS.md.
"""
import pytest
from mpmath import pslq, mp, mpf, sqrt


@pytest.fixture(autouse=True)
def _mp_dps():
    """set precision per-test (not at module level) so collection order can't leak a lower global dps."""
    mp.dps = 50


def _alpha(m):
    return 1 / ((mpf(m) + sqrt(m * m + 4)) / 2)


def test_golden_silver_module_is_rank3():
    # no integer relation among 1, 1/φ, √2-1  => rank-3 frequency module
    assert pslq([mpf(1), _alpha(1), _alpha(2)], maxcoeff=10**6, maxsteps=10**4) is None


def test_same_field_caps_at_rank2():
    # golden m=1 and m=4 are BOTH Q(√5) => Q-dependent; PSLQ finds -1 + 2α_1 - α_4 = 0
    rel = pslq([mpf(1), _alpha(1), _alpha(4)], maxcoeff=10**6, maxsteps=10**4)
    assert rel is not None
    assert abs(-1 + 2 * _alpha(1) - _alpha(4)) < mpf('1e-30')


def test_product_is_a_genuine_fourth_direction():
    # α_g·α_s is Q-independent of {1,α_g,α_s}: a product term WOULD give rank 4 (excluded by the 1D theorem)
    ag, as_ = _alpha(1), _alpha(2)
    assert pslq([mpf(1), ag, as_, ag * as_], maxcoeff=10**6, maxsteps=10**4) is None


def test_b172_label_is_rank3_element():
    ag, as_ = _alpha(1), _alpha(2)
    comb = (3 * ag - 3 * as_) % 1                      # (3,-3), both coeffs nonzero
    assert abs(comb - mpf('0.61146128')) < mpf('1e-7')
