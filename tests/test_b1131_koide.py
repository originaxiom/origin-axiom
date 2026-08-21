"""B1131 lock -- P-KOIDE: NO-BRIDGE; det phi=-2/3 is a Cartan basis-change determinant
(re-confirmed exact this bench), the four bridge routes fail, the 2/3's are coincidence."""
import json, pickle
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1131_koide_no_bridge"


def test_verdict_no_bridge():
    r = json.loads((ARC / "b1131_results.json").read_text(encoding="utf-8"))
    assert "NO-BRIDGE" in json.dumps(r)


def test_det_phi_is_exactly_minus_two_thirds():
    import sympy as sp
    phi = pickle.load(open(ROOT / "frontier/B904_barton_sudbery/stage4c_phi.pkl", "rb"))
    M = sp.Matrix(phi)
    assert M.shape == (78, 78)
    assert M.det() == sp.Rational(-2, 3)   # the object's 2/3, exact -- a determinant, not an angle


def test_findings_close_the_gap():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "NO-BRIDGE" in f
    assert "ANTIPODE" in f                        # the trit route gives 0deg not 45deg
    assert "built and failed" in f.lower()        # B1129's gap closed
    assert "wrong KIND of object" in f
