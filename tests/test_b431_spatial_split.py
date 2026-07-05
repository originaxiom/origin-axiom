"""Locks for B431 -- the seam's spatial split: support confirmed, value-level corrected."""
import json, os
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B431_seam_spatial_split")
R = json.load(open(os.path.join(HERE, "spatial_split.json")))

def test_support_split_and_gating():
    assert (R["active"], R["dark"]) == (120, 120)
    assert R["y0mod3_dark"] is True and R["x0mod10_dark"] is True
    assert R["crt_counts"] == [4, 4] + [14]*8

def test_parity_structure_corrected():
    assert R["parity_preserved"] is True and R["fixed_points"] == 0
    assert R["parity_values_equal"] is False       # conjugate, NOT equal (corrects the claim)

def test_value_orbits_corrected():
    assert R["n_orbits"] == 34                     # not 18
    assert R["orbit_sizes"] == {"2": 24, "4": 2, "8": 8}
