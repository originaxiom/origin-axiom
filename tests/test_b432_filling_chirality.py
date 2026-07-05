"""Locks for B432 -- chirality is interface-sourced (31/31 sampled fillings chiral)."""
import json, os
R = json.load(open(os.path.join(os.path.dirname(__file__), "..", "frontier",
                                "B432_filling_chirality", "filling_chirality.json")))
def test_cusped_object_is_amphichiral():
    assert abs(R["cusped_cs"]) < 1e-9              # CS(4_1) = 0: the self-mirror
def test_every_sampled_filling_is_chiral():
    assert R["n"] == 31 and R["n_chiral"] == 31    # external slope breaks the mirror, always
    assert all(r["chiral"] for r in R["rows"])
