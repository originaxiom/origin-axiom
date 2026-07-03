"""Locks for B377 — the derived existence law (banked census JSONs)."""

import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B377_existence_law_derivation")
LOCAL = json.load(open(os.path.join(HERE, "local_censuses.json")))
FULL = json.load(open(os.path.join(HERE, "full_census_225.json")))


def test_local_table_v2_law():
    assert LOCAL["3,u1"]["lines"] == [0] and LOCAL["3,u1"]["doublet_deg"] == [90.0]
    assert LOCAL["5,u1"]["lines"] == [] and LOCAL["5,u1"]["doublet_deg"] == [36.0]
    assert LOCAL["5,u2"]["lines"] == [] and LOCAL["5,u2"]["doublet_deg"] == [108.0]
    assert LOCAL["9,u1"]["doublets"] == [] and LOCAL["9,u1"]["lines"] == [0]
    assert LOCAL["25,u1"]["doublets"] == [] and LOCAL["25,u1"]["lines"] == [0]
    assert LOCAL["27,u1"]["doublet_deg"] == [90.0] and LOCAL["27,u1"]["lines"] == [0]
    assert LOCAL["81,u1"]["doublets"] == [] and LOCAL["81,u1"]["lines"] == [0]
    assert LOCAL["125,u1"]["lines"] == [] and LOCAL["125,u1"]["doublet_deg"] == [36.0]


def test_225_death_census_confirmed():
    assert FULL["hits"] == []
