"""B472 — locks: the kappa_q table, the (2,3) closure, the CRT mechanism."""
import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))


def test_kq_verify_all_checks_pass():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "..", "frontier", "B472_quantum_commutator", "kq_verify.py")],
        capture_output=True, text=True, timeout=600)
    assert "ALL CHECKS PASS" in r.stdout
