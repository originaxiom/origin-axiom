"""The restated symmetry lemma (OA_SLOW manifest lock, D8-compliant).

Runs the assert-hardened lemma_cell.py as a subprocess (exit nonzero on any
gate failure) and asserts the key output facts: J symmetric, the six-block
forced-zero split (even structural / odd genuine), and the exact J-paired
weld values.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("lemma lock requires OA_SLOW=1 (~12 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B598_l85_campaign", "lemma_cell.py")


def test_lemma_cell():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "J^T = c J with c = 1,0" in out                    # symmetric
    assert out.count("criterion: FORCED") == 4                # even blocks
    assert out.count("criterion: not forced") == 2            # theta-odd
    assert "m=4: <v0, b2 v0>_J = (-536479695357+536483888640w)" in out
    assert "m=8: <v0, b2 v0>_J = (536481792003-536481792000w)" in out
