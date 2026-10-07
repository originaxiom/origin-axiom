#!/usr/bin/env python3
"""B1602 -- the census assembled from the per-thread files (forced_<thread>.json) into census_8.jsonl and summary.json:
the cells T1-T4 as sealed, the carriers and non-carriers by parity class, the trivial-character classes."""
import json, glob, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
import forced_every as FE

rows = {}
for f in sorted(glob.glob(str(HERE / "forced_b*.json"))):
    d = json.load(open(f)); rows[d["thread"]] = d
names = FE.threads(8)
missing = [n for n in names if n not in rows]
with open(HERE / "census_8.jsonl", "w") as fh:
    for n in names:
        if n in rows:
            d = rows[n]
            fh.write(json.dumps({k: (v if k != "covers" else [{kk: vv for kk, vv in c.items() if kk != "rows"} for c in v]) for k, v in d.items()}, default=str) + "\n")
odd = [rows[n] for n in names if n in rows and rows[n]["trace"] % 2]
even = [rows[n] for n in names if n in rows and rows[n]["trace"] % 2 == 0]
seen_before_seal = {"b++LR", "b+-LR", "b++LLLR", "b+-LLLR", "b++LLRR", "b++LLR"}
len6_odd = [r for r in odd if len(r["word"]) == 6]
len8_odd = [r for r in odd if len(r["word"]) == 8]
carriers_odd = [r["thread"] for r in odd if r["any_member"]]
carriers_even = [r["thread"] for r in even if r["any_member"]]
non_even = [r["thread"] for r in even if not r["any_member"]]
triv_odd = [r["thread"] for r in odd if any(c["trivial"]["n"] > 0 for c in r["covers"])]
triv_even = [r["thread"] for r in even if any(c["trivial"]["n"] > 0 for c in r["covers"])]
summary = {
 "threads": len(names), "read": len(rows), "missing": missing, "odd": len(odd), "even": len(even),
 "T1_len6_odd_no_member": {"threads": [r["thread"] for r in len6_odd], "holds": all(not r["any_member"] for r in len6_odd)},
 "T2_len8_odd_no_member": {"threads": len(len8_odd), "carriers": [r["thread"] for r in len8_odd if r["any_member"]], "holds": all(not r["any_member"] for r in len8_odd)},
 "T3_every_even_carries": {"even": len(even), "carriers": len(carriers_even), "non_carriers": non_even, "holds": not non_even},
 "T4_trivial_character": {"odd_with_trivial_class": triv_odd, "first_half_holds": all(t in ("b++LR", "b+-LR") for t in triv_odd),
                          "even_with_trivial_class": triv_even, "fraction_even": round(len(triv_even) / max(1, len(even)), 3), "second_half_holds": len(triv_even) * 2 >= len(even)},
 "odd_carriers": carriers_odd,
 "even_by_class": {cls: {"carriers": [r["thread"] for r in even if r["deck"] == cls and r["any_member"]], "non_carriers": [r["thread"] for r in even if r["deck"] == cls and not r["any_member"]]} for cls in ("D4", "V4")},
 "member_structures_odd": sorted({tuple(s) for r in odd for c in r["covers"] for s in c["member_structures"]}),
 "member_structures_even": sorted({tuple(s) for r in even for c in r["covers"] for s in c["member_structures"]}),
 "kernels_per_class": {cls: sorted({r["kernels"] for r in rows.values() if r["deck"] == cls}) for cls in ("A4", "D4", "V4")},
 "cusps_per_class": {cls: sorted({c["cusps"] for r in rows.values() if r["deck"] == cls for c in r["covers"]}) for cls in ("A4", "D4", "V4")},
 "seconds_total": round(sum(r["s"] for r in rows.values()), 1),
}
json.dump(summary, open(HERE / "summary.json", "w"), indent=1, default=str)
print(json.dumps(summary, indent=1, default=str))
