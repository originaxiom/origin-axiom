"""Locks for B383 -- the row-16 reality theorem."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B383_row16_reality")
R = json.load(open(os.path.join(HERE, "row16.json")))


def test_theorem_all_b_real_quadratic():
    assert R["T1_ok"] is True
    for b, v in R["row16"].items():
        assert v[2] == "0" and v[3] == "0"


def test_support_values_match_banked():
    assert R["row16"]["0"] == ["1/24", "1/120", "0", "0"]
    assert R["row16"]["4"] == ["5/48", "-1/240", "0", "0"]
    assert R["row16"]["8"] == ["5/48", "-1/240", "0", "0"]


def test_row4_bright_contrast():
    assert R["row4_bright"] == {"4": ["0", "-1/40", "1/48", "-1/48"],
                                "8": ["0", "-1/40", "-1/48", "1/48"]}


def test_mechanism_class_vector_nonzero_but_killed():
    cl = R["T2_classes"]["4"]
    assert any(x != ["0", "0"] for x in cl)
