"""B598 readiness-chain step 1 lock (upgraded): the EXACT peripheral
certificate — the relator forces c^2 - c + 1 = 0; at both geometric
branches the certified longitude commutes with the meridian, is
null-homologous, group-equal to the canonical word, has the banked cusp
shape -[[1, +-2 sqrt(-3)],[0,1]] and trace -2, and c is a unit. All
symbolic (sympy over Q(sqrt-3)); runs in seconds — ungated.
"""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B598_l85_campaign", "peripheral_certificate_exact.py")


def test_step1_exact_peripheral():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "the relator forces c^2 - c + 1 = 0" in out
    assert out.count("commute True; exp-sum True; group-equal True") == 2
    assert out.count("unit True") == 2
    assert "STEP 1 UPGRADED" in out
