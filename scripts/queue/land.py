#!/usr/bin/env python3
"""The landing tool: the single writer of a banked card's arc, its lock, its ledger row and the log pair (the framework's
thin path, patch T11; draft 1 §§ 4 and 9; docs/BANKING_PROTOCOL.md Part I, A, B and D; register row P-885).

A card that the queue holds VERIFIED (two banking ACCEPTs, the runner's move, T9) is landed on main by this tool alone, so
that two banking seats and main are not three writers of arc numbers, ledger rows and log entries. In this order:

  1. THE LOCK: one landing at a time on this machine (a lock file, created exclusively; THE_SWEEP_OF_2026-11-14 Q3);
  2. A FRESH CLONE of main, made for this landing (draft § 4: "a landing runs the suite on a fresh clone");
  3. THE CARD: its record on the queue's branch (or a queue folder given) must be VERIFIED, moved there by the runner, and
     not landed before (the CHANGELOG names every card it landed). And the VERIFIED is derived again on the clone, from
     the evidence, not read from the record, which a hand could append to (main's M72 point 1): both banking seats'
     verdicts, on their own branches, are checked as T9 checks them (each hashes to its seal; the expectation sighted no
     later than the seal, K3; both verdicts sighted after both seals, K1, by the queue's sighting log; D8; the verdict's
     form, K11; K2's checks that need no run), and the outcome rule must give VERIFIED. The seats' scripts are not rerun
     here: their reruns are the runner's, and their results stand in the queue's check file;
  4. THE NUMBERS, taken at landing on the clone: the arc's (one more than the highest B<n> under frontier/ and in the arcs'
     verdict files) and the harvest row's (one more than the highest row of docs/HARVEST_LEDGER.md);
  5. THE WRITES, and no others: the arc's folder frontier/B<n>_<slug>/ (its FINDINGS.md and arc_verdict.json required,
     Part I A1 and A2), its lock tests/test_b<n>_<slug>.py (A4), the CHANGELOG's entry at the top and the PROGRESS_LOG's
     at the end (B6, B7), and the harvest row, which the tool writes itself from the queue's record;
  6. THE COMMIT, then the views regenerated (D16) and the commit amended with them;
  7. THE CHECKS on that commit: every gate (D17) and the full suite with `-rfE` (D18), compared with
     queue/KNOWN_FAILURES.json (T10). A failure or a red gate the list does not hold refuses the landing.

The tool never pushes. A landing that holds ends with the clone's path and the command that pushes it; one that is refused
leaves its clone to be read, its commit unpushed. docs/CAMPAIGN_STATUS.md's LATEST line (B8) and the surfaces of Part I C
stay main's: they are judgements, not a writer's.

THE PREPARED LANDING (a folder, written by main or a banking seat; placeholders {ARC}, {ROW} and {CARD} are replaced):
    LANDING.json   {"card": "Q0001", "slug": "lower_snake_case", "title": "the CHANGELOG heading",
                    "progress_title": "the PROGRESS_LOG heading", "message": "the commit's subject"}
    arc/           the arc's files: FINDINGS.md, arc_verdict.json (its "id" "{ARC}"), and any others
    lock.py        the arc's lock
    changelog.md   the CHANGELOG entry's body
    progress.md    the PROGRESS_LOG entry's body

    python3 scripts/queue/land.py --landing DIR [--queue-dir QDIR] [--source REPO] [--work DIR] [--at DATE]
Exit 0 when the landing holds and is ready to push; 1 when it is refused; 2 when another landing holds the lock."""
import datetime
import importlib.util
import json
import os
import pathlib
import re
import shlex
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


BL = _load("baseline_for_landing", HERE / "baseline.py")      # T10's list and its comparison
BK = _load("banking_for_landing", HERE / "banking.py")        # T9's check of a sealed verdict
D = _load("discover_for_landing", HERE / "discover.py")       # the Pins table's seat names

SUITE = "python3 -B -m pytest -q -rfE -p no:cacheprovider"
REGENERATE = (                                           # Part I D16, as main runs them; each only where its script stands
    "scripts/atlas/atlas.py",
    "frontier/B1883_where_we_stand/verification/build_where_we_stand.py --write",
    "scripts/views/generate.py",
    "scripts/views/spine.py",
    "frontier/B1861_the_closure_programme/verification/build_programme.py --write",
)
LANDING_KEYS = ("card", "slug", "title", "progress_title", "message")
SLUG = re.compile(r"[a-z0-9]+(_[a-z0-9]+)*")
CARD = re.compile(r"Q\d{4,}")
ARC_DIR = re.compile(r"B(\d+)_")
ROW_LINE = re.compile(r"\| (\d+) \|")
PLACEHOLDER = re.compile(r"\{(ARC|ROW|CARD)\}")


class Refused(Exception):
    pass


def _git(cwd, *args, check=True):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise Refused("git %s: %s" % (" ".join(args[:2]), r.stderr.strip()[:300]))
    return r.stdout


def default_lock(root=ROOT):
    common = _git(root, "rev-parse", "--git-common-dir").strip()
    return pathlib.Path(root, common, "queue-landing.lock")


def take_lock(path):
    """the lock, created exclusively; None when another landing holds it"""
    try:
        fd = os.open(str(path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        return None
    os.write(fd, ("%d\n" % os.getpid()).encode())
    os.close(fd)
    return path


def read_landing(d):
    """the prepared landing's LANDING.json and the problems of its form"""
    d = pathlib.Path(d)
    bad = []
    try:
        meta = json.loads((d / "LANDING.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return None, ["LANDING.json cannot be read: %s" % e]
    if not isinstance(meta, dict) or sorted(meta) != sorted(LANDING_KEYS):
        return None, ["LANDING.json holds exactly %s" % ", ".join(LANDING_KEYS)]
    if any(not isinstance(meta[k], str) or not meta[k].strip() or "\n" in meta[k] for k in LANDING_KEYS):
        bad.append("each field of LANDING.json is one line of text")
    if not CARD.fullmatch(meta["card"]):
        bad.append("the card is a queue id, Q followed by its number")
    if not SLUG.fullmatch(meta["slug"]):
        bad.append("the slug is lower_snake_case")
    for name in ("lock.py", "changelog.md", "progress.md", "arc/FINDINGS.md", "arc/arc_verdict.json"):
        if not (d / name).is_file():
            bad.append("the landing has no %s (BANKING_PROTOCOL Part I A)" % name)
    for f in sorted(p for p in d.rglob("*") if p.is_symlink()):
        bad.append("%s is a symbolic link" % f.relative_to(d))
    return meta, bad


def card_record(clone, cid, queue_dir=None):
    """the card's record, from a queue folder given or from the queue's branch as the clone fetched it"""
    if queue_dir:
        f = pathlib.Path(queue_dir, "cards", "%s.json" % cid)
        return json.loads(f.read_text(encoding="utf-8")) if f.is_file() else None
    r = subprocess.run(["git", "show", "origin/queue:queue/cards/%s.json" % cid], cwd=clone, capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 else None


def card_problems(rec, cid, changelog):
    if rec is None:
        return ["the queue holds no card %s" % cid]
    bad = []
    if rec.get("status") != "VERIFIED":
        bad.append("the card is %s, not VERIFIED: only two banking ACCEPTs bank a card" % rec.get("status"))
    else:
        last = rec["history"][-1]
        if last.get("status") != "VERIFIED" or last.get("by") != "runner" or "ACCEPT and ACCEPT" not in last.get("note", ""):
            bad.append("the card's VERIFIED is not the runner's move on two ACCEPTs")
    if "queue card %s)" % cid in changelog:
        bad.append("the card %s is landed already (the CHANGELOG names it)" % cid)
    return bad


def _show(cwd, spec):
    r = subprocess.run(["git", "show", spec], cwd=cwd, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def derived_problems(clone, rec, cid, queue_dir=None):
    """M72 point 1: the problems of a VERIFIED derived on the clone from the sealed verdicts; [] when it holds"""
    seats = BK.seats(pathlib.Path(clone, "queue", "BANKING_SEATS.json"))
    if not seats:
        return ["queue/BANKING_SEATS.json on main names no two banking seats"]
    if queue_dir:
        f = pathlib.Path(queue_dir, "SIGHTINGS.jsonl")
        log = f.read_text(encoding="utf-8") if f.is_file() else None
        c = pathlib.Path(queue_dir, "checks", "%s.json" % cid)
        check = c.read_text(encoding="utf-8") if c.is_file() else None
    else:
        log = _show(clone, "origin/queue:queue/SIGHTINGS.jsonl")
        check = _show(clone, "origin/queue:queue/checks/%s.json" % cid)
    if log is None:
        return ["the queue's sighting log cannot be read"]
    entries, bad = BK.CU.read_log(log)
    if bad:
        return ["the queue's sighting log does not hold its form"]
    text = _show(clone, "%s:%s" % (rec["commit"], rec["card_path"]))
    if text is None:
        return ["the card cannot be read at its commit on the clone"]
    seal_at = {}
    for v, s in seats.items():
        _c, b = BK._at(clone, "origin/" + s["branch"], BK.paths(cid)["seal"])
        e = BK.CU.first_sighting(entries, s["branch"], BK.paths(cid)["seal"], b) if b else None
        seal_at[v] = e["at"] if e else None
    got = {v: BK.check_verdict(clone, cid, rec, text, s, entries, seal_at["V2" if v == "V1" else "V1"], run=False)
           for v, s in sorted(seats.items())}
    bad = ["%s's verdict, derived again: %s" % (v, "; ".join(g["reasons"])) for v, g in sorted(got.items()) if not g["ok"]]
    if bad:
        return bad
    try:
        peer = (json.loads(check) if check else {}).get("peer") or {}
    except ValueError:
        peer = {}
    status, note = BK.outcome(rec, got["V1"]["verdict"], got["V2"]["verdict"], peer.get("other_family"), seats)
    return [] if status == "VERIFIED" else ["the verdicts, derived again, give %s, not VERIFIED: %s" % (status, note)]


def seat_name(clone, branch):
    """the seat as the harvest ledger's Pins table names it (main's M72 point 2), or its branch when no row names it"""
    for key, ref in D.branches(root=clone):
        if key != "main" and ref == "origin/" + branch:
            return key
    return branch


def numbers(clone):
    """(the arc's number, the harvest row's number), taken at landing: one more than the highest of each on the clone"""
    clone = pathlib.Path(clone)
    arcs = [int(m.group(1)) for p in (clone / "frontier").iterdir() if p.is_dir() for m in [ARC_DIR.match(p.name)] if m] \
        if (clone / "frontier").is_dir() else []
    for v in clone.glob("frontier/*/arc_verdict.json"):
        try:
            m = re.fullmatch(r"B(\d+)", str(json.loads(v.read_text(encoding="utf-8")).get("id", "")))
        except (ValueError, AttributeError):
            m = None
        if m:
            arcs.append(int(m.group(1)))
    ledger = clone / "docs" / "HARVEST_LEDGER.md"
    rows = [int(m.group(1)) for l in ledger.read_text(encoding="utf-8").splitlines() for m in [ROW_LINE.match(l)] if m] \
        if ledger.is_file() else []
    return max(arcs, default=0) + 1, max(rows, default=0) + 1


def _fill(text, subs):
    return PLACEHOLDER.sub(lambda m: subs[m.group(1)], text)


def write_landing(clone, d, meta, rec, arc, row, at):
    """the writes of step 5; returns the paths written, relative to the clone"""
    clone, d = pathlib.Path(clone), pathlib.Path(d)
    tag = "B%d" % arc
    subs = {"ARC": tag, "ROW": str(row), "CARD": meta["card"]}
    arc_dir = "frontier/%s_%s" % (tag, meta["slug"])
    if (clone / arc_dir).exists():
        raise Refused("%s exists on the clone" % arc_dir)
    written = []
    for f in sorted(p for p in (d / "arc").rglob("*") if p.is_file()):
        rel = "%s/%s" % (arc_dir, f.relative_to(d / "arc").as_posix())
        (clone / rel).parent.mkdir(parents=True, exist_ok=True)
        (clone / rel).write_text(_fill(f.read_text(encoding="utf-8"), subs), encoding="utf-8")
        written.append(rel)
    try:
        verdict = json.loads((clone / arc_dir / "arc_verdict.json").read_text(encoding="utf-8"))
    except ValueError:
        raise Refused("the arc's arc_verdict.json is not JSON")
    if not isinstance(verdict, dict) or verdict.get("id") != tag:
        raise Refused("the arc's arc_verdict.json does not name its id as {ARC}, which the tool fills (%s)" % tag)
    lock = "tests/test_b%d_%s.py" % (arc, meta["slug"])
    if (clone / lock).exists():
        raise Refused("%s exists on the clone" % lock)
    (clone / lock).parent.mkdir(parents=True, exist_ok=True)
    (clone / lock).write_text(_fill((d / "lock.py").read_text(encoding="utf-8"), subs), encoding="utf-8")
    written.append(lock)
    cl = clone / "CHANGELOG.md"
    text = cl.read_text(encoding="utf-8")
    head = "# Changelog\n\n"
    if not text.startswith(head):
        raise Refused("CHANGELOG.md does not open with its title")
    entry = "## %s (%s; queue card %s) (%s)\n\n%s\n\n" % (_fill(meta["title"], subs), tag, meta["card"], at,
                                                          _fill((d / "changelog.md").read_text(encoding="utf-8"), subs).strip())
    cl.write_text(head + entry + text[len(head):], encoding="utf-8")
    pl = clone / "PROGRESS_LOG.md"
    body = _fill((d / "progress.md").read_text(encoding="utf-8"), subs).strip()
    pl.write_text(pl.read_text(encoding="utf-8").rstrip("\n") + "\n\n## %s — %s (%s)\n\n%s\n" % (
        at, _fill(meta["progress_title"], subs), tag, body), encoding="utf-8")
    hl = clone / "docs" / "HARVEST_LEDGER.md"
    lines = hl.read_text(encoding="utf-8").split("\n")
    last = max((i for i, l in enumerate(lines) if ROW_LINE.match(l)), default=None)
    if last is None:
        raise Refused("docs/HARVEST_LEDGER.md holds no row to follow")
    cell = lambda s: s.replace("|", "/").strip()
    title = cell(_fill(meta["title"], subs))
    head = (_show(clone, "%s:%s" % (rec["commit"], rec["card_path"])) or "").split("\n", 1)[0]
    head = head[len("# CLAIM CARD — "):] if head.startswith("# CLAIM CARD — ") else ""
    words = head.split()
    quote = '"%s"' % cell(" ".join(words[:25]) + (" ..." if len(words) > 25 else "")) if words else "—"
    # main's M72 point 2: the ledger's eight cells, | # | seat | item | headline | path @ commit | disposition | arc | date |
    lines.insert(last + 1, "| %d | %s (%s) | %s | %s | %s @ %s | **VERIFIED** (two banking ACCEPTs in the queue, card %s; "
                           "landed by the landing tool) | %s | %s |" % (
                               row, seat_name(clone, rec["branch"]), rec["seat_code"], title, quote, rec["card_path"],
                               rec["commit"][:9], meta["card"], tag, at))
    hl.write_text("\n".join(lines), encoding="utf-8")
    written += ["CHANGELOG.md", "PROGRESS_LOG.md", "docs/HARVEST_LEDGER.md"]
    return written


def regenerate(clone):
    for cmd in REGENERATE:
        parts = shlex.split(cmd)
        if (pathlib.Path(clone) / parts[0]).is_file():
            subprocess.run([sys.executable, "-B", *parts], cwd=clone, capture_output=True, text=True)


GATES_RUN = ("import importlib.util, json, sys\n"
             "spec = importlib.util.spec_from_file_location('gates_at_landing', 'scripts/gates/gates.py')\n"
             "g = importlib.util.module_from_spec(spec); sys.dont_write_bytecode = True; spec.loader.exec_module(g)\n"
             "red = []\n"
             "for name, fn in g.GATES.items():\n"
             "    try:\n"
             "        ok = bool(fn()[0])\n"
             "    except Exception:\n"
             "        ok = False\n"
             "    if not ok:\n"
             "        red.append(name)\n"
             "print(json.dumps(red))\n")


def red_gates(clone):
    r = subprocess.run([sys.executable, "-B", "-c", GATES_RUN], cwd=clone, capture_output=True, text=True)
    if r.returncode != 0:
        raise Refused("the gates did not run: %s" % (r.stderr.strip().splitlines() or ["?"])[-1][:300])
    return json.loads(r.stdout.strip().splitlines()[-1])


def suite_failures(clone, suite=SUITE):
    """the failing ids of the full suite, as `-rfE` prints them; refused when the suite did not run to its end"""
    r = subprocess.run(shlex.split(suite), cwd=clone, capture_output=True, text=True)
    lines = r.stdout.splitlines()
    if r.returncode not in (0, 1) or not any(re.search(r"\d+ (passed|failed)", l) for l in lines[-3:]):
        raise Refused("the suite did not run to its end (exit %d): %s" % (r.returncode, (lines or ["no output"])[-1][:300]))
    return sorted({BL.test_id(l) for l in lines if l.startswith(("FAILED ", "ERROR "))})


def land(landing, source=None, work=None, queue_dir=None, at=None, suite=SUITE, lock=None):
    """one landing: (exit status, report lines, the clone's path or None)"""
    at = at or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    lock = pathlib.Path(lock) if lock else default_lock()
    if take_lock(lock) is None:
        return 2, ["another landing holds the lock %s; nothing was done" % lock], None
    report, clone = [], None
    try:
        meta, bad = read_landing(landing)
        if bad:
            raise Refused("; ".join(bad))
        source = source or _git(ROOT, "remote", "get-url", "origin").strip()
        work = pathlib.Path(work or tempfile.mkdtemp(prefix="landing_"))
        clone = work / "clone"
        _git(work, "clone", "-q", "--no-hardlinks", "--branch", "main", str(source), str(clone))
        _git(clone, "fetch", "-q", "origin", "queue:refs/remotes/origin/queue", check=False)
        rec = card_record(clone, meta["card"], queue_dir)
        bad = card_problems(rec, meta["card"], (clone / "CHANGELOG.md").read_text(encoding="utf-8"))
        if bad:
            raise Refused("; ".join(bad))
        bad = derived_problems(clone, rec, meta["card"], queue_dir)
        if bad:
            raise Refused("the VERIFIED in the queue's record is not borne out by the sealed verdicts: " + "; ".join(bad))
        report.append("the VERIFIED derived again from both sealed verdicts (their reruns are the runner's)")
        arc, row = numbers(clone)
        report.append("the numbers taken at landing: arc B%d, harvest row %d" % (arc, row))
        written = write_landing(clone, landing, meta, rec, arc, row, at)
        _git(clone, "add", "--", *written)
        _git(clone, "commit", "-q", "-m", "%s\n\nLanded by scripts/queue/land.py: arc B%d, harvest row %d, queue card %s."
             % (_fill(meta["message"], {"ARC": "B%d" % arc, "ROW": str(row), "CARD": meta["card"]}), arc, row, meta["card"]))
        regenerate(clone)
        if _git(clone, "status", "--porcelain").strip():
            _git(clone, "add", "-A")
            _git(clone, "commit", "-q", "--amend", "--no-edit")
        report.append("the commit %s on the fresh clone, with the views regenerated" % _git(clone, "rev-parse", "HEAD").strip()[:9])
        red = red_gates(clone)
        failures = suite_failures(clone, suite)
        new, gone = BL.compare(BL.load(clone), failures, red)
        report.append("the gates: %d red (%s); the suite: %d failing" % (len(red), ", ".join(red) or "none", len(failures)))
        for g in gone:
            report.append("on the known-failures list and passing now, to take off: %s" % g)
        if new:
            raise Refused("new against queue/KNOWN_FAILURES.json: %s" % "; ".join(new))
        report.append("ready: nothing is pushed. To land it: git -C %s push origin HEAD:main" % clone)
        return 0, report, clone
    except Refused as e:
        report.append("REFUSED: %s" % e)
        if clone and clone.exists():
            report.append("the clone is left to be read, nothing pushed: %s" % clone)
        return 1, report, clone
    finally:
        try:
            lock.unlink()
        except FileNotFoundError:
            pass


def main(argv):
    arg = lambda k: argv[argv.index(k) + 1] if k in argv else None
    if not arg("--landing"):
        print(__doc__)
        return 1
    status, report, _ = land(arg("--landing"), source=arg("--source"), work=arg("--work"), queue_dir=arg("--queue-dir"),
                             at=arg("--at"), suite=arg("--suite") or SUITE, lock=arg("--lock"))
    print("\n".join(report))
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
