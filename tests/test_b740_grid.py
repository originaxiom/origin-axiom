"""B740 lock -- the completed B288 grid: the grid arithmetic (87 = 9 exceptional + 78 hyperbolic),
the amphichirality shortcut (4_1(p,q) ~ 4_1(-p,q), verified), and the completion artifact. Pure math."""
from math import gcd
import pytest

def test_grid_arithmetic():
    total = sum(1 for p in range(-8, 9) for q in range(1, 9) if gcd(abs(p), q) == 1)
    exceptional = len({(p, 1) for p in range(-4, 5)})
    assert total == 87 and exceptional == 9 and total - exceptional == 78
    # the banked B288 record resolved 54 -> the gap was 24 hyperbolic fillings, closed by B740

def test_amphichirality_shortcut_sample():
    snappy = pytest.importorskip("snappy")
    for (a, b) in [((-1, 7), (1, 7)), ((-7, 8), (7, 8))]:
        Ma = snappy.Manifold('m004'); Ma.dehn_fill(a)
        Mb = snappy.Manifold('m004'); Mb.dehn_fill(b)
        assert Ma.is_isometric_to(Mb)                 # the mirror isometry: same abstract trace field
        assert abs(float(Ma.volume()) - float(Mb.volume())) < 1e-9

def test_completion_artifact_states_78_and_clean():
    import pathlib
    out = pathlib.Path("frontier/B740_b288_stragglers/b740_full_out.txt").read_text()
    assert "hyperbolic analyzed=78" in out and "unresolved=0" in out
    assert " True)" not in out                        # no row records a sqrt(-3) hit anywhere in the grid
