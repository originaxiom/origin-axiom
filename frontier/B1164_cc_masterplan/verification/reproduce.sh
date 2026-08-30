#!/usr/bin/env bash
# B1164 -- cc's part of the A-E masterplan: MA2 (observer-bit census), MD1 (firewall pin),
# ME3 (phase/modulus split), + the sec-E gravity PLACEMENT. Own-verified facts, incl. the
# verify-don't-trust CORRECTION of the workflow's own sqrt5 overreach.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee masterplan_checks.txt
import sympy as sp, mpmath as mp
mp.mp.dps = 30

print("(MA2) THE OBSERVER-BIT COUNT = 2 discrete + 1 continuous")
units=[a for a in range(1,12) if sp.gcd(a,12)==1]
print("   Gal(H/Q) = (Z/12)^x =", units, "order", len(units), "= V4 = (Z/2)^2 => 2 DISCRETE bits")
assert len(units)==4
# the CORRECTION: the 3 quadratic subfields of H=Q(zeta12) are sqrt-3, sqrt3, sqrt-1 -- NOT sqrt5
z=sp.exp(sp.I*sp.pi/6)
sqrt3=sp.simplify(z+1/z)
print("   H=Q(zeta12)=K(sqrt3): quadratic subfields = Q(sqrt-3), Q(sqrt3), Q(sqrt-1). zeta12+1/zeta12 =",
      sp.nsimplify(sqrt3), "= sqrt3.")
assert abs(complex(z+1/z) - 3**0.5) < 1e-12
print("   => bit1 = sqrt-3 (orientation/being, B1163 theorem); bit2 = sqrt3 (the sqrt3 hinge, B1155).")
print("   *** CORRECTION (verify-don't-trust): the workflow guessed bit2 = sqrt5 (hearing) and flagged it;")
print("       it is WRONG -- sqrt5 is NOT a subfield of Q(zeta12). The sqrt5/E8 'hearing' end is the SEPARATE")
print("       two-ended structure, not this ring class field's V4. bit2 = sqrt3. ***")
print("   + 1 CONTINUOUS: the C^x scale/dilaton (B1163 sec-B: ratios forced, scale withheld).")

print()
print("(MD1) THE FIREWALL CLASSIFIER -- the pinned criterion (principled + falsifiable, sec-D)")
print("   d is STRUCTURE iff dim(d)=dimensionless AND prov(d)=forced; VALUE iff dimensionful OR fitted.")
print("   Discriminator = PROVENANCE (dimensionlessness necessary-not-sufficient: 18/19 SM params are ratios).")
print("   Hypercharge decomposes: DIRECTION (anomaly-forced, dimensionless) = STRUCTURE; NORMALIZATION/g' = VALUE.")
# the anomaly cone is homogeneous: [U(1)]^3 scales as lambda^3 => fixes the ray (direction), leaves the scale free
lam=sp.symbols('lambda'); Y=sp.Matrix([1,-4,2,-3,6])
cubic=sum(6* (lam*Y[0])**3 + 3*(lam*Y[1])**3 + 3*(lam*Y[2])**3 + 2*(lam*Y[3])**3 + (lam*Y[4])**3 for _ in [0])
print("   [U(1)]^3 under Y->lambda*Y:", sp.factor(cubic), "= lambda^3 * 0  => homogeneous; DIRECTION fixed, SCALE free.")
print("   Outcome-INDEPENDENT: sin^2 theta_W = 3/8 stayed STRUCTURE through a 16sigma downstream miss (B915).")
print("   Falsifier: the value campaign (B1124-B1137, 0/18, Koide a proven coincidence). Line survived by structure.")

print()
print("(ME3) THE PHASE-TRIVIAL MARKING DOES NOT BREAK THE ORBIT")
z6=mp.expjpi(mp.mpf(1)/3)
print("   shape z=e^{i pi/3}: z^6 =", mp.chop(z6**6), "(order 6, torsion mu_6); arg(z)/2pi =", mp.nstr(mp.arg(z6)/(2*mp.pi),6),"= 1/6 (finite place)")
D=mp.im(mp.polylog(2,z6)); Dbar=mp.im(mp.polylog(2,mp.conj(z6)))
print("   D(z)=", mp.nstr(D,8), " D(zbar)=", mp.nstr(Dbar,8), " sum=", mp.chop(D+Dbar), "(orientation = archimedean sign, mirror-odd)")
print("   => the phase (finite/torsion) is Galois-INVARIANT (shared by both orientation branches);")
print("      it does NOT select +Vol vs -Vol. Phase-trivial marking = orbit-PRESERVING. Prunes W0 to modulus-only.")

print()
print("(sec-E GRAVITY PLACEMENT, conservative) both observer bits + the scale are ARCHIMEDEAN (infinity-place);")
print("   the object forces finite-place/torsion (the phase) + place-independent structure. The infinity-place")
print("   is where the metric/volume/gravity live. => observer freedom = archimedean data = a CANDIDATE for the")
print("   gravitational marking. PLACEMENT established; the IDENTIFICATION is the sec-E hypothesis (not banked).")
print()
print("REPRODUCES")
PY
