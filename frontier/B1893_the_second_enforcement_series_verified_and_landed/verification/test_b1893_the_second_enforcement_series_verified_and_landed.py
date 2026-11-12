"""B1893 lock -- the second patch series for enforcement, verified with main's unseen cases and landed.

What could fail: the series not being on main; a case reported as caught whose committed lines say otherwise; the one case
caught by accident being caught, or missed, for another reason than the page gives; the page giving another count than a
run; or the thing main found by reading being closed, or widened, without this lock being told."""
import importlib.util
import json
import pathlib
import re
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "GENESIS.md").is_file())
RUN = json.loads((HERE / "unseen_s2.json").read_text(encoding="utf-8"))
AGAIN = json.loads((HERE / "unseen_s2_u19.json").read_text(encoding="utf-8"))
F = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
CASES = ["U10.a", "U10.b", "U10.c", "U19.a", "U19.b", "U11.a", "U11.b", "U12.a", "U12.b", "U12.c", "U13.a", "U13.b", "U13.c"]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_series_is_on_main():
    g = _load("gates_for_b1893", ROOT / "scripts" / "gates" / "gates.py")
    assert re.fullmatch(r"[0-9a-f]{40}", g.NOTHING_LEAVES_FROM) and isinstance(g.LEFT_BY_NAME, dict) and isinstance(g.RAISED_BY_NAME, dict)
    for f in ("left_the_ledger", "held_since", "baseline_rise", "locks_that_left", "ceiling_rises", "attribution_baseline_rise"):
        assert callable(getattr(g, f)), f
    moved = {"retraction-sweep", "chain-locks", "law-map-provenance", "identification-register", "test-vacuity"}
    assert moved <= g.READS_HISTORY and not (moved & g.READS_TRACKED) and not (g.READS_TRACKED & g.READS_HISTORY)
    assert (ROOT / "tests" / "test_nothing_leaves_a_ledger.py").is_file()


def test_the_thirteen_cases_are_caught_in_the_committed_lines():
    assert [k for k in RUN if k.startswith("U")] == CASES
    for k in CASES:
        r = RUN[k]
        assert r["committed"] is True and r["CAUGHT"] is True, k
        # the first runner's commits were made under another author, which fails the attribution gate by itself: a case
        # is counted as caught only by a gate other than that one, or by the second run under the repository's author
        other = [x for x in r["gates newly failing"] if x != "attribution"]
        if k.startswith("U19"):
            assert other == [], k
        else:
            assert other, k
            if r["named gate"]:
                assert set(r["named gate"]) <= set(other), k
    # the two that only the attribution gate could catch, run again under the repository's author, with a control
    assert AGAIN["control"]["committed"] is True and AGAIN["control"]["gates newly failing"] == []
    for k in ("U19.a", "U19.b"):
        assert AGAIN[k]["CAUGHT"] is True and list(AGAIN[k]["gates newly failing"]) == ["attribution"], k
        assert "ceiling(s) in docs/ATTRIBUTION_BASELINE.json rose" in AGAIN[k]["gates newly failing"]["attribution"], k


def test_the_case_caught_by_accident_is_caught_by_the_hash_gate_alone():
    assert [x for x in RUN["U12.b"]["gates newly failing"] if x != "attribution"] == ["artifact-hashes"]
    assert "1407 files made to skip" in RUN["U12.b"]["note"]
    assert "**artifact-hashes only: by accident**" in F and "It was appended at the end" in " ".join(F.split())


def test_a_ceiling_that_falls_and_rises_back_is_still_not_seen():
    """Found by main reading patches 3 and 5.  When the seat closes it, the first assertion of each pair fails: change this
    lock and the page together, and say which series closed it."""
    lock = _load("the_series_lock_for_b1893", ROOT / "tests" / "test_nothing_leaves_a_ledger.py")
    with tempfile.TemporaryDirectory() as d:
        repo, anchor = lock._scratch(pathlib.Path(d), lock._REGISTER)
        earned = lock._IDENT.replace("| I-2 | two | A | B | x | y | **UNEARNED**", "| I-2 | two | A | B | x | y | **EARNED**")
        lock._commit(repo, "earned, and the baseline lowered", {"docs/IDENTIFICATION_LEDGER.md": earned, "docs/IDENTIFICATION_BASELINE.json": lock._baseline(0)})
        lock._commit(repo, "a new unearned row, the baseline moved back up, no record",
                     {"docs/IDENTIFICATION_LEDGER.md": earned + (lock._UNEARNED % 3), "docs/IDENTIFICATION_BASELINE.json": lock._baseline(1)})
        assert lock._gate(repo, "identification-register", anchor) == (True, "ok")              # the plant passes: not seen
    with tempfile.TemporaryDirectory() as d:
        repo, anchor = lock._scratch(pathlib.Path(d), lock._REGISTER)
        lock._commit(repo, "the same rise with no fall before it",
                     {"docs/IDENTIFICATION_LEDGER.md": lock._IDENT + (lock._UNEARNED % 3), "docs/IDENTIFICATION_BASELINE.json": lock._baseline(2)})
        ok, detail = lock._gate(repo, "identification-register", anchor)
        assert ok is False and "the baseline rose 1 -> 2" in detail                             # the control: seen
    g = lock._gates()
    then = {"a.md": 4}
    assert g.ceiling_rises("x", {"a.md": 4}, then, "the anchor", {}) == (None, "")              # 4 -> 2 -> 4 is, to this rule, 4 -> 4
    assert "a.md 4 -> 5" in g.ceiling_rises("x", {"a.md": 5}, then, "the anchor", {})[0]
    run = (HERE / "a_ceiling_that_falls_and_rises_back_run.txt").read_text(encoding="utf-8")
    assert re.search(r"A2 after the rise back[^\n]*\(True, 'ok'\)", run) and re.search(r"A-control[^\n]*\(False, ", run)
    assert re.search(r"B after a fall[^\n]*\(None, ''\)", run) and re.search(r"B-control[^\n]*rose since", run)


def test_the_pages_counts_are_the_runs():
    locks = (HERE / "each_patchs_lock_on_the_commit_before_run.txt").read_text(encoding="utf-8")
    for s in ("5 failed in", "4 failed, 5 passed", "5 failed, 9 passed", "5 failed, 14 passed", "3 failed, 19 passed", "22 passed in"):
        assert s in locks, s
    assert "patch 1: all 5 fail. Patch 2: 4 fail, 5 pass. Patch 3: 5 fail, 9 pass. Patch 4: 5 fail, 14 pass. Patch 5: 3 fail, 19 pass" in F
    gates = (HERE / "gates_on_the_series_out.txt").read_text(encoding="utf-8")
    assert len(re.findall(r"^  PASS  ", gates, re.M)) == 53 and not re.findall(r"^  (FAIL|SKIP)  ", gates, re.M) and "| all 53 gates on the end of the series, views generated | 53 pass" in F
    suite = (HERE / "planted_suite_on_the_series_out.txt").read_text(encoding="utf-8")
    cases = [l for l in suite.split("\n") if re.match(r"^PV\d+\s+\S+\s+(NOT CAUGHT|CAUGHT)", l)]
    caught = [l for l in cases if not re.match(r"^PV\d+\s+\S+\s+NOT CAUGHT", l)]
    controls = [l for l in suite.split("\n") if l.startswith("CTL")]
    assert "controls %d of %d; %d of %d planted cases caught" % (sum(1 for l in controls if "NOT CAUGHT" not in l), len(controls), len(caught), len(cases)) in F
    tests = (HERE / "mains_own_tests_on_the_series_out.txt").read_text(encoding="utf-8")
    m = re.findall(r"^(?:(\d+) failed, )?(\d+) passed(?:, (\d+) skipped)?", tests, re.M)
    assert m, "the run's summary line"
    failed, passed, skipped = (int(x or 0) for x in m[-1])
    assert "%d pass, %d skipped, %d fail" % (passed, skipped, failed) in F


def test_the_arc_says_what_it_did_not_do():
    for s in ("was not run on the series", "They were not run again on today's head", "Patch 6's lock was not run", "is not written", "## Seen first", "## Disclosed", "0 of 19"):
        assert s in F, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1893" and set(v["scope"]) == {"frame", "object", "reach", "hypotheses"} and v["scope"]["reach"] in ("single", "class", "general")
    assert v["claim_one_line"].endswith("0 of 19.")


# ------------------------------------------------------------------------------------------------ added 2026-11-12 (Review 80)
# A session that built none of this planted against the lock.  The verdict changed to another word passed, and so did a
# verdict line made to open with other words.  And four of the cases marked caught name no gate in the run file, so that
# the lock asked of them only that some gate other than the attribution gate had failed.  The gates of the committed run
# are held for those four, and among them the gate that looks for the fault.

def test_the_verdict_and_the_gates_of_the_four_cases_that_name_none_are_held():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED" and v["claim_one_line"].startswith("THE SECOND PATCH SERIES OF THE ENFORCEMENT PACKAGE (WP-0.7), BUILT BY THE ADVISOR SEAT, VERIFIED")
    want = {"U12.a": (["path-refs", "test-vacuity"], "test-vacuity"),
            "U12.b": (["artifact-hashes"], "artifact-hashes"),
            "U12.c": (["chain-locks", "law-map-provenance", "path-refs", "test-vacuity"], "test-vacuity"),
            "U13.a": (["inputs-scoreboard", "law-map-provenance", "representation-sweep"], "law-map-provenance")}
    none_named = sorted(k for k in CASES if RUN[k].get("named gate") is None and RUN[k]["CAUGHT"] is True)
    assert none_named == sorted(want), none_named
    for k, (gates, the_one) in want.items():
        other = sorted(x for x in RUN[k]["gates newly failing"] if x != "attribution")
        assert other == gates and the_one in other, (k, other)
