"""B598 readiness-chain step 6 lock: the exact stage data.

Runs the failure-enforcing v2 certification as a subprocess (exit nonzero on
any gate failure) and asserts the key output facts: all three E6_2 pair
amplitudes -(2/sqrt7) sin(2pi j'/7) zeta_14^k are SYMBOLIC IDENTITIES in
Q(zeta_84) — the squared identity p^2 = target^2 * N^2 proved exactly by
polynomial reduction mod Phi_84 over Q, the sign branch fixed at 1e-30
(achieved ~1e-41) with full-precision mpmath.

v1 (step6_exact_stage.py) is preserved on disk as the honest first attempt:
sympy simplify could not denest sqrt(N^2) and returned three false NONZEROs.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("step 6 lock requires OA_SLOW=1 (~10 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B598_l85_campaign", "step6_exact_stage_v2.py")


def test_step6_exact_stage():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert out.count("squared identity mod Phi_84: True") == 3
    assert out.count("sign branch = +1: True") == 3
    assert "SYMBOLIC IDENTITIES" in out
