"""B1181 lock -- RETRACTED at B1235 (the closure was measured by an orientation-blind method); the
one-way family test method-law it minted STANDS and this retraction is that law's second instance.

E53 rule 3 applied to itself: the previous version of this file pinned the string "83 of 83" and asserted
that reproduce.sh used is_isometric_to as "the reliable method". A lock that pins the assertion is the
error's second copy. This version pins the FACT (38/112 by the proper test) and the RETRACTION."""
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_arc_verdict_is_retracted_and_names_its_successor():
    d = json.loads((ROOT / "frontier" / "B1181_amphichirality_closure" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1181" and d["verdict"] == "RETRACTED"
    assert d["superseded_by"] == "B1235"
    assert d["creates_law"] is False  # method-laws live in LAW_MAP sec-G, not the theorem registry


def test_law_map_row_survives_the_retraction():
    lm = (ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    assert "THE ONE-WAY FAMILY TEST" in lm and "a CLAIM, never a setting" in lm


def test_the_fact_by_the_proper_method():
    """38 amphichiral of 112 (B1235 cell 1). The mirror-isometry call is orientation-blind (REPRODUCIBILITY.md:73);
    the proper test is the symmetry group's is_amphicheiral(). o10_150700 -- B1181's own 'spot-verified' witness --
    is CHIRAL under it."""
    rows = json.loads((ROOT / "frontier" / "B1235_two_seat_harvest" / "verification" / "chirality_112.json")
                      .read_text(encoding="utf-8"))
    assert len(rows) == 112
    assert sum(1 for r in rows if r["amphicheiral"] is True) == 38
    assert next(r for r in rows if r["name"] == "o10_150700")["amphicheiral"] is False
    snappy = pytest.importorskip("snappy")
    assert snappy.Manifold("o10_150700").symmetry_group().is_amphicheiral() is False


def test_the_addenda_carry_the_correction():
    for rel in ("frontier/B1163_w0_attempt/ADDENDUM_2026-09-02_family_is_38_of_112_B1235.md",
                "frontier/B1181_amphichirality_closure/ADDENDUM_2026-09-02_retracted_B1235.md",
                "frontier/B1186_family_is_112/ADDENDUM_2026-09-02_chirality_B1235.md"):
        t = (ROOT / rel).read_text(encoding="utf-8")
        assert "38" in t and "B1235" in t, rel
