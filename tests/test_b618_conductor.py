"""B618 lock: the conductor-unification third-object prediction."""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B618_conductor_test", "conductor_test.py")


def test_b618_conductor_prediction():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "sqrt(21)-bearing levels: [14, 21, 35, 42]" in out
    assert "PREDICTION VERDICT (content at d|21 levels only, d>1): PASS" in out
