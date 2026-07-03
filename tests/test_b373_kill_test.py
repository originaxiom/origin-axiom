"""Locks for B373 — the level-45 minimal-sector kill test (banked kill_test.json)."""

import json
import os
from fractions import Fraction as Fr

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B373_level45_minimal_sector")
R = json.load(open(os.path.join(HERE, "kill_test.json")))


def test_unique_invariant_sector_at_pinned_exponent():
    assert R["order_W1"] == 60
    assert R["invariant_sectors"] == [[6, 54]] or R["invariant_sectors"] == [(6, 54)]
    assert R["dihedral_global"] is True


def test_moved_verdict_traces():
    t = R["sector_traces"]["6,54"]
    assert t["A1"][0] == "1/2" and t["A1"][1] == "1/2"          # phi = 2cos36
    assert all(x == "0" for x in t["A1"][2:])
    assert t["A2"][0] == "1" and all(x == "0" for x in t["A2"][1:])
    assert all(x == "0" for x in t["Shat"])                      # helicity pairing
