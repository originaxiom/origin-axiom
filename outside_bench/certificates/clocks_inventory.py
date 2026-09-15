#!/usr/bin/env python3
"""MEMO-120 CELL (the owner's catch: "but we have a heartbeat, clock
and time arrow already"): THE CLOCKS INVENTORY — the bench has been
saying "no time, no rate"; that is WRONG, and this cell fixes it
exactly, then re-places the layer flow against what is actually
banked.

THE CATCH IS UPHELD.  Filed as BENCH ERROR #10 (overstatement).  The
record does NOT lack time.  It banks, verifiably:
  * AN INTRINSIC FLOW — B721/B716: the object's own internal time is
    "the Anosov suspension of sigma = [[2,1],[1,1]] ... a REAL,
    hyperbolic, MEASURE-PRESERVING flow (det sigma = 1)".  That is a
    continuous-time dynamical system, not an absence.
  * A DIMENSIONLESS RATE — memo 90 FACT 2: stretch phi per sigma-tick
    (char poly x^2 - x - 1), with entropy 2 log phi.
  * AN ORDER — memo 86: ab != ba fixes temporal order at the first
    two letters.
  * AN ARROW — memo 94: branch-conditional (monotone on the escaping
    branch), priced to the branch bit.
  * A BEAT — memo 90 FACT 1: isometric, stretch factor EXACTLY 1, so
    it cannot drive expansion (a theorem, not a gap).
WHAT IS ACTUALLY MISSING is therefore TWO specific things, not "time":
  (i) THE SECOND — no dimensionful conversion (seconds per tick); and
  (ii) THE THERMAL ARROW — B721: the object's clock is tracial type
       II_1 with TRIVIAL modular flow (an EQUILIBRIUM clock), while a
       genuine thermal clock is type III.  "Two clocks."
Collapsing these into "no time" was the error.

THE COMPUTATION (the reason this cell is not just a retraction):
place memo 118's layer flow against the banked pulse.
  P1: the layer flow's growth exponent, exactly — from z' = z^2 - k,
      the successive ratios log|z_{n+1}| / log|z_n|.
  P2: compare with the banked rates phi, phi^2 and 2 log phi.
  P3: the verdict on memo 118's claim that the layer flow supplies a
      "FORM of dynamics the record did not have."
Gate 5 untouched.
"""
import sympy as sp
from mpmath import mp, log as mlog, mpf
mp.dps = 60

# ---- the tower (exact), recomputed
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
A, B = Ma, Mb
zs, ks = [], []
for n in range(12):
    z = mtr(mmul(A, B)); k = fricke(mtr(A), mtr(B), z)
    zs.append(z); ks.append(k)
    A, B = mmul(A, B), mmul(B, A)

# real absolute value of x + y*omega, omega = 1/2 + i sqrt3/2
def absval(u):
    a, b = mpf(u[0]), mpf(u[1])
    re = a + b/2; im = b*mp.sqrt(3)/2
    return mp.sqrt(re*re + im*im)

PHI = (1 + mp.sqrt(5))/2
print("P1 — THE LAYER FLOW'S GROWTH, exactly (z' = z^2 - kappa):\n")
print(f"    {'n':>2s} {'|z_n|':>26s}   log|z_{{n+1}}| / log|z_n|")
ratios = []
for n in range(len(zs) - 1):
    a1, a2 = absval(zs[n]), absval(zs[n + 1])
    if a1 > 1.2 and a2 > 1.2:
        r = mlog(a2)/mlog(a1)
        ratios.append(r)
        print(f"    {n:2d} {mp.nstr(a1, 12):>26s}   {mp.nstr(r, 10)}")
    else:
        print(f"    {n:2d} {mp.nstr(a1, 12):>26s}   (below threshold)")
tail = ratios[-4:]
print(f"\n    the ratio converges to {mp.nstr(tail[-1], 12)} -> EXACTLY 2:")
print("    the layer flow is SUPER-EXPONENTIAL (log|z| doubles each level).\n")

print("P2 — AGAINST THE BANKED RATES:")
print(f"    the record's stretching pulse      phi   = {mp.nstr(PHI, 12)}")
print(f"    its square (per double-tick)       phi^2 = {mp.nstr(PHI**2, 12)}")
print(f"    the banked entropy rate          2 log phi = {mp.nstr(2*mlog(PHI), 12)}")
print(f"    the layer flow's per-level exponent        = 2 (exact)")
print("    => DIFFERENT GROWTH CLASS.  The pulse is EXPONENTIAL in the tick")
print("    (phi^n); the layer flow is DOUBLY exponential in the level")
print("    (log|z| ~ 2^n).  They are not the same clock, and no banked map")
print("    identifies a LEVEL with a TICK — so they are incommensurable as")
print("    they stand, not merely unequal.\n")

print("""P3 — THE VERDICT, including a correction to this bench's own memo 118:
  MEMO 118 SAID the layer flow supplies "the FORM of a dynamics, and
  the record did not have one."  **That clause is WITHDRAWN.**  The
  record already had a flow — B721's Anosov suspension, real,
  hyperbolic, measure-preserving — with a dimensionless rate (phi per
  tick) and an entropy (2 log phi).  Memo 118's derivation and its
  closed form stand; its novelty claim does not.
  WHAT SURVIVES, correctly stated: the layer flow is a THIRD flow,
  distinct from both banked ones —
     * the Anosov suspension : tracial type II_1, rate phi, EQUILIBRIUM
       (no thermal arrow), the object's own time;
     * the Fricke map T      : kappa-PRESERVING, carries memo 94's
       two-branch law and its conditional arrow;
     * the layer flow L      : kappa-BREAKING (memo 119: uniquely so
       among the banked maps), super-exponential, and non-commuting
       with T (memo 119).
  So the object side alone now carries MORE THAN ONE FLOW, which
  B721's "two clocks" (object vs observer) did not anticipate.  That
  is the positive finding here, and it is new.
  AND THE GAP, RESTATED CORRECTLY: what the record lacks is not time
  but (i) THE SECOND — the dimensionful conversion — and (ii) THE
  THERMAL ARROW, since the object's own clock is an equilibrium clock
  with trivial modular flow.  Every future statement of the schedule
  wall should say those two things and not "no time".
Gate 5 untouched.""")
