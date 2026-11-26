#!/usr/bin/env python3
"""The queue's schema (the framework's thin path, patch T1; draft 1 § 9, main's M54; register row P-885).

Every claim card the intake has seen is one file, `queue/cards/Q<nnnn>.json`. The runner writes these files to the
queue's own branch; the landing tool and the gate `queue-schema` read them. A file holds:

    id          "Q" and four or more digits, the same as the file's name
    seat_code   the producing seat's neutral code (below), never a name
    branch      the seat branch the card was found on
    commit      the full 40-hex commit the card was sealed at
    card_path   the card's path on that branch, under relays/claims/
    title       the card's one line
    status      one of STATUSES; the same as the last entry of the history
    deciding    true, false, or null until the runner computes it
    heavy       true when the card is rerun on the author's machine, not on the workflow
    refiles     the ids of earlier cards this one refiles (a refiled card keeps its history)
    history     the moves, oldest first, each {at, status, by, note}; append-only

THE MOVES. A card moves only along MOVES. The intake's moves (to FILED, REPRODUCED, RETURNED AT INTAKE) are made by
the runner alone. A card that is returned is not moved back: the seat refiles it, as a new card that names the old one
in `refiles`. A refile is a new id so that the old card's history is never rewritten.

THE SEAT CODE (draft § 8). `fam<n>-v<n>[.<n>]-<effort>-<nn>`: a family's number, a version, the effort the author
recorded at hire (or `unset`), and a serial for seats of the same kind. The mapping of family numbers to names is the
author's and is not in the repository. A code must not read as a code of the inputs scoreboard (A01 to A12, F1 to F4,
S01 to S03, LAMBDA, I-n) in any case, or the intake would take every card that names its seat as deciding.

Decided here, and said so for main (M54: a question of schema is decided in the patch):
  - PARKED, in the plan's list of statuses, is left out: the frozen list of unbanked claims is main's own file, and a
    claim on it becomes a card only when it is fed in;
  - "no peer check" is not a status but a move from OFFERED straight to AT_BANKING, whose note says so;
  - a returned card is never moved again; it is refiled as a new card that names it.

    python3 scripts/queue/queue_schema.py                    # the cards under queue/cards/ in this checkout
    python3 scripts/queue/queue_schema.py --dir PATH         # the cards in another directory
    python3 scripts/queue/queue_schema.py --ref REF          # the cards on a git ref, e.g. origin/queue
Exit 0 when every card holds, 1 when one does not."""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CARDS = "queue/cards"

STATUSES = ("FILED", "RETURNED_AT_INTAKE", "REPRODUCED", "OFFERED", "PEERED", "AT_BANKING",
            "SPLIT", "VERIFIED", "RETURNED", "REFUSED")
MOVES = {
    "FILED": ("REPRODUCED", "RETURNED_AT_INTAKE"),
    "REPRODUCED": ("OFFERED", "AT_BANKING"),          # a card that decides nothing stays REPRODUCED
    "OFFERED": ("OFFERED", "PEERED", "AT_BANKING"),   # a re-offer; a peer note; no peer within the time
    "PEERED": ("AT_BANKING", "RETURNED"),             # a fault found by the peer goes back to the producer
    "AT_BANKING": ("VERIFIED", "RETURNED", "REFUSED", "SPLIT"),
    "SPLIT": ("VERIFIED", "RETURNED", "REFUSED"),
    "RETURNED_AT_INTAKE": (), "VERIFIED": (), "RETURNED": (), "REFUSED": (),
}
RUNNER_ONLY = ("FILED", "REPRODUCED", "RETURNED_AT_INTAKE")
FIELDS = ("id", "seat_code", "branch", "commit", "card_path", "title", "status", "deciding", "heavy", "refiles",
          "history")
ENTRY_FIELDS = ("at", "status", "by", "note")

ID = re.compile(r"Q\d{4,}")
SEAT_CODE = re.compile(r"fam\d{1,2}-v\d{1,2}(?:\.\d{1,2})?-(?:low|medium|high|xhigh|max|unset)-\d{2,3}")
BY_OTHER = ("runner", "main", "author")
AT = re.compile(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ")
COMMIT = re.compile(r"[0-9a-f]{40}")
BRANCH = re.compile(r"[A-Za-z0-9._/-]+")
CARD_PATH = re.compile(r"relays/claims/CLAIM_[A-Za-z0-9._-]+\.md")
# the inputs scoreboard's codes, as scripts/checks/seat_intake.py reads them, here in any case
SCOREBOARD = re.compile(r"\b(A0[1-9]|A1[0-2]|F[1-4]|S0[1-3]|LAMBDA|I-\d+)\b", re.I)


def code_problems(code, what="seat_code"):
    """what is wrong with a seat code: its form, or a part that reads as a scoreboard code"""
    if not isinstance(code, str) or not SEAT_CODE.fullmatch(code):
        return ["%s %r is not of the form fam<n>-v<n>-<effort>-<nn>" % (what, code)]
    if SCOREBOARD.search(code):
        return ["%s %r reads as a code of the inputs scoreboard" % (what, code)]
    return []


def card_problems(card, name=None, vendor_re=None):
    """every way one card's record breaks the schema; [] when it holds. `name` is the file's name without .json"""
    if not isinstance(card, dict):
        return ["the file is not a table"]
    bad = []
    missing = [f for f in FIELDS if f not in card]
    extra = sorted(set(card) - set(FIELDS))
    if missing:
        bad.append("fields missing: %s" % ", ".join(missing))
    if extra:
        bad.append("fields not in the schema: %s" % ", ".join(extra))
    if missing:
        return bad
    if not isinstance(card["id"], str) or not ID.fullmatch(card["id"]):
        bad.append("id %r is not Q and four or more digits" % (card["id"],))
    elif name is not None and name != card["id"]:
        bad.append("id %s stands in the file %s.json" % (card["id"], name))
    bad += code_problems(card["seat_code"])
    if not isinstance(card["branch"], str) or not BRANCH.fullmatch(card["branch"]):
        bad.append("branch %r is not a branch's name" % (card["branch"],))
    if not isinstance(card["commit"], str) or not COMMIT.fullmatch(card["commit"]):
        bad.append("commit %r is not a full 40-hex commit" % (card["commit"],))
    if not isinstance(card["card_path"], str) or not CARD_PATH.fullmatch(card["card_path"]):
        bad.append("card_path %r is not a claim card under relays/claims/" % (card["card_path"],))
    if not isinstance(card["title"], str) or not card["title"].strip() or "\n" in card["title"] or len(card["title"]) > 240:
        bad.append("title is not one line of 1 to 240 characters")
    if card["status"] not in STATUSES:
        bad.append("status %r is not one of the queue's statuses" % (card["status"],))
    if card["deciding"] not in (True, False, None):
        bad.append("deciding is not true, false or null")
    if not isinstance(card["heavy"], bool):
        bad.append("heavy is not true or false")
    refiles = card["refiles"]
    if not isinstance(refiles, list) or any(not isinstance(r, str) or not ID.fullmatch(r) for r in refiles):
        bad.append("refiles is not a list of card ids")
    elif card["id"] in refiles:
        bad.append("the card refiles itself")
    bad += history_problems(card["history"], card["status"])
    if vendor_re is not None:
        text = json.dumps(card, ensure_ascii=False)
        if vendor_re.search(text):
            bad.append("the record names a vendor or a model; a seat is named by its code")
    return bad


def history_problems(history, status):
    """the history: oldest first, opened by the runner at FILED, each move allowed, its time not going back, and its
    last status the card's"""
    if not isinstance(history, list) or not history:
        return ["history is not a list of one or more moves"]
    bad = []
    for i, e in enumerate(history):
        if not isinstance(e, dict) or sorted(e) != sorted(ENTRY_FIELDS):
            bad.append("history entry %d does not hold exactly %s" % (i, ", ".join(ENTRY_FIELDS)))
            return bad
        if not isinstance(e["at"], str) or not AT.fullmatch(e["at"]):
            bad.append("history entry %d: at %r is not YYYY-MM-DDTHH:MM:SSZ" % (i, e["at"]))
        if e["status"] not in STATUSES:
            bad.append("history entry %d: status %r is not one of the queue's statuses" % (i, e["status"]))
        if e["by"] not in BY_OTHER:
            bad += ["history entry %d: %s" % (i, p) for p in code_problems(e["by"], "by")]
        if e["status"] in RUNNER_ONLY and e["by"] != "runner":
            bad.append("history entry %d: %s is the runner's move, made by %r" % (i, e["status"], e["by"]))
        if not isinstance(e["note"], str):
            bad.append("history entry %d: note is not text" % i)
    if bad:
        return bad
    if history[0]["status"] != "FILED":
        bad.append("the history opens at %s, not FILED" % history[0]["status"])
    for i in range(1, len(history)):
        a, b = history[i - 1], history[i]
        if b["status"] not in MOVES[a["status"]]:
            bad.append("history entry %d: %s to %s is not a move of the queue" % (i, a["status"], b["status"]))
        if b["at"] < a["at"]:
            bad.append("history entry %d goes back in time (%s after %s)" % (i, b["at"], a["at"]))
    if history[-1]["status"] != status:
        bad.append("status %s is not the history's last (%s)" % (status, history[-1]["status"]))
    return bad


def queue_problems(cards, vendor_re=None):
    """{name: text} of card files -> the list of problems, each named by its file; ids must be unique and every
    refile must name a card in the queue"""
    bad, ids = [], set()
    parsed = {}
    for name in sorted(cards):
        if name == "(strays)":
            bad.append("files in the queue that are not cards: %s" % ", ".join(json.loads(cards[name])["strays"]))
            continue
        try:
            card = json.loads(cards[name])
        except ValueError as exc:
            bad.append("%s.json: not JSON (%s)" % (name, exc))
            continue
        parsed[name] = card
        bad += ["%s.json: %s" % (name, p) for p in card_problems(card, name, vendor_re)]
        if isinstance(card, dict) and card.get("id") in ids:
            bad.append("%s.json: id %s stands twice" % (name, card.get("id")))
        if isinstance(card, dict):
            ids.add(card.get("id"))
    for name, card in parsed.items():
        if isinstance(card, dict) and isinstance(card.get("refiles"), list):
            for r in card["refiles"]:
                if isinstance(r, str) and r not in ids:
                    bad.append("%s.json: refiles %s, which is not in the queue" % (name, r))
    return bad


def read_dir(path):
    """the card files of a directory, {name: text}; a directory that is not there holds no cards"""
    p = pathlib.Path(path)
    if not p.is_dir():
        return {}
    out = {f.stem: f.read_text(encoding="utf-8") for f in sorted(p.glob("*.json"))}
    strays = [f.name for f in sorted(p.iterdir()) if f.is_file() and f.suffix != ".json" and f.name != "README.md"]
    if strays:
        out["(strays)"] = json.dumps({"strays": strays})
    return out


def read_ref(ref, root=ROOT):
    """the card files on a git ref, {name: text}, read without a checkout"""
    r = subprocess.run(["git", "ls-tree", "--name-only", "%s:%s" % (ref, CARDS)], cwd=root, capture_output=True,
                       text=True)
    if r.returncode != 0:
        raise RuntimeError("the ref %s holds no %s (%s)" % (ref, CARDS, r.stderr.strip()))
    out = {}
    for n in r.stdout.split():
        if n.endswith(".json"):
            s = subprocess.run(["git", "show", "%s:%s/%s" % (ref, CARDS, n)], cwd=root, capture_output=True, text=True)
            out[n[:-5]] = s.stdout
    return out


def _vendor_re():
    import importlib.util
    spec = importlib.util.spec_from_file_location("gates_for_the_queue", ROOT / "scripts" / "gates" / "gates.py")
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m._VENDOR_RE


def main(argv):
    if "--ref" in argv:
        cards = read_ref(argv[argv.index("--ref") + 1])
        where = argv[argv.index("--ref") + 1]
    else:
        d = argv[argv.index("--dir") + 1] if "--dir" in argv else str(ROOT / CARDS)
        cards, where = read_dir(d), ("queue/cards" if "--dir" not in argv else d)
    bad = queue_problems(cards, _vendor_re())
    for b in bad:
        print(b)
    print("%d card(s) read on %s; %d problem(s)" % (len([n for n in cards if n != "(strays)"]), where, len(bad)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
