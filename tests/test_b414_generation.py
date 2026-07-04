"""Locks for B414 -- the honest census verdict."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B414_generation_structure")


def test_core_multiplicity_is_Z2_not_Z3():
    R = json.load(open(os.path.join(HERE, "census.json")))
    assert R["core_Z2"] == 2 and R["core_Z3"] == 0
    assert R["Z3_privileged"] is False
