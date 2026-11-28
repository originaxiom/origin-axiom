"""2026-11-26 (the framework's thin path, patch T8; main's M54; register row P-885): the peer note,
scripts/queue/peer_note.py, and the runner's move from OFFERED to PEERED.

On a repository built here: a producer's card is reproduced and offered by hand; a peer's note on its own branch, with its
own script, moves the card to PEERED graded "re-derived"; a peer that reruns the producer's own script is graded "reran";
a note that says reproduced while its lines differ, a note by the card's own seat, a note sighted before the offer, a note
whose script is not the one it hashes and a note whose control crashes are refused, and the card stays OFFERED. The note's
form is planted rule by rule."""
import copy
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


IN = _load("intake_for_peer_test", "scripts/queue/intake.py")
PN = IN.PN
T = _load("intake_test_helpers", "tests/test_queue_intake.py")
PEER = "fam3-v1-max-01"
PEER_SCRIPT = ("import sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\n"
               "total = sum(1 for _ in range(12))\nprint('DECISIVE: good =', total)\n")


def _g(path):
    return lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=path,
                                     capture_output=True, text=True, check=True).stdout


CODES = {"seat/a": "fam2-v5-high-01", "seat/p": PEER}


def _setup(tmp_path):
    """a producer's card, reproduced, then offered by hand; returns (repo, queue dir, the card's id, git)"""
    repo, q = tmp_path / "repo", tmp_path / "queue"
    repo.mkdir()
    g = _g(repo)
    g("init", "-q", "-b", "seat/a")
    (repo / "s_good.py").write_text(T._script("good"), encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "the script")
    stated = g("rev-parse", "HEAD").strip()           # a card names a commit before the one that adds it (M65)
    (repo / "relays" / "claims").mkdir(parents=True)
    (repo / "relays" / "claims" / "CLAIM_good.md").write_text(T._card("a count that holds", "good", stated=stated),
                                                              encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "a card")
    g("update-ref", "refs/remotes/origin/seat/a", "HEAD")
    cards, log, att, rep, st = IN.round_(q, root=repo, refs=[("a", "origin/seat/a")], codes=CODES,
                                         at="2026-11-26T12:00:00Z", limit=60, allow_static=True)
    assert st == 0
    (cid, rec), = cards.items()
    assert rec["status"] == "REPRODUCED", rep
    rec["history"].append({"at": "2026-11-26T13:00:00Z", "status": "OFFERED", "by": "main", "note": "offered by hand"})
    rec["status"] = "OFFERED"
    IN.write(q, cards, log, att)
    return repo, q, cid, g


def _note(cid, commit, script_text=PEER_SCRIPT, finding="reproduced", peer=PEER, lines=None, path="peer/p.py"):
    n, h = IN.RR.decisive(lines or "DECISIVE: good = 12\n")
    return {"card": cid, "card_commit": commit, "peer_code": peer, "finding": finding,
            "script": {"path": path, "sha256": hashlib.sha256(script_text.encode()).hexdigest()[:16],
                       "run_as": "python3 %s" % path, "control": "python3 %s --plant" % path},
            "decisive": {"lines": n, "sha256": h}, "note": "reproduced the count with code of my own"}


def _file_note(repo, g, note, script_text=PEER_SCRIPT, branch="seat/p"):
    g("checkout", "-q", "-B", branch, "seat/a")
    (repo / note["script"]["path"]).parent.mkdir(parents=True, exist_ok=True)
    (repo / note["script"]["path"]).write_text(script_text, encoding="utf-8")
    (repo / "relays" / "claims" / "peer").mkdir(parents=True, exist_ok=True)
    (repo / PN.note_path(note["card"])).write_text(json.dumps(note), encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "a peer note")
    g("update-ref", "refs/remotes/origin/%s" % branch, "HEAD")


def _round(repo, q):
    return IN.round_(q, root=repo, refs=[("a", "origin/seat/a"), ("p", "origin/seat/p")], codes=CODES,
                     at="2026-11-26T14:00:00Z", limit=60, allow_static=True)


def test_a_peer_note_with_its_own_code_moves_the_card_to_peered_re_derived(tmp_path):
    repo, q, cid, g = _setup(tmp_path)
    rec = IN.read_queue_dir(q)[0][cid]
    _file_note(repo, g, _note(cid, rec["commit"]))
    cards, log, att, report, status = _round(repo, q)
    assert status == 0, report
    peered = [e for e in cards[cid]["history"] if e["status"] == "PEERED"]
    assert peered and "graded re-derived" in peered[0]["note"]
    # T9: a deciding card goes on to banking in the same round, once its peer's note holds
    assert cards[cid]["status"] == "AT_BANKING" and cards[cid]["history"][-1]["note"] == "to banking after the peer's note"
    assert att[cid]["peer"]["other_family"] is True and att[cid]["peer"]["grade"] == "re-derived"
    assert "peer" in {e["what"] for e in IN.CU.read_log(log)[0]}
    assert IN.QS.queue_problems({k: json.dumps(v) for k, v in cards.items()}) == []


def test_a_peer_that_reruns_the_producers_script_is_graded_reran(tmp_path):
    repo, q, cid, g = _setup(tmp_path)
    rec = IN.read_queue_dir(q)[0][cid]
    same = T._script("good")
    _file_note(repo, g, _note(cid, rec["commit"], script_text=same), script_text=same)
    cards, _, att, report, _ = _round(repo, q)
    assert "PEERED" in [e["status"] for e in cards[cid]["history"]] and att[cid]["peer"]["grade"] == "reran", report


RUNS_THE_PRODUCERS = ("import subprocess, sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\n"
                      "out = subprocess.run([sys.executable, 's_good.py'], capture_output=True, text=True).stdout\n"
                      "print(out, end='')\n")
READS_A_COPY = ("import sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\n"
                "n = len(open('peer/kept.txt').read()) * 0 + 12\nprint('DECISIVE: good =', n)\n")


def test_a_peer_that_runs_the_producers_script_or_reads_a_copy_of_its_files_is_graded_reran_m71(tmp_path):
    """main's M71 point 1: a script that runs the producer's decisive script by subprocess, or reads its committed files
    under another name, shares no file by the import rule; it reran, it did not re-derive"""
    for i, (script, extra, reason) in enumerate(((RUNS_THE_PRODUCERS, {}, "names the producer's s_good.py"),
                                                (READS_A_COPY, {"kept.txt": T._script("good")}, "copied"))):
        (tmp_path / str(i)).mkdir()
        repo, q, cid, g = _setup(tmp_path / str(i))
        rec = IN.read_queue_dir(q)[0][cid]
        for name, text in extra.items():
            (repo / "peer").mkdir(exist_ok=True)
            (repo / "peer" / name).write_text(text, encoding="utf-8")
        _file_note(repo, g, _note(cid, rec["commit"], script_text=script), script_text=script)
        cards, _, att, report, _ = _round(repo, q)
        peer = att[cid]["peer"]
        assert peer["ok"] and peer["grade"] == "reran" and any(reason in r for r in peer["reach"]), (peer, report)


def test_a_peer_that_imports_the_producers_module_where_it_stands_is_graded_reran(tmp_path):
    """the import rule's own case: the producer's module at the same path on the peer's branch, imported by name, is
    neither named by its file nor a copy beside the peer's script under another name"""
    repo, q, cid, g = _setup(tmp_path)
    rec = IN.read_queue_dir(q)[0][cid]
    script = "import s_good\n"
    _file_note(repo, g, _note(cid, rec["commit"], script_text=script, path="p_root.py"), script_text=script)
    cards, _, att, report, _ = _round(repo, q)
    peer = att[cid]["peer"]
    assert peer["ok"] and peer["grade"] == "reran" and peer["reach"] == [], (peer, report)


def test_a_note_that_does_not_hold_is_refused_and_the_card_stays_offered(tmp_path):
    repo, q, cid, g = _setup(tmp_path)
    rec = IN.read_queue_dir(q)[0][cid]
    crash = PEER_SCRIPT.replace("raise SystemExit(1)", "raise RuntimeError('planted')")
    other = PEER_SCRIPT.replace("range(12)", "range(13)")
    for note, script, words in (
            (_note(cid, rec["commit"], script_text=other, lines="DECISIVE: good = 13\n"), other,
             "its decisive lines are not the card's"),
            (_note(cid, rec["commit"], peer=rec["seat_code"]), PEER_SCRIPT, "the peer is the card's own seat"),
            (dict(_note(cid, rec["commit"]), script=dict(_note(cid, rec["commit"])["script"], sha256="0" * 16)),
             PEER_SCRIPT, "is not the one the note hashes"),
            (_note(cid, rec["commit"], script_text=crash), crash, "with a traceback")):
        _file_note(repo, g, note, script_text=script)
        cards, _, _, report, _ = _round(repo, q)
        assert cards[cid]["status"] == "OFFERED" and any(words in r for r in report), (words, report)


def test_a_note_sighted_before_the_offer_is_refused(tmp_path):
    repo, q, cid, g = _setup(tmp_path)
    cards, _ = IN.read_queue_dir(q)
    rec = cards[cid]
    note = _note(cid, rec["commit"])
    _file_note(repo, g, note)
    commit = g("rev-parse", "HEAD").strip()
    early = IN.CU.sight(repo, [], "seat/p", commit, PN.note_path(cid), "peer", "2026-11-26T12:30:00Z")
    res = PN.check(repo, note, commit, "seat/p", rec, "", [early], limit=60, prefix=[], allow_static=True)
    assert not res["ok"] and any("before the card was offered" in r for r in res["reasons"])


def test_the_notes_form_is_planted_rule_by_rule():
    rec = {"id": "Q0001", "commit": "a" * 40, "seat_code": "fam2-v5-high-01"}
    good = _note("Q0001", "a" * 40)
    assert PN.form_problems(good, rec) == []
    plants = [
        (lambda n: n.pop("note"), "fields missing"),
        (lambda n: n.update(extra=1), "not in the schema"),
        (lambda n: n.update(card="B1"), "is not a card's id"),
        (lambda n: n.update(card_commit="abc"), "full 40-hex"),
        (lambda n: n.update(peer_code="a peer"), "peer_code"),
        (lambda n: n.update(finding="agrees"), "finding 'agrees'"),
        (lambda n: n["script"].pop("control"), "script is not"),
        (lambda n: n["decisive"].update(lines=0), "decisive is not"),
        (lambda n: n.update(note=""), "note is not"),
        (lambda n: n.update(card="Q0002"), "the note is for Q0002"),
        (lambda n: n.update(card_commit="b" * 40), "not at its sealed commit"),
    ]
    for change, words in plants:
        n = copy.deepcopy(good)
        change(n)
        bad = PN.form_problems(n, rec)
        assert bad and any(words in b for b in bad), (words, bad)


def _leave_a_process(tmp_path):
    """main's M70 point 3, before a peer's or a banking seat's run (M71): a card whose run leaves a detached child that
    rewrites every data file it can reach through /proc/<pid>/cwd"""
    RT = _load("rerun_tests_for_the_peer", "tests/test_queue_rerun.py")
    if not RT.SANDBOX[0]:
        return None
    RT._commit(tmp_path / "leaver", {"x.py": RT.LEAVER})
    n, d = IN.RR.decisive("DECISIVE: left = a child\n")
    res = RT._rerun(tmp_path / "leaver", RT._card(tmp_path / "leaver", n=n, d=d), prefix=RT.SANDBOX[0])
    assert res["status"] == "REPRODUCED", res
    return RT


READS_ITS_DATA = ("import sys, time\nif '--plant' in sys.argv:\n    raise SystemExit(1)\ntime.sleep(2)\n"
                  "print('DECISIVE: good =', int(open('data.txt').read()))\n")


def test_a_peers_run_after_a_card_that_leaves_a_process_is_its_own_m71(tmp_path):
    (tmp_path / "x").mkdir()
    if _leave_a_process(tmp_path / "x") is None:
        pytest.skip("no wrap on this machine")
    repo, q, cid, g = _setup(tmp_path)
    rec = IN.read_queue_dir(q)[0][cid]
    script = READS_ITS_DATA.replace("'data.txt'", "'peer/data.txt'")
    (repo / "peer").mkdir(exist_ok=True)
    (repo / "peer" / "data.txt").write_text("12", encoding="utf-8")
    _file_note(repo, g, _note(cid, rec["commit"], script_text=script), script_text=script)
    cards, _, att, report, _ = _round(repo, q)
    assert att[cid]["peer"]["ok"] and any(e["status"] == "PEERED" for e in cards[cid]["history"]), (att[cid], report)
