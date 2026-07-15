"""B603 lock: the J-isotropy law + mechanism + the E6_2 center data.

Subprocess run of isotropy_mechanism.py; asserts: v0 is weight-pure at 0;
g_m = 0 at ALL six blocks with the move-across identity and weight-forcing
at every block; the E6_2 simple currents are primaries [3, 4] and all
three odd pairs carry conjugate nonzero Z3 charges.
"""
import os
import subprocess
import sys

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("B603 lock requires OA_SLOW=1 (~15 min)",
                allow_module_level=True)

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B603_isotropy_mechanism", "isotropy_mechanism.py")


def test_b603_isotropy_mechanism():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=7200,
                       env={**os.environ, "OA_SLOW": "1"})
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "v0 weight support: [0]" in out
    assert out.count("g_m = 0;  move-across identity [True];  "
                     "weight-FORCED zero: True") == 6
    assert "simple currents (d = 1, non-vacuum): [3, 4]" in out
    assert "odd pair   27 = (1,2): charges (2, 1)" in out
    assert "odd pair 351' = (3,4): charges (1, 2)" in out
    assert "odd pair  351 = (7,8): charges (1, 2)" in out
    assert "B603 DONE" in out
