"""Locks for B391 -- the 243/625 predictions and the general-statement bases."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B391_existence_general")
R = json.load(open(os.path.join(HERE, "census_big.json")))


def test_243_prediction_hit_both_primes():
    for row in R["243"]:
        assert row["ord"] == 324 and row["line0"] is True
        assert row["doublet"] == [81, 243] and row["doublet_deg"] == 90.0


def test_625_prediction_hit_both_primes():
    for row in R["625"]:
        assert row["ord"] == 1250 and row["line0"] is True
        assert row["doublet"] is None
