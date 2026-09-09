"""B1355 lock (fast, seconds): 2T on CP^3 = P(C^2 (+) C^2) fixes the line P(0 + C^2) pointwise with the normal action 2T c SU(2) (the E6
locus), the element -1 fixes the line P(C^2 + 0) with normal weights (-1, -1) (the A1 locus), the 14 isolated fixed points have
stabilisers of orders 4 and 6, and the centraliser of 2T in Sp(1) is {+-1}."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1355_the_e7_point_made_explicit" / "verification"


def test_the_cone_over_cp3_mod_2t_has_an_e6_locus_and_an_a1_locus_through_the_apex():
    out = subprocess.run([sys.executable, str(VER / "cone_over_cp3_mod_2t.py")], capture_output=True, text=True, timeout=600).stdout
    block = out.split("=== Z_2")[0]
    assert "fixed pointwise by 24 elements (all of the group: True)" in block
    assert "normal action = the group itself on C^2, in SU(2): True" in block
    assert "SU(2)-type (A1)" in block
    assert "isolated fixed points on L' (vertices of the polyhedral action): 14 points; stabiliser orders {4: 6, 6: 8}" in block
    assert "the centraliser of 2T in Sp(1) is {+-1}" in out
