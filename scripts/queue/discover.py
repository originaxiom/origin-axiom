#!/usr/bin/env python3
"""Discovery: the intake's search for claim cards (the framework's thin path, patch T3; draft 1 § 9, main's M54; P-885).

Reads every seat branch named in docs/HARVEST_LEDGER.md's Pins table (as scripts/checks/seat_intake.py reads it) and
main itself, and lists every claim card at each branch's head: a file under relays/claims/ whose first line opens
'# CLAIM CARD'. A card is one version of one file: (branch, path, the file's blob). A version the queue has not seen is
filed as a new card, FILED by the runner, with the next free id. Nothing is checked here but what filing needs:

  - a branch that cannot be reached is reported, and the others are read (never a stop);
  - a card whose seat code is not a seat code cannot be filed, because the queue holds codes only; it is reported to be
    told to its seat;
  - a new version of a card already in the queue, or a card with the same decisive script's hash and decisive lines'
    hash as one in the queue, is a refile; it is filed, linked to the card it refiles, and the report says whether the card itself said so (a refile
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
    """[(seat key, ref)]: main, then every seat of HARVEST_LEDGER's Pins table. A row whose branch is masked
    (`origin/<v>/...`) is resolved on its mask; a row whose branch cell names no `origin/` ref is kept as written, so that
    discovery reports it as unreadable and never passes over it (main's M66: the SM seat's row, written `<remote>/...`,
    was dropped in silence and its cards went unseen)"""
    led = pathlib.Path(root, "docs", "HARVEST_LEDGER.md")
    text = led.read_text(encoding="utf-8") if led.is_file() else ""
    sec = re.search(r"^## Pins.*?(?=^## |\Z)", text, re.M | re.S)
    out = [("main", main)]
    for line in (sec.group(0).splitlines() if sec else []):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 3 or not re.fullmatch(r"[a-z0-9]+", c[0]) or not re.fullmatch(r"`?[0-9a-f]{7,40}`?", c[2]):
            continue
        b = re.search(r"origin/[^`\s)]+", c[1])
        out.append((c[0], resolve(root, b.group(0)) if b else "(the Pins row's branch %r names no origin/ ref)" % c[1]))
    return out


def resolve(root, ref):
    """the remote-tracking ref a Pins row names. The ledger masks some prefixes (`<v>/`): such a ref is matched with the
    masked segment as any one segment and every other segment as written. A ref with no mask is read as written only
    (Review 88's C21: matching on the last segment alone took `origin/sm/banking` for `origin/sm2/banking`). It is kept as
    written when nothing single matches, and is then reported as unreadable"""
    if git(root, "rev-parse", "--verify", "-q", ref + "^{commit}")[0] == 0 or "<v>" not in ref:
        return ref
    remote = ref.split("/", 1)[0]
    pattern = re.compile("^" + "/".join("[^/]+" if part == "<v>" else re.escape(part) for part in ref.split("/")) + "$")
    rc, out, _ = git(root, "for-each-ref", "--format=%(refname:short)", "refs/remotes/%s" % remote)
    hits = [r for r in out.split() if pattern.match(r)]
    return hits[0] if len(hits) == 1 else ref


def code_for(branch, codes, known):
    """(the seat code of a branch, or None, and why not): an exact key first; else a masked key (`<v>/<rest>`, main's M66)
    matches a branch of one segment more and the same rest, and is refused when two known branches match it"""
    if branch in codes:
        return codes[branch], None
    hits = [k for k in codes if k.startswith("<v>/") and branch.split("/", 1)[-1] == k[4:] and "/" in branch]
    if len(hits) != 1:
        return None, "its branch %s is not in queue/SEAT_CODES.json" % branch
    key = hits[0]
    same = sorted(b for b in set(known) if "/" in b and b.split("/", 1)[1] == key[4:])
    if len(same) > 1:
        return None, "two branches (%s) match the masked key %s in queue/SEAT_CODES.json" % (", ".join(same), key)
    return codes[key], None


def seat_codes(path=None):
    """{branch: seat code}: main's table, queue/SEAT_CODES.json (M64 item 8, M65)"""
    p = pathlib.Path(path) if path else ROOT / "queue" / "SEAT_CODES.json"
    try:
        return dict(json.loads(p.read_text(encoding="utf-8")).get("codes", {}))
    except (OSError, ValueError):
        return {}


def cards_on(root, ref):
    """(the cards at the ref's head as [(path, blob, commit, text)], what is not read as a card [(path, why)], None) or
    ([], [], why the ref cannot be read). Read with `ls-tree -z`, so a name with any character is kept whole (A19)"""
    r = subprocess.run(["git", "ls-tree", "-r", "-z", ref, "--", CLAIMS], cwd=root, capture_output=True)
    if r.returncode != 0:
        err = r.stderr.decode("utf-8", "replace").strip()
        return [], [], "cannot be read (%s)" % (err.splitlines()[0] if err else "no such ref")
    found, passed = [], []
    for entry in r.stdout.split(b"\0"):
        if not entry:
            continue
        meta, raw = entry.split(b"\t", 1)
        mode, kind, blob = meta.decode().split()
        path = raw.decode("utf-8", "surrogateescape")
        if kind != "blob" or not path.endswith(".md"):
            continue
        rc, text, _ = git(root, "cat-file", "blob", blob)
        if rc != 0:
            continue
        if not text.startswith("# CLAIM CARD"):
            if "# CLAIM CARD" in text:                # A19: a fenced or indented title is said, not passed over
                passed.append((path, "it holds a card's title, but its first line is not the title"))
            continue
        rc, commit, _ = git(root, "log", "-1", "--format=%H", ref, "--", path)
        found.append((path, blob, commit.strip(), text))
    return found, passed, None


def _blob(root, commit, path):
    rc, out, _ = git(root, "rev-parse", "--verify", "-q", "%s:%s" % (commit, path))
    return out.strip() if rc == 0 else None


def is_mains(root, main_ref, ref, path, blob):
    """main's card carried by a seat's branch, which the seat never changed (M68 point 4, M70 point 4): the same path and
    blob as on main now, or as at the merge-base of the branch and main, when main has filed the card again since"""
    if _blob(root, main_ref, path) == blob:
        return True
    rc, base, _ = git(root, "merge-base", main_ref, ref)
    return rc == 0 and bool(base.strip()) and _blob(root, base.strip(), path) == blob


def stated_problems(root, fields, branch, found_commit):
    """M65 point 3: a card cannot name the commit that adds it; its stated commit is an ancestor of the one it was found
    at, on the same branch, and its decisive script and its control's script have the same blobs at both"""
    parts = [p.strip() for p in fields.get("seat, branch, commit", "").split(",")]
    if len(parts) != 3:
        return ["its 'seat, branch, commit' is not three parts"]
    _seat, stated_branch, stated = parts
    bad = []
    if stated_branch != branch:
        bad.append("it says it is on %s, and was found on %s" % (stated_branch, branch))
    if git(root, "merge-base", "--is-ancestor", stated, found_commit)[0] != 0:
        return bad + ["its stated commit %s is not an ancestor of %s, where it was found" % (stated[:9], found_commit[:9])]
    m = CF.SCRIPT.match(fields.get("decisive script", ""))
    scripts = [m.group(1)] if m else []
    control = CF._argv(fields.get("failing control", "")) or []
    if len(control) > 1:
        scripts.append(control[1])
    for s in scripts:                                 # absent at both is custody's and the rerun's to say, not this
        a, b = (_blob(root, c, s) for c in (stated, found_commit))
        if a != b:
            bad.append("%s is not the same at its stated commit and where it was found" % s)
    return bad


def script_hash(fields):
    """the key a refile is linked by: the decisive script's hash and the decisive lines' hash together. CHANGED 2026-11-26
    (T1b, main's M57): it was the script's hash alone, and one script can decide several claims (B2011's prints five)"""
    m = SCRIPT_HASH.search(fields.get("decisive script", ""))
    d = CF.DECISIVE.fullmatch(fields.get("decisive lines", ""))
    return (m.group(1), d.group(2)) if m and d else None


def discover(queue, refs, root=ROOT, at=None, seen_blobs=None, codes=None):
    """queue: {id: record}; refs: [(key, ref)]. -> (new records, report lines). `seen_blobs` holds the card versions
    already filed, keyed on (branch, path, blob) (Review 88's C25: the blob alone took one card's text on two branches for
    one card); `codes` is main's table of seat codes by branch (queue/SEAT_CODES.json unless given)"""
    at = at or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    seen_blobs = dict(seen_blobs or {})
    codes = seat_codes() if codes is None else codes
    by_place = {(r["branch"], r["card_path"]): i for i, r in sorted(queue.items())}
    by_script = {}
    for cid, rec in sorted(queue.items()):            # the decisive script of each card already filed, read at its commit
        rc, text, _ = git(root, "show", "%s:%s" % (rec["commit"], rec["card_path"]))
        h = script_hash(CF.read(text)[1]) if rc == 0 else None
        if h:
            by_script.setdefault(h, cid)
    numbers = [int(i[1:]) for i in queue]
    report, new = [], {}
    tell = lambda ref, path, why: report.append("%s %s: not filed, %s; to be told to its seat" % (ref, path, why))
    known = [r.split("/", 1)[1] if r.startswith("origin/") else r for _k, r in refs]
    main_ref = next((r for k, r in refs if k == "main"), "origin/main")
    for key, ref in refs:
        found, passed, why = cards_on(root, ref)
        if why:
            report.append("%s (%s): %s; its cards are not read this round" % (key, ref, why))
            continue
        for path, why in passed:
            tell(ref, path, why)
        branch = ref.split("/", 1)[1] if ref.startswith("origin/") else ref
        for path, blob, commit, text in found:
            if (branch, path, blob) in seen_blobs:
                continue
            if branch != "main" and is_mains(root, main_ref, ref, path, blob):
                continue                              # main's own card, carried by a branch cut from main (M68, M70)
            title, fields, _layout = CF.read(text)
            code = fields.get("seat code", "")
            if title is None:                                         # A18: the reason that holds
                tell(ref, path, "its first line is not '# CLAIM CARD — <the result in one line>'")
                continue
            if QS.code_problems(code):
                tell(ref, path, "its seat code %r is not a seat code" % code)
                continue
            expected, why = code_for(branch, codes, known)          # M64 item 8, M65, M66: the code is the branch's
            if expected is None:
                tell(ref, path, why)
                continue
            if expected != code:
                tell(ref, path, "its seat code %s is not %s, the code of its branch %s" % (code, expected, branch))
                continue
            if not QS.CARD_PATH.fullmatch(path):                      # A4, C16: one card's path stops no other seat
                tell(ref, path, "its path is not relays/claims/CLAIM_<name>.md")
                continue
            stated = stated_problems(root, fields, branch, commit)
            if stated:
                tell(ref, path, "; ".join(stated))
                continue
            earlier = []
            if (branch, path) in by_place:
                earlier.append(by_place[(branch, path)])
            h = script_hash(fields)
            if h and h in by_script and by_script[h] not in earlier:
                earlier.append(by_script[h])
            said = CF.CARD_ID.fullmatch(fields.get("card id", "") or "x")
            declared = said.group(1) if said and said.group(1) else None
            if declared and declared in queue and declared not in earlier:
                earlier.append(declared)                              # A8: what the card says it refiles, linked
            n = max(numbers or [0]) + 1
            numbers.append(n)
            cid = "Q%04d" % n
            if earlier and declared not in earlier:
                note = "found on its branch; a refile of %s it does not declare" % ", ".join(earlier)
            elif declared and declared not in queue:
                note = "found on its branch; it says it refiles %s, which is not in the queue" % declared
            else:
                note = "found on its branch" + ("; refiles %s" % ", ".join(earlier) if earlier else "")
            rec = {"id": cid, "seat_code": code, "branch": branch, "commit": commit, "card_path": path,
                   "title": title[:240], "status": "FILED", "deciding": None, "heavy": CF.declared_heavy(fields),
                   "refiles": sorted(set(earlier)), "history": [{"at": at, "status": "FILED", "by": "runner", "note": note}]}
            problems = QS.card_problems(rec, cid, VENDOR_RE)
            if problems:                                              # A4, C16: reported, the others still filed
                numbers.pop()
                tell(ref, path, "its record would not hold the queue's schema: " + "; ".join(problems[:3]))
                continue
            new[cid] = rec
            seen_blobs[(branch, path, blob)] = cid
            by_place[(branch, path)] = cid
            if h:
                by_script.setdefault(h, cid)
            report.append("%s: %s %s (%s)" % (cid, ref, path, note))
            for old in earlier:                                       # A24: the old version is not taken further
                report.append("%s is refiled by %s, and is not taken further" % (old, cid))
    return new, report


def _vendor_re():
    """the attribution gate's vendor pattern (Review 88's A9: discovery's own check left it out)"""
    spec = importlib.util.spec_from_file_location("gates_for_discovery", ROOT / "scripts" / "gates" / "gates.py")
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m._VENDOR_RE


VENDOR_RE = _vendor_re()


def read_queue(path):
    p = pathlib.Path(path)
    return {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in sorted(p.glob("Q*.json"))} if p.is_dir() else {}


def main(argv):
    qdir = argv[argv.index("--queue") + 1] if "--queue" in argv else str(ROOT / QS.CARDS)
    at = argv[argv.index("--at") + 1] if "--at" in argv else None
    queue = read_queue(qdir)
    seen = {}
    for cid, r in queue.items():                      # the versions already filed, read from their own branches
        rc, out, _ = git(ROOT, "rev-parse", "%s:%s" % (r["commit"], r["card_path"]))
        if rc == 0:
            seen[(r["branch"], r["card_path"], out.strip())] = cid
    new, report = discover(queue, branches(), at=at, seen_blobs=seen)
    for line in report:
        print(line)
    bad = QS.queue_problems({k: json.dumps(v) for k, v in {**queue, **new}.items()}, VENDOR_RE)
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
