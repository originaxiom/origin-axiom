"""Locks for B406."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B406_two_conductor")


def test_bridge_pattern_and_mod4():
    B = json.load(open(os.path.join(HERE, "bridge.json")))
    assert B["agree"] == [13, 17, 19, 29]
    assert B["disagree"] == [7, 11, 23, 31, 37, 41, 43]
    assert B["mod2_congruent"] is True
    M = json.load(open(os.path.join(HERE, "mod4_extension.json")))
    assert M["mod4_violations"] == []
    assert M["agree_upto_200"][:4] == [13, 17, 19, 29]
