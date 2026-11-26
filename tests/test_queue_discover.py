"""2026-11-26 (the framework's thin path, patch T3; main's M54; register row P-885): discovery, scripts/queue/discover.py,
and harvest_debt.py's stop on a pin that does not resolve.

On a small repository built here: a card on a seat branch is filed FILED by the runner under the next id and holds the
queue's schema; a branch that cannot be read is reported and the others are read; a card with no seat code is not filed
and is reported; a file that is not a card is passed over; a second look files nothing new; a new version of a card, and a
card with the same decisive script on another branch, are filed as refiles of the first, the note saying whether the card
said so; a masked ref of the Pins table is read on its last segment. And harvest_debt.py reports a pin that does not
resolve as a skipped seat with its reason, where it stopped at KeyError 'head'."""
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

CARD = """# CLAIM CARD — {title}

- card id: {cid}
- seat code: {code}
- seat, branch, commit: {code}, seat/a, 0123456789abcdef0123456789abcdef01234567
- decisive script: x.py, SHA-256 {h}, depends on the standard library, run as python3 x.py, output SHA-256 0011223344556677{heavy}
- decisive lines: 1 lines marked "DECISIVE:", SHA-256 {d}
"""
AT = "2026-11-26T12:00:00Z"


def _repo(tmp_path):
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True).stdout
    g("init", "-q", "-b", "seat/a")
    claims = tmp_path / "relays" / "claims"
    claims.mkdir(parents=True)

    def put(name, text, branch="seat/a"):
        if g("symbolic-ref", "--short", "HEAD").strip() != branch:
            g("checkout", "-q", branch)
        (claims / name).write_text(text, encoding="utf-8")
        g("add", "-A")
        g("commit", "-q", "-m", name)
        return g("rev-parse", "HEAD").strip()
    return g, put


def test_a_card_is_filed_and_what_cannot_be_filed_is_reported(tmp_path):
    g, put = _repo(tmp_path)
    put("CLAIM_one.md", CARD.format(title="a count", cid="new", code="fam2-v5-high-01", h="aaaaaaaaaaaaaaaa", d="dddddddddddddddd", heavy=""))
    put("CLAIM_no_code.md", CARD.format(title="no code", cid="new", code="a seat", h="bbbbbbbbbbbbbbbb", d="dddddddddddddddd", heavy=""))
    put("NOTES.md", "# notes, not a card\n")
    new, report = D.discover({}, [("a", "seat/a"), ("gone", "origin/no-such-branch")], root=tmp_path, at=AT)
    assert list(new) == ["Q0001"]
    rec = new["Q0001"]
    assert rec["status"] == "FILED" and rec["history"][0]["by"] == "runner" and rec["refiles"] == []
    assert rec["card_path"] == "relays/claims/CLAIM_one.md" and rec["seat_code"] == "fam2-v5-high-01"
    assert rec["commit"] == g("log", "-1", "--format=%H", "--", "relays/claims/CLAIM_one.md").strip()
    assert QS.queue_problems({k: json.dumps(v) for k, v in new.items()}) == []
    assert any("gone (origin/no-such-branch): cannot be read" in r for r in report)
    assert any("CLAIM_no_code.md: not filed" in r for r in report)
    assert not any("NOTES.md" in r for r in report)


def test_a_second_look_files_nothing_and_a_refile_is_linked(tmp_path):
    g, put = _repo(tmp_path)
    put("CLAIM_one.md", CARD.format(title="a count", cid="new", code="fam2-v5-high-01", h="aaaaaaaaaaaaaaaa", d="dddddddddddddddd", heavy=""))
    new, _ = D.discover({}, [("a", "seat/a")], root=tmp_path, at=AT)
    blob = g("rev-parse", "HEAD:relays/claims/CLAIM_one.md").strip()
    again, _ = D.discover(new, [("a", "seat/a")], root=tmp_path, at=AT, seen_blobs={blob: "Q0001"})
    assert again == {}
    # a new version of the card, which does not say it refiles: linked, and the note says so
    put("CLAIM_one.md", CARD.format(title="a count, mended", cid="new", code="fam2-v5-high-01", h="cccccccccccccccc", d="dddddddddddddddd", heavy=""))
    v2, _ = D.discover(new, [("a", "seat/a")], root=tmp_path, at=AT, seen_blobs={blob: "Q0001"})
    assert v2["Q0002"]["refiles"] == ["Q0001"] and "does not declare" in v2["Q0002"]["history"][0]["note"]
    # one that says so
    put("CLAIM_one.md", CARD.format(title="a count, mended", cid="refiles Q0001", code="fam2-v5-high-01",
                                    h="cccccccccccccccc", d="dddddddddddddddd", heavy=""))
    v3, _ = D.discover(new, [("a", "seat/a")], root=tmp_path, at=AT, seen_blobs={blob: "Q0001"})
    assert v3["Q0002"]["refiles"] == ["Q0001"] and v3["Q0002"]["history"][0]["note"] == "found on its branch; refiles Q0001"
    assert QS.queue_problems({k: json.dumps(v) for k, v in {**new, **v3}.items()}) == []
    # the same decisive script, filed again from another branch under another name
    g("checkout", "-q", "-b", "seat/b")
    put("CLAIM_two.md", CARD.format(title="the count again", cid="new", code="fam3-v1-max-01", h="aaaaaaaaaaaaaaaa", d="dddddddddddddddd", heavy=""),
        branch="seat/b")
    v4, _ = D.discover(new, [("b", "seat/b")], root=tmp_path, at=AT, seen_blobs={
        g("rev-parse", "seat/b:relays/claims/CLAIM_one.md").strip(): "Q0001"})
    two = [r for r in v4.values() if r["card_path"].endswith("CLAIM_two.md")][0]
    assert two["refiles"] == ["Q0001"] and "does not declare" in two["history"][0]["note"]
    # the same script deciding another claim (other decisive lines) is not a refile (main's M57)
    put("CLAIM_three.md", CARD.format(title="another claim of the script", cid="new", code="fam3-v1-max-01",
                                      h="aaaaaaaaaaaaaaaa", d="eeeeeeeeeeeeeeee", heavy=""), branch="seat/b")
    v5, _ = D.discover(new, [("b", "seat/b")], root=tmp_path, at=AT, seen_blobs={
        g("rev-parse", "seat/b:relays/claims/CLAIM_one.md").strip(): "Q0001",
        g("rev-parse", "seat/b:relays/claims/CLAIM_two.md").strip(): "Q0002"})
    three = [r for r in v5.values() if r["card_path"].endswith("CLAIM_three.md")][0]
    assert three["refiles"] == [] and three["history"][0]["note"] == "found on its branch"


def test_mains_own_cards_are_found_and_a_declared_heavy_card_is_filed_heavy(tmp_path):
    g, put = _repo(tmp_path)
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "HARVEST_LEDGER.md").write_text(
        "# x\n\n## Pins\n\n| seat | branch | pin | pinned at | by arc |\n|---|---|---|---|---|\n"
        "| a | `origin/seat/a` | `0000000` | 2026-11-26 | B1 |\n\n## Next\n", encoding="utf-8")
    put("CLAIM_main.md", CARD.format(title="main's own", cid="new", code="fam1-v1-unset-01", h="aaaaaaaaaaaaaaaa",
                                     d="dddddddddddddddd", heavy=", heavy"))
    g("update-ref", "refs/remotes/origin/main", "HEAD")
    refs = D.branches(root=tmp_path)
    assert refs[0] == ("main", "origin/main") and ("a", "origin/seat/a") in refs
    new, _ = D.discover({}, refs[:1], root=tmp_path, at=AT)
    found = [r for r in new.values() if r["card_path"].endswith("CLAIM_main.md")]
    assert found and found[0]["seat_code"] == "fam1-v1-unset-01" and found[0]["branch"] == "main"
    assert found[0]["heavy"] is True


def test_a_masked_ref_of_the_pins_table_is_read_on_its_last_segment(tmp_path):
    g, put = _repo(tmp_path)
    put("CLAIM_one.md", CARD.format(title="a count", cid="new", code="fam2-v5-high-01", h="aaaaaaaaaaaaaaaa", d="dddddddddddddddd", heavy=""))
    g("update-ref", "refs/remotes/origin/lane/the-branch-x1", "HEAD")
    assert D.resolve(tmp_path, "origin/<v>/the-branch-x1") == "origin/lane/the-branch-x1"
    assert D.resolve(tmp_path, "origin/<v>/no-such") == "origin/<v>/no-such"
    new, _ = D.discover({}, [("x", D.resolve(tmp_path, "origin/<v>/the-branch-x1"))], root=tmp_path, at=AT)
    assert new["Q0001"]["branch"] == "lane/the-branch-x1"


def test_the_command_runs_by_hand_and_writes_nothing_unless_asked(tmp_path):
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
