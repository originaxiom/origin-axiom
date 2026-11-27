#!/usr/bin/env python3
"""Custody: the sighting log and the custody check (the framework's thin path, patch T4; draft 1 § 9; M54; P-885).

THE SIGHTING LOG, `queue/SIGHTINGS.jsonl`, on the queue's branch: one line for each file version the runner has seen, the
first time it sees it: {at, branch, commit, path, blob, what}, `what` being "card" or "script". The log is the runner's own
clock. A commit's date is written by whoever commits and can be anything; the time at which the runner first saw a blob
cannot be set by a seat. The log is append-only: every version of it on the queue's branch begins with the version before.

THE CUSTODY CHECK, on a filed card, before its rerun:
  1. the card's sealed commit is still on its branch (a branch rewritten past it returns the card);
  2. the card at that commit is the version the runner sighted and filed;
  3. the decisive script at that commit is there, and its SHA-256 opens with the 16 hex the card gives;
  4. the runner sighted the card no later than it filed it.

WHAT CUSTODY MEANS HERE, decided in the patch (M54) and said for main. The draft asks that the expectations be committed
before the output. On a claim card the expectation is the card itself: its decisive lines' hash and its failing control.
The runner sights the card, then reruns the script at the sealed commit, so the output it compares is produced after the
expectation was fixed, by the runner, and no seat can fit the one to the other. What no tool can see is how many times a
seat ran its script privately before it wrote the card; the failing control, the peer and the two banking seats are the
answer to that, not custody.

THE QUEUE'S HISTORY (an addition to T1's schema, which reads one version of a file): on the queue's branch, every version of
a card file keeps the fields that never change (its id, seat code, branch, commit, card path, refiles), and its history
begins with the history of the version before. A card's past cannot be rewritten by a later commit.

    python3 scripts/queue/custody.py --log queue/SIGHTINGS.jsonl            # the log's form
    python3 scripts/queue/custody.py --history REF [--root DIR]             # the log and the cards along REF's history
    python3 scripts/queue/custody.py --card queue/cards/Q0001.json --log queue/SIGHTINGS.jsonl   # one card's custody
Exit 0 when all holds, 1 when something does not."""
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


QS = _load("queue_schema_for_custody", HERE / "queue_schema.py")
CF = _load("card_form_for_custody", HERE / "card_form.py")
LOG = "queue/SIGHTINGS.jsonl"
LINE_FIELDS = ("at", "branch", "commit", "path", "blob", "what")
WHATS = ("card", "script")
FIXED = ("id", "seat_code", "branch", "commit", "card_path", "refiles")


def git(root, *args):
    r = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr.strip()


# --- the log -----------------------------------------------------------------------------------------------------------
def read_log(text):
    """(entries, problems): each line one sighting of the log's form, the times never going back, no version twice. A
    line that does not hold its form is said and left out, and never stops the reading (Review 88's B22)"""
    entries, bad, seen = [], [], set()
    for i, line in enumerate(text.splitlines(), 1):
        try:
            e = json.loads(line)
        except ValueError:
            bad.append("line %d is not JSON" % i)
            continue
        if not isinstance(e, dict) or sorted(e) != sorted(LINE_FIELDS):
            bad.append("line %d does not hold exactly %s" % (i, ", ".join(LINE_FIELDS)))
            continue
        before = len(bad)
        if not QS.at_ok(e["at"]):
            bad.append("line %d: at %r is not YYYY-MM-DDTHH:MM:SSZ" % (i, e["at"]))
        if not isinstance(e["commit"], str) or not QS.COMMIT.fullmatch(e["commit"]) \
                or not isinstance(e["blob"], str) or not QS.COMMIT.fullmatch(e["blob"]):
            bad.append("line %d: commit and blob are not full 40-hex ids" % i)
        if not QS.branch_ok(e["branch"]):
            bad.append("line %d: branch %r is not a branch's name" % (i, e["branch"]))
        if not isinstance(e["path"], str) or not e["path"] or e["path"].startswith("/") or ".." in e["path"].split("/"):
            bad.append("line %d: path %r is not a path of the repository" % (i, e["path"]))
        if e["what"] not in WHATS:
            bad.append("line %d: what %r is not one of %s" % (i, e["what"], ", ".join(WHATS)))
        if len(bad) > before:
            continue
        if entries and e["at"] < entries[-1]["at"]:
            bad.append("line %d goes back in time" % i)
        key = (e["branch"], e["path"], e["blob"])
        if key in seen:
            bad.append("line %d sights again a version already sighted" % i)
        seen.add(key)
        entries.append(e)
    return entries, bad


def first_sighting(entries, branch, path, blob):
    for e in entries:
        if (e["branch"], e["path"], e["blob"]) == (branch, path, blob):
            return e
    return None


def sight(root, entries, branch, commit, path, what, at):
    """the log's new line for this file at this commit, or None when it is not there or was sighted before"""
    rc, out, _ = git(root, "rev-parse", "%s:%s" % (commit, path))
    if rc != 0:
        return None
    blob = out.strip()
    if first_sighting(entries, branch, path, blob):
        return None
    return {"at": at, "branch": branch, "commit": commit, "path": path, "blob": blob, "what": what}


def append(text, new_entries):
    """the log with the new lines at its end; nothing before them changes"""
    body = text if not text or text.endswith("\n") else text + "\n"
    return body + "".join(json.dumps(e, sort_keys=True) + "\n" for e in new_entries)


# --- custody of one card -----------------------------------------------------------------------------------------------
def custody_problems(root, rec, entries, ref=None):
    """the reasons a filed card fails custody; [] when it holds. `ref` is the ref its branch is read at (origin/<branch>
    unless given)"""
    ref = ref or ("origin/" + rec["branch"])
    bad = []
    rc, _, _ = git(root, "merge-base", "--is-ancestor", rec["commit"], ref)
    if rc != 0:
        bad.append("the sealed commit %s is no longer on %s: the branch was rewritten past it" % (rec["commit"][:9], ref))
    rc, out, _ = git(root, "rev-parse", "%s:%s" % (rec["commit"], rec["card_path"]))
    if rc != 0:
        return bad + ["the card is not at its sealed commit"]
    blob = out.strip()
    seen = first_sighting(entries, rec["branch"], rec["card_path"], blob)
    if seen is None:
        bad.append("the card at its sealed commit was never sighted by the runner")
    elif seen["at"] > rec["history"][0]["at"]:
        bad.append("the card was filed (%s) before the runner sighted it (%s)" % (rec["history"][0]["at"], seen["at"]))
    rc, text, _ = git(root, "cat-file", "blob", blob)
    fields = CF.read(text)[1]
    m = CF.SCRIPT.match(fields.get("decisive script", ""))
    if not m:
        return bad + ["the card names no decisive script in its form"]
    path, want = m.group(1), CF.HEX16.search(fields["decisive script"]).group(1)
    p = subprocess.run(["git", "cat-file", "blob", "%s:%s" % (rec["commit"], path)], cwd=root, capture_output=True)
    if p.returncode != 0:
        bad.append("the decisive script %s is not at the sealed commit" % path)
    elif hashlib.sha256(p.stdout).hexdigest()[:16] != want:
        bad.append("the decisive script at the sealed commit is not the one the card hashes (%s, the card says %s)"
                   % (hashlib.sha256(p.stdout).hexdigest()[:16], want))
    return bad


# --- the queue's history -----------------------------------------------------------------------------------------------
def versions(root, ref, path):
    """the texts of a file along the first-parent history of ref, oldest first; a commit that deletes it gives None (Review
    88's B12: a deletion was passed over)"""
    rc, out, _ = git(root, "log", "--first-parent", "--reverse", "--format=%H", ref, "--", path)
    if rc != 0:
        return None
    texts = []
    for c in out.split():
        rc, text, _ = git(root, "show", "%s:%s" % (c, path))
        texts.append((c, text if rc == 0 else None))
    return texts


def history_problems(root, ref):
    """the log and every card file along ref's history: each version begins with the one before (the log), or keeps its
    fixed fields and extends its history (a card); neither is ever deleted"""
    bad = []
    vs = versions(root, ref, LOG)
    if vs is None:
        return ["the history of %s cannot be read" % ref]
    for (c0, a), (c1, b) in zip(vs, vs[1:]):
        if a is not None and b is None:
            bad.append("%s is deleted at %s" % (LOG, c1[:9]))
        elif a is not None and not b.startswith(a):
            bad.append("%s at %s does not begin with its version at %s: the log was rewritten" % (LOG, c1[:9], c0[:9]))
    rc, out, _ = git(root, "log", "--format=", "--name-only", ref, "--", QS.CARDS)
    for path in sorted(set(p for p in out.split() if p.endswith(".json"))):
        vs = versions(root, ref, path) or []
        for (c0, a), (c1, b) in zip(vs, vs[1:]):
            if a is not None and b is None:
                bad.append("%s is deleted at %s" % (path, c1[:9]))
                continue
            if a is None:
                continue
            try:
                old, new = json.loads(a), json.loads(b)
                if any(old.get(f) != new.get(f) for f in FIXED):
                    bad.append("%s at %s changes a field that never changes" % (path, c1[:9]))
                if new.get("history", [])[:len(old.get("history", []))] != old.get("history", []):
                    bad.append("%s at %s rewrites the card's past history" % (path, c1[:9]))
            except (ValueError, AttributeError, TypeError):
                bad.append("%s at %s or %s cannot be read" % (path, c0[:9], c1[:9]))
    return bad


def main(argv):
    bad = []
    log_text = ""
    if "--log" in argv:
        p = pathlib.Path(argv[argv.index("--log") + 1])
        log_text = p.read_text(encoding="utf-8") if p.is_file() else ""
        bad += read_log(log_text)[1]
    root = pathlib.Path(argv[argv.index("--root") + 1]) if "--root" in argv else ROOT     # T7b: the queue's own checkout
    if "--history" in argv:
        bad += history_problems(root, argv[argv.index("--history") + 1])
    if "--card" in argv:
        rec = json.loads(pathlib.Path(argv[argv.index("--card") + 1]).read_text(encoding="utf-8"))
        bad += custody_problems(root, rec, read_log(log_text)[0])
    for b in bad:
        print(b)
    print("%d problem(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
