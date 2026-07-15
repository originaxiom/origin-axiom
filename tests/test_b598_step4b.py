"""B598 readiness-chain step 4b lock: the bending responses of the P2 map.

Failure-enforcing subprocess run of step4b_responses.py; asserts: the six
bending directions are peripherally fixed; the banked B599-ALG witnesses
reproduce exactly under the degree-2 truncation; the t^1 J-responses vanish
at ALL six blocks (forced at even, genuine at odd); the t^2 response matrix
has rank 2 supported exactly on the theta-odd blocks {4, 8}; and the two
hearing columns ride conjugate phases N4(1+w) / N8(1-w).
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("step 4b lock requires OA_SLOW=1 (~1 h)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B598_l85_campaign", "step4b_responses.py")


def test_step4b_responses():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=10800,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert out.count("bending direction peripherally fixed: True") == 6
    assert "(banked +2096640): True" in out
    assert "(banked -536481792000): True" in out
    assert out.count("all t^1 J-responses zero: True") == 6
    assert "rank R1 = 0;  rank R2 = 2" in out
    assert "R2 supported on the theta-odd blocks only: True" in out
    assert out.count("(2096640+2096640w)") >= 10        # the m=4 phase line
    assert out.count("(536481792000-536481792000w)") >= 10   # m=8 conjugate
    assert "STEP 4b DONE" in out
