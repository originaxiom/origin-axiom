"""B608 lock: the Rosetta Table (mixed form) + controls C1-C3.

Asserts: the full census (C2: 36 positive roots, su(3) = 3+, su(2) = 1+,
class sizes in {1,2,3,6}); the odd accounting (C3: 12 pairs, 9 of them
CLASS-MIXED, including the su3-root|su2-root pair); the even expansion
gate (C1); the class-pure (1,1,2) tips; B604's coefficients as
cross-checks.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("B608 lock requires OA_SLOW=1 (~20 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B608_rosetta_gsm", "rosetta_gsm.py")


def test_b608_rosetta_gsm():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=7200,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "C2 PASS" in out and "C3 PASS" in out and "C1 PASS" in out
    assert "class-mixed pairs: 9" in out
    assert "su2-root  q=(0, 0, 0)  |  su3-root  q=(0, 0, 0): 1 pair(s)" in out
    assert "wt +16: 1*[multiplet q=(1, 1, 2) | multiplet q=(1, 1, 2)]" in out
    assert "-443520*" in out and "-604800*" in out
    assert "B608 DONE" in out
