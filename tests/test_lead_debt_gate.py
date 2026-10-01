"""lead-debt lock -- leads and OPEN arcs are aged, with a ratchet.

Pins: (1) STALE_DAYS = 21 and the real clock with the OA_LEAD_TODAY test override; (2) the closure marker is a
marker, not the word in a title; (3) a dateless open lead is stale; (4) ESCALATED-by-name excuses; (5) a number
carried by two open leads is a collision and fails; (6) the ratchet fails when the stale count exceeds its baseline --
proved against the real register under a far-future clock (MB12: the gate can fail); (7) the gate is registered.
"""
import datetime
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "checks" / "lead_debt.py"


def _mod():
    spec = importlib.util.spec_from_file_location("lead_debt", CHECKER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_stale_days_is_21_and_the_clock_is_real():
    m = _mod()
    assert m.STALE_DAYS == 21
    os.environ["OA_LEAD_TODAY"] = "2026-10-01"
    try:
        assert m._today() == datetime.date(2026, 10, 1)
    finally:
        del os.environ["OA_LEAD_TODAY"]
    assert m._today() == datetime.date.today()


SAMPLE = """
## L900 — AN OPEN LEAD (registered 2026-09-01, B1)
text
## L901 — THE CLOSED FORM OF SOMETHING (registered 2026-09-01, B1)
the word in a title is not a closure
## L902 — CLOSED 2026-09-02 (B2): done
## L903 — A LEAD WITH NO DATE
text
## L904 — AN ESCALATED LEAD (registered 2026-08-01, B1)
**ESCALATED(2026-09-01, B3): next action named**
## L905 — FIRST LEAD OF THIS NUMBER (registered 2026-09-01, B1)
## L905 — A DIFFERENT LEAD, SAME NUMBER (registered 2026-09-05, B4)
## L906 — A LEAD (registered 2026-09-01, B1)
### L906 — CLOSED 2026-09-03 by B5
"""


def test_parser_closure_date_escalation_collision():
    m = _mod()
    L = m.parse_leads(SAMPLE)
    assert not L["L900"]["closed"] and L["L900"]["date"] == "2026-09-01"
    assert not L["L901"]["closed"], "a title containing the word CLOSED was read as a closure"
    assert L["L902"]["closed"] and L["L906"]["closed"]
    assert L["L903"]["date"] is None and not L["L903"]["closed"]
    assert L["L904"]["escalated"] and not L["L900"]["escalated"]
    assert L["L905"]["collision"] == ["2026-09-01", "2026-09-05"] and not L["L900"]["collision"]


def _run(today, *args):
    env = dict(os.environ, OA_LEAD_TODAY=today)
    return subprocess.run([sys.executable, str(CHECKER), *args], capture_output=True, text=True, env=env)


def test_register_is_within_its_baselines_at_the_landing_date():
    r = _run("2026-10-01")
    assert r.returncode == 0, r.stdout + r.stderr


def test_the_ratchet_fails_in_the_far_future():
    """the enforcement pin: every lead open today is stale by 2027-06-01, far above the baseline"""
    r = _run("2027-06-01")
    assert r.returncode == 1, "stale leads no longer fail the gate"
    assert "baseline" in r.stdout


def test_no_collision_in_the_live_register():
    m = _mod()
    L = m.parse_leads(m.LEADS.read_text(encoding="utf-8", errors="ignore"))
    assert [k for k, d in L.items() if d["collision"]] == []


def test_gate_is_registered():
    sys.path.insert(0, str(ROOT / "scripts" / "gates"))
    import gates
    assert "lead-debt" in gates.GATES
