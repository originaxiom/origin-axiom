"""B1360 lock (seconds): the E7 root system (126 roots, n_7 = 1), the 72 roots orthogonal to the omitted coweight equal E6's, the rank-one
quotient H_2 of the generic fibre, the centraliser of 2T in gl(2,C) is the scalars, and the SU(N) calibration (weight N-1, degrees 1/N^2, 1)."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1360_the_companion_free_apex" / "verification"


def test_the_inputs_of_the_companion_free_apex():
    out = subprocess.run([sys.executable, str(VER / "companion_free_apex.py")], capture_output=True, text=True, timeout=600).stdout
    assert "E7: 126 roots (63 positive); highest root (2, 2, 3, 4, 3, 2, 1); coefficient on alpha_7 = n_7 = 1" in out
    assert "roots of E7 with zero coefficient on alpha_7: 72; roots of E6 from its own Cartan matrix: 72; equal as sets (dropping the seventh coordinate): True" in out
    assert "H_2 of the E7 resolution modulo the E6 configuration: rank 1 (the surviving curve C_7): H_2(X_t; Q) = Q -> True" in out
    assert "centraliser of 2T in gl(2, C): dimension 1 (the scalars: True)" in out
    assert "N = 2: the circle rotates the core P(1,2) with relative weight -1 (trivial iff N = 1); orbifold degrees: int_U H = 1/(N N) = 1/4" in out
    assert "N = 1: the circle rotates the core P(1,1) with relative weight 0" in out
