"""B616 lock: the held-out control run pinned.

RE-PINNED 2026-09-09.  This lock asserted "observed 2 coarse-tier matches of 378
pairs".  The script has printed 3 of 390 since the day it landed: script and lock
were committed together in d6eac1ed and the lock was never run against it.  Checked,
not inferred -- b616_heldout.py was executed in a worktree AT d6eac1ed and printed
"HG2: observed 3 coarse-tier matches of 390 pairs".  So the pinned pair came from an
earlier draft of the script; nothing regressed, and the arc's verdict is unchanged.

The three matches are robust, not marginal: |d13|^2 and |d15|^2 vs sin^2th13 at
dev = 0.0071, and |arg d22|/pi vs sin^2th12 at dev = 0.0099, all against hard-coded
targets, so no bench can see a different count.

KNOWN FRAGILITY, reported not patched (it is main's arc to re-pin): the family is cut
with "0 < val", and 14 of the candidate quantities are exact zeros of the weld computed
through np.linalg.inv, landing between 2e-32 and 7e-16.  Their membership is decided by
the sign of rounding noise.  Both this bench and d6eac1ed keep all 14 (family 65, pairs
390); a cut at any threshold between 1e-14 and 1e-6 would keep 51 (pairs 306) and leave
the three matches and the verdict untouched.
"""
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
    assert "observed 3 coarse-tier matches of 390 pairs" in out
    assert "STILL-AMBIGUOUS" in out
