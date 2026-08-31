#!/usr/bin/env python3
"""THE ESSENCE CENSUS -- the structural questions, asked of the whole corpus at once.

Not a new mathematical result.  This certifies the COUNTS behind memo 168, so the memo's
claims are reproducible rather than asserted (bench error #15's lesson: a headline with no
certificate and a wrong one look identical from outside).

E-1  the verdict distribution
E-2  the law-citation graph: does the corpus LOSE its own results?
E-3  the term census behind the memo's novelty claims (memo 153: terms stated with the claim)
E-4  the send-queue coverage check

Gate 5 untouched: this reads text and counts. No measured value.
"""
import os, re, json, collections, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
F = os.path.join(ROOT, "frontier")
D = os.path.join(ROOT, "docs")

def read(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as f: return f.read()
    except OSError: return ""

recs = {}
for d in sorted(os.listdir(F)):
    p = os.path.join(F, d, "arc_verdict.json")
    if not os.path.exists(p): continue
    try: j = json.loads(read(p))
    except Exception: continue
    m = re.match(r"(B\d+)", d)
    recs[m.group(1) if m else d] = {
        "dir": d, "v": str(j.get("verdict", "")), "c": str(j.get("claim_one_line", "")),
        "law": j.get("creates_law"),
        "text": str(j.get("claim_one_line", "")) + "\n" + read(os.path.join(F, d, "FINDINGS.md")),
    }

print("=" * 78); print("E-1  THE VERDICT DISTRIBUTION"); print("=" * 78)
V = collections.Counter(r["v"] for r in recs.values())
print(f"     arcs with arc_verdict.json : {len(recs)}")
for k, n in V.most_common():
    print(f"       {n:5d}  {k:<10} {100.0*n/len(recs):5.1f}%")
laws = [a for a, r in recs.items() if r["law"] is True]
print(f"     creates_law = True         : {len(laws)}")

print("\n" + "=" * 78); print("E-2  DOES THE CORPUS LOSE ITS OWN RESULTS?"); print("=" * 78)
BID = re.compile(r"\bB(\d{1,4})\b")
num = lambda a: int(a[1:])
later = collections.Counter()
for aid, r in recs.items():
    n = num(aid)
    for m in set(BID.findall(r["text"])):
        t = "B" + m
        if t != aid and t in recs and int(m) < n: later[t] += 1
orph = sorted([a for a in laws if later[a] == 0], key=num)
newest = max(num(a) for a in recs)
print(f"     banked LAWS never cited by any later arc : {len(orph)} of {len(laws)}")
print(f"     newest arc in corpus                     : B{newest}")
print(f"     those {len(orph)} laws: {', '.join(orph)}")
print(f"     lowest of them: {orph[0] if orph else '-'}  "
      f"-> all lie within the last {newest - num(orph[0]) if orph else 0} arcs")
E2 = "E2-NO-LOSS" if all(newest - num(a) < 60 for a in orph) else "E2-ORPHANS"
print(f"     OUTCOME: {E2}   (recency, not amnesia: a law banked last week has no later arc to cite it)")

print("\n" + "=" * 78); print("E-3  TERM CENSUS -- the terms behind memo 168's claims"); print("=" * 78)
docs = {f: read(os.path.join(D, f)) for f in os.listdir(D) if f.endswith(".md")}
def census(term):
    a = sum(1 for r in recs.values() if term.lower() in r["text"].lower())
    d = sum(1 for t in docs.values() if term.lower() in t.lower())
    return a, d
for t in ["lattice VOA", "free boson", "six cusps", "degree 6 cover", "congruence cover",
          "cusp count", "multi-cusp", "Cardy", "cusp-boson", "six cusp-boson"]:
    a, d = census(t)
    print(f"     {a:5d} arcs / {d:3d} docs :: {t!r}")

print("\n" + "=" * 78); print("E-4  SEND-QUEUE COVERAGE"); print("=" * 78)
q = read(os.path.join(D, "SPECIALIST_SEND_QUEUE.md"))
rows = re.findall(r"^\|\s*(Q\d+)\s*\|", q, re.M)
print(f"     rows in docs/SPECIALIST_SEND_QUEUE.md : {len(rows)}  ({', '.join(rows)})")
for t in ["L154", "sigma", "σ", "Cardy", "central charge", "six cusp", "multi-cusp",
          "boundary CFT", "boundary VOA", "Brown-Henneaux", "E6)_1", "(E₆)₁"]:
    print(f"       {q.lower().count(t.lower()):3d}  occurrences of {t!r}")
E4 = "E4-UNQUEUED" if not re.search(r"L154|Cardy|central charge|multi-cusp", q, re.I) else "E4-QUEUED"
print(f"     OUTCOME: {E4}")

print("\n" + "=" * 78)
print(f"SUMMARY: {E2} | {E4}")
print("=" * 78)
