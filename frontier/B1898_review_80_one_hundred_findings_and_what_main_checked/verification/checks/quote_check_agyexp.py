#!/usr/bin/env python3
"""Review 80, agy-exp's file: the quotation of each finding looked for, by machine, in the file it names at the commit it
names.  The file is read raw by this script and NOTHING of it is printed: only counts and the numbers of the findings.
The control: each quotation with its last word doubled must not be found."""
import subprocess, json, re
SRC = ("42ac86532", "relays/REVIEW_80_AGY-EXP.md")
def show(rev, path):
    r = subprocess.run(["git", "show", "%s:%s" % (rev, path)], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None
flat = lambda s: " ".join(s.split())
raw = show(*SRC).split("\n")
finds, cur = [], None
i = 0
while i < len(raw):
    l = raw[i]
    m = re.match(r"^### Finding F-R80-(\d+)", l)
    if m:
        cur = {"finding": int(m.group(1)), "file": None, "commit": None, "quote": None}; finds.append(cur)
    elif cur is not None and l.startswith("- **File:**"):
        cur["file"] = l.split("**File:**", 1)[1].strip().strip("`")
    elif cur is not None and l.startswith("- **Commit read:**"):
        cur["commit"] = l.split("**Commit read:**", 1)[1].strip().strip("`")
    elif cur is not None and l.strip() == "```text" and cur["quote"] is None:
        j = i + 1; block = []
        while j < len(raw) and raw[j].strip() != "```": block.append(raw[j]); j += 1
        cur["quote"] = "\n".join(block); i = j
    i += 1
out = []
for f in finds:
    t = show(f["commit"], f["file"]) if f["file"] and f["commit"] else None
    q = f["quote"] or ""
    lines = [x for x in q.split("\n") if x.strip()]
    exact = t is not None and all(x.strip() in t for x in lines) and bool(lines)
    joined = t is not None and bool(lines) and flat(q) in flat(t)
    words = flat(q).split(); ctl = None
    if t is not None and words: ctl = flat(" ".join(words + [words[-1] + words[-1]])) in flat(t)
    out.append({"finding": f["finding"], "commit": f["commit"], "the file exists at the commit": t is not None, "lines of the quotation": len(lines),
                "every line found": bool(exact), "found as one passage": bool(joined), "the control is found": ctl})
res = {"findings": len(out), "with a file that exists at the commit named": sum(o["the file exists at the commit"] for o in out),
       "every line of the quotation found in that file": sum(o["every line found"] for o in out),
       "findings whose quotation is not found": [o["finding"] for o in out if not o["every line found"]],
       "controls found": sum(1 for o in out if o["the control is found"]), "commits named": sorted({o["commit"] for o in out})}
print(json.dumps(res, indent=1))
json.dump({"summary": res, "rows": out}, open("audit/review80/quote_check_agyexp.json", "w"), indent=1)
