"""B605 lock: Door 2 — the fixed-set type of the orientation-reversing
symmetries of the figure-eight complement.

Subprocess run of door2_involution.py; asserts: the relator gates; the
four or-reversing families with the D4-consistent orders (two glide
involutions with tau^2 a meridian conjugate; two order-4 elements); the
Gamma-lift census to reduced length 6 finding ZERO reflection-type and
ZERO antipodal-type lifts in all four families; SnapPy |Isom| = 8 (D4),
amphichiral; and the computed Gieseking identification (m000
non-orientable, 1 tetrahedron, half volume, 4_1 its degree-2 cover).
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("B605 lock requires OA_SLOW=1 (~5 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B605_door2_involution", "door2_involution.py")


def test_b605_door2():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "gate: both branches satisfy the relator exactly" in out
    assert "GLIDE (tau^2 ~ a in Gamma)" in out
    assert "GLIDE (tau^2 ~ baB in Gamma)" in out
    for fam in "aAbB":
        assert f"family phi(a)={fam}: reflection-type lifts (len<=6): 0" in out
        assert f"family phi(a)={fam}: antipodal-type lifts (len<=6): 0" in out
    assert "|Isom| = 8" in out and "D4" in out
    assert "4_1 among the degree-2 covers of m000: True" in out
    assert "B605 DONE" in out
