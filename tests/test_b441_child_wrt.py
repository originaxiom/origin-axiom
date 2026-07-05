"""Locks for B441 (C5) — the WRT surgery tool's two validations (the prereg-gate)."""
import os, sys
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B441_child_wrt")
sys.path.insert(0, HERE)
import wrt as W


def test_wrt_tool_validated():
    ok_s3, ok_amphi = W.validate(dps=40)
    assert ok_s3      # tau_r(S^3) = 1 via +1 surgery on the unknot
    assert ok_amphi   # amphichirality: tau_r(4_1(5,1)) = conj tau_r(4_1(-5,1))
