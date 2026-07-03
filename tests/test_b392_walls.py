"""Locks for B392 -- the wall probes."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B392_wall_probes")


def test_p_dynamics_no_match():
    R = json.load(open(os.path.join(HERE, "p_dynamics.json")))
    assert R["match"] is False
    assert R["ours"] == ["3/10", "7/10"] and len(R["tim"]) == 6


def test_p_scale_frozen_quarter_twisted_support():
    R = json.load(open(os.path.join(HERE, "p_scale_135.json")))
    assert len(R) == 2
    for p, cells in R.items():
        assert sorted(map(int, cells)) == [29, 74, 119, 164]
        assert all(v == "1/4" for v in cells.values())
