"""B99 (Probe 1c) -- locking tests: the SL(3) trace-map Jacobian at the geometric rep has 2 eigenvalue-1's
(tangent to V0) + 3 transverse reciprocal pairs including the SL(2) torsion pair (c=5), and is NOT the
trivial-point Dickson tower (pair-sums {-1,3,4})."""
import importlib.util
import pathlib

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b99", _ROOT / "frontier" / "B99_geometric_jacobian_sl3" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_geometric_point_is_fixed():
    c0 = B.geometric_sl3_point()
    assert np.max(np.abs(B._T1sq(c0) - c0)) < 1e-9


def test_geometric_jacobian_is_torsion_type_not_tower():
    """2 eigenvalue-1's + 3 reciprocal pairs; one pair sum is c=5 (the SL(2) torsion pair); the pair-sums
    are NOT the trivial-point Dickson tower sums {-1,3,4}."""
    n1, sums = B.reciprocal_pair_sums()
    assert n1 == 2                                          # tangent to the 2-dim V0
    assert len(sums) == 3                                  # 3 transverse reciprocal pairs
    assert any(abs(c - 5) < 1e-3 for c in sums)            # the SL(2) torsion pair (c=5) appears
    # NOT the tower: the tower pair-sums are real {-1, 3, 4}; here two pair-sums are non-real (complex)
    assert sum(1 for c in sums if abs(c.imag) > 1e-3) == 2
    tower = {-1, 3, 4}
    assert not all(any(abs(c - tw) < 1e-3 for tw in tower) for c in sums)
