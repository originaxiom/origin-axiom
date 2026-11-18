#!/usr/bin/env python3
"""The status page's section 12: this seat's own pass over every VERIFIED record of its lane in B1957's register, for
units that its own text marks as a reading or a judgement, or that the record's own text says were not computed on
main. Data-free. Computed once, post hoc; it lists candidates, which the page triages by reading each.

    python3 -I -u rv51_pass.py <a checkout of main at 26b0fbe72> <this seat's repository>

It cuts every file of the lane at the head UNITS.json names, with the register's own rule (extract.py's units_of and
tag), and joins each unit to its record. For each unit held by a VERIFIED record:
  P1  the unit's own text carries a label: "[J]", "a reading", "judgement", "not computed";
  P2  a bullet above it, at lower indentation (its ancestor), carries such a label;
  P3  a row of a table in the same file is typed with such a label in its last cell, and the unit's words overlap the
      row's first cell by at least 0.6 of that cell's words of four letters or more (rows that are themselves held by
      a record not VERIFIED are still listed, since the row's claim may stand VERIFIED elsewhere);
  P4  the record's own "how" or "note" says a figure or statement in it was not computed, rerun, re-entered or
      re-derived, or was registered as stated, with no later dated correction saying it is computed now.
Printed: per candidate, the test, the record, file, line and the unit's first 150 characters.
"""
import glob
import json
import os
import re
import subprocess
import sys

MAIN, SEAT = sys.argv[1], sys.argv[2]
V = os.path.join(MAIN, "frontier/B1957_the_seats_claims_register/verification")
src = open(os.path.join(V, "extract.py")).read()
ns = {}
exec("import re, hashlib\n" + src[src.index("BUL = re.compile"):src.index('if __name__ == "__main__":')], ns)
U = json.load(open(os.path.join(V, "UNITS.json")))
rec = {}
recobj = {}
for p in glob.glob(os.path.join(V, "records", "web-*.json")):
    r = json.load(open(p)); k = os.path.basename(p)[:-5]; recobj[k] = r
    for u in r.get("units", []):
        rec[u] = (k, r["verdict"])
LAB = re.compile(r"\[J\]|\ba reading\b|\bjudge?ment\b|not computed", re.I)
BUL = re.compile(r"^(\s*)(?:[-*+]|\d+[.)])\s+\S")
NOT = re.compile(r"not re-?(?:comput|run|deriv|enter|produc)\w*|did not recompute|has not re-entered|registered as stated"
                 r"|not computed by main|nothing here is computed", re.I)
FIXED = re.compile(r"(?:is|are) computed (?:on main|now)|computed on main|\bnow computed\b|moved to web-\S+p\b", re.I)
words = lambda s: {w.lower() for w in re.findall(r"[A-Za-z]{4,}", s)}
cands = []
for f in U["files"]:
    if f["lane"] != "web":
        continue
    text = subprocess.run(["git", "show", "%s:%s" % (f["head"], f["file"])], cwd=SEAT, capture_output=True,
                          text=True).stdout
    L = text.split("\n")
    units = ns["units_of"](text)
    tag = ns["tag"](f["file"])
    rows = []
    for i, l in enumerate(L):
        if l.startswith("|") and l.count("|") >= 3:
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cells) >= 2 and LAB.search(cells[-1]) and not set(cells[0]) <= set("-: "):
                rows.append((i + 1, cells[0]))
    for u in units:
        uid = "web:%s:%d" % (tag, u["line"]); r = rec.get(uid)
        if not r or r[1] != "VERIFIED":
            continue
        t = re.sub(r"\s+", " ", u["text"])
        hit = []
        if LAB.search(t):
            hit.append("P1")
        n = u["line"]; m = BUL.match(L[n - 1]) if n - 1 < len(L) else None
        if m:
            ind = len(m.group(1)); k = n - 2
            while k >= 0 and ind > 0 and L[k].strip():
                mm = BUL.match(L[k])
                if mm and len(mm.group(1)) < ind:
                    a = L[k]; j = k + 1
                    while j < len(L) and L[j].strip() and not BUL.match(L[j]):
                        a += " " + L[j].strip(); j += 1
                    if LAB.search(a):
                        hit.append("P2@%d" % (k + 1)); break
                    ind = len(mm.group(1))
                k -= 1
        tw = words(t)
        for rl, claim in rows:
            cw = words(claim)
            if rl != n and len(cw) >= 3 and len(cw & tw) >= 0.6 * len(cw):
                hit.append("P3@%d" % rl)
        ro = recobj[r[0]]; rt = " ".join(str(ro.get(x, "")) for x in ("how", "note"))
        if NOT.search(rt) and not FIXED.search(rt):
            hit.append("P4")
        if hit:
            cands.append((r[0], f["file"].split("/")[-1][:52], n, ",".join(hit), t[:150]))
for c in sorted(cands):
    print("%-16s %-52s %4d %-14s | %s" % c)
print("candidates: %d (P1 %d, P2 %d, P3 %d, P4 %d)" % (len(cands), sum("P1" in c[3] for c in cands),
      sum("P2" in c[3] for c in cands), sum("P3" in c[3] for c in cands), sum("P4" in c[3] for c in cands)))
