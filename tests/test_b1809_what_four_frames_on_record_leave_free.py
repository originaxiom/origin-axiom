"""B1809 -- the census's Table T at (i, zero line), main's own driver of B1656's coupling at B1667's radii."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1809_what_four_frames_on_record_leave_free" / "verification"


def test_table_t_at_i():
    t = json.loads((V / "values_at_i_main.json").read_text(encoding="utf-8"))
    assert t["R (k = -1/2)"]["L_2(i)"]["m2/m3"] == "0.019069"
    assert t["a0 = D2R - E4 R/48 (k = 7/2)"]["L_max(i)"] == {"m1/m3": "0.58547", "m2/m3": "0.73081"}
    assert t["DR (k = 3/2)"]["L_2(i)"]["m2/m3"] == "1"
    c1 = json.loads((V / "referee" / "c1_canonical_values_at_i.json").read_text(encoding="utf-8"))
    assert c1
