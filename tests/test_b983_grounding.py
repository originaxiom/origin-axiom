"""B983 — locks the grounding: the defined term, the ladder, and the binding pointer."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def test_the_defined_term_exists_and_says_full_relations():
    assert contains(DOCS / "COMPUTE_THE_PROGRAM.md",
                    "compute over the object as full relations",
                    "never as a single manifold")


def test_the_protocol_has_all_seven_steps():
    t = (DOCS / "COMPUTE_THE_PROGRAM.md").read_text(encoding="utf-8")
    for step in ("P0", "P1", "P2", "P3", "P4", "P5", "P6"):
        assert f"**{step}" in t, f"{step} missing from the pre-compute protocol"


def test_the_ladder_grades_every_rung():
    t = (DOCS / "THE_LADDER.md").read_text(encoding="utf-8")
    for grade in ("BLIND", "HOLE", "BROKEN", "BOUNDED", "OPEN"):
        assert grade in t, f"grade {grade} missing"


def test_the_ladder_covers_the_named_blind_spots():
    """The rungs nobody had ever asked about, as of 2026-08-09."""
    t = (DOCS / "THE_LADDER.md").read_text(encoding="utf-8").lower()
    for rung in ("quantum mechanics", "black hole", "dark matter",
                 "inflation", "strong cp", "neutrino", "doublet"):
        assert rung in t, f"blind rung '{rung}' missing from the ladder"


def test_working_rules_binds_the_grounding():
    assert contains(ROOT / "WORKING_RULES.md",
                    "COMPUTE_THE_PROGRAM.md", "THE_LADDER.md", "THE_FRAMEWORK.md")


def test_the_scope_sentence_rule_is_recorded_in_both_places():
    rule = "scope sentence names no manifold"
    assert contains(DOCS / "COMPUTE_THE_PROGRAM.md", rule)
    assert contains(DOCS / "THE_LADDER.md", rule)


def test_the_campaign_registers_the_order_and_the_stop_rules():
    """B987: the ladder is a list; the campaign is the order it is executed in."""
    t = (DOCS / "THE_CAMPAIGN.md").read_text(encoding="utf-8")
    for wave in ("WAVE 1", "WAVE 2", "WAVE 3", "WAVE 4"):
        assert wave in t, f"{wave} missing"
    assert "STOP RULES" in t
    assert "A criterion that cannot fail is not a test" in t
    assert "Propose and refute in the same file" in t


def test_the_campaign_puts_repairs_before_frontiers():
    """BROKEN outranks BLIND -- a wrong claim misleads, a missing one waits."""
    t = (DOCS / "THE_CAMPAIGN.md").read_text(encoding="utf-8")
    assert t.index("WAVE 1 — REPAIRS") < t.index("WAVE 4 — BLIND")
    assert "BROKEN before BLIND" in t


def test_working_rules_binds_the_campaign():
    assert contains(ROOT / "WORKING_RULES.md", "THE_CAMPAIGN.md")


def test_the_decadal_review_certifies_document_currency():
    """B988: the owner's concern -- no md document may misrepresent the current state."""
    t = (ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8")
    for step in ("7a", "7b", "7c", "7d"):
        assert f"**{step}" in t, f"review step {step} missing"
    assert "doc_currency.py" in t, "the mechanical check must be named"
    assert "A debt is not an exemption" in t


def test_the_review_reads_every_room():
    t = (ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8").lower()
    for room in ("claims", "the chain", "the negatives", "method",
                 "speculation", "interpretation", "logs"):
        assert room in t, f"room '{room}' missing from the currency reading"


def test_the_review_checks_the_named_chain_including_its_thin_links():
    t = (ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8").lower()
    for way in ("aabb", "metallic", "figure-eight", "monodromy", "cusp", "seam",
                "torus", "puncture", "markov blanket", "feedback", "gauge groups"):
        assert way in t, f"chain waypoint '{way}' missing from the review check"


def test_the_review_cannot_pass_silently_over_a_stale_room():
    """The clause that makes step 7 real."""
    assert contains(ROOT / "docs" / "progress" / "REVIEWS.md",
                    "without being misled by any document in it",
                    "names what blocks it")
