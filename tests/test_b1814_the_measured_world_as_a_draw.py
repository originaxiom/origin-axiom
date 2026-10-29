"""B1814 -- the measured world as a draw from the weave's own measure: the sealed cells and the controls, from the committed output."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1814_the_measured_world_as_a_draw_from_the_weaves_own_measure" / "verification"


def test_the_cells_as_sealed():
    c = json.loads((V / "comparison.json").read_text(encoding="utf-8"))
    cells = c["cells"]
    assert cells["D1_the_unforced_world_typical_under_the_geometric_clock"] and cells["D1h_by_hand_typical_under_the_geometric_clock"]
    assert not cells["D2_the_clock_depths_typical_under_A1_not_A0"]
    assert cells["C1_census_controls"] and cells["C2_control_chi2_reproduces_B1735"]
    r = c["results"]
    assert abs(r["A1|unforced"]["six"]["p_nn"] - 0.0719) < 1e-3 and abs(r["A0|unforced"]["six"]["p_F"] - 0.0686) < 1e-3
    assert all(v >= 0.01 / c["m"] for v in (c["specificity_r"]["D1"], c["specificity_r"]["D1h_free"], c["specificity_r"]["D2"]))
    assert c["power"]["A1 draws atypical under A0"]["p_F <= 0.05"] < 0.25
