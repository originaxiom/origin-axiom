"""B185 -- the selection/constraint door (V179). Fast locks.

The constraint (gluing) side genuinely SELECTS (continuum -> discrete kappa-fork, B174/B131), unlike
superposition which proliferates (B182) -- but it selects to DISCRETE-FINITE (the fork grows + is
choice-dependent), NOT to a forced-unique value; and the metallic units are 1-cusped, so all-unit
interaction caps at PAIRS (N>=3 needs non-unit connectors = NEEDS-SPECIALIST). Full version in
constraint_selection.py.
"""
import pytest


def _dim_result(cusp_list, n_glue):
    return sum(cusp_list) - 2 * n_glue


def _connected_all_unit_possible(k):
    return 2 * (k - 1) <= k


def test_all_unit_interaction_caps_at_pairs():
    # connected gluing of k 1-cusp units needs 2(k-1) <= k -> k <= 2
    assert _connected_all_unit_possible(2)
    assert not _connected_all_unit_possible(3)
    cap = max(k for k in range(1, 12) if _connected_all_unit_possible(k))
    assert cap == 2


def test_complete_gluing_is_zero_dimensional():
    # dim(result) = sum(cusps) - 2*gluings; closed gluings -> dim 0 (finite fork), open -> still a curve
    assert _dim_result([1, 1], 1) == 0          # a glued pair of units: closed
    assert _dim_result([1, 2, 1], 2) == 0       # unit - 2-cusp connector - unit: closed
    assert _dim_result([2, 2, 2], 3) == 0       # a ring of 2-cusp pieces: closed
    assert _dim_result([1, 2], 1) == 1          # one free cusp left -> a curve
    # physically realizable gluings never over-determine to negative dimension
    for cusps, E in [([1, 1], 1), ([1, 2, 1], 2), ([2, 2, 2], 3), ([1, 2], 1)]:
        assert _dim_result(cusps, E) >= 0


def test_metallic_units_are_one_cusped():
    snappy = pytest.importorskip("snappy")
    for k in ("4_1", "m003", "m004", "m136"):
        assert snappy.Manifold(k).num_cusps() == 1
