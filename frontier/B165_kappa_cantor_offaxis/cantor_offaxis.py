#!/usr/bin/env python3
"""B165 (P2a of Masterplan II) -- toward the off-axis (kappa<2) Cantor THEOREM.

B163 showed the kappa<2 (non-Hermitian/PT) spectrum is totally disconnected via the MST max-gap.
This stage delivers the honest P2a outcome: (i) D0 [exact] the trace-map/non-escaping-set framing;
(ii) D1 [num] EXTEND B163's WORKING MST-max-gap diagnostic to multiple seeds (golden/silver/bronze)
-- the disconnectedness is seed-robust; (iii) the CONDITIONAL THEOREM (the reduction) + NEEDS-SPECIALIST.

VERIFY-DON'T-TRUST RECORD: two ALTERNATIVE diagnostics were tried and FAILED to cleanly separate
Cantor from band, so they are NOT used (recorded so they are not re-attempted):
  - eps-component-count at a fixed fraction of the diameter: the KNOWN-Cantor control was FLAT
    (4,4,4) -- bands merge at that scale; it does not track disconnectedness.
  - a naive trace-map Jacobian "domination" ratio: contaminated by ESCAPING orbits (the kappa=2
    non-hyperbolic control also gave large ratios) -- it measures generic escape, not bounded-set
    hyperbolicity. (Real hyperbolicity evidence needs the bounded set, the open NEEDS-SPECIALIST step.)
B163's MST-max-gap remains the one clean numerical diagnostic; the off-axis THEOREM is NEEDS-SPECIALIST.
FIREWALL: spectral math; no scale/Lambda; nothing to CLAIMS.md.
"""
import numpy as np
import sympy as sp

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

# ---- D0 [exact]: the trace map conserves the Fricke-Vogt invariant ----
x, y, z = sp.symbols('x y z')
Tmap = (2*x*y - z, x, y)
I = lambda a, b, c: a**2 + b**2 + c**2 - 2*a*b*c - 1
print("== D0 [exact]: trace map T=(2xy-z,x,y) conserves I (spectrum = its non-escaping set) ==")
chk("I(T) - I = 0", sp.expand(I(*Tmap) - I(x, y, z)) == 0)

# ---- machinery (reused from B163) ----
def metallic_word(n, m):
    sub = 'a'*m + 'b'                                   # a -> a^m b, b -> a
    s = {-1: "b", 0: "a"}
    for k in range(1, n+1):
        s[k] = ''.join(sub if c == 'a' else 'a' for c in s[k-1])
    return s[n]
def H_eig(word, lam, periodic=True):
    L = len(word); V = np.array([lam if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.zeros((L, L), dtype=complex); np.fill_diagonal(H, V)
    i = np.arange(L-1); H[i, i+1] = 1.0; H[i+1, i] = 1.0
    if periodic: H[0, L-1] = 1.0; H[L-1, 0] = 1.0
    return np.linalg.eigvals(H)
def mst_max_gap_over_diam(ev):                          # the B163 diagnostic (the clean one)
    P = np.c_[ev.real, ev.imag]; n = len(P)
    intree = np.zeros(n, bool); mind = np.full(n, np.inf); mind[0] = 0.0; edges = np.empty(n)
    for t in range(n):
        u = int(np.argmin(np.where(intree, np.inf, mind))); edges[t] = mind[u]; intree[u] = True
        d = np.sqrt(((P - P[u])**2).sum(1)); upd = (~intree) & (d < mind); mind[upd] = d[upd]
    diam = np.hypot(ev.real.max()-ev.real.min(), ev.imag.max()-ev.imag.min())
    return float(edges[1:].max())/float(diam)

print("\n== D1 [num]: extend the WORKING MST max-gap diagnostic to golden/silver/bronze (seed-robust) ==")
# the bound varies with substitution length; use comparable depths per seed. lam=2i => kappa=-2.
for m, depths in [(1, (13, 15)), (2, (5, 6)), (3, (4, 5))]:
    gaps = [mst_max_gap_over_diam(H_eig(metallic_word(k, m), 2.0j)) for k in depths]
    band = mst_max_gap_over_diam(H_eig(metallic_word(depths[-1], m), 0.0+0j))   # kappa=2 band control
    chk(f"m={m} (metallic): kappa=-2 max-gap/diam persistent & >> kappa=2 band ({band:.4f}->0)",
        gaps[-1] > 0.08 and gaps[-1] > 5*band, x=f"kappa=-2 gaps {['%.3f'%g for g in gaps]} vs band {band:.4f}")

print("\n== (recorded NEGATIVE) the two alternative diagnostics that did NOT separate Cantor from band ==")
print("   - eps-component-count (fixed 5% diameter): known-Cantor control FLAT [4,4,4] -> does NOT track it.")
print("   - naive DT 'domination' ratio: kappa=2 non-hyperbolic control also large -> measures ESCAPE,")
print("     not bounded-set hyperbolicity. Both discarded; B163's MST max-gap is the clean diagnostic.")

print("\nCONDITIONAL THEOREM (the P2a contribution): the kappa<2 spectrum = the non-escaping set of the")
print("complexified trace map; IF that map is uniformly hyperbolic on its non-escaping set (a complex")
print("horseshoe) THEN the spectrum is a Cantor set. The hypothesis is supported numerically (B163 + D1,")
print("3 seeds) but the off-axis uniform-hyperbolicity proof is the one open step -- NEEDS-SPECIALIST (no")
print("off-axis ground truth; non-normal transfer matrices; Damanik-Gorodetski is Hermitian-kappa>2 only).")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
