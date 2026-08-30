"""B1172 lock -- the relay-debt gate's four repairs (the gate was silently dead since 08-09).
Pins: (1) the real-clock today with the OA_RELAY_TODAY test override; (2) stale OPEN rows FAIL
unless ESCALATED-by-name; (3) the widened regex sees every seat lane; (4) dateless OPEN = stale;
(5) STALE_DAYS = 21. Runs the checker as a subprocess against the real ledger with pinned dates."""
import datetime
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "checks" / "relay_debt.py"


def _mod():
    spec = importlib.util.spec_from_file_location("relay_debt", CHECKER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_stale_days_is_21():
    assert _mod().STALE_DAYS == 21


def test_regex_sees_every_seat_lane():
    m = _mod()
    # the B1172 widening: the codex/cloud/all-seats lanes were invisible (the MC1 miss)
    for name in [
        "CC3_TO_CC_2026-08-09_FRAMEWORK_DELTA.md",
        "CC_TO_CC3_2026-08-27_RESEND_NINE_RELAYS.md",
        "CC_TO_CODEX_2026-08-26_MC1_INDEPENDENT_REIMPLEMENTATION.md",
        "CC_TO_CLOUD_2026-08-27_G1_ARENA_RESCOPE.md",
        "CC_TO_ALL_SEATS_2026-08-27_B1169_QUALIA_PARITY_VERIFY.md",
        "CC_TO_CLOUD_CODEX_2026-08-26_CHARTER_C3_VERIFIED_C4_REFUTATION_CANDIDATE.md",
        "CODEX_TO_CC_2026-08-26_YUKAWA_PRIMARY.md",
        "HANDOFF_CC_SELECTION_COCHAIN.md",
        "README_ARC_PROPOSAL.md",
    ]:
        assert m.RELAY_RE.fullmatch(name), f"regex misses {name}"
    # non-relays stay unmatched
    for name in ["FINDINGS.md", "CHANGELOG.md", "THE_GRAVITY_CHARTER.md"]:
        assert not m.RELAY_RE.fullmatch(name), f"regex over-matches {name}"


def test_today_env_override_and_real_clock():
    m = _mod()
    os.environ["OA_RELAY_TODAY"] = "2026-08-27"
    try:
        assert m._today() == datetime.date(2026, 8, 27)
    finally:
        del os.environ["OA_RELAY_TODAY"]
    # without the override: the real clock, never the frozen ledger stamp
    assert m._today() == datetime.date.today()


def test_escalated_marker_recognized():
    m = _mod()
    assert m.ESCALATED_RE.search("xx **ESCALATED(2026-08-27, B1172): FILE LOST** yy")
    assert not m.ESCALATED_RE.search("escalated someday, promise")


def _run(today: str) -> subprocess.CompletedProcess:
    env = dict(os.environ, OA_RELAY_TODAY=today)
    return subprocess.run([sys.executable, str(CHECKER)], capture_output=True, text=True, env=env)


def test_ledger_clean_at_the_triage_date():
    # B1172's triage left the ledger green at its own date: every stale row closed or ESCALATED-by-name
    r = _run("2026-08-27")
    assert r.returncode == 0, r.stdout + r.stderr


def test_stale_unescalated_fails_in_the_far_future():
    # the enforcement pin: at a far-future date, any OPEN row without an ESCALATED marker is stale
    # and the gate FAILS (it used to print and swallow). The ledger always has recent OPEN rows,
    # so this exercises the failure path against the real file.
    r = _run("2027-06-01")
    assert r.returncode == 1, "stale debts no longer fail the gate -- repair 2 regressed"
    assert "STALE" in r.stdout.upper()
