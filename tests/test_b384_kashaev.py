"""Locks for B384 T1 -- exact Kashaev Galois components."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B384_kashaev_bridge")
R = json.load(open(os.path.join(HERE, "kashaev.json")))


def test_n5_exact_golden_value():
    assert R["5"]["rational_part"] == "46" and R["5"]["sqrt5_part"] == "2"


def test_sqrt5_content_at_every_5N_level():
    for N in ("5", "15", "25", "45", "135"):
        assert R[N]["sqrt5_part"] not in (None, "0")


def test_no_sqrt5_subfield_elsewhere():
    for N in ("7", "9", "27", "81"):
        assert R[N]["sqrt5_part"] is None


def test_scaling_gate_decreasing():
    gs = [R[N]["growth"] for N in ("5", "9", "15", "27", "45", "81", "135")]
    assert all(a > b for a, b in zip(gs, gs[1:]))
