"""Locks: B638 (the swap mechanism) + B639 (the honest partial)."""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B638 = os.path.join(HERE, "..", "frontier", "B638_swap_decomposition")
B639 = os.path.join(HERE, "..", "frontier", "B639_conjtheta_cubic")


def _ledger():
    return open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign",
                             "ARTIFACT_HASHES.txt")).read()


def test_preregs_sealed():
    led = _ledger()
    for d in (B638, B639):
        h = hashlib.sha256(open(os.path.join(
            d, "PREREGISTRATION.md"), "rb").read()).hexdigest()
        assert h in led


def test_b638_banked():
    out = open(os.path.join(B638, "b638_output.txt")).read()
    # the banked transcript is the run's tail section (the build heads are
    # reproducible; the mathematical content is complete)
    assert "sigma*(rep_i) are cocycles, all 5: True" in out
    assert "sigma*^2 = id mod coboundaries, all 5: True" in out
    assert "sigma*[0] = (1/2+1/2r) 0 0 0 0" in out
    assert "laws: ['plus_conj']" in out
    assert "'plus_conj': 3" in out


def test_b639_banked():
    out1 = open(os.path.join(B639, "b639_output.txt")).read()
    assert "no invertible +lambda intertwiner" in out1
    out2 = open(os.path.join(B639, "b639_stage2_output.txt")).read()
    assert "mu-match False" in out2
    fnd = open(os.path.join(B639, "FINDINGS.md")).read()
    assert "FIXES the holonomy pointwise" in fnd
