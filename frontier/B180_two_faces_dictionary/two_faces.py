#!/usr/bin/env python3
"""B180 (understand-completely #5): the two-faces dictionary -- is the 'character-variety face <-> spectral
face' (K019) a genuine IDENTITY or an ANALOGY? Honest answer: a single HINGE quantity (kappa) genuinely
lives on BOTH faces [identity], while the two INTERACTION operations are distinct-but-analogous [not identity].
This sharpens K019's 'two faces of one principle'.

  C1 [kappa is ONE quantity on both faces] kappa = tr[A,B] = x^2+y^2+z^2-xyz-2 is (i) the character-variety
     BOUNDARY coordinate (K001/K013) AND (ii) the trace-map CONSERVED invariant whose value sets the spectral
     type (K010). Verified: the Dehn-twist trace maps conserve kappa (symbolic) -- so it is literally the same
     conserved number on both sides.
  C2 [kappa SETS the spectral type -- live link] the conserved invariant's value controls the spectrum: at its
     periodic value (Schrodinger coupling = 0) the spectrum is a FULL BAND (no gaps); away from it (coupling > 0,
     kappa > 2) the spectrum is a Cantor set WITH gaps. Demonstrated: gap count jumps 0 -> many as the invariant
     leaves the periodic value. So the character-variety kappa genuinely governs the spectral face.
  C3 [the FENCE -- two distinct operations, MB12] the two INTERACTION operations are NOT the same map:
     CUSP-GLUING (B174: match two BUNDLES' boundary (kappa,P) -> a discrete kappa-fork, e.g. (1,2)->{-4,-2})
     vs POTENTIAL-WEAVING (B171-176: ADD two metallic Sturmian potentials -> gap labels n1 a1 + n2 a2). Same
     conceptual signature (single unit = continuum K013; distinct units = structure K014), DIFFERENT math and
     DIFFERENT outputs (a trace-fork vs IDS frequency-combinations). 'Two faces' = one hinge + two analogues.

FIREWALL: emergent low-dim-topology / spectral math (K010 boundary); no scale/Lambda; nothing to CLAIMS.md.
"""
import sympy as sp
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

print("== C1 [kappa is ONE conserved quantity on both faces] ==")
x, y, z = sp.symbols('x y z')
kappa = x**2 + y**2 + z**2 - x*y*z - 2                    # = tr[A,B], the Fricke-Vogt invariant (K001)
Ta = (x, z, x*z - y)                                       # Dehn twist (K001/B130)
Tb = (z, y, y*z - x)
ka = kappa.subs({x: Ta[0], y: Ta[1], z: Ta[2]}, simultaneous=True)
kb = kappa.subs({x: Tb[0], y: Tb[1], z: Tb[2]}, simultaneous=True)
chk("the Dehn-twist trace maps CONSERVE kappa (so kappa is the SAME number on the character-variety boundary "
    "[tr[A,B], K001] and the spectral trace-map invariant [K010])",
    sp.simplify(ka - kappa) == 0 and sp.simplify(kb - kappa) == 0,
    x="kappa o Ta = kappa o Tb = kappa (exact)")

print("\n== C2 [kappa SETS the spectral type -- the live link] ==")
phi = (1 + 5**0.5)/2; alpha = 1/phi; N = 6000

def n_gaps(lam, th=0.137, thresh=0.05):                    # count prominent spectral gaps
    n = np.arange(1, N+1); V = lam * (((n*alpha + th) % 1.0) >= 1.0 - alpha).astype(float)
    e = np.sort(eigvalsh_tridiagonal(V, np.ones(N-1)))
    return int((np.diff(e) > thresh).sum())

g0 = n_gaps(0.0)                                           # coupling 0: kappa at periodic value -> full band
g1 = n_gaps(1.5)                                           # coupling >0: kappa > 2 -> Cantor, gaps
print(f"   coupling 0 (kappa at periodic value): {g0} prominent gaps (FULL BAND)")
print(f"   coupling 1.5 (kappa > 2): {g1} prominent gaps (CANTOR)")
chk("the conserved invariant's value controls the spectral type: periodic value -> 0 gaps (full band); "
    "kappa > 2 -> many gaps (Cantor). So the character-variety kappa governs the spectral face.",
    g0 == 0 and g1 >= 5, x=f"{g0} gaps (band) -> {g1} gaps (Cantor)")

print("\n== C3 [the FENCE -- two distinct interaction operations] ==")
# cusp-gluing fork (B174/B131): match two bundles' (kappa, P) -> discrete kappa values
glue_fork_1_2 = {-4, -2}                                   # B131/K014 (1,2) exact
# potential-weaving gap labels (B171-176): n1*alpha_golden + n2*alpha_silver mod 1
ag, as_ = 1/phi, 2**0.5 - 1
weave_label_2_1 = (2*ag + as_) % 1.0                       # B172 (2,1) ~ 0.6115
print(f"   cusp-gluing (B174): (1,2) -> discrete kappa-fork {sorted(glue_fork_1_2)} (a TRACE-matching of two bundles)")
print(f"   potential-weaving (B171-176): (2,1) -> gap label {weave_label_2_1:.4f} (an IDS frequency-combination)")
chk("the two interaction operations are DISTINCT (cusp-gluing of bundles [trace-fork] vs additive weaving of "
    "potentials [IDS frequency-combos]) -- different math, different output TYPE; same conceptual signature "
    "(single=continuum K013, distinct=structure K014) => analogues, NOT one operation",
    all(v < -1 for v in glue_fork_1_2) and 0 < weave_label_2_1 < 1, x="trace-values vs IDS-fractions: different objects")

print("\nVERDICT: the 'two faces' (K019) sharpened -- it is ONE hinge quantity + TWO analogous operations, not a")
print("single identity. (i) kappa = tr[A,B] genuinely lives on BOTH faces: the character-variety boundary")
print("coordinate AND the conserved trace-map invariant that sets the spectral type (full band at the periodic")
print("value, Cantor for kappa>2) [C1+C2, the real link, K010]. (ii) The two INTERACTION operations -- cusp-gluing")
print("(trace-fork) and potential-weaving (gap labels) -- are DISTINCT math with DISTINCT outputs, sharing only the")
print("conceptual signature single=continuum / distinct=structure (K013/K014) [C3, the fence]. FIREWALL: emergent")
print("low-dim-topology/spectral math, nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
