#!/usr/bin/env python3
"""The status page's section 13: two tests that this seat's pass of section 12 (rv51_pass.py) could not make, run over
every VERIFIED record of its lane in B1957's register. Data-free. Computed once, post hoc; it lists candidates, which
the page triages by reading each.

    python3 -I -u rv52_blind.py <a checkout of main at 34d71a24e> <this seat's repository>

rv51_pass.py's P4 skipped a whole record when any dated correction in it matched "computed on main" or "moved to
web-...p", though such a correction may move only some of the record's units. And its P3 matched a typed table row to
a unit by shared words, so a row that names its statements by section ("§ 5") matched none. Here, for each unit held
by a VERIFIED record:
  P4x  the record's own "how" or "note" says something in it was not computed, rerun, re-entered or re-derived (P4's
       words), and P4 skipped it because of a correction; printed with the record's sentence that says so;
  P5   a table row of the same file is typed with a label ("[J]", "a reading", "judgement", "not computed") and its
       first cell names a section by "§ N", and the unit lies in that section (from its heading "## N." or "### N."
       to the next heading of the same or higher level).
It cuts the files with the register's own rule (extract.py's units_of and tag), as rv51_pass.py does.
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
NOT = re.compile(r"not re-?(?:comput|run|deriv|enter|produc)\w*|did not recompute|has not re-entered|registered as stated"
                 r"|not computed by main|nothing here is computed", re.I)
FIXED = re.compile(r"(?:is|are) computed (?:on main|now)|computed on main|\bnow computed\b|moved to web-\S+p\b", re.I)
HEAD = re.compile(r"^(#{2,4})\s+(?:Part\s+)?(\d+(?:\.\d+)?)[.:\s]")
cands = []
for f in U["files"]:
    if f["lane"] != "web":
        continue
    text = subprocess.run(["git", "show", "%s:%s" % (f["head"], f["file"])], cwd=SEAT, capture_output=True,
                          text=True).stdout
    L = text.split("\n")
    units = ns["units_of"](text)
    tag = ns["tag"](f["file"])
    heads = []                                   # (line, level, number)
    for i, l in enumerate(L):
        m = HEAD.match(l)
        if m:
            heads.append((i + 1, len(m.group(1)), m.group(2)))
    span = {}
    for j, (ln, lv, num) in enumerate(heads):
        end = len(L) + 1
        for ln2, lv2, _ in heads[j + 1:]:
            if lv2 <= lv:
                end = ln2; break
        span.setdefault(num, (ln, end))
    secs = []                                    # (row line, section number)
    for i, l in enumerate(L):
        if l.startswith("|") and l.count("|") >= 3:
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cells) >= 2 and LAB.search(cells[-1]):
                for num in re.findall(r"§\s*(\d+(?:\.\d+)?)", cells[0]):
                    secs.append((i + 1, num))
    for u in units:
        uid = "web:%s:%d" % (tag, u["line"]); r = rec.get(uid)
        if not r or r[1] != "VERIFIED":
            continue
        t = re.sub(r"\s+", " ", u["text"]); n = u["line"]
        hit = []
        ro = recobj[r[0]]; rt = " ".join(str(ro.get(x, "")) for x in ("how", "note"))
        if NOT.search(rt) and FIXED.search(rt):
            hit.append("P4x")
        for rl, num in secs:
            if num in span and span[num][0] < n < span[num][1] and rl != n:
                hit.append("P5@%d(§%s)" % (rl, num))
        if hit:
            cands.append((r[0], f["file"].split("/")[-1][:52], n, ",".join(hit), t[:150]))
for c in sorted(cands):
    print("%-16s %-52s %4d %-18s | %s" % c)
recs = sorted({c[0] for c in cands if "P4x" in c[3]})
print("P4x records and the sentence that says what was not recomputed:")
for k in recs:
    rt = " ".join(str(recobj[k].get(x, "")) for x in ("how", "note"))
    print("  %s: %s" % (k, " / ".join(x[:220] for x in re.split(r"(?<=[.;\]])\s+", rt) if NOT.search(x))))
print("candidates: %d (P4x %d in %d records, P5 %d)" % (len(cands), sum("P4x" in c[3] for c in cands), len(recs),
      sum("P5" in c[3] for c in cands)))
