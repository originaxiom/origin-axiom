"""B617 lock: the sign-law family theorem + closed form."""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B617_sign_law_theorem", "sign_law_theorem.py")


def test_b617_sign_law_theorem():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=1800)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "PROVED (symbolic)" in out
    assert out.count("banked-value checks: True") == 3
    assert "Fibonacci face" in out and "verified (m = 1, 4)" in out
    assert "family THEOREM" in out
