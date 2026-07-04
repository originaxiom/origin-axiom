"""Locks for B417 TW3 -- the Sturmian destination."""
import json
import os
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B417_tw3_symbolic")
def test_sturmian_no_sm():
    R = json.load(open(os.path.join(HERE, "track_symbolic.json")))
    assert R["sturmian"] is True and R["topological_entropy"] == 0
    assert R["bar"]["any_exact_SM_match"] is False
