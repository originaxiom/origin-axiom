#!/usr/bin/env python3
"""The owner's test of 2026-11-12, looking back: is every "least" pick on record a whole orbit of the rule's own symmetry?

THE RULE (B1869, main's enumerator, imported unchanged): a departure is a tuple of runs; "least" is by letters or by
extra letters; "not detected" has four readings; the levels counted are a set.  None of these distinguishes a tuple from
its reverse (B1867: the reverse is the same bundle with the base turned round).
THE PREDICTION (main's answer to the owner, 12:58): every set of least departures is closed under reversal: it is a union
of mirror pairs and of departures that are their own mirror.  ONE set that is not closed refutes it.
WHAT IS RUN: every background, level set, reading and measure of B1869's run, to 20 letters.
HOW IT COULD FAIL: the planted case at the end takes a least set and removes one member of a mirror pair."""
import importlib.util, json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
src = next((ROOT / "frontier").glob("B1869_*/verification/nc_on_main.py"))
spec = importlib.util.spec_from_file_location("nc_on_main", src); nc = importlib.util.module_from_spec(spec); spec.loader.exec_module(nc)

CASES = [("golden", 1, {"the own level 5": [5], "levels 4 and 5": [4, 5], "levels 2, 3, 4, 5": [2, 3, 4, 5], "level 2": [2], "level 3": [3], "level 4": [4], "level 7": [7], "level 11": [11]}),
         ("silver", 2, {"the own level 8": [8], "levels 2, 4, 8": [2, 4, 8]}),
         ("bronze", 3, {"the own level 13": [13]})]
closed = lambda best: all(tuple(reversed(s)) in set(best) for s in best)
rows, total, bad = [], 0, []
for name, b, level_sets in CASES:
    hits, count = nc.run(b, level_sets, 20)
    for (reading, lv), found in sorted(hits.items()):
        for key, measure in ((0, "letters"), (1, "extra letters")):
            v, best, nxt = nc.least(found, key)
            if v is None: continue
            total += 1; ok = closed(best)
            pairs = sum(1 for s in best if tuple(reversed(s)) != s) // 2; own = sum(1 for s in best if tuple(reversed(s)) == s)
            rows.append({"background": name, "levels": lv, "reading": reading, "least by": measure, "value": v, "departures": len(best), "mirror pairs": pairs, "their own mirror": own, "closed under reversal": ok})
            if not ok: bad.append(rows[-1])
    print("%s: %d departures enumerated" % (name, count), flush=True)
print("%d sets of least departures; closed under reversal: %d; not closed: %d" % (total, total - len(bad), len(bad)))
for r in rows:
    if r["departures"] > 1 and r["mirror pairs"]: print("   %-7s %-18s %-32s by %-13s %2d departures: %d mirror pairs, %d their own mirror" % (r["background"], r["levels"], r["reading"], r["least by"], r["departures"], r["mirror pairs"], r["their own mirror"]))
single = sum(1 for r in rows if r["departures"] == 1); print("sets with one departure (each its own mirror): %d" % single)
# planted: a least set with one member of a mirror pair removed must be reported as not closed
planted = next(r for r in rows if r["mirror pairs"] >= 1)
hits, _ = nc.run({"golden": 1, "silver": 2, "bronze": 3}[planted["background"]], {planted["levels"]: dict(CASES[["golden", "silver", "bronze"].index(planted["background"])][2])[planted["levels"]]}, 20)
v, best, _ = nc.least(hits[(planted["reading"], planted["levels"])], 0 if planted["least by"] == "letters" else 1)
cut = [s for s in best if s != next(t for t in best if tuple(reversed(t)) != t)]
print("planted: one member of a mirror pair removed from a least set -> closed under reversal: %s (must be False)" % closed(cut))
json.dump({"sets": total, "not closed": bad, "rows": rows, "planted is caught": not closed(cut)}, open(HERE / "orbit_closure_of_the_picks.json", "w"), indent=1)
