"""The end-to-end chain view: currency locks.

The chain is a VIEW (no new mathematics). These locks guard the one thing a
narrative document can get dangerously wrong: claiming a falsifier is pending
when it has already fired.
"""
import os
import re

DOC = os.path.join(os.path.dirname(__file__), "..", "docs",
                   "THE_END_TO_END_CHAIN.md")


def _t():
    with open(DOC) as f:
        return f.read()


def test_the_falsifier_is_recorded_as_fired():
    t = _t()
    # all three crossings named with their verdicts
    assert "B915" in t and "15.97" in t
    assert "B925" in t and "OUTCOME B" in t
    assert "B929" in t and "HIT-SHAPE" in t
    assert "not Pati" in t or "NOT Pati" in t


def test_the_standing_ruling_is_present():
    t = _t()
    assert "M0" in t and "standing default" in t
    assert "hemisphere check" in t.lower()


def test_the_value_layer_currency():
    t = _t()
    assert "B936" in t and "coboundary" in t.lower()
    assert "frame-relative" in t
    assert "B928" in t and "sigma_" in t or "σ_χ₋" in t


def test_the_view_claims_no_new_mathematics():
    t = _t()
    assert "it is a VIEW" in t or "is a VIEW" in t
