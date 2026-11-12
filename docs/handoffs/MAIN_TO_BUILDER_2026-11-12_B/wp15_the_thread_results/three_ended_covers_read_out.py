#!/usr/bin/env python3
"""WP-1.5; harvest row 909: the read-out of three_ended_covers_on_main.py against the SM seat's table (its B1549 § 3).

The seat's table, as data: for each state, the members at sign characters and at characters of order four, by their
reading (I(W1), I(Lambda^2 W1)).  A member orbit's reading is the reading of the one member read; the count is the
orbit's size.  Also: the number of covers (13), the number of members (138), that the deck group moves every member (so
they fall into 46 orbits of three), and that every sign member reads (-1, -1)."""
import sys, json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
SEAT = {"b++LLLR": {("sign", -1, -1): 3, ("order 4", -1, 0): 6}, "b+-LLLLLR": {("sign", -1, -1): 3, ("order 4", -1, 0): 6},
        "b+-LLR": {("sign", -1, -1): 6, ("order 4", -1, 0): 12, ("order 4", 0, -1): 12, ("order 4", 0, 0): 12},
        "b++LLLLLLR": {("sign", -1, -1): 6, ("order 4", -1, 0): 12}, "b++LLLRR": {("order 4", 0, -1): 12}, "b+-LLLLRR": {("order 4", 0, -1): 24},
        "b++LLLLLLRR": {("order 4", 0, -1): 24}, "b+-LLRLR": {}, "b++LLLRRR": {}, "b++LLLLRRR": {}}
COVERS = {"b++LLLRRR": 4}
rows = [json.loads(l) for l in (HERE / "three_ended_covers_on_main.jsonl").read_text().split("\n") if l.strip()]
counts = collections.defaultdict(dict); readings = {}
for r in rows:
    if r["what"] == "counts": counts[(r["state"], r["cover"])][tuple(r["e"])] = r
    else: readings[(r["state"], r["cover"], tuple(r["e"]))] = r
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:400]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:300]) if detail else ""))
got = collections.defaultdict(collections.Counter); total = 0; one_class = True; complete = True
for (st, ci), cs in sorted(counts.items()):
    for e, c in cs.items():
        if c["n"] > 0:
            r = readings.get((st, ci, e))
            if r is None: complete = False; continue
            inter = [x for x in r["readings"] if x[0].startswith("interior")]
            one_class &= (len(inter) == 1 and c["n"] == 1 and all(x[3] for x in r["readings"]))
            for x in inter: got[st][("sign" if r["sign character"] else "order 4", x[1], x[2])] += c["orbit"]; total += c["orbit"]
ncov = collections.Counter(st for (st, ci) in counts)
print({st: dict(v) for st, v in got.items()})
check("thirteen covers on ten states: one each, and four on +LLLRRR", sum(ncov.values()) == 13 and len(ncov) == 10 and all(ncov[s] == COVERS.get(s, 1) for s in ncov), dict(ncov))
check("every member orbit has its reading", complete)
check("state by state the seat's table of members by kind and reading", all({k: v for k, v in got[s].items()} == SEAT[s] for s in SEAT) and set(ncov) == set(SEAT), [s for s in SEAT if dict(got[s]) != SEAT[s]])
check("138 members; 18 at sign characters, every one reading (-1, -1); no member of order four reads (-1, -1)", total == 138 and sum(v for s in got for k, v in got[s].items() if k[0] == "sign") == 18 and all(k[1:] == (-1, -1) for s in got for k in got[s] if k[0] == "sign") and not any(k == ("order 4", -1, -1) for s in got for k in got[s]), total)
check("each member has one interior class (n = 1), and the extension is a representation at every reading", one_class)
check("two covers carry exactly three members reading (-1, -1): +LLLR's and -LLLLLR's", sorted(s for s in got if got[s].get(("sign", -1, -1)) == 3) == ["b++LLLR", "b+-LLLLLR"])
json.dump({"by state": {s: {"%s %d %d" % k: v for k, v in got[s].items()} for s in got}, "covers": dict(ncov), "members": total, "checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]},
          open(HERE / "three_ended_covers_read_out.json", "w"), indent=1)
print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
