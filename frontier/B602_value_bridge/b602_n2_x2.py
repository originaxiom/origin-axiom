"""B602 cell N2 (sealed order; runs after N1 banked): the X2 magnitude
cells, exact. J cells INVALID-DEGENERATE (g = 0, N0).

Live cells: W x identity-D and W x D. |r_cl| = (N8 tau4)/(N4 tau8) exactly
(|1-w| = |1+w| = 2); the stage magnitudes: |hbar3/h3| = 1 (identity-D) and
phi (D-norm, d = (phi, 1)). The W-norm X2 cells carried the sealed
EXPECTED-FAIL annotation; the exact residual factor is the deliverable.
"""
import sympy as sp

N4 = 2096640
N8 = 536481792000
TAU4 = 260736
TAU8 = 100636318520821923840
phi = (1 + sp.sqrt(5)) / 2

r = sp.Rational(N8, N4) * sp.Rational(TAU4, TAU8)
print(f"|r_cl| (W-norm) = (N8 tau4)/(N4 tau8) = {r} "
      f"= {sp.factorint(r.p)} / {sp.factorint(r.q)}")
print(f"                approx {float(r):.6e}")
for cell, target in (("W x identity-D", sp.Integer(1)), ("W x D", phi)):
    match = sp.simplify(r - target) == 0
    resid = sp.simplify(r / target)
    print(f"X2 [{cell}]: |r_cl| = {target}? {bool(match)}   "
          f"residual factor r/target approx {float(resid):.6e}")
print("X2 [J x identity-D]: INVALID-DEGENERATE (g = 0, per the seal)")
print("X2 [J x D]:          INVALID-DEGENERATE (g = 0, per the seal)")
print("N2 DONE")
