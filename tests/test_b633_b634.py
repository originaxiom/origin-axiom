"""Locks: B633 (B615-R integration) + B634 G1 (conductor identities)."""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
B633 = os.path.join(HERE, "..", "frontier", "B633_b615r_integration")


def test_b633_seal_hashes():
    seal = open(os.path.join(B633, "SEAL.txt")).read()
    for f in ("DESIGN.md", "run_b615r.py"):
        h = hashlib.sha256(open(os.path.join(B633, f), "rb").read()).hexdigest()
        assert h in seal, f


def test_b633_headline_reproduces():
    r = subprocess.run([sys.executable, os.path.join(B633, "run_b615r.py")],
                       capture_output=True, text=True, timeout=300)
    assert r.returncode == 0
    assert "p_final = 0.1450 -> VERDICT A" in r.stdout
    assert "c2 (octant) p = 0.3152; c3 (scheme) p = 0.1450" in r.stdout


def test_b634_g1():
    r = subprocess.run([sys.executable, os.path.join(
        HERE, "..", "frontier", "B634_conductor_chord",
        "g1_conductor_identities.py")], capture_output=True, text=True,
        timeout=120)
    assert r.returncode == 0 and "G1 PASS" in r.stdout
