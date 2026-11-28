"""2026-11-26 (the framework's thin path, patch T9; main's M54 to M56; register row P-885): the banking verdict files,
scripts/queue/banking.py, and the runner's banking moves.

On a repository built here, a card at banking, and two banking seats on their own branches, each filing its expectation
and its seal in one round and its verdict in a later one: two ACCEPTs make the card VERIFIED; an ACCEPT and a REFUSE make
it SPLIT. A verdict opened in the same round as the seals, a verdict that does not hash to its seal, and a seat whose
script is the producer's are refused, and the card stays at banking. A card of main's own with two ACCEPTs from main's
family waits for another family. The outcomes and the verdict's form are planted; no seats named, no banking."""
import copy
import hashlib
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


IN = _load("intake_for_banking_test", "scripts/queue/intake.py")
BK = IN.BK
PT = _load("peer_test_helpers", "tests/test_queue_peer_note.py")
T = PT.T
SEATS = {"V1": {"code": "fam4-v1-high-01", "branch": "seat/v1"}, "V2": {"code": "fam5-v1-high-01", "branch": "seat/v2"}}
OWN = ("import sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\n"
       "n = len([k for k in range(12)])\nprint('DECISIVE: good =', n)\n")


def _at_banking(tmp_path, seat_code=None):
    tmp_path.mkdir(parents=True, exist_ok=True)
    repo, q, cid, g = PT._setup(tmp_path)
    cards, log = IN.read_queue_dir(q)
    rec = cards[cid]
    if seat_code:                                   # main's own card: the queue's record names main's code
        rec["seat_code"] = seat_code
    rec["history"].append({"at": "2026-11-26T13:30:00Z", "status": "AT_BANKING", "by": "runner", "note": "no peer check"})
    rec["status"] = "AT_BANKING"
    IN.write(q, cards, log, {})
    seats = tmp_path / "BANKING_SEATS.json"
    seats.write_text(json.dumps(SEATS), encoding="utf-8")
    return repo, q, cid, g, seats


def _verdict(cid, commit, code, verdict="ACCEPT", script=OWN, path="bank/own.py"):
    n, h = IN.RR.decisive("DECISIVE: good = 12\n")
    v = {"card": cid, "card_commit": commit, "seat": code, "verdict": verdict,
         "reason": "recomputed the count with code of my own; it holds as filed.",
         "script": {"path": path, "sha256": hashlib.sha256(script.encode()).hexdigest()[:16],
                    "run_as": "python3 %s" % path, "control": "python3 %s --plant" % path},
         "decisive": {"lines": n, "sha256": h},
         "labels": ["recomputed independently", "expectations committed first"]}
    return json.dumps(v, indent=1).encode("utf-8")


def _put(repo, g, branch, files, base="seat/a"):
    exists = subprocess.run(["git", "rev-parse", "--verify", "-q", branch], cwd=repo, capture_output=True).returncode == 0
    g("checkout", "-q", branch) if exists else g("checkout", "-q", "-b", branch, base)
    for rel, data in files.items():
        (repo / rel).parent.mkdir(parents=True, exist_ok=True)
        (repo / rel).write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))
    g("add", "-A")
    g("commit", "-q", "-m", "banking files")
    g("update-ref", "refs/remotes/origin/%s" % branch, "HEAD")


def _round(repo, q, seats, at):
    refs = [("a", "origin/seat/a")] + [(v, "origin/" + s["branch"]) for v, s in SEATS.items()]
    out = IN.round_(q, root=repo, refs=refs, codes=PT.CODES, at=at, limit=60, allow_static=True, seats_file=seats)
    IN.write(q, out[0], out[1], out[2])
    return out


def _bank(tmp_path, verdicts, same_round=False, scripts=None, seal_of=None, seat_code=None, expect_late=(), extra=None):
    """seals and expectations in one round, the verdicts in the next (or in the same, when same_round)"""
    repo, q, cid, g, seats = _at_banking(tmp_path, seat_code)
    commit = IN.read_queue_dir(q)[0][cid]["commit"]
    files = {}
    for v, s in SEATS.items():
        script = (scripts or {}).get(v, OWN)
        data = _verdict(cid, commit, s["code"], verdicts[v], script=script)
        files[v] = data
        p = BK.paths(cid)
        seal = hashlib.sha256((seal_of or {}).get(v, data)).hexdigest()
        first = {p["seal"]: seal + "\n", "bank/own.py": script, **(extra or {}).get(v, {})}
        if v not in expect_late:
            first[p["expect"]] = "I expect twelve classes.\n"
        _put(repo, g, s["branch"], first)
    if not same_round:
        _round(repo, q, seats, "2026-11-26T15:00:00Z")
    for v, s in SEATS.items():
        later = {BK.paths(cid)["verdict"]: files[v]}
        if v in expect_late:
            later[BK.paths(cid)["expect"]] = "I expect twelve classes, written after the seal.\n"
        _put(repo, g, s["branch"], later)
    cards, _, att, report, status = _round(repo, q, seats, "2026-11-26T18:00:00Z")
    assert status == 0, report
    return cards[cid], att.get(cid, {}), report


def test_two_accepts_bank_and_an_accept_beside_a_refuse_is_a_split(tmp_path):
    rec, att, report = _bank(tmp_path / "a", {"V1": "ACCEPT", "V2": "ACCEPT"})
    assert rec["status"] == "VERIFIED" and rec["history"][-1]["by"] == "runner", report
    assert all(g["ok"] for g in att["banking"].values())
    rec, _, report = _bank(tmp_path / "b", {"V1": "ACCEPT", "V2": "REFUSE"})
    assert rec["status"] == "SPLIT", report


def test_a_verdict_that_does_not_hold_is_refused_and_the_card_stays_at_banking(tmp_path):
    rec, _, report = _bank(tmp_path / "blind", {"V1": "ACCEPT", "V2": "ACCEPT"}, same_round=True)
    assert rec["status"] == "AT_BANKING" and any("before both seals were in (K1)" in r for r in report), report
    rec, _, report = _bank(tmp_path / "seal", {"V1": "ACCEPT", "V2": "ACCEPT"}, seal_of={"V2": b"another verdict"})
    assert rec["status"] == "AT_BANKING" and any("does not hash to its seal" in r for r in report), report
    rec, _, report = _bank(tmp_path / "k3", {"V1": "ACCEPT", "V2": "ACCEPT"}, expect_late=("V1",))
    assert rec["status"] == "AT_BANKING" and any("sighted after the seal (K3)" in r for r in report), report
    rec, _, report = _bank(tmp_path / "k2", {"V1": "ACCEPT", "V2": "ACCEPT"}, scripts={"V1": T._script("good")})
    assert rec["status"] == "AT_BANKING" and any("shares a file with the producer's (K2)" in r for r in report), report


def test_a_card_of_mains_own_waits_for_another_family(tmp_path):
    main_family = {"V1": {"code": "fam1-v2-high-01", "branch": "seat/v1"}, "V2": {"code": "fam1-v2-high-02",
                                                                                 "branch": "seat/v2"}}
    rec = {"seat_code": IN.QS.MAIN_CODE}
    assert BK.outcome(rec, "ACCEPT", "ACCEPT", False, main_family)[0] is None
    assert BK.outcome(rec, "ACCEPT", "ACCEPT", True, main_family)[0] == "VERIFIED"
    assert BK.outcome(rec, "ACCEPT", "ACCEPT", False, SEATS)[0] == "VERIFIED"
    assert BK.outcome({"seat_code": "fam2-v5-high-01"}, "ACCEPT", "ACCEPT", False, main_family)[0] == "VERIFIED"


def test_the_outcomes():
    rec = {"seat_code": "fam2-v5-high-01"}
    for pair, want in ((("ACCEPT", "ACCEPT"), "VERIFIED"), (("RETURN", "RETURN"), "RETURNED"),
                       (("REFUSE", "REFUSE"), "REFUSED"), (("RETURN", "REFUSE"), "SPLIT"), (("ACCEPT", "RETURN"), "SPLIT")):
        assert BK.outcome(rec, *pair)[0] == want, pair


def test_the_verdicts_form_and_the_seats_file(tmp_path):
    rec = {"id": "Q0001", "commit": "a" * 40, "seat_code": "fam2-v5-high-01"}
    good = json.loads(_verdict("Q0001", "a" * 40, "fam4-v1-high-01"))
    assert BK.form_problems(good, rec, "fam4-v1-high-01") == []
    for change, words in ((lambda v: v.update(verdict="CANNOT DECIDE"), "is not one of ACCEPT, RETURN, REFUSE"),
                          (lambda v: v.update(reason="one.\n\ntwo."), "one paragraph"),
                          (lambda v: v.pop("decisive"), "fields missing"),
                          (lambda v: v.update(seat="fam9-v1-high-01"), "is not the banking seat"),
                          (lambda v: v.update(card_commit="b" * 40), "at its sealed commit"),
                          (lambda v: v.update(labels=[]), "section 12's labels"),
                          (lambda v: v.update(labels=["approved"]), "section 12's labels")):
        v = copy.deepcopy(good)
        change(v)
        bad = BK.form_problems(v, rec, "fam4-v1-high-01")
        assert bad and any(words in b for b in bad), (words, bad)
    own = dict(good, seat=rec["seat_code"])
    assert any("does not bank a card of its own" in b for b in BK.form_problems(own, rec, rec["seat_code"]))
    (tmp_path / "s.json").write_text(json.dumps({"V1": {"code": None, "branch": None}}), encoding="utf-8")
    assert BK.seats(tmp_path / "s.json") == {} and BK.seats(ROOT / "queue" / "BANKING_SEATS.json") == {}
    (tmp_path / "s.json").write_text(json.dumps(SEATS), encoding="utf-8")
    assert BK.seats(tmp_path / "s.json") == SEATS


def test_an_offer_with_no_note_goes_to_banking_after_72_hours(tmp_path):
    repo, q, cid, g = PT._setup(tmp_path)                      # offered at 2026-11-26T13:00:00Z
    refs = [("a", "origin/seat/a")]
    cards, *_ = IN.round_(q, root=repo, refs=refs, codes=PT.CODES, at="2026-11-29T12:00:00Z", limit=60,
                          allow_static=True)
    assert cards[cid]["status"] == "OFFERED"                   # 71 hours
    cards, *_ = IN.round_(q, root=repo, refs=refs, codes=PT.CODES, at="2026-11-29T13:00:00Z", limit=60,
                          allow_static=True)
    assert cards[cid]["status"] == "AT_BANKING" and "no peer check" in cards[cid]["history"][-1]["note"]


def _deciding_nothing(q, cid):
    cards, log = IN.read_queue_dir(q)
    cards[cid]["deciding"] = False                  # as the record check sets it for a card that decides no row
    IN.write(q, cards, log, {})


def test_a_card_that_decides_nothing_ends_at_not_banked_after_its_peer_stage_m64(tmp_path):
    # after its peer's note
    (tmp_path / "noted").mkdir()
    repo, q, cid, g = PT._setup(tmp_path / "noted")
    _deciding_nothing(q, cid)
    PT._file_note(repo, g, PT._note(cid, IN.read_queue_dir(q)[0][cid]["commit"]))
    cards, log, att, report, status = PT._round(repo, q)
    assert status == 0, report
    assert [e["status"] for e in cards[cid]["history"]][-2:] == ["PEERED", "NOT_BANKED"], report
    assert cards[cid]["history"][-1]["by"] == "runner"
    assert IN.QS.queue_problems({k: json.dumps(v) for k, v in cards.items()}) == []
    # 72 hours after the offer, with no note
    (tmp_path / "timed").mkdir()
    repo, q, cid, g = PT._setup(tmp_path / "timed")
    _deciding_nothing(q, cid)
    refs = [("a", "origin/seat/a")]
    cards, *_ = IN.round_(q, root=repo, refs=refs, codes=PT.CODES, at="2026-11-29T12:00:00Z", limit=60,
                          allow_static=True)
    assert cards[cid]["status"] == "OFFERED"
    cards, _, _, report, _ = IN.round_(q, root=repo, refs=refs, codes=PT.CODES, at="2026-11-29T13:00:00Z", limit=60,
                                       allow_static=True)
    assert cards[cid]["status"] == "NOT_BANKED" and "no peer check" in cards[cid]["history"][-1]["note"], report
    # a deciding card is never NOT_BANKED by the runner
    (tmp_path / "deciding").mkdir()
    repo, q, cid, g = PT._setup(tmp_path / "deciding")
    cards, *_ = IN.round_(q, root=repo, refs=refs, codes=PT.CODES, at="2026-11-29T13:00:00Z", limit=60,
                          allow_static=True)
    assert cards[cid]["status"] == "AT_BANKING"


def test_a_later_rounds_check_is_added_beside_the_record_check_and_does_not_replace_it(tmp_path):
    repo, q, cid, g = PT._setup(tmp_path)
    before = json.loads((q / "checks" / ("%s.json" % cid)).read_text(encoding="utf-8"))
    assert before and "peer" not in before
    PT._file_note(repo, g, PT._note(cid, IN.read_queue_dir(q)[0][cid]["commit"]))
    cards, log, att, report, status = PT._round(repo, q)
    assert IN.write(q, cards, log, att) == []
    after = json.loads((q / "checks" / ("%s.json" % cid)).read_text(encoding="utf-8"))
    assert {k: after[k] for k in before} == before and after["peer"]["ok"] is True


def test_banking_takes_cards_in_queue_order_m64():
    assert IN.queue_order({"Q0010": {}, "Q0002": {}, "Q10000": {}, "Q9999": {}}) == ["Q0002", "Q0010", "Q9999", "Q10000"]


RUNS_THE_PRODUCERS = ("import subprocess, sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\n"
                      "print(subprocess.run([sys.executable, 's_good.py'], capture_output=True, text=True).stdout, end='')\n")
READS_A_COPY = ("import sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\n"
                "n = len(open('bank/kept.txt').read()) * 0 + 12\nprint('DECISIVE: good =', n)\n")


def test_a_seat_that_reruns_the_producers_computation_by_another_door_is_refused_m71(tmp_path):
    """main's M71 point 1: a banking seat's script that runs the producer's decisive script by subprocess, or reads its
    committed files under another name, shares no file by the import rule; K2 refuses it, and its twin, the seat's own
    computation, holds"""
    rec, att, report = _bank(tmp_path / "sub", {"V1": "ACCEPT", "V2": "ACCEPT"}, scripts={"V2": RUNS_THE_PRODUCERS})
    assert rec["status"] == "AT_BANKING" and "names the producer's s_good.py" in att["banking"]["V2"]["reasons"][0], report
    assert att["banking"]["V2"]["rerun"] is None                        # refused before anything ran
    rec, att, report = _bank(tmp_path / "copy", {"V1": "ACCEPT", "V2": "ACCEPT"}, scripts={"V2": READS_A_COPY},
                             extra={"V2": {"bank/kept.txt": T._script("good")}})
    assert rec["status"] == "AT_BANKING" and "copied" in att["banking"]["V2"]["reasons"][0], report
    rec, att, report = _bank(tmp_path / "own", {"V1": "ACCEPT", "V2": "ACCEPT"}, scripts={"V2": READS_A_COPY},
                             extra={"V2": {"bank/kept.txt": "the seat's own data\n"}})
    assert rec["status"] == "VERIFIED", report


def test_the_round_says_when_both_seals_are_in_and_verdicts_may_be_opened_m71(tmp_path):
    """main's M71 point 2: K1 refuses a verdict first sighted in the round of the last seal; the report says when that is"""
    repo, q, cid, g, seats = _at_banking(tmp_path)
    commit = IN.read_queue_dir(q)[0][cid]["commit"]
    p = BK.paths(cid)
    data = _verdict(cid, commit, SEATS["V1"]["code"])
    _put(repo, g, "seat/v1", {p["seal"]: hashlib.sha256(data).hexdigest() + "\n", p["expect"]: "twelve\n",
                              "bank/own.py": OWN})
    *_, report, _ = _round(repo, q, seats, "2026-11-26T15:00:00Z")
    assert any("%s at banking: seals sighted: V1 at 2026-11-26T15:00:00Z, V2 not yet; no verdict may be opened yet" % cid
               in r for r in report), report
    data2 = _verdict(cid, commit, SEATS["V2"]["code"])
    _put(repo, g, "seat/v2", {p["seal"]: hashlib.sha256(data2).hexdigest() + "\n", p["expect"]: "twelve\n",
                              "bank/own.py": OWN})
    *_, report, _ = _round(repo, q, seats, "2026-11-26T18:00:00Z")
    assert any("both seals first sighted by 2026-11-26T18:00:00Z; verdicts may be opened from the next round on" in r
               for r in report), report


def test_a_filed_verdict_is_checked_once_not_every_round_m71(tmp_path, monkeypatch):
    """main's M71 point 3: while one seat has filed and the other has not, every round reran the filed seat's script. Its
    check is kept by its verdict, seal and expectation and the other seal's sighting, and run again only when one changes"""
    repo, q, cid, g, seats = _at_banking(tmp_path)
    commit = IN.read_queue_dir(q)[0][cid]["commit"]
    p = BK.paths(cid)
    for v, s in SEATS.items():
        data = _verdict(cid, commit, s["code"])
        _put(repo, g, s["branch"], {p["seal"]: hashlib.sha256(data).hexdigest() + "\n", p["expect"]: "twelve\n",
                                    "bank/own.py": OWN})
    _round(repo, q, seats, "2026-11-26T15:00:00Z")
    _put(repo, g, "seat/v1", {p["verdict"]: _verdict(cid, commit, SEATS["V1"]["code"])})
    runs = []
    real = BK.RR.rerun
    monkeypatch.setattr(BK.RR, "rerun", lambda *a, **k: runs.append(1) or real(*a, **k))
    for at in ("2026-11-26T18:00:00Z", "2026-11-26T21:00:00Z", "2026-11-27T00:00:00Z"):
        cards, _, att, report, _ = _round(repo, q, seats, at)
        assert att[cid]["banking"]["V1"]["ok"] and cards[cid]["status"] == "AT_BANKING", report
    assert len(runs) == 1, runs


def test_a_verdicts_run_after_a_card_that_leaves_a_process_is_its_own_m71(tmp_path):
    (tmp_path / "x").mkdir()
    if PT._leave_a_process(tmp_path / "x") is None:
        import pytest
        pytest.skip("no wrap on this machine")
    script = PT.READS_ITS_DATA.replace("'data.txt'", "'bank/data.txt'")
    rec, att, report = _bank(tmp_path / "b", {"V1": "ACCEPT", "V2": "ACCEPT"}, scripts={"V1": script},
                             extra={"V1": {"bank/data.txt": "12"}})
    assert rec["status"] == "VERIFIED", (att, report)
