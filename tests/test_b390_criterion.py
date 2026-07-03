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
