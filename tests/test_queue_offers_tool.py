"""2026-11-28 (the framework's thin path; register row P-885; main's M80, M81): the offers' tool, scripts/queue/offers.py.

The peers are main's list, each on its live branch: of the Pins table's branches for its code, the one that moved last,
left out when it has not moved in 14 days. Each card takes the next peer of another family in a rotation carried from
card to card, going on from the file's last offer; main's own cards go to the first peer of another family. Run on today's
queue with main's peers, the draft gives main's own 43 offers of 2026-11-28 (M81). Every drafted offer passes the
runner's own check."""
import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("offers_tool_under_test", ROOT / "scripts" / "queue" / "offers.py")
O = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True
spec.loader.exec_module(O)

MAIN = O.QS.MAIN_CODE
P, A2, A, C = "fam2-v1-unset-01", "fam3-v1-high-03", "fam3-v1-high-01", "fam1-v1-unset-03"
CODES = {"main": MAIN, "chat1/web-seat": C, "sm/banking": "fam1-v1-unset-04", "sm2/banking": "fam1-v1-unset-05",
         "audit/physical-bridge-2026-09-05": P, "audit/fork-2026-09-20": P, "agy/cusp-action-2026-11-20": A,
         "agy/frontier-2026-10-26": A, "agy/self-consistent-loop-2026-11-11": "fam3-v1-high-02", "agy-002/verify": A2,
         "agy-002/closure": A2, "sm/cards": "fam1-v1-unset-04"}
BANKING = {"V1": {"code": "fam1-v1-unset-04", "branch": "sm/banking"}, "V2": {"code": "fam1-v1-unset-05", "branch": "sm2/banking"}}
MOVED = {"audit/physical-bridge-2026-09-05": "2026-11-28T11:22:31Z", "audit/fork-2026-09-20": "2026-10-13T11:17:07Z",
         "chat1/web-seat": "2026-11-28T12:58:01Z", "agy/cusp-action-2026-11-20": "2026-11-28T10:17:48Z",
         "agy/frontier-2026-10-26": "2026-10-27T11:35:01Z", "agy/self-consistent-loop-2026-11-11": "2026-11-26T10:10:28Z",
         "agy-002/verify": "2026-11-28T13:01:18Z", "agy-002/closure": "2026-11-17T11:47:48Z",
         "sm/cards": "2026-11-27T23:39:49Z", "sm/banking": "2026-11-28T10:52:31Z", "sm2/banking": "2026-11-28T10:52:26Z"}
PINS = set(MOVED)
AT = "2026-11-28T15:00:00Z"
MAINS_PEERS = [P, A2, A, C]          # main's list, the four seats told their role (2026-11-28)
# main's own queue/OFFERS.json of 2026-11-28, its 43 peers in the order of the cards Q0001 to Q0043
MAINS_43 = "P P P P P P P A2 A C P A2 A P A2 A C P C P C P C P C P C P C P C P A2 A P A2 A P A2 A P A2 A".split()
SHORT = {"P": P, "A2": A2, "A": A, "C": C}


def _todays_queue():
    """the queue's 43 cards of 2026-11-28 as discovery filed them: by seat, in queue order"""
    seats = [("main", MAIN, 7), ("audit/physical-bridge-2026-09-05", P, 3), ("chat1/web-seat", C, 6),
             ("agy-002/verify", A2, 10), ("agy/cusp-action-2026-11-20", A, 6), ("sm/cards", "fam1-v1-unset-04", 11)]
    cards, n = {}, 0
    for branch, code, k in seats:
        for _ in range(k):
            n += 1
            cid = "Q%04d" % n
            cards[cid] = {"id": cid, "status": "FILED", "seat_code": code, "branch": branch,
                          "card_path": "relays/claims/CLAIM_%s.md" % cid, "history": []}
    return cards


def test_each_seat_is_offered_on_its_live_branch_and_a_stale_one_is_left_out_m81():
    live, why = O.live_branches(CODES, BANKING, PINS, MOVED, AT)
    assert live == {C: "chat1/web-seat", P: "audit/physical-bridge-2026-09-05", A: "agy/cusp-action-2026-11-20",
                    A2: "agy-002/verify", "fam3-v1-high-02": "agy/self-consistent-loop-2026-11-11"}, live
    assert MAIN not in live and "fam1-v1-unset-04" not in live          # main and the banking seats are no peers
    stale = dict(MOVED, **{"agy/self-consistent-loop-2026-11-11": "2026-11-13T10:10:28Z"})
    live, why = O.live_branches(CODES, BANKING, PINS, stale, AT)
    assert "fam3-v1-high-02" not in live and any("fam3-v1-high-02: its live branch" in w and "14 days" in w for w in why)
    live, why = O.live_branches(CODES, BANKING, PINS - {"chat1/web-seat"}, MOVED, AT)
    assert C not in live and any(w.startswith(C + ": no branch of it in the Pins table") for w in why)


def test_on_todays_queue_the_draft_gives_mains_own_43_offers_m81():
    live, _ = O.live_branches(CODES, BANKING, PINS, MOVED, AT)
    the_peers = O.peers(MAINS_PEERS, live)
    assert the_peers == [(P, "audit/physical-bridge-2026-09-05"), (A2, "agy-002/verify"), (A, "agy/cusp-action-2026-11-20"),
                         (C, "chat1/web-seat")]
    cards = _todays_queue()
    unoffered, drafts, new = O.draft(cards, {}, the_peers, CODES, statuses=("FILED", "REPRODUCED"))
    assert [d["peer"]["code"] for d in drafts] == [SHORT[s] for s in MAINS_43]
    for d in drafts:
        assert not O.IN.offer_problems(cards[d["card"]], d["peer"], CODES)
    # filled halfway, or with every other card, the cards offered already move the rotation where they stand
    half = {(o["branch"], o["path"]): o["peer"] for o in new[:20]}
    _, drafts2, _ = O.draft(cards, half, the_peers, CODES, statuses=("FILED", "REPRODUCED"))
    assert [d["peer"]["code"] for d in drafts2] == [SHORT[s] for s in MAINS_43[20:]]
    odd = {(o["branch"], o["path"]): o["peer"] for o in new[::2]}
    _, drafts4, _ = O.draft(cards, odd, the_peers, CODES, statuses=("FILED", "REPRODUCED"))
    assert [d["peer"]["code"] for d in drafts4] == [SHORT[s] for s in MAINS_43[1::2]]
    # a card of main's own filed later goes to the first peer of another family, wherever the rotation stands
    later = {k: v for k, v in cards.items() if int(k[1:]) <= 41}
    later["Q0044"] = dict(cards["Q0001"], id="Q0044", card_path="relays/claims/CLAIM_Q0044.md")
    done = {(o["branch"], o["path"]): o["peer"] for o in new[:41]}
    _, drafts3, _ = O.draft(later, done, the_peers, CODES, statuses=("FILED",))
    assert [d["card"] for d in drafts3] == ["Q0044"] and drafts3[0]["peer"]["code"] == P     # the rotation stood at agy-002
    # an offer already made for a card of main's own does not move the rotation
    some = {k: v for k, v in cards.items() if int(k[1:]) <= 9}
    some["Q0044"] = dict(cards["Q0001"], id="Q0044", card_path="relays/claims/CLAIM_Q0044.md")
    some["Q0045"] = dict(cards["Q0033"], id="Q0045", card_path="relays/claims/CLAIM_Q0045.md")
    made = {(o["branch"], o["path"]): o["peer"] for o in new[:9]}
    made[("main", "relays/claims/CLAIM_Q0044.md")] = {"code": P, "branch": "audit/physical-bridge-2026-09-05"}
    _, drafts5, _ = O.draft(some, made, the_peers, CODES, statuses=("FILED",))
    assert [(d["card"], d["peer"]["code"]) for d in drafts5] == [("Q0045", P)]      # after agy, chat1 is its own family
    # REPRODUCED cards only, by default
    assert O.draft(cards, {}, the_peers, CODES)[0] == []


def test_a_card_with_no_live_peer_of_another_family_is_listed_with_no_draft():
    cards = _todays_queue()
    _, drafts, new = O.draft(cards, {}, [(P, "audit/physical-bridge-2026-09-05")], CODES, statuses=("FILED",))
    assert drafts[7] == {"card": "Q0008", "peer": None, "why": "no live peer of another family"}    # the physical seat's own
    assert len(new) == 40


def test_the_command_by_hand_prints_a_draft_the_runner_reads(tmp_path, capsys):
    root = tmp_path / "root"
    (root / "queue").mkdir(parents=True)
    (root / "docs").mkdir()
    (root / "queue" / "SEAT_CODES.json").write_text(json.dumps({"codes": CODES}))
    (root / "queue" / "BANKING_SEATS.json").write_text(json.dumps(BANKING))
    (root / "queue" / "OFFERS.json").write_text(json.dumps({"note": "n", "peers": MAINS_PEERS, "offers": []}))
    (root / "docs" / "HARVEST_LEDGER.md").write_text("# H\n\n## Pins\n\n| seat | branch | pin |\n|---|---|---|\n" + "".join(
        "| s%d | `origin/%s` | `abcdef%d` |\n" % (i, b, i) for i, b in enumerate(sorted(PINS))))
    q = tmp_path / "q"
    (q / "cards").mkdir(parents=True)
    for cid, rec in _todays_queue().items():
        (q / "cards" / ("%s.json" % cid)).write_text(json.dumps(rec))
    assert O.main(["--queue-dir", str(q), "--all", "--at", AT], root=root, moved=MOVED) == 0
    out = capsys.readouterr().out
    assert "43 FILED or REPRODUCED card(s) with no offer:" in out and "  left out: fam3-v1-high-02" not in out
    d = json.loads(out.split("the draft of queue/OFFERS.json:\n", 1)[1])
    assert d["peers"] == MAINS_PEERS and [o["peer"]["code"] for o in d["offers"]] == [SHORT[s] for s in MAINS_43]
    (tmp_path / "draft.json").write_text(json.dumps(d))
    offers, bad = O.IN.read_offers(tmp_path / "draft.json")
    assert bad == [] and len(offers) == 43
