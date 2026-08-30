"""B1155 lock -- SEAM-A (the prize) = INDETERMINATE, leaning MISMATCH. Gate 1 (codex's zeta12=K(sqrt3)/
dP6xdP6) satisfied, Gate 2 (cc3's full arithmetic-CS action of m004) NOT; the runnable sqrt3 hinge is
banked as the real finite<->archimedean bridge over K=Q(sqrt-3), but that is not the heterotic axiom
collapsing. Asserts on COMMITTED files only (cc3 B8141 the artifact class). No crossing; Gate 5 untouched."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1155_seam_a"


def _d():
    return json.loads((ARC / "b1155_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open_indeterminate():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1155" and d["verdict"] == "OPEN"


def test_gates_gate1_satisfied_gate2_missing():
    d = _d()
    assert "SATISFIED" in d["gate1_codex_construction"]["status"]
    assert "NOT SATISFIED" in d["gate2_cc3_arith_cs"]["status"]
    assert "INDETERMINATE" in d["verdict_outcome"] and "waits on Gate 2" in d["verdict_outcome"]


def test_sqrt3_hinge_banked():
    d = _d()
    hinge = d["runnable_bridge_sqrt3_hinge"]
    assert "Q(zeta12)=K(sqrt3)" in hinge and "REAL adelic pairing" in hinge
    assert "NOT the heterotic axiom" in hinge
    # committed evidence (own sympy computation), not a gitignored artifact
    ev = (ARC / "verification" / "sqrt3_hinge.txt").read_text(encoding="utf-8")
    assert "zeta12^2 = (1+sqrt-3)/2" in ev and "True" in ev and "Q(zeta12) = K(sqrt3)" in ev


def test_leaning_mismatch_three_banked_facts():
    facts = _d()["leaning_mismatch_three_banked_facts"]
    assert len(facts) == 3
    joined = " ".join(facts)
    assert "B1108" in joined and "OA-C1045" in joined and "OA-C1002" in joined
    assert "finite" in joined.lower() and "Vol" in joined


def test_no_crossing_gate5_untouched():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 untouched" in d["fences"]
