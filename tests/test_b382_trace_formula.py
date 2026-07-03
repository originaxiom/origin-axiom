"""Locks for B382 leg 1 — the phase-ratio law (banked trace_formula.json)."""

import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B382_why_one_twelfth")
R = json.load(open(os.path.join(HERE, "trace_formula.json")))


def test_phase_ratio_law_on_domain():
    for w in ("1,0", "0,1", "1,1", "2,1", "2,3"):
        assert R[w]["pure_phase"] is True and R[w]["quadratic"] is True


def test_domain_boundary_words_fail_as_classical():
    for w in ("1,3", "3,1"):
        assert R[w]["pure_phase"] is False


def test_universal_linear_part():
    for w in ("1,0", "0,1", "1,1", "2,1", "2,3"):
        assert R[w]["Q"][3] == 7 and R[w]["Q"][4] == 8
