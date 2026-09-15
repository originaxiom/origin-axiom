#!/usr/bin/env python3
"""MEMO-118 CELL (the owner's "where can an ab/ba principle solve
bottlenecks again? read atlas and toolbox"): THE LAYER FLOW — the
layering map is a CLOSED-FORM discrete dynamical system in two
variables, and it is NOT the record's banked Fricke dynamics.

WHY THIS TARGET.  The atlas names the ab/ba principle at the
foundation (node `noncommutative_cancellation_residue`, PC04: "if
order matters, noncommutative residue can remain", with the L/R shear
system and the commutator certificates).  The TOE gap names DYNAMICS
as the one load-bearing missing ingredient.  Memo 117 showed the
layering map L : (A,B) -> (AB,BA) never collapses.  So the question
that joins them is: IS L A DYNAMICS?

THE DERIVATION (exact, and it closes):  on the character coordinates
(x, y, z) = (tr A, tr B, tr AB), the layering map acts as
    x' = tr(AB) = z,      y' = tr(BA) = z,
    z' = tr(ABBA) = tr(A B^2 A).
Using B^2 = yB - I and tr(A.AB) = x z - y and tr(A^2) = x^2 - 2:
    tr(ABBA) = y(xz - y) - (x^2 - 2) = xyz - y^2 - x^2 + 2,
and substituting xyz = x^2 + y^2 + z^2 - kappa - 2 gives the whole
map in TWO variables:
        z'     = z^2 - kappa
        kappa' = z^2 (2 - kappa) + kappa^2 - 2
CHECKS (each two-outcome):
  D1: verify the closed form against memo 117's independently computed
      tower at every level — one mismatch refutes the derivation.
  D2: is L kappa-PRESERVING?  Memo 94's banked Fricke map
      T(x,y,z) = (z, x, zx - y) IS (verified there).  If L is not,
      then L is a genuinely DIFFERENT map and must not be conflated
      with the record's banked dynamics.
  D3: the fixed points of the two-variable flow, exactly.
  D4: the honest scoping — what a canonical flow does and does not
      supply for the dynamics gap.
Gate 5 untouched.  Interpretive passages labeled.
"""
import sympy as sp
from fractions import Fraction as Fr

# ---- exact pair arithmetic (the tower, recomputed independently)
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
Ma = ((O, O), (Z, O)); Mb = ((O, Z), ((0, -1), O))
def fricke(x, y, z):
    t = padd(padd(pmul(x, x), pmul(y, y)), pmul(z, z))
    return psub(psub(t, pmul(pmul(x, y), z)), (2, 0))

# ---- D1: the closed form vs the true tower
print("D1 — the closed form  z' = z^2 - k,  k' = z^2(2-k) + k^2 - 2")
print("     checked against the independently computed tower:\n")
print(f"    {'n':>2s} {'z_n (true)':>26s} {'k_n (true)':>26s}  closed form")
A, B = Ma, Mb
z = mtr(mmul(A, B)); k = fricke(mtr(A), mtr(B), z)
ok = True
for n in range(9):
    x_t, y_t = mtr(A), mtr(B)
    z_t = mtr(mmul(A, B))
    k_t = fricke(x_t, y_t, z_t)
    match = (z_t == z) and (k_t == k)
    ok = ok and match
    shortz = str(z_t) if max(abs(z_t[0]), abs(z_t[1])) < 10**12 else "[large]"
    shortk = str(k_t) if max(abs(k_t[0]), abs(k_t[1])) < 10**12 else "[large]"
    print(f"    {n:2d} {shortz:>26s} {shortk:>26s}  {'MATCH' if match else 'MISMATCH'}")
    # advance both: the true tower, and the closed form
    A, B = mmul(A, B), mmul(B, A)
    z, k = psub(pmul(z, z), k), padd(psub(pmul(pmul(z, z), psub((2, 0), k)),
                                          (2, 0)), pmul(k, k))
assert ok
print("\n    the two-variable closed form reproduces the tower EXACTLY at every")
print("    level: the ab/ba layering IS a discrete dynamical system in (z, kappa).\n")

# ---- D2: is L kappa-preserving?  (memo 94's Fricke map T is.)
zz, kk = sp.symbols('z k')
k_next = sp.expand(zz**2*(2 - kk) + kk**2 - 2)
print("D2 — is the layer flow kappa-PRESERVING?")
print(f"    kappa' - kappa = {sp.factor(sp.expand(k_next - kk))}")
sols = sp.solve(sp.Eq(k_next, kk), kk)
print(f"    kappa' = kappa only on the locus kappa in {sols}  (a CURVE, not everywhere)")
print("    => THE LAYER FLOW IS **NOT** KAPPA-PRESERVING.  Memo 94's banked")
print("    Fricke map T(x,y,z) = (z, x, zx - y) IS (verified there).  So L and T")
print("    are DIFFERENT maps and must not be conflated: the record's banked")
print("    dynamics is NOT what layering generates.\n")

# ---- D3: fixed points, exactly
print("D3 — fixed points of the layer flow (z' = z, kappa' = kappa):")
fps = sp.solve([sp.Eq(zz**2 - kk, zz), sp.Eq(k_next, kk)], [zz, kk], dict=True)
for s in fps:
    print(f"    z = {sp.nsimplify(s[zz])},  kappa = {sp.nsimplify(s[kk])}")
print("    (these are the STATIONARY layers — configurations that layering")
print("    leaves unchanged; the record's own tower starts at kappa = 1 + omega")
print("    and is NOT at one of them, which is why the tower runs forever.)\n")

# ---- D4
print("""D4 — THE HONEST SCOPING: what this does and does not supply.
  SUPPLIES: a CANONICAL, DIMENSIONLESS, EXACTLY-SPECIFIED FLOW on the
    record's own invariants, generated by nothing but ab != ba.  Two
    variables, closed form, no free parameter, no imported premise.
    That is the FORM of a dynamics, and the record did not have one.
  DOES NOT SUPPLY: a RATE.  The flow has no time in it — the schedule
    wall (B716/B721) is untouched, and nothing here converts a layer
    index into a duration.  It is a discrete succession, not an
    equation of motion in a time variable.
  WHERE THAT LANDS ON THE GAP: the dynamics deficit is typed as
    exactly (one dimensionless flow datum + one unit).  This cell
    supplies a candidate for the FIRST HALF and provably not the
    second — the same form/rate split memo 90 found for expansion.
    So the honest statement is: **the ab/ba principle can supply the
    FORM of a dynamics; the RATE stays priced to the frame.**
  THE NAMED NEXT TEST (not run here, and not to be waved at): is the
    layer flow's step related to B723's lambda-weight — i.e. is THIS
    the flow whose rate lambda pays for?  That is the same
    level-crossing test already seated with cc, now with a concrete
    candidate flow to test AGAINST instead of an abstract one.
  FENCE: L is NOT the banked Fricke dynamics (D2), so nothing here
    inherits memo 94's two-branch law or its arrow; those results are
    about T and stay about T.  Gate 5 untouched.""")
