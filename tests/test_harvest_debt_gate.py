"""B1307 lock -- the harvest-debt gate: (1) the synthetic two-sided controls (planted NEW item reported, harvested one not,
planted missing index id in BACKLOG, planted stale row flagged, ageing at 21 days) run live; (2) the relay grammar sees every
lane; (3) the pins table parses and names every branch seat; (4) a live run on this tree returns 0 or 2 (never an integrity
failure) and reports every seat; (5) the gate is registered in the runner and `review-due` prints the strict debt."""
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "checks" / "harvest_debt.py"


def _mod():
    spec = importlib.util.spec_from_file_location("harvest_debt", CHECKER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_selftest_passes_and_can_fail():
    m = _mod()
    assert m.selftest() == []
    m.STALE_DAYS = 30                       # the ageing control must notice a wrong constant
    assert any("ageing" in f for f in m.selftest())
    m.STALE_DAYS = 21
    assert m.selftest() == []


def test_reconcile_is_two_sided():
    m = _mod()
    r = m.reconcile({"a", "b", "c"}, [{"a"}, {"b"}], {"c": 3, "b": 1})
    assert r["new_unrowed"] == ["c"] and r["new_rowed"] == ["b"] and r["backlog"] == ["c"]
    r = m.reconcile({"a"}, [{"a"}, {"z"}], {})
    assert r["stale_rows"] == ["z"] and r["backlog"] == []
    assert m.reconcile({"c"}, [], {"c": 22})["aged"] == ["c"] and m.reconcile({"c"}, [], {"c": 21})["aged"] == []


def test_relay_grammar_sees_every_lane():
    m = _mod()
    for name in ("SM_TO_CC_2026-09-08_THE_TOWER.md", "FC_TO_CC_2026-09-06_THE_LIFT_AND_THE_THIRD_ROOT.md",
                 "CODEX_TO_CC_2026-08-30_R030_PHI_COVER_SPECIALIZATION.md", "CLOUD_TO_CC_2026-09-08_Q1_THE_QUANTUM_FACE.md",
                 "CC3_TO_CC_2026-07-28_rank4_response.md", "CC_TO_ALL_SEATS_2026-09-08_HARVEST_NUMBERING.md"):
        assert m.RELAY_FILE_RE.fullmatch(name), name
    for name in ("FINDINGS.md", "THE_TOWER_2026-09-08.md", "INDEX_R56-R72.md"):
        assert not m.RELAY_FILE_RE.fullmatch(name), name


def test_pins_table_names_every_branch_seat():
    m = _mod()
    pins = m.read_pins((ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8"))
    assert pins is not None
    assert set(pins) >= {s["key"] for s in m.SEATS}, set(s["key"] for s in m.SEATS) - set(pins)


def test_live_run_reports_every_seat_and_never_breaks_integrity(tmp_path):
    out = tmp_path / "r.json"
    r = subprocess.run([sys.executable, str(CHECKER), "--json", str(out), "--quiet"], capture_output=True, text=True, timeout=600)
    assert r.returncode in (0, 2), r.stdout[-1500:] + r.stderr[-1500:]
    rep = json.loads(out.read_text(encoding="utf-8"))
    assert rep["integrity"] == []
    m = _mod()
    for s in m.SEATS:
        assert s["key"] in rep["seats"]
    # the seats whose remote is configured here are read, not skipped
    configured = set(subprocess.run(["git", "-C", str(ROOT), "remote"], capture_output=True, text=True).stdout.split())
    for s in m.SEATS:
        if s["remotes"][0] in configured and rep["seats"][s["key"]].get("skipped", "").startswith("remote"):
            raise AssertionError(f"{s['key']} skipped although its remote is configured")


def test_registered_in_the_runner_and_in_review_due():
    sys.path.insert(0, str(ROOT / "scripts" / "gates"))
    import gates  # noqa: E402
    assert "harvest-debt" in gates.GATES
    src = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    assert "--strict" in src.split('sys.argv[1] == "review-due"')[1].split("sys.exit(0)")[0]
