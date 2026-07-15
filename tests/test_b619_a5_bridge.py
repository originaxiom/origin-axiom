"""B619 lock: the A5-bridge adjudication."""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B619_a5_bridge", "a5_bridge.py")


def test_b619_a5_adjudication():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=1200)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "ord rho(A1) (projective/exact): 20 (exact)" in out
    assert "ord rho_odd(A1): 5" in out
    assert "REFUTED as stated" in out
    assert "cap hit - larger than 400" in out
