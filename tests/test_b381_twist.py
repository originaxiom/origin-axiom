"""Locks for B381 — the twist isolation (banked twist_isolation.json)."""

import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B381_twist_isolation")
R = json.load(open(os.path.join(HERE, "twist_isolation.json")))


def test_no_intertwiner_in_natural_family():
    assert R["intertwiners"] == []


def test_commutant_mechanism():
    assert R["par_commutes_canonical"] is True
    assert R["par_commutes_theta"] is False


def test_twist_cocycle_half_characteristic():
    assert R["delta_halfchar"] is True
