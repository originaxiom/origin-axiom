#!/usr/bin/env python3
"""L244 (a) census: merge the readers' tables, verify quotes verbatim against the text each reader was given, tabulate."""
import json, pathlib, collections, re
S = pathlib.Path(__file__).resolve().parent
KINDS = ("PAIRING", "FLATNESS", "NON-UNIQUENESS", "OTHER")
text = {}
for b in sorted((S / "readers").glob("batch_[0-9].json")):
    for e in json.load(open(b)):
        if e["claim_killed"] or e["id"] not in text:
            text[e["id"]] = (e["claim_killed"] or "") + "\n" + (e.get("kill_form") or "") + "\n" + (e.get("hatch") or "")
rows = {}
for o in sorted((S / "readers").glob("out_[0-9].json")):
    for r in json.load(open(o)): rows[r["id"]] = dict(r, source=o.name)
# population: entries WITH claim text (the kills). The 343 empty-text entries are B842's FACE-ONLY records (329 of them
# on PROVED arcs) -- not kills; their rebuilt readings (out_r*) are kept on disk and excluded from the census.
kills = {i for i, t in text.items() if t.split("\n")[0].strip()}
rows = {i: r for i, r in rows.items() if i in kills}
text = {i: t for i, t in text.items() if i in kills}
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
verified, discarded = {}, []
for i, r in rows.items():
    q = (r.get("quote") or "").strip()
    ok = (q == "" and r["kind"] == "OTHER") or (q and norm(q) in norm(text.get(i, "")))
    if r["kind"] not in KINDS: ok = False
    (verified.__setitem__(i, r) if ok else discarded.append((i, r.get("kind"), q[:60])))
tab = collections.Counter(r["kind"] for r in verified.values())
labels = collections.Counter((r["kind"], (r.get("label") or "").lower()) for r in verified.values() if r["kind"] == "OTHER")
conf = collections.Counter((r["kind"], r.get("confidence")) for r in verified.values())
out = dict(entries=len(text), read=len(rows), verified=len(verified), discarded=discarded, by_kind=dict(tab),
           other_labels=sorted(((k[1], v) for k, v in labels.items()), key=lambda x: -x[1]), confidence=dict((" ".join(map(str, k)), v) for k, v in conf.items()),
           members={k: sorted(i for i, r in verified.items() if r["kind"] == k) for k in KINDS},
           rows=verified)
json.dump(out, open(S / "census.json", "w"), indent=1)
print("entries", len(text), "read", len(rows), "verified", len(verified), "discarded", len(discarded))
print("by kind", dict(tab)); print("OTHER labels", out["other_labels"][:15]); print("confidence", out["confidence"])
