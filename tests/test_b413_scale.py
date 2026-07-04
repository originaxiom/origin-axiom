"""Locks for B413 -- the Scale-Genesis verdict (flat measure, no scale)."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B413_scale_genesis")


def test_measure_is_flat_no_scale():
    R = json.load(open(os.path.join(HERE, "g1_mellin.json")))
    assert R["trivial"] is False                       # not Haar
    assert abs(R["twelveL1_norm2"] - 9.0) < 1e-9       # |12 L(chi_1)|^2 = 9 (Gauss sum)
    assert abs(R["L1_abs"] - 0.25) < 1e-9              # |L(chi_1)| = mass = 1/4 (flat)
