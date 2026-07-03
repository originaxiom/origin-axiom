"""Locks for B403 -- the prime-filter verdicts."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B403_lead_package")


def test_vacuity_and_refutation():
    R = json.load(open(os.path.join(HERE, "scrutiny.json")))
    assert R["V1_bad_denominators"] == []
    assert R["V1_reps"] == {"p2": 2, "p3": 3, "p5": 5, "p17": 17, "p19": 19}
    assert R["V2_ok"] is True
