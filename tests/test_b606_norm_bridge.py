"""B606 lock: the norm-bridge cells (NF-0 gates + the NF-1 scan).

Fast (seconds, ungated): asserts N(h3) = 1/5 exactly (minpoly
5x^4+5x^3+1), the E6_2 amplitude norm-product = 1/49 (60-digit
certificate of the classical product identity), and the NF-1 scan
all-fail (no torsion-power normalization; the D-nf outcome).
"""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B606_norm_bridge", "b606_cells.py")


def test_b606_cells():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "minpoly(h3) = 5*x**4 + 5*x**3 + 1" in out
    assert "[expected 1/5: True]" in out
    assert "norm-product = 1/49 to 60 digits" in out
    assert "exact hits over |k| <= 3: NONE" in out
    assert "D-nf" in out
