"""Locks for B399 W-A."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B399_wall_scale")


def test_a3_singles_purely_generic():
    R = json.load(open(os.path.join(HERE, "a3_normalizer.json")))
    for a in ("a1", "a6"):
        assert R[a]["1"] == ["1/4", "0", "0", "0"]
        assert R[a]["3"] == ["0", "0", "0", "0"]
        assert R[a]["5"] == ["0", "0", "0", "0"]
    assert R["class_counts_l0"] == {"1": 5, "3": 5, "5": 10}
