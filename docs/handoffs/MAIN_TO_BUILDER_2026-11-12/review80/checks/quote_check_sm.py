#!/usr/bin/env python3
"""Review 80, the SM seat's file: each quotation of each finding looked for, by machine, at the commit the seat read.
A quotation is PLACED when it stands in a file the finding's own heading names, or, where the heading names no path, in
a file of the arc the finding is entered under (the arcs named in its heading, else its section's).  A quotation found
only elsewhere in the tree is counted apart.  The control: each quotation with its last word doubled must be found
nowhere."""
import subprocess, json, re
AT = "c40446392"; SRC = ("62f545ec3", "relays/REVIEW_80_SM.md")
def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True); return r.stdout if r.returncode == 0 else None
flat = lambda s: " ".join(s.split())
files = git("ls-tree", "-r", "--name-only", AT).split("\n")
cache = {}
def text(p):
    if p not in cache: cache[p] = git("show", "%s:%s" % (AT, p)) or ""
    return cache[p]
raw = git("show", "%s:%s" % SRC).split("\n")
section_arcs, finds, cur = [], [], None
for l in raw:
    if l.startswith("## ") or l.startswith("### "):
        section_arcs = re.findall(r"B\d+", l); cur = None
    m = re.match(r"^\*\*R80-SM-(\d+)\*\*(.*)$", l)
    if m:
        cur = {"finding": int(m.group(1)), "heading": m.group(2), "arcs": re.findall(r"B\d+", m.group(2)) or list(section_arcs), "quotes": []}; finds.append(cur); continue
    if cur is not None and l.startswith("- `"):
        mm = re.match(r"^- (``\s?(.*?)\s?``|`(.*?)`)(.*)$", l)
        if mm:
            q = mm.group(2) if mm.group(2) is not None else mm.group(3)
            cur["quotes"].append((q, re.findall(r"B\d+", mm.group(4))))
    elif cur is not None and l.startswith("- **What is wrong"):
        cur = None
def candidates(f, extra_arcs):
    named = [t.strip("`,.;:()") for t in f["heading"].split() if "/" in t or re.search(r"\.(md|py|json|txt)[`,.;:)]*$", t)]
    out = []
    for t in named:
        out += [p for p in files if p == t or p.endswith("/" + t)] if "/" in t else []
    arcs = extra_arcs or f["arcs"]
    for a in arcs:
        out += [p for p in files if p.startswith("frontier/%s_" % a)]
    for t in named:
        if "/" not in t:                                              # a bare file name: in the arcs' folders, else at the root or in docs
            out += [p for p in files if p == t or p == "docs/" + t]
    return list(dict.fromkeys(out))
rows = []
for f in finds:
    for q, extra in f["quotes"]:
        cand = candidates(f, extra)
        placed = any(q in text(p) or flat(q) in flat(text(p)) for p in cand)
        anywhere = placed or bool(git("grep", "-l", "-F", "-e", q, AT, "--"))
        words = q.split(); bad = " ".join(words + [words[-1] + words[-1]]) if words else None
        ctl = bool(bad) and bool(git("grep", "-l", "-F", "-e", bad, AT, "--"))
        rows.append({"finding": f["finding"], "files looked in": len(cand), "placed": bool(placed), "found somewhere at the commit": bool(anywhere), "the control is found": bool(ctl)})
res = {"at": AT, "findings": len(finds), "quotations": len(rows), "placed": sum(r["placed"] for r in rows),
       "found elsewhere only": sum(1 for r in rows if not r["placed"] and r["found somewhere at the commit"]),
       "found nowhere": [r["finding"] for r in rows if not r["found somewhere at the commit"]],
       "findings with no quotation read": [f["finding"] for f in finds if not f["quotes"]],
       "findings with a quotation found elsewhere only": sorted({r["finding"] for r in rows if not r["placed"] and r["found somewhere at the commit"]}),
       "controls found": sum(r["the control is found"] for r in rows)}
print(json.dumps(res, indent=1))
json.dump({"summary": res, "rows": rows}, open("audit/review80/quote_check_sm.json", "w"), indent=1)
