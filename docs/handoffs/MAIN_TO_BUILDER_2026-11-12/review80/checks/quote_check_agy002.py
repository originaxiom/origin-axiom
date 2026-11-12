#!/usr/bin/env python3
"""Review 80, agy-002's file: each quotation of its table looked for, by machine, in the file it names at the commit the
session read.  The file is read raw by this script and NOTHING of it is printed: only counts, and for a quotation that
is not found the number of its line in the review.  The control: each quotation with its last word doubled must not be
found."""
import subprocess, json, re, sys
AT = "c40446392"
SRC = ("origin/agy-002/verify", "relays/REVIEW_80_AGY-002.md")
def show(rev, path):
    r = subprocess.run(["git", "show", "%s:%s" % (rev, path)], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None
def flat(s):
    return " ".join(s.split())
raw = show(*SRC).split("\n")
rows = []
for n, l in enumerate(raw, 1):
    if not l.startswith("| ") or l.startswith("| arc |") or set(l.strip()) <= set("|- "):
        continue
    cells = l.strip().strip("|").split(" | ")
    cells = [c.strip() for c in cells]
    if len(cells) < 4:
        continue
    rows.append((n, cells[0], cells[1].strip("`"), " | ".join(cells[2:-1])))
out, cache = [], {}
for n, arc, path, q in rows:
    if path not in cache:
        cache[path] = show(AT, path)
    t = cache[path]
    q1 = q.strip()
    q2 = q1.strip("`")
    exact = t is not None and (q1 in t or q2 in t)
    joined = t is not None and (flat(q1) in flat(t) or flat(q2) in flat(t))
    words = q2.split()
    ctl = None
    if t is not None and words:
        bad = " ".join(words + [words[-1] + words[-1]])
        ctl = flat(bad) in flat(t)
    out.append({"line": n, "file exists at the commit": t is not None, "found": bool(exact), "found when lines are joined": bool(joined), "the control is found": ctl})
res = {"at": AT, "rows": len(out), "found exactly": sum(o["found"] for o in out), "found exactly or when lines are joined": sum(o["found"] or o["found when lines are joined"] for o in out),
       "files that do not exist at the commit": sum(not o["file exists at the commit"] for o in out),
       "lines of the review whose quotation is not found": [o["line"] for o in out if not (o["found"] or o["found when lines are joined"])],
       "controls found": sum(1 for o in out if o["the control is found"])}
print(json.dumps(res, indent=1))
json.dump({"summary": res, "rows": out}, open("audit/review80/quote_check_agy002.json", "w"), indent=1)
