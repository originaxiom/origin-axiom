"""P-616 (R76-1, 2026-11-06): the SCHEDULED count reads a row's current disposition, not its history."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "checks"))
import harvest_debt as h


def test_history_does_not_count_as_scheduled():
    assert h.is_scheduled("**SCHEDULED, first item** -- the seat attributes R49 to codex")
    assert not h.is_scheduled("**VERIFIED** -- (2026-09-08 B1303; was: SCHEDULED -- verify on the exact ring)")
    assert not h.is_scheduled("**BANKED (B1305 slice B)** the count half OPEN. Was: RECEIVED, SCHEDULED -- the seven")
    assert not h.is_scheduled("**VERIFIED-EARLIER on main** -- row 261's SCHEDULED is superseded")
    assert h.is_scheduled("**RECEIVED** (was: unread) then SCHEDULED for the next arc")


def test_the_baseline_is_the_count():
    import pathlib
    rows = h.read_rows((pathlib.Path(h.__file__).resolve().parents[2] / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8"))
    assert sum(1 for r in rows if h.is_scheduled(r["disp"])) <= h.SCHEDULED_BASELINE
