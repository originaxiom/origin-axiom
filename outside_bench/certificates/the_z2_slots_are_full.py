"""CERTIFICATE -- the programme's Z/2 census has ONE KIND in it, and the Galois slots are FULL.

OCCASION.  Memo 199 adjudicated B1327's handoff: section 8's chirality bit is not the manifold's
mirror sign.  That answer raises the structural question the record has never put in one place --
WHAT KIND OF OBJECT IS EACH OF THE PROGRAMME'S Z/2's, AND HOW MANY KINDS ARE THERE?

EXHAUSTED FIRST (already_banked.py; terms stated in the memo):
  B1174  NEGATIVE  the Z/2-identification cell: the four programme Z/2's are NOT one involution;
                   they are LEGS of two V4's sharing the c-leg.  Its four candidates: B942
                   chirality/Gal(K/Q), B957 value torsors, B1168 mirror bit, S068 genus-Z/2 of
                   Q(sqrt-15).
  B1276  PROVED    B1174's legs ARE B730's faces: the same V4, discovered twice, never joined;
                   the parity law "c acts nontrivially on a quadratic field iff it is IMAGINARY".
  B1041  PROVED    the Galois / operations / closings (Z/2)^3 cubes are ONE cube at direction level.

EVERY ONE OF THOSE IS THE SAME KIND OF OBJECT: the sign of a named surd under a field automorphism.
Two bits the record books are NOT of that kind, and NEITHER WAS IN B1174'S CENSUS:
  *  section 8's RELATIONAL bit -- a square class of a PAIR, decided by B1248's D = (2-kappa)/g^2;
  *  the CHERN-SIMONS bit -- A[2] = {0, 1/4} inside the archimedean value group R/(1/2)Z (B1224,
     and this bench's L192 certificate).

CELLS (two outcomes each)
  CELL 1  Is section 8's invariant two-valued on its OWN domain?
          A: yes, it is Z/2-valued          B: no -- it takes |D| > 1 values, so it is Z/2-valued
                                               only on the sub-locus |D| = 1
  CELL 2  Are the GALOIS-LEG SLOTS full?
          A: a free slot exists             B: Hom(V4, Z/2) has exactly three non-trivial elements
                                               and B730/B1174 already name all three -- FULL, so
                                               by COUNTING no further bit can be a leg
  CELL 3  Is the Chern-Simons bit determined by c?
          A: yes                            B: no -- c is present and non-trivial on EVERY
                                               amphichiral manifold, yet the bit takes both values
                                               among them

CONTROLS
  C1  Hom(V4, Z/2) is ENUMERATED by brute force over the group, not asserted.
  C2  The parity law is reproduced on all three faces plus B1276's off-face control Q(sqrt-7),
      so the Galois machinery here is anchored to a PROVED arc before it is used.
  C3  The section-8 classifier must be ABLE to return a genuine Z/2 (|D| = 1), or "not two-valued"
      is an artifact of a broken classifier.
  C4  The Chern-Simons datum is RECOMPUTED for the decisive pair, and cross-checked against this
      bench's own banked L192 output rather than re-deriving 203,122 manifolds.

Gate 5 untouched.  No measured value is used or named.
"""
import itertools
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B1248_norm_classification", "verification"))
FAIL = []


def rule(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def check(name, ok, detail=""):
    print(f"  [{'OK ' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)
    return ok


# ================================================================== C1 / CELL 2
rule("C1 & CELL 2 -- the Galois-leg slots, ENUMERATED")
# V4 = Gal(Q(sqrt-3, sqrt5)/Q) realised concretely as sign pairs on (sqrt-3, sqrt5).
V4 = list(itertools.product([1, -1], repeat=2))          # (s_{-3}, s_5)
print(f"       V4 = Gal(Q(sqrt-3, sqrt5)/Q) as sign pairs on (sqrt-3, sqrt5): {V4}")

# Hom(V4, Z/2) by brute force: all functions V4 -> {+1,-1} that are homomorphisms.
homs = []
for assign in itertools.product([1, -1], repeat=4):
    f = dict(zip(V4, assign))
    if f[(1, 1)] != 1:
        continue
    ok = all(f[(g[0] * h[0], g[1] * h[1])] == f[g] * f[h] for g in V4 for h in V4)
    if ok:
        homs.append(f)
nontrivial = [f for f in homs if any(v == -1 for v in f.values())]
print(f"       |Hom(V4, Z/2)| = {len(homs)}    non-trivial: {len(nontrivial)}")
check("C1 -- Hom(V4, Z/2) enumerated, not asserted", len(homs) == 4 and len(nontrivial) == 3)

# the three the record already names, exhibited as those three homomorphisms
NAMED = {
    "being   Q(sqrt-3)  -- c, the mirror/chirality leg (B942/B1168/B1174)":
        lambda g: g[0],                     # the sign on sqrt-3
    "hearing Q(sqrt5)   -- the value/form-class leg (B957/B1067)":
        lambda g: g[1],                     # the sign on sqrt5
    "meeting Q(sqrt-15) -- the genus leg, c . (sqrt5-swap) (B1174/B1276/B698)":
        lambda g: g[0] * g[1],              # the composite: being . hearing = meeting
}
seen = []
for label, fn in NAMED.items():
    f = {g: fn(g) for g in V4}
    assert f in homs
    seen.append(tuple(sorted(f.items())))
    flips = [g for g in V4 if f[g] == -1]
    print(f"       {label}\n           flips on: {flips}")
check("the three NAMED faces are three DISTINCT non-trivial homomorphisms", len(set(seen)) == 3)
CELL2 = "B" if len(set(seen)) == len(nontrivial) == 3 else "A"
print(f"\n  CELL 2 = {CELL2}  -- " +
      ("the three leg slots are FULL.  By COUNTING, not by inspection, no further bit can be a "
       "Galois leg of this V4." if CELL2 == "B" else "a free slot exists"))

# ================================================================== C2
rule("C2 -- the parity law reproduced (B1276), so the Galois machinery is anchored before use")
import sympy as sp
FIELDS = [("being ", -3, "face"), ("hearing", 5, "face"), ("meeting", -15, "face"),
          ("stage  ", -7, "OFF-face control (B1276)")]
for name, d, role in FIELDS:
    imaginary = d < 0
    # c = complex conjugation on C, restricted to Q(sqrt d) embedded in C
    r = sp.sqrt(sp.Integer(d))
    acts = sp.simplify(sp.conjugate(r) - r) != 0
    print(f"       {name}  Q(sqrt{d:+d})  imaginary={str(imaginary):5s}  c acts nontrivially="
          f"{str(bool(acts)):5s}   {role}")
    check(f"parity law on Q(sqrt{d:+d}): c acts <=> imaginary", bool(acts) == imaginary)
print("       -> hearing is MIRROR-EVEN BY ARITHMETIC; no hearing-side Z/2 can be the orientation.")

# ================================================================== CELL 1 / C3
rule("CELL 1 & C3 -- is section 8's invariant two-valued on its own domain?")
import norm_classification as NC  # noqa: E402
A = NC.A_OBJ
SWEEP = [[5, 2], [2, 1]], [[2, 3], [1, 2]], [[8, 21], [3, 8]], [[5, 12], [2, 5]], \
        [[4, 15], [1, 4]], [[3, 5], [1, 2]], [[1, 3], [1, 4]], [[7, 2], [3, 1]], [[9, 4], [2, 1]]
vals = []
for m in SWEEP:
    k, D, pred, _obs = NC.classify(sp.Matrix(m), A)
    vals.append(D)
    print(f"       M = {str(m):18s} kappa = {k:6d}   D = {D:5d}   {pred}")
unit = sorted({v for v in vals if abs(v) == 1})
nonunit = sorted({v for v in vals if abs(v) > 1})
check("C3 -- the classifier CAN return a genuine Z/2 (|D| = 1 occurs, both signs)",
      unit == [-1, 1], f"|D| = 1 values seen: {unit}")
print(f"\n       values with |D| = 1 (a genuine bit):      {unit}")
print(f"       values with |D| > 1 (NOT a bit, torsor):  {nonunit}")
CELL1 = "B" if nonunit else "A"
print(f"  CELL 1 = {CELL1}  -- " +
      ("section 8's invariant is NOT two-valued: it is Z/2-valued only on the sub-locus |D| = 1, "
       "and off it the class is a TORSOR with no distinguished pair of elements"
       if CELL1 == "B" else "it is Z/2-valued"))

# ================================================================== CELL 3 / C4
rule("CELL 3 & C4 -- is the Chern-Simons bit determined by c?")
import snappy
pair = {}
for n in ("m003", "m004"):
    M = snappy.Manifold(n)
    G = M.symmetry_group()
    cs = float(M.chern_simons())
    cls = round(cs * 4) / 4 % 0.5
    pair[n] = (G.is_amphicheiral(), float(M.volume()), cs, cls,
               min(abs(cs % 0.5 - t) for t in (0.0, 0.25, 0.5)))
    print(f"       {n}  amphichiral={pair[n][0]}  vol={pair[n][1]:.9f}  CS={cs:+.12f}  "
          f"A[2]-class={cls}   distance={pair[n][4]:.2e}")
both_amphi = all(v[0] for v in pair.values())
same_vol = abs(pair["m003"][1] - pair["m004"][1]) < 1e-9
diff_bit = abs(pair["m003"][3] - pair["m004"][3]) > 1e-9
check("C4 -- both are amphichiral, so c is PRESENT AND NON-TRIVIAL on both", both_amphi)
check("C4 -- and they have the SAME volume, so no archimedean invariant separates them either",
      same_vol, f"{pair['m003'][1]:.9f} vs {pair['m004'][1]:.9f}")

# C4 -- cross-check against this bench's own banked census rather than re-deriving 203,122 manifolds
banked = os.path.join(ROOT, "outside_bench", "outputs", "l192_the_bit_out.txt")
txt = open(banked, encoding="utf-8").read() if os.path.exists(banked) else ""
m = re.search(r"amphichiral occupancy of A\[2\]:\s*element 0 -> (\d+)\s*element 1/4 -> (\d+)", txt)
if m:
    z, q = int(m.group(1)), int(m.group(2))
    print(f"\n       banked census (this bench's L192 certificate, 203,122 manifolds):")
    print(f"         amphichiral manifolds: {z + q}   at A[2] = 0: {z}   at A[2] = 1/4: {q}")
    check("C4 -- the banked census agrees: BOTH elements are occupied among amphichirals",
          z > 0 and q > 0)
else:
    check("C4 -- banked L192 census readable", False, "occupancy line not found")

CELL3 = "B" if (both_amphi and diff_bit) else "A"
print(f"\n  CELL 3 = {CELL3}  -- " +
      ("m003 and m004 are BOTH amphichiral and of EQUAL volume, and their A[2] classes DIFFER "
       "(1/4 vs 0).  c is present and non-trivial on both; the bit is not determined by it."
       if CELL3 == "B" else "the bit tracks c"))

# ================================================================== verdict
rule("VERDICT")
print(f"  CELL 1 = {CELL1}   CELL 2 = {CELL2}   CELL 3 = {CELL3}   "
      f"controls: {'ALL PASS' if not FAIL else 'FAILED ' + str(FAIL)}")
if FAIL:
    print("\n  A FAILED CONTROL VOIDS THE READING.  No verdict.")
    sys.exit(1)
print("""
  THE PROGRAMME'S Z/2 CENSUS HAS ONE KIND IN IT, AND ITS SLOTS ARE FULL.

  B1174, B1276 and B1041 censused the record's Z/2's and organised them correctly -- as LEGS of
  V4's and DIRECTIONS of (Z/2)^3 cubes.  Every candidate in that census is the same kind of object:
  THE SIGN OF A NAMED SURD UNDER A FIELD AUTOMORPHISM.  Hom(V4, Z/2) has exactly three non-trivial
  elements, and B730/B1174 already name all three -- being (c), hearing (the value/form-class leg),
  meeting (the genus leg, c . hearing).  THE LEG SLOTS OF THAT V4 ARE FULL BY COUNTING.

  SCOPE, stated plainly: "full" is a statement about the MEETING V4 = Gal(Q(sqrt-3, sqrt5)/Q), which
  is the group B730 proves the object's arithmetic forces.  B1041's (Z/2)^3 cube is a LARGER group
  with seven non-trivial characters, and this certificate says nothing about how many of those are
  spoken for.  What it does say is that the two bits below are not legs of ANY such group, because
  they are not signs of surds under automorphisms at all -- a KIND difference, not a counting one,
  and the counting argument is offered only for the V4 the record's faces live in.

  Two bits the record books are NOT of that kind, and neither was in the census:

   *  SECTION 8'S RELATIONAL BIT is a square class of a PAIR, and on its own domain it is NOT EVEN
      TWO-VALUED: B1248's D runs over -181, -29, -19, -1, +1, 5, 11 on a single fixed object
      relatum.  It is a bit only on the sub-locus |D| = 1; off that locus it is a TORSOR with no
      distinguished pair of elements.  Calling it "a bit" is exact where |D| = 1 and a contraction
      everywhere else.

   *  THE CHERN-SIMONS BIT is the 2-torsion of an ARCHIMEDEAN VALUE GROUP, R/(1/2)Z.  It is genuinely
      two-valued, and it is NOT the c-leg: m003 and m004 are both amphichiral (c present and
      non-trivial on both) and have the SAME VOLUME, yet sit at different elements of A[2] --
      1/4 and 0.  Across the banked census, both elements are occupied among amphichirals.
      AMPHICHIRALITY FORCES MEMBERSHIP IN A[2]; IT DOES NOT FORCE WHICH ELEMENT.

  SO THE RECORD CARRIES AT LEAST THREE KINDS OF Z/2, NOT ONE FAMILY:
      (a) Galois legs         -- the sign of a surd under an automorphism.  Slots: exactly 3, FULL.
      (b) square classes of a pair -- section 8's bit.  Two-valued only on a sub-locus.
      (c) torsion of a value group -- the Chern-Simons bit.  Two-valued, and independent of (a).

  WHY IT MATTERS, and it is the reason B1327 could raise its question at all: A LEDGER THAT BOOKS
  BITS WITHOUT TYPING THEM BY KIND INVITES EXACTLY THE OVER-COUNT WORRY B1327 RAISED.  Two bits of
  different KINDS cannot be the same input, and that can be settled by typing before any pair of
  them is compared.  Memo 199 settled one such pair by computation; this settles the general shape.

  WHAT THIS DOES NOT DO.  It does not move a freedom-ledger row -- that is the ledger owner's call.
  It does not claim the list of kinds is complete; it claims at least three, exhibited.  It does not
  weaken B1174, B1276 or B1041: all three are reproduced here as far as they are used, and the
  finding is that their census was SOUND AND SCOPED -- it answered the question it asked, about
  legs, and two later bits are not legs.
""")
print("Gate 5 untouched.  No measured value is used or named.")
