"""B1425 lock -- the flaky lock was not flaky (E83), and the drift gate no longer samples.

A verification script that hands a SET to a solver as its unknowns returns a differently normalised answer
depending on PYTHONHASHSEED, so an equality test against one normalisation passes on some runs and fails on
others. B1411's geometry script did exactly that: FAIL on seeds 0-3, PASS on 4. It was misdiagnosed twice as
load. These assertions run the script under several seeds, which is the only way that class shows itself.
"""
import os
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1411_the_sm_seats_v10_arcs_harvested" / "verification" / "main_b1355_geometry.py"


@pytest.mark.parametrize("seed", ["0", "1", "2", "3", "5"])
def test_the_geometry_script_is_hash_order_independent(seed):
    env = dict(os.environ, PYTHONHASHSEED=seed)
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True, timeout=600, env=env)
    assert r.returncode == 0, "seed %s: %s" % (seed, (r.stdout + r.stderr)[-600:])
    assert "VERIFIED" in r.stdout and "|2T| = 24" in r.stdout


def test_the_script_no_longer_hands_a_set_to_the_solver():
    src = SCRIPT.read_text()
    assert "sorted(X.free_symbols" in src
    assert "solve([e for g in gens for e in (X*g - g*X)], list(" not in src


def test_the_chain_table_gate_reads_every_row():
    """it read rows[:6] + rows[-3:] -- 9 of 57 -- and the stale row sat in the 48 it skipped"""
    # read the CODE, not the file: the first version of this assertion searched the whole text and
    # tripped on the comment that quotes the old slice -- the same mistake as asserting a literal string
    # instead of the property (2026-09-18).
    code = [l.split("#", 1)[0] for l in (ROOT / "tests" / "test_paper_chain_table.py").read_text().split("\n")]
    loops = [l for l in code if "for row in" in l]
    assert loops, "the gate has no row loop at all"
    assert all("[" not in l.split("for row in", 1)[1] for l in loops), "the gate still samples rows: %s" % loops


def test_no_generated_chain_row_is_stale():
    import re
    gen = subprocess.run([sys.executable, str(ROOT / "scripts" / "checks" / "paper_chain_table.py"), "--tex"],
                         capture_output=True, text=True, cwd=ROOT).stdout
    paper = (ROOT / "papers" / "P3_THE_PAPER" / "main.tex").read_text()
    rows = [l.strip() for l in gen.split("\n") if re.match(r"^\d+ & ", l.strip())]
    assert len(rows) >= 50
    stale = [r for r in rows if r not in paper]
    assert not stale, "%d generated row(s) disagree with the paper: %s" % (len(stale), stale[:1])

def test_the_evidence_shows_the_defect_and_its_repair():
    """the pre-fix script pulled back out of git: seed-DEPENDENT (reproducible failing set, not flaky)"""
    import json
    e = json.loads((ROOT / "frontier" / "B1425_the_flaky_lock_and_the_hollow_green" / "verification"
                    / "hash_seed_evidence.json").read_text())
    assert e["pre_fix_hands_a_set_to_the_solver"] and e["post_fix_sorts_the_unknowns"]
    assert e["pre_fix_is_seed_dependent"], "the pre-fix script passed or failed on every seed: not the E83 shape"
    assert e["post_fix_is_seed_independent"] and len(e["post_fix_pass_seeds"]) == 8
    assert e["verdict"] == "E83 CONFIRMED and FIXED"


def test_the_sweep_named_every_lock_it_seed_checked():
    """a sweep that reports stable locks must have run the locks it names"""
    import json
    s = json.loads((ROOT / "frontier" / "B1425_the_flaky_lock_and_the_hollow_green" / "verification"
                    / "order_sensitivity_sweep.json").read_text())
    assert s["site_count"] >= s["unsorted_count"] > 0
    assert s["seed_checked_locks"]["locks"] == s["locks_touched"], "the sweep found a lock it did not seed-check"
    assert len(s["seed_checked_locks"]["seeds"]) >= 5 and s["seed_checked_locks"]["stable"]
    for rel in s["locks_touched"]:
        assert (ROOT / rel).exists()


def test_the_papers_retraction_count_matches_the_index():
    """the paper cites the index BY COUNT; nothing checked the two agreed, and they had drifted by two.

    The retraction-debt gate fires only on arcs whose own arc_verdict says RETRACTED. A correction banked
    the way this record prefers -- an addendum on the arc that erred, computation kept -- never earns a row,
    so the index silently lagged the corpus while the paper quoted its length. Pinned here in both directions.
    """
    import re
    idx = (ROOT / "docs" / "RETRACTIONS.md").read_text()
    rows = [l for l in idx.split("\n")
            if l.startswith("| ") and not l.startswith("|---") and "what was asserted" not in l]
    words = {27: "twenty-seven", 28: "twenty-eight", 29: "twenty-nine", 30: "thirty",
             31: "thirty-one", 32: "thirty-two", 33: "thirty-three", 34: "thirty-four", 35: "thirty-five",
             36: "thirty-six", 37: "thirty-seven", 38: "thirty-eight", 39: "thirty-nine", 40: "forty",
             41: "forty-one", 42: "forty-two", 43: "forty-three", 44: "forty-four", 45: "forty-five",
             46: "forty-six", 47: "forty-seven", 48: "forty-eight", 49: "forty-nine", 50: "fifty",
             51: "fifty-one", 52: "fifty-two", 53: "fifty-three", 54: "fifty-four", 55: "fifty-five",
             56: "fifty-six", 57: "fifty-seven", 58: "fifty-eight", 59: "fifty-nine", 60: "sixty", 61: "sixty-one", 62: "sixty-two", 63: "sixty-three", 64: "sixty-four", 65: "sixty-five", 66: "sixty-six", 67: "sixty-seven", 68: "sixty-eight", 69: "sixty-nine", 70: "seventy", 71: "seventy-one", 72: "seventy-two", 73: "seventy-three", 74: "seventy-four", 75: "seventy-five", 76: "seventy-six", 77: "seventy-seven", 78: "seventy-eight", 79: "seventy-nine", 80: "eighty",
             81: "eighty-one", 82: "eighty-two", 83: "eighty-three", 84: "eighty-four", 85: "eighty-five", 86: "eighty-six", 87: "eighty-seven", 88: "eighty-eight", 89: "eighty-nine", 90: "ninety", 91: "ninety-one", 92: "ninety-two", 93: "ninety-three", 94: "ninety-four", 95: "ninety-five", 96: "ninety-six", 97: "ninety-seven", 98: "ninety-eight", 99: "ninety-nine", 100: "one hundred", 101: "one hundred and one", 102: "one hundred and two", 103: "one hundred and three", 104: "one hundred and four", 105: "one hundred and five", 106: "one hundred and six", 107: "one hundred and seven", 108: "one hundred and eight", 109: "one hundred and nine", 110: "one hundred and ten", 111: "one hundred and eleven", 112: "one hundred and twelve", 113: "one hundred and thirteen", 114: "one hundred and fourteen", 115: "one hundred and fifteen", 116: "one hundred and sixteen", 117: "one hundred and seventeen", 118: "one hundred and eighteen", 119: "one hundred and nineteen", 120: "one hundred and twenty", 121: "one hundred and twenty-one", 122: "one hundred and twenty-two", 123: "one hundred and twenty-three", 124: "one hundred and twenty-four", 125: "one hundred and twenty-five", 126: "one hundred and twenty-six", 127: "one hundred and twenty-seven", 128: "one hundred and twenty-eight", 129: "one hundred and twenty-nine", 130: "one hundred and thirty"}
    assert len(rows) in words, "extend the number-words table: the index has %d rows" % len(rows)
    paper = (ROOT / "papers" / "P3_THE_PAPER" / "main.tex").read_text()
    # (2026-11-12: the pattern was r"retractions index holds ([a-z-]+) corrected or withdrawn statements".  From 100 rows the
    #  count is several words, and the pattern would have found no count at all; the index stands at 97.)
    count_in = lambda text: re.search(r"retractions index holds ([a-z][a-z -]*[a-z]) corrected or withdrawn statements", text)
    assert count_in("the retractions index holds one hundred and four corrected or withdrawn statements").group(1) == words[104]
    m = count_in(paper)
    assert m, "the paper no longer states the count in the expected words"
    assert m.group(1) == words[len(rows)], (
        "the paper says %s; the index has %d rows" % (m.group(1), len(rows)))
    # and the generator that emits that sentence agrees with the paper
    gen = (ROOT / "scripts" / "checks" / "paper_provenance.py").read_text()
    assert "retractions index holds %s corrected" % words[len(rows)] in gen


def test_this_file_is_in_what_a_landing_runs_when_the_index_or_the_paper_changes():
    """Review 80 (2026-11-12; main's word): the test above failed from the day the index passed 80 rows, and no landing ran
    it.  The selector of the tests a landing runs names this file, so that it does not depend on a word in its text; a
    change to the paper or to its generator is not one the selector can bound, and asks for the full suite."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("affected_tests_for_b1425", ROOT / "scripts" / "affected_tests.py")
    a = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a)
    me = "tests/test_b1425_determinism.py"
    assert me in a.ALWAYS_WITH_THE_CORPUS and me in a._corpus_scanners()
    for changed in ("docs/RETRACTIONS.md", "CHANGELOG.md", "frontier/B1425_the_flaky_lock_and_the_hollow_green/FINDINGS.md"):
        sel, full = a.select([changed])
        assert me in sel and not full, changed
    for changed in ("papers/P3_THE_PAPER/main.tex", "scripts/checks/paper_provenance.py"):
        sel, full = a.select([changed])
        assert full == [changed], changed                                  # the full suite, which holds this file
    assert a.ALWAYS_WITH_THE_CORPUS == {"tests/test_repo_gates.py", me}


def test_the_manifest_records_the_historys_length():
    """a reader on a truncated clone must be able to find that out from the package itself.

    An outside reader reported this repository as a 101-commit project and reasoned about its structure
    from that number; the published history is complete on both mirrors and their clone was depth-limited.
    Two of the package's own checks -- is the recorded commit published, is it an ancestor of HEAD --
    answer wrongly and quietly on a shallow clone, so the length is recorded and compared.
    """
    import json
    import subprocess
    m = json.loads((ROOT / "papers" / "P3_THE_PAPER" / "verification_package" / "MANIFEST.json").read_text())
    env = m["environment"]
    assert isinstance(env.get("git_commits"), int) and env["git_commits"] > 3000, (
        "the manifest does not record a plausible history length: %r" % env.get("git_commits"))
    assert env.get("git_shallow") is False, "the manifest was built on a shallow clone"
    here = int(subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True).stdout.strip())
    assert here >= env["git_commits"], "this checkout is shorter than the manifest's history"


def test_the_package_tells_a_reader_to_clone_the_whole_history():
    readme = (ROOT / "papers" / "P3_THE_PAPER" / "verification_package" / "README.md").read_text()
    assert "no --depth" in readme and "git fetch --unshallow" in readme
    assert "git rev-list --count HEAD" in readme
    runner = (ROOT / "papers" / "P3_THE_PAPER" / "verification_package" / "run_package.py").read_text()
    assert "CLONE IS TRUNCATED" in runner, "the runner does not check the clone it is running in"
    assert "is-shallow-repository" in runner


def test_the_b1411_receipt_no_longer_ships_a_failure():
    """the arc claimed its locks re-ran green while its own committed receipt ended in an AssertionError"""
    r = (ROOT / "frontier" / "B1411_the_sm_seats_v10_arcs_harvested" / "verification"
         / "main_b1355_geometry_run.txt").read_text()
    assert "VERIFIED" in r and "|2T| = 24" in r
    assert "Traceback" not in r and "AssertionError" not in r
    # the receipt as shipped is kept as this arc's evidence, so the repair cannot erase what it repairs
    old = (ROOT / "frontier" / "B1425_the_flaky_lock_and_the_hollow_green" / "verification"
           / "b1411_receipt_as_shipped.txt").read_text()
    assert "AssertionError" in old, "the preserved receipt no longer shows the failure it exists to record"


def test_the_silent_receipt_sweep_separates_declared_failures_from_silent_ones():
    """47 receipts carry a failure marker; the defect is only the ones nothing acknowledges"""
    import json
    s = json.loads((ROOT / "frontier" / "B1425_the_flaky_lock_and_the_hollow_green" / "verification"
                    / "receipt_failure_sweep.json").read_text())
    assert s["tracked_text_receipts_scanned"] > 1000
    assert 0 < s["silent_count"] < s["receipts_carrying_a_failure"], (
        "the sweep no longer distinguishes declared failures from silent ones")
    # the repaired one must no longer be on the silent list when the sweep is re-run
    assert any("B1411" in f for f in s["silent"]), "the sweep's record of B1411 is what L227 (registered as L223) is anchored on"
    assert (ROOT / "docs" / "OPEN_LEADS.md").read_text().count("L227") >= 1      # renumbered from L223 on 2026-10-01 (collision)
