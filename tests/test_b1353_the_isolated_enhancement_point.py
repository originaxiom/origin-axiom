"""B1353 -- the isolated enhancement point made finite: the fourteen orbifold groups with an isolated apex on the E6 plane, every
codimension-4 stratum through the apex meeting the E6 plane in a line; B1084's group placed (fast, ~1 minute, numpy only)."""
import sys, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1353_the_isolated_enhancement_point" / "verification"


def test_every_a_stratum_through_the_isolated_apex_contains_a_line_of_the_e6_plane():
    out = subprocess.run([sys.executable, str(VER / "isolated_point_groups.py")], capture_output=True, text=True, timeout=1800).stdout
    assert "2I: order 120; contains 2T: True; 2T normal in it: False" in out
    assert "groups enumerated: 14; all with kernel 2T and an isolated fixed point: True" in out
    assert "every codimension-4 stratum through the isolated point meets the E6 plane P in a subspace of dimension >= 1 (never only at 0): True" in out
    assert "L = D*2, L_K = C4, R = 2O: census {1: 42, 3: 53} = B1084's" in out
    assert out.count("-> ISOLATED") == 14 and "not isolated" not in out
