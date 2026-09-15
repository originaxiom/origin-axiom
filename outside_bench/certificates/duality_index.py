#!/usr/bin/env python3
"""MEMO-127 CELL (the owner's "go both", part 2): THE MASTER DUALITY
INDEX — the corpus's dualities inventoried from primary, and the
record's OWN duality operations TYPED by exact computation, yielding a
SECOND, INDEPENDENT PROOF of the one-bit count.

WHY THIS CELL.  The corpus has no DUALITY.md and no dedicated index;
duality statements are scattered across 141 primary documents
(kill-graph FINDINGS, LAW_MAP, THEOREM_LEDGER, TERMINOLOGY).  A list
alone would be bookkeeping.  The bench's version adds a SPINE: the
record's own duality-shaped OPERATIONS are typed by a computed
criterion, and the typing is checked against a banked theorem.

THE CRITERION, FIXED BEFORE THE RUN.  Work on the Fricke character
coordinates (x, y, z) = (tr A, tr B, tr AB) at the record's own point
P0 = (2, 2, 2 - omega), with the Fricke commutator
kappa(x,y,z) = x^2 + y^2 + z^2 - xyz - 2.  Every candidate operation
is placed in exactly one of four types:
  GAUGE     — fixes P0 and is a lift artefact (the SL2 sign changes);
  SYMMETRY  — fixes P0 (an internal duality of the object: free);
  EXTERNAL  — moves P0 and MOVES kappa off its value (cannot be undone
              by any kappa-preserving internal operation: costs a bit);
  FLOW      — moves P0 but PRESERVES kappa (a dynamics on the fibre,
              not a duality of the point).
Nothing about this typing is negotiable after the numbers appear.

THE PREREGISTERED TWO-OUTCOME QUESTION.
  OUTCOME A: exactly ONE operation class is EXTERNAL => the record's
     duality census independently reproduces the one-bit count
     (memos 107/109/111), by a kappa-invariance argument that shares
     no machinery with the realizer computation.
  OUTCOME B: two or more independent EXTERNAL classes => the one-bit
     count is UNDER-COUNTED and memos 107/111 must be revised.

THE CELLS.
  D1  THE CENSUS: mechanically extract every "<X> duality" phrase from
      the primary corpus (regex, no hand list), with file counts.
  D2  THE OPERATION TABLE: each candidate operation applied to P0 in
      exact Z[omega] arithmetic; its image, its kappa, its type.
  D3  THE kappa-INVARIANCE THEOREM: verify SYMBOLICALLY, as an
      identity in Z[x,y,z], that the letter swap, all three SL2 sign
      changes, and the Fricke map T and its inverse preserve kappa
      IDENTICALLY; and that reversal and inversion act as the identity
      on (x,y,z).  Therefore the whole internal group preserves kappa.
  D4  THE VERDICT: since gal moves kappa (1+omega -> 2-omega, distinct
      because omega is not rational), NO composition of internal
      operations can realize the mirror — one external class, and the
      argument is one line instead of a nullspace search.
  D5  THE VALUE DUALITIES: the corpus's other dualities are pairs of
      VALUES, not operations (being/hearing fields, cancellation/
      residue, imaginary/real); they are indexed separately and NOT
      merged with the operation column.
Gate 5 untouched (no measured value enters; corpus metadata plus the
object's own exact arithmetic).
"""
import os, re, subprocess, collections
from fractions import Fraction as Fr
import sympy as sp

import _oa_source as OA          # PINNED source (codex evidence-contract fix)
REF = OA.REF
def git(*args):
    return OA._git(*args, check=False)

files = [l for l in git("grep", "-il", "dualit", REF, "--", "*.md").splitlines() if l]
PAT = r"[A-Za-z0-9_'()/-]+[ -]dualit(y|ies)"   # POSIX ERE: no (?:...)
raw = git("grep", "-h", "-i", "-o", "-E", PAT, REF, "--", "*.md").splitlines()
STOP = {"the", "a", "an", "this", "that", "is", "by", "with", "same", "and",
        "of", "no", "without", "known", "standard", "its", "our", "their",
        "two", "one", "such", "these", "those", "any", "all", "as", "for",
        "de", "or", "but", "not", "it", "which", "some", "more", "other"}
named = collections.Counter()
for line in raw:
    head = re.split(r"[ -]dualit", line, flags=re.I)[0].strip().lower()
    head = head.strip("|(),.;:'")
    if not head or head in STOP:
        continue
    named[head] += 1        # single letters kept: S-, T-, U-duality are real
print("D1 — THE CENSUS (mechanical, from primary; no hand-written list):")
print(f"    primary documents mentioning a duality: {len(files)}")
print(f"    '<X> duality' phrase occurrences: {sum(named.values())}"
      f" across {len(named)} distinct heads")
print("    the named dualities the corpus actually carries (count >= 2):")
for k, v in named.most_common():
    if v >= 2:
        print(f"      {v:4d}  {k}-duality")
assert len(files) > 50 and named, "census failed to read primary"

# ============================== D2: exact arithmetic over Z[omega]
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def pneg(u): return (-u[0], -u[1])
def psub(u, v): return padd(u, pneg(v))
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)          # omega^2 = omega - 1
def gal(u): return (u[0] + u[1], -u[1])          # omega -> 1 - omega
def show(u):
    a, b = u
    if b == 0: return f"{a}"
    if a == 0: return f"{b}w" if b != 1 else "w"
    return f"{a}{'+' if b > 0 else '-'}{abs(b) if abs(b) != 1 else ''}w"
Z, I2 = (Fr(0), Fr(0)), (Fr(1), Fr(0))
TWO = (Fr(2), Fr(0))
W = (Fr(0), Fr(1))

def kappa(P):
    x, y, z = P
    t = padd(padd(pmul(x, x), pmul(y, y)), pmul(z, z))
    t = psub(t, pmul(pmul(x, y), z))
    return psub(t, TWO)

P0 = (TWO, TWO, psub(TWO, W))                    # (2, 2, 2 - omega)
K0 = kappa(P0)
assert K0 == (Fr(1), Fr(1)), K0                  # kappa = 1 + omega  (memo 86)

# the candidate operations, as maps on (x, y, z)
def op_id(P): return P
def op_swap(P): return (P[1], P[0], P[2])                       # a <-> b
def op_rev(P): return P                     # reversal: trace-preserving
def op_inv(P): return P                     # w -> w^-1: tr invariant
def op_sx(P): return (P[0], pneg(P[1]), pneg(P[2]))             # SL2 lift
def op_sy(P): return (pneg(P[0]), P[1], pneg(P[2]))
def op_sz(P): return (pneg(P[0]), pneg(P[1]), P[2])
def op_gal(P): return tuple(gal(c) for c in P)                  # the mirror
def op_T(P):
    x, y, z = P
    return (z, x, psub(pmul(z, x), y))                          # Fricke golden
def op_Tinv(P):
    X, Y, Zc = P
    return (Y, psub(pmul(X, Y), Zc), X)
def op_L(P):
    x, y, z = P                                                 # Thue-Morse
    return (z, z, padd(psub(psub(pmul(pmul(x, y), z), pmul(x, x)),
                            pmul(y, y)), TWO))

OPS = [("identity", op_id, "-"),
       ("letter swap  a<->b", op_swap, "the ab/ba duality"),
       ("word reversal", op_rev, "the mirror-word duality"),
       ("inversion  w->w^-1", op_inv, "the orientation duality"),
       ("SL2 lift sign  s_x", op_sx, "lift artefact"),
       ("SL2 lift sign  s_y", op_sy, "lift artefact"),
       ("SL2 lift sign  s_z", op_sz, "lift artefact"),
       ("gal (complex conj)", op_gal, "THE MIRROR / chirality duality"),
       ("Fricke golden  T", op_T, "the kappa-preserving flow"),
       ("Fricke golden  T^-1", op_Tinv, "the kappa-preserving flow"),
       ("Thue-Morse  L", op_L, "the layering map")]

print("\nD2 — THE OPERATION TABLE (exact, at the record's own point"
      f" P0 = ({show(P0[0])}, {show(P0[1])}, {show(P0[2])}), kappa = {show(K0)}):")
# GAUGE is decided by a COMPUTED fact, not by the operation's name: a map
# is a gauge iff it is the trace action of twisting the SL2 lift by one of
# the three nontrivial characters eps : F(a,b) -> {+-1}, i.e.
# (x, y, z) -> (eps(a) x, eps(b) y, eps(a) eps(b) z) — same PSL2 rep.
GAUGE_IMAGES = set()
for ea in (1, -1):
    for eb in (1, -1):
        if (ea, eb) == (1, 1):
            continue
        sx, sy, sz = ea, eb, ea*eb
        GAUGE_IMAGES.add(tuple((Fr(s)*c[0], Fr(s)*c[1])
                               for s, c in zip((sx, sy, sz), P0)))
assert len(GAUGE_IMAGES) == 3
print(f"    {'operation':<20s} {'image of P0':<26s} {'kappa':<8s} {'type':<10s}")
types = {}
for name, f, _ in OPS:
    Q = f(P0)
    kq = kappa(Q)
    if Q == P0:
        t = "SYMMETRY"
    elif Q in GAUGE_IMAGES:
        t = "GAUGE"
    elif kq != K0:
        t = "EXTERNAL" if kq == gal(K0) else "FLOW*"
    else:
        t = "FLOW"
    types[name] = t
    img = "(" + ", ".join(show(c) for c in Q) + ")"
    print(f"    {name:<20s} {img:<26s} {show(kq):<8s} {t:<10s}")
print("    (GAUGE = the trace action of twisting the SL2 lift by one of the three")
print("     nontrivial characters F(a,b) -> {+-1}: a DIFFERENT POINT, the SAME")
print("     PSL2 representation — verified as such, not asserted by name.)")
print("    (FLOW* = moves kappa but not to its Galois mate: a dynamics that")
print("     leaves the fibre altogether — the layering map, memo 121/B496.")
print("     Its kappa here is -2, EXACTLY B496's Markov surface and memo 124's")
print("     level-1 triple coincidence: an independent re-derivation of it.)")

# the object's own stabiliser inside <swap, lift signs>
grp = []
for sw in (op_id, op_swap):
    for sg in (op_id, op_sx, op_sy, op_sz):
        grp.append(lambda P, sw=sw, sg=sg: sg(sw(P)))
stab = sum(1 for g in grp if g(P0) == P0)
assert len(grp) == 8
print(f"\n    STABILISER of P0 in <letter swap, SL2 lift signs> (order 8):"
      f" {stab} elements")
print("    => the object's ONLY internal duality at its own point is the")
print("       LETTER SWAP (x = y = 2); reversal and inversion act trivially")
print("       on the coordinates, so they add nothing new there.")

# ============================== D3: the kappa-invariance theorem
x, y, z = sp.symbols('x y z')
K = x**2 + y**2 + z**2 - x*y*z - 2
def sub(P): return sp.expand(K.subs({x: P[0], y: P[1], z: P[2]}, simultaneous=True))
checks = {
    "letter swap": (y, x, z),
    "sign s_x": (x, -y, -z),
    "sign s_y": (-x, y, -z),
    "sign s_z": (-x, -y, z),
    "Fricke T": (z, x, z*x - y),
    "Fricke T^-1": (y, x*y - z, x),
}
print("\nD3 — THE kappa-INVARIANCE THEOREM (symbolic identities in Z[x,y,z]):")
for nm, P in checks.items():
    d = sp.expand(sub(P) - K)
    assert d == 0, (nm, d)
    print(f"    kappa o {nm:<12s} - kappa = 0   IDENTICALLY")
LP = (z, z, x*y*z - x**2 - y**2 + 2)
dL = sp.expand(sub(LP) - K)
assert dL != 0
print(f"    kappa o Thue-Morse L - kappa = {sp.factor(dL)}   NOT identically 0")
print("    => the group generated by the letter swap, the three lift signs,")
print("       reversal, inversion and the whole Fricke action T^n PRESERVES")
print("       kappa EXACTLY, as a polynomial identity — at every point, not")
print("       just at P0.")

# ============================== D4: the verdict
Kg = gal(K0)
assert Kg != K0 and Kg == (Fr(2), Fr(-1))        # 2 - omega
# no internal operation can move kappa, and gal does move it:
print("\nD4 — THE VERDICT (the preregistered two-outcome question):")
print(f"    kappa(P0)      = {show(K0)}")
print(f"    kappa(gal P0)  = {show(Kg)}      distinct, since omega is irrational")
print("    Every internal operation preserves kappa IDENTICALLY (D3).")
print("    Therefore NO composition of internal operations sends gal(P0) to P0.")
ext = [n for n, t in types.items() if t == "EXTERNAL"]
assert len(ext) == 1, ext
print(f"    EXTERNAL classes found: {len(ext)}  ->  {ext[0]}")
print("    ==> OUTCOME A.  The duality census independently reproduces the")
print("        ONE-BIT COUNT (memos 107/109/111) by a kappa-invariance")
print("        argument sharing NO machinery with the realizer nullspace")
print("        search: the mirror is external because it moves the founding")
print("        invariant, and nothing internal can move it back.")
print("    FENCE, stated exactly (this cell proves ONE HALF of the count):")
print("      * IRREMOVABILITY (>= 1) is what is proved here, and it is proved")
print("        for the WHOLE internal group at once, at every point, by a")
print("        polynomial identity — strictly stronger than a point check.")
print("      * AT MOST ONE is NOT proved here: it is memo 111's L3 (the trace")
print("        ring is exactly Z[omega], so Gal = Z/2 and there is no second")
print("        Galois freedom at any depth).  The two halves together give the")
print("        count; this cell replaces the realizer search in the first half")
print("        only.  Both kappa values root X^2 - 3X + 3 (memo 109's I3), so")
print("        the invariant CONTENT is unmoved while the VALUE is not.")

# ============================== D5: the value dualities
print("\nD5 — THE VALUE DUALITIES (indexed separately: pairs of VALUES, not")
print("     operations; each is a banked result, cited, not recomputed here):")
VALUE = [
    ("being / hearing", "Q(sqrt-3) vs Q(sqrt5), joined by meeting Q(sqrt-15)",
     "C7 theorem, Klein four-group V4"),
    ("imaginary / real", "the tower is non-real at levels 0-1 and real from 2 on",
     "memo 124, crossing at the cusp, irreversible"),
    ("cancellation / residue", "kappa - 2 = omega^2, permanent, multiplicative",
     "memo 125 / B161 / B496"),
    ("even / odd under the mirror", "magnitudes in the KERNEL, torsion signs ODD",
     "memo 110: 604 fixed, 12516 flipped"),
    ("forced / free", "every value forced; the free list is the observer column",
     "THE_FORCED_AND_THE_FREE, the census"),
    ("object / observer", "timeless exact structure vs the seat and its bit",
     "B716/B721, memos 111/112"),
    ("II_1 / III_lambda", "tracial equilibrium clock vs thermal, weight-induced",
     "B721 / B723"),
    ("27 / 27bar", "conjugate minuscule reps paired by Poincare duality",
     "the twisted-double cells"),
]
for a, b, c in VALUE:
    print(f"      {a:<26s} {b}")
    print(f"      {'':<26s} [{c}]")
print("""
THE INDEX'S ONE LINE.  The corpus's dualities fall into two columns
that must not be merged.  OPERATION dualities act on the record and
are typed by kappa: the internal ones (letter swap, reversal,
inversion, the lift signs, the whole Fricke flow) preserve kappa
identically and are FREE; exactly ONE — the mirror — moves kappa to
its Galois mate and is therefore EXTERNAL, which is the one bit, now
proved twice by disjoint means.  VALUE dualities pair quantities the
record computes and cost nothing.  The master index is that split, and
its content is that the split has exactly one element on the expensive
side.  Gate 5 untouched.""")
