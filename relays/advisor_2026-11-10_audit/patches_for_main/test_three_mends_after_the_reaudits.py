"""Three mends to three gates, proposed by the advisor seat after its re-audits 3 and 4 (2026-11-11).

Each case below was planted by that seat on main and passed the gate as it stood:
    t3   a copy with the sealed content, placed where the gate looked first, let the real file change unseen
    t4   a file whose mismatch was frozen by key could change again
    r2   "We claim that the Standard Model is derived." was excused, because "claim" contains "aim"
    r5   a sentence of arrival in a paper's source was not read
    r6   a sentence of arrival on a page in a folder below docs/ was not read
    c3   a co-author trailer on a commit that arrives by a merge was not read
    c4   another author's commit that arrives by a merge was not read
Each test builds a small repository or a page, plants the case, and runs the gate."""
import hashlib
import importlib.util
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = "frontier/B9002_a_sealed_run"
SCRIPT = ARC + "/verification/census.py"
LIST = ARC + "/ARTIFACT_HASHES.txt"
ELSEWHERE = "frontier/B9001_an_instrument/verification/tool.py"
CODE = "THRESHOLD = 5\nprint('the count is at most', THRESHOLD)\n"


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_three_mends", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _git(repo, *a, author="originaxiom"):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=" + author, "-c", "user.email=x@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _write(repo, rel, body):
    f = repo / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(body, encoding="utf-8")
    _git(repo, "add", rel)


def _sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _repo(tmp_path, name="r"):
    repo = tmp_path / name
    repo.mkdir()
    _git(repo, "init", "-q", "-b", "main")
    _write(repo, "a.txt", "0 " + name + "\n")
    _git(repo, "commit", "-q", "-m", "the first commit of " + name)
    return repo, _git(repo, "rev-parse", "HEAD")


def _gate(g, repo, root, frozen=frozenset(), as_found=None):
    return g.gate_artifact_hashes(_repo=repo, _frozen=frozen, _root=root, _waived={}, _amended={}, _as_found=as_found)


# ---------------------------------------------------------------- the hashed scripts: how a listed name is read
def test_t3_a_copy_beside_the_list_does_not_stand_in_for_the_real_file(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _write(repo, ELSEWHERE, CODE)
    _write(repo, LIST, "%s  %s\n" % (_sha(CODE), ELSEWHERE))                       # the list names a file from the repository's root
    _git(repo, "commit", "-q", "-m", "the seal")
    ok, why = _gate(g, repo, root)
    assert ok and "1 entries in 1 lists: 1 verify" in why, why
    _write(repo, ELSEWHERE, CODE.replace("THRESHOLD = 5", "THRESHOLD = 50"))       # the real file changes ...
    _write(repo, ARC + "/" + ELSEWHERE, CODE)                                      # ... and a copy with the sealed content is put beside the list
    _git(repo, "commit", "-q", "-m", "the instrument changed, with a copy of the old one where the gate looked first")
    assert [st for (_, _, _, st) in g.artifact_hash_state(repo)] == ["AMBIGUOUS"]
    ok, why = _gate(g, repo, root)
    assert not ok and "AMBIGUOUS" in why, why
    _git(repo, "rm", "-q", ARC + "/" + ELSEWHERE)
    _git(repo, "commit", "-q", "-m", "the copy removed")
    ok, why = _gate(g, repo, root)
    assert not ok and "MISMATCH" in why and "tool.py" in why, why                  # without the copy the change shows


def test_a_name_is_read_one_way(tmp_path):
    """a name that starts with a top-level folder is read from the root; any other name beside its list, and never from the root"""
    g = _gates()
    repo, root = _repo(tmp_path)
    _write(repo, SCRIPT, CODE)
    _write(repo, LIST, "%s  verification/census.py\n" % _sha(CODE))
    _git(repo, "commit", "-q", "-m", "the seal")
    assert [(name, st) for (_, _, name, st) in g.artifact_hash_state(repo)] == [(SCRIPT, "VERIFIES")]
    _git(repo, "rm", "-q", SCRIPT)
    _write(repo, "verification/census.py", CODE)                                   # the hashed file is gone from its place; its content stands at the root
    _git(repo, "commit", "-q", "-m", "the hashed file moved to the root")
    assert [st for (_, _, _, st) in g.artifact_hash_state(repo)] == ["ABSENT"]


def test_every_entry_of_this_repository_is_read_without_ambiguity():
    g = _gates()
    state = g.artifact_hash_state()
    assert len(state) >= 1497 and not [e for e in state if e[3] == "AMBIGUOUS"]
    tops = {f.split("/")[0] for f in subprocess.run(["git", "-C", str(ROOT), "ls-files"], capture_output=True, text=True).stdout.split("\n") if "/" in f}
    assert set(g.ARTIFACT_ROOT_FOLDERS) <= tops                                    # every folder the rule names exists


# ---------------------------------------------------------------- the hashed scripts: what a frozen entry holds
def test_t4_a_frozen_file_that_changes_again_is_refused(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _write(repo, SCRIPT, CODE)
    _write(repo, LIST, "%s  verification/census.py\n" % _sha(CODE))
    _git(repo, "commit", "-q", "-m", "the seal")
    changed = CODE.replace("THRESHOLD = 5", "THRESHOLD = 50")
    _write(repo, SCRIPT, changed)
    _git(repo, "commit", "-q", "-m", "changed after the seal; found later, and frozen as found")
    (key, _lst, _name, st), = g.artifact_hash_state(repo)
    assert st == "MISMATCH"
    frozen, as_found = frozenset({key}), {key: _sha(changed)[:16]}
    ok, why = _gate(g, repo, root, frozen, as_found)
    assert ok, why                                                                 # frozen as found: it passes
    _write(repo, SCRIPT, changed.replace("THRESHOLD = 50", "THRESHOLD = 500"))
    _git(repo, "commit", "-q", "-m", "and changed once more")
    ok, why = _gate(g, repo, root, frozen, as_found)
    assert not ok and "CHANGED AGAIN since it was frozen" in why, why
    ok, why = _gate(g, repo, root, frozen, {})                                     # without the table the second change is not seen: the gap
    assert ok, why


def test_the_frozen_entries_of_this_repository_stand_as_found():
    g = _gates()
    state = {k: (name, st) for (k, _lst, name, st) in g.artifact_hash_state()}
    for k, h in g.ARTIFACT_HASHES_BROKEN_AS_FOUND.items():
        assert k in g.ARTIFACT_HASHES_BROKEN and state[k][1] == "MISMATCH", k
        assert hashlib.sha256((ROOT / state[k][0]).read_bytes()).hexdigest()[:16] == h, state[k][0]
    assert {k for k, (_n, st) in state.items() if st == "MISMATCH" and k in g.ARTIFACT_HASHES_BROKEN} == set(g.ARTIFACT_HASHES_BROKEN_AS_FOUND)
    ok, why = g.gate_artifact_hashes()
    assert ok, why


# ---------------------------------------------------------------- a sentence of arrival: the excusing words, and the reach
def _page(tmp_path, text, name="README.md"):
    (tmp_path / "docs").mkdir(exist_ok=True)
    f = tmp_path / name
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")
    return tmp_path


def test_r2_a_word_that_only_contains_an_excusing_word_does_not_excuse(tmp_path):
    g = _gates()
    for sentence in ("We claim that the Standard Model is derived.",               # "aim" in "claim"
                     "A minor point: the Standard Model is derived.",              # "nor " in "minor "
                     "The motif is plain: the values are derived.",                # "if " in "motif "
                     "Nonetheless the Standard Model is derived.",                 # "none" in "nonetheless"
                     "Nevertheless, the values are derived."):                     # "never" in "nevertheless"
        assert g.arrival_hits(_page(tmp_path, sentence + "\n")), sentence
        ok, why = g.gate_arrival_phrases(_root=tmp_path, _baseline=0)
        assert not ok, sentence


def test_an_excusing_word_may_still_run_on(tmp_path):
    g = _gates()
    for sentence in ("The programme aims to show that the Standard Model is derived.",
                     "Among its goals: that the values are derived.",
                     "It wouldn't follow that the Standard Model is derived.",
                     "We are seeking a frame in which the values are derived.",
                     "None of this says that the Standard Model is derived.",
                     "We never say that the values are derived.",
                     "(Not yet: the Standard Model is derived only in the sense of its grammar.)"):
        assert g.arrival_hits(_page(tmp_path, sentence + "\n")) == [], sentence


def test_r5_r6_the_papers_and_the_folders_below_docs_are_read(tmp_path):
    g = _gates()
    root = _page(tmp_path, "Nothing of the kind is said on this page.\n")
    assert g.arrival_hits(root) == []
    _page(tmp_path, "With this result the Standard Model is derived.\n", "papers/a_paper/main.tex")
    _page(tmp_path, "With this result the Standard Model is derived.\n", "docs/handoffs/A_NOTE.md")
    assert sorted(h[0] for h in g.arrival_hits(root)) == ["docs/handoffs/A_NOTE.md", "papers/a_paper/main.tex"]


def test_the_wider_reach_finds_nothing_new_on_this_repository():
    g = _gates()
    hits = g.arrival_hits()
    assert sum(c for _, _, c in hits) == g.ARRIVAL_BASELINE == 3
    assert sorted(h[0] for h in hits) == ["docs/CLOSURE_MASTERPLAN.md", "docs/THE_STATE_2026-09-06.md", "docs/WHAT_WOULD_COUNT.md"]


# ---------------------------------------------------------------- commit messages: what a merge brings in
def _commit(repo, message, author="originaxiom", name="a.txt"):
    f = repo / name
    f.write_text((f.read_text(encoding="utf-8") if f.exists() else "") + "x\n", encoding="utf-8")
    _git(repo, "add", name, author=author)
    _git(repo, "commit", "-q", "-m", message, author=author)
    return _git(repo, "rev-parse", "HEAD")


def _merged(tmp_path, message, author="originaxiom"):
    repo, root = _repo(tmp_path)
    _git(repo, "checkout", "-q", "-b", "side")
    bad = _commit(repo, message, author=author)
    _git(repo, "checkout", "-q", "main")
    _commit(repo, "the line moves on", name="b.txt")
    _git(repo, "merge", "-q", "--no-ff", "-m", "the side branch merged, with a clean message", "side")
    return repo, root, bad


def test_c3_a_trailer_on_a_commit_that_arrives_by_a_merge_is_refused(tmp_path):
    g = _gates()
    repo, root, bad = _merged(tmp_path, "work on a side branch\n\nCo-Authored-By: somebody <s@example.invalid>")
    problems, n = g.attribution_history_problems(repo, root)
    assert n == 3 and problems == ["%s: a co-author trailer in the commit message" % bad[:9]], (n, problems)


def test_c4_another_author_on_a_commit_that_arrives_by_a_merge_is_refused(tmp_path):
    g = _gates()
    repo, root, bad = _merged(tmp_path, "work on a side branch", author="somebody-else")
    problems, n = g.attribution_history_problems(repo, root)
    assert n == 3 and problems == ["%s: authored by 'somebody-else', not originaxiom" % bad[:9]], (n, problems)


def test_a_clean_merge_passes(tmp_path):
    g = _gates()
    repo, root, _ = _merged(tmp_path, "work on a side branch")
    assert g.attribution_history_problems(repo, root) == ([], 3)
