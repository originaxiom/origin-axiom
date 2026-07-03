"""Locks for B389 -- the mirror-mechanism verdicts."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B389_mirror_mechanism")


def test_registered_verdicts():
    R = json.load(open(os.path.join(HERE, "mirror_mechanism.json")))
    assert R["M3"] is True
    assert R["M1"] is False and R["M2"] is False
    assert R["M1_support_closed"] is True


def test_dihedral_twist_blocked():
    D = json.load(open(os.path.join(HERE, "dihedral_check.json")))
    assert D["dihedral_exact"] is False and D["support_mismatch"] == 0
