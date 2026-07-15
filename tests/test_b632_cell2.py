"""B632 cell 2 lock — REPLACED per the repair adjudication (audit Gate 0):
mathematical gates instead of transcript greps.

Fast: seal/hash integrity (prereg, corrected code, byte-faithful failed
transcripts). OA_SLOW=1: the adopted exhaustive verifier runs (162
coboundary descents, alternating gates, exact rank) and its verdict is
asserted.
"""
import hashlib
import os
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
B632 = os.path.join(HERE, "..", "frontier", "B632_cubic_route")


def _sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def test_cell2_prereg_sealed():
    ledger = open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign",
                               "ARTIFACT_HASHES.txt")).read()
    assert _sha(os.path.join(B632, "CELL2_PREREGISTRATION.md")) in ledger


def test_corrected_code_hashed_posthoc():
    ledger = open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign",
                               "ARTIFACT_HASHES.txt")).read()
    h = _sha(os.path.join(B632, "cell2_texture.py"))
    assert h in ledger, "corrected cell2 code hash missing from ledger"
    line = [ln for ln in ledger.splitlines() if h in ln][0]
    assert "POST-HOC" in line, "the post-hoc label must stay on the code hash"


def test_failed_transcripts_recovered():
    f1 = os.path.join(B632, "FAILED_RUN_1.txt")
    f2 = os.path.join(B632, "FAILED_RUN_2.txt")
    assert _sha(f1) == ("bc517ead74c810edf28bea750f5897f19b081312ccdf3fa0"
                        "b44672c8324072d5")
    t2 = open(f2).read()
    # the failed-gates run's verdicts, preserved verbatim
    assert "class-level antisymmetry on the three pairs: [True, True, False]" in t2
    assert "coboundary control: class invariant False" in t2


def test_adjudication_present():
    adj = open(os.path.join(B632, "REPAIR_ADJUDICATION.md")).read()
    assert "rank 2 with 1-dimensional kernel" in adj
    assert "invariant-section" in adj


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="exhaustive mathematical verification (~3 min)")
def test_exhaustive_verifier():
    r = subprocess.run(
        [sys.executable, os.path.join(B632, "verify_cell2_exhaustive.py"),
         "--repo", os.path.join(HERE, "..")],
        capture_output=True, text=True, timeout=1800)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "GATE exhaustive_coboundary_descent_162_of_162 PASS" in out
    assert "GATE alternating_all_diagonals_and_pairs PASS" in out
    assert "RESULT omega_rank=2 target_dimension=2 kernel_dimension=1" in out
    assert "AUDIT_VERDICT=CORRECTED_CELL2_MAP_PASSES_EXHAUSTIVE_DESCENT" in out
