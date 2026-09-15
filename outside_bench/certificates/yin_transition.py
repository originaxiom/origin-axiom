#!/usr/bin/env python3
"""MEMO-124 CELL (the owner's yin/yang question, the computable half):
THE TOWER'S IMAGINARY→REAL TRANSITION — the record's layering tower is
PURELY IMAGINARY for exactly two steps, passes through the cusp
modulus, and is REAL forever after.  Three independently-derived facts
coincide at that one level.

WHY THIS BEARS ON THE QUESTION.  The owner asks whether the programme
is "yin only" — the positive/existence side — and whether the negative
or imaginary side is accounted for.  The record's own arithmetic
already carries that split: B721 states the two clocks "differ in
FIELD (hearing REAL Q(sqrt5) vs being IMAGINARY Q(sqrt-3))".  So the
sharp version of the question is computable: WHERE does the record's
own dynamics cross between them?

THE CHECKS (exact, integer pair arithmetic):
  Y1 THE CUSP COINCIDENCE: z_1 (the tower's level-1 coordinate) is
     claimed to be PURELY IMAGINARY and equal to memo 100's
     grammar-derived cusp modulus tau = +-(4 omega - 2) = +-2 sqrt(-3)
     — the r-bit's carrier, the disc-48 lattice generator.  Verify
     both: Re(z_1) = 0 exactly, and z_1 = -(4 omega - 2) exactly.
  Y2 THE TRANSITION: track the omega-component of (z_n, kappa_n).
     Establish exactly which levels are non-real, and that once real
     the recursion (z' = z^2 - k, k' = z^2(2-k) + k^2 - 2) keeps
     everything real forever (integer arithmetic, no escape).
  Y3 THE TRIPLE COINCIDENCE AT LEVEL 1: kappa = -2 (B496's Markov
     surface), z = the cusp modulus (memo 100, disc -48), and the
     coordinate purely imaginary (the being field's pure part).  Three
     facts from three unrelated arcs meeting at one level.
Gate 5 untouched.  Interpretive passages labeled.
"""
from fractions import Fraction as Fr

def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def psub(u, v): return (u[0] - v[0], u[1] - v[1])
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)
Z, O, W = (0, 0), (1, 0), (0, 1)
def mmul(P, Q):
    return ((padd(pmul(P[0][0], Q[0][0]), pmul(P[0][1], Q[1][0])),
             padd(pmul(P[0][0], Q[0][1]), pmul(P[0][1], Q[1][1]))),
            (padd(pmul(P[1][0], Q[0][0]), pmul(P[1][1], Q[1][0])),
             padd(pmul(P[1][0], Q[0][1]), pmul(P[1][1], Q[1][1]))))
def mtr(P): return padd(P[0][0], P[1][1])
def fricke(x, y, z):
    t = padd(padd(pmul(x, x), pmul(y, y)), pmul(z, z))
    return psub(psub(t, pmul(pmul(x, y), z)), (2, 0))
# omega = 1/2 + i sqrt3/2 :  x + y*omega has Re = x + y/2, Im = y*sqrt3/2
def re2(u): return Fr(2*u[0] + u[1], 2)      # Re, exactly (as a rational)
def im_coeff(u): return u[1]                 # Im = im_coeff * sqrt3/2

A, B = ((O, O), (Z, O)), ((O, Z), ((0, -1), O))
tower = []
for n in range(7):
    z = mtr(mmul(A, B)); k = fricke(mtr(A), mtr(B), z)
    tower.append((n, z, k))
    A, B = mmul(A, B), mmul(B, A)

# ---- Y1: the cusp coincidence
z1 = tower[1][1]
TAU = (Fr(-2), Fr(4))                        # 4*omega - 2, memo 100's tau
assert z1 == (2, -4)
assert (z1[0], z1[1]) == (-TAU[0], -TAU[1]), (z1, TAU)
assert re2(z1) == 0
sq = pmul((Fr(-1), Fr(2)), (Fr(-1), Fr(2)))  # (2 omega - 1)^2 = -3
assert sq == (Fr(-3), Fr(0))
assert pmul(z1, z1) == (-12, 0)
print("Y1 — THE CUSP COINCIDENCE:")
print(f"    z_1 = {z1[0]} + {z1[1]}*omega,  Re(z_1) = {re2(z1)}  => PURELY IMAGINARY")
print(f"    and z_1 = -(4 omega - 2) = -tau EXACTLY, where tau is memo 100's")
print("    GRAMMAR-DERIVED cusp modulus (the longitude baBAABab's holonomy,")
print("    the disc-48 lattice generator, the r-bit's carrier).")
print(f"    z_1^2 = {pmul(z1, z1)} — real, because (2 omega - 1)^2 = -3.\n")

# ---- Y2: the transition
print("Y2 — THE IMAGINARY -> REAL TRANSITION (omega-component per level):")
print(f"    {'n':>2s}  {'Re(z_n)':>12s} {'Im-coeff(z_n)':>14s}  {'Im-coeff(k_n)':>14s}  status")
first_real = None
for n, z, k in tower:
    st = "REAL" if (z[1] == 0 and k[1] == 0) else ("z imaginary" if re2(z) == 0 else "complex")
    if z[1] == 0 and k[1] == 0 and first_real is None:
        first_real = n
    rz = re2(z)
    print(f"    {n:2d}  {str(rz):>12s} {z[1]:>14d}  {k[1]:>14d}  {st}")
assert first_real == 2
assert all(tower[n][1][1] == 0 and tower[n][2][1] == 0 for n in range(2, 7))
print(f"    => the tower is NON-REAL for exactly levels 0 and 1, and REAL from")
print(f"    level {first_real} onward.  Once real it stays real: the recursion is")
print("    integer arithmetic in (z, kappa), with no route back to the")
print("    omega-component.  The crossing happens ONCE and is irreversible.\n")

# ---- Y3: the triple coincidence
k1 = tower[1][2]
assert k1 == (-2, 0)
print("Y3 — THE TRIPLE COINCIDENCE AT LEVEL 1 (three unrelated arcs, one level):")
print(f"    (i)   kappa_1 = {k1[0]} — EXACTLY B496's Markov surface kappa = -2")
print("          (the locus whose mixed semigroup B496 studied);")
print("    (ii)  z_1 = -tau = -2 sqrt(-3) — EXACTLY memo 100's grammar-derived")
print("          cusp modulus, the disc-48 carrier of the r-bit;")
print("    (iii) Re(z_1) = 0 — the coordinate is PURELY imaginary, the being")
print("          field's pure part, and squaring it is what makes everything")
print("          real thereafter.")
print("    Three facts, from B496, from memo 100, and from the field split,")
print("    meeting at the same single level of the record's own tower.\n")

print("""INTERPRETATION (labeled; the computation above is exact, this is not):
  The record's own arithmetic already HAS a two-sided structure — B721
  puts it plainly: the two clocks "differ in FIELD (hearing REAL
  Q(sqrt5) vs being IMAGINARY Q(sqrt-3))".  So the programme is not
  built on the positive side alone; it is built on a field that IS the
  imaginary one, with a real partner.
  And this cell locates the crossing precisely: the record's layering
  dynamics begins in the imaginary/being field, passes at level 1
  through the PURELY imaginary cusp modulus — the same 2 sqrt(-3) the
  grammar derives as the r-bit's carrier, at the same level where
  kappa sits on B496's Markov surface — and is REAL from level 2
  onward, irreversibly.
  So the honest shape of the answer to "are we doing yin only": the
  two sides are both present and the record knows which is which; what
  this cell adds is that the CROSSING BETWEEN THEM is a specific,
  computable event, happening once, at the cusp.  Whether the
  programme has WORKED both sides equally is a different question —
  a corpus-balance question, not a mathematical one — and it is not
  answered here.
Gate 5 untouched.""")
