#!/usr/bin/env python3
"""GC-1 mechanism piece: compute the omega-Bianchi (d=3) orbifold volume via the
Humbert/Dedekind-zeta formula, INDEPENDENTLY of snappy's manifold-volume routine,
and compare Vol(m004) and V_reg = Vol(m004)/2 to it.

Formula (Humbert 1919; see e.g. Elstrodt-Grunewald-Mennicke "Groups Acting on
Hyperbolic Space" Thm 3.2, or Maclachlan-Reid Thm 11.1.3):
    Vol(H^3 / PSL(2,O_K)) = |d_K|^{3/2} * zeta_K(2) / (4 pi^2)
for K = Q(sqrt(-d)) imaginary quadratic of discriminant d_K, with
    zeta_K(s) = zeta(s) * L(s, chi_{d_K})
the Dedekind zeta function factoring as Riemann zeta times the quadratic
Dirichlet L-function of the field's character.

For K = Q(sqrt(-3)): d_K = -3, chi_{-3} is the unique non-trivial character mod 3
(chi(1)=1, chi(2)=-1, chi(0)=0), computed here via the Hurwitz-zeta split
    L(s,chi_{-3}) = 3^{-s} [ zeta(s,1/3) - zeta(s,2/3) ]
which mpmath's zeta(s, a) (Hurwitz zeta) gives directly, at 50 dps -- no
special number-theory library, no reuse of og3_volume_spectrum.py.

PGL(2,O_3) = PSL(2,O_3) since O_3^* = {+-1,+-omega,+-omega^2} has NO element of
order making [O_K^*:{+-1}] relevant to non-torsion index here -- actually the
index [PGL:PSL] for imaginary quadratic O_K is 1 iff -1 is a square mod units...
we do NOT assume this; we report BOTH Vol(PSL2(O_3)-orbifold) and note the
PGL/PSL distinction explicitly (see printed caveat).
"""
import mpmath as mp
mp.mp.dps = 50

def dirichlet_L_chi_minus3(s):
    """L(s, chi_{-3}) via Hurwitz zeta split mod 3 (chi_{-3}(1)=+1, chi_{-3}(2)=-1)."""
    return mp.mpf(3) ** (-s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))

def dedekind_zeta_Qsqrtm3(s):
    return mp.zeta(s) * dirichlet_L_chi_minus3(s)

zK2 = dedekind_zeta_Qsqrtm3(2)
dK = 3
Vol_PSL2O3 = mp.mpf(dK) ** mp.mpf('1.5') * zK2 / (4 * mp.pi ** 2)
print("zeta_K(2) for K=Q(sqrt(-3)):", zK2)
print("Vol(H^3 / PSL(2,O_3))  [Humbert formula, independent of snappy]:", Vol_PSL2O3)

# Independent literature cross-check: this number is well known to equal
# Vol(m004)/24 in some normalizations (m004 has an order-12 orientation-preserving
# symmetry group and PGL(2,O_3)/PSL2 relation doubles it in others) -- we do NOT
# assert the ratio in advance; we COMPUTE it below against our own high-precision
# snappy volume of m004.
import snappy
V0 = mp.mpf(str(snappy.Manifold("m004").high_precision().volume()).replace(" ", ""))
print("Vol(m004) [snappy high_precision, independent recompute]:", V0)
ratio_full = V0 / Vol_PSL2O3
print("Vol(m004) / Vol(PSL2(O_3)-orbifold) =", ratio_full)
print("  -> nearest integer:", mp.nint(ratio_full), " residual:", ratio_full - mp.nint(ratio_full))

Vreg = V0 / 2
ratio_reg = Vreg / Vol_PSL2O3
print("V_reg=Vol(m004)/2 / Vol(PSL2(O_3)-orbifold) =", ratio_reg)
print("  -> nearest integer:", mp.nint(ratio_reg), " residual:", ratio_reg - mp.nint(ratio_reg))

# Also try PGL(2,O_3) = index-2 extension in some conventions -> half the volume
Vol_PGL2O3_half = Vol_PSL2O3 / 2
ratio_pgl = V0 / Vol_PGL2O3_half
print("Vol(m004) / (Vol(PSL2O3)/2) [if PGL orbifold has half PSL orbifold's volume] =", ratio_pgl,
      " -> nearest int:", mp.nint(ratio_pgl))
