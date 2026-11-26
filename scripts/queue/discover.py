#!/usr/bin/env python3
"""Discovery: the intake's search for claim cards (the framework's thin path, patch T3; draft 1 § 9, main's M54; P-885).

Reads every seat branch named in docs/HARVEST_LEDGER.md's Pins table (as scripts/checks/seat_intake.py reads it) and
main itself, and lists every claim card at each branch's head: a file under relays/claims/ whose first line opens
'# CLAIM CARD'. A card is one version of one file: (branch, path, the file's blob). A version the queue has not seen is
filed as a new card, FILED by the runner, with the next free id. Nothing is checked here but what filing needs:

  - a branch that cannot be reached is reported, and the others are read (never a stop);
  - a card whose seat code is not a seat code cannot be filed, because the queue holds codes only; it is reported to be
    told to its seat;
  - a new version of a card already in the queue, or a card with the same decisive script's hash as one in the queue, is
    a refile; it is filed, linked to the card it refiles, and the report says whether the card itself said so (a refile
    it did not declare is the form's to return, in the runner, T7).

The form check (T2), custody (T4), the rerun (T5) and the record check (T6) come after, in the runner.

    python3 scripts/queue/discover.py                          # prints what would be filed; writes nothing
    python3 scripts/queue/discover.py --queue DIR --write      # writes the new cards' files into DIR
    python3 scripts/queue/discover.py --at 2026-11-26T12:00:00Z  # the time to stamp (else now, in UTC)
Run `git fetch --all` first; discovery reads the refs it finds."""
import datetime
import importlib.util
import json
import pathlib
import re
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


QS = _load("queue_schema_for_discovery", HERE / "queue_schema.py")
CF = _load("card_form_for_discovery", HERE / "card_form.py")
CLAIMS = "relays/claims/"
SCRIPT_HASH = re.compile(r"SHA-256 ([0-9a-f]{16})")


def git(root, *args):
    r = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr.strip()


def branches(root=ROOT, main="origin/main"):
    """[(seat key, ref)]: main, then every seat of the Pins table"""
    intake = _load("seat_intake_for_discovery", pathlib.Path(root) / "scripts" / "checks" / "seat_intake.py")
    intake.ROOT = pathlib.Path(root)
    return [("main", main)] + [(key, resolve(root, ref)) for key, ref, _pin in intake.pins()]


def resolve(root, ref):
    """the remote-tracking ref a Pins row names. The ledger masks some prefixes (`<v>/`), so a ref that does not resolve
    as written is matched on its last segment, as harvest_debt.py's _resolve_branch does; it is kept as written when no
    single ref matches, and is then reported as unreadable"""
    if git(root, "rev-parse", "--verify", "-q", ref + "^{commit}")[0] == 0:
        return ref
    remote, short = ref.split("/", 1)[0], ref.rsplit("/", 1)[-1]
    rc, out, _ = git(root, "for-each-ref", "--format=%(refname:short)", "refs/remotes/%s" % remote)
    hits = [r for r in out.split() if r.rsplit("/", 1)[-1] == short]
    return hits[0] if len(hits) == 1 else ref


def cards_on(root, ref):
    """(the cards at the ref's head as [(path, blob, commit, text)], None) or ([], why the ref cannot be read)"""
    rc, out, err = git(root, "ls-tree", "-r", ref, "--", CLAIMS)
    if rc != 0:
        return [], "cannot be read (%s)" % (err.splitlines()[0] if err else "no such ref")
    found = []
    for line in out.splitlines():
        meta, path = line.split("\t", 1)
        mode, kind, blob = meta.split()
        if kind != "blob" or not path.endswith(".md"):
            continue
        rc, text, _ = git(root, "cat-file", "blob", blob)
        if rc != 0 or not text.startswith("# CLAIM CARD"):
            continue
        rc, commit, _ = git(root, "log", "-1", "--format=%H", ref, "--", path)
        found.append((path, blob, commit.strip(), text))
    return found, None


def script_hash(fields):
    m = SCRIPT_HASH.search(fields.get("decisive script", ""))
    return m.group(1) if m else None


def discover(queue, refs, root=ROOT, at=None, seen_blobs=None):
    """queue: {id: record}; refs: [(key, ref)]. -> (new records, report lines). `seen_blobs` maps a card's blob to the id
    it was filed under; the runner keeps it with the sighting log (T4), and a test may pass it"""
    at = at or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    seen_blobs = dict(seen_blobs or {})
    by_place = {(r["branch"], r["card_path"]): i for i, r in sorted(queue.items())}
    by_script = {}
    for cid, rec in sorted(queue.items()):            # the decisive script of each card already filed, read at its commit
        rc, text, _ = git(root, "show", "%s:%s" % (rec["commit"], rec["card_path"]))
        h = script_hash(CF.read(text)[1]) if rc == 0 else None
        if h:
            by_script.setdefault(h, cid)
    numbers = [int(i[1:]) for i in queue]
    report, new = [], {}
    for key, ref in refs:
        found, why = cards_on(root, ref)
        if why:
            report.append("%s (%s): %s; its cards are not read this round" % (key, ref, why))
            continue
        for path, blob, commit, text in found:
            if blob in seen_blobs:
                continue
            title, fields, _layout = CF.read(text)
            code = fields.get("seat code", "")
            if title is None or QS.code_problems(code):
                report.append("%s %s: not filed, its seat code %r is not a seat code; to be told to its seat"
                              % (ref, path, code))
                continue
            branch = ref.split("/", 1)[1] if ref.startswith("origin/") else ref
            earlier = []
            if (branch, path) in by_place:
                earlier.append(by_place[(branch, path)])
            h = script_hash(fields)
            if h and h in by_script and by_script[h] not in earlier:
                earlier.append(by_script[h])
            n = max(numbers or [0]) + 1
            numbers.append(n)
            cid = "Q%04d" % n
            said = CF.CARD_ID.fullmatch(fields.get("card id", "") or "x")
            declared = said.group(1) if said and said.group(1) else None
            if earlier and declared not in earlier:
                note = "found on its branch; a refile of %s it does not declare" % ", ".join(earlier)
            elif declared and declared not in earlier:
                note = "found on its branch; it says it refiles %s, which discovery does not link" % declared
            else:
                note = "found on its branch" + ("; refiles %s" % ", ".join(earlier) if earlier else "")
            rec = {"id": cid, "seat_code": code, "branch": branch, "commit": commit, "card_path": path,
                   "title": title[:240], "status": "FILED", "deciding": None, "heavy": False,
                   "refiles": sorted(set(earlier + ([declared] if declared and declared in queue else []))),
                   "history": [{"at": at, "status": "FILED", "by": "runner", "note": note}]}
            new[cid] = rec
            seen_blobs[blob] = cid
            by_place[(branch, path)] = cid
            if h:
                by_script.setdefault(h, cid)
            report.append("%s: %s %s (%s)" % (cid, ref, path, note))
    return new, report


def read_queue(path):
    p = pathlib.Path(path)
    return {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in sorted(p.glob("Q*.json"))} if p.is_dir() else {}


def main(argv):
    qdir = argv[argv.index("--queue") + 1] if "--queue" in argv else str(ROOT / QS.CARDS)
    at = argv[argv.index("--at") + 1] if "--at" in argv else None
    queue = read_queue(qdir)
    seen = {}
    for cid, r in queue.items():                      # the blobs already filed, read from their own branches
        rc, out, _ = git(ROOT, "rev-parse", "%s:%s" % (r["commit"], r["card_path"]))
        if rc == 0:
            seen[out.strip()] = cid
    new, report = discover(queue, branches(), at=at, seen_blobs=seen)
    for line in report:
        print(line)
    bad = QS.queue_problems({k: json.dumps(v) for k, v in {**queue, **new}.items()})
    if bad:
        print("the queue would not hold its schema: " + "; ".join(bad[:5]))
        return 1
    if "--write" in argv:
        pathlib.Path(qdir).mkdir(parents=True, exist_ok=True)
        for cid, rec in new.items():
            (pathlib.Path(qdir) / ("%s.json" % cid)).write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n",
                                                               encoding="utf-8")
    print("%d new card(s)%s" % (len(new), ", written to %s" % qdir if "--write" in argv and new else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
