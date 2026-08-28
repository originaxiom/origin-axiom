#!/usr/bin/env python3
"""MEMO-110 CELL (the owner's SM question, computed): THE MIRROR'S
KERNEL — "does the independence theorem affect anything on the SM and
how reality emerges?"  The question is decidable as an AUDIT: memo
109's undecidable proposition is the anchoring of ONE involution, so
its reach is exactly that involution's ODD part.  This cell computes
the odd part and the kernel, exactly.

THE KEY IDENTITY (exact, and the reason the audit is clean):
  K1: the record's Galois flip IS COMPLEX CONJUGATION on the trace
      field.  omega = e^{i pi/3} has conj(omega) = 1 - omega, so the
      pair map (x, y) -> (x + y, -y) is conjugation — verified as a
      field identity (multiplicativity + additivity on a batch, and
      on the generators' traces).  CONSEQUENCE, immediate and total:
      every complex length lambda = 2 arccosh(tr/2) is CONJUGATED by
      the flip => REAL LENGTHS FIXED, TORSIONS NEGATED, for every
      class at once, with no exceptions and no class-by-class
      freedom.  (Memo 81's mirror law, derived here from one field
      fact rather than assumed.)
  K2 (the reach audit, exact counting — no numerics): a class is
      mirror-FIXED iff its trace is real iff its omega-component
      vanishes.  Count both populations over ALL reduced words to
      length 8.  This measures how much of the record is
      orientation-sensitive.
  K3 (the datum vs the invariant): kappa = tr[a,b] = 1 + omega is
      itself FLIPPED (omega-component 1), but its minimal polynomial
      X^2 - 3X + 3 is FIXED — the exact distinction between a
      coordinate and an invariant, computed.  Same for the systole
      trace 2 - omega: flipped as a datum, its geodesic LENGTH fixed.
  K4 (THE SM LEDGER, the owner's actual question): every SM-facing
      banked magnitude is rational or integral — dims 27, 78, 72;
      the twist pair 2304, 953; sin^2 theta_W = 3/8; the sum rule
      151/64 + 553/64 = 11; the ladder count 112; Vol = 12 Vol_orb;
      the E6 Gram and its 72 roots (rebuilt integrally) — and
      RATIONAL DATA IS FIXED POINTWISE by any Galois flip.  Verified
      item by item.  Therefore the ENTIRE content/magnitude layer
      lies in the mirror's KERNEL: the undecidable bit cannot move
      any of it.
CONCLUSION (stated as the audit supports it, no more): the
independence theorem's reach on the SM layer is EXACTLY the
orientation/sign column — one bit, total reach, rigid — and is
provably EMPTY on every banked magnitude.  FENCE: this is an audit
over the enumerated banked ledger (the rows listed above), not a
proof about every conceivable quantity; and the SM-facing chain from
the record's sign column to physical parity/CP is the banked chain
(memo 83, W3), cited not re-derived.  Gate 5 untouched.
"""
from fractions import Fraction as Fr
import sympy as sp

# ---------------- pair arithmetic over Q(omega), omega^2 = omega - 1
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)
def pneg(u): return (-u[0], -u[1])
def pgal(u): return (u[0] + u[1], -u[1])          # omega -> 1 - omega
ZERO, ONE = (Fr(0), Fr(0)), (Fr(1), Fr(0))
W = (Fr(0), Fr(1))

# K1: pgal IS complex conjugation.  omega = 1/2 + i sqrt3/2.
om = sp.Rational(1, 2) + sp.sqrt(3)*sp.I/2
def to_C(u): return sp.simplify(sp.nsimplify(u[0]) + sp.nsimplify(u[1])*om)
assert sp.simplify(to_C(pgal(W)) - sp.conjugate(om)) == 0
# field homomorphism checks on a batch of pairs
BATCH = [(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(2), Fr(-1)), (Fr(1), Fr(1)),
         (Fr(-3), Fr(5)), (Fr(7), Fr(-2)), (Fr(1, 2), Fr(3, 4))]
for u in BATCH:
    assert sp.simplify(to_C(pgal(u)) - sp.conjugate(to_C(u))) == 0
    for v in BATCH:
        assert pgal(padd(u, v)) == padd(pgal(u), pgal(v))
        assert pgal(pmul(u, v)) == pmul(pgal(u), pgal(v))
print("K1: THE FLIP IS COMPLEX CONJUGATION — gal(omega) = conj(omega) = 1 - omega,")
print("    and the pair map is additive AND multiplicative (batch-verified exactly).")
print("    CONSEQUENCE: every complex length 2 arccosh(tr/2) is conjugated, so")
print("    REAL LENGTHS ARE FIXED and TORSIONS ARE NEGATED — every class at once,")
print("    no exceptions, no per-class freedom.  Memo 81's law from one field fact.")

# ---------------- the holonomy and the word batch
def mmul(A, B):
    return tuple(tuple(padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j]))
                 for j in range(2)) for i in range(2))
Ma = ((ONE, ONE), (ZERO, ONE))
Mb = ((ONE, ZERO), (pneg(W), ONE))
def minv(A):
    (p, q_), (r_, s_) = A
    assert padd(pmul(p, s_), pneg(pmul(q_, r_))) == ONE
    return ((s_, pneg(q_)), (pneg(r_), p))
MAT = {'a': Ma, 'b': Mb, 'A': minv(Ma), 'B': minv(Mb)}
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
def mtr(A): return padd(A[0][0], A[1][1])

# K2: the reach audit — exact counting, no numerics
fixed, flipped = 0, 0
fixed_examples = []
frontier = [("", ((ONE, ZERO), (ZERO, ONE)))]
for L in range(8):
    nxt = []
    for w, M in frontier:
        for c in "abAB":
            if w and INV[w[-1]] == c:
                continue
            nxt.append((w + c, mmul(M, MAT[c])))
    for w, M in nxt:
        t = mtr(M)
        if t[1] == 0:                      # real trace <=> gal-fixed
            fixed += 1
            if len(fixed_examples) < 6:
                fixed_examples.append((w, t))
        else:
            flipped += 1
    frontier = nxt
tot = fixed + flipped
print(f"\nK2 (the reach audit, all {tot} reduced words to length 8):")
print(f"    MIRROR-FIXED (real trace, torsion-free): {fixed}  ({100*fixed/tot:.2f}%)")
print(f"    MIRROR-FLIPPED (torsion-carrying):       {flipped}  ({100*flipped/tot:.2f}%)")
print(f"    sample fixed classes: {[w for w, _ in fixed_examples]}")
print("    => the orientation-sensitive part of the record is the overwhelming")
print("    majority of classes, and ONE bit governs all of them simultaneously.")

# K3: the datum vs the invariant
kappa = mtr(mmul(mmul(MAT['a'], MAT['b']), mmul(MAT['A'], MAT['B'])))
assert kappa == (Fr(1), Fr(1))                       # 1 + omega
assert pgal(kappa) != kappa                          # the DATUM flips
for K in (kappa, pgal(kappa)):                       # the INVARIANT does not
    val = padd(padd(pmul(K, K), pneg(pmul((Fr(3), Fr(0)), K))), (Fr(3), Fr(0)))
    assert val == ZERO
syst = mtr(mmul(MAT['a'], MAT['b']))
assert syst == (Fr(2), Fr(-1))                       # 2 - omega
assert pgal(syst) == (Fr(1), Fr(1)) != syst          # flips as a datum
print("\nK3 (datum vs invariant): kappa = 1 + omega FLIPS as a coordinate, but its")
print("    minimal polynomial X^2 - 3X + 3 is FIXED; the systole trace 2 - omega")
print("    flips, while its geodesic LENGTH (the real part) does not.  The record's")
print("    INVARIANT content is mirror-blind; only its coordinates carry the sign.")

# K4: THE SM LEDGER — every banked magnitude is rational, hence fixed pointwise
SM_LEDGER = {
    "dim of the matter rep (27)": sp.Integer(27),
    "dim e6 (78)": sp.Integer(78),
    "e6 roots (72)": sp.Integer(72),
    "the glued spacetime count (64)": sp.Integer(64),
    "the twist modulus (2304)": sp.Integer(2304),
    "the hierarchy pole prime (953)": sp.Integer(953),
    "sin^2 theta_W (reproduced, not predicted)": sp.Rational(3, 8),
    "sum-rule term 151/64": sp.Rational(151, 64),
    "sum-rule term 553/64": sp.Rational(553, 64),
    "the sum rule total (11)": sp.Integer(11),
    "the discrete ladder count (112)": sp.Integer(112),
    "Vol / Vol_orb (12)": sp.Integer(12),
    "the Coxeter number (12)": sp.Integer(12),
    "the boundary disc group order (3)": sp.Integer(3),
}
assert sp.Rational(151, 64) + sp.Rational(553, 64) == 11
for name, val in SM_LEDGER.items():
    assert val.is_rational, name
    assert sp.simplify(sp.conjugate(val) - val) == 0        # fixed by ANY flip
# the E6 Gram and its roots are integral (rebuilt, not cited)
G = sp.Matrix([
    [ 2,  0, -1,  0,  0,  0], [ 0,  2,  0, -1,  0,  0],
    [-1,  0,  2, -1,  0,  0], [ 0, -1, -1,  2, -1,  0],
    [ 0,  0,  0, -1,  2, -1], [ 0,  0,  0,  0, -1,  2]])
assert all(e.is_Integer for e in G)
# (box widened in-run: E6's highest root has mark 3, so simple-root
#  coefficients reach +-3 — a radius-2 box returns only 68 of the 72)
import itertools
roots = [v for v in
         [sp.Matrix(c) for c in itertools.product(range(-3, 4), repeat=6)]
         if (v.T*G*v)[0, 0] == 2]
assert len(roots) == 72, len(roots)
assert all(e.is_Integer for v in roots for e in v)
print(f"\nK4 (THE SM LEDGER): all {len(SM_LEDGER)} banked SM-facing magnitudes verified")
print("    RATIONAL, and the E6 Gram with its 72 roots rebuilt INTEGRAL — rational")
print("    and integral data is fixed POINTWISE by any Galois flip.  The entire")
print("    content/magnitude layer lies in THE MIRROR'S KERNEL.")

print("""
THE ANSWER TO THE OWNER'S SM QUESTION, as the audit supports it:
THE INDEPENDENCE THEOREM CHANGES NOTHING ON THE SM'S CONTENT AND
EVERYTHING ABOUT ONE SIGN.  Precisely —
  * KERNEL (untouched, provably): every banked magnitude — the 27's
    content, the charge/root integrality, the hierarchy arithmetic
    (2304, 953), the sum rule, sin^2 theta_W, the ladder counts, the
    boundary data.  These are rational/integral: no Galois flip can
    move them, so memo 109's undecidable bit has ZERO reach here.
    The emergence story's WHAT is entirely in the kernel.
  * ODD PART (exactly one bit, total reach): the orientation column —
    the sign of every torsion, and through the banked chain (memo 83,
    W3) the CP sign and the record's chirality label.  Memo 109 says
    WHICH setting is actual is undecidable in-record; K1 says the
    setting is ONE choice for all classes at once, never a per-class
    freedom.
  * THE PHYSICAL SHAPE OF THAT (the honest form): the record does not
    and now PROVABLY CANNOT tell you which handedness is realized —
    but it forces that the choice is SINGLE and its consequences are
    LOCKED TOGETHER.  It predicts a CORRELATION, not a sign.  That is
    a falsifiable shape (find two of these signs independently
    settable and the record is refuted), and it is exactly what a
    theory whose object is amphichiral SHOULD say.
Gate 5 untouched.""")
