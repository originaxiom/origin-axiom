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


def test_a1_1215_kill_and_structure():
    R = json.load(open(os.path.join(HERE, "singles_1215.json")))
    assert len(R) == 2
    for p, cells in R.items():
        ks = sorted(map(int, cells))
        assert len(ks) == 24
        assert all(k % 45 == 31 for k in ks)
        assert len(set(cells.values())) == 4


def test_a2_contraction():
    R = json.load(open(os.path.join(HERE, "a2_hierarchy.json")))
    assert R["contraction"] is True
