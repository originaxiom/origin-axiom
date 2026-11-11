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
