"""Locks for B393 M1 session 1 -- termwise s-orthogonality."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier",
                    "B393_cancellation_mechanism")
R = json.load(open(os.path.join(HERE, "k1_fullfield.json")))


def test_dark_pairs_termwise_zero():
    assert R["1,3"]["nonzero_terms"] == 0 and R["1,3"]["terms"] == 39
    assert R["3,5"]["nonzero_terms"] == 0 and R["3,5"]["terms"] == 15


def test_bright_controls_have_teeth():
    assert R["3,4"]["nonzero_terms"] == 24
    assert R["2,3"]["nonzero_terms"] == 18
