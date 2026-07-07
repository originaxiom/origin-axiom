"""Lock for B463 — the principal centralizer (exact) + the SU(6) control gate."""
import os
import subprocess
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B463_relation_r4_centralizer")


def test_centralizer():
    out = subprocess.run([sys.executable, "centralizer.py"], cwd=HERE,
                         capture_output=True, text=True, timeout=900).stdout
    assert "CONTROL (long-root A1): dim C = 35" in out
    assert "dim C_e6(principal) = 0" in out
    assert "[2, 8, 10, 14, 16, 22]" in out
    assert "ALL CHECKS PASS" in out
