"""B1014 — locks: the claim page, the anchor rule, and the meanings they must not lose."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _flat(s):
    return " ".join(s.lower().replace(">", " ").split())


def test_the_claim_page_has_its_three_sections_and_the_sentence():
    t = (ROOT / "docs" / "THE_CLAIM.md").read_text(encoding="utf-8")
    assert "THE DERIVATION THEOREM" in t and "THE ANCHOR DOCTRINE" in t
    assert "THE PREDICTION CHANNEL" in t
    f = _flat(t)
    assert "a choice the sm cannot make about itself" in f, "the Z6 overhang is the headline"
    assert "uncomputed" in f and "l149" in f, "the endpoint control must stay honestly open"
    assert "one real wall" in f or "one tested wall" in f
    assert "one-sentence claim" in f


def test_r11_licenses_anchors_by_theorem_and_keeps_parameter_free_meaning():
    t = (ROOT / "docs" / "CROSSING_REQUIREMENTS.md").read_text(encoding="utf-8")
    assert "R11" in t and "ANCHOR RULE" in t
    f = _flat(t)
    for arc in ("b782", "b936", "b1012"):
        assert arc in f, f"the theorem-backing {arc} must stay cited"
    assert "sealed in advance" in f, "post-hoc anchors must stay forbidden"
    assert "zero free dimensionless parameters" in f
    assert "declare the anchor set" in f, "preparation step 0 must stay"


def test_the_vacuity_tooth_bites():
    """outputs - anchors > 0: the MB12 clause is what stops anchoring from eating the test."""
    raw = (ROOT / "docs" / "CROSSING_REQUIREMENTS.md").read_text(encoding="utf-8")
    flat_keep_gt = " ".join(raw.lower().split())
    assert "anchors > 0" in flat_keep_gt and "vacuous" in flat_keep_gt


def test_L151_is_registered_two_outcome():
    f = _flat((ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8"))
    assert "l151" in f and "anchor budget" in f
    assert "match" in f and "mismatch" in f, "both outcomes must stay stated"


def test_the_verdict_keeps_the_non_claims():
    v = json.loads((ROOT / "frontier" / "B1014_proof_form" / "arc_verdict.json").read_text())
    c = v["claim_one_line"]
    assert "not a crossing" in c.lower()
    assert "ZERO FREE DIMENSIONLESS" in c
