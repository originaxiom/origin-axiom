"""B620 lock: the conductor mechanism."""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B620_conductor_mechanism", "conductor_mechanism.py")


def test_b620_mechanism():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "reflections: 4 - t^2  [PROVED symbolically]" in out
    assert "PROVED by interpolation" in out
    for line in ("RL kap= 5 (BEARING): sqrt(5) in reflections: True; "
                 "in identity/rotations: False",
                 "RL kap= 6 ( silent): sqrt(5) in reflections: False",
                 "RRRL kap=14 (BEARING): sqrt(21) in reflections: True; "
                 "in identity/rotations: False",
                 "RRRL kap= 9 ( silent): sqrt(21) in reflections: False"):
        assert line in out
    assert "B620 DONE" in out
