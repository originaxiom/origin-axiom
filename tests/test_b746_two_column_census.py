"""B746 — the two-column law's CENSUS: 10 of 12 declared floors are FORCED-golden.

WHY THIS FILE EXISTS. The structure paper's registry row G11 cites the two-column
law and pointed at `tests/test_b746_golden_ledger.py`. That lock exists and
passes, but it asserts THREE INDIVIDUAL GOLDEN FACTS (S1 the seed discriminant,
S2 the canonical object's factorisation, S3 the chord/tower golden powers) and
contains no mention of floors or columns at all. **The 10-of-12 census — which is
what the paper actually cites G11 for, and which is B746's own headline verdict
("GAPPED — 10/12 floors FORCED-golden; the gap IS the finding") — had no lock.**

This is the same species as the Z_6 defect: an instance was locked, the claim
made in the paper was not.

METHOD, deliberately the same as scripts/checks/forcedness_census.py: do not
restate the census, REGENERATE it from the arc's own ledger table and fail on
drift. A hand-copied count silently rots the moment the arc is edited; a parsed
one cannot.

THE GAP IS LOAD-BEARING AND IS ASSERTED, NOT TOLERATED. B746's finding is that
the hypothesis holds on every STRUCTURAL floor and fails on exactly one kind of
floor. If a later edit ever made it 12/12, that would not be a better result --
it would mean the honest negative had been lost, and this test fails in that
direction too.
"""

import os
import re

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ARC = os.path.join(ROOT, "frontier", "B746_golden_ledger", "FINDINGS.md")

EXPECTED_TOTAL = 12
EXPECTED_FORCED = 10
# The two that are NOT forced, and why -- named, so a drift in WHICH ones fails.
EXPECTED_NOT_FORCED = {"F11": "voice", "F12": "children"}


def _ledger_rows():
    """Parse the arc's own floor table: {floor_id: grade_cell}."""
    return {f: g for f, (g, _a) in _ledger_full().items()}


def _ledger_full():
    """{floor_id: (grade_cell, appearance_cell)} from the arc's own table."""
    with open(ARC, encoding="utf-8") as fh:
        text = fh.read()
    rows = {}
    for line in text.splitlines():
        if not line.startswith("| F"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        m = re.match(r"(F\d+)", cells[0])
        if not m:
            continue
        rows[m.group(1)] = (cells[2], cells[1])
    return rows


def test_arc_is_present_and_parsed():
    """Empty must FAIL, not pass -- a census over nothing is not a census."""
    assert os.path.exists(ARC), f"B746 arc missing: {ARC}"
    rows = _ledger_rows()
    assert rows, "no floor rows parsed from the ledger table"
    assert len(rows) == EXPECTED_TOTAL, (len(rows), sorted(rows))


def test_ten_of_twelve_floors_are_forced_golden():
    """The claim registry row G11 actually makes."""
    rows = _ledger_rows()
    forced = {f for f, g in rows.items() if g.upper().startswith("FORCED")}
    assert len(forced) == EXPECTED_FORCED, sorted(forced)


def test_the_two_gaps_are_the_named_ones():
    """WHICH floors fail matters: the voice is B746's finding, not a rounding error."""
    rows = _ledger_rows()
    not_forced = {f for f, g in rows.items() if not g.upper().startswith("FORCED")}
    assert not_forced == set(EXPECTED_NOT_FORCED), sorted(not_forced)

    # F11 is graded GAP and its APPEARANCE cell is a genuine NONE (zero golden
    # markers in the banked voice artifacts); F12 is OBSERVED-but-not-FORCED.
    full = _ledger_full()
    assert "GAP" in full["F11"][0].upper(), full["F11"][0]
    assert "NONE" in full["F11"][1].upper(), full["F11"][1]
    assert "OBSERVED" in full["F12"][0].upper(), full["F12"][0]


def test_the_honest_negative_cannot_be_silently_upgraded():
    """A drift to 12/12 fails too. The gap is the finding; losing it is a regression."""
    rows = _ledger_rows()
    forced = [f for f, g in rows.items() if g.upper().startswith("FORCED")]
    assert len(forced) != EXPECTED_TOTAL, (
        "all 12 floors now read FORCED -- B746's headline verdict is GAPPED "
        "(10/12, 'the gap IS the finding'). Either the arc was edited wrongly or "
        "a genuine result changed; in the second case update this test DELIBERATELY.")


def test_grades_use_a_closed_vocabulary():
    """A typo'd grade must not silently count as not-forced.

    The arc's grade vocabulary is FORCED / GAP / OBSERVED. (F11 reads "**GAP**
    (as predicted in the sealed prereg)" -- the word NONE lives in its APPEARANCE
    cell, not its grade. Writing this test against the wrong column is how the
    first version of this file failed, which is the whole argument for parsing the
    arc rather than restating it from memory.)"""
    rows = _ledger_rows()
    for floor, grade in rows.items():
        g = grade.upper()
        assert (g.startswith("FORCED") or "GAP" in g or "OBSERVED" in g), (floor, grade)


@pytest.mark.parametrize("floor", sorted(EXPECTED_NOT_FORCED))
def test_named_gap_still_present(floor):
    assert floor in _ledger_rows()
