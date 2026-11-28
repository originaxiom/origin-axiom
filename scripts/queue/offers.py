#!/usr/bin/env python3
"""The offers' tool for main (the framework's thin path; register row P-885; main's M80, M81).

Main fills `queue/OFFERS.json` (main's M79), and the runner moves each REPRODUCED card whose offer holds to OFFERED. This
command prints, from the queue's branch, every REPRODUCED card that has no offer yet (its id, branch, path and seat code),
and a draft offer for each. The same rule drafts every card's offer, so that no offer tells one card from another.

  THE PEERS, in their order: the codes `queue/OFFERS.json` lists under "peers", main's choice of the seats that serve as
    peers (the ones told their role); without that list, every seat of `queue/SEAT_CODES.json` but main and the banking
    seats, in the order of their codes. Each is offered on its LIVE BRANCH (main's M81): of the branches the harvest
    ledger's Pins table names for its code, as discovery reads it, the one that moved last. A seat whose live branch has
    not moved in 14 days is left out, and said; so is a seat with no branch in the Pins table.
  THE ROTATION, carried from card to card in queue order: each card takes the next peer, going round, whose family (the
    code's first part) is not the card's own, and the next card starts after it. A card offered already moves the
    rotation past its own peer, where it stands in queue order, so the draft hangs neither on the file's order nor on
    when each card was offered. A card of main's own takes the first peer of another family and does not move the rotation: main's
    cards are one batch, offered to one peer (main's M24, for the trial). A card for which no peer of another family is
    live is listed with no draft, and said.

The draft is a whole `queue/OFFERS.json`: the offers already there, then the new ones. Nothing is written: main reads
it, and commits the file itself. Every drafted offer is one the runner's own check (`intake.offer_problems`) accepts.

    python3 scripts/queue/offers.py                      # reads origin/queue's cards; prints the list and the draft
    python3 scripts/queue/offers.py --queue-dir DIR      # reads DIR/cards instead (the queue/ folder of the queue's branch)
      [--at TIME]                                        # the time "14 days" counts back from; now by default
      [--all]                                            # every FILED or REPRODUCED card with no offer, offered ahead
                                                         # of its rerun, as main offered the first 43
"""
import datetime
import importlib.util
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STALE_DAYS = 14


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


IN = _load("intake_for_the_offers_tool", HERE / "intake.py")
D, QS = IN.D, IN.QS


def queue_cards(root=ROOT, queue_dir=None, ref="origin/queue"):
    """{id: record}: the queue's cards, from a folder or from the queue's branch"""
    if queue_dir:
        return {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in sorted(pathlib.Path(queue_dir, "cards").glob("Q*.json"))}
    r = subprocess.run(["git", "ls-tree", "--name-only", "%s:queue/cards" % ref], cwd=root, capture_output=True, text=True)
    out = {}
    for name in r.stdout.split() if r.returncode == 0 else []:
        s = subprocess.run(["git", "show", "%s:queue/cards/%s" % (ref, name)], cwd=root, capture_output=True, text=True)
        if s.returncode == 0 and name.endswith(".json"):
            out[name[:-5]] = json.loads(s.stdout)
    return out


def moved_at(root, branch):
    """the time the branch's head was committed, UTC, or None"""
    r = subprocess.run(["git", "log", "-1", "--format=%cI", "origin/%s" % branch], cwd=root, capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    return datetime.datetime.fromisoformat(r.stdout.strip()).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def live_branches(codes, banking, pins_branches, moved, at, days=STALE_DAYS):
    """({code: its live branch}, [why a seat is left out]): of the Pins table's branches for each code, the one that moved
    last; a code whose live branch has not moved in `days` days, or that the Pins table names on no branch, is left out"""
    left_out = {QS.MAIN_CODE} | {s.get("code") for s in (banking or {}).values() if isinstance(s, dict)}
    since = (datetime.datetime.strptime(at, "%Y-%m-%dT%H:%M:%SZ") - datetime.timedelta(days=days)).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    by_code = {}
    for branch, code in codes.items():
        if code not in left_out and not branch.startswith("<v>/"):
            by_code.setdefault(code, []).append(branch)
    live, why = {}, []
    for code in sorted(by_code):
        named = [b for b in by_code[code] if b in pins_branches and moved.get(b)]
        if not named:
            why.append("%s: no branch of it in the Pins table" % code)
            continue
        branch = max(named, key=lambda b: (moved[b], b))
        if moved[branch] < since:
            why.append("%s: its live branch %s has not moved since %s, more than %d days" % (code, branch, moved[branch], days))
            continue
        live[code] = branch
    return live, why


def peers(order, live):
    """[(code, branch)]: the peers in their order, each on its live branch; a code not live is left out"""
    return [(code, live[code]) for code in (order if order is not None else sorted(live)) if code in live]


def draft(cards, offers, the_peers, codes, statuses=("REPRODUCED",)):
    """(the cards with no offer, [{card, peer or None, why}], the drafted file's new offers). The rotation walks every
    card in queue order: a card offered already moves it past its peer, where it stands, so a draft does not hang on the
    file's order or on when a card was offered"""
    start = 0
    unoffered, drafts = [], []
    for cid in IN.queue_order(cards):
        rec = cards[cid]
        have = offers.get((rec["branch"], rec["card_path"]))
        if have is not None:
            idx = [i for i, p in enumerate(the_peers) if p[0] == have.get("code")]
            if rec["seat_code"] != QS.MAIN_CODE and idx:
                start = (idx[0] + 1) % len(the_peers)
            continue
        if rec.get("status") not in statuses:
            continue
        unoffered.append({"id": cid, "branch": rec["branch"], "path": rec["card_path"], "seat_code": rec["seat_code"]})
        mains = rec["seat_code"] == QS.MAIN_CODE
        got = None
        for k in range(len(the_peers)):
            i = (k if mains else start + k) % len(the_peers)
            peer = {"code": the_peers[i][0], "branch": the_peers[i][1]}
            if not IN.offer_problems(rec, peer, codes):
                got = peer
                if not mains:
                    start = (i + 1) % len(the_peers)
                break
        drafts.append({"card": cid, "peer": got, "why": None if got else "no live peer of another family"})
    new = [{"branch": cards[d["card"]]["branch"], "path": cards[d["card"]]["card_path"], "peer": d["peer"]}
           for d in drafts if d["peer"]]
    return unoffered, drafts, new


def main(argv, root=ROOT, moved=None):
    arg = lambda k: argv[argv.index(k) + 1] if k in argv else None
    at = arg("--at") or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    cards = queue_cards(root, arg("--queue-dir"))
    offers_path = pathlib.Path(root, "queue", "OFFERS.json")
    offers, bad = IN.read_offers(offers_path)
    for b in bad:
        print("queue/OFFERS.json: %s" % b)
    current = json.loads(offers_path.read_text(encoding="utf-8")) if offers_path.is_file() else {"note": "", "offers": []}
    codes = D.seat_codes(pathlib.Path(root, "queue", "SEAT_CODES.json"))
    try:
        banking = json.loads(pathlib.Path(root, "queue", "BANKING_SEATS.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        banking = {}
    pins = {r.split("/", 1)[1] for k, r in D.branches(root=root) if k != "main" and r.startswith("origin/")}
    moved = moved if moved is not None else {b: moved_at(root, b) for b in pins}
    live, why = live_branches(codes, banking, pins, moved, at)
    the_peers = peers(current.get("peers"), live)
    unoffered, drafts, new = draft(cards, offers, the_peers, codes,
                                   ("FILED", "REPRODUCED") if "--all" in argv else ("REPRODUCED",))
    print("the peers, in their order, on their live branches: %s" % (", ".join("%s on %s" % p for p in the_peers) or "none"))
    for w in why:
        print("  left out: %s" % w)
    print("%d %s card(s) with no offer:" % (len(unoffered), "FILED or REPRODUCED" if "--all" in argv else "REPRODUCED"))
    for u, d in zip(unoffered, drafts):
        print("  %s  %s  %s  %s  ->  %s" % (u["id"], u["seat_code"], u["branch"], u["path"],
                                          "%s on %s" % (d["peer"]["code"], d["peer"]["branch"]) if d["peer"] else d["why"]))
    print("the draft of queue/OFFERS.json:")
    print(json.dumps(dict(current, offers=list(current.get("offers", [])) + new), indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
