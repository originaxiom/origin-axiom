"""2026-11-26 (the framework's thin path, patch T1; main's M54; register row P-885): the queue's schema and the gate
queue-schema. A card that breaks any rule of scripts/queue/queue_schema.py fails the gate, and its twin passes; each rule
is planted once; the seat code can never read as a code of the inputs scoreboard; the command runs by hand on a directory
and on a git ref."""
import copy
import importlib.util
import itertools
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


QS = _load("queue_schema_under_test", "scripts/queue/queue_schema.py")
GATES = _load("gates_for_the_queue_test", "scripts/gates/gates.py")

TWIN = {
    "id": "Q0007",
    "seat_code": "fam2-v5.5-high-01",
    "branch": "seat/frontier-2026-11-26",
    "commit": "0123456789abcdef0123456789abcdef01234567",
    "card_path": "relays/claims/CLAIM_2026-11-26_a_count.md",
    "title": "a count, reproduced",
    "status": "AT_BANKING",
    "deciding": True,
    "heavy": False,
    "refiles": [],
    "history": [
        {"at": "2026-11-26T10:00:00Z", "status": "FILED", "by": "runner", "note": "found on its branch"},
        {"at": "2026-11-26T10:20:00Z", "status": "REPRODUCED", "by": "runner", "note": "its decisive lines' hash"},
        {"at": "2026-11-26T10:21:00Z", "status": "OFFERED", "by": "main", "note": "offered by hand (the trial)"},
        {"at": "2026-11-29T10:21:00Z", "status": "AT_BANKING", "by": "runner", "note": "no peer check"},
    ],
}


def _gate(cards):
    return GATES.gate_queue_schema({k: json.dumps(v) if not isinstance(v, str) else v for k, v in cards.items()})


def _broken(change):
    card = copy.deepcopy(TWIN)
    change(card)
    return QS.card_problems(card, "Q0007", GATES._VENDOR_RE)


def test_a_card_that_breaks_the_schema_fails_the_gate_and_its_twin_passes():
    assert _gate({"Q0007": TWIN}) == (True, "ok (1 card(s) in the queue hold its schema)")
    bad = copy.deepcopy(TWIN)
    bad["history"][1]["by"] = "fam2-v5.5-high-01"                 # the intake's move made by a seat
    ok, detail = _gate({"Q0007": bad})
    assert not ok and "the runner's move" in detail


def test_each_rule_is_planted_once():
    vendor = GATES._VENDOR_TOKS[0]
    plants = {
        "fields missing": lambda c: c.pop("heavy"),
        "fields not in the schema": lambda c: c.update(score=1),
        "stands in the file": lambda c: c.update(id="Q0008"),
        "is not Q and four": lambda c: c.update(id="Q7"),
        "is not of the form": lambda c: c.update(seat_code="F1"),
        "not a branch's name": lambda c: c.update(branch="a branch"),
        "full 40-hex": lambda c: c.update(commit="0123456"),
        "not a claim card": lambda c: c.update(card_path="frontier/B1/FINDINGS.md"),
        "one line": lambda c: c.update(title="two\nlines"),
        "queue's statuses": lambda c: c.update(status="PARKED"),
        "deciding is not": lambda c: c.update(deciding="yes"),
        "heavy is not": lambda c: c.update(heavy=0),
        "refiles itself": lambda c: c.update(refiles=["Q0007"]),
        "not a list of card ids": lambda c: c.update(refiles=["B1858"]),
        "one or more moves": lambda c: c.update(history=[]),
        "opens at": lambda c: c["history"].pop(0),
        "is not a move of the queue": lambda c: c["history"].__setitem__(2, dict(c["history"][2], status="VERIFIED")),
        "goes back in time": lambda c: c["history"][3].update(at="2026-11-25T10:00:00Z"),
        "is not the history's last": lambda c: c.update(status="OFFERED"),
        "YYYY-MM-DD": lambda c: c["history"][0].update(at="2026-11-26"),
        "does not hold exactly": lambda c: c["history"][0].pop("note"),
        "by 'x'": lambda c: c["history"][2].update(by="x"),
        "names a vendor": lambda c: c["history"][2].update(note="read by " + vendor),
    }
    assert _broken(lambda c: None) == []
    for words, change in plants.items():
        bad = _broken(change)
        assert bad and any(words in b for b in bad), (words, bad)


def test_the_queue_as_a_whole():
    other = dict(copy.deepcopy(TWIN), id="Q0009", refiles=["Q0007"])
    assert QS.queue_problems({"Q0007": json.dumps(TWIN), "Q0009": json.dumps(other)}) == []
    assert any("not in the queue" in b for b in QS.queue_problems({"Q0009": json.dumps(other)}))
    assert any("stands twice" in b for b in QS.queue_problems({"Q0007": json.dumps(TWIN), "Q0008": json.dumps(TWIN)}))
    assert any("not JSON" in b for b in QS.queue_problems({"Q0007": "{"}))


def test_a_seat_code_never_reads_as_a_scoreboard_code():
    """the form leaves no room for one: every code of the form, over every family, version and effort, is clean; and
    the second check catches one if the form is ever widened"""
    for fam, ver, effort, n in itertools.product(range(100), ("1", "4", "5.5", "12.10"),
                                                 ("low", "medium", "high", "xhigh", "max", "unset"), ("01", "99")):
        code = "fam%d-v%s-%s-%s" % (fam, ver, effort, n)
        assert QS.SEAT_CODE.fullmatch(code) and QS.code_problems(code) == [], code
    for code in ("F1", "A01", "S02", "LAMBDA", "I-3", "fam1-v5-high", "Fam1-v5-high-01", "fam1-v5-turbo-01"):
        assert QS.code_problems(code), code
    form = QS.SEAT_CODE
    try:
        QS.SEAT_CODE = __import__("re").compile(r"[\w.-]+")
        assert QS.code_problems("fam1-F2-high-01") and QS.code_problems("I-3")
        assert QS.code_problems("fam1-v5-high-01") == []
    finally:
        QS.SEAT_CODE = form


def test_every_status_has_its_moves_and_a_returned_card_never_moves():
    assert set(QS.MOVES) == set(QS.STATUSES)
    assert all(set(v) <= set(QS.STATUSES) for v in QS.MOVES.values())
    for end in ("RETURNED_AT_INTAKE", "RETURNED", "REFUSED", "VERIFIED"):
        assert QS.MOVES[end] == ()


def test_the_command_runs_by_hand_on_a_directory_and_on_a_ref(tmp_path):
    d = tmp_path / "queue" / "cards"
    d.mkdir(parents=True)
    (d / "Q0007.json").write_text(json.dumps(TWIN), encoding="utf-8")
    run = lambda *a: subprocess.run([sys.executable, "-B", str(ROOT / "scripts/queue/queue_schema.py"), *a],
                                    capture_output=True, text=True)
    assert run("--dir", str(d)).returncode == 0
    (d / "notes.txt").write_text("a stray", encoding="utf-8")
    r = run("--dir", str(d))
    assert r.returncode == 1 and "not cards: notes.txt" in r.stdout
    (d / "notes.txt").unlink()
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True)
    g("init", "-q")
    g("add", "queue")
    g("commit", "-q", "-m", "a queue")
    assert QS.read_ref("HEAD", root=tmp_path) == {"Q0007": json.dumps(TWIN)}
    assert QS.queue_problems(QS.read_ref("HEAD", root=tmp_path)) == []


def test_the_gate_passes_on_the_record():
    ok, detail = GATES.gate_queue_schema()
    assert ok, detail


def _moved(*moves, seat="fam2-v5.5-high-01", deciding=True):
    """a card filed and reproduced by the runner, then the moves given as (status, by)"""
    card = copy.deepcopy(TWIN)
    card["seat_code"], card["deciding"] = seat, deciding
    card["history"] = card["history"][:2]
    for i, (status, by) in enumerate(moves):
        card["history"].append({"at": "2026-11-27T%02d:00:00Z" % i, "status": status, "by": by, "note": ""})
    card["status"] = card["history"][-1]["status"]
    return QS.card_problems(card, "Q0007")


def test_who_may_move_a_card_t1b():
    """main's M56: a peer's note sends nothing back; WITHDRAWN is the card's own seat's alone; the banking outcomes are the
    runner's; a split is main's on a seat's card and the auditor's or the author's on main's own; after FILED the card's
    own seat makes no other move; deciding is set past FILED, and true for banking"""
    own, main = "fam2-v5.5-high-01", QS.MAIN_CODE
    assert _moved(("OFFERED", "main"), ("PEERED", "fam3-v1-max-01"), ("AT_BANKING", "runner"), ("VERIFIED", "runner")) == []
    assert any("PEERED to RETURNED is not a move" in b for b in
               _moved(("OFFERED", "main"), ("PEERED", "fam3-v1-max-01"), ("RETURNED", "runner")))
    assert _moved(("OFFERED", "main"), ("WITHDRAWN", own)) == []
    assert any("WITHDRAWN is made by the card's own seat alone" in b for b in _moved(("WITHDRAWN", "main")))
    assert any("WITHDRAWN to OFFERED is not a move" in b for b in _moved(("WITHDRAWN", own), ("OFFERED", "main")))
    assert any("the card's own seat makes no move but WITHDRAWN" in b for b in _moved(("OFFERED", own)))
    assert any("the banking outcome VERIFIED is the runner's" in b for b in _moved(("AT_BANKING", "runner"), ("VERIFIED", "main")))
    assert _moved(("AT_BANKING", "runner"), ("SPLIT", "runner"), ("VERIFIED", "main")) == []
    assert any("settled by main, not 'author'" in b for b in
               _moved(("AT_BANKING", "runner"), ("SPLIT", "runner"), ("VERIFIED", "author")))
    assert _moved(("AT_BANKING", "runner"), ("SPLIT", "runner"), ("REFUSED", "auditor"), seat=main) == []
    assert any("a split on main's own card is settled by auditor or author" in b for b in
               _moved(("AT_BANKING", "runner"), ("SPLIT", "runner"), ("VERIFIED", "main"), seat=main))
    assert any("deciding is null past FILED" in b for b in _moved(("OFFERED", "main"), deciding=None))
    assert any("went to banking without deciding" in b for b in _moved(("AT_BANKING", "runner"), deciding=False))
    assert _moved(("OFFERED", "main"), deciding=False) == []
