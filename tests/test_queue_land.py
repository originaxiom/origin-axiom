"""2026-11-27 (the framework's thin path, patch T11; draft 1 §§ 4 and 9; BANKING_PROTOCOL Part I; register row P-885): the
landing tool, scripts/queue/land.py.

On a repository built here, standing for main, with a queue's branch: a card the queue holds VERIFIED lands on a fresh
clone, its arc's number and its harvest row's taken at landing, the arc, its lock, the log pair and the row written, and
nothing pushed. Refused, each with its twin passing: a card not VERIFIED, a VERIFIED made by hand, a card landed before, a
new failing test, a new red gate, a suite that did not run, and a landing whose form fails. Two landings at once: the second
waits on the lock."""
import importlib.util
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("land_under_test", ROOT / "scripts" / "queue" / "land.py")
L = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True
spec.loader.exec_module(L)

SUITE = L.SUITE + " tests"
ENV = {"GIT_AUTHOR_NAME": "a", "GIT_AUTHOR_EMAIL": "a@example.org", "GIT_COMMITTER_NAME": "a",
       "GIT_COMMITTER_EMAIL": "a@example.org"}
GATES = ("import pathlib\nROOT = pathlib.Path(__file__).resolve().parents[2]\n"
         "GATES = {'no-bad-file': lambda: (not list(ROOT.glob('frontier/*/BAD')), 'a file named BAD')}\n")


def _g(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True).stdout


BT = None


def _banking_tests():
    global BT
    if BT is None:
        s = importlib.util.spec_from_file_location("banking_tests_for_landing", ROOT / "tests" / "test_queue_banking.py")
        BT = importlib.util.module_from_spec(s)
        s.loader.exec_module(BT)
    return BT


def _origin(tmp_path, monkeypatch):
    """a repository standing for main: a producer's card banked by two sealed ACCEPTs through the runner (T9's own test
    path), its branches kept; `main` with the record's files and the banking seats; `queue` with the runner's folder, and
    three records more: Q0002 at banking, Q0003 with a VERIFIED appended by hand in the runner's words and no verdicts
    behind it (main's M72), Q0004 with a VERIFIED by main"""
    bt = _banking_tests()
    (tmp_path / "b").mkdir()
    rec, att, report = bt._bank(tmp_path / "b", {"V1": "ACCEPT", "V2": "ACCEPT"})
    assert rec["status"] == "VERIFIED" and rec["id"] == "Q0001", report
    for k, v in ENV.items():
        monkeypatch.setenv(k, v)
    o, q = tmp_path / "b" / "repo", tmp_path / "b" / "queue"
    files = {
        "CHANGELOG.md": "# Changelog\n\n## AN OLD ENTRY (2026-11-01)\n\nold.\n",
        "PROGRESS_LOG.md": "# Progress\n\n## 2026-11-01 — old\n\nold.\n",
        "docs/HARVEST_LEDGER.md": "# Harvest\n\n| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition "
                                  "| main arc | date |\n|---|---|---|---|---|---|---|---|\n"
                                  "| 6 | s | a | b | c | d | B3 | 2026-11-01 |\n| 7 | s | a | b | c | d | B3 | 2026-11-01 |\n\n"
                                  "## Pins\n\n| seat | branch | pin | pinned at | by arc |\n|---|---|---|---|---|\n"
                                  "| sa | `origin/seat/a` | `abcdef1` | 2026-11-27 | B3 |\n",
        "docs/POINT_REGISTER.md": "| P-1 | 2026-11-01 | a debt |\n",
        "queue/KNOWN_FAILURES.json": json.dumps({"note": "n", "gates": [], "tests": [
            {"id": "tests/test_known.py::test_known", "row": "P-1", "why": "a standing debt"}]}),
        "queue/BANKING_SEATS.json": json.dumps(bt.SEATS),
        "tests/test_known.py": "def test_known():\n    assert False\n",
        "tests/test_fine.py": "def test_fine():\n    assert True\n",
        "scripts/gates/gates.py": GATES,
        "frontier/B0003_a/FINDINGS.md": "a\n",
        "frontier/an_arc_renamed/arc_verdict.json": json.dumps({"id": "B12"}),     # its number in its verdict alone
    }
    _g(o, "checkout", "-q", "--orphan", "main")
    _g(o, "rm", "-rqf", "--cached", ".")
    _g(o, "clean", "-qfdx")
    for rel, text in files.items():
        (o / rel).parent.mkdir(parents=True, exist_ok=True)
        (o / rel).write_text(text, encoding="utf-8")
    _g(o, "add", "-A")
    _g(o, "commit", "-q", "-m", "main")
    _g(o, "checkout", "-q", "--orphan", "queue")
    _g(o, "rm", "-rqf", "--cached", ".")
    _g(o, "clean", "-qfdx")
    import shutil
    shutil.copytree(q, o / "queue")
    good = json.loads((o / "queue" / "cards" / "Q0001.json").read_text())
    for cid, status, by in (("Q0002", "AT_BANKING", "runner"), ("Q0003", "VERIFIED", "runner"), ("Q0004", "VERIFIED", "main")):
        r = json.loads(json.dumps(good), object_hook=None)
        r["id"], r["history"] = cid, [e for e in good["history"] if e["status"] != "VERIFIED"]
        if status == "VERIFIED":
            r["history"].append({"at": "2026-11-27T12:00:00Z", "status": "VERIFIED", "by": by,
                                 "note": "the banking verdicts: ACCEPT and ACCEPT"})
        r["status"] = status
        (o / "queue" / "cards" / ("%s.json" % cid)).write_text(json.dumps(r), encoding="utf-8")
    _g(o, "add", "queue")
    _g(o, "commit", "-q", "-m", "the queue")
    _g(o, "checkout", "-q", "-f", "main")
    _g(o, "clean", "-qfdx")
    return o


def _landing(tmp_path, name="landing", card="Q0001", lock="def test_{ARC}_holds():\n    assert 12 == 12\n", extra=None,
             verdict_id="{ARC}", slug="the_count"):
    d = tmp_path / name
    (d / "arc").mkdir(parents=True)
    (d / "LANDING.json").write_text(json.dumps({"card": card, "slug": slug, "title": "THE COUNT HOLDS ({CARD})",
                                                "progress_title": "the count holds", "message": "{ARC} the count holds"}))
    (d / "arc" / "FINDINGS.md").write_text("# {ARC}: the count holds\n\nThe card {CARD}, row {ROW}.\n")
    (d / "arc" / "arc_verdict.json").write_text(json.dumps({"id": verdict_id, "verdict": "PROVED"}))
    (d / "lock.py").write_text(lock)
    (d / "changelog.md").write_text("- the count, banked as {ARC}.\n")
    (d / "progress.md").write_text("**What happened.** The count holds.\n")
    for rel, text in (extra or {}).items():
        (d / rel).write_text(text)
    return d


def _land(tmp_path, o, d, name="w", **kw):
    (tmp_path / name).mkdir()
    return L.land(d, source=o, work=tmp_path / name, at="2026-11-27", suite=kw.pop("suite", SUITE),
                  lock=tmp_path / "landing.lock", **kw)


def test_a_verified_card_lands_on_a_fresh_clone_with_its_numbers_taken_at_landing_and_nothing_pushed(tmp_path, monkeypatch):
    o = _origin(tmp_path, monkeypatch)
    head = _g(o, "rev-parse", "main")
    status, report, clone = _land(tmp_path, o, _landing(tmp_path))
    assert status == 0, report
    assert "the numbers taken at landing: arc B13, harvest row 8" in report
    assert any(r.startswith("ready: nothing is pushed") for r in report)
    assert _g(o, "rev-parse", "main") == head                              # the tool never pushes
    arc = clone / "frontier" / "B13_the_count"
    assert json.loads((arc / "arc_verdict.json").read_text())["id"] == "B13"
    assert (arc / "FINDINGS.md").read_text() == "# B13: the count holds\n\nThe card Q0001, row 8.\n"
    assert (clone / "tests" / "test_b13_the_count.py").read_text().startswith("def test_B13_holds")
    cl = (clone / "CHANGELOG.md").read_text()
    assert cl.startswith("# Changelog\n\n## THE COUNT HOLDS (Q0001) (B13; queue card Q0001) (2026-11-27)\n\n- the count, banked")
    assert (clone / "PROGRESS_LOG.md").read_text().endswith("## 2026-11-27 — the count holds (B13)\n\n"
                                                             "**What happened.** The count holds.\n")
    rows = [l for l in (clone / "docs" / "HARVEST_LEDGER.md").read_text().splitlines() if l.startswith("| ")]
    cells = [c.strip() for c in rows[3].strip("|").split("|")]             # main's M72 point 2: the ledger's eight cells
    assert len(cells) == 8 and cells[:4] == ["8", "sa (fam2-v5-high-01)", "THE COUNT HOLDS (Q0001)", '"a count that holds"']
    assert cells[4].startswith("relays/claims/CLAIM_good.md @ ") and cells[5].startswith("**VERIFIED**")
    assert cells[6:] == ["B13", "2026-11-27"]
    assert rows[4].startswith("| seat | branch |")                         # the row joins the table, not the Pins
    assert "the VERIFIED derived again from both sealed verdicts (their reruns are the runner's)" in report
    assert _g(clone, "rev-list", "--count", "origin/main..HEAD").strip() == "1"
    assert _g(clone, "log", "-1", "--format=%s").strip() == "B13 the count holds"
    # landed and pushed, the card cannot land again, and the next landing would take the next numbers
    _g(o, "fetch", "-q", str(clone), "HEAD")                               # as main's push would
    _g(o, "reset", "-q", "--hard", "FETCH_HEAD")
    assert L.numbers(o) == (14, 9)
    status, report, _ = _land(tmp_path, o, _landing(tmp_path, "again"), "w2")
    assert status == 1 and any("is landed already" in r for r in report), report


def test_a_card_not_verified_or_verified_by_hand_or_missing_is_refused_m72(tmp_path, monkeypatch):
    """main's M72 point 1: Q0003's VERIFIED is appended by hand in the runner's words; no sealed verdict bears it out"""
    o = _origin(tmp_path, monkeypatch)
    for i, (card, why) in enumerate((("Q0002", "is AT_BANKING, not VERIFIED"), ("Q0004", "not the runner's move"),
                                     ("Q0009", "holds no card Q0009"),
                                     ("Q0003", "not borne out by the sealed verdicts: V1's verdict, derived again: no verdict"))):
        status, report, _ = _land(tmp_path, o, _landing(tmp_path, "l%d" % i, card=card), "w%d" % i)
        assert status == 1 and any(why in r for r in report), report
    # both verdicts hold, but the outcome rule does not give VERIFIED (here, as if the seats had split)
    monkeypatch.setattr(L.BK, "outcome", lambda *a, **k: ("SPLIT", "the banking verdicts: ACCEPT and REFUSE"))
    status, report, _ = _land(tmp_path, o, _landing(tmp_path, "split"), "wsplit")
    assert status == 1 and any("derived again, give SPLIT, not VERIFIED" in r for r in report), report


def test_a_new_failure_or_a_new_red_gate_refuses_the_landing_and_the_known_one_does_not(tmp_path, monkeypatch):
    o = _origin(tmp_path, monkeypatch)
    status, report, clone = _land(tmp_path, o, _landing(tmp_path, "f", lock="def test_{ARC}_holds():\n    assert 1 == 2\n"), "wf")
    assert status == 1 and any("new against queue/KNOWN_FAILURES.json: test tests/test_b13_the_count.py::test_B13_holds"
                               in r for r in report), report
    assert any("the clone is left to be read" in r for r in report)
    status, report, _ = _land(tmp_path, o, _landing(tmp_path, "g", extra={"arc/BAD": "x"}), "wg")
    assert status == 1 and any("gate no-bad-file" in r for r in report), report
    status, report, _ = _land(tmp_path, o, _landing(tmp_path, "s"), "ws", suite="python3 -c pass")
    assert status == 1 and any("the suite did not run to its end" in r for r in report), report


def test_the_landings_form_is_checked(tmp_path, monkeypatch):
    o = _origin(tmp_path, monkeypatch)
    d = _landing(tmp_path, "nofind")
    (d / "arc" / "FINDINGS.md").unlink()
    assert any("no arc/FINDINGS.md" in b for b in L.read_landing(d)[1])
    assert any("lower_snake_case" in b for b in L.read_landing(_landing(tmp_path, "slug", slug="The-Count"))[1])
    d = _landing(tmp_path, "link")
    os.symlink("/etc/hostname", d / "arc" / "host")
    assert any("symbolic link" in b for b in L.read_landing(d)[1])
    d = _landing(tmp_path, "keys")
    (d / "LANDING.json").write_text(json.dumps({"card": "Q0001"}))
    assert any("holds exactly" in b for b in L.read_landing(d)[1])
    assert L.read_landing(_landing(tmp_path, "good"))[1] == []
    status, report, _ = _land(tmp_path, o, _landing(tmp_path, "vid", verdict_id="B999"), "wv")
    assert status == 1 and any("does not name its id as {ARC}" in r for r in report), report


def test_a_second_landing_waits_on_the_lock(tmp_path, monkeypatch):
    o = _origin(tmp_path, monkeypatch)
    (tmp_path / "landing.lock").write_text("1\n")
    status, report, clone = _land(tmp_path, o, _landing(tmp_path))
    assert status == 2 and clone is None and "another landing holds the lock" in report[0]
    assert (tmp_path / "landing.lock").exists()                           # the other landing's lock is not taken away
    (tmp_path / "landing.lock").unlink()
    status, report, _ = _land(tmp_path, o, _landing(tmp_path, "l2"), "w2")
    assert status == 0, report
    assert not (tmp_path / "landing.lock").exists()                       # and a landing releases its own


def test_by_hand(tmp_path, monkeypatch):
    o = _origin(tmp_path, monkeypatch)
    cmd = [sys.executable, "-B", str(ROOT / "scripts" / "queue" / "land.py")]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 1 and "THE PREPARED LANDING" in r.stdout
    (tmp_path / "w").mkdir()
    r = subprocess.run(cmd + ["--landing", str(_landing(tmp_path)), "--source", str(o), "--work", str(tmp_path / "w"),
                              "--at", "2026-11-27", "--suite", SUITE, "--lock", str(tmp_path / "landing.lock")],
                       capture_output=True, text=True)
    assert r.returncode == 0 and "arc B13, harvest row 8" in r.stdout and "ready: nothing is pushed" in r.stdout, r.stdout
