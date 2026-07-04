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
