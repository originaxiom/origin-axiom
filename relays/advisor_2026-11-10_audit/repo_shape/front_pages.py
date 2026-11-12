#!/usr/bin/env python3
"""The pages a first reader meets: which could be gathered into one archive folder, and what each move would touch.

    python3 front_pages.py CHECKOUT [--json OUT]

The pages are the tracked .md files at the repository's root and directly under docs/ (not in a folder of docs/).
For each: the day it last changed; whether its first lines say what it is (generated, current, superseded, historical,
archived); and who names it by its path -- code (a script, a test, the gates), a page of the same front, or another page.
Nothing is written but the --json file.  Standard library only."""
import collections, json, os, re, subprocess, sys

root = os.path.abspath(sys.argv[1])
git = lambda *a: subprocess.run(["git", "-C", root, *a], capture_output=True, text=True).stdout
tracked = [f for f in git("ls-files").split("\n") if f]
front = sorted(f for f in tracked if f.endswith(".md") and (("/" not in f) or (f.startswith("docs/") and f.count("/") == 1)))
head_day = git("log", "-1", "--format=%cs").strip()
last = {}
for f in front:
    last[f] = git("log", "-1", "--format=%cs", "--", f).strip()
MARK = re.compile(r"generated|do not hand-edit|superseded|historical|archived|retired|current as of|currency|status:|\bLATEST\b|living document|frozen", re.I)
says = {}
for f in front:
    head = "\n".join(open(os.path.join(root, f), encoding="utf-8", errors="replace").read().split("\n")[:12])
    m = MARK.search(head)
    says[f] = m.group(0).lower() if m else ""
# who names each page by its path
names = {}
for f in front:
    names[f] = re.compile((r"(?<![\w/.-])" if "/" not in f else r"") + re.escape(f) + r"(?![\w-])")
TEXT = (".md", ".py", ".json", ".txt", ".tex", ".sh", ".toml", ".yml", ".yaml", ".cfg", ".html")
by = {f: collections.Counter() for f in front}
who = {f: collections.defaultdict(set) for f in front}
big = re.compile("|".join(re.escape(os.path.basename(f)) for f in front))
for t in tracked:
    if not t.endswith(TEXT) or t.startswith("relays/"):
        continue
    p = os.path.join(root, t)
    try:
        if os.path.getsize(p) > 5_000_000: continue
        text = open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    if not big.search(text):
        continue
    kind = ("the gates" if t == "scripts/gates/gates.py" else "code" if t.endswith((".py", ".sh", ".toml", ".yml", ".yaml", ".cfg")) else
            "a front page" if t in by else "a generated view" if t.startswith(("docs/views/", "docs/atlas/")) else "another page" if t.endswith(".md") else "data")
    for f in front:
        if t == f: continue
        n = len(names[f].findall(text))
        if n:
            by[f][kind] += n; who[f][kind].add(t)
rows = []
for f in front:
    code = by[f]["the gates"] + by[f]["code"]
    pages = by[f]["a front page"] + by[f]["another page"] + by[f]["a generated view"] + by[f]["data"]
    rows.append({"page": f, "last changed": last[f], "says": says[f], "named by code": code, "files of code": len(who[f]["the gates"] | who[f]["code"]),
                 "named by pages": pages, "pages that name it": len(who[f]["a front page"] | who[f]["another page"] | who[f]["a generated view"] | who[f]["data"])})
old = lambda r: r["last changed"] < "2026-10-01"
A = [r for r in rows if r["named by code"]]
B = [r for r in rows if not r["named by code"] and r["named by pages"]]
C = [r for r in rows if not r["named by code"] and not r["named by pages"]]
print("the pages a first reader meets, at %s (%s): %d  (%d at the root, %d directly under docs/)" % (git("rev-parse", "--short=9", "HEAD").strip(), head_day, len(front),
      sum(1 for f in front if "/" not in f), sum(1 for f in front if "/" in f)))
print("that say in their first twelve lines what they are (generated, current, superseded, historical...): %d" % sum(1 for r in rows if r["says"]))
print("last changed before 2026-10-01: %d;  in October: %d;  in November: %d" % (sum(1 for r in rows if old(r)), sum(1 for r in rows if "2026-10-01" <= r["last changed"] < "2026-11-01"), sum(1 for r in rows if r["last changed"] >= "2026-11-01")))
print()
print("WHO NAMES A PAGE BY ITS PATH (a move must change every one of these, in the same commit)")
print("  A. named by code -- a script, a test or the gates reads or cites the path:  %d pages  (%d of them last changed before October)" % (len(A), sum(map(old, A))))
print("  B. named by other pages only:                                              %d pages  (%d before October); %d citations in all" % (len(B), sum(map(old, B)), sum(r["named by pages"] for r in B)))
print("  C. named by nothing:                                                       %d pages  (%d before October)" % (len(C), sum(map(old, C))))
print()
JOBS = [("status / state / where we stand", r"STATUS|STATE|STAND|PROGRESS|SUMMARY|OVERVIEW"), ("plan / roadmap / next", r"PLAN|ROADMAP|NEXT|TODO|AGENDA|PROGRAMME|PROGRAM"),
        ("claim / result / verdict", r"CLAIM|RESULT|VERDICT|THEOREM|FINDING"), ("start / read me / guide / index / map", r"START|README|GUIDE|INDEX|MAP|ONBOARD|HOWTO|CONTEXT"),
        ("ledger / register / log", r"LEDGER|REGISTER|LOG\b|_LOG|CHANGELOG")]
print("PAGES BY THE JOB THEIR NAME GIVES (a name can give more than one)")
for job, pat in JOBS:
    hit = [r for r in rows if re.search(pat, os.path.basename(r["page"]).upper())]
    print("  %-40s %3d pages, %d last changed before October" % (job, len(hit), sum(map(old, hit))))
print()
print("THE PAGES OF B AND C LAST CHANGED BEFORE OCTOBER (candidates to read first; the script does not say they are out of date)")
for r in sorted(B + C, key=lambda r: r["last changed"]):
    if old(r):
        print("  %-10s %-52s named by %d page(s), %d time(s)%s" % (r["last changed"], r["page"][:52], r["pages that name it"], r["named by pages"], ("; says: " + r["says"]) if r["says"] else ""))
if "--json" in sys.argv:
    open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8").write(json.dumps(rows, indent=1) + "\n")
