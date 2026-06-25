"""B207 -- golden shadow's breaking lattice + the metallic scale-spectrum (firewall-clean MATH).
Finite-group structure + dimensionless invariants only; NO physics; nothing to CLAIMS.md."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B207_golden_breaking_and_scale"))
from golden_breaking import summary as gb  # noqa: E402
from scale_spectrum import hierarchy_diagnostics, regulator, spectrum  # noqa: E402


def test_golden_breaking_lattice():
    s = gb()
    assert s["order_2I"] == 120
    assert s["RL_order"] == 10 and s["RL_cyclic_order"] == 10
    assert s["normalizer_order"] == 20            # residual = dicyclic 2D5
    assert s["contains_2T_E6"] is True            # 2I > 2T (E6)
    assert s["contains_2O_E7"] is False           # 2I does NOT contain 2O (E7) -- skips E7


def test_scale_spectrum_no_intrinsic_hierarchy():
    h = hierarchy_diagnostics()
    # regulator grows ~ log m (slope ~1), consecutive ratio -> 1, max/min O(1): NO exp hierarchy
    assert 0.7 < h["reg_vs_logm_slope"] < 1.2
    assert h["max_over_min_ratio"] < 10
    # golden has the smallest regulator
    assert min(r["reg"] for r in spectrum()) == regulator(1)


if __name__ == "__main__":
    test_golden_breaking_lattice()
    test_scale_spectrum_no_intrinsic_hierarchy()
    print("ALL CHECKS PASS")
