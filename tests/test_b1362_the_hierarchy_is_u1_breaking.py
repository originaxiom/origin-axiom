"""B1362 lock (about a minute): the circulant degeneracy, Weyl's bound (0.332 m_t, 0.327 m_b, 0.313 m_tau) and the numerical minimum
attaining it."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1362_the_hierarchy_is_u1_breaking" / "verification"


def test_the_deck_degeneracy_and_the_third_of_the_top():
    out = subprocess.run([sys.executable, str(VER / "hierarchy_bound.py")], capture_output=True, text=True, timeout=1500).stdout
    assert "-> a degenerate pair x - y (multiplicity 2): True" in out
    assert "up: ||E||_op >= (m3 - m2 - m1)/3 = 57.29 GeV = 0.332 m_3" in out
    assert "down: ||E||_op >= (m3 - m2 - m1)/3 = 0.9341 GeV = 0.327 m_3" in out
    assert "charged leptons: ||E||_op >= (m3 - m2 - m1)/3 = 0.5569 GeV = 0.313 m_3" in out
    import re
    m = re.search(r"up: minimal max\|M_ii\| = ([0-9.]+) GeV = ([0-9.]+) m_3", out)
    assert m and abs(float(m.group(2)) - 0.3321) < 0.002
