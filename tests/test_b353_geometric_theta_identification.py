"""B353 -- the geometric theta-identification: hyperelliptic involution = theta on the E6 tangent."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B353_geometric_theta_identification'))
import mpmath as mp
import pytest

# E12 (module-level-dps sweep): geometric_theta sets mp.mp.dps=100 at module
# level and computes its import-time chain under that dps itself; restore the
# entry dps after the collection-time import so the assignment cannot leak into
# later-collected modules (the runtime side is covered by the _dps_100 fixture
# below, the original cell-5 repair).
_saved_dps = mp.mp.dps
from geometric_theta import (
    EXPONENTS, SIGN,
    theta_chain_blockscalar_residual, theta_commutes_with_holonomy, hyperelliptic_certificate,
)
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_100():
    # E12 repair (B666 cell 5): these locks compute their residuals at RUNTIME and
    # need the dps=100 that geometric_theta sets at import — but pytest imports every
    # test module at COLLECTION time, so any later-collected module-level dps
    # assignment (e.g. test_cc2_r5_adopted.py, test_b598_p0.py) is what tests
    # actually run under. Per-test fixture sets what this file needs (the b204
    # pattern); the conftest autouse restore alone cannot help, since it restores
    # to the already-leaked entry value.
    saved = mp.mp.dps
    mp.mp.dps = 100
    yield
    mp.mp.dps = saved


def test_theta_is_the_blockscalar_in_the_geometric_basis():
    # S^-1 theta S = (+)_m (-1)^{m+1} Id_{2m+1}, the full 78x78 identity (Schur made exact)
    assert theta_chain_blockscalar_residual() < mp.mpf(10) ** -60


def test_theta_commutes_with_the_holonomy_image():
    # theta fixes the principal SL2 pointwise -> sigma-twisted complex = theta-twisted complex
    assert theta_commutes_with_holonomy() < mp.mpf(10) ** -60


def test_hyperelliptic_action_equals_theta_with_gauge_certificate():
    # J(z0) = (-1)^{m+1} z0 + d0(v): eigenvalue exact, explicit-coboundary residual at the floor
    for m in EXPONENTS:
        lam, resid = hyperelliptic_certificate(m)
        assert abs(lam.imag) < mp.mpf(10) ** -30, (m, lam)
        assert abs(lam.real - SIGN[m]) < mp.mpf(10) ** -30, (m, lam)
        assert resid < mp.mpf(10) ** -40, (m, resid)
