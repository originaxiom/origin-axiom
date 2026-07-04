"""Locks for B408 -- the seam persistence verdict."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B408_seam_hierarchy")


def test_seam_persistence():
    R = json.load(open(os.path.join(HERE, "seam_hierarchy.json")))
    assert R["env15"] == "1/48"
    assert R["verdict"] == "PERSISTENCE"
    assert R["ratio"] > 1.2 and R["ratio"] < 1.25
    assert R["cell"] == "4,8"


def test_scout_void_gate():
    S = json.load(open(os.path.join(HERE, "scout_135.json")))
    assert abs(S["15"] - 1/48) > 1e-6      # the gate failed => scout void (the lock
    # records the FAILURE so no one mistakes scout numbers for verdicts)
