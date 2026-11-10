"""A sealed file does not change after its seal (G2 of the advisor seat's audit, graded critical; its PV3 to PV6).

Before, an edit of a sealed file after its seal was detected for the few files with a hand-written ledger row only. Each
test here builds a small repository, COMMITS the violation, and runs the check on the clean tree at that commit."""
import hashlib
import importlib.util
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
SEAL = "frontier/B9001_a_sealed_test/PREREGISTRATION.md"
TEXT = "# Pre-registration\n\nThe rule, fixed before the run: the count is at most five.\n"


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_seal_immutable", ROOT / "scripts" / "gates" / "gates.py")
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


def _repo(tmp_path, name="r"):
    repo = tmp_path / name
    repo.mkdir()
    _git(repo, "init", "-q", "-b", "main")
    _write(repo, "README.md", "root of " + name + "\n")
    _git(repo, "commit", "-q", "-m", "root of " + name)
    root = _git(repo, "rev-parse", "HEAD")
    _write(repo, SEAL, TEXT)
    _git(repo, "commit", "-q", "-m", "the seal")
    return repo, root


def _commit(repo, msg):
    _git(repo, "commit", "-q", "-m", msg)
    return _git(repo, "rev-parse", "HEAD")


def test_a_seal_and_a_new_file_beside_it_pass(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _write(repo, "frontier/B9001_a_sealed_test/FINDINGS.md", "the result\n")
    _write(repo, "frontier/B9001_a_sealed_test/AMENDMENT_1.md", "an amendment is a new file beside the seal\n")
    _commit(repo, "the result and an amendment")
    problems, n = g.seal_immutable_problems(repo, root)
    assert problems == [] and n == 1


def test_pv3_a_sentence_appended_to_a_sealed_file_is_refused(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _write(repo, SEAL, TEXT + "\nA criterion added after the result was seen.\n")
    bad = _commit(repo, "append to the seal")
    assert _git(repo, "status", "--porcelain") == ""
    problems, _ = g.seal_immutable_problems(repo, root)
    assert problems == ["%s edits the sealed file %s" % (bad[:9], SEAL)]


def test_pv4_a_deleted_sealed_file_is_refused(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _git(repo, "rm", "-q", SEAL)
    bad = _commit(repo, "delete the seal")
    problems, _ = g.seal_immutable_problems(repo, root)
    assert problems == ["%s deletes the sealed file %s" % (bad[:9], SEAL)]


def test_pv5_an_edit_with_its_ledger_row_rewritten_in_the_same_commit_is_refused(tmp_path):
    """no row of any ledger can launder the edit: the check reads the file's own history"""
    g = _gates()
    repo, root = _repo(tmp_path)
    new = TEXT.replace("at most five", "at most six")
    _write(repo, SEAL, new)
    _write(repo, "docs/SEAL_LEDGER.md", "| %s | %s | abc | 1 | yes |\n" % (SEAL, hashlib.sha256(new.encode()).hexdigest()[:8]))
    bad = _commit(repo, "edit the seal and its ledger row")
    problems, _ = g.seal_immutable_problems(repo, root)
    assert len(problems) == 1 and bad[:9] in problems[0] and "edits the sealed file" in problems[0]


def test_a_moved_seal_and_the_other_seal_names_are_covered(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    for name in ("PREREG.md", "THE_DESIGN_NOTE.md", "SEALED_CARD.md", "DECLARATION.md"):
        _write(repo, "frontier/B9002_other_names/" + name, "sealed: " + name + "\n")
    _commit(repo, "four seals under other names")
    assert g.seal_immutable_problems(repo, root)[0] == []
    for name in ("PREREG.md", "THE_DESIGN_NOTE.md", "SEALED_CARD.md", "DECLARATION.md"):
        _write(repo, "frontier/B9002_other_names/" + name, "sealed: " + name + "\nedited\n")
    _commit(repo, "edit all four")
    assert len(g.seal_immutable_problems(repo, root, limit=10)[0]) == 4
    repo2, root2 = _repo(tmp_path, "r2")
    _git(repo2, "mv", SEAL, "frontier/B9001_a_sealed_test/OLD_RULE.md")
    bad = _commit(repo2, "move the seal")
    problems, _ = g.seal_immutable_problems(repo2, root2)
    assert len(problems) == 1 and bad[:9] in problems[0] and SEAL in problems[0]
    # a file that is not sealed-style changes freely
    repo3, root3 = _repo(tmp_path, "r3")
    _write(repo3, "frontier/B9001_a_sealed_test/FINDINGS.md", "v1\n")
    _commit(repo3, "findings")
    _write(repo3, "frontier/B9001_a_sealed_test/FINDINGS.md", "v2\n")
    _commit(repo3, "findings corrected")
    assert g.seal_immutable_problems(repo3, root3)[0] == []


def test_a_violation_stays_until_waived_by_commit_and_path(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _write(repo, SEAL, TEXT + "\nedited\n")
    bad = _commit(repo, "edit")
    _write(repo, SEAL, TEXT)
    back = _commit(repo, "restore")
    problems, _ = g.seal_immutable_problems(repo, root)
    assert len(problems) == 2                                   # the edit, and the edit that restores
    waived = {(bad, SEAL): "planted", (back, SEAL): "planted"}
    assert g.seal_immutable_problems(repo, root, waived)[0] == []
    assert len(g.seal_immutable_problems(repo, root, {(bad, SEAL): "planted"})[0]) == 1


def test_it_fails_closed_where_history_cannot_be_read(tmp_path):
    g = _gates()
    repo, root = _repo(tmp_path)
    _write(repo, "x.txt", "x\n")
    _commit(repo, "more")
    shallow = tmp_path / "shallow"
    subprocess.run(["git", "clone", "-q", "--depth", "1", "file://" + str(repo), str(shallow)], check=True, capture_output=True)
    problems, _ = g.seal_immutable_problems(shallow, root)
    assert problems and "cannot verify" in problems[0]
    plain = tmp_path / "export"
    plain.mkdir()
    problems, _ = g.seal_immutable_problems(plain, root)
    assert problems and "cannot verify" in problems[0]


def test_the_gate_itself_fails_on_a_post_seal_edit(tmp_path, monkeypatch):
    """the registered control: the gate function, pointed at a repository whose history holds the violation"""
    g = _gates()
    repo, root = _repo(tmp_path)
    monkeypatch.setattr(g, "ROOT", str(repo))
    monkeypatch.setattr(g, "SEAL_IMMUTABLE_FROM", root)
    ok, why = g.gate_seal_immutable()
    assert ok, why
    _write(repo, SEAL, TEXT + "\nedited after the seal\n")
    _commit(repo, "edit")
    ok, why = g.gate_seal_immutable()
    assert ok is False and "edits the sealed file" in why


def test_pv6_a_ledger_row_changed_by_hand_is_refused(monkeypatch):
    """the ledger gate recomputes every generated row from its file"""
    g = _gates()
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    import re
    m = re.search(r"^\| (frontier/B1841[^ |]+) \| ([0-9a-f]{8}) \|", ledger, re.M)
    assert m
    wrong = ("%08x" % ((int(m.group(2), 16) + 1) % 16 ** 8))
    forged = ledger.replace("| %s | %s |" % (m.group(1), m.group(2)), "| %s | %s |" % (m.group(1), wrong))
    real = g._read
    monkeypatch.setattr(g, "_read", lambda rel: forged if rel == "docs/SEAL_LEDGER.md" else real(rel))
    ok, why = g.gate_seal_ledger_current()
    assert ok is False and "is not the file's" in why and m.group(1) in why
    # a row for a file that is not in the tree
    gone = ledger + "\n| frontier/B9999_never/PREREGISTRATION.md | 00000000 | abc | 1 | yes |\n"
    monkeypatch.setattr(g, "_read", lambda rel: gone if rel == "docs/SEAL_LEDGER.md" else real(rel))
    ok, why = g.gate_seal_ledger_current()
    assert ok is False and "is listed and is not in the tree" in why


def test_pv7_the_ledger_does_not_vouch_for_itself(tmp_path):
    """G3: with the previous ledger in its evidence, the generator's second run reported nothing unrecorded; and it read
    every untracked file on the machine. Two runs must agree, and only a TRACKED file other than the ledger records a hash."""
    import shutil
    import sys
    repo, root = _repo(tmp_path)
    (repo / "scripts").mkdir()
    shutil.copy(ROOT / "scripts" / "seal_ledger.py", repo / "scripts" / "seal_ledger.py")
    (repo / "docs").mkdir()
    _git(repo, "add", "scripts/seal_ledger.py")
    _commit(repo, "the generator")
    run = lambda: subprocess.run([sys.executable, str(repo / "scripts" / "seal_ledger.py")], capture_output=True, text=True, check=True).stdout.strip()
    first = run()
    assert first == "1 rows; unrecorded single-commit 1; unrecorded amended 0"
    assert run() == first                                        # the ledger written by the first run is not evidence
    h8 = hashlib.sha256(TEXT.encode()).hexdigest()[:8]
    assert h8 in (repo / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    # an untracked note that quotes the hash does not record it
    (repo / "scratch_note.md").write_text("the seal is " + h8 + "\n", encoding="utf-8")
    assert run() == first
    # a tracked file that quotes it does
    _git(repo, "add", "scratch_note.md")
    _commit(repo, "the hash recorded in a tracked file")
    assert run() == "1 rows; unrecorded single-commit 0; unrecorded amended 0"


def test_pv8_a_seal_under_another_name_committed_with_its_results_is_in_the_class(tmp_path, monkeypatch):
    """G4: the seal-order gate read one file name, so an arc sealed as PREREG.md or DESIGN.md and first committed together
    with its FINDINGS.md was not in the class of seals whose order git cannot show, and not on the list."""
    g = _gates()
    repo, root = _repo(tmp_path)
    for arc, seal in (("B9003_together", "PREREG.md"), ("B9004_design_together", "DESIGN.md")):
        _write(repo, "frontier/%s/%s" % (arc, seal), "the rule\n")
        _write(repo, "frontier/%s/FINDINGS.md" % arc, "the result\n")
        _commit(repo, arc + ": rule and record in one commit")
    _write(repo, "frontier/B9005_in_order/PREREG.md", "the rule\n")
    _commit(repo, "B9005: the rule alone")
    _write(repo, "frontier/B9005_in_order/FINDINGS.md", "the result\n")
    _commit(repo, "B9005: the record, after")
    monkeypatch.setattr(g, "ROOT", str(repo))
    cls = g.seal_order_class()
    assert set(cls) == {"B9003", "B9004"}                       # the two committed together; not the one sealed first
    problems = g.seal_order_problems(cls, listed={}, ceiling=frozenset(), off_main={})
    assert len(problems) == 2 and all("rule and record first committed together" in x for x in problems)


def test_the_gates_are_green_on_this_repository():
    g = _gates()
    for name in ("seal-immutable", "seal-ledger-current", "seal-order-unshown"):
        ok, why = g.GATES[name]()
        assert ok, (name, why)
    assert len(g.SEAL_IMMUTABLE_FROM) == 40 and g.SEAL_IMMUTABLE_WAIVED == {}
    # the order gate reads every seal name: the audit's own example, B1297, is in the class and on the list
    cls = g.seal_order_class()
    assert "B1297" in cls and "B1297" in g.SEAL_ORDER_UNSHOWN_CEILING and len(cls) >= 110
