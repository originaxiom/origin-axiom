"""Lock for B386 L1 -- the Par-trace tensor identity."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B386_crt_closed_form")


def test_tensor_gate_exact_at_banked_convention():
    R = json.load(open(os.path.join(HERE, "tensor_gate.json")))
    assert R["convention"] == [2, 2] and R["mismatches"] == 0


def test_closed_form_assembles_both_classes():
    R = json.load(open(os.path.join(HERE, "closed_form.json")))
    assert R["class1"]["match"] is True and R["class5"]["match"] is True


def test_class5_offparity_vanishes():
    R = json.load(open(os.path.join(HERE, "closed_form.json")))
    gh = R["class5"]["factors"]["term(6,2)"]["GH"]
    assert gh["01"] == ["0", "0", "0", "0"] and gh["10"] == ["0", "0", "0", "0"]


def test_end_to_end_partials_from_tensor():
    W = json.load(open(os.path.join(HERE, "windowed_split.json")))
    assert W["class1"] == ["0", "0", "-1/16", "-1/16"]
    assert W["class5"] == ["0", "0", "-1/48", "-1/48"]
