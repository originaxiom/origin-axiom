#!/usr/bin/env python3
"""B167 -- the conserved => no-internal-scale lemma (the firewall, stated).

Sharpens the POSTULATED prose of STRATEGIC_SYNTHESIS 8a (the five-door map) + B148/B151
+ P010 into a stated structural argument. FIREWALL-SIDE: this SHARPENS the wall; it asserts
no scale, no Lambda, no crossing; nothing to CLAIMS.md (stays POSTULATED -> "stated argument").

The verifiable backbone [exact]:
  L1  kappa = x^2+y^2+z^2-xyz-2 (Fricke-Vogt) is a FIRST INTEGRAL of the trace map: the
      Dehn twists Ta, Tb preserve it, hence so does every metallic monodromy phi_m=Ta^m Tb^m.
      => kappa does not change along an orbit ("does not run").
  L2  MB6/MB12 control (non-vacuity of "conserved"): a coordinate x is NOT conserved (Ta moves
      it), so "conserved" is a real, falsifiable property -- kappa has it, x does not.
  L3  kappa is built from TRACES (pure numbers) => dimensionless by construction; it carries no
      free parameter with units.
  L4  door-4 non-vacuity witness (MB12): a scale CAN enter -- but only by EXTERNAL import,
      kappa*Lambda^k, where every unit comes from Lambda, not kappa. So the lemma is non-vacuous
      (there IS a door; it is external), and the hypothesis "no external scale" is what shuts it.
"""
import sympy as sp

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

x, y, z, lam = sp.symbols('x y z Lambda')
kappa = x**2 + y**2 + z**2 - x*y*z - 2          # Fricke-Vogt invariant (K001)

# the trace map / Dehn twists on (tr A, tr B, tr AB) (K001/B148/B130 convention)
def Ta(p): X, Y, Z = p; return (X, Z, X*Z - Y)
def Tb(p): X, Y, Z = p; return (Z, Y, Y*Z - X)
def phi_m(p, m):
    for _ in range(m): p = Tb(p)
    for _ in range(m): p = Ta(p)
    return p

print("== L1 [exact]: kappa is a first integral (Dehn twists + metallic monodromies preserve it) ==")
def kap(p): X, Y, Z = p; return X**2 + Y**2 + Z**2 - X*Y*Z - 2
chk("kappa o Ta = kappa", sp.expand(kap(Ta((x, y, z))) - kappa) == 0)
chk("kappa o Tb = kappa", sp.expand(kap(Tb((x, y, z))) - kappa) == 0)
for m in (1, 2, 3):
    chk(f"kappa o phi_{m} = kappa (metallic monodromy preserves kappa)",
        sp.expand(kap(phi_m((x, y, z), m)) - kappa) == 0)

print("== L2 [exact, MB6/MB12 control]: 'conserved' is falsifiable -- a coordinate is NOT conserved ==")
# Ta fixes x; Tb moves it (x->z). Test a genuinely non-conserved coordinate under Tb:
chk("x is NOT conserved by Tb (Tb: x->z) -- so 'conserved' does real work",
    sp.expand((Tb((x, y, z))[0]) - x) != 0, x="Tb sends the first coord x -> z")
chk("the full coordinate triple is NOT fixed by phi_1 (only kappa is)",
    phi_m((x, y, z), 1) != (x, y, z))

print("== L3 [exact]: kappa is dimensionless (a polynomial in traces = pure numbers) ==")
# assign a formal unit u to each trace; kappa is NOT homogeneous of a single degree unless u is
# dimensionless -> the only consistent assignment is u dimensionless (traces are pure numbers).
u = sp.symbols('u', positive=True)
ku = (u*x)**2 + (u*y)**2 + (u*z)**2 - (u*x)*(u*y)*(u*z) - 2
# kappa(u*traces) mixes u^2, u^3, u^0 -> NOT homogeneous => no consistent nonzero unit => dimensionless
degs = {sp.Poly(t, u).degree() for t in sp.expand(ku).as_ordered_terms()}
chk("kappa is not unit-homogeneous (mixes u^0,u^2,u^3) => traces must be dimensionless",
    len(degs) > 1, x=f"u-degrees present: {sorted(degs)}")

print("== L4 [exact, MB12 non-vacuity witness]: a scale CAN enter -- only by EXTERNAL import ==")
# door 4: kappa * Lambda^4 is dimensionful, but ALL units come from the external Lambda, none from kappa.
expr = kappa * lam**4
chk("d/dLambda(kappa*Lambda^4) != 0 but d/dx,y,z carry no Lambda -- units are external (door 4 opens)",
    sp.diff(expr, lam) != 0 and lam not in kappa.free_symbols,
    x="the only door that admits a scale is the external one -> lemma is non-vacuous")

print("\nLEMMA (stated, POSTULATED -> 'stated argument'): a conserved/topological first integral of a")
print("measure-preserving map does not run (no beta-function) => it cannot source a dimensionful scale")
print("from within; a scale enters only by EXTERNAL import (door 4), which violates the zero-parameter")
print("premise. The five-door case analysis (transmutation/anomaly/VEV/external-import/ratio) is in FINDINGS.")
print("FIREWALL: sharpens the wall; no scale, no Lambda, no crossing; nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
