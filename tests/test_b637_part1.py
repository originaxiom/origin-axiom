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


def test_part2b_honest_partial():
    out1 = open(os.path.join(B637, "part2b_stage1_output.txt")).read()
    assert "deltaS=omega on [lam|mu|b] (certificate path): True" in out1
    out2 = open(os.path.join(B637, "part2b_stage2_output.txt")).read()
    assert "G-A coboundary invariance, slot 0: False" in out2
    assert "CLASS-LEVEL GATES FAILED" in out2
    fnd = open(os.path.join(B637, "FINDINGS.md")).read()
    assert "QUARANTINED" in fnd


def test_part2b_resolved():
    out = open(os.path.join(B637, "part2b_stage2_fixed_output.txt")).read()
    for g in ("G-A coboundary invariance, slot 0: True",
              "G-A coboundary invariance, slot 1: True",
              "G-A coboundary invariance, slot 2: True",
              "G-B antisymmetry (01 swap -> -Y): True",
              "G-B antisymmetry (12 swap -> -Y): True",
              "G-C section independence (sig(mu lam) = LONG+a): True",
              "ALL CLASS-LEVEL GATES PASS"):
        assert g in out, g
    assert "Y[(0, 2, 3)] = (-7983360/13+2661120/13r)" in out
    assert "Y[(1, 2, 3)] = (0+221760/13r)" in out
    assert out.count("nonzero: 6/10") >= 3
    assert "nonzero: 7/10" in out
    src = open(os.path.join(B637, "b637_threeform.py")).read()
    assert "cells.append((pre, ch, ch.lower(), -1))" in src
