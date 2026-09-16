"""B1373 lock (seconds): along the cone-manifold path on every free cusp of the 35 candidates, the order-4 point is reached on 132 of
166 (cusp, curve) pairs with a non-unitary other eigenvalue at every one (Theorem B); the other 34 (all meridians) degenerate before the
point on a deterministic fine path, 23 near cone angle pi and 11 near 2 pi / 3, the other translation length monotone increasing."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1373_the_order_4_points_on_the_geometric_components" / "verification"


def test_no_order_4_point_on_the_geometric_path_of_any_free_cusp():
    out = subprocess.run([sys.executable, str(VER / "order4_points.py")], capture_output=True, text=True, timeout=1500).stdout
    assert "points followed: 132; closed by Theorem B (non-unitary other eigenvalue): 132; closed by Theorem C: 0; survivors: 0 []" in out
    assert "continuations that did not converge on the coarse path: 34" in out
    assert ("failures resolved on the fine path: 34 (converged: 0, survivors: 0; degenerate before or at cone angle pi: 34 -- "
            "wall within 1/16 of p = 1 (cone angle pi): 23, within 1/16 of p = 3/2 (cone angle 2pi/3): 11, elsewhere: 0); "
            "|Re H(other)| monotone increasing on the approach: 34 of 34") in out
    assert "|Re H(other)| at the last non-degenerate step: from 10.22 to 27.00" in out
    assert "t06828      cusp 0 mu of order 4     : contains negatively oriented tet vol  2.786805  H(other) = +4.397146" in out
    assert "o10_150725  cusp 1 mu of order 4     : degenerates near cone angle 2pi/3 (wall p = 1.5000;" in out
    assert "DONE" in out
