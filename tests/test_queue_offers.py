"""2026-11-28 (the framework's thin path; register row P-885; main's M79): the offers to peers, main's
queue/OFFERS.json, and the runner's move from REPRODUCED to OFFERED.

The queue's branch is written by the runner's key alone, so main cannot offer a card by hand there. On a repository built
here: a REPRODUCED card whose offer holds is OFFERED by the runner, its note naming the peer; a card with no offer stays
REPRODUCED and the report says so; an offer to the card's own seat, its own family, or a branch that is not the code's is
refused; the offered peer's note is taken, and another seat's note, or a note in another code, is refused. The file's
form is planted rule by rule."""
import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


PT = _load("peer_tests_for_the_offers", "tests/test_queue_peer_note.py")
IN, T = PT.IN, PT.T
OTHER = "fam4-v1-high-01"
CODES = {"seat/a": "fam2-v5-high-01", "seat/p": PT.PEER, "seat/x": OTHER, "seat/kin": "fam2-v6-high-02"}
REFS = [("a", "origin/seat/a"), ("p", "origin/seat/p"), ("x", "origin/seat/x")]


def _reproduced(tmp_path):
    repo, q = tmp_path / "repo", tmp_path / "queue"
    repo.mkdir(parents=True)
    g = PT._g(repo)
    g("init", "-q", "-b", "seat/a")
    (repo / "s_good.py").write_text(T._script("good"), encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "the script")
    stated = g("rev-parse", "HEAD").strip()
    (repo / "relays" / "claims").mkdir(parents=True)
    (repo / "relays" / "claims" / "CLAIM_good.md").write_text(T._card("a count that holds", "good", stated=stated),
                                                              encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "a card")
    g("update-ref", "refs/remotes/origin/seat/a", "HEAD")
    return repo, q, g


def _offers(tmp_path, *offers):
    f = tmp_path / "OFFERS.json"
    f.write_text(json.dumps({"note": "n", "offers": [
        {"branch": b, "path": "relays/claims/CLAIM_good.md", "peer": {"code": c, "branch": pb}} for b, c, pb in offers]}))
    return f


def _round(repo, q, offers, at="2026-11-26T12:00:00Z"):
    out = IN.round_(q, root=repo, refs=REFS, codes=CODES, at=at, limit=60, allow_static=True, offers_file=offers)
    IN.write(q, out[0], out[1], out[2])
    return out


def test_a_reproduced_card_with_an_offer_is_offered_by_the_runner_and_one_with_none_stays_m79(tmp_path):
    repo, q, g = _reproduced(tmp_path / "none")
    cards, _, _, report, status = _round(repo, q, _offers(tmp_path / "none"))
    (cid, rec), = cards.items()
    assert status == 0 and rec["status"] == "REPRODUCED", report
    assert "%s REPRODUCED, and queue/OFFERS.json offers it to no peer yet" % cid in report
    repo, q, g = _reproduced(tmp_path / "one")
    cards, _, _, report, status = _round(repo, q, _offers(tmp_path / "one", ("seat/a", PT.PEER, "seat/p")))
    (cid, rec), = cards.items()
    assert rec["status"] == "OFFERED" and rec["history"][-1]["by"] == "runner", report
    assert rec["history"][-1]["note"] == "offered to %s on seat/p (queue/OFFERS.json)" % PT.PEER
    assert IN.offered_to(rec) == (PT.PEER, "seat/p")
    assert IN.QS.queue_problems({k: json.dumps(v) for k, v in cards.items()}) == []


def test_an_offer_to_the_cards_own_seat_its_own_family_or_a_branch_not_the_codes_is_refused_m79(tmp_path):
    for i, (code, branch, words) in enumerate((("fam2-v5-high-01", "seat/a", "the card's own seat"),
                                               ("fam2-v6-high-02", "seat/kin", "the card's own family (fam2)"),
                                               (OTHER, "seat/p", "seat/p is %s in queue/SEAT_CODES.json, not %s" % (PT.PEER, OTHER)),
                                               (OTHER, "seat/nowhere", "is not in queue/SEAT_CODES.json"))):
        repo, q, g = _reproduced(tmp_path / str(i))
        cards, _, _, report, _ = _round(repo, q, _offers(tmp_path / str(i), ("seat/a", code, branch)))
        (cid, rec), = cards.items()
        assert rec["status"] == "REPRODUCED" and any("its offer in queue/OFFERS.json is refused" in r and words in r
                                                     for r in report), (words, report)


def test_only_the_offered_peers_note_is_taken_m79(tmp_path):
    # the offered peer's note is taken
    repo, q, g = _reproduced(tmp_path / "ok")
    offers = _offers(tmp_path / "ok", ("seat/a", PT.PEER, "seat/p"))
    cards, *_ = _round(repo, q, offers)
    (cid, rec), = cards.items()
    PT._file_note(repo, g, PT._note(cid, rec["commit"]))
    cards, _, att, report, _ = _round(repo, q, offers, at="2026-11-26T14:00:00Z")
    assert "PEERED" in [e["status"] for e in cards[cid]["history"]], report
    # another seat's note, on its own branch, is refused, and the card stays OFFERED
    repo, q, g = _reproduced(tmp_path / "other")
    offers = _offers(tmp_path / "other", ("seat/a", PT.PEER, "seat/p"))
    cards, *_ = _round(repo, q, offers)
    (cid, rec), = cards.items()
    PT._file_note(repo, g, PT._note(cid, rec["commit"], peer=OTHER), branch="seat/x")
    cards, _, att, report, _ = _round(repo, q, offers, at="2026-11-26T14:00:00Z")
    assert cards[cid]["status"] == "OFFERED", report
    assert any("on origin/seat/x is refused: the card is offered to %s on seat/p" % PT.PEER in r for r in report), report
    # a note on the offered branch in another seat's code is refused too
    repo, q, g = _reproduced(tmp_path / "code")
    offers = _offers(tmp_path / "code", ("seat/a", PT.PEER, "seat/p"))
    cards, *_ = _round(repo, q, offers)
    (cid, rec), = cards.items()
    PT._file_note(repo, g, PT._note(cid, rec["commit"], peer=OTHER))
    cards, _, att, report, _ = _round(repo, q, offers, at="2026-11-26T14:00:00Z")
    assert cards[cid]["status"] == "OFFERED" and "is not the offered peer" in att[cid]["peer"]["reasons"][0], report


def test_the_offers_file_form_and_the_one_shipped(tmp_path):
    f = tmp_path / "o.json"
    good = {"branch": "seat/a", "path": "relays/claims/CLAIM_good.md", "peer": {"code": PT.PEER, "branch": "seat/p"}}
    for offers, words in (([dict(good, name="x")], "holds exactly branch, path and peer"),
                          ([dict(good, peer={"code": PT.PEER})], "holds exactly branch, path and peer"),
                          ([dict(good, peer={"code": "a name", "branch": "seat/p"})], "the peer's code"),
                          ([dict(good, path="docs/x.md")], "not under relays/claims/"),
                          ([dict(good, branch="../x")], "the card's branch is not a branch's name"),
                          ([good, dict(good)], "the card is offered twice")):
        f.write_text(json.dumps({"note": "n", "offers": offers}))
        offers_read, bad = IN.read_offers(f)
        assert any(words in b for b in bad), (words, bad)
    f.write_text("not json")
    assert IN.read_offers(f) == ({}, ["queue/OFFERS.json is not JSON"])
    assert IN.read_offers(tmp_path / "absent.json") == ({}, [])
    shipped, bad = IN.read_offers(ROOT / "queue" / "OFFERS.json")
    assert bad == [], bad
