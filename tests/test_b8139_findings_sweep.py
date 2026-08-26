"""Lock: no arc carries a verdict without a findings document, and the sweep's own record is honest."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8139_findings_omission_swept/results.json").read_text())

def test_no_arc_has_a_verdict_without_a_findings_document():
    bad = [d.name for d in (ROOT / "frontier").iterdir()
           if d.is_dir() and (d / "arc_verdict.json").is_file()
           and not any((d / n).is_file() for n in ("FINDINGS.md", "VERDICT.md"))]
    assert not bad, bad[:10]

def test_every_verdict_is_in_the_live_sealed_vocabulary():
    allowed = {"PROVED", "NEGATIVE", "OPEN", "RETRACTED"}
    bad = [(p.parent.name, json.loads(p.read_text()).get("verdict"))
           for p in (ROOT / "frontier").glob("*/arc_verdict.json")
           if json.loads(p.read_text()).get("verdict") not in allowed]
    assert not bad, bad[:6]

def test_instrument_is_a_bool_everywhere():
    bad = [p.parent.name for p in (ROOT / "frontier").glob("*/arc_verdict.json")
           if not isinstance(json.loads(p.read_text()).get("instrument"), bool)]
    assert not bad, bad[:6]

def test_the_reconstructions_are_marked_not_backdated():
    d = ROOT / "frontier/B8110_scale_factorisation/FINDINGS.md"
    t = d.read_text()
    assert "RECONSTRUCTED 2026-08-26" in t and "NOT contemporaneous" in t

def test_the_root_cause_is_recorded_as_cost_not_weakness():
    f = R["the_finding"]
    assert "EXISTS AND WORKS" in f["why_undetected"]
    assert "never REACHED" in f["the_lesson"]

def test_normalised_verdicts_preserve_their_originals():
    for a in ("B8068_j2t_charge_field", "B8080_assembly_classification"):
        d = json.loads((ROOT / "frontier" / a / "arc_verdict.json").read_text())
        assert d.get("verdict_original") and d.get("verdict_normalisation_note")

def test_the_owner_email_conflict_is_flagged_not_silently_fixed():
    f = R["flagged_for_the_owner"]
    assert "FLAGGED, not touched" in f["why_not_fixed_here"]
