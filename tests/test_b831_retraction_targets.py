"""B831 — locks that a retraction is recorded on its TARGET, not only on the auditor.

B818 established that an arc which withdraws ANOTHER arc's claim is labelled by what IT
established, and the retraction lands on the target's record. That rule is only useful if the
target's record actually changes -- which for B225 and B58 it had not.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _v(rel):
    return json.loads((ROOT / "frontier" / rel / "arc_verdict.json").read_text(encoding="utf-8"))


def test_b225_records_its_own_withdrawn_half():
    v = _v("B225_conductor_decomposition_test")
    assert v["verdict"] == "RETRACTED", "the '2 = octahedral parent' half does not stand (B742/B745)"
    c = v["claim_one_line"]
    assert "VACUOUS" in c and "returns to OPEN" in c, "the withdrawal must be stated"
    assert "SURVIVES" in c and "conductor 40" in c, "the surviving prime-5 result must not be lost"


def test_b58_tower_subarc_records_its_negated_headline():
    v = _v("B58_sl4_tower_test")
    assert v["verdict"] == "RETRACTED"
    assert "NEGATED" in v["claim_one_line"]
    assert "B742" in v["authored_by"] or "B745" in v["authored_by"], "provenance must cite the source"


def test_both_targets_agree_with_their_own_findings_headers():
    """The verdicts are read OFF the arcs, not invented -- each file says so itself."""
    b225 = (ROOT / "frontier" / "B225_conductor_decomposition_test"
            / "FINDINGS.md").read_text(encoding="utf-8")[:400]
    assert "RETRACTED BY B742 + B745" in b225
    b58 = (ROOT / "frontier" / "B58_sl4_tower_test" / "FINDINGS.md").read_text(encoding="utf-8")[:400]
    assert "HEADLINE CORRECTED BY B742 + B745" in b58


def test_the_split_b58_directories_are_still_distinguishable():
    """B58 spans three dirs; two now carry verdicts and they must not be confused."""
    a = _v("B58_phaseA")
    b = _v("B58_sl4_tower_test")
    assert a["verdict"] == "NEGATIVE" and b["verdict"] == "RETRACTED"
    assert a["claim_one_line"] != b["claim_one_line"]
