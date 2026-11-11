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
        calls = re.findall(r'"%s"[^\n]*' % re.escape(checker), src)
        assert calls and all("_today_args()" in c for c in calls), (checker, calls)


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
