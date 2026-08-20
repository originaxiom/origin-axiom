"""B1099 lock: the decided stratum's arithmetic + the record's presence."""
import sympy as sp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_determinant_5_squarefree_and_disc():
    assert sp.factorint(5) == {5: 1}                      # squarefree -> Cor 16 transitivity
    assert sp.factorint(6237) == {3: 4, 7: 1, 11: 1}      # 5 does not divide disc K
    assert 6237 % 5 != 0

def test_reading_record_banked():
    v = ROOT / "frontier/B1099_route_a_counter/arc_verdict.json"
    t = v.read_text()
    assert "Prop 12(i)" in t and "Cor 16" in t and "FRONTIER" in t
