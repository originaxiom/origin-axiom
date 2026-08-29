#!/usr/bin/env python3
"""MEMO-136 CELL (the owner's "run go" on the cheapest item): THE
CONTACT-QUANTITY KIND-ROW ADJUDICATION — one of the four pre-work items
I3 owes, and the one the record has been explicitly asking someone to
state.  Answer: the mirror row's kind-admissible pairing is 5/8 ALREADY
SPENT, its independent content is EXACTLY THREE VALUES, and the mechanism
is a 2T half-scaling.  No contact is made; this is typing, not a shot.

WHAT THE RECORD ASKED FOR, verbatim (the license agent's forward-looking
note on the crossing spec): "the mirror set (B1011 C6, theta-even) was
never itself numerically fitted to SM data, only the TONE SUBSET was
(B1066 R-B); B1066's own verdict language books SPENT status at the KIND
level ('both remaining kind-rows consumed'), NOT the row level, so a
future arc using Lambda's output on the mirror sector SHOULD STATE
EXPLICITLY WHICH READING IT RELIES ON before treating that pairing as
licensed."  This cell states it.

THE TWO BANKED SETS:
  tones  (B1011 C5, theta-odd, FIVE)  : {0, +-1/(2phi), +-1/2, +-phi/2, +-1}
  mirror (B1011 C6, theta-even, EIGHT):
      {0, +-1/4, +-1/(4phi), +-1/2, +-1/(2phi), +-phi/4, +-phi/2, +-1}
  B1032's TYPE LAW banks the mechanism: "the mirror set IS the tensor
  character menu |chi_{V2(2T)}/2| * |chi_{V2(2I)}/2| = B1011 C6's eight
  magnitudes exactly (tone(5) != mirror(8), two distinct banked sets)".

THE PREREGISTERED FORK (fixed before any set is built):
  K-A  the mirror magnitudes are DISJOINT from the tone magnitudes =>
       the mirror row is fully independent territory and its one-shot is
       worth its full price.
  K-B  the mirror magnitudes CONTAIN the tone magnitudes => a
       modulus-kind mirror pairing RE-POSES an already-spent comparison
       on that part of its menu, and the row's independent content is
       only the complement, which must be counted exactly.
Gate 5 untouched: exact character arithmetic and set containment.  NO
measured value is touched and NO contact row is drawn on.
"""
import itertools
from fractions import Fraction as F
import sympy as sp

phi = (1 + sp.sqrt(5))/2

# ---- K1: the two banked sets, written down
TONES = sorted({sp.Integer(0), 1/(2*phi), sp.Rational(1,2), phi/2, sp.Integer(1)},
               key=lambda e: float(e))
MIRROR = sorted({sp.Integer(0), sp.Rational(1,4), 1/(4*phi), sp.Rational(1,2),
                 1/(2*phi), phi/4, phi/2, sp.Integer(1)}, key=lambda e: float(e))
print("K1 — THE TWO BANKED MAGNITUDE SETS (B1011 C5 / C6):")
print(f"    tones  ({len(TONES)}): " + ", ".join(sp.nsimplify(t).__str__() for t in TONES))
print(f"    mirror ({len(MIRROR)}): " + ", ".join(sp.nsimplify(m).__str__() for m in MIRROR))
assert len(TONES) == 5 and len(MIRROR) == 8

# ---- K2: the 2T factor, computed from character theory (not cited)
# 2T = binary tetrahedral, order 24; its faithful 2-dim rep V2 has character
# values 2, -2, 0 (order 4), and +-1 on the order-3/order-6 classes.
CHI_2T = [sp.Integer(2), sp.Integer(-2), sp.Integer(0),
          sp.Integer(1), sp.Integer(-1), sp.Integer(1), sp.Integer(-1)]
half_2T = sorted({abs(c)/2 for c in CHI_2T}, key=lambda e: float(e))
print("\nK2 — THE 2T FACTOR, from its 2-dimensional character:")
print(f"    chi_{{V2(2T)}} class values : {[str(c) for c in CHI_2T]}")
print(f"    |chi/2| menu ({len(half_2T)}): {[str(h) for h in half_2T]}")
assert half_2T == [sp.Integer(0), sp.Rational(1,2), sp.Integer(1)]

# ---- K3: the tensor menu REBUILT, and checked against B1011 C6
prod = set()
for a in half_2T:
    for b in TONES:
        prod.add(sp.nsimplify(sp.simplify(a*b)))
prod = sorted(prod, key=lambda e: float(e))
print("\nK3 — THE TENSOR MENU REBUILT (B1032's mechanism, verified not cited):")
print(f"    |chi_2T/2| x |chi_2I/2| -> {len(prod)} distinct magnitudes:")
print("      " + ", ".join(str(p) for p in prod))
same = (len(prod) == len(MIRROR) and
        all(sp.simplify(a-b) == 0 for a, b in zip(prod, MIRROR)))
print(f"    equals B1011 C6's banked eight: {same}")
assert same
print("    => B1032's tensor claim REPRODUCES EXACTLY on this bench.")

# ---- K4: THE CONTAINMENT — the fork's decision
contained = [t for t in TONES if any(sp.simplify(t-m) == 0 for m in MIRROR)]
extra = [m for m in MIRROR if not any(sp.simplify(m-t) == 0 for t in TONES)]
print("\nK4 — THE CONTAINMENT (the preregistered fork):")
print(f"    tone magnitudes ALSO in the mirror set : {len(contained)} of {len(TONES)}")
print("      " + ", ".join(str(t) for t in contained))
print(f"    mirror magnitudes NOT in the tone set  : {len(extra)} of {len(MIRROR)}")
print("      " + ", ".join(str(e) for e in extra))
assert len(contained) == 5 and len(extra) == 3
halves = [sp.nsimplify(sp.simplify(t/2)) for t in TONES if t != 0]
is_halves = all(any(sp.simplify(e-h) == 0 for h in halves) for e in extra)
print(f"    and the 3 extras are exactly TONE MAGNITUDES HALVED: {is_halves}")
assert is_halves
print("    (mechanism, from K2: the 2T factor contributes exactly {0, 1/2, 1},")
print("     so the mirror menu IS the tone menu UNION its own half.)")

print("""
K5 — THE ADJUDICATION: OUTCOME K-B.
  THE KIND.  The mirror set is typed AMPLITUDE-PART (signed, [-1,1],
  Q(sqrt5), coupling channel).  The KIND_TABLE's admissible-pairs
  corollary sends the coupling channel to mixing/moduli/phases, and the
  SM row for CKM/PMNS moduli |V_ij| names its admissible partner as
  |tone|-TYPE — a MODULUS.  So a kind-admissible mirror pairing must take
  ABSOLUTE VALUES, which DISCARDS THE SIGN — and the sign is exactly what
  makes the row the MIRROR row.  First finding: the only kind-admissible
  pairing throws away the row's distinguishing structure.
  THE OVERLAP.  On magnitudes, FIVE of the mirror row's EIGHT values ARE
  the tone values, and the tones row is CONSUMED — B1066 R-B (MISS,
  decisive), with its kind-correct moduli pairing already sealed as B1075.
  So a modulus-kind mirror contact RE-POSES an already-spent comparison
  across 5/8 of its menu.
  THE ROW'S INDEPENDENT CONTENT IS EXACTLY THREE VALUES:
  {1/4, phi/4, 1/(4phi)} — the tone menu halved by the 2T factor.
  ANSWERING THE LICENSE AGENT'S QUESTION DIRECTLY (which reading?):
  the KIND-level reading and the ROW-level reading DISAGREE here, and the
  disagreement is now quantified rather than left open:
    * ROW-level: the mirror row is UNCONSUMED, so its one shot is fully
      available.  TRUE as bookkeeping.
    * KIND-level: 5/8 of what that shot would compare is already spent on
      a decisive MISS.  ALSO TRUE, and it is the one that bears on
      whether the shot is worth taking.
  The honest statement is BOTH, with the 5/8 quoted — not a choice
  between them.

K6 — THE CONSUMPTION-RULE CORRECTION (against THIS BENCH's memo 135):
  Memo 135 leaned on I3's word "IRREVERSIBLE" and called firing it
  "spending an irreversible resource".  THE LEDGER'S OWN GOVERNING NOTE IS
  WEAKER, and it is the owner's own catch (2026-08-19): "the consumption
  ledger books CONTACT PAIRINGS UNDER SEALS, NOT ROWS-FOREVER" — with the
  worked precedent that the tones row, though marked CONSUMED, had its
  kind-correct moduli pairing seal afterwards as B1075 "with the
  second-shot status priced".
  SO: firing the mirror row would spend THAT PAIRING, not the row forever;
  a kind-correct different pairing would remain available as a new arc
  under a new seal at second-shot price.  MEMO 135's VERDICT IS UNCHANGED
  (the shot is still not fireable — u is unpinned), but ITS STATEMENT OF
  THE STAKES WAS TOO STRONG and is corrected here at the point of
  discovery.  The cost of a bad shot is a spent pairing plus second-shot
  pricing on any re-pose — real, but not total.
  FENCE: no contact row is drawn on by this cell, no measured value is
  touched, and the ledger is unchanged.  Typing only.  Gate 5 untouched.""")
