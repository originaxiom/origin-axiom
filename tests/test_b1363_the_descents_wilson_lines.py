"""B1363 lock (seconds): the six order-3 Kac classes of E6 and the eleven order-4 ones, none with the Standard-Model commutant; the
coinvariants Z/2 of A_4 on Z^3."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1363_the_descents_wilson_lines" / "verification"


def test_no_order_3_or_4_element_of_e6_has_the_standard_model_commutant():
    out = subprocess.run([sys.executable, str(VER / "descent_lines.py")], capture_output=True, text=True, timeout=600).stdout
    assert "s = (0, 0, 0, 0, 1, 0, 0): fixed subalgebra A2 + A2 + A2 + 0 u(1)" in out
    assert "an order-3 element with commutant exactly SU(3) x SU(2) x U(1)^2 exists: False" in out
    assert "an order-4 element with commutant exactly SU(3) x SU(2) x U(1)^2 exists: False" in out
    assert out.count("fixed subalgebra") == 17
    assert "Smith form of the span of (1 - g) Z^3 over g in A_4: [1, 1, 2]" in out
