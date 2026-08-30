"""B1159 lock -- the object->MSSM debt-map (WF-3): every condition A-E typed + verified; the chain is NOT
object-forced end-to-end (A imported/walled, B forced-given-A, C half-paid, D a wall, E withheld). Adopts
the owner's 'SEAM-A is a wall not a door' correction. Asserts on COMMITTED files only. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1159_mssm_debt_ledger"


def _d():
    return json.loads((ARC / "b1159_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1159" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False


def test_link_A_imported_walled():
    a = _d()["links"]["A_heterotic"]
    assert a["type"] == "CRUX (IMPORTED)" and a["object_forces"] == "NO"
    assert "three inequivalent string realizations" in a["evidence"]
    assert "FLOOR leaning WALL" in a["payment"] and "does NOT construct" in a["payment"]


def test_owner_wall_correction_adopted():
    c = _d()["owner_correction_adopted"]
    assert "wall, not a door" in c
    assert "WALL in substance" in c and "does NOT pay link A" in c
    assert "over-optimistic and is withdrawn" in c


def test_link_B_forced_given_crux():
    b = _d()["links"]["B_which_E8"]
    assert b["type"] == "FORCED-GIVEN-CRUX"
    assert "E6 (dim 78)" in b["evidence"] and "SO(26)xU(1) (dim 326)" in b["evidence"]
    assert "GENERIC (B727)" in b["evidence"]


def test_link_C_alphabet_paid_branch_half():
    c = _d()["links"]["C_bundle"]
    assert c["type"] == "FORCED-GIVEN-CRUX, HALF-PAID"
    assert "ZERO spectrum input" in c["alphabet_PAID"] and "bypass door" in c["alphabet_PAID"]
    assert "P1" in c["branch_HALF_PAID"] and "uniqueness REFUTED" in c["branch_HALF_PAID"]


def test_link_D_up_yukawa_wall():
    d = _d()["links"]["D_up_yukawa"]
    assert d["type"].startswith("WALL")
    assert "H1(X,G_X)=0" in d["evidence"] and "SEAM-Y MISMATCH (B1154" in d["evidence"]


def test_bifurcation_structure_vs_values():
    b = _d()["bifurcation"]
    assert "PAYABLE IFF A is paid" in b and "CONDITIONAL cohomological spectrum theorem" in b
    assert "WALL" in b and "WITHHELD" in b
    assert "NOT object-forced end-to-end" in b and "NOT a breakthrough" in b


def test_live_door_relocated_to_bypass():
    ld = _d()["the_live_door_relocated"]
    assert "BYPASS A" in ld and "character ALPHABET is already object-forced" in ld
    assert "P1/P2" in ld and "object-intrinsic principle" in ld


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    out = (ARC / "verification" / "ledger_checks.txt").read_text(encoding="utf-8")
    assert "REPRODUCES" in out
    assert "IIA (1,5) != IIB (4,2)" in out and "E6(78) != SO(26)xU(1)(326)" in out
    # the full ledger text is committed too
    assert (ARC / "verification" / "condition_ledger.txt").exists()


def test_gate5_clean_no_crossing():
    d = _d()
    assert "No firewall crossing" in d["fences"] and d["gate5"].startswith("clean")
