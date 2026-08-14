"""B1035 locks — the receipts and the register."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1035_receipts_and_register"


def _cells():
    spec = importlib.util.spec_from_file_location("b1035_verify", ARC / "b1035_verify.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_v1_v2_v3_all_verify():
    m = _cells()
    assert all(m.v1_theta_receipt().values())
    assert all(m.v2_falsifier_register().values())
    assert all(m.v3_main_register().values())


def test_register_on_main_carries_the_honest_rows():
    t = " ".join((ROOT / "docs" / "FALSIFIER_REGISTER.md").read_text(encoding="utf-8").replace("*", "").split())
    assert "NOT FALSIFIABLE, AND WHY" in t
    assert "Earned confirmations: 1" in t
    assert "cannot be made testable by wording" in t
    assert "WHAT_WOULD_COUNT" in t
    # the two integration hashes:
    assert "f0f336ce" in t and "4ff7fc23" in t


def test_b1021_addendum_closes_the_held_rows():
    a = (ROOT / "frontier" / "B1021_cell9_receipt" / "ADDENDUM_2026-08-12.md").read_text(encoding="utf-8")
    assert "closed by B1035" in a
    assert "f0f336ce" in a and "7ea68d34" in a


def test_verdict():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1035" and v["verdict"] == "PROVED"
    assert "RELAYS ARE UNGATED" in v["claim_one_line"]
    for dep in ("B1021", "B1009", "B999"):
        assert dep in v["depends_on"]
