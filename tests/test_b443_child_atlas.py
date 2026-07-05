"""Lock for B443 (C6) — the Child Atlas verdict: no bar cleared, nothing figure-eight-unique."""
import os, sys
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B443_child_atlas")
sys.path.insert(0, HERE)
import child_atlas as A


def test_no_emergence_bar_cleared():
    assert A.any_bar_cleared() == []            # exact-SM leg fails at every floor


def test_verdict_falsified():
    v = A.verdict()
    assert v["bars_cleared"] == 0
    assert v["figure_eight_unique_features"] == 0
    assert v["hypothesis_status"].startswith("FALSIFIED")


def test_all_floors_present():
    waves = {f["wave"] for f in A.FLOORS}
    assert {"C0", "C1", "C2", "B438", "C3", "C4", "C5"} <= waves
