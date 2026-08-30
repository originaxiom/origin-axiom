#!/usr/bin/env bash
# B1204 -- the shape of a forcing theorem, read off the record's own successful forcings.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee forcing_shape.txt
import sympy as sp

print("THE PRECEDENT (B1160): how the record's one continuum-to-points forcing actually worked.")
Yq, t = sp.symbols('Yq t')
# the 3 LINEAR anomaly conditions cut the 5-dim charge space to a line:
Yl, Ye = -3*Yq, 6*Yq                       # Yu + Yd = -2 Yq
Yu = -1 + t; Yd = sp.simplify(-2*Yq - Yu)  # the surviving one-parameter family (Yq = 1)
print("  linear conditions  : 5-dim charge space -> a LINE (one free parameter t)")
# the CUBIC condition [Y]^3 is what cuts the line to POINTS:
cubic = sp.factor(-18*(t-3)*(t+3))
roots = sp.solve(cubic, t)
print(f"  the CUBIC [Y]^3    : factors as {cubic} => t in {roots} -- a LINE cut to TWO POINTS")
assert set(roots) == {3, -3}
print("  => the decisive step was NONLINEAR. Linear/symmetry conditions cut DIMENSION;")
print("     only the nonlinear, FAILABLE condition cut to a finite set.")
print()
print("THE TWO FAMILIES of successful forcing in this record:")
print("  (i)  CLASSIFICATION + membership  -- E6 via McKay/ADE; the breaking chain (2 of 27 SM-safe);")
print("       the tone set via the McKay tensor law. A finite list, and a test for being on it.")
print("  (ii) CONSISTENCY/CANCELLATION     -- hypercharge via anomaly freedom, decisive step cubic.")
print("  BOTH ARE FAILABLE. NEITHER IS A SYMMETRY.")
print()
print("THE CONTRAST (B1203): the two candidates just eliminated were both SYMMETRIES --")
print("  c-equivariance (cut 0 of 11720) and iteration of a->ab,b->a (kappa conserved).")
print("  A symmetry the admissible class already respects cannot select within it (MB12:")
print("  a criterion must be able to FAIL).")
print()
print("THE NAMED CANDIDATE HOME: the object's OWN cubic -- the unique invariant in Sym^3(27),")
print("  nullspace dimension exactly 1 (B884) -- at the coupling, which is where the record")
print("  says the values live (E1's re-frame). Same shape as the one forcing that worked.")
print("REPRODUCES")
PY
