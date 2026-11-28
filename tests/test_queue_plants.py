"""2026-11-28 (the framework's thin path, patch T12; draft 1 §§ 4 and 9; docs/roles/BANKING.md; register row P-885): the
plant ledger, scripts/queue/plants.py, and the gate plant-ledger.

No plant is in this file: the ledgers here are made up for the tests, and the builder does not see main's. On a repository
built here, a ledger sealed in one commit and opened in a later one passes the gate; opened with its seal, opened with no
seal, not hashing to its seal, changed after it was opened, or with a seal line rewritten along the history, it fails.
The ledger's form is planted rule by rule. The measure gives each seat's catches over its plants, the shapes not yet
planted, and leaves out a plant whose verdicts were sighted before its seal."""
import hashlib
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


P = _load("plants_under_test", "scripts/queue/plants.py")
GATES = _load("gates_for_the_plants", "scripts/gates/gates.py")
NONCE = "ab" * 32


def _ledger(n=1, plants=None):
    return {"round": n, "nonce": NONCE, "plants": plants if plants is not None else [
        {"branch": "seat/a", "path": "relays/claims/CLAIM_count.md", "shape": "K6", "stage": "banking", "source": "main",
         "fault": "a map that matches orders and is not a homomorphism", "caught_by": ["REFUSE", "RETURN"]}]}


def _repo(tmp_path):
    tmp_path.mkdir(parents=True, exist_ok=True)

    def g(*a, at=None):
        env = dict(os.environ, **({"GIT_COMMITTER_DATE": at, "GIT_AUTHOR_DATE": at} if at else {}))
        return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                              capture_output=True, text=True, check=True, env=env).stdout
    g("init", "-q", "-b", "main")
    g("commit", "-q", "--allow-empty", "-m", "main")
    return g


def _seal(tmp_path, g, ledger, at=None, extra=""):
    raw = (json.dumps(ledger, indent=1) + "\n").encode()
    (tmp_path / "queue").mkdir(exist_ok=True)
    with open(tmp_path / P.SEALS, "a", encoding="utf-8") as f:
        f.write(P.seal_line(raw, ledger["round"]) + "\n" + extra)
    g("add", "-A")
    g("commit", "-q", "-m", "seal round %d" % ledger["round"], at=at)
    return raw


def _open(tmp_path, g, ledger, raw, at=None):
    (tmp_path / P.LEDGERS).mkdir(parents=True, exist_ok=True)
    (tmp_path / P.LEDGERS / ("ROUND_%d.json" % ledger["round"])).write_bytes(raw)
    g("add", "-A")
    g("commit", "-q", "-m", "open round %d" % ledger["round"], at=at)


def test_a_ledger_opened_with_its_seal_or_unsealed_or_changed_fails_the_gate_and_its_twin_passes(tmp_path):
    # the twin: sealed in one commit, opened in a later one
    g = _repo(tmp_path / "ok")
    raw = _seal(tmp_path / "ok", g, _ledger())
    assert P.problems(tmp_path / "ok") == []                       # sealed, not yet opened
    _open(tmp_path / "ok", g, _ledger(), raw)
    assert P.problems(tmp_path / "ok") == [] and GATES.gate_plant_ledger(tmp_path / "ok")[0] is True
    # changed after it was opened
    led = tmp_path / "ok" / P.LEDGERS / "ROUND_1.json"
    led.write_bytes(raw.replace(b"a map", b"the map"))
    ok, detail = GATES.gate_plant_ledger(tmp_path / "ok")
    assert not ok and "does not hash to round 1's seal" in detail and "not the ledger as opened" in detail
    g("commit", "-q", "-am", "the ledger changed")
    assert any("changes at" in b and "after it was opened" in b for b in P.problems(tmp_path / "ok"))
    # opened in the commit that seals it
    g = _repo(tmp_path / "same")
    raw = (json.dumps(_ledger(), indent=1) + "\n").encode()
    (tmp_path / "same" / P.LEDGERS).mkdir(parents=True)
    (tmp_path / "same" / P.LEDGERS / "ROUND_1.json").write_bytes(raw)
    (tmp_path / "same" / P.SEALS).write_text(P.seal_line(raw, 1) + "\n", encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "sealed and opened at once")
    assert any("opened in the commit that seals it" in b for b in P.problems(tmp_path / "same"))
    # opened first, and sealed after
    g = _repo(tmp_path / "before")
    raw = (json.dumps(_ledger(), indent=1) + "\n").encode()
    _open(tmp_path / "before", g, _ledger(), raw)
    (tmp_path / "before" / P.SEALS).write_text(P.seal_line(raw, 1) + "\n", encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "the seal, after the opening")
    assert any("is opened before its seal" in b for b in P.problems(tmp_path / "before"))
    # opened with no seal; and not hashing to its seal
    g = _repo(tmp_path / "none")
    _open(tmp_path / "none", g, _ledger(), (json.dumps(_ledger()) + "\n").encode())
    assert any("opened with no seal for round 1" in b for b in P.problems(tmp_path / "none"))
    g = _repo(tmp_path / "hash")
    _seal(tmp_path / "hash", g, _ledger())
    _open(tmp_path / "hash", g, _ledger(), (json.dumps(_ledger(plants=[])) + "\n").encode())
    assert any("does not hash to round 1's seal" in b for b in P.problems(tmp_path / "hash"))


def test_the_seals_are_only_appended_to_and_their_rounds_go_in_order(tmp_path):
    g = _repo(tmp_path / "a")
    raw = _seal(tmp_path / "a", g, _ledger(1))
    _open(tmp_path / "a", g, _ledger(1), raw)                         # round 1 opened before round 2 is sealed (M76)
    _seal(tmp_path / "a", g, _ledger(2))
    assert P.problems(tmp_path / "a") == []
    f = tmp_path / "a" / P.SEALS
    lines = f.read_text().splitlines()
    f.write_text(lines[1] + "\n", encoding="utf-8")                   # round 1's seal taken out
    assert any("changes a committed line" in b for b in P.problems(tmp_path / "a"))
    g("commit", "-q", "-am", "a seal taken out")
    bad = P.problems(tmp_path / "a")
    assert any("changes or takes out a line before it" in b for b in bad), bad
    assert any("is for round 2; the rounds go 1, 2, 3" in b for b in bad), bad
    g = _repo(tmp_path / "b")
    _seal(tmp_path / "b", g, _ledger(1), extra=json.dumps({"round": 3, "sha256": "0" * 64}) + "\n")
    assert any("is for round 3" in b for b in P.problems(tmp_path / "b"))
    seals, bad = P.read_seals('{"round": 1, "sha256": "x"}\nnot json\n')
    assert len(bad) == 2 and seals == []


def test_the_ledgers_form_is_planted_rule_by_rule():
    assert P.ledger_problems(_ledger(), 1) == [] and P.ledger_problems(_ledger(plants=[]), 1) == []
    good = _ledger()["plants"][0]
    plants = {
        "its round is a number from 1": dict(_ledger(), round=0),
        "it says round 1 and its file says 2": _ledger(),
        "its nonce is 64 hex digits": dict(_ledger(), nonce="short"),
        "holds exactly round, nonce and plants": dict(_ledger(), extra=1),
        "its shape is one of": _ledger(plants=[dict(good, shape="K3")]),       # K3 is the verdict files' custody, not a plant
        "its stage is one of": _ledger(plants=[dict(good, stage="intake")]),
        "its source is one of": _ledger(plants=[dict(good, source="a seat")]),
        "its fault is one line": _ledger(plants=[dict(good, fault="two\nlines")]),
        "caught_by is a list of": _ledger(plants=[dict(good, caught_by=["ACCEPT"])]),
        "its path is a card's": _ledger(plants=[dict(good, path="docs/x.md")]),
        "its branch is a branch's name": _ledger(plants=[dict(good, branch="../x")]),
        "the same card is planted twice": _ledger(plants=[good, dict(good)]),
        "holds exactly branch": _ledger(plants=[dict(good, seat="a name")]),
    }
    for words, d in plants.items():
        bad = P.ledger_problems(d, 2 if words.startswith("it says round") else 1)
        assert any(words in b for b in bad), (words, bad)
    assert set(P.SHAPES) == {"K2", "K4", "K5", "K6", "K7", "K8", "K9", "K10"}


def _queue(tmp_path, first_seen="2026-11-28T15:00:00Z"):
    q = tmp_path / "queue_dir"
    (q / "cards").mkdir(parents=True)
    (q / "checks").mkdir()
    rec = {"id": "Q0001", "branch": "seat/a", "card_path": "relays/claims/CLAIM_count.md", "status": "REFUSED",
           "history": [{"at": "2026-11-28T13:00:00Z", "status": "PEERED", "by": "runner",
                        "note": "the peer note on seat/p at abcdef123: fault, graded re-derived"}]}
    (q / "cards" / "Q0001.json").write_text(json.dumps(rec), encoding="utf-8")
    (q / "checks" / "Q0001.json").write_text(json.dumps({"banking": {
        "V1": {"ok": True, "verdict": "REFUSE"}, "V2": {"ok": True, "verdict": "ACCEPT"}}}), encoding="utf-8")
    (q / "SIGHTINGS.jsonl").write_text(json.dumps({"at": first_seen, "what": "verdict", "branch": "sm/banking",
                                                   "path": "relays/claims/banking/VERDICT_Q0001.json", "blob": "b" * 40})
                                       + "\n", encoding="utf-8")
    return q


def test_the_measure_gives_each_seats_catches_and_the_shapes_not_yet_planted(tmp_path):
    g = _repo(tmp_path / "r")
    raw = _seal(tmp_path / "r", g, _ledger(), at="2026-11-28T12:00:00+00:00")
    _open(tmp_path / "r", g, _ledger(), raw, at="2026-11-28T18:00:00+00:00")
    (tmp_path / "r" / "queue" / "BANKING_SEATS.json").write_text(json.dumps(
        {"V1": {"code": "fam1-v1-unset-04", "branch": "sm/banking"}, "V2": {"code": "fam1-v1-unset-05", "branch": "sm2/banking"}}))
    (tmp_path / "r" / "queue" / "SEAT_CODES.json").write_text(json.dumps({"codes": {"seat/p": "fam3-v1-high-01"}}))
    m = P.measure(_queue(tmp_path), root=tmp_path / "r")
    assert m["seats"] == {"fam1-v1-unset-04": [1, 1], "fam1-v1-unset-05": [0, 1], "fam3-v1-high-01": [1, 1]}, m
    assert m["plants"][0]["card"] == "Q0001" and m["late"] == []
    assert m["unplanted"] == ["K2", "K4", "K5", "K7", "K8", "K9", "K10"] and m["rounds_sealed"] == 1
    # a verdict sighted before the round's seal: sealed late, and not counted
    late = P.measure(_queue(tmp_path / "late", first_seen="2026-11-28T11:00:00Z"), root=tmp_path / "r")
    assert late["seats"] == {} and len(late["late"]) == 1 and "sealed late" in late["plants"][0]["note"]


def test_the_commands_by_hand_and_the_gate_on_the_record(tmp_path):
    led = tmp_path / "ROUND_1.json"
    raw = (json.dumps(_ledger(), indent=1) + "\n").encode()
    led.write_bytes(raw)
    cmd = [sys.executable, "-B", str(ROOT / "scripts" / "queue" / "plants.py")]
    r = subprocess.run(cmd + ["--seal", str(led)], capture_output=True, text=True)
    assert r.returncode == 0 and json.loads(r.stdout) == {"round": 1, "sha256": hashlib.sha256(raw).hexdigest()}
    led.write_text(json.dumps(dict(_ledger(), nonce="x")))
    assert subprocess.run(cmd + ["--seal", str(led)], capture_output=True, text=True).returncode == 1
    r = subprocess.run(cmd + ["--nonce"], capture_output=True, text=True)
    assert r.returncode == 0 and P.HEX64.fullmatch(r.stdout.strip())
    assert subprocess.run(cmd + ["--check"], capture_output=True, text=True).returncode == 0
    assert GATES.gate_plant_ledger()[0] is True


def test_an_opened_ledger_stays_and_a_round_is_opened_before_the_next_is_sealed_m76(tmp_path):
    """main's M76 point 2: an opened ledger deleted in a later commit passed; so did round 2 sealed, round 3 sealed and
    round 2 never opened. Each twin passes"""
    g = _repo(tmp_path / "gone")
    raw = _seal(tmp_path / "gone", g, _ledger(1))
    _open(tmp_path / "gone", g, _ledger(1), raw)
    assert P.problems(tmp_path / "gone") == []
    g("rm", "-q", "%s/ROUND_1.json" % P.LEDGERS)
    g("commit", "-q", "-m", "the ledger taken out")
    bad = P.problems(tmp_path / "gone")
    assert any("ROUND_1.json was opened and is gone" in b for b in bad), bad
    g = _repo(tmp_path / "skip")
    raw1 = _seal(tmp_path / "skip", g, _ledger(1))
    _open(tmp_path / "skip", g, _ledger(1), raw1)
    _seal(tmp_path / "skip", g, _ledger(2))
    assert P.problems(tmp_path / "skip") == []                          # round 2 sealed, its round still running
    _seal(tmp_path / "skip", g, _ledger(3))
    bad = P.problems(tmp_path / "skip")
    assert bad == ["round 3 is sealed and round 2's ledger was not opened by then"], bad


def _times(tmp_path, seal_at, open_at, seen_at, what="verdict"):
    g = _repo(tmp_path / "r")
    raw = _seal(tmp_path / "r", g, _ledger(), at=seal_at)
    _open(tmp_path / "r", g, _ledger(), raw, at=open_at)
    (tmp_path / "r" / "queue" / "BANKING_SEATS.json").write_text(json.dumps(
        {"V1": {"code": "fam1-v1-unset-04", "branch": "sm/banking"}, "V2": {"code": "fam1-v1-unset-05", "branch": "sm2/banking"}}))
    q = _queue(tmp_path, first_seen=seen_at)
    if what != "verdict":
        line = json.loads((q / "SIGHTINGS.jsonl").read_text())
        line.update(what=what, path="relays/claims/banking/EXPECT_Q0001.md")
        (q / "SIGHTINGS.jsonl").write_text(json.dumps(line) + "\n")
    return P.measure(q, root=tmp_path / "r")


def test_a_verdict_sighted_after_the_opening_is_opened_early_and_an_expectation_before_the_seal_is_sealed_late_m76(tmp_path):
    """main's M76 point 2, its probe: the seal at 01:00, the opening at 02:00, both verdicts first sighted at 05:00; V1's
    REFUSE was counted as a catch. An expectation is a seat's content too"""
    m = _times(tmp_path / "early", "2026-11-28T01:00:00+00:00", "2026-11-28T02:00:00+00:00", "2026-11-28T05:00:00Z")
    assert m["seats"] == {} and len(m["early"]) == 1 and m["late"] == [], m
    assert "opened early: a seat's content was sighted at 2026-11-28T05:00:00Z" in m["plants"][0]["note"]
    m = _times(tmp_path / "twin", "2026-11-28T01:00:00+00:00", "2026-11-28T09:00:00+00:00", "2026-11-28T05:00:00Z")
    assert m["seats"]["fam1-v1-unset-04"] == [1, 1] and m["early"] == [] and m["late"] == [], m
    m = _times(tmp_path / "expect", "2026-11-28T06:00:00+00:00", "2026-11-28T09:00:00+00:00", "2026-11-28T05:00:00Z",
               what="expect")
    assert len(m["late"]) == 1 and m["seats"] == {}, m


def test_main_s_gitignore_ignores_neither_the_seals_nor_a_ledger_m77():
    """main's M77: .gitignore's *.jsonl ignored queue/PLANT_SEALS.jsonl, and round 1's seal could not be committed; the
    tests built repositories without main's .gitignore and could not see it"""
    for rel in (P.SEALS, "%s/ROUND_1.json" % P.LEDGERS, "%s/ROUND_12.json" % P.LEDGERS):
        r = subprocess.run(["git", "check-ignore", "-q", "--no-index", rel], cwd=ROOT, capture_output=True)
        assert r.returncode == 1, "%s is ignored by main's .gitignore" % rel
