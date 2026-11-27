"""2026-11-26, rebuilt 2026-11-27 by T7b (the framework's thin path, patches T3 and T7b; main's M57, M64 and M65; register
row P-885): discovery, scripts/queue/discover.py, and harvest_debt.py's stop on a pin that does not resolve.

On small repositories built here, with a table of seat codes by branch: a card on its branch, under its branch's code, whose
stated commit is an ancestor of where it was found with the same script there, is filed FILED by the runner; a card on a
branch not in the table, under another branch's code, with a malformed title, at a path the schema refuses, with a fenced
title, with a stated commit that is not an ancestor, or with a script that changed since, is not filed and its seat is told,
and the other cards are still filed; one card's text on two branches is two cards; a new version, or a card with the same
script and decisive lines, is a refile, and so is a card that says what it refiles; the old version is not taken further;
main's cards are found first; a masked ref is read only in its masked segment."""
import importlib.util
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


D = _load("discover_under_test", "scripts/queue/discover.py")
QS = D.QS
AT = "2026-11-27T12:00:00Z"
A, B = "fam2-v5-high-01", "fam3-v1-max-01"
CODES = {"seat/a": A, "seat/c": A, "seat/b": B, "main": QS.MAIN_CODE}
CARD = """# CLAIM CARD — {title}

- card id: {cid}
- seat code: {code}
- seat, branch, commit: {code}, {branch}, {stated}
- decisive script: x.py, SHA-256 {h}, depends on the standard library, run as python3 x.py, output SHA-256 0011223344556677{heavy}
- decisive lines: 1 lines marked "DECISIVE:", SHA-256 {d}
- failing control: python3 x.py --plant
"""


def _repo(tmp_path, branch="seat/a"):
    tmp_path.mkdir(parents=True, exist_ok=True)
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True).stdout
    g("init", "-q", "-b", branch)
    (tmp_path / "x.py").write_text("print('DECISIVE: n = 12')\n", encoding="utf-8")
    (tmp_path / "relays" / "claims").mkdir(parents=True)
    g("add", "-A")
    g("commit", "-q", "-m", "the script")
    base = g("rev-parse", "HEAD").strip()

    def card(title, cid="new", code=A, br=None, stated=None, h="aaaaaaaaaaaaaaaa", d="dddddddddddddddd", heavy=""):
        return CARD.format(title=title, cid=cid, code=code, branch=br or branch, stated=stated or base, h=h, d=d,
                           heavy=heavy)

    def put(name, text, on=None):
        on = on or branch
        if g("symbolic-ref", "--short", "HEAD").strip() != on:
            g("checkout", "-q", on) if subprocess.run(["git", "rev-parse", "--verify", "-q", on], cwd=tmp_path,
                                                      capture_output=True).returncode == 0 else g("checkout", "-q", "-b", on)
        (tmp_path / "relays" / "claims").mkdir(parents=True, exist_ok=True)
        (tmp_path / "relays" / "claims" / name).write_text(text, encoding="utf-8")
        g("add", "-A")
        g("commit", "-q", "-m", name)
        g("update-ref", "refs/remotes/origin/%s" % on, "HEAD")
        return g("rev-parse", "HEAD").strip()
    return g, put, card, base


def _discover(queue, refs, root, **kw):
    return D.discover(queue, refs, root=root, at=AT, codes=CODES, **kw)


def test_a_card_is_filed_and_each_card_that_cannot_be_filed_is_told_while_the_others_are_filed(tmp_path):
    g, put, card, base = _repo(tmp_path)
    put("CLAIM_one.md", card("a count"))
    put("CLAIM_other_code.md", card("under another branch's code", code=B))
    put("CLAIM_bad_title.md", card("x").replace("# CLAIM CARD — x", "# CLAIM CARD x"))
    put("CLAIM_no code.md", card("a path the schema refuses"))
    put("CLAIM_é.md", card("a name with a letter outside ASCII"))             # A19: read whole with -z, and said
    put("NOTES.md", "a note\n\n# CLAIM CARD — fenced, not a card's first line\n")
    put("CLAIM_not_ancestor.md", card("a stated commit that is not an ancestor", stated="0" * 40))
    put("CLAIM_branch.md", card("a stated branch that is not where it is", br="seat/z"))
    new, report = _discover({}, [("a", "origin/seat/a"), ("gone", "origin/no-such")], tmp_path)
    paths = sorted(r["card_path"] for r in new.values())
    assert paths == ["relays/claims/CLAIM_one.md"], (paths, report)
    rec = list(new.values())[0]
    assert rec["status"] == "FILED" and rec["history"][0]["by"] == "runner" and rec["seat_code"] == A
    told = "\n".join(report)
    assert any("CLAIM_é.md: not filed, its path is not" in r for r in report)
    for words in ("its seat code %s is not %s, the code of its branch seat/a" % (B, A),
                  "its first line is not '# CLAIM CARD", "its path is not relays/claims/CLAIM_<name>.md",
                  "NOTES.md: not filed, it holds a card's title", "is not an ancestor of",
                  "it says it is on seat/z, and was found on seat/a", "gone (origin/no-such): cannot be read"):
        assert words in told, words
    assert QS.queue_problems({k: json.dumps(v) for k, v in new.items()}) == []


def test_a_branch_not_in_the_table_and_a_script_changed_since_the_stated_commit(tmp_path):
    g, put, card, base = _repo(tmp_path)
    put("CLAIM_one.md", card("a count"), on="seat/unknown")
    new, report = _discover({}, [("u", "origin/seat/unknown")], tmp_path)
    assert new == {} and any("its branch seat/unknown is not in queue/SEAT_CODES.json" in r for r in report)
    g("checkout", "-q", "seat/a")
    (tmp_path / "x.py").write_text("print('DECISIVE: n = 13')\n", encoding="utf-8")
    g("commit", "-q", "-am", "the script changed after the stated commit")
    put("CLAIM_one.md", card("a count"))
    new, report = _discover({}, [("a", "origin/seat/a")], tmp_path)
    assert new == {} and any("x.py is not the same at its stated commit" in r for r in report)


def test_a_second_look_files_nothing_and_refiles_are_linked(tmp_path):
    g, put, card, base = _repo(tmp_path)
    put("CLAIM_one.md", card("a count"))
    new, _ = _discover({}, [("a", "origin/seat/a")], tmp_path)
    (q1,) = new
    blob = g("rev-parse", "HEAD:relays/claims/CLAIM_one.md").strip()
    seen = {("seat/a", "relays/claims/CLAIM_one.md", blob): q1}
    assert _discover(new, [("a", "origin/seat/a")], tmp_path, seen_blobs=seen)[0] == {}
    # a new version that says what it refiles: linked, the note agrees with the record, and the old one is set aside
    put("CLAIM_one.md", card("a count, mended", cid="refiles %s" % q1, h="cccccccccccccccc"))
    v2, report = _discover(new, [("a", "origin/seat/a")], tmp_path, seen_blobs=seen)
    (r2,) = v2.values()
    assert r2["refiles"] == [q1] and r2["history"][0]["note"] == "found on its branch; refiles %s" % q1
    assert any("%s is refiled by %s, and is not taken further" % (q1, r2["id"]) in r for r in report)
    # a card that names a refile of a card in the queue, at another path: linked as it says (A8)
    put("CLAIM_two.md", card("the count, filed again", cid="refiles %s" % q1, h="eeeeeeeeeeeeeeee", d="ffffffffffffffff"))
    v3, _ = _discover(new, [("a", "origin/seat/a")], tmp_path, seen_blobs=seen)
    two = [r for r in v3.values() if r["card_path"].endswith("CLAIM_two.md")][0]
    assert two["refiles"] == [q1] and "does not declare" not in two["history"][0]["note"]
    # the same script and decisive lines on another branch, undeclared: linked, and the note says so
    put("CLAIM_three.md", card("the same lines", code=B, br="seat/b"), on="seat/b")
    v4, _ = _discover(new, [("b", "origin/seat/b")], tmp_path, seen_blobs=seen)
    three = [r for r in v4.values() if r["card_path"].endswith("CLAIM_three.md")][0]
    assert three["refiles"] == [q1] and "does not declare" in three["history"][0]["note"]


def test_one_cards_text_on_two_branches_is_two_cards(tmp_path):
    g, put, card, base = _repo(tmp_path)
    put("CLAIM_one.md", card("a count"))
    g("checkout", "-q", "-b", "seat/c", base)
    text = card("a count").replace("seat/a,", "seat/c,")
    put("CLAIM_one.md", text, on="seat/c")
    new, _ = _discover({}, [("a", "origin/seat/a"), ("c", "origin/seat/c")], tmp_path)
    assert sorted(r["branch"] for r in new.values()) == ["seat/a", "seat/c"]


def test_mains_own_cards_are_found_first_and_a_declared_heavy_card_is_filed_heavy(tmp_path):
    g, put, card, base = _repo(tmp_path, branch="main")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "HARVEST_LEDGER.md").write_text(
        "# x\n\n## Pins\n\n| seat | branch | pin | pinned at | by arc |\n|---|---|---|---|---|\n"
        "| a | `origin/seat/a` | `0000000` | 2026-11-26 | B1 |\n\n## Next\n", encoding="utf-8")
    put("CLAIM_main.md", card("main's own", code=QS.MAIN_CODE, heavy=", heavy"))
    refs = D.branches(root=tmp_path)
    assert refs[0] == ("main", "origin/main") and ("a", "origin/seat/a") in refs
    new, _ = _discover({}, refs[:1], tmp_path)
    (rec,) = new.values()
    assert rec["seat_code"] == QS.MAIN_CODE and rec["branch"] == "main" and rec["heavy"] is True


def test_a_masked_ref_is_read_only_in_its_masked_segment(tmp_path):
    g, put, card, base = _repo(tmp_path)
    g("update-ref", "refs/remotes/origin/lane/the-branch-x1", "HEAD")
    g("update-ref", "refs/remotes/origin/sm2/banking", "HEAD")
    assert D.resolve(tmp_path, "origin/<v>/the-branch-x1") == "origin/lane/the-branch-x1"
    assert D.resolve(tmp_path, "origin/<v>/no-such") == "origin/<v>/no-such"
    assert D.resolve(tmp_path, "origin/sm/banking") == "origin/sm/banking"            # C21: never sm2's branch
    g("update-ref", "refs/remotes/origin/sm/banking", "HEAD")
    assert D.resolve(tmp_path, "origin/<v>/banking") == "origin/<v>/banking"          # two match: none is taken


def test_a_card_that_names_a_vendor_is_not_filed_and_the_others_are(tmp_path):
    """Review 88's A9: discovery's own check holds the gate's vendor rule"""
    g, put, card, base = _repo(tmp_path)
    vendor = D._load("gates_for_the_vendor_test", ROOT / "scripts" / "gates" / "gates.py")._VENDOR_TOKS[0]
    put("CLAIM_one.md", card("a count"))
    put("CLAIM_named.md", card("a count by " + vendor))
    new, report = _discover({}, [("a", "origin/seat/a")], tmp_path)
    assert [r["card_path"] for r in new.values()] == ["relays/claims/CLAIM_one.md"]
    assert any("CLAIM_named.md: not filed, its record would not hold the queue's schema" in r for r in report)


def test_a_masked_pins_row_is_read_and_an_unreadable_row_is_reported_m66(tmp_path):
    g, put, card, base = _repo(tmp_path, branch="main")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "HARVEST_LEDGER.md").write_text(
        "# x\n\n## Pins\n\n| seat | branch | pin | pinned at | by arc |\n|---|---|---|---|---|\n"
        "| sm | `origin/<v>/the-derivation-x1` | `0000000` | 2026-11-26 | B1 |\n"
        "| old | `<remote>/the-old-branch` | `0000000` | 2026-11-26 | B1 |\n\n## Next\n", encoding="utf-8")
    g("update-ref", "refs/remotes/origin/main", "HEAD")
    g("update-ref", "refs/remotes/origin/lane/the-derivation-x1", "HEAD")
    refs = dict(D.branches(root=tmp_path))
    assert refs["sm"] == "origin/lane/the-derivation-x1"
    _, report = _discover({}, [("old", refs["old"])], tmp_path)
    assert any("old (" in r and "names no origin/ ref" in r and "cannot be read" in r for r in report), report


def test_a_masked_key_of_the_seat_codes_matches_on_the_rest_and_two_matches_refuse_m66(tmp_path):
    codes = {"<v>/the-derivation-x1": "fam1-v1-unset-04", "main": QS.MAIN_CODE}
    assert D.code_for("lane/the-derivation-x1", codes, ["lane/the-derivation-x1"]) == ("fam1-v1-unset-04", None)
    code, why = D.code_for("lane/the-derivation-x1", codes, ["lane/the-derivation-x1", "other/the-derivation-x1"])
    assert code is None and "two branches" in why
    assert D.code_for("the-derivation-x1", codes, [])[0] is None
    assert D.code_for("a/b/the-derivation-x1", codes, [])[0] is None


def test_the_table_on_main_names_main_and_the_command_runs_by_hand(tmp_path):
    codes = D.seat_codes()
    assert codes.get("main") == QS.MAIN_CODE and all(not QS.code_problems(c) for c in codes.values())
    q = tmp_path / "cards"
    r = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/queue/discover.py"), "--queue", str(q), "--at", AT],
                       capture_output=True, text=True, timeout=600)
    assert r.returncode == 0 and r.stdout.strip().splitlines()[-1].endswith("new card(s)")
    assert not q.exists()


def test_harvest_debt_reports_a_pin_that_does_not_resolve_and_does_not_stop(monkeypatch):
    hd = _load("harvest_debt_under_test", "scripts/checks/harvest_debt.py")
    keys = [s["key"] for s in hd.SEATS]
    monkeypatch.setattr(hd, "read_pins", lambda text: {k: "0000000" for k in keys})
    rep = hd.run(strict=False)
    lost = [k for k, s in rep["seats"].items() if s.get("skipped") == "pin 0000000 does not resolve"]
    assert lost and all("%s: pin 0000000 does not resolve" % k in rep["integrity"] for k in lost)
    assert all("head" in s or "skipped" in s for s in rep["seats"].values())
    hd.print_report(rep)                                   # it stopped here at KeyError 'head'
