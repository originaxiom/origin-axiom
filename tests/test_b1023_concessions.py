"""B1023 — locks: the corrected authorities, the pin, and the sealed file's survival."""
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_gate5_cites_the_real_authorities():
    t = (ROOT / "WORKING_RULES.md").read_text(encoding="utf-8")
    flat = " ".join(t.split())
    assert "obstructs sector-by-sector" in flat
    for a in ("B811", "B813", "B936", "B782"):
        assert a in flat, f"Gate 5's clause must cite {a}"
    assert "DISCHARGED (B650/B644)" in flat, "the two-functors correction must stay stated"


def test_r11_carries_the_pin_v2():
    t = (ROOT / "docs" / "CROSSING_REQUIREMENTS.md").read_text(encoding="utf-8")
    flat = " ".join(t.replace("**", "").split())
    assert "FRAME-SELECTORS" in flat and "CALIBRATION CONSTANTS" in flat
    assert "2 \u2264 d \u2264 4" in flat or "2 <= d <= 4" in flat or "deficit is 2" in flat, (
        "Blocker 1: the deficit range must stay open until L153")
    assert "WITHDRAWN" in flat and "SIGHTED in" in flat, (
        "Blocker 2: the B1012-externality license must stay withdrawn")
    assert "OUTPUT" in flat and "SHRINKS" in flat, "L154's stakes must stay stated"
    assert "consumes neither type" in flat.lower()


def test_the_two_leads_are_registered():
    t = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    flat = " ".join(t.replace("**", "").split())
    assert "L153" in flat and "no identifying arc" in flat.lower()
    assert "L154" in flat and "c = 6 is DERIVED" in flat.replace("**","")
    assert "sighted" in flat.lower()


def test_the_sealed_declaration_survives_its_addendum():
    """The correction pattern for sealed files: addendum beside, never an edit inside."""
    d = (ROOT / "frontier" / "B1015_anchor_declaration")
    manifest = (d / "ARTIFACT_HASHES.txt").read_text().split()[0]
    actual = hashlib.sha256((d / "DECLARATION.md").read_bytes()).hexdigest()
    assert actual == manifest, "the sealed DECLARATION was edited -- corrections go in the addendum"
    assert (d / "ADDENDUM_2026-08-10.md").is_file()
    add = (d / "ADDENDUM_2026-08-10.md").read_text()
    flat_add = " ".join(add.split())
    assert "unit freedom" in flat_add and "HELD-PENDING-L154" in flat_add


def test_b1009_carries_the_citation_correction_and_the_refusal_stands():
    f = (ROOT / "frontier" / "B1009_verification_pass" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "SECOND ADDENDUM" in f and "DISCHARGED" in f
    flat = " ".join(f.split())
    assert "The refusal itself STANDS" in flat.replace("**", ""), (
        "correcting the citations must not be read as withdrawing the refusal")
