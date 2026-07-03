"""Locks for B401 -- the sixth angle (class field theory of Q(sqrt-15))."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B401_sixth_angle")


def test_p1_orbits():
    R = json.load(open(os.path.join(HERE, "p1_p2.json")))
    assert R["orbit"]["slot"]["equals_minus"] == "3block"
    assert R["orbit"]["face_B382"]["equals"] == "face_B397"


def test_p1_prediction_confirmed():
    P = json.load(open(os.path.join(HERE, "p1_prediction.json")))
    assert P["match"] is True
    assert P["partials"]["1"] == ["0", "0", "-1/16", "1/16"]
    assert P["partials"]["5"] == ["0", "0", "-1/48", "1/48"]


def test_p2_spectroscopy_anchors():
    R = json.load(open(os.path.join(HERE, "p1_p2.json")))
    s = R["spectroscopy"]
    assert s["23"]["cls"] == "nonprincipal" and s["2"]["cls"] == "nonprincipal"
    assert s["7"]["cls"] == "inert" and s["11"]["cls"] == "inert"
    assert s["3"]["cls"] == "ramified" and s["5"]["cls"] == "ramified"


def test_p3_eisenstein_gate_and_equipartition():
    R = json.load(open(os.path.join(HERE, "p3_genus.json")))
    assert R["chi5=1,chi3=1"]["partial"][2] == "0"
    assert R["chi5=-1,chi3=1"]["partial"][2] == "0"
    assert R["chi5=1,chi3=-1"]["partial"][2] == "-1/24"
    assert R["chi5=-1,chi3=-1"]["partial"][2] == "-1/48"
    assert R["cls5,chi3=1"]["partial"] == ["0", "0", "-1/96", "-1/96"]
    assert R["cls5,chi3=-1"]["partial"] == ["0", "0", "-1/96", "-1/96"]
    assert R["cls5,chi3=1"]["cells"] == 4 and R["cls5,chi3=-1"]["cells"] == 64
