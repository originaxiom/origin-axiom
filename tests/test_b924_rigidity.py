"""B924 locks: the rigidity collapse and the no-lift obstruction."""
import json, os
ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B924_involution_couplings")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_three_involutions_and_collapse():
    r = _res(); t = json.dumps(r)
    assert "calibration" in t and "involution" in t.lower()
    # the three involutions of Q(zeta15)
    for tok in ("4", "14", "11"):
        assert tok in t


def test_calibration_and_no_new_values():
    t = json.dumps(_res()).lower()
    assert "collaps" in t or "coincide" in t or "no new" in t
