"""S14: recompute the identification ledger's irreducible input count, B1266's method, on today's rows.

B1266 (2026-09-06) reduced 10 UNEARNED rows to 7 irreducible sources by union-find over the rows' own stated
dependencies, with two traps: an EARNED row is not a debt, and a 2-cycle is one source, not two. Four rows have
landed since. Control: restricted to B1266's ten rows this reproduces its partition exactly.
Run: python3 identification_recount.py
"""
import re, io, collections, pathlib
LEDGER = pathlib.Path(__file__).resolve().parents[3] / "docs" / "IDENTIFICATION_LEDGER.md"
rows = {}
for line in io.open(LEDGER, encoding="utf-8").read().split("\n"):
    m = re.match(r"\|\s*(I-\d+)\s*\|(.*)$", line)
    if not m:
        continue
    st = "UNKNOWN"
    for s in ("EARNED", "REFUTED", "UNEARNED", "PRICED", "SCOPED", "CLOSED"):
        if re.search(r"\*\*" + s + r"\*\*", m.group(2)):
            st = s
            break
    rows[m.group(1)] = (st, m.group(2))
unearned = [r for r, (s, _) in rows.items() if s == "UNEARNED"]
parent = {r: r for r in unearned}
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[ra] = rb
for r in unearned:
    for tgt in re.findall(r"I-\d+", rows[r][1]):
        if tgt != r and rows.get(tgt, ("", ""))[0] == "UNEARNED":   # an EARNED row is not a debt
            union(r, tgt)                                           # symmetric: a 2-cycle is ONE source
groups = collections.defaultdict(list)
for r in unearned:
    groups[find(r)].append(r)
print("rows %d  EARNED %d  REFUTED %d  UNEARNED %d" % (len(rows),
      sum(1 for s, _ in rows.values() if s == "EARNED"),
      sum(1 for s, _ in rows.values() if s == "REFUTED"), len(unearned)))
for k, v in sorted(groups.items(), key=lambda kv: int(kv[0][2:])):
    print("   source:", sorted(v, key=lambda x: int(x[2:])))
print("irreducible sources: %d   free inputs = 4 axioms + %d = %d" % (len(groups), len(groups), 4 + len(groups)))
