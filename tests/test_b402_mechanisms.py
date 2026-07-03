"""Locks for B402 Q1."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier",
                    "B402_stripped_mechanisms")


def test_q1_seed_split():
    R = json.load(open(os.path.join(HERE, "q1_single_reality.json")))
    assert R["m1"]["real_cells"] == 20 and R["m1"]["imag_cells"] == 0
    assert R["m2"]["real_cells"] == 8 and R["m2"]["imag_cells"] == 4
    imag_j = sorted(x[0] for x in R["m2"]["examples"])
    assert imag_j == [1, 5, 7, 11]
