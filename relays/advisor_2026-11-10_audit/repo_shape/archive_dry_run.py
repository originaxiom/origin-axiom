#!/usr/bin/env python3
"""A dry run of gathering old front pages into one archive folder: what the move touches, and which gates it turns.

    python3 archive_dry_run.py SCRATCH_CHECKOUT FRONT_PAGES_JSON [--folder docs/archive]

SCRATCH_CHECKOUT is a throw-away checkout of main's head: THIS SCRIPT CHANGES IT AND COMMITS IN IT.  FRONT_PAGES_JSON is the
output of front_pages.py for the same commit.  The pages moved are an EXAMPLE SET chosen by a rule and by no reading: the
front pages that no code names and that last changed before 2026-10-01.  Whether a page is out of date is not decided here.

What it does: (1) leaves out a page that a list of hashes names; (2) moves the rest with git mv; (3) rewrites each citation
of an old path, in every tracked text file that may be edited -- not in the append-only logs, not in a sealed file, not in
a file a list of hashes names; (4) commits; (5) generates the views and commits; (6) runs every gate before and after.
It prints what it could not rewrite and which gates changed.  Standard library only."""
import collections, fnmatch, glob, importlib.util, json, os, re, subprocess, sys

root = os.path.abspath(sys.argv[1])
rows = json.load(open(sys.argv[2], encoding="utf-8"))
folder = sys.argv[sys.argv.index("--folder") + 1] if "--folder" in sys.argv else "docs/archive"
WHO = ["-c", "user.name=originaxiom", "-c", "user.email=dryrun@example.invalid"]
PLAIN = {k: v for k, v in os.environ.items() if not k.startswith(("OA_", "GIT_"))}
PLAIN["PYTHONDONTWRITEBYTECODE"] = "1"


def git(*a, check=True):
    r = subprocess.run(["git", "-C", root, *a], capture_output=True, text=True, env=PLAIN)
    if check and r.returncode != 0:
        sys.exit("git %s failed: %s" % (" ".join(a)[:80], r.stderr[:300]))
    return r.stdout


def gates():
    code = ("import sys, json, importlib.util\nsys.dont_write_bytecode = True\n"
            "s = importlib.util.spec_from_file_location('g', 'scripts/gates/gates.py'); g = importlib.util.module_from_spec(s); s.loader.exec_module(g)\n"
            "out = {}\n"
            "for n, f in g.GATES.items():\n"
            "    try:\n        r = f(); out[n] = [bool(r[0]), (r[1] if isinstance(r[1], str) else ' | '.join(map(str, r[1])))[:500]]\n"
            "    except Exception as e:\n        out[n] = [None, 'RAISED %s: %s' % (type(e).__name__, str(e)[:200])]\n"
            "print('@@' + json.dumps(out))\n")
    r = subprocess.run([sys.executable, "-B", "-c", code], cwd=root, capture_output=True, text=True, env=PLAIN)
    return json.loads(r.stdout.split("@@")[-1])


tracked = [f for f in git("ls-files").split("\n") if f]
# what may not be edited: the append-only logs, sealed-style files, files a list of hashes names
SEALS = ("PREREG*", "*DESIGN*.md", "SEALED*.md", "DECLARATION.md")
sealed = {f for f in tracked if f.startswith("frontier/") and f.count("/") == 2 and any(fnmatch.fnmatch(os.path.basename(f), p) for p in SEALS)}
hashed = set()
for lst in [f for f in tracked if fnmatch.fnmatch(os.path.basename(f), "ARTIFACT_HASHES*.txt")]:
    base = os.path.dirname(lst)
    for line in open(os.path.join(root, lst), encoding="utf-8", errors="replace"):
        for tok in re.findall(r"[\w./\-]+\.\w+", line):
            for cand in (os.path.normpath(os.path.join(base, tok)), os.path.normpath(tok)):
                if cand in set(tracked): hashed.add(cand)
LOGS = {"PROGRESS_LOG.md", "CHANGELOG.md"}
frozen = sealed | hashed | LOGS

chosen = [r["page"] for r in rows if not r["named by code"] and r["last changed"] < "2026-10-01"]
left_out = [p for p in chosen if p in hashed]
moved = {p: folder + "/" + os.path.basename(p) for p in chosen if p not in hashed}
print("the example set: %d front pages that no code names and that last changed before 2026-10-01" % len(chosen))
print("left where they are, because a list of hashes names them: %d %s" % (len(left_out), left_out))
before = gates()
print("gates before the move: %d of %d pass%s" % (sum(1 for v in before.values() if v[0]), len(before), "".join("\n   not passing before: %s: %s" % (k, v[1][:150]) for k, v in before.items() if not v[0])))

for old, new in moved.items():
    os.makedirs(os.path.join(root, os.path.dirname(new)), exist_ok=True)
    git("mv", old, new)
# every citation of an old path
pat = {old: re.compile((r"(?<![\w/.-])" if "/" not in old else r"(?<![\w.-])") + re.escape(old) + r"(?![\w-])") for old in moved}
TEXT = (".md", ".py", ".json", ".txt", ".tex", ".sh", ".toml", ".yml", ".yaml", ".html")
rewritten = collections.Counter(); kept = collections.defaultdict(collections.Counter)
now = [f for f in git("ls-files").split("\n") if f]
for t in now:
    if not t.endswith(TEXT): continue
    p = os.path.join(root, t)
    try:
        if os.path.getsize(p) > 5_000_000: continue
        text = open(p, encoding="utf-8", errors="surrogateescape").read()
    except OSError:
        continue
    new_text, n_here = text, 0
    for old, new in moved.items():
        if os.path.basename(old) not in text: continue
        hits = len(pat[old].findall(new_text))
        if not hits: continue
        if t in frozen or t.startswith(("legacy/", "relays/")):
            kind = "an append-only log" if t in LOGS else "a sealed file" if t in sealed else "a file a list of hashes names" if t in hashed else "legacy/ or a session's relay"
            kept[kind][t] += hits
        else:
            new_text = pat[old].sub(new, new_text); n_here += hits
    if n_here:
        open(p, "w", encoding="utf-8", errors="surrogateescape").write(new_text); rewritten[t] += n_here
git("add", "-A"); git(*WHO, "commit", "-q", "-m", "a dry run: %d front pages moved into %s, their citations rewritten" % (len(moved), folder))
print("\nmoved: %d pages into %s/" % (len(moved), folder))
print("citations rewritten: %d, in %d files" % (sum(rewritten.values()), len(rewritten)))
for kind, files in kept.items():
    print("citations left as they were, in %s: %d, in %d file(s)%s" % (kind, sum(files.values()), len(files), "" if len(files) > 4 else " (" + ", ".join(sorted(files)) + ")"))
for gen in ("scripts/views/generate.py", "scripts/views/spine.py"):
    subprocess.run([sys.executable, "-B", gen], cwd=root, capture_output=True, text=True, env=PLAIN)
changed = [l[3:] for l in git("status", "--porcelain").split("\n") if l]
if changed:
    git("add", "-A"); git(*WHO, "commit", "-q", "-m", "a dry run: the views generated")
print("generated pages that changed when the views were built again: %d %s" % (len(changed), changed[:6]))
after = gates()
turned = {k: after[k] for k in after if before[k][0] and not after[k][0]}
print("\ngates after the move: %d of %d pass" % (sum(1 for v in after.values() if v[0]), len(after)))
for k, v in turned.items():
    print("   TURNED RED: %s: %s" % (k, v[1][:420]))
if not turned: print("   no gate that passed before fails after")
