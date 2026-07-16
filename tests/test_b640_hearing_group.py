"""B640 lock — the hearing-group theorem."""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B640 = os.path.join(HERE, "..", "frontier", "B640_hearing_group")


def test_prereg_sealed():
    h = hashlib.sha256(open(os.path.join(
        B640, "PREREGISTRATION.md"), "rb").read()).hexdigest()
    led = open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign",
                            "ARTIFACT_HASHES.txt")).read()
    assert h in led


def test_banked_verification():
    out = open(os.path.join(B640, "b640_output.txt")).read()
    assert "|im rho| = 360" in out
    assert "|ker det| = 120" in out
    assert "{1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24}" in out
    assert "unique involution: True" in out
    assert "9 classes, sizes [1, 1, 12, 12, 12, 12, 20, 20, 30]" in out
    assert "unidentified 0" in out
    assert "tr = -1/phi: True" in out
    assert "ord(rho(RL))   = 10" in out
    assert "ord(M_odd(RL)) = 5" in out
    assert "ord(W(RL)) on the FULL 6-dim stage = 20" in out
    assert "scalar-symmetric-part law failures: 232/360" in out
    assert out.count("tone-zero True") == 3
