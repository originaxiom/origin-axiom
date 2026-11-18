#!/usr/bin/env python3
"""The status page's section 16: the packets for this seat's own reading of main's second reading (M55). Data-free;
clerical (it computes nothing about the work, it gathers what each reader needs).

    python3 -I -u rv55_packets.py <a checkout of main at 4921ee923> <this seat's repository> <out dir> <n packets>

The set read is every unit of this seat's lane that was VERIFIED before M55's landing: the units now under a VERIFIED
record, and the units in the second reading's companions (web-<record>-r2p, -r2n, -r2c). For each unit it writes: the
id, file and line, the unit's text as the register cuts it, the record it is under now with its verdict, the parent
record's "how" and "note", the companion's "how" and "note" if any, and, if the unit was a candidate, the sorter's
class and reason and main's decision. Units are grouped by parent record, and records are dealt into n packets of
about equal size. Printed: the counts.
"""
import glob
import json
import os
import re
import subprocess
import sys

MAIN, SEAT, OUT, N = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
V = os.path.join(MAIN, "frontier/B1957_the_seats_claims_register/verification")
src = open(os.path.join(V, "extract.py")).read(); ns = {}
exec("import re, hashlib\n" + src[src.index("BUL = re.compile"):src.index('if __name__ == "__main__":')], ns)
U = json.load(open(os.path.join(V, "UNITS.json")))
text = {}
for f in U["files"]:
    if f["lane"] != "web":
        continue
    t = subprocess.run(["git", "show", "%s:%s" % (f["head"], f["file"])], cwd=SEAT, capture_output=True, text=True).stdout
    for u in ns["units_of"](t):
        text["web:%s:%d" % (ns["tag"](f["file"]), u["line"])] = (f["file"], u["line"], re.sub(r"\s+", " ", u["text"]))
R = {os.path.basename(p)[:-5]: json.load(open(p)) for p in glob.glob(os.path.join(V, "records", "web-*.json"))}
SR = {x["unit"]: x for x in json.load(open(os.path.join(V, "second_reading", "web.json")))["units"]}
COMP = re.compile(r"-r2[pnc]$")
rows = {}
for k, r in R.items():
    parent = COMP.sub("", k)
    if not (r["verdict"] == "VERIFIED" or COMP.search(k)):
        continue
    for u in r.get("units", []):
        if u not in text:
            continue
        p = R.get(parent, {})
        sr = SR.get(u, {})
        rows.setdefault(parent, []).append({
            "unit": u, "file": text[u][0], "line": text[u][1], "text": text[u][2][:1200],
            "now": "%s %s" % (k, r["verdict"]),
            "parent_how": p.get("how", "(parent record gone: see the companion)"), "parent_note": p.get("note", ""),
            "companion_how": r.get("how", "") if COMP.search(k) else "", "companion_note": r.get("note", "") if COMP.search(k) else "",
            "sorter": "%s: %s" % (sr.get("class", ""), sr.get("why", "")) if sr else "(not a candidate)",
            "main_decision": sr.get("decision", "") if sr else "(unmarked; still VERIFIED)"})
order = sorted(rows, key=lambda k: -len(rows[k]))
packs = [[] for _ in range(N)]; size = [0] * N
for k in order:
    i = size.index(min(size)); packs[i].append(k); size[i] += len(rows[k])
os.makedirs(OUT, exist_ok=True)
for i, ks in enumerate(packs):
    json.dump({k: sorted(rows[k], key=lambda x: (x["file"], x["line"])) for k in ks}, open(os.path.join(OUT, "packet_%d.json" % (i + 1)), "w"),
              ensure_ascii=False, indent=1)
tot = sum(len(v) for v in rows.values())
print("units: %d in %d parent records; now VERIFIED %d, in companions %d; packets: %s" % (
    tot, len(rows), sum(1 for v in rows.values() for x in v if x["now"].endswith("VERIFIED")),
    sum(1 for v in rows.values() for x in v if not x["now"].endswith("VERIFIED")), size))
