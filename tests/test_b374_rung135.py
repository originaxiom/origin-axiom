"""Locks for B374 — the level-135 rung (banked rung135.json)."""

import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B374_level135_rung")
R = json.load(open(os.path.join(HERE, "rung135.json")))


def test_refutation_of_the_pinned_exponent_law():
    assert R["order_W1"] == 180
    assert R["invariant_sectors"] in ([[54, 126]], [(54, 126)])
    assert R["prediction_hit"] is False            # the registered kill fired


def test_gates():
    assert R["dihedral_global"] is True
    assert R["cross_prime_confirmed"] is True


def test_rung75_quarter_turn():
    r = json.load(open(os.path.join(HERE, "rung75.json")))
    assert r["order"] == 100
    assert r["sectors"] in ([[25, 75]], [(25, 75)])
    assert r["phase_deg_25"] == 90.0
    assert r["cross_prime_confirmed"] is True


def test_rung225_no_sector():
    r = json.load(open(os.path.join(HERE, "rung225.json")))
    assert r["order"] == 300 and r["n_mult1"] == 16
    assert r["sectors"] == []
    assert r["cross_prime_confirmed"] is True
