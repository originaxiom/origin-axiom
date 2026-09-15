"""B1410 lock — the POINT ledger and the H5 predicate.

Pins what DECIDES, not strings (E53's standing fix, and the defect this arc repaired in B1264):
the seal's hash, the decision rule in all four branches, the ledger's recorded verdicts, and the
closure's amendment count — which is the arc's headline metric, because one amendment per awkward
candidate is H5 losing in slow motion and it has to be visible.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1410_the_point_ledger"
CHECKER = ROOT / "scripts" / "checks" / "point_census.py"

# The seal, as recorded in ARTIFACT_HASHES.txt at the commit that pushed it before any compute.
SEAL = "9ac73d7acaa3acf0d733e810d89db5be04a100e0af6ec8e0feaf0a461a4a470d"


def _mod():
    spec = importlib.util.spec_from_file_location("point_census", CHECKER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_preregistration_is_unmodified_since_it_was_sealed():
    """A seal that can be edited afterwards is not a seal. Corrections go in dated addenda."""
    got = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert got == SEAL, f"the sealed prereg changed: {got[:16]} != {SEAL[:16]}"
    recorded = (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert SEAL in recorded, "ARTIFACT_HASHES.txt no longer records the seal it was written for"


def test_the_decision_rule_reaches_all_four_verdicts():
    """If OTHER is unreachable, H5 is analytic and cannot lose. The can-fail witness must fire."""
    c = _mod().classify
    base = {"derivation": {"identifications_used": [], "anchors_T1": 0, "anchors_T2": 0}}
    assert c({**base, "target": {"generated_by_object": False},
              "specificity": {"object_unique": "UNTESTED"}})[0] == "OTHER"
    assert c({**base, "target": {"generated_by_object": True},
              "specificity": {"object_unique": True}})[0] == "SELF"
    assert c({**base, "target": {"generated_by_object": True},
              "specificity": {"object_unique": False}})[0] == "GENERIC"
    assert c({"target": {"generated_by_object": False},
              "derivation": {"identifications_used": ["I-13"], "anchors_T1": 0, "anchors_T2": 0},
              "specificity": {}})[0] == "UNDECIDED"


def test_untested_specificity_never_reads_as_true():
    """E67: the thing that can break is WHICH OBJECT, so object_unique is measured, not declared."""
    c = _mod().classify
    row = {"target": {"generated_by_object": True},
           "derivation": {"identifications_used": [], "anchors_T1": 0, "anchors_T2": 0},
           "specificity": {"object_unique": "UNTESTED"}}
    assert c(row)[0] == "UNDECIDED"


def test_an_anchor_blocks_other_just_as_an_identification_does():
    c = _mod().classify
    for field in ("anchors_T1", "anchors_T2"):
        row = {"target": {"generated_by_object": False},
               "derivation": {"identifications_used": [], "anchors_T1": 0, "anchors_T2": 0},
               "specificity": {}}
        row["derivation"][field] = 1
        assert c(row)[0] == "UNDECIDED", f"{field} does not block OTHER"


def test_the_ledger_classifies_as_the_findings_reports():
    """A silent re-adjudication is caught here rather than discovered later."""
    m = _mod()
    led = json.loads((ROOT / "docs" / "POINT_LEDGER.json").read_text(encoding="utf-8"))
    got = {r["arc"]: m.classify(r)[0] for r in led["rows"]}
    assert got == {"B862": "UNDECIDED", "B287": "UNDECIDED", "B1345": "UNDECIDED"}, got
    # B862 is blocked by the OWED BRIDGE, not by an anchor -- that distinction IS the finding
    b862 = next(r for r in led["rows"] if r["arc"] == "B862")
    assert b862["target"]["generated_by_object"] is False
    assert b862["derivation"]["anchors_T1"] == 0 and b862["derivation"]["anchors_T2"] == 0
    assert len(b862["derivation"]["identifications_used"]) == 1


def test_the_closure_amendment_count_is_visible_and_the_policy_survives():
    d = json.loads((ROOT / "docs" / "OBJECT_CLOSURE.json").read_text(encoding="utf-8"))
    assert "NAMES THE CANDIDATE THAT FORCED IT" in d["amendment_policy"]
    assert len(d["amendments"]) == 0, (
        f"{len(d['amendments'])} closure amendment(s) — each one is H5 absorbing a counterexample "
        f"and must be argued in FINDINGS, not merely recorded: {d['amendments']}")
    # Q(sqrt5) is OUT by a banked theorem, which is what makes the closure a boundary not a convenience
    assert any("sqrt5" in e["structure"] for e in d["out"])


def test_the_calibration_sets_have_not_drifted_from_the_seal():
    """The join rule: this arc's constants and its sealed prereg are two artifacts, checked by one
    command over both. Every self-correction in the preceding window was a join asserted."""
    assert _mod is not None
    m = _mod()
    seal = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    for i in m.MUST_RECOVER + m.MUST_REJECT:
        assert i in seal, f"{i} is calibrated against but absent from the sealed prereg"


def test_the_selftest_passes():
    assert _mod().selftest() == 0
