"""B1175 lock -- the charter-close harvest (cloud Addendum 1 + codex R020/R021/R022, all verified)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1175_charter_close_harvest"


def _d():
    return json.loads((ARC / "b1175_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1175" and d["verdict"] == "OPEN"
    assert "C4'" in d["claim_one_line"] and "G-IDENT'" in d["claim_one_line"]


def test_charter_rows_all_moved():
    a = _d()["cloud_addendum1"]
    assert "accepted" in a["g_ident"]
    assert "VERIFIED" in a["c3"]
    assert "REFUTED-AS-STATED" in a["c4"] and "C4'" in a["c4"]
    assert "SUPERSEDED BY THE LAW" in a["c5"]


def test_codex_trio_byte_identical():
    t = _d()["codex_trio_byte_identical"]
    assert "separator confirmed exact" in t["r022"]
    assert "not subset V64" in t["r020"]
    assert "restriction CONSTANT" in t["r021"] and "NOT identified" in t["r021"]


def test_composition_bounded_question():
    c = _d()["composition_with_b1174"]
    assert "one exact question" in c and "theta=cr" in c


def test_reproduce_and_gate5():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    assert "Gate 5 clean" in _d()["fences"]
