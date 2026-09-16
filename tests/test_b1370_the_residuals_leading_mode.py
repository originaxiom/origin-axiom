"""B1370 lock (about ten seconds): the four residual cusps developed from the tetrahedra shapes (lattices agreeing with SnapPy's cusp
moduli), the fixing isometries' affine actions, and the allowed Fourier shells -- the unique shortest mode allowed for every Higgs
class on all four cusps, the first two-direction shell 4, 2, 4, 2 allowed single-direction shells deep."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1370_the_residuals_leading_mode" / "verification"


def test_the_shortest_cusp_mode_is_allowed_on_every_residual_cusp():
    out = subprocess.run([sys.executable, str(VER / "residual_cusp_modes.py")], capture_output=True, text=True, timeout=1500).stdout
    assert out.count("reduced modulus") == 4 and out.count(") agree") == 4 and "DISAGREE" not in out     # the four developed moduli against SnapPy's
    assert "o10_150688, cusp 0: b_1 2, ranks [1], free classes on cusp 0: 1, |Aut| = |Isom| = 2" in out
    assert "o10_150725, cusp 1: b_1 3, ranks [2, 1, 2], free classes on cusp 1: 2, |Aut| = |Isom| = 12" in out
    assert "special lines in the free classes (eigenlines of fixers): 6" in out
    assert "o10_150688 cusp 0, the free class: lowest allowed shell |k|^2 = 0.013333, vectors [(0, -1), (0, 1)], dimension 1, directions [(0, 1)] -> annular unless the coefficients of the first 4 allowed shells all vanish" in out
    assert "o10_150708 cusp 0, the free class: lowest allowed shell |k|^2 = 0.037037, vectors [(0, -1), (0, 1)], dimension 1, directions [(0, 1)] -> annular unless the coefficients of the first 2 allowed shells all vanish" in out
    assert "o10_150716 cusp 0, the free class: lowest allowed shell |k|^2 = 0.013333, vectors [(0, -1), (0, 1)], dimension 1, directions [(0, 1)] -> annular unless the coefficients of the first 4 allowed shells all vanish" in out
    assert "o10_150725 cusp 1, a generic class (stabiliser: the identity alone): lowest allowed shell |k|^2 = 0.037037, vectors [(0, -1), (0, 1)], dimension 2, directions [(0, 1)] -> annular unless the coefficients of the first 2 allowed shells all vanish" in out
    assert out.count("cross-check: (trace, det) of the fixers' linear parts agree with SnapPy's cusp maps: True; lattice modulus agrees with SnapPy's cusp_translations: True") == 4
    assert "killed by symmetry" in out            # some higher shells are killed: the half-period translations have teeth
    assert "partition depends on the coefficients" not in out.split("=== (D)")[1]
    assert "DONE" in out
