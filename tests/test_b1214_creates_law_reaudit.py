"""B1214 — the creates_law re-audit. The locks keep the recovered laws registered and the audit honest."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1214_creates_law_reaudit"
LAWS = ["B393", "B557", "B727", "B885", "B886", "B910", "B918", "B952", "B991", "B996", "B997",
        "B1070", "B1073"]


def _arcs():
    for p in ROOT.glob("frontier/*/arc_verdict.json"):
        try: v = json.loads(p.read_text(encoding="utf-8"))
        except Exception: continue
        if isinstance(v.get("id"), str): yield v


def test_the_thirteen_declare_and_register_with_dated_notes():
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    by_id = {v["id"]: v for v in _arcs()}
    for a in LAWS:
        v = by_id[a]
        assert v["creates_law"] is True, a
        assert "creates_law_corrected" in v, f"{a}: the flip must be dated, not silent"
        assert a in reg, f"{a} declares creates_law but has no registry row"


def test_the_genericity_theorem_is_registered():
    """B727 is the arc any object-specificity claim must clear -- including the paper's. It was
    invisible to the registry until this audit, and losing it again would be the worst single
    regression available here."""
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "B727" in reg
    i = reg.index("T-E6-RECURRENCE-GENERIC")
    row = reg[i:i + 1400]
    assert "generic" in row and "ADE" in row
    assert "arithmetic atom" in row, "the row must say what SURVIVES the genericity"


def test_absence_became_a_decision_not_a_silence():
    """The audit's real product: 104 arcs that had no call now carry a dated, classified one."""
    reviewed = [v for v in _arcs() if "creates_law_reviewed" in v
                and v["creates_law_reviewed"].get("arc") == "B1214"]
    assert len(reviewed) >= 100, f"only {len(reviewed)} carry a recorded decision"
    for v in reviewed[:20]:
        r = v["creates_law_reviewed"]
        assert r["decision"] == "false" and r["class"], v["id"]
        assert "basis" in r, "each decision must record how it was reached"


def test_the_read_asymmetry_is_declared():
    """13 read in full, 104 classified from headlines. That asymmetry runs the safe way and must
    stay stated -- an audit that hides how carefully each call was made is not an audit."""
    r = json.loads((ARC / "b1214_results.json").read_text(encoding="utf-8"))
    a = r["asymmetry_declared"]
    assert "in full" in a and "headline" in a
    assert "safe way" in a


def test_the_unlocked_laws_are_visible_rather_than_blank():
    """Registered-and-unlocked is a state worth seeing; the registry says so in the lock column."""
    r = json.loads((ARC / "b1214_results.json").read_text(encoding="utf-8"))
    sf = r["second_finding"]
    assert set(sf["laws_with_no_lock_at_all"]) == {"B1070", "B1073"}
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "NO LOCK" in reg, "the absence of a lock must be written, not left blank"


def test_the_field_was_not_mass_set():
    """Setting 828 unadjudicated arcs would be the over-declaration flood in reverse. The base does
    not depend on the field (B1213); the field stays honestly blank where unexamined."""
    r = json.loads((ARC / "b1214_results.json").read_text(encoding="utf-8"))
    after = r["field_state"]["after"]
    assert after["absent"] > 500, "the unexamined band must remain absent, not be filled wholesale"
    assert "union criterion" in r["deliberately_not_done"]
