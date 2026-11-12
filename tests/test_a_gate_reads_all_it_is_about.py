"""A gate reads all it is about, and what it does not read it says (the closure programme's WP-0.7, series 3).

The seat's planted cases PV16, PV17, PV20, PV21 and PV24.  Five gates passed because each read less than it is about: three
kinds of file of many, two shapes of row of three, a control's name and not the control, a cited lock and not whether one is
cited, an assert and not whether it can fail.  After this series each of the five reads the whole of what it is about, counts
in its sentence what it did not read, and holds by name what stood on the day the rule came.

Each test makes the situation in a small repository of its own, which holds this repository's gates and checkers and a few
pages, and runs the gate there.  Nothing in the environment moves a gate."""
import importlib.util
import json
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_the_reach_rule", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _commit(repo, message, files=None):
    for rel, text in (files or {}).items():
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(text, bytes):
            p.write_bytes(text)
        else:
            p.write_text(text, encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "--allow-empty", "-m", message)
    return _git(repo, "rev-parse", "HEAD")


def _scratch(tmp_path, files):
    """a small repository holding this repository's gates and checkers, and `files`, committed"""
    repo = tmp_path / "repo"
    skip = shutil.ignore_patterns("__pycache__", "*.pyc")
    shutil.copytree(ROOT / "scripts" / "gates", repo / "scripts" / "gates", ignore=skip)
    shutil.copytree(ROOT / "scripts" / "checks", repo / "scripts" / "checks", ignore=skip)
    _git(repo, "init", "-q")
    _commit(repo, "a small repository", files)
    return repo


_RUN = ("import sys, json, inspect, subprocess, importlib.util\n"
        "sys.dont_write_bytecode = True\n"
        "s = importlib.util.spec_from_file_location('scratch_gates', 'scripts/gates/gates.py')\n"
        "g = importlib.util.module_from_spec(s); s.loader.exec_module(g)\n"
        "gate = g.GATES[%r]\n"
        "takes = '_anchor' in inspect.signature(getattr(gate, '__wrapped__', gate)).parameters\n"
        "first = subprocess.run(['git', 'rev-list', '--max-parents=0', 'HEAD'], capture_output=True, text=True).stdout.strip()\n"
        "r = gate(_anchor=first) if takes else gate()\n"
        "print(json.dumps([bool(r[0]), r[1] if isinstance(r[1], str) else ' | '.join(map(str, r[1]))]))\n")


def _gate(repo, name):
    """the gate `name` of the small repository's own copy of the gates.  A gate that reads the past from an anchor (series 2)
    is given the small repository's first commit as its anchor."""
    r = subprocess.run([sys.executable, "-B", "-c", _RUN % name], cwd=str(repo), capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-800:]
    ok, detail = json.loads(r.stdout.strip().splitlines()[-1])
    return ok, detail


# ---- PV21: the framing gate read three kinds of file, and compared letter for letter -----------------------------------
def _banned():
    """one of the gate's banned phrases, taken from the gate and not typed here"""
    phrase = _gates().BANNED[2]
    assert "'" in phrase and " " in phrase          # the tests below break it at a space and change its apostrophe
    return phrase


def test_a_banned_phrase_written_as_the_gate_holds_it_fails_the_framing_gate(tmp_path):
    """the control: this held before the series"""
    repo = _scratch(tmp_path, {"docs/PAGE.md": "In this note " + _banned() + ".\n"})
    ok, detail = _gate(repo, "framing")
    assert ok is False and "docs/PAGE.md" in detail


def test_a_banned_phrase_in_a_tex_file_fails_the_framing_gate(tmp_path):
    repo = _scratch(tmp_path, {"papers/note.tex": "In this note " + _banned() + ".\n"})
    ok, detail = _gate(repo, "framing")
    assert ok is False, "a banned phrase in a .tex file under papers/, and the framing gate passed: " + detail
    assert "papers/note.tex" in detail


def test_a_banned_phrase_in_capitals_fails_the_framing_gate(tmp_path):
    repo = _scratch(tmp_path, {"README.md": "# A page\n\n" + _banned().upper() + ".\n"})
    ok, detail = _gate(repo, "framing")
    assert ok is False, "a banned phrase in capitals on the front page, and the framing gate passed: " + detail
    assert "README.md" in detail


def test_a_banned_phrase_is_read_as_a_reader_reads_it(tmp_path):
    """broken over two lines; with the apostrophe a typesetter sets; with a word in emphasis"""
    phrase = _banned()
    first, rest = phrase.split(" ", 1)
    for name, text in (("two_lines", first + "\n" + rest), ("apostrophe", phrase.replace("'", "’")),
                       ("emphasis", first + " **" + rest.split(" ", 1)[0] + "** " + rest.split(" ", 1)[1])):
        repo = _scratch(tmp_path / name, {"docs/PAGE.md": "It is said that " + text + ", and more.\n"})
        ok, detail = _gate(repo, "framing")
        assert ok is False, f"a banned phrase ({name}) passed the framing gate: {detail}"


def test_the_framing_gate_reads_a_file_whatever_its_name_ends_in(tmp_path):
    phrase = _banned()
    for rel in ("docs/page.rst", "frontier/B1_an_arc/arc_verdict.json", "papers/refs.bib", "story/chapter", "NOTES"):
        text = json.dumps({"claim_one_line": phrase}) if rel.endswith(".json") else "Here: " + phrase + "\n"
        repo = _scratch(tmp_path / rel.replace("/", "_"), {rel: text})
        ok, detail = _gate(repo, "framing")
        assert ok is False, f"a banned phrase in {rel} passed the framing gate: {detail}"
        assert rel in detail


def test_the_framing_gate_says_what_it_did_not_read(tmp_path):
    limit = getattr(_gates(), "FRAMING_MAX_BYTES", 5_000_000)
    data = "0123456789abcdef\n" * (limit // 17 + 2)                                    # a file above the limit: data, not a page
    repo = _scratch(tmp_path, {"docs/PAGE.md": "A page that claims nothing.\n", "frontier/B1_an_arc/census.jsonl": data,
                               "frontier/B1_an_arc/picture.png": b"\x89PNG\r\n\x1a\n\xff\xfe\x00\x00"})
    ok, detail = _gate(repo, "framing")
    assert ok is True, detail
    assert "1 above" in detail and "1 that are not text" in detail, "the gate does not say what it did not read: " + detail


def test_what_the_framing_gate_exempts_is_held_by_name():
    """an exemption is a file in which a banned phrase may stand.  A new one shows here as well as in the gate."""
    g = _gates()
    assert g.FRAMING_EXEMPT == {"GOVERNANCE.md", "scripts/gates/gates.py", "tests/test_repo_gates.py", "docs/atlas/FAILURE_ATLAS.md",
                                "frontier/B887_gate_audit/audit_reports.json"}
    ok, detail = g.GATES["framing"]()
    assert ok is True, detail


# ---- PV20: the claims gate checked that a cited lock exists, and not that a proven row cites one -----------------------
_CLAIMS = ("# Claims\n\n## Proven — exact, checkable\n\n| ID | Claim | Evidence |\n|---|---|---|\n"
           "| P1 | A proven claim. | `tests/test_p1.py` ✓ |\n%s\n"
           "## Conditional — given assumptions\n\n| ID | Claim | Named assumption |\n|---|---|---|\n| C1 | A conditional claim. | an assumption |\n\n"
           "## Certified data — test-locked\n\n| ID | Exhibit | Evidence |\n|---|---|---|\n| E1 | An exhibit. | `tests/test_e1.py` |\n%s\n"
           "## Open — targets\n\n| ID | Target |\n|---|---|\n| O1 | A target. |\n\n"
           "## Dead — falsified\n\n| ID | Killed claim | Why it died |\n|---|---|---|\n| D1 | A dead claim. | why |\n")
_A_TEST = "def test_it():\n    assert sum([1, 2]) == 3\n"


def _claims_repo(tmp_path, proven="", certified="", more=None):
    files = {"CLAIMS.md": _CLAIMS % (proven, certified), "tests/test_p1.py": _A_TEST, "tests/test_e1.py": _A_TEST}
    files.update(more or {})
    return _scratch(tmp_path, files)


def test_a_cited_lock_that_is_not_there_fails_the_claims_gate(tmp_path):
    """the control: this held before the series"""
    repo = _claims_repo(tmp_path, proven="| P2 | Another. | `tests/test_not_there.py` |\n")
    ok, detail = _gate(repo, "claims")
    assert ok is False and "tests/test_not_there.py" in detail


def test_a_proven_row_that_cites_no_lock_fails_the_claims_gate(tmp_path):
    repo = _claims_repo(tmp_path, proven="| P999 | A planted proven claim that cites no lock. | (no lock) |\n")
    ok, detail = _gate(repo, "claims")
    assert ok is False, "a proven row that cites no lock, and the claims gate passed: " + detail
    assert "P999" in detail


def test_a_certified_row_that_cites_no_lock_fails_the_claims_gate(tmp_path):
    repo = _claims_repo(tmp_path, certified="| E2 | An exhibit locked by nothing. | `frontier/B1_an_arc` |\n")
    ok, detail = _gate(repo, "claims")
    assert ok is False, "a row of the table that says it is test-locked cites no lock, and the claims gate passed: " + detail
    assert "E2" in detail


def test_a_row_that_cites_a_file_holding_no_test_fails_the_claims_gate(tmp_path):
    repo = _claims_repo(tmp_path, proven="| P2 | Another. | `tests/test_empty.py` |\n", more={"tests/test_empty.py": "# nothing here yet\n"})
    ok, detail = _gate(repo, "claims")
    assert ok is False, "a proven row cites a file with no test in it, and the claims gate passed: " + detail
    assert "tests/test_empty.py" in detail


def test_the_rows_that_are_not_locked_need_no_lock(tmp_path):
    """a conditional, an open and a dead row cite none, and the gate passes: the rule is for the two tables that say locked"""
    repo = _claims_repo(tmp_path)
    ok, detail = _gate(repo, "claims")
    assert ok is True, detail
    assert "2 rows in the locked tables, 2 citing a lock" in detail, "the gate does not say what it read: " + detail


def test_the_one_proven_row_without_a_lock_is_held_by_name():
    """on this repository one proven row cited no lock on the day the rule came.  It is named, and a second shows here too."""
    g = _gates()
    assert getattr(g, "CITES_NO_LOCK_AS_FOUND", None) == frozenset(("P51",)), "no table of the rows held by name"
    n, without = g.rows_that_cite_no_lock((ROOT / "CLAIMS.md").read_text(encoding="utf-8"))
    assert set(without) <= g.CITES_NO_LOCK_AS_FOUND, without
    ok, detail = g.GATES["claims"]()
    assert ok is True, detail
    assert "by name" in detail


# ---- PV24: the vacuity gate refused a test with no assert, and not a test in which no assert can fail ------------------
_REAL = "def test_real():\n    assert sum([1, 2]) == 3\n"


def _vacuity(tmp_path, name, body, where="tests/test_planted.py"):
    repo = _scratch(tmp_path / name, {"tests/test_real.py": _REAL, where: body})
    return _gate(repo, "test-vacuity")


def test_a_test_with_no_assert_fails_the_vacuity_gate(tmp_path):
    """the control: this held before the series"""
    ok, detail = _vacuity(tmp_path, "control", "def test_nothing():\n    pass\n")
    assert ok is False and "test_nothing" in detail


def test_a_test_whose_only_assert_is_between_two_literals_fails_the_vacuity_gate(tmp_path):
    """PV24 as planted"""
    ok, detail = _vacuity(tmp_path, "pv24", "def test_orbit_counts_differ():\n    assert 1 != 2\n")
    assert ok is False, "a test whose only assert is `assert 1 != 2`, and the vacuity gate passed: " + detail
    assert "tests/test_planted.py::test_orbit_counts_differ" in detail


_CANNOT_FAIL = {
    "another operator": "def test_x():\n    assert 1 < 2\n",
    "a name bound to a literal": "def test_x():\n    n = 5\n    assert n * n - 1 == 24\n    assert n - 1 == 4\n",
    "and, or, in": "def test_x():\n    assert 2 + 2 == 4 and 'a' in 'abc' or 0 > 1\n",
    "an entry of a literal table": "def test_x():\n    t = {'a': 1.8, 'b': 0.9}\n    assert t['a'] > 1.5 and t['b'] < 1.0\n",
    "identity of constants": "def test_x():\n    assert True is not False\n",
    "a small power": "def test_x():\n    assert 63 + 6 + 1 + 11 == 81 == 3**4\n",
    "a call beside it": "def test_x():\n    unused = sorted([3, 1])\n    assert 1 != 2\n",
    "in a loop over something computed": "def test_x():\n    for row in sorted([3, 1]):\n        assert 52 + 26 == 78\n",
}


def test_every_shape_of_a_test_in_which_no_assert_can_fail_is_refused(tmp_path):
    for name, body in _CANNOT_FAIL.items():
        ok, detail = _vacuity(tmp_path, name.replace(" ", "_").replace(",", ""), body)
        assert ok is False, f"a test in which no assert can fail ({name}) passed the vacuity gate: {detail}"
        assert "no assert can fail" in detail and "test_x" in detail


_CAN_FAIL = {
    "one literal assert among real ones": "def test_x():\n    assert 52 + 26 == 78\n    assert sum([1, 2]) == 3\n",
    "assert False under a condition": "def test_x():\n    for v in sorted([3, 1]):\n        if v > 5:\n            assert False, v\n",
    "an assert that is false when reached": "def test_x():\n    for v in sorted([3, 1]):\n        if v > 5:\n            assert 1 == 0, 'unreachable'\n",
    "a flag set on two paths": ("def test_x():\n    try:\n        int('x')\n        raised = False\n    except ValueError:\n        raised = True\n"
                                "    assert raised is True\n"),
    "a list handed to a call": "def _fill(xs):\n    xs.append(1)\n\n\ndef test_x():\n    seen = []\n    _fill(seen)\n    assert seen == [1]\n",
    "an argument": "import pytest\n\n\n@pytest.mark.parametrize('n', [3])\ndef test_x(n):\n    assert n == 3\n",
    "a name bound under a condition": "def test_x():\n    if sum([1, 2]) == 3:\n        n = 3\n    assert n == 3\n",
    "a call in the assert": "def test_x():\n    assert len([1, 2]) == 2\n",
    "a call named assert": "def _assert_close(a, b):\n    assert abs(a - b) < 1e-9\n\n\ndef test_x():\n    _assert_close(sum([1, 2]), 3)\n    assert 78 == 52 + 26\n",
}


def test_a_test_that_can_fail_is_not_refused(tmp_path):
    """the other side: nothing here is in the class, and the gate passes.  (`a call in the assert` cannot fail either; the
    class stops at a call, which is a computation whatever it calls, and this pins where it stops.)"""
    for name, body in _CAN_FAIL.items():
        ok, detail = _vacuity(tmp_path, name.replace(" ", "_"), body)
        assert ok is True, f"a test that can fail ({name}) was refused by the vacuity gate: {detail}"


def test_the_vacuity_gate_reads_an_arcs_own_lock(tmp_path):
    arc = "frontier/B1_an_arc/verification/test_b1_an_arc.py"
    ok, detail = _vacuity(tmp_path, "arc_no_assert", "def test_nothing():\n    pass\n", where=arc)
    assert ok is False, "an arc's own lock with a test that asserts nothing, and the vacuity gate passed: " + detail
    assert arc in detail
    ok, detail = _vacuity(tmp_path, "arc_literal", "def test_x():\n    assert 1 != 2\n", where=arc)
    assert ok is False and arc in detail
    ok, detail = _vacuity(tmp_path, "arc_real", _REAL.replace("test_real", "test_b1"), where=arc)
    assert ok is True and "1 more in the arcs' own locks" in detail, "the gate does not say that it read the arc's lock: " + detail


def test_the_tests_in_which_no_assert_can_fail_are_held_by_name():
    """26 stood on this repository on the day the rule came.  A 27th fails the gate, and a new name in the table shows here."""
    g = _gates()
    held = getattr(g, "CANNOT_FAIL_AS_FOUND", None)
    assert held is not None and len(held) == 26, "no table of the tests held by name, or not the 26 that were found"
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    try:
        import check_test_vacuity as ctv
    finally:
        sys.path.pop(0)
    found = set(ctv.read_locks()["CANNOT-FAIL"])
    assert found <= held, sorted(found - held)
    assert "tests/test_b710_thimbles.py::test_orbit_counts_differ" in held          # the one the planted case was written after


# ---- PV17: the sweep read two shapes of row of its registry, and passed over the rest in silence -----------------------
# The phrases here are made up, so that this file holds none that main's registry sweeps.
_REG_HEAD = "# The registry\n\n| # | phrase | arc | why |\n|---|---|---|---|\n| 1 | `the lamp is always green` | B1 | it was wrong |\n\n"
_UNQUOTED = ("## Added later: phrasings withdrawn in a later window\n\n| withdrawn phrase | why | the current statement |\n|---|---|---|\n"
             "| the gadget is forced, and no choice is made (B7) | two choices exist | a convention |\n"
             "| a third carrier, reading (+3, +1) (B8) | noise | the pair is alone |\n")


def _sweep_repo(tmp_path, name, registry, pages):
    files = {"docs/RETRACTED_PHRASES.md": registry}
    files.update(pages)
    return _scratch(tmp_path / name, files)


def _in_the_sweeps_table(repo, table, entry):
    """an entry in the small repository's own copy of one of the sweep's two tables, as main would write one"""
    p = repo / "scripts" / "checks" / "retraction_sweep.py"
    src = p.read_text(encoding="utf-8")
    assert src.count(table + " = {") == 1, "no table %s in the sweep" % table
    p.write_text(src.replace(table + " = {", table + " = {" + entry + ",", 1), encoding="utf-8")
    _commit(repo, "an entry in " + table)


def test_a_registered_phrase_in_a_numbered_row_is_swept(tmp_path):
    """the control: this held before the series"""
    repo = _sweep_repo(tmp_path, "control", _REG_HEAD, {"README.md": "We find that the lamp is always green, as before.\n"})
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is False and "README.md" in detail


def test_a_phrase_in_an_unquoted_row_is_swept(tmp_path):
    """PV17 as planted: a row whose phrase stands unquoted in the first cell, and the phrase on the front page"""
    repo = _sweep_repo(tmp_path, "pv17", _REG_HEAD + _UNQUOTED, {"README.md": "# A page\n\nThe gadget is forced, and no choice is made.\n"})
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is False, "a phrase of an unquoted row of the registry stands on the front page, and the sweep passed: " + detail
    assert "README.md" in detail and "the gadget is forced" in detail


def test_the_note_that_ends_an_unquoted_cell_is_not_part_of_the_phrase(tmp_path):
    repo = _sweep_repo(tmp_path, "note", _REG_HEAD + _UNQUOTED, {"docs/PAGE.md": "There is a third carrier, reading (+3, +1), we said.\n"})
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is False, "the phrase without its source note passed the sweep: " + detail
    assert "reading (+3, +1)" in detail and "(B8)" not in detail


def test_a_row_in_no_shape_the_sweep_reads_is_refused(tmp_path):
    for name, row in (("a_number_and_no_backticks", "| 2 | a sentence with no backticks | B2 | why |"),
                      ("a_quote_that_does_not_close", '| "a sentence whose quote does not close | B2 | why |'),
                      ("an_empty_first_cell", "|  | B2 | why |")):
        repo = _sweep_repo(tmp_path, name, _REG_HEAD + "| h | h | h |\n|---|---|---|\n" + row + "\n", {"README.md": "# A page\n"})
        ok, detail = _gate(repo, "retraction-sweep")
        assert ok is False, f"a row the sweep cannot read ({name}) was passed over in silence: {detail}"
        assert "in no shape the sweep reads" in detail


def test_a_registered_phrase_that_can_never_fire_is_refused(tmp_path):
    """the sweep allows any line that carries a word of mention (a retraction's own vocabulary), so a registered phrase that
    holds such a word is swept by nothing.  This seat's first made-up phrase for these tests was one, and its control passed."""
    registry = _REG_HEAD + "| 2 | `the result was formerly exact` | B2 | it was not |\n"
    repo = _sweep_repo(tmp_path, "mute", registry, {"README.md": "# A page\n\nThe result was formerly exact.\n"})
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is False, "a registered phrase that no line can violate, and the sweep passed: " + detail
    assert "can ever be a violation" in detail and "formerly exact" in detail


def test_a_row_named_as_a_reading_is_read_and_not_swept(tmp_path):
    pages = {"README.md": "# A page\n\nThe gadget is forced, and no choice is made.\n"}
    repo = _sweep_repo(tmp_path, "reading", _REG_HEAD + _UNQUOTED, pages)
    assert _gate(repo, "retraction-sweep")[0] is False
    _in_the_sweeps_table(repo, "NOT_SWEPT_BY_NAME", '"the gadget is forced, and no choice is made (B7)": "2026-11-11 -- only a reading of it is withdrawn"')
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is True, detail
    assert "1 that retract a reading and are not swept, 1 of them by name" in detail


def test_where_a_phrase_already_stood_it_is_held_by_its_file_and_its_phrase(tmp_path):
    title = "# B7: the gadget is forced, and no choice is made\n\nCorrected below.\n"
    pages = {"frontier/B7_the_gadget/FINDINGS.md": title, "README.md": "# A page\n"}
    repo = _sweep_repo(tmp_path, "stands", _REG_HEAD + _UNQUOTED, pages)
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is False and "frontier/B7_the_gadget/FINDINGS.md" in detail
    _in_the_sweeps_table(repo, "STANDS_AS_FOUND", '("frontier/B7_the_gadget/FINDINGS.md", "the gadget is forced, and no choice is made"): "the title as first written"')
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is True and "1 standing instance(s) of a phrase held by name as found" in detail, detail
    # the phrase is swept everywhere else
    _commit(repo, "the phrase on the front page", {"README.md": "# A page\n\nThe gadget is forced, and no choice is made.\n"})
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is False and "README.md" in detail and "FINDINGS.md" not in detail
    # and the file is held for that phrase alone
    _commit(repo, "another phrase in the held file", {"README.md": "# A page\n", "frontier/B7_the_gadget/FINDINGS.md": title + "And the lamp is always green there.\n"})
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is False and "FINDINGS.md" in detail and "the lamp is always green" in detail


def test_the_sweep_says_how_many_rows_it_read(tmp_path):
    reading = '| "a sentence" read as more than it says | B3 | only the reading |\n'
    repo = _sweep_repo(tmp_path, "says", _REG_HEAD + _UNQUOTED + reading, {"README.md": "# A page\n"})
    ok, detail = _gate(repo, "retraction-sweep")
    assert ok is True, detail
    assert "4 rows of the registry read: 3 swept, 1 that retract a reading and are not swept" in detail, "the sweep does not say what it read: " + detail


def test_on_this_repository_every_row_of_the_registry_is_read():
    """no row is passed over; the rows that only retract a reading, and the lines where a phrase already stood, are by name"""
    g = _gates()
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    try:
        import retraction_sweep as rs
    finally:
        sys.path.pop(0)
    rows = getattr(rs, "rows_in", lambda text: [("unread", None, "the reader accounts for no row")])((ROOT / "docs" / "RETRACTED_PHRASES.md").read_text(encoding="utf-8"))
    kinds = [kind for kind, _phrase, _cell in rows]
    assert "unread" not in kinds and kinds.count("swept") >= 46 and kinds.count("reading") >= 8, kinds
    swept = [phrase for kind, phrase, _cell in rows if kind == "swept"]
    assert any(p.startswith("the convention ") and p.endswith("no choice is made") for p in swept)       # a row the planted case took its phrase from
    # 12 until 2026-11-12: main mended the one instance that was not a record, the row of the paper's table of candidate claims,
    # in the commit that landed this series (B1896), and shortened the table in that commit, as the sentence asks
    assert len(rs.NOT_SWEPT_BY_NAME) == 2 and len(rs.STANDS_AS_FOUND) == 11                             # a new name shows here as well
    ok, detail = g.GATES["retraction-sweep"]()
    assert ok is True, detail
    assert "by name" in detail and "shorten the table" not in detail


# ---- PV16: the controls gate checked that a control's name is defined, and nothing of the control ----------------------
_CONTROL_OK = ("def test_the_gate_fails_on_a_planted_case():\n    answers = sorted([False, True])\n    assert answers[0] is False\n")


def _controls_repo(tmp_path, name, controls_file):
    """a small repository whose every gate has the same honest control, in tests/test_controls.py"""
    names = sorted(_gates().GATES)
    reg = {g: "tests/test_controls.py::test_the_gate_fails_on_a_planted_case" for g in names}
    files = {"tests/test_controls.py": controls_file, "tests/GATE_CONTROLS.json": json.dumps(reg, indent=1) + "\n"}
    return _scratch(tmp_path / name, files), reg


def _repoint(repo, reg, gate, ref, more=None):
    files = {"tests/GATE_CONTROLS.json": json.dumps(dict(reg, **{gate: ref}), indent=1) + "\n"}
    files.update(more or {})
    _commit(repo, "a control pointed elsewhere", files)


def test_a_control_whose_function_is_not_there_fails_the_controls_gate(tmp_path):
    """the control: this held before the series"""
    repo, reg = _controls_repo(tmp_path, "control", _CONTROL_OK)
    assert _gate(repo, "gate-controls")[0] is True
    _repoint(repo, reg, "framing", "tests/test_controls.py::test_that_is_not_there")
    ok, detail = _gate(repo, "gate-controls")
    assert ok is False and "not defined" in detail


def test_every_control_pointed_at_a_skipped_trivial_test_fails_the_controls_gate(tmp_path):
    """PV16 as planted: one skipped test for every gate, whose only line is an assert between constants"""
    names = sorted(_gates().GATES)
    planted = "import pytest\n" + "".join(
        "\n\n@pytest.mark.skip(reason='planted')\ndef test_control_%s():\n    assert True is not False\n" % g.replace("-", "_") for g in names)
    reg = {g: "tests/test_zz_planted_controls.py::test_control_%s" % g.replace("-", "_") for g in names}
    repo = _scratch(tmp_path, {"tests/test_zz_planted_controls.py": planted, "tests/GATE_CONTROLS.json": json.dumps(reg, indent=1) + "\n"})
    ok, detail = _gate(repo, "gate-controls")
    assert ok is False, "every gate's control is a skipped test that asserts nothing of it, and the controls gate passed: " + detail
    assert "is skipped" in detail


_NO_CONTROL = {
    "a skipif mark": ("import pytest\n\n\n@pytest.mark.skipif(True, reason='x')\n" + _CONTROL_OK, "is skipped"),
    "an xfail mark": ("import pytest\n\n\n@pytest.mark.xfail\n" + _CONTROL_OK, "is skipped"),
    "a skip in its body": ("import pytest\n\n\ndef test_the_gate_fails_on_a_planted_case():\n    pytest.skip('not today')\n    assert sorted([2, 1])[0] == 1\n", "may skip itself"),
    "an importorskip in its body": ("import pytest\n\n\ndef test_the_gate_fails_on_a_planted_case():\n    pytest.importorskip('a_package_nobody_has')\n"
                                    "    assert sorted([2, 1])[0] == 1\n", "may skip itself"),
    "a module marked skip": ("import pytest\n\npytestmark = pytest.mark.skip(reason='the whole file')\n\n\n" + _CONTROL_OK, "module marked"),
    "a module that may skip at import": ("import pytest\n\npytest.importorskip('a_package_nobody_has')\n\n\n" + _CONTROL_OK, "skip itself at import"),
    "no assert": ("def test_the_gate_fails_on_a_planted_case():\n    sorted([2, 1])\n", "asserts nothing"),
    "no assert that can fail": ("def test_the_gate_fails_on_a_planted_case():\n    assert True is not False\n", "no assert that can fail"),
    "a method of a class, not a test of the file": ("class TestIt:\n    def test_the_gate_fails_on_a_planted_case(self):\n        assert sorted([2, 1])[0] == 1\n", ""),
}


def test_a_control_that_cannot_control_is_refused_in_every_form(tmp_path):
    for name, (body, words) in _NO_CONTROL.items():
        repo, reg = _controls_repo(tmp_path, name.replace(" ", "_").replace(",", ""), body)
        ok, detail = _gate(repo, "gate-controls")
        assert ok is False, f"a control that cannot control ({name}) passed the controls gate: {detail}"
        assert words in detail, (name, detail)


def test_a_control_pointed_at_another_test_has_left_the_register(tmp_path):
    """the rule of series 2, for the register of controls: a gate pointed at another test, however honest that test looks, is
    a row that left.  It needs a recorded act."""
    repo, reg = _controls_repo(tmp_path, "repoint", _CONTROL_OK)
    assert _gate(repo, "gate-controls")[0] is True
    other = "def test_something_else():\n    assert sorted([2, 1])[0] == 1\n"
    _repoint(repo, reg, "framing", "tests/test_other.py::test_something_else", {"tests/test_other.py": other})
    ok, detail = _gate(repo, "gate-controls")
    assert ok is False, "a gate's control was pointed at another test with no record, and the controls gate passed: " + detail
    assert "1 control(s) left tests/GATE_CONTROLS.json" in detail and "framing -> tests/test_controls.py" in detail
    # the recorded act
    p = repo / "scripts" / "gates" / "gates.py"
    src = p.read_text(encoding="utf-8")
    assert src.count("LEFT_BY_NAME = {}") == 1
    key = "framing -> tests/test_controls.py::test_the_gate_fails_on_a_planted_case"
    p.write_text(src.replace("LEFT_BY_NAME = {}", "LEFT_BY_NAME = {%r: {%r: %r}}" % ("tests/GATE_CONTROLS.json", key, "2026-11-12 -- replaced by a control that plants the case in a file")), encoding="utf-8")
    _commit(repo, "the act recorded")
    ok, detail = _gate(repo, "gate-controls")
    assert ok is True and "1 control(s) left by name" in detail, detail


def test_on_this_repository_every_control_is_read_and_none_is_refused():
    g = _gates()
    ok, detail = g.GATES["gate-controls"]()
    assert ok is True, detail
    assert "each read: none is kept from running" in detail, "the controls gate does not say that it read the controls: " + detail
    assert g.result_line("gate-controls", ok, detail).strip().startswith("PASS")          # the runner prints a sentence with the word "skipped" as a skip
    reg = json.loads((ROOT / "tests" / "GATE_CONTROLS.json").read_text(encoding="utf-8"))
    assert len(reg) == len(g.GATES)
    for gate, ref in reg.items():
        f, fn = ref.split("::")
        assert g.control_cannot_control((ROOT / f).read_text(encoding="utf-8"), fn) is None, gate
