#!/usr/bin/env python3
"""B1480 cell: the class index's firing on own-level word states (B1439's banked census by slope, to length 12), read
against the sign of the word and against amphichirality (B1479's table).  No index is computed here: this is a
tabulation of two banked results."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; FR = next(p for p in HERE.parents if p.name == "frontier")
C = FR / "B1439_the_census_by_slope" / "verification"
rows = []
for i in range(4):
    for r in json.load(open(C / ("census_by_slope_%d.json" % i))):
        if r.get("k") == 1: rows.append(r)
for r in json.load(open(FR / "B1438_the_slope_law" / "verification" / "slope_census.json")):
    if r.get("k") == 1: rows.append(r)
seen = {}
for r in rows: seen.setdefault(r["state"], r)
rows = list(seen.values())
S = json.load(open(FR / "B1479_the_bit_is_the_sign_of_the_word_state" / "verification" / "sign_law.json"))["rows"]
def canon(w):
    sw = w.translate(str.maketrans("LR", "RL")); return min([w[i:] + w[:i] for i in range(len(w))] + [sw[i:] + sw[:i] for i in range(len(sw))])
amph = {(r["sign"], r["word"]): r["amphichiral"] for r in S}
out = []
for r in rows:
    sg, w = r["state"][0], canon(r["state"][1:])
    out.append(dict(state=r["state"], sign=sg, word=w, length=len(w), amphichiral=amph.get((sg, w)), firing=r["firing"], generation_backgrounds=r["generation_backgrounds"], characters=r["characters"]))
tab = collections.Counter(); 
for r in out: tab[(r["sign"], r["amphichiral"], r["firing"] > 0, r["generation_backgrounds"] > 0)] += 1
summ = dict(own_level_states=len(out), by_sign={s: sum(1 for r in out if r["sign"] == s) for s in "+-"},
            firing_by_sign={s: sum(1 for r in out if r["sign"] == s and r["firing"] > 0) for s in "+-"},
            generation_by_sign={s: sum(1 for r in out if r["sign"] == s and r["generation_backgrounds"] > 0) for s in "+-"},
            amphichiral_states=sum(1 for r in out if r["amphichiral"]), unknown_amphichirality=sum(1 for r in out if r["amphichiral"] is None),
            amphichiral_firing={s: [r["state"] for r in out if r["amphichiral"] and r["sign"] == s and r["firing"] > 0] for s in "+-"},
            amphichiral_generation={s: [r["state"] for r in out if r["amphichiral"] and r["sign"] == s and r["generation_backgrounds"] > 0] for s in "+-"},
            words_firing_with_both_signs=sorted({r["word"] for r in out if r["firing"] > 0 and any(q["word"] == r["word"] and q["sign"] != r["sign"] and q["firing"] > 0 for q in out)}),
            table={str(k): v for k, v in sorted(tab.items(), key=str)})
json.dump(dict(summary=summ, rows=out), open(HERE / "index_by_sign.json", "w"), indent=0); print(json.dumps(summ)[:2400])
