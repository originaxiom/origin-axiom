"""B1870 -- the reports cover the backlog, every command is read-only, the programme's states are the ones this arc records,
and three findings are checked live here.  A live check is written so that REPAIRING a finding does not break this lock: it
asks that the finding still reproduces OR that the programme no longer calls it merely reproduced."""
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REPORTS = json.loads((HERE / "checkers_reports.json").read_text(encoding="utf-8"))
OPEN_BEFORE = "E12 G11 G12 L1 L2 L3 L8 M2 M4 M5 M6 M7 M8 M9 M10 M11 P1 P3 P4 P6 P7 R2 V1 V2 V3 V5 W2 W3 W4 W5 X1 X2 X3 X4".split()
BY_PLANTING = "G6 G7 G8 G9 G10 G14 L7".split()


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


RR = _load("b1870_rerun", HERE / "rerun.py")
S = _load("b1870_programme_source", ROOT / "frontier" / "B1861_the_closure_programme" / "verification" / "programme_source.py")


def test_the_reports_cover_the_backlog_and_tally():
    assert sorted(r["id"] for r in REPORTS) == sorted(OPEN_BEFORE) and len(REPORTS) == 34
    tally = {}
    for r in REPORTS:
        tally[r["checker_verdict"]] = tally.get(r["checker_verdict"], 0) + 1
        assert r["commands"] and len(r["commands"]) == len(r["main_rerun"]), r["id"]
        assert r["minimal_fix"] and r["acceptance_test"], r["id"]
        assert not any(x["rc"] == "TIMEOUT" for x in r["main_rerun"]), r["id"]
    assert tally == {"REPRODUCES": 24, "PARTLY": 9, "CANNOT_CHECK": 1}
    blob = json.dumps(REPORTS)
    assert ("/" + "Users" + "/") not in blob and "/private/" not in blob            # no local path in a tracked file


def test_every_command_is_read_only_and_the_screen_can_refuse():
    for r in REPORTS:
        for c in r["commands"]:
            assert RR.screened(c), (r["id"], c[:80])
    for bad in ("echo x > README.md", "rm -f a", "git checkout main", "git stash", "python3 -c \"open('a','w').write('x')\"", "sed -i s/a/b/ f", "cp a b"):
        assert not RR.screened(bad), bad
    for fine in ("grep -c 'a>b' f", "sed -n 1,2p f 2>/dev/null", "git log --oneline -3", "python3 -c \"print(1 > 0)\""):
        assert RR.screened(fine), fine


def test_the_programme_carries_these_states_with_the_old_ones_kept():
    F = S.FINDINGS
    for fid in OPEN_BEFORE:
        assert F[fid].get("was", [None])[0] == "OPEN", fid
    for fid in BY_PLANTING:
        assert F[fid].get("was", [None])[0] == "READER", fid
    assert F["V1"]["state"] == "OPEN" and "not checked" in F["V1"]["note"]
    states = {}
    for f in F.values():
        states[f["state"]] = states.get(f["state"], 0) + 1
    assert sum(states.values()) == 73
    # dated: the tally of this arc.  A later repair moves a finding forward and never back to OPEN or READER.
    assert states.get("OPEN", 0) <= 1 and states.get("READER", 0) <= 5
    partly = [r["id"] for r in REPORTS if r["checker_verdict"] == "PARTLY"]
    for fid in partly:
        # a later arc may have re-examined a finding this arc confirmed in part (its trail then holds this arc's note)
        notes = [F[fid]["note"]] + [n for _, n in F[fid].get("trail", [])]
        assert any("in part" in n for n in notes) or F[fid]["state"] in ("PARTLY FIXED", "FIXED"), fid


def _state(fid):
    return S.FINDINGS[fid]["state"]


def test_three_findings_live():
    # R2: no pinned lock file is tracked
    files = subprocess.run(["git", "-C", str(ROOT), "ls-files"], capture_output=True, text=True).stdout.split("\n")
    if files and files != [""]:
        pinned = [f for f in files if re.search(r"(^|/)(uv\.lock|poetry\.lock|Pipfile\.lock|constraints.*\.txt|requirements\.lock|environment\.ya?ml)$", f)]
        assert not pinned or _state("R2") != "REPRODUCED"
    # M11: the reviewer page's sentence is a fixed string in the generator
    gen = (ROOT / "scripts" / "views" / "generate.py").read_text(encoding="utf-8")
    assert "Every PROVED arc names its **test locks**" in gen or _state("M11") != "REPRODUCED"
    # X2: three files each say they win a disagreement
    gov = (ROOT / "GOVERNANCE.md").read_text(encoding="utf-8")
    gen_ = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    cla = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    three = ("constitution" in gov) and ("this file holds" in " ".join(gen_.split())) and ("living source of truth" in cla)
    assert three or _state("X2") != "REPRODUCED"
    # the control: the screen and the tally above would fail on a planted report
    planted = REPORTS + [dict(REPORTS[0], id="Z9", commands=["rm -rf frontier"])]
    assert any(not RR.screened(c) for r in planted for c in r["commands"])


def test_the_findings_say_what_was_and_was_not_done():
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The repo sweep:", "Nothing is fixed here", "They are readers", "does not fail", "| V1 |", "OPEN, not checked"):
        assert s in f, s
    assert f.count("\n| ") >= 34
