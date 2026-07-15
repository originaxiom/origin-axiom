"""B604 lock: the Rosetta resolution.

Subprocess run of rosetta_blocks.py; asserts: the root/fold verification
gates; the corrected pair-label table ((D5,D5) pairs at h = 1, 2, 3; both
pairs (D5,16) at h = 4; (16,16) at h = 8); and the resolution — every
block line at every ambiguous height is MIXED (no pair-to-block
assignment exists).
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("B604 lock requires OA_SLOW=1 (~20 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B604_rosetta_blocks", "rosetta_blocks.py")


def test_b604_rosetta():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=7200,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "V1 PASS: 36 roots; 12 theta-fixed + 12 pairs" in out
    assert "theta gates PASS" in out
    for h in (1, 2, 3):
        assert f"h={h}: pairs {{D5,16}} {{D5,D5}}" in out
    assert "h=4: pairs {D5,16} {D5,16}" in out
    assert "h=8: pair {16,16}" in out
    assert out.count("[MIXED]") == 8              # both lines, h = 1..4
    assert "B604 DONE" in out
