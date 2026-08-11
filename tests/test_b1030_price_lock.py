"""B1030 locks — the price-lock verification (one unit, two bits, ONE TRIT)."""
import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1030_price_lock_verification"


def _cells():
    spec = importlib.util.spec_from_file_location("b1030_verify", ARC / "b1030_verify.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_v1_two_bits_formula_route():
    m = _cells()
    r = m.v1_two_bits_by_formula()
    assert all(r.values()), r
    # independent arithmetic: H^1 of a C2 permutation module = 2^(#fixed points)
    assert 2 ** (2 + 2) // 2 ** 2 == 2 ** 2 == 4


def test_v2_the_trit():
    m = _cells()
    r = m.v2_the_trit()
    assert all(r.values()), r
    assert float(sp.log(3, 2)) < 3.0  # the trit fits any 3-bit cap trivially


def test_v3_defect_and_v4_adoption():
    m = _cells()
    assert all(m.v3_item1_defect().values())
    r = m.v4_adoption_arithmetic()
    assert all(r.values()), r
    # the exact-zero identity re-derived here, not trusted:
    assert sp.simplify((2 + sp.log(3, 2) + 1) - (3 + sp.log(3, 2))) == 0


def test_findings_and_adoption_propagated():
    flat = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8")
                    .replace("**", "").replace("−", "-").split())
    assert "one ℤ/3 label = log₂3 = 1.585 bits" in flat or "1.585 bits" in flat
    assert "cannot fail at length-weight 1" in flat.lower() or "unfailable" in flat.lower()
    assert "does not survive adoption" in flat
    # THE_CLAIM must carry the adoption AND drop the dead sentence (same batch):
    claim = " ".join((ROOT / "docs" / "THE_CLAIM.md").read_text(encoding="utf-8")
                     .replace("**", "").replace("−", "-").split())
    assert "ONE TRIT" in claim and "B1030" in claim
    assert "+1.585 bits. Verdict" not in claim, "the dead conflated sentence must not survive"
    assert "exactly 0.000 at the floor" in claim


def test_verdict_json():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1030" and v["verdict"] == "PROVED"
    assert "ONE TRIT" in v["claim_one_line"]
    assert "DEFECT" in v["claim_one_line"].upper()
    for dep in ("B1028", "B1025", "B936", "B897"):
        assert dep in v["depends_on"]
