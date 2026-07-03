"""Locks for B400 W-B1 -- the canonical-frame kill."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B400_canonical_frame")


def test_mercedes_exact_and_golden_line_orthogonal():
    R = json.load(open(os.path.join(HERE, "canonical_frame.json")))
    assert R["mercedes"] is True and R["kernel_zero"] is True
    assert R["inner"] == "-1/1152" and R["g6"]["norm2"] == "1/1152"
    for g in ("g6", "g14"):
        assert R["rel"][g]["onto_e1"] == "0" and R["rel"][g]["onto_e2"] == "0"
