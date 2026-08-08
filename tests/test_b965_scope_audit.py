"""B965 locks — the LAW_MAP scope audit, and the three fixes it forced."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B965_lawmap_scope_audit"
LAWMAP = ROOT / "docs" / "LAW_MAP.md"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_audit_covered_the_whole_surface():
    r = _res()
    assert r["claim_rows"] >= 160
    assert r["rows_flagged"] == 5 and r["fixes_applied"] == 3


def test_every_flagged_row_was_written_today():
    """The diagnosis: rate, not competence."""
    r = _res()
    assert r["older_rows_flagged"] == 0
    assert "2026-08-08" in r["all_flagged_rows_are_from"]


def test_fix1_the_inference_is_now_marked_as_inferred():
    t = LAWMAP.read_text(encoding="utf-8")
    assert "INFERRED from the rank bookkeeping, NOT computed" in t


def test_fix2_the_cited_facts_are_now_marked_as_cited():
    t = LAWMAP.read_text(encoding="utf-8")
    assert "STANDARD, CITED not re-derived here" in t


def test_fix3_the_bare_VEV_is_gone_from_the_F4_row():
    """The error class B964 retracted, which had survived in a row written today."""
    t = LAWMAP.read_text(encoding="utf-8")
    assert "what a generic 27 VEV does" in t
    assert "two 27 VEVs are FORCED" in t
    assert "every VEV here is a 27 VEV" in t


def test_the_uncomfortable_finding_is_recorded():
    assert contains(CELL / "FINDINGS.md",
                    "retracting a claim does not retract its instances",
                    "a retraction needs a sweep",
                    "compression drops qualifiers",
                    "l139", "l140")


def test_the_heuristics_limits_are_stated():
    assert contains(CELL / "FINDINGS.md",
                    "keyword heuristic", "triage tool",
                    "only", "not that the older corpus is clean")
