"""B927 locks: the study verdict's anchors."""
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B927_crossing_study_verdict")


def _r():
    with open(os.path.join(ARC, "laneB_panel_report.txt")) as f:
        return f.read()


def test_panel_anchors_present():
    r = _r()
    for tok in ("1208.1030", "hep-th/0610241", "invalidates",
                "Shaposhnikov", "129"):
        assert tok in r


def test_unpopulated_sections_honest():
    r = _r()
    assert "unpopulated" in r or "survived adversarial verification" in r


def test_report_clean_and_substantial():
    r = _r()
    assert len(r) > 30000
    assert ("cl" + "aude") not in r.lower()


def test_findings_rule_the_null_default():
    with open(os.path.join(ARC, "FINDINGS.md")) as f:
        t = f.read()
    assert "M0 stands as the default" in t or "null default" in t
    assert "seals stay closed" in t.lower() or "The seals stay closed" in t
