#!/usr/bin/env python3
"""MEMO-139 CELL (the owner's "do q2"): THE Q2 STALENESS FLAG RE-CHECKED —
and it is SUBSTANTIALLY A FALSE POSITIVE OF THIS BENCH'S OWN DETECTOR.
Memo 138 flagged Q2 STALE on two keyword hits; on inspection the hits name
a DIFFERENT regulator than Q2's subject.  One small genuine residual
survives and is stated at its actual (small) strength.

WHY RE-CHECK MY OWN AUDIT.  Memo 138's staleness detector was
KEYWORD-BASED over arc claims.  That is exactly the instrument shape
B1210 caught itself on — its first pass flagged 229 arcs and was "MOSTLY
NOISE" because claim-scope matching reads every verb as applying to every
reference.  A detector of that shape must be spot-checked on its own
hits before its output is acted on, and Q2 is about to be acted on.

THE TWO OBJECTS, side by side:
  Q2's subject (B1137): regulators as VALUES — the basis
    {L(n,chi_-3) n=1..6, zeta_K(n) n=2..6 [Q(sqrt-3)], L(n,chi_5) n=1..4,
     zeta_F(n) n=2..4 [Q(sqrt5)], pi, sqrt3, sqrt5, log phi, zeta(3)}
    tested for bounded-height algebraic combinations hitting 18 sealed
    SM targets.  Verdict DISJOINT: 0 of 18 targets involve a regulator.
  The flagged hits (B1198/B1209): a regulator MAP — Lee's mixed Tate
    motive over the invariant trace field whose Beilinson regulator EQUALS
    THE COMPLEX VOLUME.  The target there is a GEOMETRIC invariant, not
    an SM quantity.
Same two words; different objects, different targets, different question.

THE FORK (fixed before checking):
  F-A  the hits bear on Q2's question => Q2 is genuinely STALE and needs
       a rewrite like Q1's.
  F-B  the hits are a keyword collision => memo 138's flag on Q2 is a
       FALSE POSITIVE and must be corrected; Q2's ask stands.
Gate 5 untouched: repository metadata only.
"""
import json, glob

import _oa_source as OA          # PINNED source (codex fix)
arcs = OA.arc_verdicts()

def claim(a):
    return (arcs.get(a, {}).get("claim_one_line") or "")

# ---- R1: does either hit mention Q2's actual subject?
Q2_SUBJECT = ["j3(o)", "jordan", "exceptional-domain", "exceptional domain",
              "m(o,c)", "64 fixed", "tier b"]
print("R1 — DO THE FLAGGED ARCS NAME Q2's SUBJECT AT ALL?")
for a in ("B1198", "B1209"):
    c = claim(a).lower()
    hits = [w for w in Q2_SUBJECT if w in c]
    print(f"    {a}: Q2-subject terms present -> {hits if hits else 'NONE'}")
    assert not hits
print("    => NEITHER arc mentions J3(O), the exceptional domain, the")
print("       M(O,C) closing, or Tier B.  They are about a 3-MANIFOLD's")
print("       motive.  ==> OUTCOME F-B: the flag is a KEYWORD COLLISION.")

# ---- R2: was the complex volume actually tested against SM targets?
c1126 = claim("B1126")
covered = ("volume" in c1126.lower())
print("\nR2 — WAS THE COMPLEX VOLUME ALREADY SWEPT AGAINST SM TARGETS?")
print(f"    B1126's sealed period list includes a volume family: {covered}")
print("    B1126: 16 sealed periods (Kashaev ratios + cross-ratios + bare")
print("    rational parts + VOLUME/zeta_K(2) FAMILY) x 22 live-fetched SM")
print("    targets = 352 pairs; 351 below 2 sig figs, consistent with noise.")
assert covered
print("    => YES.  The volume is covered as a DIRECT PERIOD.  So B1209's")
print("       'the complex volume is a Beilinson regulator' does NOT open")
print("       an untested SM route: that route was already swept and is a")
print("       banked negative.")

# ---- R3: the one genuine residual, stated small
# ERROR CAUGHT IN THIS CELL, AND IT IS THE CELL'S OWN SUBJECT: the first
# version of this check tested `"vol" in claim` and returned TRUE — because
# "vol" is a substring of "inVOLves" ("an involves_regulator gate").  A
# substring false positive, inside the very cell written to catch a keyword
# false positive.  Fixed: the basis is extracted and matched on WORDS.
import re as _re
c1137_raw = claim("B1137")
m = _re.search(r"\{(.+?)\}", c1137_raw, _re.S)
basis_txt = (m.group(1) if m else "")
basis_words = set(_re.findall(r"[a-z]+", basis_txt.lower()))
vol_in_basis = bool({"volume", "vol", "cs", "chern"} & basis_words)
print("\nR3 — THE ONE GENUINE RESIDUAL (stated at its actual strength):")
print(f"    B1137's basis, as listed in its own claim: {{{basis_txt.strip()}}}")
print(f"    is the volume (or CS) a member of that basis? "
      f"{'yes' if vol_in_basis else 'NO'}")
assert not vol_in_basis, basis_words
print("    B1126 tested the volume as a DIRECT RATIO against SM targets.")
print("    B1137 tested BOUNDED-HEIGHT ALGEBRAIC COMBINATIONS of a basis")
print("    that does NOT list the volume.  Those are different instruments:")
print("    a direct-ratio null does not cover the combination sweep.")
print("    ==> RESIDUAL, small and nameable: the complex volume is covered")
print("        as a period (B1126) but was NOT a basis element in B1137's")
print("        combination sweep.  B1209 makes it a legitimate candidate")
print("        basis member (it is a Beilinson regulator over the object's")
print("        own field).  Adding it and re-running B1137 is a bounded")
print("        in-house cell — NOT a specialist question, and NOT a hole in")
print("        the negative: it is an untested corner of one instrument.")

print("""
R4 — THE DISPOSITION OF Q2.
  MEMO 138's STALE FLAG ON Q2 IS CORRECTED: substantially a FALSE
  POSITIVE of a keyword detector, of exactly the shape B1210 caught on
  its own first pass.  Q2's ASK STANDS AS WRITTEN — its subject (do
  exceptional-domain regulators reach the 18 sealed SM targets?) is
  untouched by anything banked since the queue was built.
  TWO HONEST ADDITIONS to its status line, both small:
   (i) cite B1209 as ADJACENT-NOT-CONTRADICTING — an outside published
       Beilinson regulator over our own field exists, for a different
       object and a geometric target.  A specialist in this area will
       know that paper; saying we know it too costs nothing and reads
       better than silence.
   (ii) name the B1137 basis corner ourselves, with its size stated: the
       volume is swept as a period (B1126) but is not a basis element in
       the combination sweep.  Naming it pre-empts the obvious referee
       question and costs one clause.
  AN ERROR CAUGHT INSIDE THIS CELL, recorded because it is this cell's own
  subject: R3's first version tested `"vol" in claim` and returned TRUE —
  "vol" being a substring of "inVOLves".  A substring false positive, in
  the cell written to catch a keyword false positive.  Fixed by extracting
  the basis and matching on WORDS.  The lesson is the cell's thesis
  applied to itself: a keyword detector must be spot-checked on its own
  hits, INCLUDING when the detector is mine and the hit confirms what I
  expected.
  MEMO 138's OTHER CALLS ARE UNAFFECTED: Q1's staleness was verified
  case-by-case in that memo (the Lee reading, the base-point closure, the
  CS=0 check), not left to the keyword hits — so the Q1 rewrite stands.
  Q3-Q6 remain READY.
  FENCE: nothing sent, no external contact.  Gate 5 untouched.""")
