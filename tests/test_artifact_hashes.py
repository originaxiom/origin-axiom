"""What a seal hashed does not change after the seal (the advisor seat's second re-audit, 2026-11-10; its planted case s1).

Before, a sealed rule's text was protected and the scripts its seal hashed were not: 189 folders carried a list of hashed
files and no gate read one.  Each test here builds a small repository, COMMITS the violation, and runs the gate on the clean
tree at that commit."""
import hashlib
import importlib.util
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = "frontier/B9002_a_sealed_run"
SCRIPT = ARC + "/verification/census.py"
LIST = ARC + "/ARTIFACT_HASHES.txt"
CODE = "THRESHOLD = 5\nprint('the count is at most', THRESHOLD)\n"


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_artifact_hashes", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
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
    """a repository with a root commit, then a seal: a script and the list that records its hash"""
    repo = tmp_path / name
    repo.mkdir()
    _git(repo, "init", "-q", "-b", "main")
    _write(repo, "README.md", "root of " + name + "\n")
    _git(repo, "commit", "-q", "-m", "root of " + name)
    root = _git(repo, "rev-parse", "HEAD")
    _write(repo, SCRIPT, CODE)
    _write(repo, LIST, "# sealed with the rule: sha256 of the instrument\n%s  verification/census.py\n" % _sha(CODE))
    _git(repo, "commit", "-q", "-m", "the seal")
    return repo, root


def _gate(g, repo, root, **kw):
    return g.gate_artifact_hashes(_repo=repo, _frozen=kw.pop("frozen", frozenset()), _root=root, _waived=kw.pop("waived", {}), _amended=kw.pop("amended", {}))


def test_a_seal_whose_script_is_unchanged_passes(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    ok, why = _gate(g, repo, root)
    assert ok and "1 entries in 1 lists: 1 verify" in why, why


def test_s1_a_line_added_to_a_script_the_seal_hashed_is_refused(tmp_path):
    """the re-audit's s1: the criterion could not be changed after the fact, and the script that evaluates it could"""
    g = _gates()
    repo, root = _repo(tmp_path)
    _write(repo, SCRIPT, CODE.replace("THRESHOLD = 5", "THRESHOLD = 50"))
    _git(repo, "commit", "-q", "-m", "the threshold loosened after the seal")
    ok, why = _gate(g, repo, root)
    assert not ok and "MISMATCH" in why and "census.py" in why, why


def test_the_script_and_its_list_changed_together_is_refused(tmp_path):
    """the same edit with the list rewritten to match: every hash verifies, and the gate reads the list's history"""
    g = _gates()
    repo, root = _repo(tmp_path)
    new = CODE.replace("THRESHOLD = 5", "THRESHOLD = 50")
    _write(repo, SCRIPT, new)
    _write(repo, LIST, "# sealed with the rule: sha256 of the instrument\n%s  verification/census.py\n" % _sha(new))
    _git(repo, "commit", "-q", "-m", "the script and the list rewritten together")
    assert all(st == "VERIFIES" for (_, _, _, st) in g.artifact_hash_state(repo))
    ok, why = _gate(g, repo, root)
    assert not ok and "edits the list of hashed files" in why, why


def test_a_list_deleted_or_moved_is_refused(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _git(repo, "rm", "-q", LIST)
    _git(repo, "commit", "-q", "-m", "the list removed")
    ok, why = _gate(g, repo, root)
    assert not ok and "deletes the list of hashed files" in why, why
    repo2, root2 = _repo(tmp_path, "r2")
    _git(repo2, "mv", LIST, ARC + "/OLD_HASHES.txt")
    _git(repo2, "commit", "-q", "-m", "the list renamed out of sight")
    ok, why = _gate(g, repo2, root2)
    assert not ok and "the list of hashed files" in why, why


def test_a_disclosed_amendment_is_a_new_list_and_a_named_key_and_is_printed(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    new = CODE + "# amended after the seal, disclosed in the findings\n"
    _write(repo, SCRIPT, new)
    _write(repo, ARC + "/ARTIFACT_HASHES_AMENDMENT_1.txt", "%s  verification/census.py\n" % _sha(new))
    _git(repo, "commit", "-q", "-m", "an amendment: a new list beside the old")
    ok, why = _gate(g, repo, root)
    assert not ok and "MISMATCH" in why                                   # the old entry no longer verifies, and nothing names it
    old_key = next(k for (k, lst, name, st) in g.artifact_hash_state(repo) if st == "MISMATCH")
    ok, why = _gate(g, repo, root, amended={old_key: "FINDINGS, the dated note"})
    assert ok and "amended by name: 1" in why and old_key in why and "the dated note" in why, why


def test_a_list_that_names_what_is_not_there_is_refused(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _write(repo, ARC + "/ARTIFACT_HASHES_MORE.txt", "%s  verification/not_there.py\n" % _sha("x"))
    _git(repo, "commit", "-q", "-m", "a list naming a file that is not in the repository")
    ok, why = _gate(g, repo, root)
    assert not ok and "ABSENT" in why, why


def test_every_format_the_record_uses_is_read(tmp_path):
    g = _gates()
    h = _sha("x")
    assert g._hash_list_entry("%s  verification/a.py" % h) == (h, "verification/a.py")
    assert g._hash_list_entry("PREREGISTRATION.md  sha256  %s" % h) == (h, "PREREGISTRATION.md")
    assert g._hash_list_entry("PREREGISTRATION.md sha256: %s" % h) == (h, "PREREGISTRATION.md")
    assert g._hash_list_entry("GATE.md  sha256=%s" % h) == (h, "GATE.md")
    assert g._hash_list_entry("# sealed files (sha256), 2026-10-20") is None
    assert g._hash_list_entry("%s before the run" % h) == (h, None)


def test_it_fails_closed_where_history_or_the_file_list_cannot_be_read(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    plain = tmp_path / "plain"
    plain.mkdir()
    ok, why = g.gate_artifact_hashes(_repo=plain, _frozen=frozenset(), _root=root)
    assert not ok and "cannot verify" in why
    ok, why = g.gate_artifact_hashes(_repo=repo, _frozen=frozenset(), _root="0" * 40)
    assert not ok and "cannot verify" in why


def test_the_gate_itself_fails_on_main_when_one_frozen_entry_is_forgotten():
    """the real repository: the gate passes with the frozen keys, and with any one of them removed it fails"""
    g = _gates()
    ok, why = g.gate_artifact_hashes()
    assert ok, why
    assert len(g.ARTIFACT_HASHES_BROKEN) == 63
    one = sorted(g.ARTIFACT_HASHES_BROKEN)[0]
    ok, why = g.gate_artifact_hashes(_frozen=g.ARTIFACT_HASHES_BROKEN - {one})
    assert not ok and ("MISMATCH" in why or "ABSENT" in why or "NOT TRACKED" in why or "NO NAME" in why), why
    assert "artifact-hashes" in g.GATES


def test_the_older_gates_print_their_waivers(tmp_path):
    """the re-audit's a2 and s5: a waiver must not vanish from the gate's own sentence. On main the lists of waivers are
    empty and the sentences say so. Then a violation is COMMITTED in a small repository and waived by name: the gate passes,
    and its sentence names the commit, the file and the reason."""
    g = _gates()
    ok, why = g.gate_seal_immutable()
    assert ok and "waived: 0" in why, why
    ok, why = g.gate_append_only()
    assert ok and "0 waived by name" in why, why
    # a sealed rule edited after its seal, in a repository of its own
    repo, root = _repo(tmp_path, "w")
    rule = "frontier/B9002_a_sealed_run/PREREG.md"
    _write(repo, rule, "the count is at most 5\n")
    _git(repo, "commit", "-q", "-m", "the rule")
    _write(repo, rule, "the count is at most 50\n")
    _git(repo, "commit", "-q", "-m", "the rule, moved after the fact")
    bad = _git(repo, "rev-parse", "HEAD")
    g.ROOT, g.SEAL_IMMUTABLE_FROM, g.SEAL_IMMUTABLE_WAIVED = repo, root, {}
    ok, why = g.gate_seal_immutable()
    assert not ok and "PREREG.md" in why, why
    g.SEAL_IMMUTABLE_WAIVED = {(bad, rule): "the owner's reason, in words"}
    ok, why = g.gate_seal_immutable()
    assert ok and "waived: 1" in why and bad[:9] in why and rule in why and "the owner's reason, in words" in why, why
    line = g.result_line("seal-immutable", ok, why)
    assert "the owner's reason, in words" in line and bad[:9] in line and line.strip() != "PASS  seal-immutable: ok"


def test_the_runner_prints_the_whole_sentence_of_a_gate_that_holds_waivers():
    """what main found when mending a2 and s5: each gate put its waivers in its sentence, and the runner printed a bare 'ok'
    for every pass, so the sentence never reached the reader."""
    g = _gates()
    for name in ("append-only", "seal-immutable", "artifact-hashes"):
        assert name in g.PRINTS_ITS_SENTENCE and name in g.GATES
        ok, detail = g.GATES[name]()
        line = g.result_line(name, ok, detail)
        assert ok and line.strip().startswith("PASS  %s: " % name) and "waived" in line and line.strip() != "PASS  %s: ok" % name, line
    assert "amended by name: 0" in g.result_line("artifact-hashes", *g.GATES["artifact-hashes"]())
    # the other gates are printed as before, and a gate that checked nothing is still SKIP
    assert g.result_line("vendor", True, "ok").strip() == "PASS  vendor: ok"
    assert g.result_line("vendor", True, ["x"]).strip() == "PASS  vendor: ok"
    assert g.result_line("attribution", True, "skipped: no git").strip().startswith("SKIP  attribution")
    assert g.result_line("append-only", False, "cannot verify").strip() == "FAIL  append-only: cannot verify"
    src = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    assert "print(result_line(name, ok, detail))" in src
