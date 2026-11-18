#!/usr/bin/env python3
"""The status page's section 24.5, item 1: companion records whose grounds list lines they no longer hold.
Data-free. Reads only the register's records (JSON) at a checkout of main; changes nothing.

    python3 -I companion_grounds.py <a checkout of main>

For every record of the web lane named <parent>-r2x or -r3x, the line numbers its ground ("how") lists are collected
from three forms: "Lines: a, b", "line n:" and the "by line" list. A listed line the record does not hold is looked up
among the units of the files that the record, its parent and its parent's companions cover. Printed: how many such
records and lines; where each line is held now, by verdict; whether the receiving record's ground or note names the
line with a dated move (RESTORED, REFILED, moved, returned, "(line n)" or "line n of"); whether the companion's own
note says its lines moved; and the three records whose reasons the seat's corrected section 17 overturned.
"""
import collections
import glob
import json
import os
import re
import sys

V = os.path.join(sys.argv[1], "frontier/B1957_the_seats_claims_register/verification/records/")
recs = {os.path.basename(p)[:-5]: json.load(open(p)) for p in glob.glob(V + "web-*.json")}
owner = {u: k for k, r in recs.items() if isinstance(r.get("units"), list) for u in r["units"]}
tot, amb, undated, comps, silent = 0, [], [], 0, 0
by = collections.Counter()
for k, r in sorted(recs.items()):
    if not re.search(r"-r[23][pncs]$", k):
        continue
    h = r.get("how", "")
    nums = set()
    for m in re.finditer(r"Lines?: ([\d, ]+)", h):
        nums |= set(re.findall(r"\d+", m.group(1)))
    nums |= set(re.findall(r"\bline (\d+):", h))
    i = h.find("by line")
    if i >= 0:
        nums |= set(re.findall(r"(?:\): |; )(\d+): ", h[i:]))
    parent = re.sub(r"-r[23][pncs]$", "", k)
    tags = {u.split(":")[1] for u in r.get("units", [])}
    for c in recs:
        if c == parent or c.startswith(parent + "-r"):
            tags |= {u.split(":")[1] for u in recs[c].get("units", [])}
    held = {u.rsplit(":", 1)[1] for u in r.get("units", [])}
    miss = sorted((n for n in nums if n not in held), key=int)
    if not miss:
        continue
    comps += 1
    note = r.get("note", "")
    if not any(s in note for s in ("KEPT 2026-11-18 for its ground", "HAS MOVED", "restored to", "never held")):
        silent += 1
    for n in miss:
        c = [u for u in owner if u.rsplit(":", 1)[1] == n and u.split(":")[1] in tags]
        if len(c) != 1:
            amb.append((k, n, len(c)))
            continue
        o = owner[c[0]]
        tot += 1
        by[recs[o]["verdict"]] += 1
        txt = recs[o].get("note", "") + " " + recs[o].get("how", "")
        if not (re.search(r"(RESTORED|REFILED|moved|returned)[^.]{0,200}\b(line|lines|row)\b[^.]{0,80}\b%s\b" % n, txt)
                or "(line %s)" % n in txt or "line %s of" % n in txt):
            undated.append((k, n, o))
print("companion records listing lines they no longer hold: %d; their notes silent on it: %d" % (comps, silent))
print("such lines placed in another record: %d, by that record's verdict: %s" % (tot, dict(by)))
print("lines not placed (none or several candidates): %s" % amb)
print("placed lines whose receiving record does not name the line with a dated move: %d %s" % (len(undated), undated[:10]))
for k, lines in (("web-wb2-d1-05-r3p", ["126", "127"]), ("web-wf24-05-r2n", ["86"]), ("web-r79b-01-r2p", ["20", "22", "29"])):
    r = recs[k]
    print("%s: lists %s; holds %s; those lines now in %s" % (k, lines, sorted(u.rsplit(":", 1)[1] for u in r["units"]),
          sorted({(owner.get(u), recs[owner[u]]["verdict"]) for u in owner if u.rsplit(":", 1)[1] in lines
                  and u.split(":")[1] in {x.split(":")[1] for x in recs[re.sub(r"-r[23][pncs]$", "", k)]["units"]}})))
