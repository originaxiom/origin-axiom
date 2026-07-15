"""B598 readiness-chain steps 3+5 (OA_SLOW manifest lock, D8-compliant).

Runs the failure-enforcing script as a subprocess (exit nonzero on any gate
failure) and asserts the key output facts: the universal boundary ratio -2w
at all six blocks, the Schur-unique invertible J, the zero-dimensional
untwisted-form space, and the J-L1 parity zeros.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("steps 3+5 lock requires OA_SLOW=1 (~25 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B598_l85_campaign", "steps3and5.py")


def test_steps_3_and_5():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert out.count("ratio I_lam/I_mu = (0-2w)") == 6      # the universal ratio
    assert "solution space dim (Schur gate, expect 1): 1" in out
    assert "rank(J) = 27 (invertible: True)" in out
    assert "untwisted-form solution dim (seat 4's claim, expect 0): 0" in out
    assert out.count("^T J v0 = 0") == 2                    # J-L1 zeros
