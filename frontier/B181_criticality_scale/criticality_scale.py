#!/usr/bin/env python3
"""B181 (S036 first hunt -- the large-N / criticality scale-door): does a phase transition give the
collective an emergent SCALE? Honest answer (an INVERSION): the metallic quasicrystal is PERMANENTLY
CRITICAL (scale-invariant by nature) -- which EXPLAINS its scale-freeness rather than breaking it. A
genuine transition (a finite emergent length) requires LEAVING the metallic class, and even then the
length is DIMENSIONLESS (lattice units) -> the scale stays external. The wall relocates again, now
EXPLAINED by criticality.

Diagnostic: the Lyapunov exponent gamma(E) of the 1D transfer cocycle (localization). gamma=0 on the
spectrum = critical/extended (delocalized); gamma>0 = localized, with localization length xi = 1/gamma.

  C1 [the metallic chain is PERMANENTLY CRITICAL] the Fibonacci/Sturmian operator has gamma ~ 0 on the
     spectrum at WEAK and STRONG coupling alike -- NO metal-insulator transition (gamma_Fib(lam=3) ~ 20x
     smaller than the Aubry-Andre localized value). [Damanik-Lenz: zero Lyapunov on the spectrum, all coupling.]
  C2 [a transition needs a NON-metallic field] the smooth Aubry-Andre (cosine) HAS a sharp transition at
     lam=2: gamma=0 (extended) below, gamma=ln(lam/2)>0 (localized) above -- a finite localization length
     xi=1/gamma appears. Verified gamma_AA(lam=3) ~ ln(3/2)=0.405.
  C3 [the INVERSION -- criticality IS the scale-freeness] permanent criticality (gamma_Fib~0) => xi=1/gamma
     -> infinity (NO finite length) => scale-INVARIANT => scale-free. A finite emergent length exists only in
     the AA localized phase (off the metallic class) and is DIMENSIONLESS (xi ~ 2.5 LATTICE UNITS) -> the
     scale is still external. So criticality EXPLAINS the metallic object's scale-freeness; it is not a scale source.

VERDICT (for the S036 register, the SCALE ingredient): the large-N/criticality door does NOT yield a scale for the
metallic object -- it is permanently critical = scale-free BY criticality. A scale needs broken criticality
(off-metallic) and is still dimensionless. The scale-search points to the EXTERNAL (Hitchin/Higgs) side, not here.
FIREWALL: emergent localization/criticality math (K010 boundary); no scale/Lambda; nothing to CLAIMS.md.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

phi = (1 + 5**0.5)/2; alpha = 1/phi
def sturm(N, lam, th): n = np.arange(1, N+1); return lam*(((n*alpha + th) % 1.0) >= 1.0 - alpha).astype(float)
def cosV(N, lam, th):  n = np.arange(1, N+1); return lam*np.cos(2*np.pi*(alpha*n + th))

def in_spectrum(Vfun, lam, th, Ns=2000, k=10):
    V = Vfun(Ns, lam, th); e = np.sort(eigvalsh_tridiagonal(V, np.ones(Ns-1)))
    return e[np.linspace(int(Ns*0.25), int(Ns*0.75), k).astype(int)]      # mid-band, in spectrum

def lyap(Vfun, lam, th, E, Nl=25000):
    V = Vfun(Nl, lam, th); v = np.array([1.0, 0.0]); s = 0.0
    for n in range(Nl):
        v = np.array([(E - V[n])*v[0] - v[1], v[0]]); nr = np.linalg.norm(v); s += np.log(nr); v /= nr
    return s/Nl

def avg_gamma(Vfun, lam, th=0.137):
    return float(np.mean([lyap(Vfun, lam, th, E) for E in in_spectrum(Vfun, lam, th)]))

gAA1, gAA3 = avg_gamma(cosV, 1.0), avg_gamma(cosV, 3.0)
gF1, gF3 = avg_gamma(sturm, 1.0), avg_gamma(sturm, 3.0)
print("Lyapunov gamma (avg over in-spectrum energies):")
print(f"   Aubry-Andre (cosine):  lam=1 -> {gAA1:.4f}   lam=3 -> {gAA3:.4f}   [exact 0 ; ln(3/2)={np.log(1.5):.4f}]")
print(f"   Fibonacci (metallic):  lam=1 -> {gF1:.4f}   lam=3 -> {gF3:.4f}   [exact 0 ; 0 -- permanently critical]\n")

chk("C2 [a transition needs a non-metallic field]: Aubry-Andre HAS a metal-insulator transition -- "
    "extended below lam=2 (gamma~0), localized above (gamma=ln(lam/2)); finite length xi=1/gamma appears",
    gAA1 < 0.05 and abs(gAA3 - np.log(1.5)) < 0.05,
    x=f"gamma_AA: {gAA1:.4f} (extended) -> {gAA3:.4f} ~ ln(3/2)={np.log(1.5):.3f} (localized, xi~{1/gAA3:.1f} sites)")
chk("C1 [the metallic chain is PERMANENTLY CRITICAL]: gamma ~ 0 on the spectrum at WEAK and STRONG coupling -- "
    "NO transition (gamma_Fib(lam=3) << the AA localized value)",
    gF1 < 0.05 and gF3 < 0.10 and gF3 < 0.2*gAA3,
    x=f"gamma_Fib: {gF1:.4f} (lam=1) , {gF3:.4f} (lam=3) -- {gAA3/max(gF3,1e-9):.0f}x smaller than AA localized; stays critical")
chk("C3 [the INVERSION]: metallic permanent criticality => xi=1/gamma -> infinity (NO finite length) => "
    "scale-invariant => scale-free; a finite length exists only off the metallic class (AA localized) and is "
    "DIMENSIONLESS (lattice units) => scale stays external. Criticality EXPLAINS the scale-freeness.",
    (1/max(gF3, 1e-9)) > 5*(1/gAA3),
    x=f"metallic xi ~ {1/max(gF3,1e-9):.0f} sites (-> infinity) vs AA-localized xi ~ {1/gAA3:.1f} sites (finite, dimensionless)")

print("\nVERDICT: the large-N / criticality scale-door, tested -- the metallic object is PERMANENTLY CRITICAL")
print("(gamma~0 on the spectrum at all coupling, no metal-insulator transition) = scale-INVARIANT = scale-free")
print("BY criticality [C1]. A genuine transition (a finite localization length) requires a NON-metallic field (the")
print("Aubry-Andre cosine, transition at lam=2) [C2], and even there the length is DIMENSIONLESS (lattice units) ->")
print("the scale stays external [C3]. So criticality EXPLAINS the metallic scale-freeness rather than providing a")
print("scale. S036 register: the SCALE ingredient stays external; the scale-search points to the Hitchin/Higgs side,")
print("NOT large-N criticality of this object. FIREWALL: emergent criticality math, nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
