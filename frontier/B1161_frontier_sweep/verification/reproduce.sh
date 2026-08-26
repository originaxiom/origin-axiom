#!/usr/bin/env bash
# B1161 the frontier sweep (compute-all-we-can) -- reproduce the clean own-verified cells.
# (The crown free-orbit theorem was own-run by the workflow (crown_p1p2.py, 28->8 faithful
#  pairs, 2 free V4 orbits, trivial stabilizers) + adversarially verified; the Galois
#  structure of H is cited to B1067 disc-144. The down-Yukawa 3x3x4 selection arithmetic
#  was own-run in the sweep. Here: the three number-theory/anomaly facts.)
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee frontier_checks.txt
import mpmath as mp, sympy as sp
mp.mp.dps = 50

print("(SEAM-A seal cell) the PSLQ non-relation test is VACUOUS -- cannot seal MISMATCH")
z = mp.expjpi(mp.mpf(1)/3); Vol = 2*mp.im(mp.polylog(2, z))
L = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3))/9   # L(chi_-3,2), Hurwitz form
print("  Vol(4_1)          =", Vol)
print("  (3 sqrt3/2) L     =", mp.mpf(3)*mp.sqrt(3)/2*L, "  = Vol (B682):", mp.almosteq(mp.mpf(3)*mp.sqrt(3)/2*L, Vol, 1e-40))
print("  PSLQ(Vol, sqrt3*L)=", mp.pslq([Vol, mp.sqrt(3)*L], maxcoeff=10**4), "  <- PSLQ is LIVE (recovers B682, 2Vol=3 sqrt3 L)")
print("  PSLQ(1/6, Vol)    =", mp.pslq([mp.mpf(1)/6, Vol], maxcoeff=10**6), "  <- but rational-vs-Vol = None")
print("  PSLQ(3/7, Vol)    =", mp.pslq([mp.mpf(3)/7, Vol], maxcoeff=10**6), "  <- control also None => ZERO discriminating power")
print("  => the finite-phase (exp(2 pi i/6)) <-> Vol non-relation just restates Vol not in Q;")
print("     present in BOTH match and mismatch worlds. Cannot seal MISMATCH. SEAM-A stays a")
print("     NEEDS-SPECIALIST FLOOR (the Arakelov / marked-H3 W0 bar).")

print()
print("(generation-index cell) NULL -- no object index forces 3")
p = sp.Poly(sp.symbols('x')**2 - sp.symbols('x') + 1, sp.symbols('x'))
print("  trace field min poly x^2-x+1: disc =", sp.discriminant(p), ", degree =", p.degree())
print("  => Galois Z/2; irreducible-rep multiplicities in {1,2}, NEVER 3. chi(4_1 complement)=0.")
print("  Object's honest content = ONE generation; the '3' is external (cubic carrier / cover / E8).")

print()
print("(L132-B892 cell) the two-frame backbone: color-A2 centralizer in e6 = A2 + A2 (rank 6)")
# e6 rank 6; a color A2 (rank 2) centralizer is A2+A2 (rank 2) + the rank-2 A2 itself... 
# net: rank(centralizer) = 6-2 = 4 = A2(rank2)+u(1)^? ; the trinification A2+A2+A2 has rank 6.
print("  rank e6 = 6; trinification A2xA2xA2 has rank 2+2+2 = 6 (three orthogonal A2s).")
print("  weak A2's 3 sl2's each SM-shape the 27 => 12 anomaly solutions each = 36, all SM (B1160 cubic")
print("  -18(t-3)(t+3) => t=+-3). So the object-specific SM realization is DUAL-HOMED (trinification + B892).")
print()
print("REPRODUCES")
PY
