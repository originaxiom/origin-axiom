"""B1896 lock -- the third patch series for enforcement, verified with main's unseen cases and landed.

What could fail: the series not being on main; a case reported as caught, or as passing, whose committed lines say otherwise;
the page giving another number than a run; one of the shapes that still pass being closed, or one that is caught being let
through, without this lock being told; a mend main made at the landing being undone; or this arc's own files holding a phrase
that the framing gate bans, now that the gate reads them."""
import importlib.util
import json
import pathlib
import re
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "GENESIS.md").is_file())
RUN = json.loads((HERE / "unseen_s3.json").read_text(encoding="utf-8"))
AFTER = json.loads((HERE / "after_reading_s3.json").read_text(encoding="utf-8"))
F = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
CASES = ["U16.a", "U16.b", "U16.c", "U16.d", "U17.a", "U17.b", "U17.c", "U21.a", "U21.b", "U21.c", "U21.d", "U20.a", "U20.b", "U20.c",
         "U24.a", "U24.b", "U24.c", "U24.d", "U24.e", "U24.f", "U24.g", "U24.h"]
PASS_UNSEEN = ["U17.b", "U24.a", "U24.d", "U24.f", "U24.g"]
PASS_AFTER = ["AR1", "AR2", "AR5"]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _gates():
    return _load("gates_for_b1896", ROOT / "scripts" / "gates" / "gates.py")


def _the_series_lock():
    """the series' own lock, for its helpers: a small repository holding this repository's gates and checkers, and a gate run there"""
    return _load("the_series_lock_for_b1896", ROOT / "tests" / "test_a_gate_reads_all_it_is_about.py")


def test_the_series_is_on_main(tmp_path):
    g = _gates()
    rs = _load("sweep_for_b1896", ROOT / "scripts" / "checks" / "retraction_sweep.py")
    assert g.FRAMING_MAX_BYTES == 5_000_000 and g.CITES_NO_LOCK_AS_FOUND == frozenset(("P51",)) and len(g.CANNOT_FAIL_AS_FOUND) == 26
    assert "gate-controls" in g.READS_HISTORY and not (g.READS_TRACKED & g.READS_HISTORY)
    assert len(rs.NOT_SWEPT_BY_NAME) == 2 and isinstance(rs.STANDS_AS_FOUND, dict)
    repo = tmp_path / "initialised_and_empty"
    repo.mkdir()
    assert subprocess.run(["git", "-C", str(repo), "init", "-q"], capture_output=True).returncode == 0
    assert g.checkout_state(repo) == "empty"                                    # the gap of the first series, closed by the fourth patch
    assert (ROOT / "tests" / "test_a_gate_reads_all_it_is_about.py").is_file()


def test_the_unseen_cases_are_as_the_committed_lines_have_them():
    assert [k for k in RUN if re.fullmatch(r"U\d+\.[a-h]", k)] == CASES
    assert RUN["control"]["gates newly failing"] == []
    for k in CASES:
        c = RUN[k]
        assert c["committed"] is True, k
        if k in PASS_UNSEEN:
            assert c["gates newly failing"] == {} and c["CAUGHT BY THE NAMED GATE"] is False and c["CAUGHT BY SOME GATE"] is False, k
        else:
            assert c["CAUGHT BY THE NAMED GATE"] is True and all(m in c["gates newly failing"] for m in c["named gate"]), k
    caught = [k for k in CASES if k not in PASS_UNSEEN]
    assert len(caught) == 17 and "17 of main's 22 unseen cases are caught" in F
    # the first series' case again: every gate of the two tables refuses a repository with no commit
    u9 = RUN["U9.b git init and no commit"]
    assert u9["gates in the two tables"] == 24 == len(u9["refused"]) and not u9["failing otherwise"] and not u9["PASSING"] and not u9["absent"]
    # the page's table says of each case what the lines say
    for k in CASES:
        row = [l for l in F.split("\n") if l.startswith("| %s |" % k) and (l.rstrip().endswith("| **not caught** |") or " | caught: " in l)]     # the cases' table, not the table of why five pass
        assert len(row) == 1, k
        assert ("**not caught**" in row[0]) == (k in PASS_UNSEEN), k
        if k not in PASS_UNSEEN:
            assert all(m in row[0] for m in RUN[k]["named gate"]), k
    # what the gates said holds no banned phrase: the committed lines mask it
    g = _gates()
    lines = g._framing_plain(json.dumps(RUN))
    assert not any(g._framing_plain(p) in lines for p in g.BANNED) and "[the phrase]" in json.dumps(RUN)


def test_the_cases_written_after_reading_are_as_the_committed_lines_have_them():
    assert [k for k in AFTER if k.startswith("AR")] == ["AR1", "AR2", "AR3", "AR4", "AR5"] and AFTER["control"]["gates newly failing"] == []
    for k in ("AR1", "AR2", "AR3", "AR4", "AR5"):
        assert (AFTER[k]["gates newly failing"] == {}) == (k in PASS_AFTER), k
        row = [l for l in F.split("\n") if l.startswith("| %s |" % k)]
        assert len(row) == 1 and ("**passes every gate**" in row[0]) == (k in PASS_AFTER), k
    assert list(AFTER["AR3"]["gates newly failing"]) == ["test-vacuity"] == list(AFTER["AR4"]["gates newly failing"])


_TEST = "def test_planted():\n%s\n"
_STILL_PASS = {     # the shapes that pass the vacuity gate: (the test's body, where it stands)
    "U24.a": ("    assert len([1, 2]) == 2", "tests/test_planted.py"),
    "U24.g": ("    assert len([1, 2]) == 2", "frontier/B9002_planted/verification/test_b9002_planted.py"),
    "U24.d": ("    if False:\n        assert 1 == 2", "tests/test_planted.py"),
    "AR2": ("    x, y = 3, 3\n    assert x == y", "tests/test_planted.py"),
    "AR5": ("    x = 3\n    x = 3\n    assert x == 3", "tests/test_planted.py"),
}
_ARE_CAUGHT = {
    "U24.b": '    assert "a" in "abc"',
    "U24.c": "    assert True is not False",
    "U24.e": "    assert not None",
    "U24.h": "    x = 3\n    assert x == 3",
    "AR3": "    assert (1, 2) == (1, 2)",
    "AR4": '    assert 2 > 1 and "a" < "b"',
}


def test_the_shapes_that_pass_still_pass_and_this_lock_is_told_when_one_is_closed(tmp_path):
    """Each shape main found passing is made again in a small repository of its own, with the series' own helpers, and the gate
    is run there.  When a later series closes one, its line here fails and is changed in the commit that lands the mend.  The
    shapes that are caught are run beside them, so that the passing ones are not passing for want of a gate."""
    s = _the_series_lock()
    # the vacuity gate
    for name, (body, where) in _STILL_PASS.items():
        ok, detail = s._vacuity(tmp_path, "pass_" + name.replace(".", ""), _TEST % body, where=where)
        assert ok is True, (name, detail)
    ok, detail = s._vacuity(tmp_path, "pass_U24f", "import pytest\n\n\n" + _TEST % "    with pytest.raises(ZeroDivisionError):\n        1 / 0")
    assert ok is True, ("U24.f", detail)
    for name, body in _ARE_CAUGHT.items():
        ok, detail = s._vacuity(tmp_path, "caught_" + name.replace(".", ""), _TEST % body)
        assert ok is False and "test_planted" in detail, (name, detail)
    # the sweep: a registered phrase over two lines, and the same on one line
    phrase = re.search(r"`([^`]+)`", s._REG_HEAD).group(1)
    words = phrase.split(" ")
    broken = " ".join(words[:2]) + "\n" + " ".join(words[2:])
    repo = s._sweep_repo(tmp_path, "pass_U17b", s._REG_HEAD, {"README.md": "# A page\n\nWe find that " + broken + ", as before.\n"})
    ok, detail = s._gate(repo, "retraction-sweep")
    assert ok is True, ("U17.b", detail)
    repo = s._sweep_repo(tmp_path, "caught_one_line", s._REG_HEAD, {"README.md": "# A page\n\nWe find that " + phrase + ", as before.\n"})
    ok, detail = s._gate(repo, "retraction-sweep")
    assert ok is False and "README.md" in detail
    # the claims gate: a row that cites a folder named like a test file, and one that cites a folder with another name
    repo = s._claims_repo(tmp_path / "pass_AR1", proven="| P2 | Another claim. | `tests/test_a_folder.py` ✓ |", more={"tests/test_a_folder.py/.gitkeep": ""})
    ok, detail = s._gate(repo, "claims")
    assert ok is True, ("AR1", detail)
    repo = s._claims_repo(tmp_path / "caught_U20c", proven="| P2 | Another claim. | `tests/a_folder.py` ✓ |", more={"tests/a_folder.py/.gitkeep": ""})
    ok, detail = s._gate(repo, "claims")
    assert ok is False and "P2" in detail


def test_the_page_gives_the_numbers_of_the_runs():
    per = (HERE / "each_patchs_lock_on_the_commit_before_run.txt").read_text(encoding="utf-8")
    want = {1: "6 failed, 1 passed", 2: "5 failed, 8 passed", 3: "4 failed, 15 passed", 4: "3 failed, 56 passed", 5: "10 failed, 40 passed", 6: "4 failed, 46 passed"}
    for k, s in want.items():
        line = [l for l in per.split("\n") if l.startswith("patch %d " % k)]
        assert len(line) == 1 and s in line[0], k
    assert "Patch 1: 6 fail. Patch 2: 5. Patch 3: 4. Patch 4: 2, and one in B1890's lock. Patch 5: 8, and two in the second series' lock. Patch 6: 4" in F
    assert "2 failed, 15 passed" in per and "8 failed, 20 passed" in per and "2 failed, 20 passed" in per and "1 failed, 4 passed" in per
    gates = (HERE / "gates_on_the_series_out.txt").read_text(encoding="utf-8")
    assert len(re.findall(r"^\s*PASS\s", gates, re.M)) == 53 and not re.search(r"^\s*(FAIL|SKIP)\s", gates, re.M) and "53 pass" in F
    locks = (HERE / "the_series_locks_out.txt").read_text(encoding="utf-8")
    assert "72 passed" in locks and "72 pass" in F
    own = (HERE / "mains_own_tests_on_the_series_out.txt").read_text(encoding="utf-8")
    m = re.search(r"(\d+) passed, (\d+) skipped", own)
    assert m and " failed" not in own.split("\n")[-2] and "%s pass, %s skipped, 0 fail" % (m.group(1), m.group(2)) in F
    suite = (HERE / "planted_suite_on_the_series_out.txt").read_text(encoding="utf-8")
    caught = len(re.findall(r"^PV\d+\s+(?!twin)\S+\s+CAUGHT", suite, re.M))                        # a twin is the honest form of a case, not a case
    cases = len(re.findall(r"^PV\d+\s+(?!twin)\S+\s+(?:CAUGHT|NOT CAUGHT)", suite, re.M))
    controls = len(re.findall(r"^CTL\d+\s+\S+\s+CAUGHT", suite, re.M))
    twins = re.findall(r"^PV\d+\s+twin\s+(\S+)", suite, re.M)
    assert (controls, caught, cases) == (5, 24, 32) and twins == ["PASSES"] * 6
    assert F.count("controls %d of 5; %d of %d planted cases caught" % (controls, caught, cases)) == 2, (controls, caught, cases)
    assert "the end of the second series caught 19" in F and "catches 24, where the end of the second series caught 19" in json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]


def test_what_main_changed_at_the_landing_stands():
    g = _gates()
    ok, detail = g.GATES["retraction-sweep"]()
    assert ok is True and "11 standing instance(s)" in detail and "shorten the table" not in detail, detail
    c = json.loads((ROOT / "frontier" / "B1632_w45_verified_on_main" / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert c.startswith("[READ THIS FIRST, placed at the head 2026-11-12") and "REFUTED IN PART by B1634" in c[:400] and c.rstrip().endswith("the computation stands.]")
    page = (ROOT / "papers" / "P3_THE_PAPER" / "CLAIM_CANDIDATES.md").read_text(encoding="utf-8")
    row = [l for l in page.split("\n") if l.startswith("| `B1632` |")]
    assert len(row) == 1 and "[CORRECTED 2026-11-12 (P-808; B1896)" in row[0] and "genuine representation" in row[0]
    reg = (ROOT / "docs" / "RETRACTED_PHRASES.md").read_text(encoding="utf-8")
    assert reg.count("[CHANGED 2026-11-12") == 2 and "Descriptive rows, not swept as live phrases" in reg and "does not\nparse (E66" in reg       # what they said is kept
    lock = (ROOT / "frontier" / "B1890_the_first_enforcement_series_verified_and_landed" / "verification" / "test_b1890_the_first_enforcement_series_verified_and_landed.py").read_text(encoding="utf-8")
    assert "def test_the_gap_is_closed_and_a_repository_with_no_commit_is_read_as_empty(" in lock and "def test_the_gap_is_still_there" not in lock
    rows = {l.split(" | ")[0].strip("| "): l for l in (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8").split("\n") if l.startswith("| P-")}
    assert rows["P-154"].split(" | ")[4] == "DONE" and "B1896" in rows["P-154"] and rows["P-820"].split(" | ")[4] == "QUEUED" and "[DEBT]" in rows["P-820"]


def test_the_arc_says_what_it_is_and_what_it_is_not():
    for s in ("## Seen first", "## Disclosed", "## Reproduce", "0 of 19", "06d73fbb029a832de6e2b144965711f0bc5cb94b107e494aefa9ab783f6ff893",
              "591e7e85ca300e1354d7902299f0e1a7113ca81de21aa92900371daddc59d573", "None of these is opened by the series",
              "Main did not build the series and did not change a line of it", "The whole suite on a fresh clone", "the other nine stay sealed"):
        assert s in F, s
    assert len(re.findall(r"^\| U\d", F, re.M)) == 22 + 4 and len(re.findall(r"^\| AR\d", F, re.M)) == 5     # the 22 cases and the four rows of the table of why five pass; the five written after reading
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1896" and v["verdict"] == "PROVED" and v["instrument"] is True and v["claim_one_line"].endswith("0 of 19.")
    assert set(v["scope"]) == {"frame", "object", "reach", "hypotheses"} and v["scope"]["reach"] in ("single", "class", "general")
    # the framing gate reads this arc now: none of its files holds a phrase the gate bans, as the gate reads
    g = _gates()
    banned = [g._framing_plain(p) for p in g.BANNED]
    for p in sorted(ARC.rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts:
            try:
                plain = g._framing_plain(p.read_text(encoding="utf-8"))
            except UnicodeDecodeError:
                continue
            assert not any(b in plain for b in banned), p.name


# ------------------------------------------------------------------------------------------------ added 2026-11-12 (Review 80)
# A session that built none of this planted against the lock.  "Five are not caught" turned into "None is not caught"
# passed; a verdict line made to open with other words passed; either of the two runners deleted passed.

def test_the_headline_the_verdict_and_the_two_runners_are_held():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED" and v["claim_one_line"].startswith("THE THIRD PATCH SERIES OF THE ENFORCEMENT PACKAGE (WP-0.7; the advisor seat's; six patches under one rule:")
    assert "- **17 of main's 22 unseen cases are caught, each by the gate that looks for the fault.**" in F
    assert "- **Five are not caught.**" in F
    assert len(PASS_UNSEEN) == 5 and len(CASES) == 22 and all(RUN[k]["CAUGHT BY SOME GATE"] is False for k in PASS_UNSEEN)     # the five are the run's
    for name in ("run_unseen_s3.py", "after_reading_s3.py"):
        assert (HERE / name).is_file(), name


# ---- ADDED 2026-11-12 (Review 80; a reader's check of main's answers, its row A9, not checked by main, made again by the
# builder in a scratch checkout).  The lock held the verdict line by its first 106 characters.  Made again: the line with
# "17 OF MAIN'S 22" turned into "22 OF MAIN'S 22" passes, and so does "FIVE PASS" turned into "NONE PASSES".  The reader's
# second pass, the gates named for two rows replaced on the page, is caught as the builder made it (another gate's name in
# their place); a row is now also asked to open its answer with a gate the run names.
_THE_LINE_SAYS = ("THE THIRD PATCH SERIES OF THE ENFORCEMENT PACKAGE (WP-0.7; the advisor seat's; six patches under one rule:",
                  "VERIFIED WITH MAIN'S UNSEEN CASES AND LANDED AS SENT.",
                  "17 OF MAIN'S 22 UNSEEN CASES ARE CAUGHT, each by the gate that looks for the fault",
                  "FIVE PASS:",
                  "OF FIVE CASES MAIN WROTE AFTER READING THE PATCHES THREE PASS:",
                  "None is opened by the series, each passing without it; all go to the seat (P-820)")
_IN_WORDS = {3: "THREE", 5: "FIVE", 17: "17", 22: "22"}


def _what_the_verdict_line_and_the_rows_do_not_say(verdict, page):
    line = " ".join(str(verdict.get("claim_one_line", "")).split())
    out = [] if line.startswith(_THE_LINE_SAYS[0]) else ["the verdict line does not open as it did"]
    out += ["the verdict line does not say: " + s for s in _THE_LINE_SAYS[1:] if s not in line]
    for k in CASES:
        if k in PASS_UNSEEN:
            continue
        rows = [l for l in page.split("\n") if l.startswith("| %s |" % k) and " | caught: " in l]
        if len(rows) != 1:
            out.append("the page has not one row that says %s is caught" % k)
            continue
        answer = rows[0].split(" | caught: ", 1)[1]
        first = re.match(r"[a-z-]+", answer)
        if not first or first.group(0) not in RUN[k]["named gate"]:
            out.append("the row of %s does not open its answer with a gate the run names for it" % k)
    return out


def test_the_verdict_line_is_held_by_its_sentences_and_a_row_by_the_gate_the_run_names():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert _what_the_verdict_line_and_the_rows_do_not_say(v, F) == []
    # the numbers of the sentences are the runs'
    caught = [k for k in CASES if k not in PASS_UNSEEN]
    assert (_IN_WORDS[len(caught)], _IN_WORDS[len(CASES)], _IN_WORDS[len(PASS_UNSEEN)], _IN_WORDS[len(PASS_AFTER)]) == ("17", "22", "FIVE", "THREE")
    assert len([k for k in AFTER if k.startswith("AR")]) == 5
    line = v["claim_one_line"]
    as_the_lock_asked = lambda w: w["verdict"] == "PROVED" and w["claim_one_line"].startswith(_THE_LINE_SAYS[0]) and w["claim_one_line"].endswith("0 of 19.")
    a_row = next(l for l in F.split("\n") if l.startswith("| U16.b |") and " | caught: " in l)
    for what, w, page in (
            ("'17 OF MAIN'S 22' turned into '22 OF MAIN'S 22'", dict(v, claim_one_line=line.replace("17 OF MAIN'S 22 UNSEEN CASES ARE CAUGHT", "22 OF MAIN'S 22 UNSEEN CASES ARE CAUGHT")), F),
            ("'FIVE PASS' turned into 'NONE PASSES'", dict(v, claim_one_line=line.replace("FIVE PASS:", "NONE PASSES:")), F),
            ("'THREE PASS' turned into 'NONE PASSES'", dict(v, claim_one_line=line.replace("THE PATCHES THREE PASS:", "THE PATCHES NONE PASSES:")), F),
            ("the line cut after the part the lock held, its last words kept", dict(v, claim_one_line=line[:106] + " a gate reads all it is about). 0 of 19."), F),
            ("a row's gate replaced by another gate's name, the run's gate kept after it", v, F.replace(a_row, a_row.replace(" | caught: gate-controls", " | caught: framing, and not gate-controls")))):
        assert (w, page) != (v, F), what
        assert as_the_lock_asked(w), what                                         # what the lock asked of the verdict before passes each of them
        assert _what_the_verdict_line_and_the_rows_do_not_say(w, page), what
