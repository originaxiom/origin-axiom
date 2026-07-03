"""Locks for B390 -- the locality criterion (P67)."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B390_criterion_tensor")
R = json.load(open(os.path.join(HERE, "criterion.json")))


def test_g1_tensor_identity_all_pairs():
    assert all(v["G1"] is True for v in R.values())


def test_g2_local_classification_12_of_12():
    for k, v in R.items():
        assert v["match"] is True
        if v["status"] == "dark":
            assert v["n_s_cells"] == 0
        else:
            assert v["n_s_cells"] > 0


def test_out_of_sample_2_5():
    O = json.load(open(os.path.join(HERE, "out_of_sample_25.json")))
    assert O["prediction"] == "dark" and O["verdict"] == "dark" and O["match"] is True


def test_attribution_pairing():
    A = json.load(open(os.path.join(HERE, "attribution.json")))
    assert A["rankB"] == 2
    assert A["1,5"]["all5_right"] is True and A["4,5"]["all5_right"] is True
    for k in ("1,3", "1,4", "3,5"):
        assert A[k]["all5_right"] is False and A[k]["all3_left"] is False
        assert A[k]["attribution"].startswith("KILL-C")
    for k in ("3,4", "2,3"):
        assert A[k]["status"] == "bright"
