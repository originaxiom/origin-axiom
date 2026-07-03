"""Locks for B404/P68."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B404_gate_derivation")


def test_root_of_unity_and_gates():
    R = json.load(open(os.path.join(HERE, "root_of_unity.json")))
    assert R["tot"] == 142 and R["not_root"] == 0 and R["gate_viol"] == 0
    assert R["l3_minus"] == ["True"] and sorted(R["l3_plus"]) == ["False", "True"]
