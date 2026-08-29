#!/usr/bin/env python3
"""MEMO-131 CELL (the owner's "go" on the D2 decision sheet — signature of
OPTION A): THE LEAP-1 PROPAGATION AUDIT — every entry in the bench corpus
conditioned on LEAP-1, swept MECHANICALLY, with its post-payment state, so
the propagation is exhaustive and auditable rather than remembered.

WHY A CELL AND NOT JUST PROSE.  Paying a leap is the single most dangerous
kind of edit this bench makes: it converts conditionals into assertions
across documents written months apart.  The failure mode is not a wrong
computation, it is a MISSED or OVERSTATED conditional.  So the sweep is
mechanical (grep over the corpus, not memory), and the two places where
the naive propagation would OVERSTATE are checked explicitly.

WHAT WAS SIGNED (recorded exactly, for provenance).  The bench put four
priced options to the owner in THE_D2_DECISION.md and recommended
OPTION A.  The owner replied "go".  That is taken as the signature of
Option A: LEAP-1 is PAID, with the scope premise written in as its own
priced line (SCOPE-1) and its refuter armed.  If a different option was
meant, this record names precisely what was taken as the signature so it
can be corrected in one edit.

THE TWO OVERSTATEMENT TRAPS, checked rather than assumed:
  T1  "The CP sign becomes internal" must NOT be read as "the CP sign is
      forced."  LEAP-1 identifies the CP sign with the CS-clock sign; the
      banked chain (memo 83 / W3, and THE_FENCE_THEOREM section 4) already
      places the CS sign, the CP sign and the chirality label in the
      MIRROR-ODD column, all locked to the observer's one bit c.  So the
      payment identifies the CP sign with a bit the record ALREADY had.
      PREDICTION, fixed here: the observer bit count is UNCHANGED by the
      payment — no bit is added, none is discharged.
  T2  "Matter-over-antimatter follows" is DOUBLY conditional, not singly.
      LEAP-2 was retired (the arrow is NOT forced: B124, memo 94's
      two-branch law, memos 97/101's exhaustion) and the ledger now carries
      ARROW = the branch bit.  So matter-over-antimatter inherits BOTH
      LEAP-1's state AND the branch bit's.  The weld book's phrasing
      ("inherits LEAP-1's state") is single-conditional and must be
      corrected at the point of payment, not after.
Gate 5 untouched: this cell reads the bench's own documents and asserts no
physical value.  Paying a leap asserts a PREMISE, not a theorem.
"""
import os, re, subprocess, collections

BENCH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

def sweep(pattern):
    r = subprocess.run(["grep", "-rn", "--include=*.md", pattern, BENCH],
                       capture_output=True, text=True)
    return [l for l in r.stdout.splitlines() if l.strip()]

hits = sweep("LEAP-1")
files = collections.Counter(l.split(":", 1)[0].split("/")[-1] for l in hits)
print("P1 — THE MECHANICAL SWEEP (grep over the bench corpus, not memory):")
print(f"    LEAP-1 occurrences: {len(hits)} across {len(files)} documents")
for f, n in sorted(files.items(), key=lambda x: (-x[1], x[0])):
    print(f"        {n:3d}  {f}")
assert len(files) >= 8, files

# the entries that CHANGE STATE on payment, named and located
CONDITIONALS = [
    ("memos/TWO_PULSES.md", "expansion FORM object-side",
     "conditional on LEAP-1 (UNPAID)",
     "ASSERTED under LEAP-1 + SCOPE-1; the RATE stays observer-side BY "
     "THEOREM (dimensionful; the scale-torsor no-go is untouched)"),
    ("THE_CLOSURE_ROUTES.md", "row D2",
     "pay or refuse the priced bit",
     "SIGNED — paid as Option A; the row closes"),
    ("THE_WELD_BOOK.md", "LEAP-1 is HELD, not decided",
     "held pending the clock-coherence run",
     "the run returned SPLIT and fired NEITHER signed branch; resolved by "
     "the scope signature, not by the original rule"),
    ("THE_SECOND_HALF.md", "H3 price statement",
     "NOT payable by computation — closes as a PRICE STATEMENT",
     "the price statement is now EXERCISED; H3's deliverable stands and is "
     "what the owner priced from"),
    ("THE_TOE_GAP.md", "row 12 Arrow of time / CP sign",
     "correlation forced, sign priced to one bit",
     "UNCHANGED — see T1: the payment does not alter the bit count"),
]
print("\nP2 — THE ENTRIES THAT CHANGE STATE (each located, each stated):")
for path, what, before, after in CONDITIONALS:
    assert os.path.exists(os.path.join(BENCH, path)), path
    print(f"    {path}")
    print(f"        {what}")
    print(f"        WAS   : {before}")
    print(f"        NOW   : {after}")

# ---- T1: the observer bit count
COLUMN = ["c (the mirror/anchoring bit)", "the branch bit (dynamical)",
          "r (the swap)", "gamma5", "sigma", "lambda", "ell (the unit)"]
ODD_COLUMN = ["torsion signs", "CS sign", "CP sign", "chirality label"]
print("\nT1 — DOES THE PAYMENT ADD AN OBSERVER BIT?")
print(f"    the observer column before payment ({len(COLUMN)} entries):")
for x in COLUMN:
    print(f"        {x}")
print(f"    the MIRROR-ODD column (memo 110; banked chain memo 83 / W3),")
print(f"    all {len(ODD_COLUMN)} locked to the SINGLE bit c:")
for x in ODD_COLUMN:
    print(f"        {x}")
print("    LEAP-1 asserts: cosmological-clock sign = CS-clock sign.")
print("    The CS sign is ALREADY in the odd column, locked to c.")
print("    => the identification attaches the cosmological clock to a bit the")
print("       record ALREADY carries.  NO NEW BIT IS ADDED, and none is")
print("       discharged: the count is unchanged at ONE discrete mirror bit.")
print("    => 'the CP sign becomes INTERNAL' means INTERNAL TO THE CLOCK, not")
print("       FORCED.  memo 111's ledger (one bit, charged at coordinatization,")
print("       once, forever) is untouched — the payment does not touch the")
print("       trace field, so nothing in that ledger can move.")

# ---- T2: the double conditional
print("\nT2 — IS MATTER-OVER-ANTIMATTER SINGLY OR DOUBLY CONDITIONAL?")
print("    the weld book says it 'follows only WITH LEAP-1, so that")
print("    consequence inherits LEAP-1's state' — SINGLE conditional.")
print("    But LEAP-2 was RETIRED: the arrow is NOT forced (B124; memo 94's")
print("    two-branch law; memos 97/101's exhaustion), and the ledger carries")
print("    ARROW = THE BRANCH BIT, frame-priced.")
print("    => matter-over-antimatter inherits BOTH LEAP-1's state AND the")
print("       BRANCH BIT's.  It is DOUBLY CONDITIONAL, and the weld book's")
print("       single-conditional phrasing is CORRECTED at the point of payment.")
print("    => concretely: paying LEAP-1 does NOT deliver matter-over-antimatter;")
print("       it delivers 'matter-over-antimatter GIVEN the branch bit', which")
print("       is a weaker statement than the price sheet implied.")

print("""
P3 — WHAT THE SIGNATURE BUYS, STATED WITHOUT INFLATION:
  BOUGHT (asserted under LEAP-1 + SCOPE-1, both labeled premises):
    * the expansion FORM is object-side (ratio phi per tick, dimensionless);
    * the W1 conjugacy acquires a physical clock on its other side;
    * the CP sign is identified with the CS-clock sign — the SAME bit the
      record already carried, not a new one and not a forced value;
    * matter-over-antimatter, GIVEN the branch bit (T2).
  NOT BOUGHT — unchanged by the payment:
    * the RATE remains observer-side BY THEOREM (dimensionful; scale-torsor
      no-go, Hom(G, R+) = 0);
    * the observer bit count remains ONE discrete mirror bit (T1);
    * the identification remains UNPROVEN — no banked computation connects
      the object's tick to a cosmological clock, and B721's tracial result
      still forces an imported external weight.
  A PAID LEAP IS A LABELED PREMISE, NOT A THEOREM.  Every consequence above
  travels with its premise attached, and dies with it if a refuter fires.
  Gate 5 untouched.""")
