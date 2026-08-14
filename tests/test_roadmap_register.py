"""The roadmap register lock (owner directive 2026-08-05: no unintentional drift).

Pins: the register exists; the four ladder rungs appear in binding order; the
crossing protocol's non-weakening clause is present verbatim-enough; the drift
rule is present. Amendments are allowed -- silent drift is not.
"""
import os
import re

MP = os.path.join(os.path.dirname(__file__), "..", "docs",
                  "STRUCTURE_TO_NATURE_MASTERPLAN.md")


def _text():
    with open(MP) as f:
        return f.read()


def test_register_exists():
    assert "ROADMAP REGISTER v1" in _text()


def test_ladder_rungs_in_binding_order():
    t = _text()
    idx = [t.index("R1 — the e₆(2) norm cell"),
           t.index("R2 — the 15 atom scales"),
           t.index("R3 — the tree-level coupling-ratio table"),
           t.index("R4 — THE SEALED COMPARISON")]
    assert idx == sorted(idx)


def test_crossing_protocol_not_weakened():
    t = _text()
    clause = " ".join(t[t.index("R4 — THE SEALED COMPARISON"):].split())
    for token in ("ONE measured input", "sealed before any data contact",
                  "two-outcome", "no fitting",
                  "may not be weakened"):
        assert token in clause, f"crossing-protocol token missing: {token}"


def test_drift_rule_present():
    t = _text()
    assert "THE DRIFT RULE" in t
    assert "dated amendment" in t
    assert "never silently absorbed" in t


def test_masterplan_v2_locked():
    t = _text()
    assert "MASTERPLAN v2 — THE THREE CROSSINGS AND THE ONE MEASUREMENT" in t
    # the six phases in binding order
    idx = [t.index("PHASE I — CLOSE THE LEDGER"),
           t.index("PHASE II — THE SECOND CROSSING"),
           t.index("PHASE III — THE ONE MEASUREMENT"),
           t.index("PHASE IV — THE THIRD CROSSING"),
           t.index("PHASE V — THE RESIDUE FRONTIER"),
           t.index("PHASE VI — THE OPENING")]
    assert idx == sorted(idx)


def test_kill_conditions_locked():
    t = " ".join(_text().split())
    assert "THE KILL CONDITIONS (locked — may not be moved, only executed)" in t
    for token in ("R4b MISS", "L113 YES", "Third crossing MISS", "All three HIT"):
        assert token in t


def test_third_crossing_inherits_the_r4_protocol():
    t = " ".join(_text().split())
    clause = t[t.index("PHASE IV — THE THIRD CROSSING"):]
    for token in ("one input", "sealed prereg", "two outcomes", "no fitting"):
        assert token in clause
