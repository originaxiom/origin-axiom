"""B1614 -- THE OBSERVER LAYER ON THE WEAVE: the sealed instrument unchanged; the four rungs and the reading cell as recorded."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1614_the_observer_layer_on_the_weave"


def test_sealed_and_recorded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at c04b1acb2: ")
    assert hashlib.sha256(open(ARC / "verification" / "observer_on_the_weave.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "observer_on_the_weave.json"))
    assert d["A1"]["irreducible"].count(True) == 1 and {"x": "0", "y": "0", "z": "0"} in d["A1"]["joint_fixed_points"]
    a2 = d["A2"]
    assert a2["adjoint Ad rho_Q"]["private"] == 0 and a2["adjoint Ad rho_Q"]["H1"] == 3
    assert all(a2[k]["private"] == 2 and a2[k]["H1_puncture"] == 0 for k in a2 if k.startswith("matter block"))
    assert all(a2[k]["private"] == 0 for k in a2 if k.startswith("parity line"))
    assert d["A3"]["fixes_common_point"] and d["A3"]["exchanges_the_sheets"] and d["A3"]["conjugates_have_det_1"]
    assert d["A4"]["sheet_equals_det"] and d["A4"]["sheet_equals_cp"] and not d["A4"]["mckay_equals_sheet"] and d["A4"]["rank_of_the_odd_bits_over_F2"] == 2
    assert abs(d["A5"]["L"]["odd_part_Im"] + 0.707107) < 1e-5 and d["A5"]["LR"]["abs"] == 0.0
