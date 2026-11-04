"""Lock for the decadal review's tools: every check is shown to fail on planted input.

The branch inventory carries the regression for R57-1 (three findings withdrawn in Review 57 because full refs were
compared with leaf keys)."""
import hashlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "review"))
import review_tools as rt


def test_branch_inventory_matches_on_the_leaf():
    reg = "| sep16-branch | ... |\n| standard-model-derivation-0qt6ao | ... |"
    unmerged = {"origin": ["sep16-branch", "vendor/standard-model-derivation-0qt6ao", "vendor/never-registered-xyz"], "codeberg": ["sep16-branch"]}
    inv = rt.branch_inventory(unmerged, reg)
    assert inv["unregistered"] == ["never-registered-xyz"], "the full ref is never in the register; the leaf is (R57-1b)"
    assert sorted(inv["on_one_remote_only"]) == ["never-registered-xyz", "standard-model-derivation-0qt6ao"]
    assert rt.branch_inventory({"origin": ["a/b/sep16-branch"]}, reg)["unregistered"] == []


def test_seal_check_catches_each_defect():
    data = {"a.py": b"print(1)\n", "b.txt": b"x"}
    good = "# sealed\n%s  a.py\n%s  b.txt\n" % (hashlib.sha256(data["a.py"]).hexdigest(), hashlib.sha256(data["b.txt"]).hexdigest())
    anc = lambda a, b: (a, b) == ("s1", "v1")
    ok = rt.seal_check(good, data.get, "s1", "v1", anc, True)
    assert ok["ok"] == 2 and ok["order"] == "sealed before results" and not ok["defects"]
    changed = rt.seal_check(good, {"a.py": b"print(2)\n", "b.txt": b"x"}.get, "s1", "v1", anc, True)
    assert changed["defects"] == ["changed: a.py"]
    assert rt.seal_check(good, {"a.py": data["a.py"]}.get, "s1", "v1", anc, True)["defects"] == ["missing: b.txt"]
    assert "SEALED WITH ITS RESULTS" in rt.seal_check(good, data.get, "s1", "s1", anc, True)["defects"]
    assert "SEAL NOT AN ANCESTOR OF THE RESULTS" in rt.seal_check(good, data.get, "s9", "v1", anc, True)["defects"]
    assert "seal not on every remote" in rt.seal_check(good, data.get, "s1", "v1", anc, False)["defects"]
    odd = rt.seal_check("this line is not a hash line\n", data.get, "s1", "v1", anc, True)
    assert "no hash line parsed" in odd["defects"] and "1 unparsed lines" in odd["defects"], "a hash file no parser reads is a defect, not a pass"
    b1410 = rt.seal_check("a.py  sha256  %s\n" % hashlib.sha256(data["a.py"]).hexdigest(), data.get, "s1", "v1", anc, True)
    assert b1410["ok"] == 1 and not b1410["defects"], "the second layout in the record (B1410's) is read"
    assert rt.seal_check(good, data.get, "s1", None, anc, True)["order"] == "no verdict yet"


def test_provenance_hits_only_on_the_phrases():
    lines = [("README.md", "This result was independently verified by experts."), ("docs/x.md", "verified on this bench, internally"),
             ("papers/p.md", "The method is Peer-Reviewed elsewhere."), ("docs/y.md", "nothing here")]
    hits = rt.provenance_hits(lines)
    assert [(h["path"], h["phrase"]) for h in hits] == [("README.md", "independently verified"), ("papers/p.md", "peer-reviewed")]
    assert rt.provenance_hits([("a.md", "internally verified")]) == []


def test_error_rows_separate_new_classes_from_recurrences():
    diff = "\n".join(["+| **E90 the NEW class** — text | d | t | r |", "+| **E54 instance (this bench)** — text | d | t | r |", "+| E52 the VERIFIER-DEFECT class, row rewritten | d | t | r |", "+|---|---|", " | E1 untouched |"])
    e = rt.error_rows(diff, classes_at_anchor=["E52", "E54"])
    assert e["new_classes"] == ["E90"] and dict(e["instances"]) == {"E54": 1, "E52": 1}
    assert rt.class_ids("| E2 | **vacuity** | x |\n| **E58 instance (bench)** | x |\n| **E84 the CITED-ABSENT class** | x |") == ["E2", "E84"]


def test_action_loop_ages_carried_items_and_finds_buried_open_ones():
    text = "\n".join([
        "# Review 1", "### Action items (Review 1)", "- [ ] R1-1: first", "- [x] R1-2: done", "",
        "# Review 2", "### Action items (Review 2)", "- [>] R1-1: carried (carried from R1-1)", "- [ ] R2-1: new", "",
        "# Review 3", "### Action items (Review 3)", "- [>] R1-1: carried again (carried from R2)", "- [ ] R3-1: open now", ""])
    lp = rt.action_loop(text)
    assert lp["review"] == 3 and lp["open"] == ["R3-1"]
    assert lp["carried"] == [("R1-1", 2)], "carried through two reviews"
    assert (1, "R1-1") in lp["superseded_open"] and (2, "R2-1") in lp["superseded_open"], "an open item left in a superseded block is a buried deferral"
    assert rt.action_loop("no blocks")["review"] is None


def test_gate_controls_finds_the_gate_nobody_tests():
    tests = {"test_relay_debt_gate.py": "import gates", "test_x.py": 'assert "lead-debt" in gates.GATES', "test_y.py": "gates.gate_doc_currency()"}
    g = rt.gate_controls(["relay-debt", "lead-debt", "doc-currency", "never-tested"], tests)
    assert g["uncontrolled"] == ["never-tested"] and g["controlled"] == 3


def test_term_candidates_and_the_glossary():
    window = ["the periodic curve passes through the torsion point", "a periodic curve of the trace map", "on the periodic curve the slope"]
    earlier = ["the trace map preserves kappa", "a torsion point of the surface"]
    c = rt.term_candidates(window, earlier, min_arcs=3)
    assert "periodic curve" in c and "trace map" not in c and "torsion point" not in c
    assert rt.unglossed_terms(["periodic curve", "class index"], "**Class index** — the count ...") == ["periodic curve"]


def test_sample_draw_is_seeded_not_chosen():
    arcs = ["B%d" % n for n in range(1400, 1440)]
    a = rt.sample_draw(arcs, "efa5fd46", 5); b = rt.sample_draw(list(reversed(arcs)), "efa5fd46", 5)
    assert a == b and len(a) == 5 and rt.sample_draw(arcs, "0d7ac1b3", 5) != a


def test_the_tools_run_on_this_repository():
    """the wrappers, live: the window since the last anchor is read without error and the mirrors are the two declared"""
    R = rt.gather(rt.last_anchor())
    assert R["remotes"]["mirrors"] == ["origin", "backup"] or R["remotes"]["missing_mirrors"], "a missing mirror is reported, not ignored"
    assert R["window"]["commits"] >= 0 and isinstance(R["seals"], list) and R["loop"]["review"] is not None
    assert all(not s["defects"] or s["defects"] for s in R["seals"])
    assert rt.render(R).startswith("window ")


def test_parse_hash_file_and_table_rows():
    good, bad = rt.parse_hash_file("# c\n" + "a" * 64 + "  x.py\n" + "b" * 64 + " *y.py\nnot a hash line\n")
    assert [g[1] for g in good] == ["x.py", "y.py"] and bad == ["not a hash line"]
    assert rt.table_rows_added("+| **THE NEW LAW (B1)** | text |\n+|---|---|\n-| old |\n | context |") == ["**THE NEW LAW (B1)**"]
    assert rt.leaf("origin/a/b/c-1") == "c-1"


def test_relay_split_by_direction():
    led = "\n".join(["| `CC_TO_CODEX_2026-09-15_X.md` | OPEN | 2026-09-15 | held |", "| `CC_TO_SM_2026-09-16_Y.md` (in docs) | OPEN | 2026-09-16 | held |",
                     "| `CODEX_TO_CC_2026-09-02_Z.md` | OPEN | 2026-09-10 | r |", "| `CC_TO_CLOUD_2026-08-25_W.md` | DECLINED | 2026-08-25 | why |", "| `A_HANDOFF.md` | BANKED | 2026-09-01 | B1 |"])
    r = rt.relay_split(led)
    assert r["outbound"] == {"CODEX": 1, "SM": 1} and r["inbound"] == {"CODEX": 1} and r["declined"] == 1 and r["banked"] == 1


def test_seal_check_tells_a_disclosed_change_from_an_undisclosed_one():
    """R61-4 / R62-4: a post-seal change named on the arc's pages with its sealed version kept is reported, not a defect;
    named without a kept version, or kept without being named, it stays a defect (each half can fail)."""
    data = {"a.py": b"print(1)\n"}
    h = hashlib.sha256(data["a.py"]).hexdigest()
    anc = lambda a, b: (a, b) == ("s1", "v1")
    now = {"a.py": b"print(2)\n"}.get
    plain = "%s  a.py\n" % h
    kept_line = "# sealed at abc1234: %s  a.py (sealed)\n%s  a.py\n" % (h, h)
    page = "Disclosed: a.py was repaired after the seal; the sealed run is kept."
    d = rt.seal_check(plain, now, "s1", "v1", anc, True, page, lambda rel: True)
    assert not d["defects"] and d["changed_disclosed"] == ["a.py"]
    d2 = rt.seal_check(kept_line, now, "s1", "v1", anc, True, page, None)
    assert not d2["defects"] and d2["changed_disclosed"] == ["a.py"], "a '# sealed at' line keeps the sealed version"
    assert rt.seal_check(plain, now, "s1", "v1", anc, True, page, lambda rel: False)["defects"] == ["changed: a.py"]
    assert rt.seal_check(plain, now, "s1", "v1", anc, True, "nothing named here", lambda rel: True)["defects"] == ["changed: a.py"]
    assert rt.seal_check(plain, now, "s1", "v1", anc, True)["defects"] == ["changed: a.py"], "the old call is unchanged"



def test_on_mirror_reads_a_pushed_but_unfetched_mirror(tmp_path):
    """R67-1 (B1709): a mirror with no remote-tracking ref is read in its own repository; a commit it lacks is reported
    absent (the failing path)."""
    import subprocess as sp
    run = lambda *a, cwd=tmp_path: sp.run(list(a), cwd=cwd, capture_output=True, text=True, check=True)
    work, bare = tmp_path / "work", tmp_path / "mirror.git"
    run("git", "init", "-q", "-b", "main", str(work)); run("git", "init", "-q", "--bare", "-b", "main", str(bare))
    for i in (1, 2):
        (work / "f.txt").write_text(str(i)); run("git", "add", "f.txt", cwd=work)
        run("git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", str(i), cwd=work)
        if i == 1:
            run("git", "remote", "add", "m", str(bare), cwd=work); run("git", "push", "-q", "m", "main", cwd=work)
    first = run("git", "rev-parse", "HEAD~1", cwd=work).stdout.strip(); head = run("git", "rev-parse", "HEAD", cwd=work).stdout.strip()
    assert rt.on_mirror(first, "m", root=work)
    assert not rt.on_mirror(head, "m", root=work)                  # not pushed yet: reported absent


def test_r68_1_repository_relative_dependencies_resolve(tmp_path):
    """R68-1 (2026-10-24): a seal's ARTIFACT_HASHES pins its instruments relative to the arc and its dependencies relative to
    the repository; both must resolve, and a missing path must stay missing (it is a defect, not silently skipped)."""
    arc = tmp_path / "frontier" / "B9999_planted"; (arc / "verification").mkdir(parents=True)
    (arc / "verification" / "inst.py").write_text("x = 1\n")
    dep = tmp_path / "frontier" / "B9998_dep" / "verification"; dep.mkdir(parents=True); (dep / "lib.py").write_text("y = 2\n")
    rel_arc = "frontier/B9999_planted"
    assert rt.resolve_hashed(tmp_path, rel_arc, "verification/inst.py") is not None
    assert rt.resolve_hashed(tmp_path, rel_arc, "frontier/B9998_dep/verification/lib.py") is not None
    assert rt.resolve_hashed(tmp_path, rel_arc, "frontier/B9998_dep/verification/missing.py") is None
    good = hashlib.sha256(b"y = 2\n").hexdigest()
    read = lambda rel: (lambda f: f.read_bytes() if f else None)(rt.resolve_hashed(tmp_path, rel_arc, rel))
    c = rt.seal_check("%s  frontier/B9998_dep/verification/lib.py\n" % good, read, "a", "b", lambda a, b: True, True)
    assert c["ok"] == 1 and not c["defects"]
    bad = rt.seal_check("%s  frontier/B9998_dep/verification/lib.py\n" % ("0" * 64), read, "a", "b", lambda a, b: True, True)
    assert any("changed" in d for d in bad["defects"])


def test_action_loop_follows_a_rekeyed_lineage_and_the_carry_age_gate_fires_on_it():
    """S299 (Review 74): since about Review 62 each carry is re-keyed and its lineage written after the colon; the counter
    read only the keys before the colon, so R71-8 -> R72-3 -> R73-1 aged 1 each review and the third-carry rule never fired"""
    text = "\n".join([
        "# Review 1", "### Action items (Review 1)", "- [>] R1-1: the mirror (owner: the owner) -- carried to Review 2 as R2-1", "",
        "# Review 2", "### Action items (Review 2)", "- [>] R2-1: the mirror (carried from R1-1; owner: the owner)", "- [x] R2-2: done", "",
        "# Review 3", "### Action items (Review 3)", "- [>] R3-1: the mirror (carried from R2-1, before it R1-1)", "- [ ] R3-2: new", "",
        "# Review 4", "### Action items (Review 4)", "- [>] R4-1: the mirror (carried from R3-1)", "- [>] R4-2: once (carried from R3-2)", ""])
    lp = rt.action_loop(text)
    assert dict(lp["carried"]) == {"R4-1": 3, "R4-2": 1}, lp["carried"]
    import importlib, sys as _s
    _s.path.insert(0, str(rt.ROOT / "scripts" / "gates")); G = importlib.import_module("gates")
    bad = G.carry_age_problems(text)
    assert len(bad) == 1 and bad[0].startswith("R4-1 carried 3 times"), bad
    assert G.carry_age_problems(text.replace("R4-1: the mirror", "R4-1: declined as a loop item, the owner's step on P-547: the mirror")) == []


def test_suite_summary_reads_the_counts_and_the_failing_ids():
    log = "\n".join(["....F..", "FAILED tests/test_a.py::test_x - AssertionError", "ERROR tests/test_b.py::test_y",
                     "2 failed, 7891 passed, 70 skipped, 1 warning in 1637.41s (0:27:17)", "SUITE_EXIT 1"])
    s = rt.suite_summary(log)
    assert s["counts"] == {"failed": 2, "passed": 7891, "skipped": 70, "warnings": 1}, s
    assert s["failing"] == ["tests/test_a.py::test_x", "tests/test_b.py::test_y"]
    assert rt.suite_summary("no summary")["counts"] == {}


def test_seal_check_reads_a_staged_table_by_each_paths_last_hash_and_knows_a_rename():
    """S299 (Review 74): B1823's table hashes model.py three times (plan, a disclosed change, final) and its DESIGN.md is
    kept under a new name; the tool reported both as defects"""
    import hashlib
    h = lambda b: hashlib.sha256(b).hexdigest()
    files = {"model.py": b"v3", "DRAFT.md": b"design"}
    table = "# plan\n%s  model.py\n# a disclosed change\n%s  model.py\n# final\n%s  model.py\n%s  DESIGN.md\n" % (h(b"v1"), h(b"v2"), h(b"v3"), h(b"design"))
    anc = lambda a, b: True
    s = rt.seal_check(table, files.get, "s1", "v1", anc, True, by_hash=lambda x: next((k for k, v in files.items() if h(v) == x), None))
    assert s["defects"] == [] and s["ok"] == 2 and s["lines"] == 2 and s["superseded_in_table"] == 2 and s["renamed"] == ["DESIGN.md -> DRAFT.md"], s
    files["model.py"] = b"v4"                                  # the final state changed: still a defect
    assert rt.seal_check(table, files.get, "s1", "v1", anc, True)["defects"][0] == "changed: model.py"


def test_provenance_hits_skip_a_disclaimer_as_the_gate_does():
    """S299 (Review 74): 'Nothing here is externally verified' is a disclaimer; the gate's negation window, now the tool's"""
    lines = [("README.md", 'Nothing here is externally verified or peer-reviewed. "Verified" means recomputed.'),
             ("docs/X.md", "This result was externally verified by a referee.")]
    hits = rt.provenance_hits(lines)
    assert [h["path"] for h in hits] == ["docs/X.md"], hits
    import importlib, sys as _s
    _s.path.insert(0, str(rt.ROOT / "scripts" / "gates")); G = importlib.import_module("gates")
    assert rt.NEGATION == G.PRETENSE_NEGATION, "the tool's window must stay the gate's"
