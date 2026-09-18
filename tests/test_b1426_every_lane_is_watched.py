"""B1426 lock -- no lane may exist outside the gate.

harvest_debt.py walks a hard-coded list of seats. A branch absent from that list is not unread, it is
INVISIBLE: no report names it, so no amount of attention finds it. Two lanes were in that state on
2026-09-18, one of which had relayed a written request to be registered two days earlier. These
assertions fail if a lane with unique work is ever again outside the gate's list.
"""
import json
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SURVEY = ROOT / "frontier" / "B1426_the_unwatched_seat" / "verification" / "lane_survey.py"


@pytest.mark.slow
def test_no_lane_with_unique_work_is_outside_the_gate():
    r = subprocess.run([sys.executable, str(SURVEY)], capture_output=True, text=True, cwd=ROOT, timeout=900)
    assert r.returncode == 0, r.stdout[-800:] + r.stderr[-800:]
    res = json.loads((SURVEY.parent / "lane_survey.json").read_text())
    assert not res["unwatched_lanes"], "lane(s) outside the gate: %s" % res["unwatched_lanes"]


def test_both_lanes_are_in_the_gates_seat_list():
    gate = (ROOT / "scripts" / "checks" / "harvest_debt.py").read_text()
    for branch in ("sep16-branch", "paper-review-verification-kaz3f5"):
        assert 'branch="%s"' % branch in gate, "%s is not a seat in the gate" % branch


def test_both_lanes_are_pinned_and_rowed():
    ledger = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text()
    register = (ROOT / "docs" / "SEAT_REGISTER.md").read_text()
    for name in ("sep16-branch", "paper-review-verification-kaz3f5"):
        assert name in ledger, "%s has no harvest pin" % name
        assert name in register, "%s has no seat-register row" % name


def test_the_seat_opening_relay_has_a_row():
    """it proposed its own register row on 2026-09-16 and was not rowed for two days"""
    relays = (ROOT / "docs" / "RELAY_LEDGER.md").read_text()
    assert "XB_TO_CC_2026-09-16_SEAT_OPENED_AND_TWO_DEBTS_PAID.md" in relays


def test_the_survey_measures_shared_history_rather_than_totals():
    """the outside claim was drawn from commit TOTALS; the discriminating facts are root and merge base"""
    res = json.loads((SURVEY.parent / "lane_survey.json").read_text())
    assert res["main_commits"] > 3000
    assert res["every_same_repo_lane_shares_mains_root"] is True
    assert res["every_same_repo_lane_has_a_merge_base"] is True
    assert res["other_repository_lanes"], "the survey no longer separates the other repository's lane"
