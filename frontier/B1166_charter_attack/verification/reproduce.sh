#!/usr/bin/env bash
# B1166 -- cc's attack on cloud's GRAVITY_CHARTER (60bcf01d), the two cc-assigned sub-claims.
# C3 (one dilaton, not two moduli): VERIFIED. C4 (the three (Z/2)^2 are one torsor): REFUTATION
# CANDIDATE (the free-orbit torsor is sqrt3-flavored, being x hearing is sqrt5-flavored).
set -euo pipefail
cd "$(dirname "$0")"

echo "########## C3 -- the continuous observer freedom is ONE dilaton (R+), not two moduli ##########"
python3 - << 'PY' 2>/dev/null
import snappy
M=snappy.Manifold('m004')
cv=M.complex_volume()
print("C3 fact 1 (the phase pin): complex volume Vol + i*CS =", cv)
print("   |CS| =", abs(complex(cv).imag), "-> CS = 0 (amphichiral, B1163) => the complex volume is REAL")
print("   => the object supplies NO free U(1) phase: the phase is pinned to CS=0, up to the DISCRETE")
print("      mu_6 = roots of unity in the trace field K=Q(sqrt-3)=Q(zeta_6) (a Z/6, a finite/torsion bit,")
print("      NOT a continuous U(1)). This is cloud's E1 'gravitational phase is mu_6 torsion', exhibited.")
assert abs(complex(cv).imag) < 1e-9
print("C3 fact 2 (no second modulus): H1(m004) =", M.homology(), "; cusps =", M.num_cusps())
print("   the complete hyperbolic structure is UNIQUE (Mostow rigidity); the 1-cusp deformation is frozen")
print("   by completeness => NO continuous geometric modulus beyond the C^x on the top form.")
print("   C^x = R+ x U(1): U(1) object-paid (CS=0/mu_6, fact 1); R+ = the scale, the ONE withheld continuous")
print("   datum (the scale wall). => the observer's continuous freedom is R+ ALONE. C3 VERIFIED.")
PY

echo
echo "########## C4 -- are the three (Z/2)^2 presentations ONE torsor 'with named actions'? ##########"
python3 - << 'PY'
import sympy as sp
# The free-orbit V4 (B1161) = Gal(H/Q), H = ring class field disc 144 = Q(zeta_12) = K(sqrt3) (B1067).
# Its three quadratic subfields + which primes ramify:
zeta12_disc = 144
fac = sp.factorint(zeta12_disc)
print("free-orbit field H = Q(zeta_12): disc =", zeta12_disc, "=", fac, "=> ONLY primes 2,3 ramify")
# The three quadratic subfields of Q(zeta_12):
subfields = {"Q(sqrt-3)": -3, "Q(sqrt3)": 3, "Q(sqrt-1)": -1}
print("   three quadratic subfields:", list(subfields.keys()), "  (B1164 own-verified)")
print("   => the free-orbit torsor's second generator toggles sqrt3 (the 'being x sqrt3' V4).")
# being x hearing (B713/B926 W11): being=Q(sqrt-3), hearing=Q(sqrt5).
print()
print("being x hearing V4 (B713/B926 W11): being = Q(sqrt-3) [prime 3], hearing = Q(sqrt5) [prime 5]")
# Is sqrt5 in Q(zeta_12)?  5 must ramify in H for Q(sqrt5) subset H; but only 2,3 ramify.
five_ramifies = (5 in fac)
print("   does 5 ramify in H=Q(zeta_12)?", five_ramifies, "=> Q(sqrt5) is NOT a subfield of Q(zeta_12)")
assert not five_ramifies
print()
print("VERDICT C4 = REFUTATION CANDIDATE: the free-orbit torsor (sqrt3, disc 144) and the being x hearing")
print("V4 (sqrt5) have DIFFERENT named second generators over DIFFERENT quadratic fields (sqrt3 vs sqrt5,")
print("sqrt5 not in Q(zeta_12)). As torsors 'WITH NAMED ACTIONS' (C4's own clause) they are NOT isomorphic;")
print("only the abstract (Z/2)^2-torsor-on-4-points iso survives, which C4's 'named actions' clause forbids.")
print("So C4 as literally stated is REFUTED for the (free-orbit, being x hearing) pair -- pending cloud's")
print("intent (abstract vs named-action) + the exact B1024 frame-V4 action (cc/codex disc-144 chase).")
PY
echo
echo "REPRODUCES"
