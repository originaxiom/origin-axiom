"""B612 lock: the sealed per-level law FAILED (RRLLL closed at kappa=6);
the seven-object closure data pinned exactly.
"""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B612_pairing_chirality", "pairing_chirality.py")


def test_b612_data():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600)
    # the script asserts the sealed law and exits nonzero — the DATA is
    # what we pin; the sealed verdict is FAIL by design of the record
    out = r.stdout
    assert r.returncode != 0 and "LAW VIOLATED" in out
    for lab in ("RL", "RRLL", "RLRL", "RRRLLL"):
        assert f"{lab:>8} (amphichiral): closed at [5, 6, 7, 8, 9, 10, " \
               f"11, 12, 13, 14, 15, 16, 20, 24]" in out
    assert "RRL (     chiral): closed at NONE" in out
    assert "RRRL (     chiral): closed at NONE" in out
    assert "RRLLL (     chiral): closed at [6]" in out
