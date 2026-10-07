#!/usr/bin/env python3
"""B1489 -- the nine proposals' bookkeeping: each [sm Pn] mark is in the seat's file; each ruling's anchor is in the received
v1.15 once; v1.16 carries nine [v1.16 marks; every seat arc a ruling cites has a row in docs/HARVEST_LEDGER.md."""
import hashlib, json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent; D = HERE.parent; ROOT = D.parents[1]
sys.path.insert(0, str(D / "adoption")); import amend
out = {}
sm = (D / "received/GENESIS_v1_10_with_proposals_sm.md").read_text()
out["sm_file_sha256"] = hashlib.sha256(sm.encode()).hexdigest()
out["marks_in_the_seats_file"] = {("P%d" % n): len(re.findall(r"\*\*\[sm P%d\]\*\*" % n, sm)) for n in range(1, 10)}
v115 = (D / "received/GENESIS_v1_15_main.md").read_text()
out["anchors_unique_in_v1_15"] = all(v115.count(old) == 1 for old, _ in amend.CHANGES)
v116 = amend.build(); out["v1_16_marks"] = v116.count("[v1.16"); out["v1_16_sha256"] = hashlib.sha256(v116.encode()).hexdigest()
ledger = (ROOT / "docs/HARVEST_LEDGER.md").read_text()
cited = sorted(set(re.findall(r"sm:B15\d\d", "".join(new for _, new in amend.CHANGES))))
out["seat_arcs_cited"] = cited; out["rowed"] = {c: bool(re.search(r"\| %s\b" % re.escape(c), ledger) or (c + " ") in ledger or (c + ",") in ledger or (c + ")") in ledger or (c + ";") in ledger) for c in cited}
out["all_cited_arcs_rowed"] = all(out["rowed"].values())
out["ok"] = out["anchors_unique_in_v1_15"] and out["v1_16_marks"] == 9 and all(v >= 1 for v in out["marks_in_the_seats_file"].values()) and out["all_cited_arcs_rowed"]
json.dump(out, open(HERE / "proposals_check.json", "w"), indent=1); print(json.dumps(out, indent=1))
