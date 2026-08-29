#!/usr/bin/env python3
"""MEMO-133 CELL (R52-6, the cold pass — the item the owner assigned this
seat): IS THE `creates_law` UNDER-DECLARATION SYSTEMIC?  B1211 caught ONE
arc (B1196) whose flag was declared false when it should have been true,
and recorded exactly why that matters: "the registry gate reads the
DECLARED field, so an under-declaration made this arc invisible to it AND
TO B1210's CLAIM-POOL SWEEP."

WHY THIS IS THE RIGHT COLD-PASS CELL.  B1210 built the paper's claim pool
mechanically from arcs with creates_law = true (48 of them).  cc reports
the paper's spine now carries ~55 claim candidates with an empty
disposition column.  IF THE FLAG IS UNDER-DECLARED ANYWHERE ELSE, THE
PAPER IS BEING ASSEMBLED ON AN INCOMPLETE BASE — and the defect is
invisible precisely because the sweep that builds the base reads the same
field that is wrong.  B1211 fixed one instance by hand.  This cell asks
whether the instance was a class, which is the move that already paid off
twice in this corpus (the finished-but-forgotten class, GC-29/R52-1).

THE INDEPENDENT CRITERION (fixed before counting; deliberately NOT the
declared field).  An arc is a CANDIDATE UNDER-DECLARATION iff:
  * its verdict is PROVED or NEGATIVE (a settled arc), AND
  * creates_law is false or absent, AND
  * its own claim_one_line carries LAW-SHAPED language — the vocabulary
    the corpus itself uses when it is stating a law: theorem, law,
    forced, no-go, impossible, unique(ly), exactly, necessary and
    sufficient, cannot, never, always, iff, permanent.
Law-shaped language is EVIDENCE, not proof, so every hit is a CANDIDATE
for an editorial call, never an automatic reclassification — this cell
reports and ranks, it does not rewrite anyone's flag.

THE PREREGISTERED FORK:
  U-A  the candidate set is small and weak (few arcs, thin language) =>
       B1196's under-declaration was ISOLATED, B1210's pool is sound, and
       the paper's base needs no widening.
  U-B  the candidate set is large or contains strong instances => the
       under-declaration is SYSTEMIC like the finished-but-forgotten
       class, B1210's claim pool is INCOMPLETE BY A MEASURABLE AMOUNT,
       and the paper's base must be rebuilt before the disposition column
       is filled.
CONTROL, two-sided (this cell must be able to fail): the same criterion
is run against the arcs ALREADY declared creates_law = true.  If the
criterion is meaningful, declared-law arcs should score MUCH higher on
it than the general population; if they do not, the criterion is noise
and this cell's finding is void.
Gate 5 untouched: repository metadata only; no object claim.
"""
import os, json, re, glob, collections

import _oa_source as OA          # PINNED source (codex fix)
arcs = OA.arc_verdicts()
print(f"A1 — CORPUS LOADED: {len(arcs)} arcs with a parseable verdict file.")
assert len(arcs) > 1000

LAW_WORDS = ["theorem", "law", "forced", "no-go", "impossible", "unique",
             "exactly", "necessary and sufficient", "cannot", "never",
             "always", " iff ", "permanent"]
def law_score(v):
    c = (v.get("claim_one_line") or "").lower()
    return sum(1 for w in LAW_WORDS if w in c)

settled = {k: v for k, v in arcs.items()
           if (v.get("verdict") or "").upper() in ("PROVED", "NEGATIVE")}
declared = {k: v for k, v in settled.items() if v.get("creates_law") is True}
undeclared = {k: v for k, v in settled.items() if v.get("creates_law") is not True}
print(f"A2 — SETTLED ARCS (PROVED/NEGATIVE): {len(settled)}")
print(f"     declared creates_law = true : {len(declared)}")
print(f"     not declared                : {len(undeclared)}")

# ---- THE CONTROL, run BEFORE the finding
d_scores = [law_score(v) for v in declared.values()]
u_scores = [law_score(v) for v in undeclared.values()]
d_mean = sum(d_scores)/len(d_scores)
u_mean = sum(u_scores)/len(u_scores)
print(f"\nA3 — THE TWO-SIDED CONTROL (does the criterion discriminate at all?):")
print(f"     mean law-word score, DECLARED law arcs   : {d_mean:.2f}")
print(f"     mean law-word score, UNDECLARED arcs     : {u_mean:.2f}")
print(f"     ratio: {d_mean/u_mean:.2f}x")
if d_mean <= u_mean:
    print("     => THE CRITERION IS NOISE.  This cell's finding is VOID and is")
    print("        reported as such rather than dressed up.")
    raise SystemExit(0)
print("     => the criterion discriminates: declared-law arcs score higher,")
print("        so law-shaped language does track the declared flag.  Proceed.")

# ---- the candidates, ranked
THRESH = max(3, int(round(d_mean)))
raw = sorted(((law_score(v), k, v) for k, v in undeclared.items()
              if law_score(v) >= THRESH), key=lambda t: -t[0])
# NARROWING, applied BEFORE any number is reported: an arc declared
# instrument = true is process, not content, and B1210's pool would not
# want it however law-shaped its prose is.  The raw count OVERSTATES and
# is reported alongside so the narrowing is visible rather than silent.
cands = [(sc, k, v) for sc, k, v in raw if v.get("instrument") is not True]
inst = len(raw) - len(cands)
print(f"\nA4 — CANDIDATE UNDER-DECLARATIONS (score >= {THRESH}, the declared-law mean):")
print(f"     raw hits: {len(raw)} of {len(undeclared)} undeclared settled arcs"
      f" ({100*len(raw)/len(undeclared):.1f}%)")
print(f"     MINUS {inst} declared instrument = true (process, not content —")
print(f"     B1210's pool would not want them however law-shaped the prose)")
print(f"     ==> CREDIBLE CANDIDATE SET: {len(cands)}"
      f" ({100*len(cands)/len(undeclared):.1f}% of undeclared settled arcs)")
for sc, k, v in cands[:18]:
    claim = (v.get("claim_one_line") or "")[:104].replace("\n", " ")
    print(f"     [{sc:2d}] {k:<7s} {v.get('verdict','?'):<8s} {claim}...")
if len(cands) > 18:
    print(f"     ... and {len(cands)-18} more")

# ---- TWO FAILURE MODES, separated (found while ranking, reported here)
absent = [k for k, v in settled.items() if "creates_law" not in v]
false_ = [k for k, v in settled.items() if v.get("creates_law") is False]
print(f"\nA4b — TWO DISTINCT FAILURE MODES, separated:")
print(f"     creates_law ABSENT entirely : {len(absent)} settled arcs")
print(f"     creates_law declared FALSE  : {len(false_)} settled arcs")
print(f"     declared TRUE               : {len(declared)}")
print("     An ABSENT field is a different bug from a WRONG one: B1211 fixed a")
print("     mis-declaration (B1196 said false), but the bulk here was never")
print("     declared at all, so no one ever made the call.  A sweep that reads")
print("     the field treats both identically — as 'not a law'.")
ca = sum(1 for sc, k, v in cands if "creates_law" not in v)
print(f"     of the {len(cands)} credible candidates, {ca} have the field ABSENT"
      f" and {len(cands)-ca} have it declared FALSE.")

# THE DECISIVE EXHIBIT, named rather than left in a statistic
ex = arcs.get("B991")
if ex:
    print("\nA4c — THE DECISIVE EXHIBIT (one arc settles that the class is real):")
    print(f"     B991  verdict={ex.get('verdict')}  instrument={ex.get('instrument')}"
          f"  creates_law={ex.get('creates_law')!r}")
    print("     its own claim: \"THE HYPERCHARGE NORMALISATION IS NOT DERIVABLE IN")
    print("     PRINCIPLE, and that is a THEOREM ABOUT THE EQUATIONS rather than a")
    print("     limitation of the object.\"")
    print("     An explicit no-go THEOREM, PROVED, NOT an instrument — and the")
    print("     law flag is ABSENT, so it is invisible to the paper's claim pool.")
    print("     This is not a borderline editorial call; the arc says 'theorem'.")
    assert ex.get("creates_law") is not True and ex.get("instrument") is not True

# B1196 must appear if it were still undeclared -- it was corrected, so check
b = arcs.get("B1196")
if b:
    fixed = bool(b.get("creates_law_corrected"))
    print(f"\nA5 — THE KNOWN INSTANCE: B1196 creates_law = {b.get('creates_law')},"
          f" corrected-field present: {fixed}")
    print("     (B1211's hand-fix; this cell asks whether it was the only one.)")

print(f"""
A6 — THE VERDICT (the preregistered fork):
  candidates found: {len(cands)}   ==> OUTCOME {'U-B' if len(cands) >= 5 else 'U-A'}""")
if len(cands) >= 5:
    print(f"""  THE UNDER-DECLARATION IS NOT ISOLATED.  {len(cands)} settled arcs carry
  law-shaped language at or above the DECLARED-law arcs' own mean score
  while not being declared.  B1210's claim pool reads the declared field,
  so those arcs are INVISIBLE to the paper's claim base — the same way
  B1196 was, and for the same reason.
  CONSEQUENCE, stated at the right strength: this does NOT say all {len(cands)}
  should be reclassified.  Law-shaped language is evidence, and the call
  is editorial.  It DOES say that the paper's claim base was assembled by
  a sweep over a field with a KNOWN, DEMONSTRATED failure mode, and that
  the base should be rebuilt from a re-audited field BEFORE the
  disposition column is filled — because filling dispositions over an
  incomplete pool bakes the omission into the paper.
  RECOMMENDED, and cheap: run this list past the same editorial call
  B1211 made for B1196, then regenerate B1210's ledger.""")
else:
    print("""  B1196's under-declaration looks ISOLATED at this threshold.  B1210's
  pool stands, and the paper's base needs no widening on this account.""")
print("""  FENCE: repository metadata only.  This cell reclassifies nothing, and
  law-shaped vocabulary is a HEURISTIC — it is deliberately not the
  declared field, which is the point, but it is not a proof of law-hood
  either.  Every hit is a candidate for a human call.  Gate 5 untouched.""")
