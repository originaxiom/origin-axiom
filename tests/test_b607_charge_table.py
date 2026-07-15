"""B607 lock: the exact bicharge census of the odd-block lines.

Asserts: exactly two PURE lines — V(m=8)'s extremal weights +-16 with
bicharge (1,1) (the double-spinor tips) — and every other line MIXED;
the h = 4 coefficients reproduce B604's banked values.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("B607 lock requires OA_SLOW=1 (~20 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B607_charge_table", "charge_table.py")


def test_b607_charge_census():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=7200,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "V(m=8) wt +16: bicharges [(1, 1)]  [PURE]" in out
    assert "V(m=8) wt -16: bicharges [(1, 1)]  [PURE]" in out
    assert out.count("[MIXED]") == 22
    assert out.count("[PURE]") == 2
    assert "-443520*" in out and "-604800*" in out     # B604 cross-check
    assert "B607 DONE" in out
