"""B632 cell 2 lock — the cubic, the vev coupling, the obstruction
gates, and the full antisymmetric Omega.

Fast: prereg sealed; the banked output's gates. OA_SLOW=1: full rerun.
"""
import hashlib
import os
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
B632 = os.path.join(HERE, "..", "frontier", "B632_cubic_route")


def test_cell2_prereg_sealed():
    h = hashlib.sha256(open(os.path.join(
        B632, "CELL2_PREREGISTRATION.md"), "rb").read()).hexdigest()
    ledger = open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign",
                               "ARTIFACT_HASHES.txt")).read()
    assert h in ledger


def test_banked_cell2_output():
    out = open(os.path.join(B632, "cell2_output.txt")).read()
    assert "GATE PASS: the invariant space is EXACTLY 1-dim" in out
    assert "nonzero sorted coefficients: 45/45" in out
    assert "B_C off-block entries all zero: True" in out
    for c in ("c_8", "c_4", "c_0"):
        assert f"{c} (V(" in out
    assert out.count("NONZERO") >= 6          # three c's + three Omega pairs
    assert "spins (8, 4, 0): absent" in out
    assert "spins (8, 0, 0): absent" in out
    assert "spins (4, 0, 0): absent" in out
    assert "diagonal class [z4 cup z4] = (0, 0)" in out
    assert "diagonal class [z8 cup z8] zero: True" in out
    assert "class-level antisymmetry on the three pairs: [True, True, True]" in out
    assert "coboundary control: class invariant True, raw cochain changed True" in out
    assert "Omega(z0, z4) = NONZERO" in out
    assert "Omega(z0, z8) = NONZERO" in out
    assert "Omega(z4, z8) = NONZERO" in out


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="full exact rerun (~4 min, OA_SLOW=1)")
def test_full_rerun():
    r = subprocess.run([sys.executable,
                        os.path.join(B632, "cell2_texture.py")],
                       capture_output=True, text=True, timeout=1800)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "class-level antisymmetry on the three pairs: [True, True, True]" \
        in r.stdout
    assert "B632 cell 2 DONE" in r.stdout
