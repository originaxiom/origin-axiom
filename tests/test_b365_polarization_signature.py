"""B365 -- the half-period vanishing signature discriminates the polarizations."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B365_polarization_signature'))
from s_side import fam, E_tri, E_sq, TAU


def _min_over_j(E, z0):
    return min(abs(fam(j, z0, TAU, E)) for j in range(15))


def test_triangular_vanishes_exactly_at_one_half_period():
    assert _min_over_j(E_tri, 0.5) < 1e-15                 # the exact zero (odd-theta signature)
    assert _min_over_j(E_tri, 0) > 1e-7                    # genuinely nonzero elsewhere
    assert _min_over_j(E_tri, TAU / 2) > 1e-1
    assert _min_over_j(E_tri, (1 + TAU) / 2) > 1e-1


def test_square_vanishes_at_all_four_half_periods():
    for z0 in (0, 0.5, TAU / 2, (1 + TAU) / 2):
        assert _min_over_j(E_sq, z0) < 1e-6
