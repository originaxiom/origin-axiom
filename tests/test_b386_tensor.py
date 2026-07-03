"""Lock for B386 L1 -- the Par-trace tensor identity."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B386_crt_closed_form")


def test_tensor_gate_exact_at_banked_convention():
    R = json.load(open(os.path.join(HERE, "tensor_gate.json")))
    assert R["convention"] == [2, 2] and R["mismatches"] == 0
