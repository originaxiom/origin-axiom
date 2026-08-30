#!/usr/bin/env python3
"""THE REGISTER-TO-QUEUE JOIN SWEEP.

Route A surfaced because a paper audit happened to walk past it. If the join between
the registers (which TYPE residuals as specialist-shaped) and SPECIALIST_SEND_QUEUE.md
(which carries Q1-Q6) is broken in general, the programme's specialist questions are
being found by luck. This measures the join.

Pinned to the paper's own commit. Reads text only; Gate 5 untouched.
"""
import os, re, sys, subprocess
PIN = "89affd5bbd4b900397af2bf3b987ff8f05f5cb80"
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
def show(p): return subprocess.run(["git","-C",REPO,"show",f"{PIN}:{p}"],
                                   capture_output=True, text=True).stdout

REGISTERS = ["docs/OPEN_PROBLEMS.md", "docs/OPEN_LEADS.md", "docs/CAMPAIGN_STATUS.md",
             "docs/THE_LADDER.md", "docs/THE_FRAMEWORK.md", "docs/SEAL_LEDGER.md",
             "docs/HINT_LEDGER.md", "docs/views/REVIEWER.md"]
# how the corpus marks "this needs someone outside"
MARKERS = [r"NEEDS[- ]SPECIALIST", r"specialist-shaped", r"specialist question",
           r"frontier mathematics", r"literature[- ]floor", r"literature residual",
           r"literature lane", r"needs a specialist"]
MARK_RE = re.compile("|".join(MARKERS), re.I)

print("="*80); print("THE REGISTER-TO-QUEUE JOIN SWEEP  @", PIN[:8]); print("="*80)

# ---- 1. what the queue currently carries
q = show("docs/SPECIALIST_SEND_QUEUE.md")
qrows = re.findall(r"^\|\s*(Q\d)\s*\|\s*\*\*(.+?)\*\*", q, re.M)
print(f"\nQUEUE: {len(qrows)} items")
for qid, subj in qrows: print(f"  {qid}  {subj}")
qtext = q.lower()

# ---- 2. every specialist-marked passage in the registers
hits = []
for f in REGISTERS:
    t = show(f)
    if not t: continue
    for m in MARK_RE.finditer(t):
        ls = t.rfind("\n", 0, max(0, m.start()-1500)) + 1
        le = t.find("\n", m.end() + 900)
        seg = t[ls:le if le > 0 else len(t)]
        hits.append((f, m.group(0), seg))
print(f"\nSPECIALIST-MARKED PASSAGES across {len(REGISTERS)} registers: {len(hits)}")
byfile = {}
for f, mk, _ in hits: byfile[f] = byfile.get(f, 0) + 1
for f, n in sorted(byfile.items(), key=lambda x: -x[1]): print(f"  {n:>3}  {f}")

# ---- 3. does each marked passage's SUBJECT appear in the queue?
#     mechanical proxy: the arc ids and the distinctive capitalised subject tokens
def subject_keys(seg):
    arcs = set(re.findall(r"\bB\d{3,4}\b", seg))
    caps = set(re.findall(r"\b(?:Kato[-–]Yukie|Bhargava|Krutelevich|Thorne|Freudenthal|"
                          r"Andersen[-–]Hansen|Cappell[-–]Miller|Beilinson|Seiberg[-–]Witten|"
                          r"Weil|Arakelov|Ruelle|Maass|Kim|Lee|Borel)\b", seg))
    return arcs, caps

print("\n" + "-"*80)
print("JOIN TEST -- for each marked passage, is its subject reachable from the queue?")
print("-"*80)
unjoined = []
for f, mk, seg in hits:
    arcs, caps = subject_keys(seg)
    if not arcs and not caps: continue
    in_q = [c for c in caps if c.lower() in qtext] + [a for a in arcs if a in q]
    if not in_q:
        line = " ".join(seg.split())
        unjoined.append((f, mk, sorted(caps) or sorted(arcs)[:4], line))
print(f"\nmarked passages whose subject is NOT reachable from the queue: {len(unjoined)}")
seen = set()
for f, mk, keys, line in unjoined:
    k = tuple(keys)
    if k in seen: continue
    seen.add(k)
    print(f"\n  [{f}]  marker={mk!r}")
    print(f"    subject keys: {keys}")
    print(f"    ...{line[:330]}...")
print("\n" + "="*80)
print(f"JOIN: queue carries {len(qrows)} items; registers mark specialist-shaped "
      f"material in {len(hits)} passages; {len(seen)} distinct subjects are unreachable.")
print("="*80)

# ---- 4. ADJUDICATION: the raw count is a detector's output, not a result.
#     B1210 cut 15/24 -> 5/24 by scoping; this bench has produced three keyword false
#     positives this session. So filter to passages whose OWN disposition still reads live.
DEAD = re.compile(r"\b(CLOSED|RESOLVED|DONE|RETIRED|SUPERSEDED|WITHDRAWN|ANSWERED|"
                  r"CHARACTERIZED|DISSOLVED|COMPUTE CLOSED|NOT-POSABLE)\b")
LIVE = re.compile(r"\b(OPEN|NEEDS-SPECIALIST|remains|still|residual|owed|not attempted|"
                  r"never attempted|unproved)\b", re.I)
live = []
for f, mk, keys, line in unjoined:
    tail = line[-700:]
    if DEAD.search(tail) and not re.search(r"remains (the |a )?(literature|specialist)", line, re.I):
        continue
    if not LIVE.search(line):
        continue
    live.append((f, mk, keys, line))
print("\n" + "="*80)
print("ADJUDICATED -- passages still reading LIVE and still unreachable from the queue")
print("="*80)
seen2 = set()
for f, mk, keys, line in live:
    k = tuple(keys)
    if k in seen2: continue
    seen2.add(k)
    print(f"\n  [{os.path.basename(f)}] {mk!r}  keys={keys}")
    print(f"    ...{line[:260]}...")
print(f"\nRAW unreachable subjects: {len(seen)}   ADJUDICATED live-and-unreachable: {len(seen2)}")
print("Report BOTH numbers -- the gap between them is the detector's noise, and it is the point.")

