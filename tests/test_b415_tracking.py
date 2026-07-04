"""Locks for B415 T1 -- the tracked destination + the registered bar."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B415_behavior_tracking")


def test_destination_named_no_emergence():
    R = json.load(open(os.path.join(HERE, "t1_continuum.json")))
    assert R["bar"]["any_exact_SM_match"] is False
    assert "Haar" in R["characterization"]
