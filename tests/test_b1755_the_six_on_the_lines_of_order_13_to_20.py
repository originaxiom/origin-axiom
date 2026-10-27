"""B1755 -- the six on the lines of order 13, 14, 15, 20.  The committed comparison's cells and the per-line read-out: the
decisive cell holds at 78 of 80 000 on 15 and 20; every line below 16.75 has alpha = 2/5."""
import json, pathlib, hashlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1755_the_six_on_the_lines_of_order_13_to_20" / "verification"


def test_the_sealed_instruments_and_the_cells():
    assert hashlib.sha256((A / "compare.py").read_bytes()).hexdigest().startswith("c96a47ae")
    assert hashlib.sha256((A / "census.py").read_bytes()).hexdigest().startswith("bd9f6aa5")
    c = json.loads((A / "comparison.json").read_text(encoding="utf-8"))
    cells = c["cells"]
    assert cells["D_DECISIVE_specific_on_15_and_20_at_0.1pc_and_not_on_13_nor_14_at_1pc"] and cells["P1_chi2_six_below_16.75_on_15_and_20"]
    assert cells["C1_control"] and cells["C2_control_chi2_reproduces_B1735"]
    six = c["chi2"]["15+20"]["six|seat"]
    assert six["hits"] == 78 and abs(six["min"] - 5.3303) < 1e-3
    assert c["chi2"]["13"]["six|seat"]["fraction_mean"] > 0.01 and c["chi2"]["14"]["six|seat"]["fraction_mean"] > 0.01


def test_every_line_below_the_bar_has_slope_two_fifths():
    pl = json.loads((A / "comparison.json").read_text(encoding="utf-8"))["readout_per_line"]
    below = [v for v in pl.values() if v["chi2_six_seat"] < 16.75]
    assert len(below) == 8 and all(v["alpha"] == "2/5" for v in below)
    assert {v["order"] for v in below} == {15, 20}
