"""B1811 -- the symmetry-selection values against the six (sealed; NEGATIVE as sealed): the committed comparison's cells."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1811_the_symmetry_selection_values_against_the_six" / "verification"


def test_the_sealed_cells():
    c = json.loads((V / "comparison.json").read_text(encoding="utf-8"))
    assert c["cells"]["DECISIVE_P1_and_P2_seat_0.1pc"] is False and c["cells"]["P1_chi2_six_below_16.75_seat"] is False
    assert c["cells"]["C1_control"] is True and c["cells"]["C2_control_chi2_reproduces_B1735"] is True
    assert c["chi2"]["six|seat"]["min"] > 1000
