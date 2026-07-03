"""Locks for B405."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier",
                    "B405_supersingular_check")


def test_counts_and_supersingular_pair():
    R = json.load(open(os.path.join(HERE, "counts_15a1.json")))
    assert R["7"]["points"] == 8 and R["7"]["supersingular"] is True
    assert R["23"]["points"] == 24 and R["23"]["supersingular"] is True
    for p in ("11", "13", "17", "19"):
        assert R[p]["points"] == 16 and R[p]["supersingular"] is False


def test_sentinel_list():
    S = json.load(open(os.path.join(HERE, "sentinels.json")))
    ss = S["supersingular_below_200"]
    assert ss[:2] == [7, 23] and all(x > 23 for x in ss[2:])
