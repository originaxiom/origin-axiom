"""Locks for B375 — the four-qubit compilation (banked circuit_simulation.json)."""

import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B375_four_qubit_compilation")
R = json.load(open(os.path.join(HERE, "circuit_simulation.json")))


def test_primitives_exact():
    assert R["UF_unitary_exact"] is True
    assert R["WR_from_primitives_exact"] is True


def test_protocol_theorem():
    assert R["protocol_reproduces_banked_cells"] is True


def test_kappa_word_trace():
    assert R["kappa_word_trace"] == ["1", "0", "0", "0"]
