"""B1350 — the V_10 direction: the subregular point's block multiplicities, its 27 / 27bar cohomology (N = 0), the two exact
V_10 cocycle classes and their cusp restrictions, the first-order trace-flatness (fast, a few minutes: exact Q(omega) work
including the 78-dimensional adjoint exponentials); the Newton deformations and N along the four directions (slow)."""
import sys, subprocess
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1350_the_v10_direction" / "verification"
sys.path.insert(0, str(VER))
pytest.importorskip("flint")


def test_the_point_the_classes_and_their_cusp_restrictions():
    import v10_direction as V                       # runs stages 0..3 at import
    assert V.blocks == {2: 1, 4: 1, 6: 1, 8: 1, 10: 2, 12: 0, 14: 1, 16: 1}
    assert V.h1x == 3 and V.h1d == 3 and V.rep0['N'] == 0 and V.rep0d['N'] == 0 and V.rep0['h0t'] == 3
    assert [c[2]['h1'] for c in V.COC] == [1, 1] and all(c[2]['cusp_trivial'] is False for c in V.COC)
    assert V.r_joint == 2
    assert V.flat < 1e-100


@pytest.mark.slow
def test_the_deformations_and_n27():
    out = subprocess.run([sys.executable, str(VER / "v10_direction.py"), "01234"], capture_output=True, text=True, timeout=10800).stdout
    assert "=== (4)" in out
    assert out.count('N(27) = h1(27) - h1(27bar) =') == 4
