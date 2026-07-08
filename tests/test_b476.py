"""B476 — lock: the span dimensions (49 / 5 / 13; no factorization)."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def test_span_dims():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "..", "frontier", "B476_interaction_algebra", "span_verify.py")],
        capture_output=True, text=True, timeout=300)
    assert "ALL CHECKS PASS" in r.stdout
