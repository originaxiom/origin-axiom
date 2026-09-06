"""B1274 — the tower and its doubles: descent iff 3 | n, the image dichotomy A4 / V4, the class counts on
M_n, Y_n and the double bounds, for all 48 surjections (n <= 6)."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
for arc in ("B1267_spectrum_law_rebuilt", "B1269_transport_computed", "B1268_cusped_net_chirality_bound",
            "B1273_the_three_fold_closing", "B1274_the_tower_and_its_doubles"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))


def test_the_tower_dichotomy(capsys):
    import tower_and_doubles as TD
    assert TD.main()
    out = capsys.readouterr().out
    assert "{2: 'no', 3: 'yes', 4: 'no', 5: 'no', 6: 'yes'}" in out
    assert "M_2 (cusped): h0 = 0, h1(M_2; 3_rho) = 1" in out and "image order 12 (A4)" in out
    assert "Y_3 (closed, branched): h0 = 0, h1(Y_3; 3_rho) = 3, image order 4" in out
    assert "3_rho (x) sgn: (0, 0, 0, 0, 0)" in out
    assert "carrying >= 3 classes of the IRREDUCIBLE family system: NONE" in out
