#!/usr/bin/env python3
"""The intake runner: one round of the intake (the framework's thin path, patch T7, with T7b; draft 1 § 9; main's M54,
M62, M64 and M65; P-885).

One round, in this order, for every claim card the queue's branch has not finished with:

  1. discovery (T3, T7b): every card version not yet in the queue is filed FILED by the runner, its seat code tied to its
     branch by queue/SEAT_CODES.json; the runner sights the card and its decisive script (T4) at the same moment;
  2. the form (T2): a card whose form fails is RETURNED_AT_INTAKE, with the form's reasons; so is a refile the card does
     not declare. A card that a later card refiles is not taken further;
  3. custody (T4): a card whose branch was rewritten past its commit, or whose script is not the one it hashes, is
     RETURNED_AT_INTAKE;
  4. the record check (T6), attached under queue/checks/: a premise arc RETRACTED or superseded returns the card; a
     premise card not VERIFIED, or a premise arc whose own card is not (D6), keeps it FILED, waiting; the firewall's words
     (A3) are a flag to the author, listed in the round's report;
  5. the rerun (T5, rebuilt by T7b): REPRODUCED, with `deciding` set from the record check; RETURNED_AT_INTAKE with its
     reasons; or HEAVY, when the card stays FILED, marked heavy, for the author's machine;
  6. the peer note (T8): a card OFFERED to a peer moves to PEERED once the peer's note, on its own branch, holds the
     runner's check (scripts/queue/peer_note.py), the peer's script rerun in the same sandbox; a note that does not is
     reported and the card stays OFFERED. Offers are made by hand in the trial;
  7. the end of the peer stage (T9): after the peer's note, or 72 hours after the offer with no note that holds, a card
     that decides something goes to AT_BANKING, and a card that decides nothing ends at NOT_BANKED;
  8. banking (T9): the cards AT_BANKING, in queue order (M64 item 13), are checked against the two banking seats'
     sealed verdicts (scripts/queue/banking.py); two verdicts that hold decide the card, as banking.outcome has it.

A later round's peer or banking check is added to the card's check file under queue/checks/, beside its record check.

THE SANDBOX (T7b; main's M62 and M68). Seat code runs as the unprivileged user nobody in a network and a mount namespace,
with its own temporary directories (scripts/queue/rerun.py). Where no such wrap can be made the round goes on, and no seat
code runs: every rerun is HEAVY. `--allow-static-guard` runs seat code without the wrap, on the author's machine and by the
author's choice; the workflow never passes it.

THE QUEUE'S FOLDER (T7b; main's M62). The round reads the folder once, at the start, and holds what it decides in memory.
It writes only after every rerun, and writes nothing if the folder changed while it ran. It closes what it wrote with a
manifest, `.round_manifest.json`, and the record job refuses a file the round did not write (`--check-manifest`).

The queue as the round leaves it must hold its schema (T1, T1b, T7b) and the log its form (T4), or nothing is written.

    python3 scripts/queue/intake.py --queue-dir DIR                   # a round, printed; writes nothing
    python3 scripts/queue/intake.py --queue-dir DIR --write           # and writes the queue's files under DIR
      [--max-cards N] [--limit SECONDS] [--at TIME] [--allow-static-guard]
    python3 scripts/queue/intake.py --check-manifest DIR              # the record job's check of a round's queue
DIR holds `cards/`, `checks/` and `SIGHTINGS.jsonl`: the `queue/` folder of the queue's branch. Run `git fetch --all`
first. Exit 0 when the round ran, 1 when it refused to write or a manifest does not hold."""
import datetime
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


QS = _load("queue_schema_for_intake", HERE / "queue_schema.py")
CF = _load("card_form_for_intake", HERE / "card_form.py")
D = _load("discover_for_intake", HERE / "discover.py")
CU = _load("custody_for_intake", HERE / "custody.py")
RC = _load("record_check_for_intake", HERE / "record_check.py")
RR = _load("rerun_for_intake", HERE / "rerun.py")
PN = _load("peer_note_for_intake", HERE / "peer_note.py")
BK = _load("banking_for_intake", HERE / "banking.py")
PEER_HOURS = 72                    # § 9: an offer with no note that holds goes to banking after 72 hours, marked so
MAX_CARDS = 3                      # cards rerun in one round, so that a round stays inside the job's time


def _now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _move(rec, status, note, at):
    rec["history"].append({"at": at, "status": status, "by": "runner", "note": note[:2000]})
    rec["status"] = status


def _card_text(root, rec):
    r = subprocess.run(["git", "show", "%s:%s" % (rec["commit"], rec["card_path"])], cwd=root, capture_output=True,
                       text=True)
    return r.stdout if r.returncode == 0 else None


def read_queue_dir(qdir):
    qdir = pathlib.Path(qdir)
    cards = D.read_queue(qdir / "cards")
    log = (qdir / "SIGHTINGS.jsonl").read_text(encoding="utf-8") if (qdir / "SIGHTINGS.jsonl").is_file() else ""
    return cards, log


def read_checks(qdir):
    """{id: the check attached to the card} as the queue's folder holds them, read once at the start of a round"""
    out = {}
    for f in sorted(pathlib.Path(qdir, "checks").glob("Q*.json")):
        try:
            out[f.stem] = json.loads(f.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return out


def snapshot(qdir):
    """{relative path: sha256} of every file under the queue's folder"""
    qdir = pathlib.Path(qdir)
    if not qdir.is_dir():
        return {}
    return {str(f.relative_to(qdir)): hashlib.sha256(f.read_bytes()).hexdigest()
            for f in sorted(qdir.rglob("*")) if f.is_file()}


def _hours(a, b):
    f = "%Y-%m-%dT%H:%M:%SZ"
    return (datetime.datetime.strptime(b, f) - datetime.datetime.strptime(a, f)).total_seconds() / 3600


def queue_order(cards):
    """the cards' ids in queue order: by the number of the id, Q0001 first (M64 item 13: banking takes cards so)"""
    return sorted(cards, key=lambda c: (int(c[1:]) if c[1:].isdigit() else float("inf"), c))


def round_(qdir, root=ROOT, record_root=ROOT, refs=None, at=None, limit=RR.TIME_LIMIT, max_cards=MAX_CARDS,
           prefix=None, allow_static=False, codes=None, seats_file=None):
    """one round: (the cards after it, the log after it, {id: attachment}, report lines, exit status). The queue's folder
    is read once, at the start; what the round decides is held in memory and written only after every rerun (main's M62)"""
    at = at or _now()
    cards, log_text = read_queue_dir(qdir)
    cards = json.loads(json.dumps(cards))
    old_checks = read_checks(qdir)
    entries, bad = CU.read_log(log_text)
    if bad:
        return cards, log_text, {}, ["the sighting log does not hold its form: " + "; ".join(bad[:3])], 1
    if prefix is None:
        prefix, guard = RR.sandbox_prefix()
    else:
        guard = " ".join(prefix) or "no sandbox"
    # T7b (M64 item 4): where no sandbox can be made, the round goes on and no seat code runs: each rerun is HEAVY
    report, attached, new_lines = ["the network guard: %s" % (guard if prefix else
                                                               guard + "; no seat code runs this round")], {}, []

    def attach(cid):
        """the card's check, as filed with what this round adds: a later round's peer or banking part is added to it,
        and never takes the place of the record check filed before"""
        if cid not in attached:
            attached[cid] = json.loads(json.dumps(old_checks.get(cid, {})))
        return attached[cid]
    seen = {}
    for cid, r in cards.items():                      # the versions already filed, keyed on branch, path and blob (C25)
        rc = subprocess.run(["git", "rev-parse", "%s:%s" % (r["commit"], r["card_path"])], cwd=root, capture_output=True,
                            text=True)
        if rc.returncode == 0:
            seen[(r["branch"], r["card_path"], rc.stdout.strip())] = cid
    new, found = D.discover(cards, refs if refs is not None else D.branches(), root=root, at=at, seen_blobs=seen,
                            codes=codes)
    report += found
    for cid, rec in new.items():
        for path, what in [(rec["card_path"], "card")] + [(p, "script") for p in _script_path(root, rec)]:
            e = CU.sight(root, entries + new_lines, rec["branch"], rec["commit"], path, what, at)
            if e:
                new_lines.append(e)
    cards.update(new)
    entries = entries + new_lines
    done = 0
    refiled = {old for r in cards.values() for old in r["refiles"]}
    for cid in sorted(cards):
        rec = cards[cid]
        if rec["status"] != "FILED" or rec["heavy"]:
            continue
        if cid in refiled:                            # Review 88's A24: a refiled card's old version is not taken further
            report.append("%s is refiled by a later card, and is not taken further" % cid)
            continue
        text = _card_text(root, rec)
        if text is None:
            _move(rec, "RETURNED_AT_INTAKE", "the card is not at its sealed commit", at)
            continue
        problems = CF.form_problems(text)
        if "a refile of" in rec["history"][0]["note"] and "does not declare" in rec["history"][0]["note"]:
            problems.append("it refiles a card it does not declare: write 'card id: refiles Q<nnnn>'")
        if problems:
            _move(rec, "RETURNED_AT_INTAKE", "the form: " + "; ".join(problems), at)
            report.append("%s RETURNED_AT_INTAKE (form)" % cid)
            continue
        problems = CU.custody_problems(root, rec, entries)
        if problems:
            _move(rec, "RETURNED_AT_INTAKE", "custody: " + "; ".join(problems), at)
            report.append("%s RETURNED_AT_INTAKE (custody)" % cid)
            continue
        check = attach(cid)
        check.update(RC.check(record_root, text, cards))
        if check["firewall"]:
            report.append("%s FLAG for the author (A3): %s" % (cid, ", ".join(check["firewall"])))
        if check["retracted"]["premises"]:
            _move(rec, "RETURNED_AT_INTAKE", "the record: " + "; ".join(check["retracted"]["premises"]), at)
            report.append("%s RETURNED_AT_INTAKE (a premise retracted or superseded)" % cid)
            continue
        if check["waits_on"]:
            report.append("%s waits on %s (D6)" % (cid, ", ".join(check["waits_on"])))
            continue
        if done >= max_cards:
            report.append("%s left for the next round (%d cards rerun in this one)" % (cid, max_cards))
            continue
        done += 1
        res = RR.rerun(root, rec["commit"], text, limit=limit, prefix=prefix, allow_static=allow_static)
        check["rerun"] = res
        if res["status"] == "REPRODUCED":
            rec["deciding"] = bool(check["deciding"])
            _move(rec, "REPRODUCED", "the rerun at the sealed commit: %d decisive lines, hash %s; the control exited 1; "
                  "guard: %s" % (res["decisive"]["lines"], res["decisive"]["sha256"], res["guard"]), at)
            report.append("%s REPRODUCED (deciding: %s)" % (cid, rec["deciding"]))
        elif res["status"] == "HEAVY":
            rec["heavy"] = True
            report.append("%s HEAVY, for the author's machine: %s" % (cid, "; ".join(res["reasons"])))
        else:
            _move(rec, "RETURNED_AT_INTAKE", "the rerun: " + "; ".join(res["reasons"]), at)
            report.append("%s RETURNED_AT_INTAKE (rerun)" % cid)
    # T8: a card OFFERED to a peer moves to PEERED when the peer's note, on the peer's own branch, holds the runner's check
    for cid in sorted(cards):
        rec = cards[cid]
        if rec["status"] != "OFFERED":
            continue
        text = _card_text(root, rec)
        for key, ref in (refs if refs is not None else D.branches()):
            branch = ref.split("/", 1)[1] if ref.startswith("origin/") else ref
            rc = subprocess.run(["git", "log", "-1", "--format=%H", ref, "--", PN.note_path(cid)], cwd=root,
                                capture_output=True, text=True)
            commit = rc.stdout.strip()
            if rc.returncode != 0 or not commit:
                continue
            raw = subprocess.run(["git", "show", "%s:%s" % (commit, PN.note_path(cid))], cwd=root, capture_output=True,
                                 text=True)
            if raw.returncode != 0:
                continue                                  # the note was removed at the branch's head
            try:
                note = json.loads(raw.stdout)
            except ValueError:
                report.append("%s: the peer note on %s is not JSON" % (cid, ref))
                continue
            paths = [(PN.note_path(cid), "peer")]
            if isinstance(note, dict) and isinstance(note.get("script"), dict) and note["script"].get("path"):
                paths.append((note["script"]["path"], "script"))
            for path, what in paths:
                e = CU.sight(root, entries, branch, commit, path, what, at)
                if e:
                    new_lines.append(e)
                    entries = entries + [e]
            res = PN.check(root, note, commit, branch, rec, text or "", entries, limit=limit, prefix=prefix,
                           allow_static=allow_static)
            attach(cid)["peer"] = dict(res, branch=branch, commit=commit)
            if res["ok"]:
                _move(rec, "PEERED", "the peer note on %s at %s: %s, graded %s%s" % (
                    branch, commit[:9], note["finding"], res["grade"],
                    "; a check from another family" if res["other_family"] else ""), at)
                report.append("%s PEERED (%s, %s)" % (cid, note["finding"], res["grade"]))
                break
            report.append("%s: the peer note on %s is refused: %s" % (cid, ref, "; ".join(res["reasons"])))
    # T9: the end of the peer stage. A deciding card goes to banking once its peer's note holds, or when no note has held
    # 72 hours after the offer; a card that decides nothing ends there at NOT_BANKED (T7b, M64 item 10)
    order = queue_order(cards)
    for cid in order:
        rec = cards[cid]
        if rec["deciding"] not in (True, False):
            continue
        if rec["status"] == "PEERED":
            why = "after the peer's note"
        elif rec["status"] == "OFFERED" and _hours(
                [e["at"] for e in rec["history"] if e["status"] == "OFFERED"][-1], at) >= PEER_HOURS:
            why = "no peer check: no note held within %d hours of the offer" % PEER_HOURS
        else:
            continue
        if rec["deciding"]:
            _move(rec, "AT_BANKING", "to banking " + why if why.startswith("after") else why, at)
            report.append("%s AT_BANKING (%s)" % (cid, why))
        else:
            _move(rec, "NOT_BANKED", "it decides nothing; its peer stage is over (%s)" % why, at)
            report.append("%s NOT_BANKED (it decides nothing; %s)" % (cid, why))
    the_seats = BK.seats(seats_file) if seats_file else BK.seats()
    waiting = [cid for cid in order if cards[cid]["status"] == "AT_BANKING"]
    if waiting:
        report.append("the banking queue, in queue order (M64 item 13): " + ", ".join(waiting))
    for cid in waiting:
        rec = cards[cid]
        if rec["status"] != "AT_BANKING":
            continue
        if not the_seats:
            report.append("%s waits at banking: queue/BANKING_SEATS.json names no two seats yet" % cid)
            continue
        for e in BK.sightings(root, entries, cid, the_seats, at):
            new_lines.append(e)
            entries = entries + [e]
        text = _card_text(root, rec) or ""
        seal_at = {}
        for v, s in the_seats.items():
            c, b = BK._at(root, "origin/" + s["branch"], BK.paths(cid)["seal"])
            e = CU.first_sighting(entries, s["branch"], BK.paths(cid)["seal"], b) if b else None
            seal_at[v] = e["at"] if e else None
        if all(seal_at.values()):                     # main's M71 point 2: when a seat may open its verdict
            report.append("%s at banking: both seals first sighted by %s; verdicts may be opened from the next round on, "
                          "and one first sighted by then is refused (K1)" % (cid, max(seal_at.values())))
        else:
            report.append("%s at banking: seals sighted: %s; no verdict may be opened yet (K1)" % (cid, ", ".join(
                "%s at %s" % (v, a) if a else "%s not yet" % v for v, a in sorted(seal_at.items()))))
        got, before = {}, attach(cid).get("banking") or {}
        for v, s in sorted(the_seats.items()):
            other = seal_at["V2" if v == "V1" else "V1"]
            got[v] = BK.check_verdict(root, cid, rec, text, s, entries, other, limit=limit, prefix=prefix,
                                      allow_static=allow_static, cached=before.get(v))
        attach(cid)["banking"] = got
        if all(g["ok"] for g in got.values()):
            peer = attach(cid).get("peer") or {}
            status, note = BK.outcome(rec, got["V1"]["verdict"], got["V2"]["verdict"], peer.get("other_family"), the_seats)
            if status:
                _move(rec, status, note, at)
                report.append("%s %s (%s)" % (cid, status, note))
            else:
                report.append("%s waits at banking: %s" % (cid, note))
        else:
            report.append("%s at banking: %s" % (cid, "; ".join("%s: %s" % (v, "; ".join(g["reasons"]))
                                                             for v, g in sorted(got.items()) if not g["ok"])))
    log_after = CU.append(log_text, new_lines)
    problems = QS.queue_problems({k: json.dumps(v) for k, v in cards.items()}) + CU.read_log(log_after)[1]
    if problems:
        return cards, log_after, attached, report + ["the queue would not hold its schema: " + "; ".join(problems[:5])], 1
    return cards, log_after, attached, report, 0


def _script_path(root, rec):
    text = _card_text(root, rec) or ""
    m = CF.SCRIPT.match(CF.read(text)[1].get("decisive script", ""))
    return [m.group(1)] if m else []


MANIFEST = ".round_manifest.json"


def write(qdir, cards, log_text, attached, before=None):
    """write the round's queue: refused when the folder changed while the round ran (`before`, its snapshot at the start),
    and closed by a manifest of what the round wrote, which the record job checks (main's M62). -> problems, [] when done"""
    qdir = pathlib.Path(qdir)
    if before is not None:
        now = snapshot(qdir)
        changed = sorted(set(before) ^ set(now) | {k for k in before if k in now and before[k] != now[k]})
        if changed:
            return ["the queue's folder changed while the round ran, so the round writes nothing: %s" % ", ".join(changed[:5])]
    (qdir / "cards").mkdir(parents=True, exist_ok=True)
    (qdir / "checks").mkdir(parents=True, exist_ok=True)
    for cid, rec in cards.items():
        (qdir / "cards" / ("%s.json" % cid)).write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for cid, check in attached.items():
        (qdir / "checks" / ("%s.json" % cid)).write_text(json.dumps(check, indent=1, ensure_ascii=False) + "\n",
                                                        encoding="utf-8")
    (qdir / "SIGHTINGS.jsonl").write_text(log_text, encoding="utf-8")
    written = {k: v for k, v in snapshot(qdir).items() if k != MANIFEST}
    (qdir / MANIFEST).write_text(json.dumps(written, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return []


def manifest_problems(qdir):
    """the record job's check: every file of the round's queue is one the round wrote, with the content it wrote"""
    qdir = pathlib.Path(qdir)
    try:
        written = json.loads((qdir / MANIFEST).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ["the round's queue has no manifest of what it wrote"]
    now = {k: v for k, v in snapshot(qdir).items() if k != MANIFEST}
    extra, lost = sorted(set(now) - set(written)), sorted(set(written) - set(now))
    changed = sorted(k for k in set(now) & set(written) if now[k] != written[k])
    return (["a file the round did not write: %s" % ", ".join(extra[:5])] if extra else []) + \
           (["a file the round wrote is missing: %s" % ", ".join(lost[:5])] if lost else []) + \
           (["a file is not as the round wrote it: %s" % ", ".join(changed[:5])] if changed else [])


def main(argv):
    arg = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    if "--check-manifest" in argv:
        bad = manifest_problems(arg("--check-manifest"))
        for b in bad:
            print(b)
        print("%d problem(s) in the round's manifest" % len(bad))
        return 1 if bad else 0
    qdir = arg("--queue-dir")
    if not qdir:
        print(__doc__)
        return 1
    before = snapshot(qdir)
    cards, log_text, attached, report, status = round_(
        qdir, at=arg("--at"), limit=int(arg("--limit", RR.TIME_LIMIT)), max_cards=int(arg("--max-cards", MAX_CARDS)),
        allow_static="--allow-static-guard" in argv)
    for line in report:
        print(line)
    if status == 0 and "--write" in argv:
        bad = write(qdir, cards, log_text, attached, before)
        for b in bad:
            print(b)
        if bad:
            return 1
        print("written to %s" % qdir)
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
