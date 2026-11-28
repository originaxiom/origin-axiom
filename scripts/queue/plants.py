#!/usr/bin/env python3
"""The plant ledger: its format, its seal per round, its opening, and the catch rates it gives (the framework's thin path,
patch T12; draft 1 §§ 4 and 9; docs/roles/BANKING.md, "How you are measured"; register row P-885).

A fixed share of the queue is planted: cards with a known fault, under real producers' ids, arranged by the author, mixed
into the peer stage and banking, unknown to the seats. Which cards are planted, and how, is main's alone. This file holds
the format and the checks, never a plant: the builder does not see the ledger's contents (main's M54).

THE WORD "ROUND" (main's M76 point 3). The ledger's round is a batch of cards, not one run of the runner, which the queue's
README also calls a round and which comes every three hours. A ledger's round ends when every card it names has ended (its
status final: VERIFIED, RETURNED, REFUSED, WITHDRAWN, NOT_BANKED, RETURNED_AT_INTAKE); only then is its ledger opened.

EACH ROUND, in this order, all on main:
  1. main writes the round's ledger, `queue/plants/ROUND_<n>.json`, and keeps it untracked;
  2. main commits its seal, one line appended to `queue/PLANT_SEALS.jsonl`: {"round": n, "sha256": <the ledger's SHA-256>}
     (`plants.py --seal LEDGER` prints the line);
  3. the round runs: the seats file their notes and verdicts;
  4. after the round, main commits the ledger itself, which opens it.

THE LEDGER, `queue/plants/ROUND_<n>.json`:
    {"round": n, "nonce": <64 hex, fresh each round, so that a small ledger cannot be guessed from its hash>,
     "plants": [{"branch": <the seat branch the card is filed on>, "path": <the card's path, under relays/claims/>,
                 "shape": one of SHAPES, the banking rule whose plant it is (BANKING.md's table),
                 "stage": "peer", "banking" or "both", where the fault is meant to be caught,
                 "source": "main", "auditor" or "calibration" (draft § 9, the advisor's fifth question),
                 "fault": one line, what is wrong with the card,
                 "caught_by": the verdicts that catch it, a list of "REFUSE" and "RETURN"}]}
  A round may hold no plant; its ledger is sealed and opened all the same, so that the seals do not tell which rounds had
  plants.

THE RULES (the gate `plant-ledger`, fail-closed):
  - `queue/PLANT_SEALS.jsonl` holds its form: one JSON object a line, its rounds 1, 2, 3, ... in order;
  - it is only appended to, along main's first-parent history: no line is ever changed or taken out;
  - every opened ledger holds its form, has its round's seal, and hashes, byte for byte, to it;
  - a ledger is opened in a commit after the one that added its seal, never in the same one;
  - an opened ledger never changes afterwards, and is never taken out (main's M76);
  - round n's ledger is opened by the commit that seals round n + 1, or before it (main's M76): a round is not left
    sealed and never opened.

THE MEASURE (`--measure QDIR`): for each plant of every opened ledger, the queue's card filed from its branch and path, and
what each seat said of it. A banking seat catches a plant when its verdict is one of the plant's `caught_by`; a peer, when
its note's finding is "fault". The report gives each seat's catches over its plants, and the shapes not yet planted in
any round (THE_RULES_SORTED: one plant of each shape over the rounds). Two kinds of plant are reported and not counted:
  - sealed late: a seat's content for the card (a verdict, a note or an expectation) was first sighted by the runner
    before its round's seal was committed;
  - opened early (main's M76): a seat's content for the card was first sighted after the commit that opened the ledger,
    which is public on main from then on.

    python3 scripts/queue/plants.py --check                 # the gate's rules on this checkout; exit 1 when one fails
    python3 scripts/queue/plants.py --seal LEDGER           # the seal line for LEDGER, after its form is checked
    python3 scripts/queue/plants.py --nonce                 # a fresh nonce
    python3 scripts/queue/plants.py --measure QDIR          # the catch rates, from the queue's folder QDIR
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SEALS = "queue/PLANT_SEALS.jsonl"
LEDGERS = "queue/plants"
LEDGER_NAME = re.compile(r"ROUND_(\d+)\.json")
SHAPES = ("K2", "K4", "K5", "K6", "K7", "K8", "K9", "K10")     # BANKING.md: the rules whose check is a plant
STAGES = ("peer", "banking", "both")
SOURCES = ("main", "auditor", "calibration")
CATCHES = ("REFUSE", "RETURN")
HEX64 = re.compile(r"[0-9a-f]{64}")
SEAT_CONTENT = ("verdict", "peer", "expect")          # what a seat files about a card, as the sighting log names it (M76)
PLANT_KEYS = ("branch", "path", "shape", "stage", "source", "fault", "caught_by")


def _git(root, *args):
    r = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return r.returncode, r.stdout


def ledger_problems(d, n=None):
    """the problems of a ledger's form; n, when given, is the round its file name says"""
    if not isinstance(d, dict) or sorted(d) != ["nonce", "plants", "round"]:
        return ["a ledger holds exactly round, nonce and plants"]
    bad = []
    if not isinstance(d["round"], int) or isinstance(d["round"], bool) or d["round"] < 1:
        bad.append("its round is a number from 1")
    elif n is not None and d["round"] != n:
        bad.append("it says round %s and its file says %s" % (d["round"], n))
    if not isinstance(d["nonce"], str) or not HEX64.fullmatch(d["nonce"]):
        bad.append("its nonce is 64 hex digits")
    if not isinstance(d["plants"], list):
        return bad + ["its plants are a list"]
    seen = set()
    for i, p in enumerate(d["plants"]):
        where = "plant %d" % (i + 1)
        if not isinstance(p, dict) or sorted(p) != sorted(PLANT_KEYS):
            bad.append("%s holds exactly %s" % (where, ", ".join(PLANT_KEYS)))
            continue
        if not isinstance(p["branch"], str) or not p["branch"] or p["branch"].startswith(("-", "/")) or ".." in p["branch"]:
            bad.append("%s: its branch is a branch's name" % where)
        if not isinstance(p["path"], str) or not p["path"].startswith("relays/claims/") or ".." in p["path"]:
            bad.append("%s: its path is a card's, under relays/claims/" % where)
        if p["shape"] not in SHAPES:
            bad.append("%s: its shape is one of %s" % (where, ", ".join(SHAPES)))
        if p["stage"] not in STAGES:
            bad.append("%s: its stage is one of %s" % (where, ", ".join(STAGES)))
        if p["source"] not in SOURCES:
            bad.append("%s: its source is one of %s" % (where, ", ".join(SOURCES)))
        if not isinstance(p["fault"], str) or not p["fault"].strip() or "\n" in p["fault"]:
            bad.append("%s: its fault is one line" % where)
        if not isinstance(p["caught_by"], list) or not p["caught_by"] or any(c not in CATCHES for c in p["caught_by"]):
            bad.append("%s: caught_by is a list of %s" % (where, " and ".join(CATCHES)))
        key = (p.get("branch"), p.get("path"))
        if key in seen:
            bad.append("%s: the same card is planted twice" % where)
        seen.add(key)
    return bad


def read_seals(text):
    """([{round, sha256}], problems)"""
    out, bad = [], []
    for i, line in enumerate(text.splitlines(), 1):
        try:
            s = json.loads(line)
        except ValueError:
            bad.append("seal line %d is not JSON" % i)
            continue
        if not isinstance(s, dict) or sorted(s) != ["round", "sha256"] or not isinstance(s["sha256"], str) \
                or not HEX64.fullmatch(s["sha256"]):
            bad.append("seal line %d holds exactly round and sha256 (64 hex digits)" % i)
            continue
        if s["round"] != len(out) + 1:
            bad.append("seal line %d is for round %s; the rounds go 1, 2, 3, ... in order" % (i, s["round"]))
        out.append(s)
    return out, bad


def seal_line(raw, n):
    return json.dumps({"round": n, "sha256": hashlib.sha256(raw).hexdigest()}, sort_keys=True)


def _first_parent(root, path):
    rc, out = _git(root, "log", "--first-parent", "--reverse", "--format=%H", "HEAD", "--", path)
    return out.split() if rc == 0 else None


def _blob_at(root, commit, path):
    r = subprocess.run(["git", "show", "%s:%s" % (commit, path)], cwd=root, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def problems(root=ROOT):
    """the gate's rules on a checkout: [] when they hold"""
    root = pathlib.Path(root)
    f = root / SEALS
    text = f.read_text(encoding="utf-8") if f.is_file() else ""
    seals, bad = read_seals(text)
    by_round = {s["round"]: s for s in seals}
    # the seals only appended to, along main's first-parent history
    commits = _first_parent(root, SEALS)
    if commits is None:
        return bad + ["the history of %s cannot be read" % SEALS]
    sealed_in, before = {}, ""
    for c in commits:
        now = (_blob_at(root, c, SEALS) or b"").decode("utf-8", "replace")
        if not now.startswith(before):
            bad.append("%s at %s changes or takes out a line before it: it is only appended to" % (SEALS, c[:9]))
        for s in read_seals(now)[0]:
            sealed_in.setdefault(s["round"], c)
        before = now
    if not text.startswith(before):
        bad.append("%s in the working tree changes a committed line: it is only appended to" % SEALS)
    # a ledger once opened stays (main's M76): every ROUND_<n>.json ever added along main's first-parent history is here
    rc, added = _git(root, "log", "--first-parent", "--diff-filter=A", "--name-only", "--format=", "HEAD", "--", LEDGERS)
    for rel in sorted(set(l.strip() for l in added.splitlines() if l.strip())):
        if not (root / rel).is_file():
            bad.append("%s was opened and is gone: an opened ledger stays" % rel)
    # every round sealed after the first: the round before it opened by then (main's M76)
    for n in sorted(sealed_in):
        if n - 1 >= 1 and n - 1 in sealed_in:
            opened_prev = _first_parent(root, "%s/ROUND_%d.json" % (LEDGERS, n - 1)) or []
            if not opened_prev or _git(root, "merge-base", "--is-ancestor", opened_prev[0], sealed_in[n])[0] != 0:
                bad.append("round %d is sealed and round %d's ledger was not opened by then" % (n, n - 1))
    # every opened ledger: its form, its seal, its hash, opened after its seal and never changed
    d = root / LEDGERS
    for led in sorted(d.iterdir()) if d.is_dir() else []:
        m = LEDGER_NAME.fullmatch(led.name)
        rel = "%s/%s" % (LEDGERS, led.name)
        if not m:
            bad.append("%s is not named ROUND_<n>.json" % rel)
            continue
        n = int(m.group(1))
        raw = led.read_bytes()
        try:
            bad += ["%s: %s" % (rel, p) for p in ledger_problems(json.loads(raw.decode("utf-8")), n)]
        except ValueError:
            bad.append("%s is not JSON" % rel)
        if n not in by_round:
            bad.append("%s is opened with no seal for round %d" % (rel, n))
            continue
        if hashlib.sha256(raw).hexdigest() != by_round[n]["sha256"]:
            bad.append("%s does not hash to round %d's seal" % (rel, n))
        opened = _first_parent(root, rel) or []
        if opened:
            if n in sealed_in and opened[0] == sealed_in[n]:
                bad.append("%s is opened in the commit that seals it" % rel)
            elif n in sealed_in and _git(root, "merge-base", "--is-ancestor", sealed_in[n], opened[0])[0] != 0:
                bad.append("%s is opened before its seal" % rel)
            elif n not in sealed_in:
                bad.append("%s is opened, and its seal is not in the committed history" % rel)
            first = _blob_at(root, opened[0], rel)
            for c in opened[1:]:
                if _blob_at(root, c, rel) != first:
                    bad.append("%s changes at %s after it was opened" % (rel, c[:9]))
                    break
            if first is not None and raw != first:
                bad.append("%s in the working tree is not the ledger as opened" % rel)
    return bad


def _commit_time(root, commit):
    rc, out = _git(root, "show", "-s", "--format=%cI", commit)
    if rc != 0:
        return None
    import datetime
    t = datetime.datetime.fromisoformat(out.strip()).astimezone(datetime.timezone.utc)
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


PEERED = re.compile(r"the peer note on (\S+) at [0-9a-f]+: (reproduced|fault|extended), graded")


def _json(f):
    try:
        return json.loads(pathlib.Path(f).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def measure(qdir, root=ROOT):
    """{seats: {code: [caught, planted]}, plants: [...], unplanted: [shapes], late: [...]}, from the opened ledgers and
    the queue's folder: its cards, its check files and its sighting log"""
    root, qdir = pathlib.Path(root), pathlib.Path(qdir)
    cards = {}
    for f in sorted((qdir / "cards").glob("Q*.json")):
        r = json.loads(f.read_text(encoding="utf-8"))
        cards[(r["branch"], r["card_path"])] = r
    log = qdir / "SIGHTINGS.jsonl"
    entries = [json.loads(l) for l in log.read_text(encoding="utf-8").splitlines() if l.strip()] if log.is_file() else []
    seals = read_seals((root / SEALS).read_text(encoding="utf-8") if (root / SEALS).is_file() else "")[0]
    sealed_at = {}
    for c in _first_parent(root, SEALS) or []:
        for s in read_seals((_blob_at(root, c, SEALS) or b"").decode("utf-8", "replace"))[0]:
            sealed_at.setdefault(s["round"], _commit_time(root, c))
    banking = _json(root / "queue" / "BANKING_SEATS.json")
    codes = (_json(root / "queue" / "SEAT_CODES.json") or {}).get("codes", {})
    opened_at = {}
    for led in sorted((root / LEDGERS).glob("ROUND_*.json")) if (root / LEDGERS).is_dir() else []:
        first = (_first_parent(root, "%s/%s" % (LEDGERS, led.name)) or [None])[0]
        m = LEDGER_NAME.fullmatch(led.name)
        if first and m:
            opened_at[int(m.group(1))] = _commit_time(root, first)
    seats, out, late, early, shapes = {}, [], [], [], set()
    for led in sorted((root / LEDGERS).glob("ROUND_*.json")) if (root / LEDGERS).is_dir() else []:
        d = json.loads(led.read_text(encoding="utf-8"))
        for p in d["plants"]:
            shapes.add(p["shape"])
            rec = cards.get((p["branch"], p["path"]))
            row = {"round": d["round"], "branch": p["branch"], "path": p["path"], "shape": p["shape"],
                   "card": rec["id"] if rec else None, "said": {}}
            if rec is None:
                row["note"] = "not filed in the queue"
                out.append(row)
                continue
            cf = qdir / "checks" / ("%s.json" % rec["id"])
            check = json.loads(cf.read_text(encoding="utf-8")) if cf.is_file() else {}
            seen = sorted(e["at"] for e in entries if e.get("what") in SEAT_CONTENT and rec["id"] in e.get("path", ""))
            if seen and sealed_at.get(d["round"]) and seen[0] < sealed_at[d["round"]]:
                late.append(row)
                row["note"] = "sealed late: a seat's content was sighted at %s, before the seal at %s" % (
                    seen[0], sealed_at[d["round"]])
                out.append(row)
                continue
            if seen and opened_at.get(d["round"]) and seen[-1] > opened_at[d["round"]]:
                early.append(row)
                row["note"] = "opened early: a seat's content was sighted at %s, after the ledger was opened at %s" % (
                    seen[-1], opened_at[d["round"]])
                out.append(row)
                continue
            for v, g in sorted((check.get("banking") or {}).items()):
                if not isinstance(g, dict) or not g.get("ok"):
                    continue
                code = ((banking or {}).get(v) or {}).get("code") or v
                caught = g.get("verdict") in p["caught_by"]
                row["said"][code] = g.get("verdict")
                seats.setdefault(code, [0, 0])
                seats[code][0] += int(caught)
                seats[code][1] += 1
            peered = [PEERED.match(e.get("note", "")) for e in rec["history"] if e["status"] == "PEERED"]
            if peered and peered[0]:                  # the runner's move names the peer's branch and its finding (T8)
                code = codes.get(peered[0].group(1), peered[0].group(1))
                row["said"][code] = peered[0].group(2)
                seats.setdefault(code, [0, 0])
                seats[code][0] += int(peered[0].group(2) == "fault")
                seats[code][1] += 1
            out.append(row)
    return {"seats": seats, "plants": out, "late": late, "early": early, "unplanted": [s for s in SHAPES if s not in shapes],
            "rounds_sealed": len(seals)}


def main(argv):
    arg = lambda k: argv[argv.index(k) + 1] if k in argv else None
    if "--check" in argv:
        bad = problems()
        print("\n".join(bad) or "ok")
        return 1 if bad else 0
    if "--nonce" in argv:
        print(os.urandom(32).hex())
        return 0
    if arg("--seal"):
        raw = pathlib.Path(arg("--seal")).read_bytes()
        m = LEDGER_NAME.fullmatch(pathlib.Path(arg("--seal")).name)
        d = json.loads(raw.decode("utf-8"))
        bad = ledger_problems(d, int(m.group(1)) if m else None)
        if bad:
            print("\n".join(bad))
            return 1
        print(seal_line(raw, d["round"]))
        return 0
    if arg("--measure"):
        print(json.dumps(measure(arg("--measure")), indent=1, ensure_ascii=False))
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
