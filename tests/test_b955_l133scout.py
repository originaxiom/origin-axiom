"""B955 locks — the L133 scouting result.

The load-bearing locks: (a) the abelian candidate is dead for a KNOT-specific
reason, (b) the group theory must never be claimed as the obstruction, and
(c) the null is not certified.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B955_l133_scout"


def _n(p):
    t = re.sub(r"(?m)^\s*>\s?", "", p.read_text(encoding="utf-8")).replace("*", "")
    return " ".join(t.split())


def test_the_abelian_candidate_is_dead_for_a_knot_specific_reason():
    t = _n(CELL / "FINDINGS.md")
    assert "knot complement has H₁ = ℤ" in t
    assert "preserves rank NECESSARILY, not" in t
    assert "same defect as the measurement operation" in t


def test_the_risk_was_logged_before_the_answer():
    t = _n(CELL / "FINDINGS.md")
    assert "before this panel returned" in t
    b956 = _n(ROOT / "frontier" / "B956_l133_analysis" / "FINDINGS.md")
    assert "RANK-PRESERVING" in b956 and "NOT settled here" in b956


def test_the_group_theory_must_NOT_be_claimed_as_the_obstruction():
    """E6 -> SU(5) via two 27 VEVs keeps the 27 complex. Standard, not novel."""
    t = _n(CELL / "FINDINGS.md")
    assert "already exists" in t
    assert "must not claim" in t.lower()
    assert "Spin(10)" in t


def test_the_knot_constraint_and_the_surviving_hatch():
    t = _n(CELL / "FINDINGS.md")
    assert "cyclic abelianization" in t
    assert "not importable" in t
    assert "A₄" in t and "S₅" in t


def test_the_nearest_exhaustive_scan_skips_rank_four():
    t = _n(CELL / "FINDINGS.md")
    assert "{6, 2, 0}" in t
    assert "never occurs" in t.lower()


def test_the_null_is_explicitly_not_certified():
    t = _n(CELL / "FINDINGS.md")
    assert "NOT certified" in t
    assert "not found by this sweep" in t
    assert "137" in t
