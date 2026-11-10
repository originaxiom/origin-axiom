"""The append-only gate reads history (G1 of the advisor seat's audit, 2026-11-10; its planted violations PV1 and PV2).

Before, the gate compared the working file with the same file at HEAD. A deletion that was committed passed, and at the
push hook's clean checkout the gate could not fail at all. Each test here builds a small repository of its own, COMMITS
the violation, and runs the gate on the clean tree at that commit."""
import importlib.util
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOG = "PROGRESS_LOG.md"
V1 = "# Progress log\n\n## 2026-01-01 -- A\n\nfirst entry\nsecond line\nthird line\n"
V2 = V1 + "\n## 2026-01-02 -- B\n\nmore\n"


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_append_only", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _repo(tmp_path, name="r", first=V1):
    repo = tmp_path / name
    repo.mkdir()
    _git(repo, "init", "-q", "-b", "main")
    (repo / LOG).write_text(first, encoding="utf-8")
    _git(repo, "add", LOG)
    _git(repo, "commit", "-q", "-m", "root of " + name)        # the name keeps two repositories' roots distinct
    return repo, _git(repo, "rev-parse", "HEAD")


def _commit(repo, text, msg, extra=None):
    (repo / LOG).write_text(text, encoding="utf-8")
    for rel, body in (extra or {}).items():
        f = repo / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(body, encoding="utf-8")
        _git(repo, "add", rel)
    _git(repo, "add", LOG)
    _git(repo, "commit", "-q", "-m", msg)
    return _git(repo, "rev-parse", "HEAD")


def test_an_append_passes(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _commit(repo, V2, "append")
    problems, n = g.append_only_problems(repo, root)
    assert problems == [] and n == 1


def test_pv1_a_committed_deletion_is_refused(tmp_path):
    """delete lines from the middle of the log and commit: the working tree is clean, and the gate fails"""
    g = _gates()
    repo, root = _repo(tmp_path)
    _commit(repo, V2, "append")
    lines = V2.split("\n")
    bad = _commit(repo, "\n".join(lines[:4] + lines[6:]), "delete two lines")
    assert _git(repo, "status", "--porcelain") == ""
    problems, n = g.append_only_problems(repo, root)
    assert len(problems) == 1 and bad[:9] in problems[0] and "changes or removes earlier text" in problems[0]


def test_pv2_the_log_replaced_by_one_line_is_refused(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    bad = _commit(repo, "one line\n", "replace")
    problems, _ = g.append_only_problems(repo, root)
    assert len(problems) == 1 and bad[:9] in problems[0]


def test_a_violation_stays_in_history_until_it_is_waived_by_name(tmp_path):
    """restoring the text in a later commit does not erase the step: it is refused until the owner waives that commit"""
    g = _gates()
    repo, root = _repo(tmp_path)
    bad = _commit(repo, "one line\n", "replace")
    _commit(repo, V2, "restore and append")
    problems, _ = g.append_only_problems(repo, root)
    assert any(bad[:9] in p for p in problems)
    # the restoring commit is itself a change of earlier text relative to its parent, so it is named too
    assert len(problems) == 2
    waived = {c: "planted" for c in _git(repo, "log", "--format=%H", root + "..HEAD").split()}
    assert g.append_only_problems(repo, root, waived)[0] == []


def test_a_roll_up_passes_only_with_its_archive(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _commit(repo, V2, "append")
    moved = V2[V2.index("## 2026-01-01"):V2.index("## 2026-01-02")]
    kept = "# Progress log\n\n" + V2[V2.index("## 2026-01-02"):]
    _commit(repo, kept, "roll-up with archive", extra={"docs/progress/ARCHIVE_2026Q1.md": "# archive\n\n" + moved})
    assert g.append_only_problems(repo, root)[0] == []
    repo2, root2 = _repo(tmp_path, "r2")
    _commit(repo2, V2, "append")
    bad = _commit(repo2, kept, "roll-up with no archive")
    problems, _ = g.append_only_problems(repo2, root2)
    assert len(problems) == 1 and bad[:9] in problems[0] and "archived verbatim: False" in problems[0]


def test_it_fails_closed_where_history_cannot_be_read(tmp_path):
    """PV9 and PV22: no repository, or a shallow clone that does not hold the rule's first commit, is not 'ok'"""
    g = _gates()
    repo, root = _repo(tmp_path)
    _commit(repo, V2, "append")
    _commit(repo, V2 + "\n## 2026-01-03 -- C\n", "append again")
    shallow = tmp_path / "shallow"
    subprocess.run(["git", "clone", "-q", "--depth", "1", "file://" + str(repo), str(shallow)], check=True, capture_output=True)
    problems, _ = g.append_only_problems(shallow, root)
    assert problems and "cannot verify" in problems[0] and "shallow" in problems[0]
    plain = tmp_path / "export"
    plain.mkdir()
    (plain / LOG).write_text(V2, encoding="utf-8")
    problems, _ = g.append_only_problems(plain, root)
    assert problems and "cannot verify" in problems[0]
    # a history that does not descend from the rule's first commit
    other, other_root = _repo(tmp_path, "other", first="# another log\n")
    assert other_root != root
    _git(repo, "fetch", "-q", str(other), "main:other")
    _git(repo, "checkout", "-q", "other")
    problems, _ = g.append_only_problems(repo, root)
    assert problems and "does not descend" in problems[0]


def test_the_gate_itself_fails_on_a_committed_deletion(tmp_path, monkeypatch):
    """the registered control: the gate function, pointed at a repository whose history holds the violation"""
    g = _gates()
    repo, root = _repo(tmp_path)
    _commit(repo, V2, "append")
    monkeypatch.setattr(g, "ROOT", str(repo))
    monkeypatch.setattr(g, "APPEND_ONLY_FROM", root)
    ok, why = g.gate_append_only()
    assert ok, why
    _commit(repo, "one line\n", "replace")
    ok, why = g.gate_append_only()
    assert ok is False and "changes or removes earlier text" in why


def test_the_gate_is_green_on_this_repository():
    g = _gates()
    ok, why = g.gate_append_only()
    assert ok, why
    assert len(g.APPEND_ONLY_FROM) == 40 and g.APPEND_ONLY_WAIVED == {}


def test_without_a_repository_no_gate_prints_a_bare_ok(tmp_path):
    """PV9, in part: on an export with no repository the append-only gate FAILS, and a gate that checks nothing there is
    printed SKIP with its own words. Before, the runner printed 'ok' for every pass and hid the word 'skipped'."""
    import shutil
    import sys
    exp = tmp_path / "export"
    (exp / "scripts").mkdir(parents=True)
    shutil.copytree(ROOT / "scripts" / "gates", exp / "scripts" / "gates")
    shutil.copytree(ROOT / "scripts" / "checks", exp / "scripts" / "checks")
    shutil.copy(ROOT / "PROGRESS_LOG.md", exp / "PROGRESS_LOG.md")
    out = subprocess.run([sys.executable, str(exp / "scripts" / "gates" / "gates.py")], capture_output=True, text=True, cwd=str(exp), timeout=600).stdout
    lines = {l.split(":")[0].strip(): l for l in out.splitlines() if l.strip().startswith(("PASS", "FAIL", "SKIP"))}
    assert lines["FAIL  append-only"].strip().startswith("FAIL  append-only: cannot verify")
    for gate in ("attribution", "tracked-forbidden", "log-changelog-paired"):
        hit = [l for k, l in lines.items() if k.endswith("  " + gate)]
        assert len(hit) == 1 and hit[0].strip().startswith("SKIP") and "skipped" in hit[0], (gate, hit)
    assert not any(l.strip() == "PASS  %s: ok" % g for l in out.splitlines() for g in ("attribution", "tracked-forbidden", "log-changelog-paired", "append-only"))
