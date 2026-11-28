"""2026-11-28 (the framework's thin path; register row P-885; main's M83): a heavy card's path to the queue.

A heavy card (sage or GAP, or declared heavy) is not rerun on the workflow. On the author's machine,
`rerun.py --heavy-result Q<nnnn>` reruns it at its sealed commit with the caller's PATH and writes queue/heavy/<id>.json;
main lands it; each round checks it against the card and moves the card, the runner's key alone writing the record. On
a repository built here: a heavy card waits, and says so each round; its author's result moves it to REPRODUCED, its note
naming the file and its commit; a result that does not match the card returns it; another seat's card is rerun only with
the author's word; a sage card runs with the caller's PATH."""
import importlib.util
import json
import os
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


T = _load("intake_tests_for_heavy", "tests/test_queue_intake.py")
RT = _load("rerun_tests_for_heavy", "tests/test_queue_rerun.py")
IN = T.IN
RR = IN.RR


def _g(cwd, *a):
    return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=cwd, capture_output=True,
                          text=True, check=True).stdout


def _setup(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir(parents=True)
    T._repo(repo)
    main = tmp_path / "main"                          # main's checkout, where the author's result files land
    main.mkdir()
    _g(main, "init", "-q", "-b", "main")
    _g(main, "commit", "-q", "--allow-empty", "-m", "main")
    return repo, main


def _round(tmp_path, repo, main, at=T.AT):
    out = IN.round_(tmp_path / "q", root=repo, refs=[("a", "origin/seat/a")], codes=T.CODES, at=at, limit=60,
                    allow_static=True, heavy_root=main)
    IN.write(tmp_path / "q", out[0], out[1], out[2])
    return out


def _heavy(cards):
    (cid, rec), = [(k, v) for k, v in cards.items() if v["card_path"].endswith("CLAIM_heavy.md")]
    return cid, rec


def _land(main, cid, result):
    (main / "queue" / "heavy").mkdir(parents=True, exist_ok=True)
    (main / "queue" / "heavy" / ("%s.json" % cid)).write_text(json.dumps(result), encoding="utf-8")
    _g(main, "add", "-A")
    _g(main, "commit", "-q", "-m", "the author's heavy result for %s" % cid)
    return _g(main, "rev-parse", "--short", "HEAD").strip()


def test_a_heavy_card_waits_saying_so_and_moves_on_its_authors_result_m83(tmp_path):
    repo, main = _setup(tmp_path)
    cards, _, _, report, status = _round(tmp_path, repo, main)
    cid, rec = _heavy(cards)
    assert status == 0 and rec["status"] == "FILED" and rec["heavy"] is True
    line = "%s HEAVY, waits for the author's machine: no queue/heavy/%s.json on main yet" % (cid, cid)
    assert line in report, report
    cards, _, _, report, _ = _round(tmp_path, repo, main, at="2026-11-26T13:00:00Z")
    assert line in report                              # every round says it, until the result lands
    result, why = RR.heavy_result(repo, rec, limit=60, author_allows=True)
    assert why is None and result["status"] == "REPRODUCED" and result["control_exit"] == 1
    assert result["card"] == cid and result["commit"] == rec["commit"] and "sage" in result["versions"]
    commit = _land(main, cid, result)
    cards, _, att, report, _ = _round(tmp_path, repo, main, at="2026-11-26T14:00:00Z")
    rec = cards[cid]
    assert rec["status"] == "REPRODUCED" and rec["history"][-1]["by"] == "runner", report
    assert rec["history"][-1]["note"].startswith("the author's heavy rerun, queue/heavy/%s.json at %s:" % (cid, commit))
    assert rec["deciding"] is True and att[cid]["heavy_result"]["problems"] == []
    assert "%s REPRODUCED from the author's heavy rerun (deciding: True)" % cid in report
    assert IN.QS.queue_problems({k: json.dumps(v) for k, v in cards.items()}) == []


def test_a_result_that_does_not_match_its_card_returns_it_m83(tmp_path):
    repo, main = _setup(tmp_path / "base")
    cards, *_ = _round(tmp_path / "base", repo, main)
    cid, rec = _heavy(cards)
    good, _ = RR.heavy_result(repo, rec, limit=60, author_allows=True)
    text = IN._card_text(repo, rec)
    assert IN.heavy_problems(rec, good, text) == []
    for change, words in ((dict(commit="0" * 40), "its commit is"), (dict(card="Q9999"), "its card is"),
                          (dict(script={"path": "s_heavy.py", "sha256": "0" * 16}), "is not the card's"),
                          (dict(decisive={"lines": 1, "sha256": "0" * 16}), "its decisive lines"),
                          (dict(status="RETURNED_AT_INTAKE", reasons=["the decisive lines differ"]), "did not reproduce it"),
                          (dict(control_exit=0), "its failing control exited 0"), (dict(extra=1), "holds exactly")):
        assert any(words in b for b in IN.heavy_problems(rec, dict(good, **change), text)), (change, words)
    # through a round: the card is returned, with the reasons
    _land(main, cid, dict(good, decisive={"lines": 1, "sha256": "0" * 16}))
    cards, _, att, report, _ = _round(tmp_path / "base", repo, main, at="2026-11-26T14:00:00Z")
    assert cards[cid]["status"] == "RETURNED_AT_INTAKE" and "the author's heavy rerun" in cards[cid]["history"][-1]["note"]


def test_another_seats_card_is_rerun_on_the_authors_machine_only_at_the_authors_word_m83(tmp_path):
    repo, main = _setup(tmp_path)
    cards, *_ = _round(tmp_path, repo, main)
    cid, rec = _heavy(cards)
    out, why = RR.heavy_result(repo, rec, limit=60)
    assert out is None and "only at the author's word (--author-allows)" in why
    cmd = [sys.executable, "-B", str(ROOT / "scripts" / "queue" / "rerun.py"), "--heavy-result", cid,
           "--queue-dir", str(tmp_path / "q"), "--root", str(repo)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 1 and "refused" in r.stdout and not (repo / "queue" / "heavy").exists()
    r = subprocess.run(cmd + ["--author-allows"], capture_output=True, text=True, timeout=300)
    written = repo / "queue" / "heavy" / ("%s.json" % cid)
    assert r.returncode == 0 and written.is_file(), r.stdout + r.stderr
    assert json.loads(written.read_text())["status"] == "REPRODUCED"
    main_card = dict(rec, seat_code=IN.QS.MAIN_CODE)
    assert RR.heavy_result(repo, main_card, limit=60)[1] is None     # main's own card needs no word


def test_a_sage_card_runs_with_the_callers_path_on_the_authors_machine_m83(tmp_path, monkeypatch):
    """a stand-in for sage on the caller's PATH: the workflow's own runs never see it, the author's heavy rerun does"""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (bin_dir / "sage").write_text('#!/bin/sh\nif [ "$1" = "--version" ]; then echo "SageMath version 10.0, a stand-in"; '
                                  'exit 0; fi\nexec %s "$@"\n' % sys.executable)
    os.chmod(bin_dir / "sage", 0o755)
    repo = tmp_path / "s"
    script = "import sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\nprint('DECISIVE: good = 12')\n"
    RT._commit(repo, {"x.sage": script})
    n, d = RR.decisive("DECISIVE: good = 12\n")
    card = RT._card(repo, script="x.sage", cmd="sage x.sage", control="sage x.sage --plant", n=n, d=d)
    commit = _g(repo, "rev-parse", "HEAD").strip()
    assert RR.rerun(repo, commit, card, limit=60, allow_static=True)["status"] == "HEAVY"
    monkeypatch.setenv("PATH", "%s:%s" % (bin_dir, os.environ["PATH"]))
    res = RR.rerun(repo, commit, card, limit=60, heavy=True)
    assert res["status"] == "REPRODUCED" and res["guard"].startswith("none: the author's machine"), res
    assert RR.tool_versions()["sage"] == "SageMath version 10.0, a stand-in"


def test_main_s_gitignore_lets_a_heavy_result_be_committed():
    r = subprocess.run(["git", "check-ignore", "-q", "--no-index", "queue/heavy/Q0006.json"], cwd=ROOT, capture_output=True)
    assert r.returncode == 1
