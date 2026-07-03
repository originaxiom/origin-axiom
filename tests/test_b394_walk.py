"""Locks for B394 M2 -- the 405 rung and the unified singles law."""
import json
import os
from fractions import Fraction as Fr

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B394_support_walk")
R = json.load(open(os.path.join(HERE, "singles_405.json")))


def test_support_31_mod_45_twelve_cells():
    for p, cells in R.items():
        assert sorted(map(int, cells)) == [31 + 45*k for k in range(12)]


def test_registered_candidates_killed():
    for p, cells in R.items():
        assert "59" not in cells and "86" not in cells


def test_triple_is_one_plus_c_over_12():
    T = json.load(open(os.path.join(HERE, "triple.json")))
    assert T["xyz"] == ["1/12", "-1/12", "-1/12"]


def test_values_not_rational_quarter():
    for p, cells in R.items():
        assert all(v.startswith("other") for v in cells.values())
