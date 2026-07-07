"""Lock for B457 — Ethogram EZ: the gates run on the verified freeze; H0a."""
import os
import subprocess
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B457_ethogram_ez_verdict")


def test_gates_verdict():
    out = subprocess.run([sys.executable, "gates.py"], cwd=HERE,
                         capture_output=True, text=True, timeout=600).stdout
    assert "freeze verified" in out
    assert "FIRES: False" in out
    assert "H1: NO" in out
    assert "H0a EARNED" in out
