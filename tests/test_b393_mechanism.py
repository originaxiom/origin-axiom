"""Locks for B393 M1 session 1 -- termwise s-orthogonality."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier",
                    "B393_cancellation_mechanism")
R = json.load(open(os.path.join(HERE, "k1_fullfield.json")))


def test_dark_pairs_termwise_zero():
    assert R["1,3"]["nonzero_terms"] == 0 and R["1,3"]["terms"] == 39
    assert R["3,5"]["nonzero_terms"] == 0 and R["3,5"]["terms"] == 15


def test_bright_controls_have_teeth():
    assert R["3,4"]["nonzero_terms"] == 24
    assert R["2,3"]["nonzero_terms"] == 18


def test_14_completes_the_class():
    r = json.load(open(os.path.join(HERE, "k1_14.json")))
    assert r["nonzero_terms"] == 0 and r["terms"] == 39


def test_product_field_stratification():
    R = json.load(open(os.path.join(HERE, "product_fields.json")))
    assert R["1,4"]["real(x,y)"] == 39 and R["1,4"]["s-carrying"] == 0
    assert R["3,5"]["real(x,y)"] == 15 and R["3,5"]["s-carrying"] == 0
    assert R["1,3"]["z-only"] == 24 and R["1,3"]["s-carrying"] == 0
    assert R["3,4"]["s-carrying"] == 24 and R["2,3"]["s-carrying"] == 18


def test_galois_pattern_does_not_discriminate():
    G = json.load(open(os.path.join(HERE, "galois_why.json")))
    for k, v in G.items():
        pats = [(t["sigma19"], t["sigma31"], t["sigma49"]) for t in v["patterns"]]
        assert sorted(pats, key=str) == sorted([(0, 0, 0), (None, None, 0), (None, None, 0)], key=str)
