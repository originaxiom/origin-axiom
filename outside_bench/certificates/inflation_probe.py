#!/usr/bin/env python3
"""MEMO-132 CELL (ranked remainder item 1a): THE COSMOLOGY LEDGER'S ROW 2
(INFLATION) FIRST PROBE, RUN — and it returns a STRUCTURAL OBSTRUCTION, not
a stall: every map in the record's tower is volume-preserving or
volume-destroying BY IDENTITY, so no net volume growth exists anywhere in
the object, and an e-fold count is not merely unavailable but UNDEFINABLE.

THE LEDGER'S OWN WORDS (row 2, MISSING, first probe named there and never
run): "does any dimensionless ratio built from this depth-grading or this
entropy reproduce a horizon-problem or flatness-problem STRUCTURAL
SIGNATURE ... under a preregistered, two-sided, Gate-5-compliant test?"
It also records the honest prior — that the probe would likely stall as
row 1's three attempts did — and the one retraction: S008's "iterations
~ e-folds" was REMOVED by S002/B124/V113 as value-matching.  Nothing here
re-opens that; the probe asked is the STRUCTURAL one.

REFRAMING THE PROBE SO IT IS DECIDABLE (stated before running).  A tilt or
an e-fold count is not a free-floating "dimensionless ratio": both are
measures of NET VOLUME GROWTH per step.  e-folds count log of a volume
ratio; a spectral tilt requires a preferred sign of growth across modes.
So the probe has an exact and Gate-5-clean form:
    DOES ANY MAP IN THE RECORD'S TOWER PRODUCE NET VOLUME GROWTH?
and that is settled by the Jacobian determinant as an IDENTITY, with no
measured value anywhere near it.

THE PREREGISTERED FORK (fixed before any determinant is printed):
  I-A  some tower map has |det J| > 1 on the record's orbit => net volume
       growth exists => an e-fold-like quantity IS definable => row 2's
       probe returns a genuine CANDIDATE and the row stays MISSING with a
       live lead.
  I-B  every tower map has |det J| identically 1 or 0 => the sum of
       Lyapunov exponents is zero (or minus infinity) => NO net volume
       growth exists anywhere => the probe returns a STRUCTURAL
       OBSTRUCTION, and row 2's grade should move from MISSING (no arc)
       to a PROVED NEGATIVE with the mechanism named.
Neither outcome is preferred; the identities decide.

THE MAPS TESTED (the record's own, nothing invented):
  * T, the Fricke/golden map (x,y,z) -> (z, x, zx - y)   [memo 121/B496,
    verified kappa-preserving];
  * L, the Thue-Morse/layering map (x,y,z) -> (z, z, xyz - x^2 - y^2 + 2)
    [B496's T1, memo 117's layering];
  * sigma, the golden substitution a->ab, b->a, and its square, which is
    B721's Anosov matrix [[2,1],[1,1]] (memo 90's "one stretching pulse").
Gate 5 untouched: determinants and identities only.  No measured n_s, no
measured e-fold count, no Planck datum enters — and the retracted S008
coincidence is cited, not used.
"""
import sympy as sp

x, y, z, t = sp.symbols('x y z t')

# ---------------- N1/N2: the maps and their determinants AS IDENTITIES
T = sp.Matrix([z, x, z*x - y])
L = sp.Matrix([z, z, x*y*z - x**2 - y**2 + 2])
V = sp.Matrix([x, y, z])
JT = T.jacobian(V)
JL = L.jacobian(V)
dT = sp.simplify(JT.det())
dL = sp.simplify(JL.det())
print("N1 — THE RECORD'S TOWER MAPS, and their Jacobians:")
print(f"    T (Fricke/golden): {list(T)}")
print(f"        J_T = {JT.tolist()}")
print(f"    L (Thue-Morse/layering): {list(L)}")
print(f"        J_L = {JL.tolist()}")
print("\nN2 — THE DETERMINANTS, as IDENTITIES in Z[x,y,z] (not point values):")
print(f"    det J_T = {dT}      <- constant, independent of the point")
print(f"    det J_L = {dL}      <- identically zero")
assert dT == -1, dT
assert dL == 0, dL
# why L degenerates, exhibited rather than asserted
print(f"    (J_L's first two rows are identical: {JL.row(0).tolist()} =="
      f" {JL.row(1).tolist()} — L sends x and y to the same coordinate,")
print("     so one direction is destroyed at every step.)")
assert JL.row(0) == JL.row(1)

# the substitution side
S = sp.Matrix([[1, 1], [1, 0]])          # sigma: a->ab, b->a
S2 = S**2
print(f"\n    sigma = {S.tolist()}   det = {S.det()}   eigenvalues"
      f" {sorted(sp.Matrix(S).eigenvals().keys(), key=lambda e: sp.re(e))}")
print(f"    sigma^2 = {S2.tolist()}   det = {S2.det()}   (B721's Anosov matrix)")
assert abs(S.det()) == 1 and S2.det() == 1
ev = list(S2.eigenvals().keys())
prod = sp.simplify(ev[0]*ev[1])
assert sp.simplify(prod - 1) == 0
print(f"    eigenvalue product = {prod} — one stretches by phi^2, the other")
print("    contracts by phi^-2: RECIPROCAL, exactly compensating.")

# ---------------- N3: the Lyapunov sum
print("\nN3 — THE SUM OF LYAPUNOV EXPONENTS (= log|det J|, by definition):")
print(f"    T      : log|det J_T| = log|{dT}| = 0        -> VOLUME-PRESERVING")
print(f"    L      : det J_L = 0                          -> VOLUME-DESTROYING")
print(f"    sigma  : log|det sigma| = log 1 = 0           -> VOLUME-PRESERVING")
print("    Every one of the record's tower maps therefore has ZERO or")
print("    NEGATIVE-INFINITE net volume growth per step, AT EVERY POINT,")
print("    as an identity rather than as a fact about some orbit.")

# ---------------- N4: on the record's own orbit
W = sp.Rational(1, 2) + sp.sqrt(3)*sp.I/2          # omega
P0 = (sp.Integer(2), sp.Integer(2), 2 - W)
print("\nN4 — ON THE RECORD'S OWN POINT AND ORBIT (P0 = (2, 2, 2-omega)):")
P = P0
for lvl in range(4):
    jt = JT.subs({x: P[0], y: P[1], z: P[2]})
    d = sp.simplify(jt.det())
    print(f"    level {lvl}: det J_T = {d}")
    assert sp.simplify(d + 1) == 0
    P = tuple(sp.simplify(c) for c in T.subs({x: P[0], y: P[1], z: P[2]}))
print("    the determinant does not drift along the orbit — it cannot,")
print("    because it is a constant polynomial.")

# ---------------- N5: the verdict
print("""
N5 — THE VERDICT (the preregistered fork):
  No tower map has |det J| > 1 anywhere.  ==> OUTCOME I-B.
  ROW 2's FIRST PROBE RETURNS A STRUCTURAL OBSTRUCTION, NOT A STALL:
    * e-folds count the logarithm of a VOLUME RATIO.  The record's tower
      has log|det| = 0 identically (T, sigma) or det = 0 identically (L).
      So the e-fold count is not "unavailable pending a computation" — it
      is IDENTICALLY ZERO or undefined, and no choice of coordinates,
      depth-grading or entropy can change a determinant identity.
    * a spectral TILT needs a preferred sign of growth across modes.
      Volume preservation with reciprocal eigenvalue pairs (sigma^2:
      phi^2 and phi^-2, product exactly 1) supplies expansion and
      contraction in exactly compensating measure — which is precisely
      S002/B124's banked "reciprocal-closed, two-headed time" finding,
      NOW WITH ITS MECHANISM: the closure is forced by det = 1.
  PROPOSED GRADE CHANGE for the cosmology ledger's row 2: from MISSING
  (no dedicated arc) to a PROVED NEGATIVE with the mechanism named —
  the object cannot inflate because its tower is measure-preserving by
  identity.  This is the same SHAPE as the scale-torsor no-go (no
  dimensionful rate) but a DIFFERENT and independent theorem: it forbids
  the dimensionless volume growth too.

A SHARPENING THE RECORD SHOULD CARRY (this cell's second finding):
  memo 90 types the expansion FORM as object-side, "ratio phi per tick".
  That is TRUE and UNCHANGED — but sigma has det = -1, so the phi is a
  stretch in ONE direction against a 1/phi contraction in the other.
  THE RECORD'S EXPANSION IS A SHEAR, NOT A DILATION: anisotropic, with
  zero net volume change.  Any reading of memo 90 as an isotropic
  FRW-like expansion is wrong, and the LEAP-1 payment (which asserts the
  FORM is object-side) inherits this caveat: what is object-side is a
  volume-preserving shear form, which is NOT what an FRW scale factor is.
  Filed here so the payment cannot drift into claiming more than it buys.
  FENCE: this cell tests NET VOLUME GROWTH, which is what e-folds and
  tilts measure.  It does not claim the object is dynamically trivial —
  it has positive entropy log phi (S045) and a genuine Anosov flow
  (B721); those are SHEAR entropies, and shear is not expansion.
  Gate 5 untouched.""")
