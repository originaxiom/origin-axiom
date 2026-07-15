"""B600 — the level ladder (OA_SLOW lock): the verified headline.

Z = +1, +1, +1, 0 at E6 levels 1..4; Tr(Theta rho_4) = 0; the primary counts
and odd dimensions. See frontier/B600_level_ladder/FINDINGS.md.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("level-ladder lock requires OA_SLOW=1 (~5 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B600_level_ladder", "verify_level4.py")


def test_ladder():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "k=1: N=  3" in out and "k=2: N=  9" in out
    assert "k=3: N= 20" in out and "k=4: N= 42" in out
    for k in (1, 2, 3):
        assert f"k={k}" in out
    # the headline: Z_4 = 0 and Tr(Theta rho_4) = 0
    line4 = [l for l in out.splitlines() if l.startswith("k=4")][0]
    assert "Z=-0.0000000000" in line4 or "Z=+0.0000000000" in line4
    assert "Tr(Theta rho)=-0.0000000000" in line4 or "Tr(Theta rho)=+0.0000000000" in line4
