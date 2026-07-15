"""B598 readiness-chain step 7 lock: G1-FINITE — the dial-map closure.

Failure-enforcing subprocess run of step7_g1_finite.py; asserts: all six
dial slots peripherally fixed under the certified longitude; every
generator exactly inside the e6 span (the SUBSET face); the mod-p closure
dims at two primes: no-twist 3, slot 1 -> 3 (its top IS the principal e),
theta-even {5,7,11} -> 52 = f4 (the theta-fixed/deaf subalgebra),
theta-odd {4,8} -> 78 = e6 (the RANK face certificate). Closes the B582
provenance hole at finite t with committed code.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("step 7 lock requires OA_SLOW=1 (~20 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B598_l85_campaign", "step7_g1_finite.py")


def test_step7_g1_finite():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=7200,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert out.count("fixed by (mu, lambda): True") == 6
    assert out.count("membership [True, True, True]") == 7
    assert "no-twist: closure dim = 3 / 3 (primes agree: True)" in out
    assert "slot 1: closure dim = 3 / 3 (primes agree: True)" in out
    for m in (5, 7, 11):
        assert f"slot {m}: closure dim = 52 / 52 (primes agree: True)" in out
    for m in (4, 8):
        assert f"slot {m}: closure dim = 78 / 78 (primes agree: True)" in out
    assert "theta-odd dials reach 78 (= e6): True" in out
    assert "STEP 7 (G1-FINITE) DONE" in out
