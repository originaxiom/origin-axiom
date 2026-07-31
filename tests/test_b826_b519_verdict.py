"""B826 — locks B519's verdict and the widened writer-safety invariant."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B519_re_mining"


def test_b519_carries_its_retraction():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "RETRACTED"
    assert "B826" in v["authored_by"] and "VERDICT.md" in v["authored_by"], (
        "provenance must say the verdict came from the arc's own document, not from invention")


def test_the_verdict_is_sourced_from_the_arcs_own_banner():
    """Not invented: the arc says it itself."""
    t = (ARC / "VERDICT.md").read_text(encoding="utf-8")
    assert "CRACKED by the B525" in t
    assert "this headline is CORRECTED below" in t


def test_b519_has_no_findings_md_and_that_is_fine():
    """The whole point: the arc documents its result in VERDICT.md."""
    assert not (ARC / "FINDINGS.md").is_file()
    assert (ARC / "VERDICT.md").is_file()


def test_the_widened_invariant_is_a_property_not_a_filename():
    """A prereg records INTENT, not result -- admitting it would let a verdict precede the work."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("w2", ROOT / "tests" / "test_b817_wave2.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    assert set(m.FINDINGS_DOCS) == {"FINDINGS.md", "VERDICT.md"}


def test_both_narrow_reads_were_fixed_together():
    """The same invariant was encoded as the same filename in two places (B826's lesson)."""
    b818 = (ROOT / "tests" / "test_b818_retracted_rule.py").read_text(encoding="utf-8")
    assert "VERDICT.md" in b818, (
        "B818's self-retraction-marker check had the same narrow read and must have moved too")
