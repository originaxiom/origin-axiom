"""Locks for B418 TW4 -- emergence is intrinsic (mirror not local upstairs)."""
import json
import os
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B418_tw4_upstairs")
def test_mirror_not_local_upstairs():
    R = json.load(open(os.path.join(HERE, "track_upstairs.json")))
    assert R["mirror_upstairs_galois"] == []
    assert R["support"] == 49
    assert R["bar"]["any_exact_SM_match"] is False
