"""B613 lock: the closure theorem's verification suite."""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B613_closure_theorem", "closure_theorem.py")


def test_b613_theorem():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=1800)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert out.count("axioms+ingredients ALL PASS") == 4
    assert out.count("conj(W) = Q^-1 W^T Q  [True]") == 16
    assert out.count("identity fails with this Q [True]") == 12
    assert "THE CLOSURE THEOREM VERIFIED" in out
