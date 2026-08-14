"""B899 locks: the hierarchy-source check is an earned negative."""
import json
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B899_hierarchy_check")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_exactly_four_registered_comparisons():
    r = _res()
    assert len(r["tests"]) == 4


def test_at_most_one_order_match_and_large_residuals():
    r = _res()
    matches = sum(1 for t in r["tests"].values() if t["order_match"])
    assert matches <= 1          # consistent with chance across 4 tests
    # no comparison achieves a clean power law (residual near 0)
    assert all(t["resid"] > 1.0 for t in r["tests"].values())


def test_frame_root_map_is_the_banked_bijection():
    r = _res()
    assert r["frame_to_root"] == {"0": 2, "1": 0, "2": 1}
