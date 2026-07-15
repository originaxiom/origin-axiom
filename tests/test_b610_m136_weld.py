"""B610 slice-1 lock: the m136 (RRL) weld scan universality rows.

Pins: chat-1's complex-trace claim confirmed (omega at kappa=5, zeta_6
family at 6/10/15); the conjugation-closure failure at EVERY level (the
fig-8's B601 law is object-specific); unit-modulus everywhere scanned
(no magnitude-chirality window for m136 at kappa <= 24); the fig-8
controls unchanged.
"""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B610_m136_weld", "m136_weld_scan.py")


def test_b610_slice1():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=1800)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    rows = [l for l in out.splitlines()
            if l.strip() and l.split()[0].isdigit()]
    assert len(rows) == 15
    for l in rows:
        cols = l.split()
        assert cols[3] == "False"                 # cc fails at every level
        assert cols[4] == "True"                  # unit-modulus everywhere
    assert "     5   -0.500000000   +0.866025404" in out   # omega at k=5
    assert "CONFIRMED at the listed kappa" in out
    assert "B610 SLICE-1 DONE" in out
