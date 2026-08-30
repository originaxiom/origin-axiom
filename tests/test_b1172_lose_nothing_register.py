"""B1172 lock -- the trigger + the backlog + the register. The relay-debt gate's repairs are locked
separately (tests/test_relay_debt_gate.py); this lock pins the triage's committed state + the register."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1172_lose_nothing_register"


def _d():
    return json.loads((ARC / "b1172_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open_instrument():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1172" and d["verdict"] == "OPEN"
    assert d["instrument"] is True and d["creates_law"] is False
    assert "RETENTION-GAP" in d["claim_one_line"] and "E51" in d["claim_one_line"]


def test_triage_on_the_ledger():
    ledger = (ROOT / "docs" / "RELAY_LEDGER.md").read_text(encoding="utf-8")
    assert "TRIAGED B1172" in ledger                      # p3 closed
    assert ledger.count("ESCALATED(2026-08-27, B1172)") >= 11
    assert "RESEND_NINE_RELAYS" in ledger                 # the re-send ask rowed
    assert "O3 EXECUTED (B1172)" in ledger                # MC1 assignment


def test_leads_and_error_class():
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "## L187" in leads and "depth-closure" in leads.lower()
    assert "## L188" in leads and "reconciliation addendum" in leads
    errors = (ROOT / "docs" / "ERROR_LEDGER.md").read_text(encoding="utf-8")
    assert "E51 the RETENTION gap" in errors
    assert "nothing preserved the untracked FILES" in errors


def test_register_carries_both_wave_queues():
    d = _d()
    assert len(d["the_register_wave2_queue"]) >= 10
    assert len(d["the_register_wave3_queue"]) >= 12
    assert any("Z/2 IDENTIFICATION" in q for q in d["the_register_wave3_queue"])
    assert any("review-carry leak" in q for q in d["the_register_wave2_queue"])


def test_reproduce_runner_committed():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")


def test_gate5_clean():
    assert "Gate 5 clean" in _d()["fences"]
