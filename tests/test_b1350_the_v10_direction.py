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

@pytest.mark.slow
def test_the_exact_second_order_obstruction_vanishes_on_the_v10_plane():
    out = subprocess.run([sys.executable, str(VER / "obstruction.py")], capture_output=True, text=True, timeout=3600).stdout
    assert "rank d1 = 70" in out
    assert out.count("UNOBSTRUCTED (Q in im d1)") == 16            # eight blocks, two primes
    assert "V10 classes: [True, True]" in out and "V10 plane span 0" in out
    assert "agreement of the two primes on every rank: True" in out


@pytest.mark.slow
def test_the_v10_classes_are_formally_integrable_through_order_six():
    out = subprocess.run([sys.executable, str(VER / "obstruction_higher.py"), "6"], capture_output=True, text=True, timeout=3600).stdout
    for k in ("V10  ", "V10#2", "V10+V10#2", "V10-V10#2"):
        assert any(line.strip().startswith(k.strip()) and ": None" in line for line in out.splitlines()), k
    assert out.count("integrable to order 6") == 8                   # four directions, two primes

@pytest.mark.slow
def test_the_converged_points_re_read_at_2000_bits():
    """the banked converged points (600-bit midpoints) re-read with 200-digit ranks: every direction has h1(27) = h1(27bar) = 0,
    no cusp-fixed vector in either, torus Euler characteristic and duality consistent, N(27) = 0; the control at rho_0 reproduces the exact stage."""
    out = subprocess.run([sys.executable, str(VER / "report_hp.py"), str(VER / "v10_direction_points.json")], capture_output=True, text=True, timeout=3600).stdout
    assert "27 at rho_0: h0(M) = 0, h1(M) = 3, h2(M) = h1 - h0 = 3; torus: h0 = 3, h1 = 6, h2 = 3 (Euler ok); rank(res) = 3" in out
    lines = [l for l in out.splitlines() if l.strip().startswith(("class 1 ", "class 2 ", "class 1 + class 2", "class 1 - class 2")) and "N(27) =" in l]
    assert len(lines) == 4, out[-2000:]
    for l in lines:
        assert "N(27) = 0; h1(27) = 0, h1(27bar) = 0; cusp h0(27) = 0, h0(27bar) = 0; torus Euler ok: True" in l, l
