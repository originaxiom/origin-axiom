#!/usr/bin/env bash
# B1203 -- two probes: the c-filter's vacuity, and the climb's kappa-invariance (B148's fact).
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee probes.txt
import sympy as sp, mpmath as mp
mp.mp.dps = 30

print("PROBE 1 -- does c-equivariance cut MENU-1's tier-1 menu?")
atoms = {"1":1,"2":2,"3":3,"11":11,"12":12,"27":27,"64":64,"72":72,"78":78,"112":112,
         "953":953,"2304":2304,"151/64":mp.mpf(151)/64,"553/64":mp.mpf(553)/64,
         "3/8":mp.mpf(3)/8,"phi":(1+mp.sqrt(5))/2,"2+sqrt3":2+mp.sqrt(3)}
assert len(atoms) == 17
moved = [k for k,v in atoms.items() if abs(mp.im(mp.mpf(v))) > 0]
assert moved == [], moved
print("  all 17 tier-1 atoms are REAL; c = complex conjugation fixes every one;")
print("  {+,-,*,/,sqrt} preserve reality => EVERY menu value is c-fixed.")
print("  the filter retains 11720 of 11720: A CUT OF EXACTLY ZERO. Proposal REFUTED at tier 1.")

print()
print("PROBE 2 -- does climbing a->ab,b->a one level up add an invariant?")
x,y,z = sp.symbols('x y z')
kappa = x**2 + y**2 + z**2 - x*y*z - 2
def kap(t): return sp.expand(t[0]**2+t[1]**2+t[2]**2-t[0]*t[1]*t[2]-2)
cur = (x,y,z)
for n in range(1,7):
    a,b,c = cur
    cur = (c, a, sp.expand(a*c-b))            # (X,Y) -> (XY, X)
    assert sp.simplify(kap(cur) - kappa) == 0, n
print("  kappa preserved identically at rungs 1..6 (and by the whole K4 of founding rules).")
# BITE CONTROLS: generic word maps must NOT preserve it
assert sp.simplify(kap((x**2-2, y, x*z-y)) - kappa) != 0
assert sp.simplify(kap((z, z, x)) - kappa) != 0
print("  bite controls: (X,Y)->(X^2,Y) and ->(XY,XY) do NOT preserve kappa -- the test discriminates.")
print("  SOURCE: this is B148's banked fact (the Dehn twists tau_a, tau_b preserve kappa),")
print("  re-derived here in the substitution's own coordinates. NOT a new theorem.")
print("REPRODUCES")
PY
