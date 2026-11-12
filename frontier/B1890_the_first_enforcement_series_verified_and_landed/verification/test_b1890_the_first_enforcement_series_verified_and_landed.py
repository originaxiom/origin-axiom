"""B1890 lock -- the first patch series for enforcement, verified with main's unseen cases and landed.

What could fail: the series not being on main; a case reported as holding whose committed lines say otherwise; the page
giving another count than the run; or the one gap main found being closed, or widened, without this lock being told."""
import importlib.util
import json
import pathlib
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "GENESIS.md").is_file())
RUN = json.loads((HERE / "unseen_cases_run.json").read_text(encoding="utf-8"))
F = (ARC / "FINDINGS.md").read_text(encoding="utf-8")


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_b1890", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def test_the_series_is_on_main():
    g = _gates()
    # CORRECTED 2026-11-12 (B1893).  This line pinned the sizes of the two tables, 6 and 14.  The second series moved two
    # gates from the first table to the second and added three, and a lock that pins a count fails on every honest change
    # (register row P-808).  It now holds the rule: no gate is in both tables, every entry is a gate, and the six gates that
    # read the tracked files only on the day of the first series are each still in one of the two.
    then = {"arrival-phrases", "path-refs", "retraction-sweep", "test-vacuity", "tracked-deps", "tracked-forbidden"}
    assert callable(g.checkout_state) and not (g.READS_TRACKED & g.READS_HISTORY) and then <= (g.READS_TRACKED | g.READS_HISTORY) <= set(g.GATES)
    assert (ROOT / "scripts" / "checks" / "commit_day.py").is_file() and (ROOT / "tests" / "test_gates_are_a_function_of_the_commit.py").is_file()
    assert g.COMMIT_DAY_FROM.startswith("ea41e6fc9") and g.commit_day_problems() == []


def test_the_eight_cases_that_hold_hold_in_the_committed_lines():
    e, s, d, c = RUN["export"], RUN["shallow"], RUN["dates"], RUN["clock"]
    assert len(e["U9.a an empty .git directory"]["refused"]) == 20 and not e["U9.a an empty .git directory"]["PASSING"]
    assert all(v[0] == "FAIL" and "refused" in v[1] for v in e["U9.c the five the seat's list of ten did not name"].values())
    assert len(e["U9.c the five the seat's list of ten did not name"]) == 5
    for k in ("U15.a/b +400 days", "U15.a/b -30 days", "U15.c the system's date + 400 days"):
        assert d[k]["gates whose line changed"] == [], k
    assert c["U15.c the system's date + 400 days"]["gates whose line changed"] == []
    assert c["U15.c the system's date + 400 days"]["stub says"].split() == ["2027-12-16"] * 3          # every way of asking the day was stubbed
    assert d["baseline"]["gates"] == 53 and d["baseline"]["failing"] == ["views-generated"]
    for k in ("U22.a depth 1", "U22.b depth 50", "U22.c a full clone cut by a hand-written .git/shallow"):
        assert s[k]["git says shallow"] == "true" and len(s[k]["history gates refused as shallow"]) == 14, k
        assert s[k]["history gates NOT refused"] == {} and s[k]["tracked-file gates refused"] == []
    assert int(s["U22.c a full clone cut by a hand-written .git/shallow"]["commits it holds"]) > 3000


def test_the_one_that_does_not_hold_is_stated_as_it_was_found():
    b = RUN["export"]["U9.b git init and no commit"]
    assert b["refused"] == ["harvest-debt", "lead-debt", "point-debt", "relay-debt"] and len(b["PASSING"]) == 9
    assert "skipped" in b["PASSING"]["log-changelog-paired"]                 # a pass that says it looked at nothing
    for name in b["PASSING"]:
        assert name in F, name
    assert "**does not hold**: 4 refused, 7 fail for other reasons, **9 pass**" in F and "Eight of main's nine unseen cases hold. One does not." in F


def test_the_gap_is_still_there_and_this_lock_is_told_when_it_is_closed(tmp_path):
    """A repository with no commit is read as a full clone.  When a later series closes it, this assertion is changed in the
    same commit to the word the patch gives such a folder: a mend that arrives unannounced fails here."""
    g = _gates()
    repo = tmp_path / "initialised_and_empty"
    repo.mkdir()
    assert subprocess.run(["git", "-C", str(repo), "init", "-q"], capture_output=True).returncode == 0
    assert g.checkout_state(repo) == "full"
    assert g.checkout_state(tmp_path / "no_such_folder") == "export"          # the control: where there is no repository it says so


def test_the_page_quotes_the_sealed_file_and_says_what_was_not_run():
    assert "06d73fbb029a832de6e2b144965711f0bc5cb94b107e494aefa9ab783f6ff893" in F
    assert F.count("| U") == 9 and "The other 44 stay sealed" in F
    for s in ("The whole suite on a fresh clone", "is the seat's run", "patch 1: all 7 fail. Patch 2: 2 fail, 7 pass. Patch 3: 4 fail, 8 pass. Patch 4: 2 fail, 12 pass"):
        assert s in F, s
    other = (HERE / "other_checks_run.txt").read_text(encoding="utf-8")
    assert "7 failed in" in other and "2 failed, 7 passed" in other and "4 failed, 8 passed" in other and "2 failed, 12 passed" in other
    assert "2 failed, 366 passed, 5 skipped" in other and "8 passed" in other
    # ADDED 2026-11-12 (Review 79): the page's row "14 pass" had no run behind it in this file.  The run is the file's last section now.
    last = other.split("ADDED 2026-11-12 (REVIEW 79)")
    assert len(last) == 2 and "tests/test_gates_are_a_function_of_the_commit.py" in last[1] and "\n14 passed in" in last[1] and "failed" not in last[1]
