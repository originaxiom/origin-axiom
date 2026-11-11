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


# ---- PV13: the law map and the theorem ledger ---------------------------------------------------------------------------
_LAWS = ("# The law map\n\n| law | statement | status | source | tension |\n|---|---|---|---|---|\n"
         "| **The first law (B11)** | a statement | PROVED | B11 | - |\n"
         "| **The second law (B12)** | another | PROVED | B12 | - |\n"
         "| **The third law (B13)** | a third | PROVED | B13 | - |\n")
_CHAIN = ("# THE CHAIN\n\n**C1 [THEOREM].** A first link. Lock: `tests/test_a.py`.\n\n"
          "**C2 [THEOREM].** A second link. Lock: `tests/test_a.py`.\n\n**C3 [AXIOM].** A declared choice.\n")
_PAGES = {"docs/LAW_MAP.md": _LAWS, "docs/THEOREM_LEDGER.md": _CHAIN, "tests/test_a.py": "def test_a():\n    assert 1 + 1 == 2\n"}


def test_the_law_map_and_the_theorem_ledger_emptied_turn_their_gates_red(tmp_path):
    """PV13 as planted.  Each gate checked every row it found, and with no rows nothing could fail."""
    repo, anchor = _scratch(tmp_path, _PAGES)
    ok, detail = _gate(repo, "law-map-provenance", anchor)
    assert ok is True and "3 rows all traceable" in detail and "by name" not in detail
    ok, detail = _gate(repo, "chain-locks", anchor)
    assert ok is True and "3 links" in detail and "by name" not in detail
    _commit(repo, "both pages emptied", {"docs/LAW_MAP.md": "# The law map\n", "docs/THEOREM_LEDGER.md": "# THE CHAIN\n"})
    ok, detail = _gate(repo, "law-map-provenance", anchor)
    assert ok is False and "3 law(s) left docs/LAW_MAP.md" in detail and "The first law (B11)" in detail
    ok, detail = _gate(repo, "chain-locks", anchor)
    assert ok is False and "3 link(s) left docs/THEOREM_LEDGER.md" in detail and "C1" in detail


def test_one_law_or_one_link_removed_turns_its_gate_red_unless_it_is_named(tmp_path):
    repo, anchor = _scratch(tmp_path, _PAGES)
    fewer_laws = "\n".join(l for l in _LAWS.split("\n") if "second law" not in l)
    fewer_links = _CHAIN.replace("**C2 [THEOREM].** A second link. Lock: `tests/test_a.py`.\n\n", "")
    _commit(repo, "one row and one link removed", {"docs/LAW_MAP.md": fewer_laws, "docs/THEOREM_LEDGER.md": fewer_links})
    ok, detail = _gate(repo, "law-map-provenance", anchor)
    assert ok is False and "1 law(s) left" in detail and "The second law (B12)" in detail
    ok, detail = _gate(repo, "chain-locks", anchor)
    assert ok is False and "1 link(s) left" in detail and "C2" in detail
    _name_in_the_gate(repo, "docs/LAW_MAP.md", "The second law (B12)", "2026-11-11 -- merged into the first law's row")
    _commit(repo, "the law's leaving is recorded")
    ok, detail = _gate(repo, "law-map-provenance", anchor)
    assert ok is True and "1 law(s) left by name" in detail and "merged into the first law" in detail
    assert _gate(repo, "chain-locks", anchor)[0] is False                    # the link was not named, and is still missed


def test_a_law_keeps_its_place_when_its_row_is_added_to_and_loses_it_when_its_title_changes(tmp_path):
    """A note may grow after the title, and the rest of the row may be corrected: the law is still there.  A changed title is
    a law that left and one that came, and that is a recorded act."""
    repo, anchor = _scratch(tmp_path, _PAGES)
    grown = _LAWS.replace("| **The first law (B11)** | a statement |", "| **The first law (B11)** [scope: a note added later] | a statement, corrected (B14) |")
    _commit(repo, "a note and a correction", {"docs/LAW_MAP.md": grown})
    assert _gate(repo, "law-map-provenance", anchor)[0] is True
    _commit(repo, "a title is changed", {"docs/LAW_MAP.md": grown.replace("**The third law (B13)**", "**The third law, for the median only (B13)**")})
    ok, detail = _gate(repo, "law-map-provenance", anchor)
    assert ok is False and "The third law (B13)" in detail


def test_on_main_the_two_pages_hold_everything_they_held_at_the_anchor():
    g = _gates()
    for path, keys in ((g.LAW_MAP, g._law_titles), (g.CHAIN, g._chain_links)):
        text = (ROOT / path).read_text(encoding="utf-8")
        assert len(keys(text)) == len(set(keys(text))) > 50, path                      # each row and each link has a name of its own
        assert g.left_the_ledger(path, keys, text) == (None, ""), path


# ---- PV10: the identification register and its baseline -----------------------------------------------------------------
_IDENT_HEAD = "# The identification ledger\n\n| id | what | a | b | map | acts | state | arc | note |\n|---|---|---|---|---|---|---|---|---|\n"
_IDENT = _IDENT_HEAD + "| I-1 | one | A | B | x | y | **EARNED** | B11 | - |\n| I-2 | two | A | B | x | y | **UNEARNED** | B12 | - |\n"
_UNEARNED = "| I-%d | planted | A | B | x | y | **UNEARNED** | B13 | - |\n"


def _baseline(unearned, raises=()):
    return json.dumps({"_note": "the ratchet", "unearned": unearned, "_baseline_raises": list(raises)}, indent=1) + "\n"


_REGISTER = {"docs/IDENTIFICATION_LEDGER.md": _IDENT, "docs/IDENTIFICATION_BASELINE.json": _baseline(1)}


def test_the_identification_baseline_deleted_and_three_unearned_rows_added_turns_the_gate_red(tmp_path):
    """PV10 as planted.  The ratchet ran only if its baseline was there."""
    repo, anchor = _scratch(tmp_path, _REGISTER)
    assert _gate(repo, "identification-register", anchor) == (True, "ok")
    _commit(repo, "the baseline deleted, three unearned rows added", {"docs/IDENTIFICATION_LEDGER.md": _IDENT + "".join(_UNEARNED % n for n in (3, 4, 5))},
            delete=["docs/IDENTIFICATION_BASELINE.json"])
    ok, detail = _gate(repo, "identification-register", anchor)
    assert ok is False and "IDENTIFICATION_BASELINE.json missing or unreadable" in detail


def test_the_baseline_rises_only_by_a_raise_recorded_in_its_own_list(tmp_path):
    repo, anchor = _scratch(tmp_path, _REGISTER)
    three_more = {"docs/IDENTIFICATION_LEDGER.md": _IDENT + "".join(_UNEARNED % n for n in (3, 4, 5))}
    # raised in the commit that adds the rows, with no record: the count agrees with the baseline, and the baseline rose
    _commit(repo, "three rows, and the baseline moved to fit them", dict(three_more, **{"docs/IDENTIFICATION_BASELINE.json": _baseline(4)}))
    ok, detail = _gate(repo, "identification-register", anchor)
    assert ok is False and "the baseline rose 1 -> 4" in detail and "account for 0" in detail
    # a record that does not say why is not a record
    _commit(repo, "a raise with no reason", {"docs/IDENTIFICATION_BASELINE.json": _baseline(4, [{"date": "2026-11-11", "from": 1, "to": 4, "reason": " "}])})
    ok, detail = _gate(repo, "identification-register", anchor)
    assert ok is False and "no date, no reason" in detail
    # the recorded act: the raise in the file's own list, dated, with its reason.  The gate passes and says so
    raise_ = {"date": "2026-11-11", "from": 1, "to": 4, "row": "I-3, I-4, I-5", "reason": "three identifications registered unearned, each with what would earn it"}
    _commit(repo, "the raise recorded", {"docs/IDENTIFICATION_BASELINE.json": _baseline(4, [raise_])})
    ok, detail = _gate(repo, "identification-register", anchor)
    assert ok is True and "raised 1 time(s) by name" in detail and "1 -> 4 (2026-11-11)" in detail
    # a recorded raise does not leave the list afterwards
    _commit(repo, "the record of the raise removed", {"docs/IDENTIFICATION_BASELINE.json": _baseline(4)})
    ok, detail = _gate(repo, "identification-register", anchor)
    assert ok is False and "the baseline rose 1 -> 4" in detail


def test_the_baseline_may_fall_freely_and_must_hold_a_count(tmp_path):
    repo, anchor = _scratch(tmp_path, _REGISTER)
    earned = _IDENT.replace("| I-2 | two | A | B | x | y | **UNEARNED**", "| I-2 | two | A | B | x | y | **EARNED**")
    _commit(repo, "the unearned row is earned and the baseline lowered", {"docs/IDENTIFICATION_LEDGER.md": earned, "docs/IDENTIFICATION_BASELINE.json": _baseline(0)})
    assert _gate(repo, "identification-register", anchor) == (True, "ok")
    for broken in ('{"unearned": "many"}', '{"unearned": null}', "{}", "not json at all", '{"unearned": true}'):
        _commit(repo, "the baseline no longer holds a count", {"docs/IDENTIFICATION_BASELINE.json": broken + "\n"})
        ok, detail = _gate(repo, "identification-register", anchor)
        assert ok is False and "the ratchet cannot be read" in detail, broken


def test_a_row_that_leaves_the_identification_ledger_turns_the_gate_red_unless_it_is_named(tmp_path):
    repo, anchor = _scratch(tmp_path, _REGISTER)
    _commit(repo, "the unearned row is deleted, which also lowers the count", {"docs/IDENTIFICATION_LEDGER.md": _IDENT_HEAD + "| I-1 | one | A | B | x | y | **EARNED** | B11 | - |\n"})
    ok, detail = _gate(repo, "identification-register", anchor)
    assert ok is False and "1 identification(s) left docs/IDENTIFICATION_LEDGER.md" in detail and "I-2" in detail
    _name_in_the_gate(repo, "docs/IDENTIFICATION_LEDGER.md", "I-2", "2026-11-11 -- a duplicate of I-1, merged into it")
    _commit(repo, "its leaving recorded")
    ok, detail = _gate(repo, "identification-register", anchor)
    assert ok is True and "1 identification(s) left by name" in detail


def test_the_rule_of_the_raises_on_its_own():
    g = _gates()
    then = {"unearned": 5, "_baseline_raises": [{"date": "d", "from": 4, "to": 5, "reason": "r"}]}
    grow = lambda b, more: {"unearned": b, "_baseline_raises": then["_baseline_raises"] + more}
    r = lambda a, b: {"date": "2026-11-12", "from": a, "to": b, "reason": "why"}
    assert g.baseline_rise(grow(5, []), then) == (None, "")
    assert g.baseline_rise(grow(3, []), then) == (None, "")                              # it may fall with no record
    assert "rose 5 -> 6" in g.baseline_rise(grow(6, []), then)[0]
    assert g.baseline_rise(grow(6, [r(5, 6)]), then)[0] is None
    assert "rose 5 -> 8" in g.baseline_rise(grow(8, [r(5, 6)]), then)[0]                 # one raise recorded, three taken
    assert g.baseline_rise(grow(8, [r(5, 6), r(6, 8)]), then)[0] is None
    assert "removed or changed" in g.baseline_rise({"unearned": 5, "_baseline_raises": []}, then)[0]
    assert "does not go up" in g.baseline_rise(grow(5, [r(6, 5)]), then)[0]
    assert g.baseline_rise(grow(99, []), None) == (None, "")                             # no baseline at the anchor: not re-judged


# ---- PV12: the locks themselves -----------------------------------------------------------------------------------------
_LOCK = "def test_%s():\n    assert sum([1, 2]) == 3\n"
_LOCKS = {"tests/test_one.py": _LOCK % "one", "tests/test_two.py": _LOCK % "two", "frontier/B11_an_arc/verification/test_b11_an_arc.py": _LOCK % "three"}


def test_every_lock_deleted_turns_the_vacuity_gate_red(tmp_path):
    """PV12 as planted.  The gate counted the tests that cannot fail among the tests present; among none it counted none."""
    repo, anchor = _scratch(tmp_path, _LOCKS)
    ok, detail = _gate(repo, "test-vacuity", anchor)
    assert ok is True and "2 tests, 0 vacuous" in detail and "by name" not in detail
    _commit(repo, "every lock in tests/ deleted", delete=["tests/test_one.py", "tests/test_two.py"])
    ok, detail = _gate(repo, "test-vacuity", anchor)
    assert ok is False and "2 lock file(s) left the repository" in detail and "tests/test_one.py" in detail


def test_one_lock_deleted_turns_the_gate_red_unless_its_retirement_is_recorded(tmp_path):
    repo, anchor = _scratch(tmp_path, _LOCKS)
    _commit(repo, "an arc's own lock deleted", delete=["frontier/B11_an_arc/verification/test_b11_an_arc.py"])
    ok, detail = _gate(repo, "test-vacuity", anchor)
    assert ok is False and "1 lock file(s) left" in detail and "test_b11_an_arc.py" in detail
    _name_in_the_gate(repo, "locks", "frontier/B11_an_arc/verification/test_b11_an_arc.py", "2026-11-11 -- the arc is retracted (B12); its lock retired with it")
    _commit(repo, "the retirement recorded")
    ok, detail = _gate(repo, "test-vacuity", anchor)
    assert ok is True and "1 lock file(s) left by name" in detail and "retired with it" in detail


def test_a_lock_that_is_moved_has_not_left_and_one_added_and_dropped_has(tmp_path):
    repo, anchor = _scratch(tmp_path, _LOCKS)
    _git(repo, "mv", "tests/test_one.py", "tests/test_one_renamed.py")
    _commit(repo, "a lock renamed")
    assert _gate(repo, "test-vacuity", anchor)[0] is True
    _git(repo, "mv", "tests/test_one_renamed.py", "tests/test_one_again.py")
    _commit(repo, "and renamed again")
    assert _gate(repo, "test-vacuity", anchor)[0] is True
    _commit(repo, "a lock added after the anchor", {"tests/test_late.py": _LOCK % "late"})
    _commit(repo, "and dropped", delete=["tests/test_late.py"])
    ok, detail = _gate(repo, "test-vacuity", anchor)
    assert ok is False and "tests/test_late.py" in detail and "test_one" not in detail


def test_a_lock_gone_from_the_disk_or_from_the_index_has_left_before_any_commit_says_so(tmp_path):
    repo, anchor = _scratch(tmp_path, _LOCKS)
    (repo / "tests" / "test_two.py").unlink()                                   # deleted, not committed
    ok, detail = _gate(repo, "test-vacuity", anchor)
    assert ok is False and "tests/test_two.py" in detail
    _git(repo, "checkout", "--", "tests/test_two.py")
    assert _gate(repo, "test-vacuity", anchor)[0] is True
    _git(repo, "rm", "-q", "--cached", "tests/test_two.py")                     # on the disk still, and no longer tracked
    ok, detail = _gate(repo, "test-vacuity", anchor)
    assert ok is False and "tests/test_two.py" in detail


def test_on_main_no_lock_has_left_since_the_anchor():
    g = _gates()
    assert g.locks_that_left() == (None, "")
