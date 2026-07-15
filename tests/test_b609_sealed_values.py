"""B609 lock: the Phase-2 sealed extraction (E3 fast cells + table pins).

The fast lock runs E3 (b238-based, ~1 min) and pins its gates and the
new exact structures; E1's l51-based fractions are pinned from the
committed output (the heavy recompute lives in the OA_SLOW E1 script).
"""
import os
import subprocess
import sys

HERE = os.path.dirname(__file__)
_E3 = os.path.join(HERE, "..", "frontier", "B609_sealed_values",
                   "b609_e3_spectra.py")
_E1OUT = os.path.join(HERE, "..", "frontier", "B609_sealed_values",
                      "e1_output.txt")


def test_e3_spectra():
    r = subprocess.run([sys.executable, _E3], capture_output=True,
                       text=True, timeout=1200)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "GATE kappa=4: dim_odd = 1" in out and "expect -1, REAL" in out
    assert out.count("trace = +0.618033989") == 2          # kappa = 5, 10
    assert "kappa=7: dim_odd = 6 (formula 6: True)" in out
    assert "kappa=13: dim_odd = 30 (formula 30: True)" in out
    assert out.count("law 0: True") == 2
    assert out.count("conj-closed: True") >= 3
    assert "E3 DONE" in out


def test_e1_pins():
    out = open(_E1OUT).read()
    assert "E1-a PASS" in out and "E1-b PASS" in out
    assert "wt +16: multiplet(1, 1, 2):1" in out
    assert "su3-root(0, 0, 0):1/2" in out                  # both wt+2 lines
    assert out.count("su3-root(0, 0, 0):1/2") == 2
