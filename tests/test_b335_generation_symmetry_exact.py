"""B335 -- the generation Z/3 is an exact isometry (mass degeneracy = theorem). Recorded values; sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B335_generation_symmetry_exact'))
from generation_symmetry_exact import (volume_ratio_is_three, geodesic_multiplicities,
                                       cusp_shape_modulus_squared, cover_group_is_not_2T)


def test_generation_cover_is_isometric_threefold():
    assert volume_ratio_is_three() == 3.0            # deck is an isometry: exact 3x volume
    assert geodesic_multiplicities() == (3, 3)       # three isometric sheets -> real invariants degenerate


def test_cusp_shape_modulus_is_coxeter_number():
    assert cusp_shape_modulus_squared() == 12        # |2 sqrt3|^2 = 12 = h(E6) (B302)


def test_order24_cover_group_is_not_2T():
    # verify-don't-trust on this seat's own hope: order-24 coincidence != E6 McKay group
    assert cover_group_is_not_2T()                   # ab (Z/2)^2 != 2T's Z/3
