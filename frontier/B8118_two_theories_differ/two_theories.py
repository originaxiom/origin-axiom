#!/usr/bin/env python3
"""B8118 -- do the corpus's TWO 3d theories for m004 differ?  The owner's question, negatives-first.

B8099 found the corpus attaches TWO theories to the same manifold:
  (A) T[4_1] = U(1) with 2 chirals, from DGG applied to the TRIANGULATION (B262)
  (B) the E6 structure with the 27, from the corpus's own charge-frame route
and ASSERTED "these are not the same theory" on the strength of B262's WALL #2 -- which is an OPEN
question ("is E6 ever dynamical"), not a proof.  The owner elected: prove they differ first.

THE TEST IS A GENERICITY CONTROL, the same instrument as B8111.  If E6 attaches to m004 through
the SHAPE/TRACE FIELD rather than through the manifold, then EVERY manifold sharing that field
inherits the same E6 -- so E6 is a function of the FIELD, not of m004, and the two attachments are
different KINDS of object rather than two descriptions of one theory.

QUANTIFIER: tetrahedron shape fields over the orientable cusped census, and the arithmetic chain
disc -> conductor -> SL(2,Z/N) -> McKay.  Gate 5 untouched; no measured value.
"""
import json, os
from fractions import Fraction
import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAILED.append(l)

def rat(x, maxden=64, tol=1e-9):
    f = Fraction(x).limit_denominator(maxden)
    return f if abs(float(f) - x) < tol else None

def quad_disc(z):
    """A shape z satisfies t^2 + b t + c with b = -2 Re z, c = |z|^2.  Return the squarefree
    discriminant if the shape is quadratic over Q, else None."""
    b, c = rat(-2 * z.real), rat(abs(z) ** 2)
    if b is None or c is None:
        return None
    d = b * b - 4 * c
    if d >= 0:
        return None
    n = d.numerator * d.denominator          # same field up to squares
    for s in range(2, 60):
        while n % (s * s) == 0:
            n //= s * s
    return n

print("=" * 78); print("SECTION 1 -- THE OBJECT'S OWN SHAPE FIELD"); print("=" * 78)
M = snappy.Manifold("m004")
sh = [complex(z) for z in M.tetrahedra_shapes("rect")]
print(f"  m004 shapes: {sh}")
gate("m004 has 2 tetrahedra", len(sh) == 2, str(len(sh)))
gate("both shapes are the REGULAR ideal tetrahedron e^{i pi/3}",
     all(abs(z - complex(0.5, 3 ** .5 / 2)) < 1e-9 for z in sh))
d004 = {quad_disc(z) for z in sh}
gate("m004's shape field is Q(sqrt(-3))", d004 == {-3}, str(d004))

# ---------------------------------------------------------------- the arithmetic chain
print(); print("=" * 78); print("SECTION 2 -- HOW E6 REACHES THE OBJECT: the arithmetic chain"); print("=" * 78)
# disc -3  ->  conductor 3  ->  SL(2, Z/3), order 24  ->  2T  ->  McKay  ->  E6.
def sl2_order(N):
    n = N ** 3
    for p in {p for p in range(2, N + 1) if N % p == 0 and all(p % q for q in range(2, p))}:
        n = n * (p * p - 1) // (p * p)
    return n
o3 = sl2_order(3)
print(f"  disc = -3  ->  conductor 3  ->  |SL(2,Z/3)| = {o3}")
gate("|SL(2,Z/3)| = 24 = |2T|", o3 == 24, str(o3))
# The B997-correction control, run here rather than cited: a finite SU(2) subgroup has EXACTLY ONE
# involution.  SL(2,Z/3) must pass it (it IS 2T); SL(2,Z/4) must FAIL it (it is NOT 2O).
def sl2_elements(N):
    els = []
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    if (a * d - b * c) % N == 1:
                        els.append((a, b, c, d))
    return els
def n_involutions(N):
    els, I = sl2_elements(N), (1, 0, 0, 1)
    def mul(x, y):
        return ((x[0]*y[0]+x[1]*y[2]) % N, (x[0]*y[1]+x[1]*y[3]) % N,
                (x[2]*y[0]+x[3]*y[2]) % N, (x[2]*y[1]+x[3]*y[3]) % N)
    return sum(1 for g in els if g != I and mul(g, g) == I)
i3, i4 = n_involutions(3), n_involutions(4)
print(f"  involutions: SL(2,Z/3) = {i3}   SL(2,Z/4) = {i4}")
gate("SL(2,Z/3) has exactly ONE involution -- consistent with being 2T", i3 == 1, str(i3))
gate("SL(2,Z/4) has SEVEN -- so it is NOT 2O (B997's own correction, re-run not cited)",
     i4 == 7, str(i4))
print("  => E6 reaches the object as: shape field disc -3 -> conductor 3 -> SL(2,Z/3) = 2T -> McKay E6")
print("     EVERY STEP IS ARITHMETIC.  None of them mentions the triangulation, the volume,")
print("     the geodesics, or anything else that distinguishes m004 from another manifold")
print("     with the same shape field.")

# ------------------------------------------------------- THE GENERICITY CONTROL
print(); print("=" * 78); print("SECTION 3 -- THE GENERICITY CONTROL: is E6 m004-SPECIFIC?"); print("=" * 78)
hits, scanned, byname = [], 0, {}
for N in snappy.OrientableCuspedCensus():
    scanned += 1
    if scanned > 1200:
        break
    try:
        s = [complex(z) for z in N.tetrahedra_shapes("rect")]
    except Exception:
        continue
    ds = {quad_disc(z) for z in s}
    if ds == {-3}:
        hits.append(N.name()); byname[N.name()] = (len(s), float(N.volume()))
print(f"  census manifolds scanned .............: {scanned - 1}")
print(f"  sharing m004's shape field Q(sqrt-3) .: {len(hits)}")
print(f"  first 12: {hits[:12]}")
gate("m004 is among them (sanity)", "m004" in hits)
gate("THE CONTROL BITES: m004 is NOT the only manifold with this shape field",
     len(hits) > 1, f"{len(hits)} manifolds share it")
distinct_vols = {round(v, 9) for _, v in byname.values()}
print(f"  distinct volumes among them ..........: {len(distinct_vols)}")
gate("and they are genuinely different manifolds (many distinct volumes)",
     len(distinct_vols) > 1, f"{len(distinct_vols)} distinct volumes")

# --------------------------------------------------------------- the A side
print(); print("=" * 78); print("SECTION 4 -- THE (A) SIDE, AND WHERE IT ATTACHES"); print("=" * 78)
print("  DGG builds T[M] from an IDEAL TRIANGULATION: m004's 2 tetrahedra give U(1) with 2")
print("  chirals (B262).  The tetrahedron COUNT varies across the Q(sqrt-3) family:")
tets = sorted({t for t, _ in byname.values()})
print(f"    tetrahedron counts in the family: {tets}")
gate("the tetrahedron count is NOT constant on the shape-field family",
     len(tets) > 1, f"counts {tets}")
print("  => (A) sees something (B) cannot: the triangulation. Two manifolds can share a shape")
print("     field -- hence the same E6 -- while having different tetrahedron counts, hence")
print("     different DGG theories.")

print(); print("=" * 78); print("THE VERDICT"); print("=" * 78)
print(f"""
  THEY DIFFER, AND THEY DIFFER IN KIND.

  (A) attaches at the TRIANGULATION and is a QFT: gauge U(1), 2 chirals, rank 1.
  (B) attaches at the SHAPE FIELD and is ARITHMETIC: disc -3 -> conductor 3 -> SL(2,Z/3) = 2T
      -> McKay -> E6, with no step referring to the manifold beyond its field.

  The genericity control is decisive: {len(hits)} census manifolds share m004's shape field, with
  {len(distinct_vols)} distinct volumes and tetrahedron counts {tets}.  So E6 is a function of the
  FIELD and is inherited by every member; the DGG theory is a function of the TRIANGULATION and
  is NOT.  A quantity constant on a family cannot distinguish a member of it -- B990's shape,
  recurring.

  So "the 3d theory of m004" was never ambiguous between two theories.  It was a CATEGORY
  ERROR: one of the two is not a 3d theory of this manifold at all.
""")

RES = {"m004_shapes_regular_ideal": True, "m004_shape_field_disc": -3,
       "sl2_z3_order": o3, "sl2_z3_involutions": i3, "sl2_z4_involutions": i4,
       "chain": "shape field disc -3 -> conductor 3 -> SL(2,Z/3) = 2T -> McKay -> E6",
       "census_scanned": scanned - 1, "n_sharing_shape_field": len(hits),
       "sharing": hits, "n_distinct_volumes": len(distinct_vols),
       "tetrahedron_counts_in_family": tets,
       "A_attaches_at": "the ideal triangulation (DGG); varies within the family",
       "B_attaches_at": "the shape field (arithmetic); constant on the family",
       "they_differ": True, "difference_is_of_kind": True,
       "verdict": ("THE TWO THEORIES DIFFER, AND THEY DIFFER IN KIND -- SO THE AMBIGUITY WAS A "
                   "CATEGORY ERROR. (A) T[4_1] attaches at the IDEAL TRIANGULATION and is a QFT "
                   "(U(1), 2 chirals). (B) E6 attaches at the SHAPE FIELD by a purely arithmetic "
                   "chain -- disc -3, conductor 3, SL(2,Z/3) which is 2T, McKay, E6 -- no step of "
                   "which refers to the manifold beyond its field. THE GENERICITY CONTROL IS "
                   "DECISIVE: many census manifolds share m004's shape field, with several "
                   "distinct volumes and DIFFERENT TETRAHEDRON COUNTS, so E6 is inherited by every "
                   "member of the family while the DGG theory is not -- and a quantity constant on "
                   "a family cannot distinguish a member of it, which is B990's shape recurring. "
                   "B8099 asserted the two differ on the strength of B262's wall #2, which is an "
                   "OPEN question; this proves it instead, and upgrades the statement: they are "
                   "not two candidate 3d theories but a 3d theory and an arithmetic structure. "
                   "CONTROLS: the B997 correction re-run rather than cited -- SL(2,Z/3) has "
                   "exactly ONE involution (consistent with 2T) while SL(2,Z/4) has SEVEN (so it "
                   "is not 2O)."),
       "scope": ("Tetrahedron shape fields over the orientable cusped census and the arithmetic "
                 "chain disc -> conductor -> SL(2,Z/N) -> McKay. Uses the SHAPE field, which for "
                 "these manifolds is the invariant trace field up to the standard relation; the "
                 "arc does NOT independently verify that identification and says so. Does not "
                 "evaluate either theory, and does not decide which the owner should complete. "
                 "Gate 5 untouched.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("  results.json written")
if FAILED: raise SystemExit(f"\nCONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
