"""Locks for B410 Phase 2b."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B410_coupling_derivation")


def test_2bi_no_window_class_action():
    R = json.load(open(os.path.join(HERE, "b2i_window.json")))
    assert R["exists"] is False


def test_2bii_fullfield_criterion_separates():
    R = json.load(open(os.path.join(HERE, "b2ii_fullfield.json")))
    assert R["separates"] is True
    assert R["fullfield_scounts"]["1,3"] == 0 and R["fullfield_scounts"]["3,4"] == 24
