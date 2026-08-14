"""B901 locks: the C-stabilizer results."""
import json
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B901_c_stabilizers")


def test_normalizer_equals_centralizer_equals_floor():
    with open(os.path.join(ARC, "normalizer.json")) as f:
        r = json.load(f)
    assert r["dim_normalizer"] == 12
    assert r["dim_centralizer"] == 12


def test_spectral_obstructions():
    with open(os.path.join(ARC, "spectral_obstructions.json")) as f:
        r = json.load(f)
    # the within-plane swap is forbidden: exact spectra differ
    assert r["x8_x16_same_spectrum"] is False
    # sign flips allowed: all nonzero factors even
    assert r["x8_factors_even"] is True
    assert r["x16_factors_even"] is True
