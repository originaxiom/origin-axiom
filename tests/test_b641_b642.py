"""Locks: B641 (twist-frame law) + B642 (the Galois ear)."""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B641 = os.path.join(HERE, "..", "frontier", "B641_twistframe_law")
B642 = os.path.join(HERE, "..", "frontier", "B642_galois_ear")


def test_preregs_sealed():
    led = open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign",
                            "ARTIFACT_HASHES.txt")).read()
    for d in (B641, B642):
        h = hashlib.sha256(open(os.path.join(
            d, "PREREGISTRATION.md"), "rb").read()).hexdigest()
        assert h in led


def test_b641():
    out = open(os.path.join(B641, "b641_output.txt")).read()
    assert "Cayley-Klein form: 120/120" in out
    assert "law holds at 45+ digits: True" in out
    assert "'1': 6" in out and "'1/2': 120" in out and "'0': 90" in out
    assert "five absolute tones, all identified: True" in out
    assert "twisted strict-law exceptions: 8 (expect 8)" in out
    assert out.count("order=12") == 4
    assert "<|chi|^2> over ker(det) = 1" in out
    assert "mean-square universal tone (det=1) = 0.250000000000000" in out


def test_b642():
    out = open(os.path.join(B642, "b642_output.txt")).read()
    assert "P1: |im rho| = 360" in out
    assert "[1, 1, 12, 12, 12, 12, 20, 20, 30]" in out
    assert "P3: = +phi: True" in out
    assert "'phi/2': 72" in out and "'1/(2phi)': 72" in out
