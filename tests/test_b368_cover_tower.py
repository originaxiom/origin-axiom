"""Locks for B368 — the cover tower (banked cover_tower.json)."""

import json
import os
from fractions import Fraction as Fr

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B368_cover_tower")
REPORT = json.load(open(os.path.join(HERE, "cover_tower.json")))
B367 = os.path.join(os.path.dirname(__file__), "..", "frontier", "B367_value_map")


def test_deck_identity_and_order():
    assert REPORT["deck_identity_exact"] is True
    assert REPORT["cover_order"] == 20


def test_cover_exponent_list():
    assert REPORT["cover_exponents"] == [0, 2, 3, 5, 7, 8, 12, 13, 15, 17, 18]
    K1 = [0, 1, 4, 5, 6, 9, 11, 14, 15, 16, 19]
    assert sorted((3 * a) % 20 for a in K1) == REPORT["cover_exponents"]


def test_tower_singles_clean():
    assert all(REPORT["tower_singles_clean_k2_k5"][k] for k in ("2", "3", "4", "5"))


def test_trace18_twins_differ_at_seam():
    cover = {Fr(v) for v in REPORT["cover_pair_svals"]}
    seed4 = {Fr(v) for v in REPORT["seed4_pair_svals"]}
    assert seed4 == {Fr(s, d) for d in (120, 240, 480) for s in (1, -1)}
    assert cover == {Fr(s, d) for d in (48, 60, 80, 120, 160, 240, 480) for s in (1, -1)}
    assert cover != seed4
    # the cover's value multiset is the base pair's (deck relabeling preserves values)
    base = json.load(open(os.path.join(B367, "step0_tables.json")))["1,2"]
    base_sv = {Fr(v[3]) for v in base.values() if Fr(v[3]) != 0}
    assert cover == base_sv
