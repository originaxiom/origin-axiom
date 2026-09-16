"""B1368 lock (~1 min): the Riley representation and Calegari's trace -2 for the longitude; the Alexander polynomial z^2 - 3z + 1 and the
twisted Alexander polynomial z^2 - 4z + 1 of the geometric representation by Fox calculus; h^1(Ad) = 1; spin-1/2 sectors never
cusp-fixed for the geometric representation; the frame theorem (the 10 and the 5bar of SU(5) never share an SL(2)_beta spin); the
eight lambda-parabolic points of the character variety."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1368_the_objects_own_sm_connections" / "verification"


def test_no_flat_e6_connection_of_m004_gives_a_chiral_generation_with_the_sm_unbroken():
    out = subprocess.run([sys.executable, str(VER / "sm_connections_of_m004.py")], capture_output=True, text=True, timeout=1500).stdout
    assert "relator a w b^-1 w^-1 holds: True; longitude lambda = w w*: trace -2 (Calegari's -2)" in out
    assert "lambda + 1 is nilpotent (lambda = -(unipotent)): True" in out
    assert "the Alexander polynomial Delta(z) = -(z**2 - 3*z + 1)/z" in out
    assert "Wada's twisted Alexander polynomial = (z**2 - 4*z + 1)/z**2" in out
    assert "generic (h^0, h^1) = (0, 0); at the twisted roots: [(0, 1), (0, 1)]; at z = 1 (the untwisted V_2): (0, 0); at z = -1 (the other lift): (0, 0)" in out
    assert "spin 1 (Ad rho, neutral): (h^0, h^1) = (0, 1)" in out
    assert "spin 1/2, z = 1: fixed dim 0" in out and "spin 0, z = 1: fixed dim 1" in out and "spin 1 (Ad rho): fixed dim 1" in out
    assert "27-frame: the 10 in spin 0 (True), the 5bar in spin 1/2 (True); 78-frame: the 10 in spin 1/2 (True), the 5bar in spin 0 (True)" in out
    assert "resultant in m of (Phi, tr lambda - 2): m**6*(m**2 + 1)**4*(m**2 - m - 1)**2*(m**2 + m - 1)**2" in out
    assert "points with tr rho(lambda) = 2: 8" in out
