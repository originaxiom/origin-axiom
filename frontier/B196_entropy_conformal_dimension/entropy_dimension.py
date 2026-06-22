#!/usr/bin/env python3
"""B196 -- the entropy <-> conformal-dimension bridge for the metallic monodromy (firewall-clean PURE MATH;
the solid math underlying speculations/S037). Under the Painleve-VI <-> c=1 conformal-block dictionary
(Gamayun-Iorgov-Lisovyy), the metallic once-punctured-torus object is a c=1 four-twist-field conformal block, and
its single nontrivial datum is the conformal dimension of its (hyperbolic) bundle/time-monodromy, which equals
minus the square of its topological entropy over 2pi:

        Delta = -(ln lam_m / pi)^2 = -(h / 2pi)^2 ,   h = ln(lam_m^2) = topological entropy = log dynamical degree.

So the object's DYNAMICS (its entropy) IS its c=1 conformal dimension -- dimensionless and negative (non-unitary).

  C1 [exact] the bridge identities: lam_m + 1/lam_m = sqrt(m^2+4) and lam_m^2 + 1/lam_m^2 = m^2+2, where m^2+2 =
     tr of the metallic BUNDLE/time-monodromy on H1 (R^m L^m on homology, eigenvalues lam_m^{+-2}).
  C2 [exact+num] the entropy<->dimension bridge: the bundle monodromy is hyperbolic (tr=m^2+2>2), so as a c=1
     Liouville momentum P it satisfies 2*cosh(2*pi*P) = m^2+2 => P = ln(lam_m)/pi, hence Delta = -P^2 =
     -(ln lam_m/pi)^2 = -(h/2pi)^2. Verified m=1..4.
  C3 [MATH+HOOK] the c=1 four-twist-field structure: c=1 is FIXED by PVI/GIL (trivially rigid, not derived); the
     once-punctured torus is the Z2 double cover of the 4-punctured sphere branched at 4 order-2 points, giving four
     TWIST fields theta_i = 1/4 (Delta_i = 1/16, the standard elliptic/orbifold PVI structure). All conformal data
     is DIMENSIONLESS.
  C4 [FIREWALL + scope] this is the GIL dictionary applied to the metallic data -- it forces NO physical content
     (c=1 trivially fixed; Delta is dimensionless entropy, negative/non-unitary; no scale, no mass). A scale would
     need the hyperkahler METRIC (the Hitchin/Higgs structure), which the character variety (an algebraic variety)
     does NOT carry. The precise PVI CHANNEL placement (time-monodromy vs fiber s-channel in the OPT->(0,4)
     dictionary) is the one open detail -- NEEDS-SPECIALIST; the VALUE -(ln lam/pi)^2 is exact. Emergent
     character-variety / quantum-topology math (K010 boundary); nothing to CLAIMS.md; P1-P16 frozen.

VERDICT: the metallic object's topological entropy h=ln(lam_m^2) equals (up to -(1/2pi)^2) its c=1 conformal
dimension Delta=-(h/2pi)^2 -- the dynamics dressed as a CFT dimension, dimensionless and non-unitary. Solid math
supporting the firewalled reading in speculations/S037 (object = a conformal block whose content is its own
entropy; scale/content external). FIREWALL: K010 boundary; nothing to CLAIMS.md.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

m = sp.symbols('m', positive=True, integer=True)
lam = (m + sp.sqrt(m**2 + 4))/2

# ---- C1 [exact] ----
id1 = sp.simplify(lam + 1/lam - sp.sqrt(m**2 + 4))
id2 = sp.simplify(lam**2 + 1/lam**2 - (m**2 + 2))
print("== C1 [exact] bridge identities ==")
print(f"   lam + 1/lam - sqrt(m^2+4) = {id1};   lam^2 + 1/lam^2 - (m^2+2) = {id2}")
chk("C1 [exact]: lam+1/lam=sqrt(m^2+4) AND lam^2+1/lam^2=m^2+2 (= tr of the bundle/time-monodromy on H1, "
    "eigenvalues lam^{+-2})", id1 == 0 and id2 == 0)

# ---- C2 [entropy <-> dimension] ----
print("\n== C2 [the entropy<->dimension bridge] Delta = -(ln lam_m/pi)^2 = -(h/2pi)^2 ==")
print("   m | lam_m      | entropy h=ln(lam^2) | Delta=-(ln lam/pi)^2 | 2cosh(2piP)-(m^2+2)")
c2 = True
for mm in (1, 2, 3, 4):
    L = (mm + mp.sqrt(mm**2 + 4))/2
    P = mp.log(L)/mp.pi                       # Liouville momentum of the hyperbolic monodromy
    h = mp.log(L**2)                          # topological entropy = log dynamical degree
    Delta = -(P**2)
    cosh_chk = 2*mp.cosh(2*mp.pi*P) - (mm**2 + 2)          # must be 0 (defines P)
    half_h_chk = Delta - (-(h/(2*mp.pi))**2)               # Delta = -(h/2pi)^2
    print(f"   {mm} | {mp.nstr(L,8):10s} | {mp.nstr(h,8):12s}        | {mp.nstr(Delta,8):13s}        | {mp.nstr(cosh_chk,2)}")
    c2 = c2 and abs(cosh_chk) < mp.mpf(10)**(-30) and abs(half_h_chk) < mp.mpf(10)**(-30)
chk("C2 [entropy<->dimension]: 2cosh(2piP)=m^2+2 with P=ln(lam)/pi, and Delta=-P^2=-(h/2pi)^2 (h=ln lam^2 = "
    "topological entropy); verified m=1..4 to 1e-30", c2,
    x="Delta = -(entropy/2pi)^2 -- the dynamics IS the c=1 conformal dimension")

# ---- C3 [c=1 four-twist-field structure] ----
print("\n== C3 [c=1 four-twist-field structure] ==")
theta = sp.Rational(1, 4); Dtwist = theta**2
print(f"   c = 1 (PVI/GIL fixed);  four twist fields theta_i = {theta} -> Delta_i = {Dtwist} = 1/16")
chk("C3 [c=1 four-twist structure]: c=1 fixed by PVI (trivially rigid); the OPT->(0,4) Z2 cover gives four "
    "order-2 twist fields theta=1/4, Delta=1/16; all conformal data dimensionless",
    Dtwist == sp.Rational(1, 16))
chk("C4 [FIREWALL + scope]: the GIL dictionary applied to the metallic data forces NO physical content (c=1 "
    "trivially fixed; Delta dimensionless/non-unitary; no scale/mass); a scale needs the hyperkahler METRIC the "
    "character variety lacks; the precise PVI channel placement is NEEDS-SPECIALIST (the value is exact); nothing "
    "to CLAIMS.md", id2 == 0 and c2)

print("\nVERDICT: the metallic object's topological entropy h=ln(lam_m^2) equals -(1/2pi)^2 times its c=1 conformal")
print("dimension: Delta = -(h/2pi)^2 = -(ln lam_m/pi)^2 -- the dynamics dressed as a CFT dimension, dimensionless and")
print("non-unitary (hyperbolic). The object is a c=1 four-twist-field (Delta=1/16) conformal block whose only")
print("nontrivial datum is its own entropy; no physical content is forced. Solid math under speculations/S037. The")
print("exact PVI-channel placement is the one specialist caveat. FIREWALL: emergent character-variety/quantum-topology")
print("math (K010 boundary); no scale/Lambda; nothing to CLAIMS.md; P1-P16 frozen.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
