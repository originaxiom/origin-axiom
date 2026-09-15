"""B1358 lock (seconds): the census of the twistor cones of S^4/(2T x Gamma_R) -- companions A1 (degree 12), A5, A3, A5, D4, E6 at the
second pole, the mixed loci, the 14 enhanced points of B1355's cone, and the inflow ratio 12 : 1 for Gamma_R = 1."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1358_the_e6_apex_family" / "verification"


def test_the_apex_family_census_companions_mixed_loci_and_inflow_ratios():
    out = subprocess.run([sys.executable, str(VER / "apex_family.py")], capture_output=True, text=True, timeout=900).stdout
    assert "Gamma_R =  1: first pole 2T (E6) (degree 1); second pole Z2 (A1) (degree 12); mixed loci none; inflow ratio A(U(1).E6^2) : A(U(1).companion^2) = 12 : 1; companion in B1357's background: the SU(2) copy of Y_3" in out
    assert "Gamma_R = Z3: first pole 2T (E6) (degree 3); second pole Z6 (A5) (degree 12); mixed loci [(4, 'Z3 (A2)'), (4, 'Z3 (A2)'), (4, 'Z3 (A2)'), (4, 'Z3 (A2)')]" in out
    assert "Gamma_R = Z4: first pole 2T (E6) (degree 2); second pole Z4 (A3) (degree 12); mixed loci [(6, 'Z2 (A1)'), (6, 'Z2 (A1)')]" in out
    assert "Gamma_R = Q8: first pole 2T (E6) (degree 4); second pole Q8 (D4) (degree 12); mixed loci [(12, 'Z2 (A1)'), (12, 'Z2 (A1)'), (12, 'Z2 (A1)')]" in out
    assert "Gamma_R = 2T: first pole 2T (E6) (degree 12); second pole 2T (E6) (degree 12); mixed loci [(36, 'Z2 (A1)'), (16, 'Z3 (A2)'), (16, 'Z3 (A2)'), (16, 'Z3 (A2)'), (16, 'Z3 (A2)')]" in out
    assert "enhanced points on the fixed lines (stabiliser jumps): 14 points, (orbit size, effective stabiliser): [((4, 6), 2), ((6, 4), 1)]" in out
    assert out.count("isolated fixed points off every locus (codimension-6 lines of the cone): 0 points") == 7
