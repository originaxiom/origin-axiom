"""B1787 -- P210 reviewed and accepted by main.  Main's review record satisfies the audit lane's prospective.py review schema
(binding the sealed specification, a non-authoring reviewer, APPROVE_EXECUTION, unresolved empty) and states the caveats in its
scope; the acceptance, once committed, binds that review."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1787_p210_reviewed_and_accepted_by_main"
SPEC = {"path": "reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_p210/SPECIFICATION.json",
        "sha256": "f33348144c91711b0bcc3a05cf62974aac28a468eb57181f1ea6dfc93077f948"}


def test_main_review_record():
    r = json.loads((A / "MAIN_REVIEW.json").read_text(encoding="utf-8"))
    assert set(r) == {"schema", "experiment_id", "sealed_commit", "specification", "reviewer", "nonauthoring", "source_complete", "decision", "unresolved", "scope"}
    assert r["schema"] == 1 and r["specification"] == SPEC and r["sealed_commit"].startswith("39ce620a8")
    assert r["reviewer"] == "main" and r["nonauthoring"] is True and r["source_complete"] is True
    assert r["decision"] == "APPROVE_EXECUTION" and r["unresolved"] == []
    for caveat in ("P-210 is sharpened, not answered", "missing controls", "generic tau", "fresh clone"):
        assert caveat in r["scope"]


def test_acceptance_binds_the_review_when_present():
    p = A / "ACCEPTANCE.json"
    if not p.exists():
        return
    a = json.loads(p.read_text(encoding="utf-8"))
    assert a["receiver"] == "main" and a["decision"] == "ACCEPT_INDEPENDENT_REVIEW"
    assert a["verified_independence"] is True and a["verified_source_completeness"] is True
    assert a["review"]["path"] == "frontier/B1787_p210_reviewed_and_accepted_by_main/MAIN_REVIEW.json" and a["specification"] == SPEC
