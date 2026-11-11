"""Nothing leaves a ledger, and no ceiling rises, without a recorded act (the closure programme's WP-0.7, series 2; built by
the advisor seat and verified by main).

The seat's planted cases PV10 to PV13 and PV19.  Five gates passed on a page that had been deleted or emptied, and one
ceiling could be raised by the commit it was meant to stop.  The rule is read from history: after an anchor commit, what a
ledger has held it still holds, unless it is named with its date and what became of it.

Each test makes the situation in a small repository of its own, which holds this repository's gates and checkers and a
page of a few rows, and runs the gate there.  The anchor is passed to the gate as an argument; nothing in the environment
moves a gate."""
import importlib.util
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_the_ledger_rule", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _commit(repo, message, files=None, delete=()):
    for rel, text in (files or {}).items():
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    for rel in delete:
        (repo / rel).unlink()
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "--allow-empty", "-m", message)
    return _git(repo, "rev-parse", "HEAD")


def _scratch(tmp_path, files):
    """a small repository holding this repository's gates and checkers, and `files`; returns it with its first commit"""
    repo = tmp_path / "repo"
    skip = shutil.ignore_patterns("__pycache__", "*.pyc")
    shutil.copytree(ROOT / "scripts" / "gates", repo / "scripts" / "gates", ignore=skip)
    shutil.copytree(ROOT / "scripts" / "checks", repo / "scripts" / "checks", ignore=skip)
    _git(repo, "init", "-q")
    return repo, _commit(repo, "the anchor", files)


_RUN = ("import sys, json, inspect, importlib.util\n"
        "sys.dont_write_bytecode = True\n"
        "s = importlib.util.spec_from_file_location('scratch_gates', 'scripts/gates/gates.py')\n"
        "g = importlib.util.module_from_spec(s); s.loader.exec_module(g)\n"
        "gate = g.GATES[%r]\n"
        "takes = '_anchor' in inspect.signature(getattr(gate, '__wrapped__', gate)).parameters\n"
        "r = gate(_anchor=%r) if takes else gate()      # a gate from before this rule takes no anchor: it is run as it was\n"
        "print(json.dumps([bool(r[0]), r[1] if isinstance(r[1], str) else ' | '.join(map(str, r[1]))]))\n")


def _gate(repo, name, anchor):
    """the gate `name` of the small repository's own copy of the gates, read from `anchor` on.  (On the commit before a
    mend the gate takes no anchor and is run as it was, so that each case's test fails there for the case's own reason.)"""
    r = subprocess.run([sys.executable, "-B", "-c", _RUN % (name, anchor)], cwd=str(repo), capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-800:]
    ok, detail = json.loads(r.stdout.strip().splitlines()[-1])
    return ok, detail


def _name_in_the_gate(repo, path, key, record):
    """the recorded act: an entry in the small repository's LEFT_BY_NAME, as main would write one"""
    p = repo / "scripts" / "gates" / "gates.py"
    src = p.read_text(encoding="utf-8")
    assert src.count("LEFT_BY_NAME = {}") == 1
    p.write_text(src.replace("LEFT_BY_NAME = {}", "LEFT_BY_NAME = {%r: {%r: %r}}" % (path, key, record)), encoding="utf-8")


# ---- the rule itself, on a page of three rows ----------------------------------------------------------------------------
_rows = lambda text: re.findall(r"^\| (\w+) \|", text, re.M)


def test_what_a_page_has_held_is_read_from_the_anchor_on(tmp_path):
    g = _gates()
    repo = tmp_path / "small"
    repo.mkdir()
    _git(repo, "init", "-q")
    before = _commit(repo, "before the anchor", {"page.md": "| old |\n| a |\n"})
    anchor = _commit(repo, "the anchor", {"page.md": "| a |\n| b |\n"})                 # "old" left before the anchor: not re-judged
    assert g.held_since("page.md", _rows, anchor, repo) == ({"a", "b"}, None)
    _commit(repo, "a row is added", {"page.md": "| a |\n| b |\n| c |\n"})
    _commit(repo, "and taken away again, with another", {"page.md": "| a |\n"})
    held, why = g.held_since("page.md", _rows, anchor, repo)
    assert why is None and held == {"a", "b", "c"}                                      # c was never at the anchor, and it was held
    now = (repo / "page.md").read_text(encoding="utf-8")
    problem, note = g.left_the_ledger("page.md", _rows, now, "row", anchor, repo, named={})
    assert problem and "2 row(s) left page.md" in problem and "b" in problem and "c" in problem and note == ""
    # one of the two named: the other still fails, and the named one is in the note
    problem, note = g.left_the_ledger("page.md", _rows, now, "row", anchor, repo, named={"c": "2026-11-11 -- merged into a"})
    assert problem and "1 row(s) left page.md" in problem and "by name" in note and "merged into a" in note
    # both named: no problem, and the sentence says how many left by name
    problem, note = g.left_the_ledger("page.md", _rows, now, "row", anchor, repo, named={"b": "2026-11-11 -- x", "c": "2026-11-11 -- y"})
    assert problem is None and "2 row(s) left by name" in note
    # a name with no reason is not a record
    problem, _ = g.left_the_ledger("page.md", _rows, now, "row", anchor, repo, named={"b": "", "c": "  "})
    assert problem and "2 row(s) left" in problem
    # the page deleted outright: everything it held has left
    problem, _ = g.left_the_ledger("page.md", _rows, "", "row", anchor, repo, named={})
    assert problem and "3 row(s) left" in problem
    # a page that was not there at the anchor held nothing then
    assert g.held_since("other.md", _rows, anchor, repo) == (set(), None)
    # and where the history cannot be read back to the anchor, the answer is that it cannot be verified
    assert "cannot verify" in g.held_since("page.md", _rows, "0" * 40, repo)[1]
    _git(repo, "checkout", "-q", "--detach", before)
    assert "does not descend" in g.held_since("page.md", _rows, anchor, repo)[1]


def test_the_rule_reads_main_from_its_anchor_and_nothing_is_named_yet():
    g = _gates()
    assert g.LEFT_BY_NAME == {}, "a row that leaves a ledger is named here with its date and what became of it; say so in this lock too"
    assert re.fullmatch(r"[0-9a-f]{40}", g.NOTHING_LEAVES_FROM)
    assert subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", g.NOTHING_LEAVES_FROM, "HEAD"]).returncode == 0


# ---- PV11: the registry of retracted phrases -----------------------------------------------------------------------------
_REGISTRY = ("# Retracted phrases\n\n| # | phrase | arc | why |\n|---|---|---|---|\n"
             "| 1 | `the first retracted phrase` | B1 | it was wrong |\n| 2 | `the second retracted phrase` | B2 | so was this |\n")


def test_the_registry_of_retracted_phrases_deleted_turns_the_sweep_red(tmp_path):
    """PV11 as planted.  With no registry the sweep read no phrase, swept for nothing and passed."""
    repo, anchor = _scratch(tmp_path, {"docs/RETRACTED_PHRASES.md": _REGISTRY})
    assert _gate(repo, "retraction-sweep", anchor) == (True, "ok")
    _commit(repo, "the registry is deleted", delete=["docs/RETRACTED_PHRASES.md"])
    ok, detail = _gate(repo, "retraction-sweep", anchor)
    assert ok is False and "RETRACTED_PHRASES.md missing" in detail


def test_a_phrase_that_leaves_the_registry_turns_the_sweep_red_unless_it_is_named(tmp_path):
    repo, anchor = _scratch(tmp_path, {"docs/RETRACTED_PHRASES.md": _REGISTRY})
    thinned = "\n".join(l for l in _REGISTRY.split("\n") if "second retracted" not in l)
    _commit(repo, "one phrase leaves the registry", {"docs/RETRACTED_PHRASES.md": thinned})
    ok, detail = _gate(repo, "retraction-sweep", anchor)
    assert ok is False and "1 retracted phrase(s) left docs/RETRACTED_PHRASES.md" in detail and "the second retracted phrase" in detail
    # emptied, not deleted: the file is there and holds no phrase
    _commit(repo, "the registry is emptied", {"docs/RETRACTED_PHRASES.md": "# Retracted phrases\n"})
    ok, detail = _gate(repo, "retraction-sweep", anchor)
    assert ok is False and "2 retracted phrase(s) left" in detail
    # the recorded act: the phrase named in the gate, with its date and what became of it
    _commit(repo, "one phrase back", {"docs/RETRACTED_PHRASES.md": thinned})
    _name_in_the_gate(repo, "docs/RETRACTED_PHRASES.md", "the second retracted phrase", "2026-11-11 -- the retraction was itself withdrawn (B3)")
    _commit(repo, "and the other named")
    ok, detail = _gate(repo, "retraction-sweep", anchor)
    assert ok is True and "1 retracted phrase(s) left by name" in detail and "withdrawn (B3)" in detail
    # the runner prints that sentence whole, where it prints a bare ok for a pass with nothing to say
    g = _gates()
    assert g.result_line("retraction-sweep", True, detail).strip() == "PASS  retraction-sweep: " + detail
    assert g.result_line("retraction-sweep", True, "ok").strip() == "PASS  retraction-sweep: ok"


def test_a_phrase_added_after_the_anchor_and_then_removed_has_left_too(tmp_path):
    repo, anchor = _scratch(tmp_path, {"docs/RETRACTED_PHRASES.md": _REGISTRY})
    _commit(repo, "a third phrase is registered", {"docs/RETRACTED_PHRASES.md": _REGISTRY + "| 3 | `the third retracted phrase` | B3 | later |\n"})
    assert _gate(repo, "retraction-sweep", anchor) == (True, "ok")
    _commit(repo, "and quietly dropped", {"docs/RETRACTED_PHRASES.md": _REGISTRY})
    ok, detail = _gate(repo, "retraction-sweep", anchor)
    assert ok is False and "the third retracted phrase" in detail
