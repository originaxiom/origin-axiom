"""Locks for B387 2a/2b -- the level-45 Par-darkness of the value sector."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B387_forced_ratio_ladder")
SW = os.path.join(os.path.dirname(__file__), "..", "frontier", "B372_level45_sweeper")


def test_sector_rows_absent_from_banked_support():
    R = json.load(open(os.path.join(HERE, "extract_45.json")))
    assert R["sector_rows_absent"] == [6, 54]
    assert all(v is None for v in R["cells"].values())


def test_recomputed_from_banked_table():
    pair = json.load(open(os.path.join(SW, "sweep45.json")))["pair"]
    rows = {int(k.split(",")[0]) for k in pair}
    assert 6 not in rows and 54 not in rows


def test_rung135_sector_rows_zero_all_primes():
    R = json.load(open(os.path.join(HERE, "rung135_sector_rows.json")))
    assert len(R) == 3
    for p, cells in R.items():
        assert cells == {"54,2": "zero", "54,10": "zero",
                         "126,2": "zero", "126,10": "zero"}
