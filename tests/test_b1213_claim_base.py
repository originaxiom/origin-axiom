"""B1213 — the claim base must not depend on a field 89% of the corpus never filled."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1213_claim_base_rebuilt"
POOL = ROOT / "papers" / "P3_THE_PAPER" / "CLAIM_CANDIDATES.md"


def _res():
    return json.loads((ARC / "b1213_results.json").read_text(encoding="utf-8"))


def test_the_declaration_census_is_recorded_as_measured():
    """The finding that forced the rebuild. If the field ever gets populated corpus-wide this
    fails, and the base should then be re-derived rather than assumed still broken."""
    r = _res()
    assert r["absent"] > 0.8 * r["settled"], "the field's absence is the premise of this rebuild"
    assert r["absent_pct"] >= 85


def test_the_vocabulary_criterion_carries_its_two_sided_control():
    """MB12: a criterion adopted without a discriminating control is a wish. The control must be
    recorded AND passing — a criterion that scored the same on both sides would prove nothing."""
    c = _res()["control"]
    assert c["passes"] is True
    assert c["ratio"] >= 1.5, f"declared-law vocabulary must separate from the rest; got {c['ratio']}"
    assert c["declared_mean"] > c["rest_mean"]


def test_the_pool_is_a_union_and_not_the_flag_alone():
    """The whole repair: arcs the flag cannot see must still reach the page."""
    r = _res()
    assert len(r["pool_new"]) > len(r["pool_old"])
    added = r["added_by_vocabulary"]
    assert added, "if the vocabulary criterion adds nothing, the union is decoration"
    assert len(added) >= 20


def test_the_rendered_document_is_the_pool_not_a_subset():
    """B1210's actual leak: the pool held 442 and the page listed 48. The page must now carry the
    pool, or the rebuild has fixed a number nobody reads."""
    text = POOL.read_text(encoding="utf-8")
    listed = set(re.findall(r"\| `(B\d+)` \|", text))
    pool = set(_res()["pool_new"])
    missing = sorted(pool - listed, key=lambda a: int(re.sub(r"\D", "", a) or 0))
    assert not missing, f"{len(missing)} pool arcs absent from the rendered page: {missing[:8]}"


def test_the_tier_is_shown_so_an_editor_knows_why_each_arc_is_there():
    text = POOL.read_text(encoding="utf-8")
    assert "| tier |" in text and "vocabulary criterion" in text
    for t in ("**L**", "**S**", "**V**"):
        assert t in text, f"tier legend missing {t}"


def test_the_disposition_stays_an_editorial_call():
    text = POOL.read_text(encoding="utf-8")
    assert "editorial call" in text
    assert "IN** / **SUP** / **OUT" in text or "IN / SUP / OUT" in text
