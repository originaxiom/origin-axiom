"""B344 -- the deviation space's forced reciprocal (symplectic) pairing. sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B344_deviation_symplectic_pairing'))
import sympy as sp
from deviation_symplectic_pairing import det_is_one, reciprocal_pair_at_fixed_point, kappa_is_casimir


def test_trace_map_is_volume_preserving():
    assert all(det_is_one(m) for m in (1, 2, 3))        # det(d phi_m) = 1


def test_forced_reciprocal_pairing_and_casimir():
    has_unit, prod = reciprocal_pair_at_fixed_point()
    assert has_unit and prod == 1                        # modes {1, L, 1/L}: reciprocal pair
    assert kappa_is_casimir()                            # kappa = un-paired central direction (scale door)
