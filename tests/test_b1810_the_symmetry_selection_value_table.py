"""B1810 -- the symmetry-selection value table (P-432, first half): the committed summary."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1810_the_symmetry_selection_value_table" / "verification"


def test_the_summary():
    s = json.loads((V / "symmetry_selection_table.json").read_text(encoding="utf-8"))["summary"]
    assert s["rows"] == 832 and s["controls"] == "hold"
    assert s["V defined"] == 400 and s["V a permutation (full 3x3, 1e-6)"] == 320
    assert s["max |J| where V is defined"] < 1e-25
    assert s["distinct outputs (omega, 0)"] == {"masses": 2, "masses + V": 2}
    ang = s["a0 at (i, (1/2, 1/2)), S~SS: the non-0/1 |V| entries by L"]
    assert ang["L = 2.71926"][0] == 0.101033 and ang["L = 2560"][0] < 1e-4
