"""B8114 -- locks the related-work armor: five differentiators, every cite present in the prose."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARC = os.path.join(ROOT, "frontier", "B8114_related_work_armor")
R = json.load(open(os.path.join(ARC, "results.json")))
PROSE = open(os.path.join(ARC, "FINDINGS.md")).read()


def test_there_are_exactly_five_differentiators():
    assert R["n_differentiators"] == 5
    assert len(R["differentiators"]) == 5


def test_every_differentiator_ends_in_a_non_claim():
    for d in R["differentiators"]:
        assert d["not_claimed"].strip()
        assert d["cites"], f"{d['key']} has no citation"


def test_every_citation_appears_in_the_prose():
    """The lock that bites: a cite dropped from FINDINGS.md while left in the data fails here."""
    for d in R["differentiators"]:
        for c in d["cites"]:
            assert c in PROSE, f"citation {c} missing from FINDINGS.md"


def test_the_distler_garibaldi_obstruction_is_recorded_as_chirality():
    e8 = next(d for d in R["differentiators"] if d["key"] == "e8")
    assert "arXiv:0905.2658" in e8["cites"]
    assert "CHIRALITY" in e8["what_they_did"]
    assert "Theorem 1.3" in e8["what_they_did"] or "THEOREM 1.3" in e8["what_they_did"]
    # and our side is a NON-claim, not a counter-claim
    assert "NO CLAIM THAT THE OBJECT SUPPLIES CHIRALITY" in e8["not_claimed"]


def test_c5_is_retyped_to_a_fourth_label_with_a_named_paper():
    assert R["c5"]["typing"] == "NEEDS-READING"
    assert "arXiv:1905.13610" in R["c5"]["why"]
    for wrong in ("literature-empty", "DECIDABLE-HERE"):
        assert wrong in R["c5"]["why"]  # each explicitly considered and rejected


def test_scope_declares_the_date_and_that_nothing_is_recalled():
    assert "2026-08-21" in R["scope"]
    assert "none is recalled" in R["scope"]
