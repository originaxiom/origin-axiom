"""B357 -- the E6 boundary restriction: rank 6/6, Lagrangian certified, the universal-tau identity."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B357_e6_boundary_restriction'))
import mpmath as mp
from boundary_restriction import (
    EXPONENTS, CUSP_SHAPE, peripheral_gates, restriction, tau_identity, omega_on_h1,
)


def test_peripheral_gates():
    assert peripheral_gates()                       # mu, lam commute; both parabolic tr=-2


def test_rank_and_tau_fast_blocks():
    for m in (1, 4):
        r = restriction(m)
        assert r["rank"] == 1 and r["resid"] < mp.mpf(10) ** -30
        assert abs(r["phi_mu"]) > mp.mpf(10) ** -18          # opens the cusp at leading order
        t, dev = tau_identity(m)
        assert dev < mp.mpf(10) ** -40
        assert abs(abs(t) - abs(CUSP_SHAPE)) < mp.mpf(10) ** -40   # |tau| = 2*sqrt(3) (sign = orientation)
        M = omega_on_h1(m)
        det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
        assert abs(det) > mp.mpf(10) ** -10                  # MB12: ambient form nondegenerate
        assert abs(M[0, 1] + M[1, 0]) < mp.mpf(10) ** -40    # antisymmetry on the honest basis


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="all six blocks ~minutes; banked verdict asserted under OA_SLOW=1")
def test_all_six_blocks_slow():
    taus = []
    total = 0
    for m in EXPONENTS:
        r = restriction(m)
        total += r["rank"]
        t, dev = tau_identity(m)
        assert dev < mp.mpf(10) ** -20
        taus.append(t)
    assert total == 6                                        # Lagrangian certified (rank 6/6)
    assert max(abs(t - taus[0]) for t in taus) < mp.mpf(10) ** -20   # tau uniform across exponents
