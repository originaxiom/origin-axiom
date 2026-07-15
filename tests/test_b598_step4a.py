"""B598 readiness-chain step 4a lock: the typed domain of the P2 map.

Failure-enforcing subprocess run of step4a_domain.py; asserts the uniform
six-block picture: dim H1(pi_K; V_m) = 1, the T^2 module has h0 = 1,
h1 = 2, h2 = 1 with duality h0 = h2, the peripheral pair commutes, and
res: H1(pi_K) -> H1(T^2) is injective (nonzero mod B1) at every block.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("step 4a lock requires OA_SLOW=1 (~30 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B598_l85_campaign", "step4a_domain.py")


def test_step4a_domain():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=7200,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert out.count("dim H1(pi_K)=1 [True]") == 6
    assert out.count("h0=1") == 6
    assert out.count("h1=2") == 6
    assert out.count("duality(h0=h2): True") == 6
    assert out.count("[mu,lam]=1[True]") == 6
    assert out.count("res in Z1[True] nonzero mod B1[True]") == 6
    assert "the domain is TYPED" in out
