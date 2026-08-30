"""B1144 lock -- the adoption-layer correction: four fixes from the cloud's CORPUS_ADOPTION_AUDIT,
verified (three from golden_gate primary source). The math is untouched in all four; these tests
lock that the CORRECTIONS are in place -- the Q(sqrt-3) convention map banked, B1141's errata
withdrawn, B1138's cert note corrected, B1140's debt cleared, B1139's stale tag flagged."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1144_adoption_audit"


def _read(p):
    return (ROOT / p).read_text(encoding="utf-8")


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1144" and d["verdict"] == "PROVED"


def test_results_math_untouched():
    d = json.loads((ARC / "b1144_results.json").read_text(encoding="utf-8"))
    assert d["math_changed"] is False
    assert d["point1_qsqrt3_basis"]["verdict"] == "cloud right"
    assert d["point2_family_triplet_cartan"]["verdict"] == "cloud right"
    assert d["point4_bl_catch"]["verdict"] == "cloud right"


def test_qsqrt3_convention_map_banked():
    t = _read("TERMINOLOGY.md")
    assert "convention map" in t.lower()
    assert "x²−x+1" in t and "x²+x+1" in t            # both minpolys present
    assert "x²+xy+y²" in t and "x²−xy+y²" in t          # both norms present


def test_b1141_errata_withdrawn():
    t = _read("frontier/B1141_spin_payment/FINDINGS.md")
    assert "WITHDRAWN" in t and "convention map" in t.lower()


def test_b1138_cert_note_corrected():
    t = _read("frontier/B1138_structural_completion/FINDINGS.md")
    assert "CORRECTED B1144" in t and "symmetric and valid" in t


def test_b1140_debt_cleared():
    assert "RESOLVED (B1144" in _read("docs/OPEN_LEADS.md")


def test_b1139_tag_addendum():
    t = _read("frontier/B1139_symmetry_point_table/FINDINGS.md")
    assert "B1144" in t and "stale" in t.lower()


def test_findings_documents_four_fixes_bidirectional():
    t = _read("frontier/B1144_adoption_audit/FINDINGS.md")
    for s in ("§1", "§2", "§3", "§4"):
        assert s in t
    assert "bidirectional" in t.lower()
