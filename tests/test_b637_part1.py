"""B637 part 1 lock — the dimension table."""
import hashlib
import os
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "frontier", "B637_corrected_cell3")


def test_prereg_sealed():
    h = hashlib.sha256(open(os.path.join(
        B637, "PREREGISTRATION.md"), "rb").read()).hexdigest()
    ledger = open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign",
                               "ARTIFACT_HASHES.txt")).read()
    assert h in ledger


def test_banked_table():
    out = open(os.path.join(B637, "part1_output.txt")).read()
    assert "control (trivial coefficients): h0 = 1, h1 = 1" in out
    for line in ("none: h0 = 1, h1(D;27) = 5", "m=4: h0 = 0, h1(D;27) = 2",
                 "m=8: h0 = 0, h1(D;27) = 2", "m=11: h0 = 1, h1(D;27) = 5"):
        assert line in out, line
    assert "ALL PREDICTIONS CONFIRMED" in out
    assert "mu-match True, lambda-inversion True" in out


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="full exact rerun (~6 min)")
def test_full_rerun():
    r = subprocess.run([sys.executable,
                        os.path.join(B637, "b637_dimension_table.py")],
                       capture_output=True, text=True, timeout=3600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "ALL PREDICTIONS CONFIRMED" in r.stdout


def test_banked_part2a():
    out = open(os.path.join(B637, "part2a_output.txt")).read()
    assert out.count("mu-gate True, lambda-gate True") == 4
    assert out.count("VERDICT: COMPATIBLE") == 4
    assert out.count("h1(D;27) = 5") == 4
    assert out.count("trivial control: h0 = 1, b1(D_phi) = 1") == 4
