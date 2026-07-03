"""Locks for B396 M4 -- the universal formula gate."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B396_allpairs_gate")


def test_zero_mismatches_all_pairs():
    R = json.load(open(os.path.join(HERE, "allpairs_gate.json")))
    assert len(R) == 6
    assert all(v["mismatch"] == 0 for v in R.values())
    assert sum(v["match"] for v in R.values()) == 661
