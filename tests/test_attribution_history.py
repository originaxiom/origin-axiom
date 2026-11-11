"""The attribution rule is about commits, and the gate now reads them (the owner's ruling R3, confirmed to main on
2026-11-10; the advisor seat's finding G9; carried out at B1878).

Before, the gate read tracked files and the author of the last commit.  A co-author trailer, or a vendor's name in a
commit message, passed.  Each test here builds a small repository, COMMITS the violation, and reads the history."""
import importlib.util
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
VENDOR = "".join(["an", "thro", "pic"])            # spelt in pieces: the gate under test bans the word from tracked files


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_attribution_history", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _git(repo, *a, author="originaxiom"):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=" + author, "-c", "user.email=x@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _repo(tmp_path, name="r"):
    repo = tmp_path / name
    repo.mkdir()
    _git(repo, "init", "-q", "-b", "main")
    (repo / "a.txt").write_text("0 " + name + "\n", encoding="utf-8")
    _git(repo, "add", "a.txt")
    _git(repo, "commit", "-q", "-m", "the first commit of " + name)        # the name keeps two repositories' first commits apart
    return repo, _git(repo, "rev-parse", "HEAD")


def _commit(repo, message, author="originaxiom"):
    f = repo / "a.txt"
    f.write_text(f.read_text(encoding="utf-8") + "x\n", encoding="utf-8")
    _git(repo, "add", "a.txt", author=author)
    _git(repo, "commit", "-q", "-m", message, author=author)
    return _git(repo, "rev-parse", "HEAD")


def test_clean_commits_pass(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _commit(repo, "a landing, described in plain words")
    _commit(repo, "another")
    assert g.attribution_history_problems(repo, root) == ([], 2)


def test_a_co_author_trailer_is_refused(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    bad = _commit(repo, "a landing\n\nCo-Authored-By: somebody <s@example.invalid>")
    problems, n = g.attribution_history_problems(repo, root)
    assert n == 1 and problems == ["%s: a co-author trailer in the commit message" % bad[:9]]


def test_a_vendors_name_in_a_commit_message_is_refused(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    bad = _commit(repo, "a landing written with a tool of " + VENDOR)
    problems, n = g.attribution_history_problems(repo, root)
    assert n == 1 and problems == ["%s: a vendor token in the commit message" % bad[:9]]


def test_another_author_is_refused(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    bad = _commit(repo, "a landing", author="somebody-else")
    problems, n = g.attribution_history_problems(repo, root)
    assert n == 1 and problems == ["%s: authored by 'somebody-else', not originaxiom" % bad[:9]]


def test_it_fails_closed_where_the_history_cannot_be_read(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    problems, n = g.attribution_history_problems(repo, "0" * 40)
    assert n == 0 and problems and problems[0].startswith("cannot verify: the commit the attribution rule is read from")
    other, other_root = _repo(tmp_path, "other")
    _commit(other, "unrelated")
    subprocess.run(["git", "-C", str(repo), "fetch", "-q", str(other), "main"], check=True, capture_output=True)
    problems, n = g.attribution_history_problems(repo, other_root)                 # a commit this history does not descend from
    assert n == 0 and problems and "does not descend from" in problems[0]
    bare = tmp_path / "not_a_repository"
    bare.mkdir()
    assert g.attribution_history_problems(bare, root) == ([], 0)                   # nothing to read: the caller prints SKIP, as before


def test_this_repository_since_the_last_commit_that_carried_one():
    g = _gates()
    problems, n = g.attribution_history_problems(ROOT, g.ATTRIBUTION_FROM)
    assert problems == [] and n >= 695
    last = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%B", g.ATTRIBUTION_FROM], capture_output=True, text=True).stdout
    assert g._VENDOR_RE.search(last) or g._TRAILER_RE.search(last)                 # the commit the rule is read from is itself one that carried one
    ok, why = g.gate_attribution()
    assert ok and "each by originaxiom" in why
