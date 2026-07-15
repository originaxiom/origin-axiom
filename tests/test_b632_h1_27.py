"""B632 cell 1 lock — h^1(M; 27_rho) = 3.

Fast: prereg sealed; banked output asserts the exact verdict; the
decomposition arithmetic. OA_SLOW=1: full exact rerun of cell 1.
"""
import hashlib
import os
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
B632 = os.path.join(HERE, "..", "frontier", "B632_cubic_route")


def test_prereg_sealed():
    h = hashlib.sha256(
        open(os.path.join(B632, "PREREGISTRATION.md"), "rb").read()).hexdigest()
    ledger = open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign",
                               "ARTIFACT_HASHES.txt")).read()
    assert h in ledger


def test_banked_output():
    out = open(os.path.join(B632, "cell1_output.txt")).read()
    assert "27 = V(16) + V(8) + V(0)" in out
    assert "h^0 = 1,  h^1 = 3,  h^2 = 2" in out
    assert "Euler gate PASS" in out
    assert "direct vs blocks: AGREE" in out
    assert "h^1(M; 27_rho) = 3" in out


def test_decomposition_arithmetic():
    spins = [8, 4, 0]
    dims = [2 * s + 1 for s in spins]
    assert sum(dims) == 27 and dims == [17, 9, 1]
    exponents = {1, 4, 5, 7, 8, 11}
    theta_odd = {4, 8}                     # banked (B575/B576)
    assert set(spins) - {0} == theta_odd and theta_odd <= exponents


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="full exact rerun (~3 min, OA_SLOW=1)")
def test_full_rerun():
    r = subprocess.run([sys.executable,
                        os.path.join(B632, "h1_27_generations.py")],
                       capture_output=True, text=True, timeout=1200)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "h^1(M; 27_rho) = 3" in r.stdout
    assert "direct vs blocks: AGREE" in r.stdout
