"""Locks for B407."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B407_support_nesting")


def test_nesting_census():
    R = json.load(open(os.path.join(HERE, "nesting.json")))
    assert R["1,2"] == dict(both=28, z_only=0, s_only=16,
                            verdict="z-supp SUBSET s-supp")
    assert R["1,3"]["z_only"] == 24 and R["1,3"]["both"] == 0
    assert R["2,4"]["z_only"] == 8 and R["2,4"]["s_only"] == 16
    assert R["1,4"] == dict(both=0, z_only=0, s_only=0, verdict="NO nesting")
