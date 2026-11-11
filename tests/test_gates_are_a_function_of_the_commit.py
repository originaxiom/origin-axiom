"""A gate is a function of the commit (the closure programme's WP-0.7, built by the advisor seat and verified by main).

The seat's planted case PV9: the gates were run on a `git archive` export, where there is no git, and nine of the ten that
need it passed.  Three answered "skipped" and returned a pass.  Six asked git for the tracked files, were given none, and
found nothing wrong among none ("ok (0 tests, 0 vacuous)", "ok (0 citations resolve)").

PV22: on a clone fifty commits deep, `lead-debt` read the history that was there and passed.  A gate that reads the past
is refused on a shallow clone, whatever its depth.

PV15: three gates were run at the commit's own date and sixty days later, and changed their answer.  Their checkers aged
the rows against the wall clock, and the variable that moves the date for a test moved it for the gate.  A gate's day is
the date of HEAD's commit, and nothing in the environment moves it.

Each test here makes the situation and runs the gate.  The first test of each case fails on the commit before it."""
import ast
import datetime
import importlib.util
import pathlib
import re
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

# the ten gates the planted case names: all ten need git
PV9 = ["append-only", "attribution", "tracked-forbidden", "log-changelog-paired", "views-fresh", "path-refs", "test-vacuity",
       "retraction-sweep", "review-fires", "harvest-debt"]


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_the_commit_rule", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _small_repo(tmp_path):
    repo = tmp_path / "repo"
    (repo / "sub").mkdir(parents=True)
    (repo / "sub" / "page.md").write_text("a page\n", encoding="utf-8")
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "one page")
    return repo


def test_on_an_export_the_ten_gates_that_need_git_do_not_pass(tmp_path, monkeypatch):
    """PV9.  No git is made here the way an export has none: every git call, the gates' own and their checkers', is sent to
    a repository that does not exist."""
    monkeypatch.setenv("GIT_DIR", str(tmp_path / "no_repository_here"))
    g = _gates()
    passing = sorted(name for name in PV9 if g.GATES[name]()[0])
    assert not passing, "with no git these gates still pass: %s" % ", ".join(passing)
    for name in sorted(g.READS_GIT):
        ok, detail = g.GATES[name]()
        assert ok is False and "refused" in detail and "no git repository" in detail, (name, detail)


def test_an_export_a_copy_and_a_folder_inside_another_repository_are_all_read_as_exports(tmp_path):
    g = _gates()
    repo = _small_repo(tmp_path)
    assert g.checkout_state(repo) == "full"
    # the push hook gates each commit in a detached worktree: that is a full checkout
    wt = tmp_path / "worktree"
    _git(repo, "worktree", "add", "-q", "--detach", str(wt), "HEAD")
    assert g.checkout_state(wt) == "full"
    # an export
    export = tmp_path / "export"
    export.mkdir()
    tar = subprocess.run(["git", "-C", str(repo), "archive", "HEAD"], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", str(export)], input=tar, check=True)
    assert g.checkout_state(export) == "export"
    # the same export unpacked INSIDE another repository: git would answer for the outer one
    inner = repo / "unpacked_here"
    inner.mkdir()
    subprocess.run(["tar", "-x", "-C", str(inner)], input=tar, check=True)
    assert g.checkout_state(inner) == "export"
    # a folder of the repository is not the repository
    assert g.checkout_state(repo / "sub") == "export"
    # a folder that does not exist
    assert g.checkout_state(tmp_path / "nothing_here") == "export"


def _exported(tmp_path, name):
    """a folder that holds an export of a small repository's files: the gates, their checkers and a page"""
    import shutil
    src = tmp_path / (name + "_source")
    skip = shutil.ignore_patterns("__pycache__", "*.pyc")
    shutil.copytree(ROOT / "scripts" / "gates", src / "scripts" / "gates", ignore=skip)
    shutil.copytree(ROOT / "scripts" / "checks", src / "scripts" / "checks", ignore=skip)
    (src / "README.md").write_text("# a page\n", encoding="utf-8")
    _git(src, "init", "-q")
    _git(src, "add", "-A")
    _git(src, "commit", "-q", "-m", "a small repository")
    out = tmp_path / name
    out.mkdir()
    tar = subprocess.run(["git", "-C", str(src), "archive", "HEAD"], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", str(out)], input=tar, check=True)
    return out


_RUN_THE_TABLE = ("import sys, json, importlib.util\n"
                  "sys.dont_write_bytecode = True\n"
                  "s = importlib.util.spec_from_file_location('scratch_gates', 'scripts/gates/gates.py')\n"
                  "g = importlib.util.module_from_spec(s); s.loader.exec_module(g)\n"
                  "out = {}\n"
                  "for name in sorted(g.READS_GIT):\n"
                  "    try:\n"
                  "        ok, detail = g.GATES[name]()\n"
                  "    except Exception as exc:\n"
                  "        ok, detail = False, 'raised: %r' % (exc,)\n"
                  "    out[name] = [bool(ok), str(detail)]\n"
                  "print(json.dumps([getattr(g, 'checkout_state')(), out]))\n")


def _the_table_there(folder):
    """every gate of the table READS_GIT, run by the folder's own copy of the gates: (what the folder is to git, the answers)"""
    import json
    r = subprocess.run([sys.executable, "-B", "-c", _RUN_THE_TABLE], cwd=str(folder), capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-800:]
    state, out = json.loads(r.stdout.strip().splitlines()[-1])
    return state, out


def test_a_repository_with_no_commit_is_not_a_full_clone_and_no_gate_of_the_table_passes_there(tmp_path):
    """Main's unseen case U9.b (B1890): an export's files in a folder made a repository with `git init`, and no commit.  It
    was read as a full clone, and nine gates of the table passed with nothing to look at.  Three forms of it."""
    forms = {}
    forms["git init and no commit"] = _exported(tmp_path, "initialised")
    _git(forms["git init and no commit"], "init", "-q")
    forms["the files added and not committed"] = _exported(tmp_path, "added")
    _git(forms["the files added and not committed"], "init", "-q")
    _git(forms["the files added and not committed"], "add", "-A")
    forms["a commit that holds no file, the files beside it"] = _exported(tmp_path, "empty_commit")
    _git(forms["a commit that holds no file, the files beside it"], "init", "-q")
    _git(forms["a commit that holds no file, the files beside it"], "commit", "-q", "--allow-empty", "-m", "nothing")
    for form, folder in forms.items():
        state, out = _the_table_there(folder)
        passing = sorted(name for name, (ok, detail) in out.items() if ok)
        assert not passing, f"{form}: read as {state!r}, and these gates of the table pass with nothing to look at: " + ", ".join(passing)
        assert state == "empty", (form, state)
        assert len(out) >= 20 and all("refused" in detail and "no commit" in detail for ok, detail in out.values()), (form, out)


def test_a_repository_whose_commit_does_not_hold_the_gates_is_not_a_full_clone_either(tmp_path):
    """The seat's own variant of U9.b: the repository holds one commit, with a note in it, and the export's files stand beside
    it untracked.  Git has something to say there, about something else, and eight gates of the table passed on the whole tree."""
    folder = _exported(tmp_path, "a_note_committed")
    _git(folder, "init", "-q")
    (folder / "A_NOTE_OF_ITS_OWN.txt").write_text("the only file this repository holds\n", encoding="utf-8")
    _git(folder, "add", "A_NOTE_OF_ITS_OWN.txt")
    _git(folder, "commit", "-q", "-m", "a note")
    state, out = _the_table_there(folder)
    passing = sorted(name for name, (ok, detail) in out.items() if ok)
    assert not passing, f"read as {state!r}, and these gates of the table pass on a tree the commit does not hold: " + ", ".join(passing)
    assert state == "untracked"
    assert all("refused" in detail and "does not hold the gates" in detail for ok, detail in out.values()), out


def test_a_repository_that_holds_a_commit_with_a_file_is_not_empty(tmp_path):
    """the other side: the smallest repository that has something to say is read as full, and its gates answer"""
    g = _gates()
    assert g.checkout_state(_small_repo(tmp_path)) == "full"
    folder = _exported(tmp_path, "committed")
    _git(folder, "init", "-q")
    _git(folder, "add", "-A")
    _git(folder, "commit", "-q", "-m", "the export, committed")
    state, out = _the_table_there(folder)
    assert state == "full"
    assert not any("no commit" in detail for ok, detail in out.values()), out


def test_a_shallow_clone_is_read_as_shallow_at_any_depth(tmp_path):
    """PV22, the reading.  A clone of depth 1, and one of a depth greater than the history it was cut from."""
    g = _gates()
    repo = _small_repo(tmp_path)
    for n in range(3):
        (repo / "sub" / "page.md").write_text("a page, edit %d\n" % n, encoding="utf-8")
        _git(repo, "commit", "-q", "-a", "-m", "edit %d" % n)
    one = tmp_path / "depth_one"
    subprocess.run(["git", "clone", "-q", "--depth", "1", "file://" + str(repo), str(one)], check=True, capture_output=True)
    assert g.checkout_state(one) == "shallow"
    three = tmp_path / "depth_three"
    subprocess.run(["git", "clone", "-q", "--depth", "3", "file://" + str(repo), str(three)], check=True, capture_output=True)
    assert g.checkout_state(three) == "shallow"
    whole = tmp_path / "whole"
    subprocess.run(["git", "clone", "-q", "file://" + str(repo), str(whole)], check=True, capture_output=True)
    assert g.checkout_state(whole) == "full"
    # a depth that reaches the first commit cuts nothing, and git does not call such a clone shallow
    deep = tmp_path / "deeper_than_the_history"
    subprocess.run(["git", "clone", "-q", "--depth", "50", "file://" + str(repo), str(deep)], check=True, capture_output=True)
    assert g.checkout_state(deep) == "full"


def test_on_a_shallow_clone_every_gate_that_reads_the_past_is_refused_and_says_why(monkeypatch):
    """PV22, the refusal.  The planted case ran `lead-debt` on a clone fifty commits deep and it passed."""
    g = _gates()
    monkeypatch.setattr(g, "checkout_state", lambda repo=None: "shallow", raising=False)
    ok, detail = g.GATES["lead-debt"]()
    assert ok is False and "shallow" in detail.lower(), ("lead-debt", ok, detail)
    for name in sorted(g.READS_HISTORY):
        ok, detail = g.GATES[name]()
        assert ok is False and "refused" in detail and "shallow" in detail, (name, detail)
    # a gate that asks only which files are tracked has all it needs on a shallow clone, and is not refused
    for name in sorted(g.READS_TRACKED):
        assert "refused" not in str(g.GATES[name]()[1]), name


DATED = {"lead-debt": "OA_LEAD_TODAY", "point-debt": "OA_POINT_TODAY", "relay-debt": "OA_RELAY_TODAY", "harvest-debt": "OA_HARVEST_TODAY"}


def test_a_debt_gate_answers_the_same_whatever_day_the_environment_names(monkeypatch):
    """PV15.  The planted case set the day through the checkers' own seam, to the commit's date and to sixty days on."""
    g = _gates()
    head = datetime.date.fromisoformat(_git(ROOT, "log", "-1", "--format=%cs", "HEAD"))
    answers = {}
    for days in (0, 60, 600):
        for env in DATED.values():
            monkeypatch.setenv(env, (head + datetime.timedelta(days=days)).isoformat())
        answers[days] = {name: tuple(map(str, g.GATES[name]())) for name in DATED}
    changed = sorted(name for name in DATED if len({answers[d][name] for d in answers}) > 1)
    assert not changed, "these gates change their answer with the day the environment names: %s" % ", ".join(changed)


def test_no_gate_and_no_checker_reads_the_wall_clock():
    """A duration may be timed.  A date may not be taken from the clock."""
    clock = re.compile(r"\bdate\.today\(|\bdatetime\.now\(|\butcnow\(|\btime\.(?:localtime|gmtime|strftime|ctime|asctime)\(")
    found = []
    for p in sorted((ROOT / "scripts" / "gates").glob("*.py")) + sorted((ROOT / "scripts" / "checks").glob("*.py")):
        for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if clock.search(line.split("#", 1)[0]):
                found.append("%s:%d" % (p.relative_to(ROOT), n))
    assert not found, "the wall clock is read at: %s" % ", ".join(found)


def test_the_day_is_decided_in_one_place_and_in_one_order(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("commit_day_for_the_commit_rule", ROOT / "scripts" / "checks" / "commit_day.py")
    cd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cd)
    repo = _small_repo(tmp_path)
    head = datetime.date.fromisoformat(_git(repo, "log", "-1", "--format=%cs", "HEAD"))
    monkeypatch.delenv("OA_X_TODAY", raising=False)
    assert cd.today("OA_X_TODAY", argv=[], root=repo) == head                                   # 3. the commit's own date
    monkeypatch.setenv("OA_X_TODAY", "2031-05-06")
    assert cd.today("OA_X_TODAY", argv=[], root=repo) == datetime.date(2031, 5, 6)               # 2. the seam, with no --today
    assert cd.today("OA_X_TODAY", argv=["--today", "2029-01-02"], root=repo) == datetime.date(2029, 1, 2)   # 1. beats the seam
    assert cd.today("OA_X_TODAY", argv=["--list", "--today=2029-01-03"], root=repo) == datetime.date(2029, 1, 3)
    # with nothing given and no commit to read, a refusal and not the clock
    monkeypatch.delenv("OA_X_TODAY")
    with pytest.raises(SystemExit) as e:
        cd.today("OA_X_TODAY", argv=[], root=tmp_path / "no_repository_here")
    assert "refused" in str(e.value)
    # a day that is not a day is refused in plain words, from the command line and from the seam alike
    for argv, seam in ((["--today", "tomorrow"], None), (["--today=11/11/2026"], None), ([], "next week")):
        if seam:
            monkeypatch.setenv("OA_X_TODAY", seam)
        with pytest.raises(SystemExit) as e:
            cd.today("OA_X_TODAY", argv=argv, root=repo)
        assert "refused" in str(e.value) and "not a day" in str(e.value), (argv, seam)
    monkeypatch.delenv("OA_X_TODAY")
    # and each gate does pass the commit's day on the command line
    g = _gates()
    assert g._today_args() == ["--today", _git(ROOT, "log", "-1", "--format=%cs", "HEAD")]
    src = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    for checker in ("relay_debt.py", "harvest_debt.py", "lead_debt.py", "point_debt.py"):
        calls = [c for c in re.findall(r'[^\n]*"%s"[^\n]*' % re.escape(checker), src) if "subprocess.run" in c or "_debt_checker" in c]
        assert calls and all("_today_args()" in c or "_debt_checker(" in c for c in calls), (checker, calls)


def _commit_dated(repo, when, text):
    """one more commit on `repo`, its committer date set to `when` (seconds since the epoch)"""
    (repo / "sub" / "page.md").write_text(text, encoding="utf-8")
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-q", "-a", "-m", text.strip()],
                       capture_output=True, text=True, env={**__import__("os").environ, "GIT_COMMITTER_DATE": "%d +0000" % when, "GIT_AUTHOR_DATE": "%d +0000" % when})
    assert r.returncode == 0, r.stderr
    return _git(repo, "rev-parse", "HEAD")


def test_a_commit_dated_before_its_parent_is_refused_as_a_day(tmp_path):
    """The seat's own variant of PV15.  With the day taken from the commit, a commit dated a month back makes every debt a
    month younger.  After the rule's first commit, time may not run backwards on the first-parent line."""
    g = _gates()
    repo = _small_repo(tmp_path)
    t0 = int(_git(repo, "log", "-1", "--format=%ct", "HEAD"))
    root = _git(repo, "rev-parse", "HEAD")
    a = _commit_dated(repo, t0 + 3600, "an hour on\n")
    assert g.commit_day_problems(repo, root) == []
    same = _commit_dated(repo, t0 + 3600, "the same second\n")                # not before its parent
    assert g.commit_day_problems(repo, root) == []
    back = _commit_dated(repo, t0 + 3600 - 30 * 86400, "a month back\n")
    bad = g.commit_day_problems(repo, root)
    assert len(bad) == 1 and back[:9] in bad[0] and "before its parent" in bad[0], bad
    # a later commit dated rightly does not hide it: the rule reads every commit after its root, not the tip alone
    _commit_dated(repo, t0 + 7200, "two hours on\n")
    assert any(back[:9] in b for b in g.commit_day_problems(repo, root))
    # and it fails closed where it cannot read back to its root
    assert "cannot verify" in g.commit_day_problems(repo, "0" * 40)[0]
    shallow = tmp_path / "shallow"
    subprocess.run(["git", "clone", "-q", "--depth", "1", "file://" + str(repo), str(shallow)], check=True, capture_output=True)
    assert "cannot verify" in g.commit_day_problems(shallow, root)[0]
    assert a


def test_the_debt_gates_do_not_answer_on_a_day_that_cannot_be_trusted(monkeypatch):
    g = _gates()
    # the rule's first commit is moved only by a recorded act: whoever moves it changes this line too, and says why
    assert g.COMMIT_DAY_FROM == "ea41e6fc96012acfe5ec91478eadd7c5cfe95cbe"
    assert g.commit_day_problems() == [], "on this clone time has not run backwards since the rule's first commit"
    monkeypatch.setattr(g, "commit_day_problems", lambda *a, **k: ["abc123def is dated 2026-10-01, before its parent"], raising=False)
    for name in DATED:
        ok, detail = g.GATES[name]()
        assert ok is False and "before its parent" in str(detail), (name, ok, detail)


def test_in_a_clone_no_gate_is_refused():
    g = _gates()
    assert g.checkout_state() == "full", "this lock is run in a clone"
    assert g.GATES["tracked-forbidden"]()[0] is True


def test_a_gate_is_one_thing_in_the_table_and_under_its_own_name():
    """Main's rule R60-4: a test names the gate it controls (`GATES["path-refs"] is gate_path_refs`).  The refusal does not make
    two things of one gate.  Every gate is the same object in GATES and under its own name, so a gate called by its name is
    refused as well; and the gates of the table, and only those, were replaced."""
    g = _gates()
    for name, fn in g.GATES.items():
        assert getattr(g, fn.__name__) is fn, name
        assert hasattr(fn, "__wrapped__") == (name in g.READS_GIT), name
    assert len({fn.__name__ for fn in g.GATES.values()}) == len(g.GATES)


def test_a_test_may_still_drive_a_gate_on_a_tree_of_its_own(tmp_path, monkeypatch):
    """Called with arguments, a gate of the table is the gate itself: it is not asked where it runs."""
    g = _gates()
    monkeypatch.setenv("GIT_DIR", str(tmp_path / "no_repository_here"))
    calls = []
    gate = g._refusing("tracked-forbidden", lambda *a, **k: calls.append((a, k)) or (True, "driven"))
    ok, detail = gate()
    assert ok is False and "refused" in detail and not calls
    assert gate("a tree of its own") == (True, "driven") and calls == [(("a tree of its own",), {})]


# ---- the table is held to the code ------------------------------------------------------------------------------------------
def test_a_gate_that_is_not_in_the_table_answers_the_same_with_git_as_without(tmp_path, monkeypatch):
    """The table READS_GIT says which gates need git.  Every other gate is run twice here, in the clone and with git taken
    away, and must say the same thing word for word.  A gate that calls git, by itself or through any script it runs, and is
    not in the table, answers differently and fails this."""
    g = _gates()
    others = sorted(set(g.GATES) - g.READS_GIT)
    assert len(others) >= 30
    with_git = {name: g.GATES[name]() for name in others}
    monkeypatch.setenv("GIT_DIR", str(tmp_path / "no_repository_here"))
    g2 = _gates()
    differ = [name for name in others if tuple(map(str, g2.GATES[name]())) != tuple(map(str, with_git[name]))]
    assert not differ, "these gates answer differently without git and are not in READS_GIT: %s" % ", ".join(differ)


_SUB = re.compile(r'''(?:_git|git)\(\s*["']([a-z-]+)["']|\[\s*["']git["']\s*,(?:\s*["']-C["']\s*,[^,\]]+,)?\s*["']([a-z-]+)["']''')
_PAST = {"log", "rev-list", "diff-tree", "merge-base", "cat-file", "show", "ls-tree", "for-each-ref", "diff", "fetch",
         "ls-remote", "tag", "describe", "blame", "reflog"}


def _used_part(path, names):
    """the source of the functions `names` of the script at `path`, of the functions of that script they call, and of the
    script's own top-level statements (which run when it is loaded)"""
    src = path.read_text(encoding="utf-8", errors="replace")
    tree = ast.parse(src)
    funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    top = [ast.get_source_segment(src, n) or "" for n in tree.body if not isinstance(n, (ast.FunctionDef, ast.ClassDef))]
    seen, todo = set(), [n for n in names if n in funcs]
    while todo:
        name = todo.pop()
        if name in seen:
            continue
        seen.add(name)
        todo += [n.func.id for n in ast.walk(funcs[name]) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in funcs]
    return "\n".join(top + [ast.get_source_segment(src, funcs[n]) for n in sorted(seen)])


def _git_subcommands(gate_function_name):
    """the git subcommands in a gate's own code, in the functions of gates.py it calls, and in what it uses of the scripts under
    scripts/ that it names.  A script that is run is read whole.  A script imported as a module is read in the functions the
    gate calls on it, with what those call."""
    path = ROOT / "scripts" / "gates" / "gates.py"
    src = path.read_text(encoding="utf-8")
    funcs = {n.name: n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef)}
    scripts = {}
    for p in (ROOT / "scripts").rglob("*.py"):
        if p != path:
            scripts.setdefault(p.name, []).append(p)

    def reach(name, seen):
        if name in seen or name not in funcs:
            return seen
        seen.add(name)
        for n in ast.walk(funcs[name]):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
                reach(n.func.id, seen)
        return seen

    text = "\n".join(ast.get_source_segment(src, funcs[f]) for f in sorted(reach(gate_function_name, set())))
    as_module = {}
    for module, alias in re.findall(r"\bimport (\w+)(?: as (\w+))?", text):
        if module + ".py" in scripts:
            as_module.setdefault(module + ".py", set()).update(re.findall(r"\b%s\.(\w+)\(" % (alias or module), text))
    for script in sorted(set(re.findall(r'["\']([\w.-]+\.py)["\']', text)) - set(as_module)):
        for p in scripts.get(script, []):
            text += "\n" + p.read_text(encoding="utf-8", errors="replace")
    for script, names in sorted(as_module.items()):
        for p in scripts.get(script, []):
            text += "\n" + _used_part(p, names)
    # the date of HEAD's commit is the commit itself, not the past: that one call is set aside before the commands are read
    text = re.sub(r'"log",\s*"-1",\s*"--format=%cs",\s*"HEAD"', '"head-date"', text)
    return {a or b for a, b in _SUB.findall(text)}


def test_a_gate_listed_as_reading_the_tracked_files_only_reads_nothing_of_the_past():
    g = _gates()
    assert not (g.READS_TRACKED & g.READS_HISTORY)
    assert g.READS_GIT <= set(g.GATES), "the table names a gate that is not there: %s" % sorted(g.READS_GIT - set(g.GATES))
    seen_any = 0
    for name in sorted(g.READS_TRACKED):
        used = _git_subcommands(g.GATES[name].__wrapped__.__name__)
        seen_any += bool(used)
        assert not (used & _PAST), "%s is listed as reading the tracked files only and calls git %s" % (name, sorted(used & _PAST))
    assert seen_any == len(g.READS_TRACKED), "the source scan no longer sees the git calls of the gates it is meant to read"
    # and the scan does see the past where it is read: three gates of READS_HISTORY, by their own code
    for name in ("append-only", "lead-debt", "views-fresh"):
        assert _git_subcommands(g.GATES[name].__wrapped__.__name__) & _PAST, name
    # the four debt gates read the date of HEAD's commit, and the scan sees that they do
    for name in DATED:
        assert "head-date" in _git_subcommands(g.GATES[name].__wrapped__.__name__), name
