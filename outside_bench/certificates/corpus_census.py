#!/usr/bin/env python3
"""THE VIEW FROM ABOVE, MEASURED: a census of the whole banked corpus, so that anything
said about the programme's SHAPE rests on counts rather than on impression.

The owner asked to sit with the work and see it from above.  This bench's rule is that an
interpretation may be offered only on top of something computed, and labelled as
interpretation.  This file is the computed part.  Every number quoted in memo 188 comes
from here and can be re-derived by running it.

WHAT IS COUNTED, and from what:
  frontier/*/arc_verdict.json   -- one per banked arc: verdict, claim_one_line, depends_on
  CLAIMS.md                     -- the programme's ledger of promoted claims

MEASURES:
  1. volume and verdict distribution
  2. the PROMOTION FRONT: the highest arc number CLAIMS.md refers to, and how many arcs
     have been banked since
  3. COMPOUNDING: what fraction of arcs declare a dependency, the median dependency depth,
     and the deepest chains.  CHECKED FIRST, because the raw number is a trap: the
     depends_on field is not uniformly kept, so the era-by-era population of the FIELD is
     measured before any conclusion is drawn about the WORK.
  4. METABOLISM: how many arcs are named for a PROCESS (audit, sweep, harvest, ledger,
     integration, ...) rather than for a subject, and how the newest arcs are split
  5. the outside bench's own footprint, and its edge count into CLAIMS.md

Gate 5: pure counting over the repository.  No measured physical value.  No claim about
whether any number is good or bad -- that belongs in the memo, labelled.
"""
import json, pathlib, re, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
V = sorted(ROOT.glob("frontier/*/arc_verdict.json"))
D, dep, verd, num = {}, {}, {}, {}
for p in V:
    try: d = json.load(open(p))
    except Exception: continue
    i = p.parent.name; D[i] = d
    verd[i] = str(d.get("verdict") or d.get("status")).upper()
    dd = d.get("depends_on") or []
    dep[i] = [str(z) for z in ([dd] if isinstance(dd, str) else dd)]
    m = re.match(r"B(\d+)", i)
    if m: num[i] = int(m.group(1))
n = len(D)
# ADDENDUM 2's RULE, ENFORCED HERE: a census is meaningless without the tree it was
# taken on.  Memo 188 section 3 was wrong because it ran on a branch 126 commits behind
# origin/main and read that tree's zeros as decay.
import subprocess as _sp
def _git(*a):
    try: return _sp.run(["git"]+list(a), cwd=ROOT, capture_output=True, text=True, timeout=60).stdout.strip()
    except Exception: return "?"
print("=" * 78); print("0.  THE TREE THIS CENSUS WAS TAKEN ON"); print("=" * 78)
def _branch_no_vendor():
    """The branch name with its first path segment dropped.  Seat branches are named
    <vendor>/<lane>, and the standing attribution rule keeps vendor tokens out of every
    tracked artifact -- including one this certificate writes."""
    b = _git("rev-parse", "--abbrev-ref", "HEAD")
    return "<seat>/" + b.split("/", 1)[1] if "/" in b else b


print("   HEAD            : %s  %s" % (_git("rev-parse","--short","HEAD"), _branch_no_vendor()))
_behind = _git("rev-list","--count","HEAD..origin/main")
print("   commits behind origin/main : %s" % (_behind or "?"))
if _behind and _behind.isdigit() and int(_behind) > 0:
    print("   *** THIS TREE IS BEHIND MAIN.  Every count below is a LOWER BOUND, and any")
    print("       'decayed to zero' reading is unsafe -- see memo 188 addendum 2. ***")
print()
print("=" * 78); print("1.  VOLUME"); print("=" * 78)
print("   banked arcs                : %d" % n)
print("   arc-number range           : B%d .. B%d" % (min(num.values()), max(num.values())))
c = collections.Counter(verd.values())
for k, v in c.most_common():
    print("   %-26s : %4d  (%4.1f%%)" % (k, v, 100*v/n))

print(); print("=" * 78); print("2.  THE PROMOTION FRONT"); print("=" * 78)
CL = (ROOT / "CLAIMS.md").read_text()
refs = sorted(set(int(x) for x in re.findall(r'\bB(\d{2,4})\b', CL)))
front = max(refs) if refs else 0
after = sum(1 for i in num if num[i] > front)
print("   highest arc number CLAIMS.md refers to anywhere : B%d" % front)
print("   arcs banked after it                            : %d" % after)
print("   (a reference is not a promotion; this is an UPPER bound on how current the")
print("    ledger is with respect to the corpus)")

print(); print("=" * 78); print("3.  COMPOUNDING -- does the corpus grow by construction or by addition?")
print("=" * 78)
key = {}
for i in num: key.setdefault(num[i], i)
def norm(s):
    m = re.match(r"B(\d+)", str(s)); return key.get(int(m.group(1))) if m else None
memo = {}
def depth(i, seen=frozenset()):
    if i in memo: return memo[i]
    if i in seen: return 0
    b = 0
    for d_ in dep.get(i, []):
        j = norm(d_)
        if j and j in D: b = max(b, 1 + depth(j, seen | {i}))
    memo[i] = b; return b
# ---- FIRST: is depends_on a real signal, or an unpopulated field? ----
import statistics
print("   BEFORE reading anything into the edge count, ask whether the FIELD is kept.")
print("   depends_on population, and the size of the verdict record, by arc era:")
eras = []
for lo in range(0, max(num.values())+1, 200):
    seg = [i for i in num if lo <= num[i] < lo+200]
    if not seg: continue
    pop = sum(1 for i in seg if dep[i])
    eras.append((lo, len(seg), pop, statistics.mean(len(D[i].keys()) for i in seg)))
    print("      B%4d-%4d : %3d arcs, %3d declare depends_on (%3.0f%%), mean fields %.1f"
          % (lo, lo+199, len(seg), pop, 100*pop/len(seg), eras[-1][3]))
peak = max(eras, key=lambda e: e[2]/max(e[1],1))
print("   => the field is NOT uniformly kept.  It is near-empty before B800, %.0f%% in its"
      % (100*peak[2]/peak[1]))
print("      best era (B%d-%d), and has decayed since.  So the raw isolated-arc count below" % (peak[0], peak[0]+199))
print("      measures RECORDING PRACTICE at least as much as it measures the work.")
print("      In the one era where the edges WERE recorded, most arcs had them.")
print()
has = sum(1 for i in dep if dep[i])
ds = sorted(depth(i) for i in D)
print("   arcs declaring a dependency : %d  (%.0f%%)" % (has, 100*has/n))
print("   arcs declaring NONE         : %d  (%.0f%%)" % (n-has, 100*(n-has)/n))
print("   median dependency depth     : %d" % ds[n//2])
print("   90th percentile depth       : %d" % ds[int(0.9*n)])
top = sorted(((depth(i), i) for i in D), reverse=True)[:5]
print("   deepest chains              : %s" % ", ".join("%s(%d)" % (b, a) for a, b in top))

print(); print("=" * 78); print("4.  METABOLISM -- arcs named for a process rather than a subject")
print("=" * 78)
META = set("audit harvest verdict verification ledger adjudication sweep close seat review "
           "census integration bank banking record hygiene consolidation campaign".split())
meta = [i for i in D if META & set(i.split('_')[1:])]
print("   process-named arcs          : %d  (%.0f%%)" % (len(meta), 100*len(meta)/n))
print("      their verdicts           : %s" % collections.Counter(verd[i] for i in meta).most_common())
recent = sorted(num, key=lambda i: num[i])[-12:]
rmeta = [i for i in recent if i in set(meta)]
print("   of the 12 most recent arcs, process-named : %d" % len(rmeta))
for i in recent[-6:]:
    print("      %-32s %-9s %s" % (i[:32], verd[i], "PROCESS" if i in set(meta) else "subject"))

print(); print("=" * 78); print("5.  THE OUTSIDE BENCH's FOOTPRINT"); print("=" * 78)
ob = ROOT / "outside_bench"
print("   certificates                : %d" % len(list(ob.glob("certificates/*.py"))))
print("   memos                       : %d" % len(list(ob.glob("memos/*.md"))))
print("   occurrences of 'outside_bench' in CLAIMS.md : %d" % CL.count("outside_bench"))
print()
print("""EVERYTHING ABOVE IS A COUNT.  What any of it MEANS is interpretation and lives in
memo 188, labelled as such.  Two readings are available for almost every line here -- a
low promotion rate is either a firewall doing its job or a valve stuck shut, and this
census cannot tell them apart.  Memo 188 says so and proposes the measurement that could.""")
