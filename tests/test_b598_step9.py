"""B598 readiness-chain step 9 lock: the clean-room independent P1.

Failure-enforcing subprocess run of step9_independent_p1.py (a fresh
construction from the E6 Cartan matrix with Frenkel-Kac signs and its own
Q(sqrt-3) arithmetic — no shared code, no imported values): asserts all
construction gates (G-A..G-D) and the invariant table — dim H1 = 1 and
I_lambda/I_mu = -2 sqrt(-3) at all six blocks.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("step 9 lock requires OA_SLOW=1 (~2 h)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B598_l85_campaign", "step9_independent_p1.py")


def test_step9_independent_p1():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=14400,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    for g in ("G-A PASS", "G-B PASS", "G-C PASS", "G-D PASS"):
        assert g in out
    assert "block dims [3, 9, 11, 15, 17, 23]" in out
    assert out.count("[-2w: True]") == 6
    assert out.count("dimH1=1[True]") == 6
    assert "STEP 9 DONE" in out
