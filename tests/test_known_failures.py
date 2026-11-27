"""2026-11-26 (the framework's thin path, patch T10; register row P-885): the known-failures baseline,
scripts/queue/baseline.py, and the gate known-failures.

A list whose entry names no register row, or a row the register does not hold, fails the gate, and its twin passes; a
list that grows along the history fails it, and one that shrinks passes; a run with a failure or a red gate the list does
not hold is a new failure, and an entry that now passes is reported for taking off; the draft leaves the rows to main; the
list holds main's seven first entries (M63) and the gate passes on the record."""
import importlib.util
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


BL = _load("baseline_under_test", "scripts/queue/baseline.py")
GATES = _load("gates_for_the_baseline", "scripts/gates/gates.py")
TWIN = {"note": "x", "tests": [{"id": "tests/test_a.py::test_one", "row": "P-885", "why": "a seat branch not fetched"}],
        "gates": [{"id": "harvest-debt", "row": "P-881", "why": "a pin that does not resolve in a shallow clone"}]}


def test_a_list_that_grows_or_names_no_row_fails_the_gate_and_its_twin_passes(tmp_path):
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True)
    g("init", "-q")
    g("commit", "-q", "--allow-empty", "-m", "a repository whose list is not committed yet")
    assert GATES.gate_known_failures(TWIN, tmp_path)[0] is True
    bad = json.loads(json.dumps(TWIN))
    bad["tests"][0]["row"] = "P-99999"
    ok, detail = GATES.gate_known_failures(bad, tmp_path)
    assert not ok and "not a row of the register" in detail
    (tmp_path / "queue").mkdir()
    f = tmp_path / "queue" / "KNOWN_FAILURES.json"
    for version, msg in ((TWIN, "the list"), (dict(TWIN, gates=[]), "it shrinks")):
        f.write_text(json.dumps(version), encoding="utf-8")
        g("add", "-A")
        g("commit", "-q", "-m", msg)
    assert GATES.gate_known_failures(dict(TWIN, gates=[]), tmp_path)[0] is True
    f.write_text(json.dumps(TWIN), encoding="utf-8")
    g("commit", "-q", "-am", "it grows")
    ok, detail = GATES.gate_known_failures(TWIN, tmp_path)
    assert not ok and "adds harvest-debt: the list may only shrink" in detail


def test_the_lists_form():
    known = {"P-885", "P-881"}
    assert BL.form_problems(TWIN, known) == []
    for change, words in ((lambda d: d.update(score=1), "not in the schema"),
                          (lambda d: d.update(tests="none"), "tests is not a list"),
                          (lambda d: d["tests"].append(dict(d["tests"][0])), "stands twice"),
                          (lambda d: d["tests"][0].update(row="885"), "names no register row"),
                          (lambda d: d["tests"][0].update(why=""), "says not why"),
                          (lambda d: d["gates"][0].pop("why"), "is not {id, row, why}")):
        d = json.loads(json.dumps(TWIN))
        change(d)
        bad = BL.form_problems(d, known)
        assert bad and any(words in b for b in bad), (words, bad)


def test_a_run_against_the_list():
    new, gone = BL.compare(TWIN, ["tests/test_a.py::test_one", "tests/test_b.py::test_two"], ["harvest-debt"])
    assert new == ["test tests/test_b.py::test_two"] and gone == []
    new, gone = BL.compare(TWIN, [], ["harvest-debt", "attribution"])
    assert new == ["gate attribution"] and gone == ["test tests/test_a.py::test_one"]


def test_the_commands_by_hand_and_mains_first_entries(tmp_path):
    f = tmp_path / "failed.txt"
    f.write_text("FAILED tests/test_b.py::test_two - AssertionError: x\n", encoding="utf-8")
    run = lambda *a: subprocess.run([sys.executable, "-B", str(ROOT / "scripts/queue/baseline.py"), *map(str, a)],
                                    capture_output=True, text=True)
    r = run("--compare", f)
    assert r.returncode == 1 and "NEW: test tests/test_b.py::test_two" in r.stdout
    draft = json.loads(run("--draft", f).stdout)
    assert draft["tests"] == [{"id": "tests/test_b.py::test_two", "row": "P-?", "why": "?"}]
    assert run("--check").returncode == 0
    shipped = json.loads((ROOT / "queue" / "KNOWN_FAILURES.json").read_text(encoding="utf-8"))
    assert GATES.gate_known_failures()[0]
    # the list as shipped: its form and rows, and no flake on it (M63). Not its count: the list is meant to shrink (M65)
    assert BL.form_problems(shipped, BL.rows()) == []
    assert not any("b618" in e["id"] or "b1968" in e["id"] for e in shipped["tests"] + shipped["gates"])


def test_a_list_grown_in_the_working_tree_fails_the_gate(tmp_path):
    """main's M65: the history alone passed a list grown and not committed"""
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True)
    g("init", "-q")
    (tmp_path / "queue").mkdir()
    (tmp_path / "queue" / "KNOWN_FAILURES.json").write_text(json.dumps(dict(TWIN, gates=[])), encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "the list")
    assert GATES.gate_known_failures(dict(TWIN, gates=[]), tmp_path)[0] is True
    ok, detail = GATES.gate_known_failures(TWIN, tmp_path)
    assert not ok and "to its last committed version" in detail


def test_a_runs_lines_are_read_to_their_test_ids():
    for line, want in (("FAILED tests/test_b.py::test_two - AssertionError: x", "tests/test_b.py::test_two"),
                       ("ERROR tests/x.py - ImportError: no module", "tests/x.py"),
                       ("FAILED tests/t.py::test_p[a - b] - assert 1", "tests/t.py::test_p[a - b]"),
                       ("tests/t.py::test_plain", "tests/t.py::test_plain")):
        assert BL.test_id(line) == want, line
