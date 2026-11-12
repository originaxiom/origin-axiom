"""The listener between main and the seats (scripts/seats/listen.py; the owner's ruling of 2026-11-11, P-795).

What could fail: a seat not told of a new message; a seat told twice of the same one; a seat told of nothing when its page
has not changed; main not told that a seat's branch moved; the listener touching the working tree or HEAD; or a listener
that cannot look saying nothing new instead of saying that it could not look."""
import importlib.util
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LISTEN = ROOT / "scripts" / "seats" / "listen.py"


def _git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _page(*numbers):
    body = "# a seat's page\n\nsome words\n\n## Messages from main (newest first)\n\n"
    for n in sorted(numbers, reverse=True):
        body += "### M%d — a day — a subject\n\nthe text of message %d\n\n" % (n, n)
    return body + "## What main is waiting for from you\n\nnothing yet\n"


def _origin_and_clone(tmp_path):
    origin = tmp_path / "origin"
    (origin / "docs" / "seats").mkdir(parents=True)
    (origin / "docs" / "seats" / "x.md").write_text(_page(1), encoding="utf-8")
    _git(origin, "init", "-q", "-b", "main")
    _git(origin, "add", "-A")
    _git(origin, "commit", "-q", "-m", "the page, with its first message")
    clone = tmp_path / "clone"
    subprocess.run(["git", "clone", "-q", "file://" + str(origin), str(clone)], check=True, capture_output=True)
    return origin, clone


def _listen(clone, *args):
    return subprocess.run([sys.executable, str(LISTEN), "--once", "--repo", str(clone), *args], capture_output=True, text=True, timeout=120)


def test_a_seat_is_told_of_each_message_once_and_of_nothing_when_nothing_is_new(tmp_path):
    origin, clone = _origin_and_clone(tmp_path)
    head, status = _git(clone, "rev-parse", "HEAD"), _git(clone, "status", "--porcelain")
    r = _listen(clone, "--seat", "x")
    assert r.returncode == 0 and "the text of message 1" in r.stdout and "M1" in r.stdout
    assert _listen(clone, "--seat", "x").returncode == 3                       # the same page: nothing new, and no words
    assert _listen(clone, "--seat", "x").stdout == ""
    # main adds a message: the seat is told of the new one and not again of the old
    (origin / "docs" / "seats" / "x.md").write_text(_page(1, 2), encoding="utf-8")
    _git(origin, "commit", "-q", "-a", "-m", "a second message")
    r = _listen(clone, "--seat", "x")
    assert r.returncode == 0 and "the text of message 2" in r.stdout and "the text of message 1" not in r.stdout
    assert _listen(clone, "--seat", "x").returncode == 3
    # main changes the page elsewhere: the seat is told to read it, with no message repeated
    (origin / "docs" / "seats" / "x.md").write_text(_page(1, 2).replace("nothing yet", "your card"), encoding="utf-8")
    _git(origin, "commit", "-q", "-a", "-m", "what main waits for")
    r = _listen(clone, "--seat", "x")
    assert r.returncode == 0 and "No new message" in r.stdout and "the text of message" not in r.stdout
    # the listener fetched and did nothing else: the seat's checkout is where it was
    assert _git(clone, "rev-parse", "HEAD") == head and _git(clone, "status", "--porcelain") == status


def test_peeking_does_not_count_as_having_read(tmp_path):
    _, clone = _origin_and_clone(tmp_path)
    assert _listen(clone, "--seat", "x", "--peek").returncode == 0
    r = _listen(clone, "--seat", "x")
    assert r.returncode == 0 and "the text of message 1" in r.stdout


def test_a_listener_that_cannot_look_says_so(tmp_path):
    _, clone = _origin_and_clone(tmp_path)
    r = _listen(clone, "--seat", "nobody")
    assert r.returncode == 2 and "no page docs/seats/nobody.md" in r.stderr     # not 3: 'nothing new' would be untrue
    bare = tmp_path / "not_a_repository"
    bare.mkdir()
    r = _listen(bare, "--seat", "x")
    assert r.returncode == 2 and "could not look" in r.stderr
    r = _listen(clone, "--seat", "../x")
    assert r.returncode == 2 and "refused" in r.stderr


def test_main_is_told_when_a_seats_branch_moves_and_shown_names_only(tmp_path):
    origin, clone = _origin_and_clone(tmp_path)
    _git(origin, "checkout", "-q", "-b", "lane/one")
    (origin / "secret.txt").write_text("what the lane holds: 0.123456\n", encoding="utf-8")
    _git(origin, "add", "-A")
    _git(origin, "commit", "-q", "-m", "a lane's first commit")
    _git(origin, "checkout", "-q", "main")
    first = _listen(clone, "--main")                                            # the first look has nothing to compare with: it shows where the
    assert first.returncode == 0 and "FIRST LOOK" in first.stdout and "origin/lane/one" in first.stdout          # branches are, once (Review 79)
    assert "0.123456" not in first.stdout
    assert _listen(clone, "--main").returncode == 3
    _git(origin, "checkout", "-q", "lane/one")
    (origin / "secret.txt").write_text("what the lane holds: 0.654321\n", encoding="utf-8")
    _git(origin, "commit", "-q", "-a", "-m", "the lane moves")
    _git(origin, "checkout", "-q", "main")
    r = _listen(clone, "--main")
    assert r.returncode == 0 and "origin/lane/one" in r.stdout and "->" in r.stdout
    assert "0.654321" not in r.stdout and "what the lane holds" not in r.stdout   # names and commits, nothing a branch holds
    assert _listen(clone, "--main").returncode == 3
    # a commit on main itself is not a seat's move
    (origin / "docs" / "seats" / "x.md").write_text(_page(1, 2), encoding="utf-8")
    _git(origin, "commit", "-q", "-a", "-m", "main's own commit")
    assert _listen(clone, "--main").returncode == 3


def test_the_messages_of_a_page_are_read_whole_and_in_their_numbers():
    spec = importlib.util.spec_from_file_location("seat_listener_lock", LISTEN)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    ms = m.messages(_page(1, 2, 10))
    assert sorted(ms) == [1, 2, 10] and ms[10].startswith("### M10 ") and "the text of message 10" in ms[10]
    assert "What main is waiting for" not in ms[1] and "the text of message 2" not in ms[1]
    # every page main has written is read by the same rule: each has its messages, numbered from 1 with none missing
    pages = sorted((ROOT / "docs" / "seats").glob("*.md"))
    seats = [p for p in pages if p.name != "README.md"]
    assert len(seats) >= 6
    for p in seats:
        got = sorted(m.messages(p.read_text(encoding="utf-8")))
        assert got and got == list(range(1, len(got) + 1)), (p.name, got)


def test_a_message_is_stored_as_read_only_after_it_is_shown_and_never_when_the_page_cannot_be_read(tmp_path):
    """Review 79, found by a reading of the listener by a session that did not build it: the page was stored as read before
    its messages were printed, and a `git show` that failed was taken for an empty page and stored as read.  Either lost a
    message for good."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("listen_for_test", LISTEN); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
    origin, clone = _origin_and_clone(tmp_path)
    status, text, remember = L.look_seat("x", str(clone), "origin", False)
    state = pathlib.Path(L.memory(str(clone))) / "x.json"
    assert status == 0 and "M1" in text and callable(remember) and not state.exists()      # shown to the caller, not yet stored
    remember()
    assert state.exists() and L.look_seat("x", str(clone), "origin", False)[0] == 3         # stored: nothing new
    state.unlink()
    real = L.git
    L.git = lambda *a, cwd=None: (1, "", "planted: the page cannot be read") if a and a[0] == "show" else real(*a, cwd=cwd)
    try:
        status, text, remember = L.look_seat("x", str(clone), "origin", False)
    finally:
        L.git = real
    assert status == 2 and "could not be read" in text and remember is None and not state.exists()




def test_an_amended_message_is_shown_a_fenced_heading_is_not_a_heading_and_a_damaged_memory_is_said(tmp_path):
    """Review 79, from a reading of the listener on another family of model: a message changed in place was never shown again;
    a line beginning with # inside a block of code cut a message short; a damaged memory file crashed the listener."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("listen_for_test2", LISTEN); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
    # the fenced heading
    page = "## Messages from main (newest first)\n\n### M2 — a day — with code\n\nrun this:\n\n```\n# a comment, not a heading\n## nor this\ngit status\n```\n\nand then stop.\n\n### M1 — a day — plain\n\ntext one\n\n## What main is waiting for from you\n\nnothing\n"
    ms = L.messages(page)
    assert sorted(ms) == [1, 2] and "and then stop." in ms[2] and "git status" in ms[2] and "What main is waiting" not in ms[1]
    # the amendment
    origin, clone = _origin_and_clone(tmp_path)
    r = _listen(clone, "--seat", "x"); assert r.returncode == 0 and "M1" in r.stdout
    assert _listen(clone, "--seat", "x").returncode == 3
    p = origin / "docs" / "seats" / "x.md"
    p.write_text(p.read_text(encoding="utf-8").replace("the text of message 1", "the text of message 1, AMENDED"), encoding="utf-8")
    _git(origin, "commit", "-q", "-a", "-m", "main amends its first message in place")
    r = _listen(clone, "--seat", "x")
    assert r.returncode == 0 and "CHANGED since: M1" in r.stdout and "AMENDED" in r.stdout
    assert _listen(clone, "--seat", "x").returncode == 3
    # the damaged memory
    mem = pathlib.Path(L.memory(str(clone))) / "x.json"
    mem.write_text("{ this is not json", encoding="utf-8")
    r = _listen(clone, "--seat", "x")
    assert r.returncode == 2 and "memory cannot be read" in r.stderr
