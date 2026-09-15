#!/usr/bin/env python3
"""MEMO-138 CELL (the owner released the specialist send-queue hold, in
words): THE READINESS AUDIT — run BEFORE anything leaves, because a send
is outward-facing and cannot be recalled.  Result: the queue is STALE on
its highest-priority bar, and the staleness is exactly the kind that
damages a send.

WHAT THE RELEASE DOES AND DOES NOT DO.  The owner's 2026-08-27 decision
box read "ALL SIX = HOLD", with the reason recorded verbatim: "I don't
plan to send anything yet.  We will craft another paper ... after we
exhaust the math."  The owner has now reversed that, which is theirs to
do.  TWO THINGS IN THE QUEUE'S OWN CONSTRUCTION SURVIVE THE REVERSAL:
  * "nothing leaves without the owner's PER-ITEM word" — a blanket
    release does not supply six per-item words; and
  * "the send is THE OWNER'S ACT UNDER THE OWNER'S NAME" — so this bench
    does not transmit, by the queue's own mechanics.  It prepares.
This cell therefore does the one thing that IS the bench's: check whether
each bar's stated status is still TRUE, since a specialist who is sent a
stale status is being misinformed by us, and that cannot be taken back.

THE TEST.  The queue was built at B1179.  Any arc numbered ABOVE B1179
that names a bar's subject is movement the queue does not reflect.
Mechanical, over the corpus's own arc claims.
  READY   — no post-B1179 arc touches the bar; the status line stands.
  STALE   — post-B1179 arcs touch it; the status line must be rewritten
            before the item can go out.
Gate 5 untouched: repository metadata only.
"""
import json, glob, re, collections

import _oa_source as OA          # PINNED source (codex fix)
arcs = OA.arc_verdicts()

def num(a):
    m = re.match(r"^B(\d+)$", a or "")
    return int(m.group(1)) if m else -1

BUILT_AT = 1179
later = {k: v for k, v in arcs.items() if num(k) > BUILT_AT}
print(f"A1 — the queue was built at B{BUILT_AT}; the corpus has banked"
      f" {len(later)} arcs above it.")
assert len(later) > 10

BARS = [
    ("Q1", "SEAM-A Gate 2 (the prize crossing)", 4,
     ["seam-a", "gate 2", "andersen", "arithmetic-cs", "cusped extension",
      "lee", "w0 bar", "arakelov"]),
    ("Q2", "J3(O) Beilinson regulators", 3,
     ["j3(o)", "beilinson", "regulator", "tier b", "exceptional-domain"]),
    ("Q3", "the B491 seam form", 3,
     ["b491", "seam form", "level 15", "weil representation", "sqrt(-15)"]),
    ("Q4", "Cappell-Miller order of vanishing", 2,
     ["cappell", "miller", "ruelle", "analytic torsion", "sym^2"]),
    ("Q5", "B165 complexified hyperbolicity", 2,
     ["b165", "complexified", "cantat", "loray", "off-axis"]),
    ("Q6", "the closed-form k (rider)", 1,
     ["closed-form k", "b154", "order-based exponent"]),
]
print("\nA2 — PER-BAR STALENESS (arcs above B1179 that name the bar's subject):")
verdicts = {}
for qid, name, prio, kws in BARS:
    hits = []
    for k, v in sorted(later.items(), key=lambda t: num(t[0])):
        c = (v.get("claim_one_line") or "").lower()
        if any(w in c for w in kws):
            hits.append(k)
    verdicts[qid] = hits
    tag = "STALE" if hits else "READY"
    print(f"    [{tag:>5s}] {qid} ({'*'*prio}) {name}")
    if hits:
        print(f"            touched by {len(hits)} post-queue arcs: {', '.join(hits)}")
stale = [q for q, h in verdicts.items() if h]
print(f"\n    ==> {len(stale)} of {len(BARS)} bars are STALE: {', '.join(stale)}")

# ---- A3: the decisive one
print("\nA3 — THE DECISIVE CASE: Q1, the queue's own four-star item.")
for a in ("B1198", "B1201", "B1209"):
    v = arcs.get(a)
    if v:
        print(f"    {a}: {(v.get('claim_one_line') or '')[:150]}...")
print("    The queue's Q1 status line reads: \"FLOOR (B1156); the a-priori")
print("    MISMATCH refuted; the full/Arakelov row carries Vol as the Borel")
print("    regulator; the one bar is the cusped extension.\"")
print("    SINCE THEN, on this same bar: the Lee paper was OBTAINED AND READ")
print("    on-bench (B1209, the CITED/UNVERIFIED grade paid), the admissible")
print("    tangential base point was answered FROM THE SOURCE and found")
print("    UNIQUE not free (B1201 correcting B1198), and a hoped-for bridge")
print("    to the observer's bit was CLOSED.")
print("    => sending Q1 as written would hand a specialist a status line")
print(f"       that omits {len(verdicts['Q1'])} of our own subsequent arcs, INCLUDING ONE THAT")
print("       KILLED A BRIDGE WE HAD HOPED FOR.  That is not a small edit:")
print("       it misstates what we already know, and it cannot be recalled.")
assert verdicts["Q1"]

print("""
A4 — THE VERDICT AND THE ASK.
  THE HOLD IS RELEASED — recorded, and the owner's reversal of their own
  2026-08-27 decision box is theirs to make.  NOTHING IS BLOCKED BY THIS
  BENCH.  But two of the queue's own rules survive the release, and one
  finding is added:
   (1) THE SEND IS THE OWNER'S ACT UNDER THE OWNER'S NAME (the queue's
       mechanics).  This bench does not transmit; it prepares.
   (2) NOTHING LEAVES WITHOUT A PER-ITEM WORD (the queue's own rule).  A
       blanket release does not supply six.
   (3) THE QUEUE IS STALE WHERE IT MATTERS MOST.  Q1 — the single
       four-star item, "the one live crossing" — has had four arcs land
       on it since the queue was written (8 by the sweep), one of
       which closed a bridge.
       Its ask must be REWRITTEN before it goes anywhere.
  RECOMMENDED SEQUENCE, cheapest first:
   a. REWRITE Q1's status line from B1198/B1201/B1209 (the ask NARROWS:
      the literature half is partly done in-house now, so the specialist
      is being asked something sharper than before — which makes it a
      BETTER send, not a worse one).
   b. Re-check Q2's status against B1209's surviving half ("an outside
      motive over our field whose Beilinson regulator is our complex
      volume") — that is Q2's own subject and may have moved too.
   c. Then take the six per-item decisions in one pass.
  ONE THING RECORDED WITHOUT RELITIGATING IT: the owner's original reason
  for the hold was sequencing — "we will craft another paper ... after we
  exhaust the math."  The paper is currently mid-flight WITH A KNOWN
  DEFECT (memo 133: its claim base reads a field 89% of settled arcs
  never filled).  Stated once, because it bears on sequencing; the
  decision remains the owner's and this bench proceeds either way.
  FENCE: nothing was sent, no address was touched, no external contact of
  any kind was made by this cell.  Gate 5 untouched.""")
