"""Locks for B409 Phase 2c -- the transport kill."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier",
                    "B409_stratification_transport")


def test_transport_holds_only_low_multiplicity():
    R = json.load(open(os.path.join(HERE, "transport.json")))
    assert R["all_match"] is False
    for k in ("1,3", "1,4", "2,3", "3,4"):
        assert R[k]["match"] is True
    assert R["1,2"]["match"] is False and R["2,4"]["match"] is False
