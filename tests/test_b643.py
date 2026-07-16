import hashlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
B643 = os.path.join(HERE, "..", "frontier", "B643_flip_symmetry")
def test_prereg_sealed():
    h = hashlib.sha256(open(os.path.join(B643, "PREREGISTRATION.md"), "rb").read()).hexdigest()
    led = open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign", "ARTIFACT_HASHES.txt")).read()
    assert h in led
def test_obstruction_banked():
    out = open(os.path.join(B643, "b643_output.txt")).read()
    assert "cocycle (J-choice A): False" in out
    assert "cocycle (J-choice B): False" in out
    assert "BANKED OBSTRUCTION" in out
