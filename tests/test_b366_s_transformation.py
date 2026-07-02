"""Locks for B366 part 2 — the derived level-15 S-transformation formulas."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B366_invariant_spin_sector"))

from s_transformation import TAU, sq_S_pair, tri_S_pair, twist_shift_pair

K = 60
Z1, Z2 = 0.17 + 0.05j, -0.23 + 0.11j


def test_triangular_s_closure_exact_formula():
    """The seam-bearing class closes onto itself at fixed tau (z + (tau+1)/30)."""
    for j in (0, 8):
        for z in (Z1, Z2):
            lhs, rhs = tri_S_pair(j, z, TAU, K)
            assert abs(lhs - rhs) / abs(lhs) < 1e-8


def test_square_s_image_at_quarter_tau():
    """The canonical class exits: its S-image lives at (z/2, tau/4)."""
    for j in (4, 12):
        for z in (Z1, Z2):
            lhs, rhs = sq_S_pair(j, z, TAU, K)
            assert abs(lhs - rhs) / abs(lhs) < 1e-6


def test_sign_twist_is_a_real_shift():
    """ftw_r(z) = e(-r/30) f_r(z + 1/30): the twist collapses to a 1/30 shift."""
    for r in (0, 5, 13):
        a, b = twist_shift_pair(r, Z1, TAU, K)
        assert abs(a - b) / abs(a) < 1e-12
