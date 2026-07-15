"""B616 lock: the held-out control run pinned."""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B616_heldout", "b616_heldout.py")


def test_b616_heldout():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=1800)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "design hash: a11491e6" in out
    assert "sign pattern [-1, 1, -1, -1, 1, -1]" in out
    assert "same: True" in out                      # the sign-law match
    assert "observed 2 coarse-tier matches of 378 pairs" in out
    assert "STILL-AMBIGUOUS" in out
