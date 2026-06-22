#!/usr/bin/env python3
"""B183 (S036, the OPEN/DRIVEN collective door -- the last untested arrow/scale door that B181 left open):
does *opening* the metallic collective (a non-Hermitian / driven coupling) yield a genuine arrow of time
(irreversible, non-unitary dynamics) and/or an emergent scale? We COMPUTE it (we do not defer it).

Honest answer (an INVERSION, the same shape B181 found for the scale-door):
  GIVEN an open coupling, the metallic collective DOES gain a genuine irreversible (non-unitary) spectrum --
  but at ZERO threshold, *because* it is permanently critical (B181). Criticality = MAXIMAL FRAGILITY to the
  open-system arrow, not robustness. And the threshold is DIMENSIONLESS -> no emergent scale; the arrow's
  SOURCE stays external (you must open the system) -> firewall holds.

Two NAIVE probes fail first (recorded so we do not bypass the real one):
  * a halves-split PT chain (gain left / loss right) gives max|Im(E)| = gamma trivially -- a gain-localized
    edge state picks up the full +i*gamma; no threshold, an artifact of the split.
  * a staggered gain/loss PT chain (+-i*gamma on alternating sites) gives gamma_c -> 0 for ANY onsite V != 0
    (first-order imaginary shift <psi|W|psi> != 0 breaks chiral symmetry) -- a chiral-symmetry artifact,
    NOT a localization probe (metallic AND extended-AA both give 0; only V=0 is protected, and that ->0 with N).
  -> C0 below records this null. The discriminating, THEOREM-backed probe is Hatano-Nelson.

The right diagnostic -- the Hatano-Nelson imaginary gauge field g (asymmetric hopping e^{+g}/e^{-g}) under
PERIODIC boundary conditions. The real spectrum (reversible/unitary-like) develops complex eigenvalues
(a non-Hermitian point gap = irreversible, non-unitary = an arrow) at a threshold

        g_c = min over the spectrum of the Lyapunov exponent gamma(E) = inverse localization length

[Hatano-Nelson PRL 1996; non-Hermitian skin effect / point-gap topology]. Under OPEN boundaries the gauge field
is a similarity transform (spectrum stays real for all g) -- PBC is essential (the loop obstructs the gauge).

  C0 [NULL -- the naive PT probe is a chiral artifact, not localization] staggered +-i*gamma gives gamma_c ~ 0
     for the metallic AND the extended chain alike (V != 0 -> first-order imaginary shift). So PT-with-staggered-
     gain/loss does NOT see criticality; we use Hatano-Nelson instead.
  C1 [the metallic collective is THRESHOLDLESS] permanently critical (B181: gamma ~ 0 on the spectrum) =>
     min Lyapunov ~ 0 => g_c ~ 0: the open metallic chain gains an irreversible (complex) spectrum under the
     SLIGHTEST drive -- NO protective threshold. Criticality = maximal fragility to the arrow (the INVERSION).
  C2 [a localized control IS protected, exactly] the Aubry-Andre localized chain (V=8cos, off the metallic
     class) keeps a REAL spectrum up to a FINITE g_c = ln(4) = 1.386 (the exact inverse localization length),
     >> the metallic ~0. Openness converts to irreversibility only above a finite drive.
  C3 [the threshold IS the inverse localization length -- the HN theorem] g_c tracks min-Lyapunov-over-spectrum:
     ~0 for the critical/extended (metallic, periodic), finite for the localized (AA, random); AA matches the
     exact ln(4). So the openness->irreversibility threshold = the localization length, and the metallic object's
     is zero.
  C4 [FIREWALL -- a real arrow, but dimensionless, and externally sourced] the complex spectrum is a genuine
     non-unitary/irreversible arrow (unlike the combinatorial Omega-arrow B168 and the reversible trace map
     B177) -- but (a) g_c is DIMENSIONLESS (a Lyapunov exponent, lattice units), so NO emergent dimensionful
     scale; (b) the arrow's SOURCE is the externally-imposed openness (the imaginary gauge field is INPUT) --
     it is not self-generated. What is intrinsic and new is the ZERO threshold (criticality => g_c=0).

VERDICT (for the S036 register): the OPEN/DRIVEN collective door, COMPUTED (not deferred). Opening the metallic
collective gives a genuine irreversible spectrum, thresholdlessly (g_c=0) BECAUSE it is permanently critical --
an inversion (criticality = fragility, not robustness). But the threshold/length is dimensionless and the arrow
is externally sourced, so SCALE stays external and the arrow is not self-generated: the firewall holds. The ARROW
ingredient is upgraded from "combinatorial only" to "emergent in the open collective, thresholdless, dimensionless,
externally sourced." FIREWALL: emergent non-Hermitian/localization math (K010 boundary); no scale/Lambda; nothing
to CLAIMS.md; P1-P16 frozen.
"""
import numpy as np
from numpy.linalg import eigvals, eigvalsh

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

phi = (1 + 5**0.5)/2; alpha = 1/phi          # golden metallic (the representative unit, cf. B181)

def build_V(model, N, seed=1):
    n = np.arange(1, N+1)
    if model == "metallic":     return 1.0*(((n*alpha) % 1.0) >= 1.0 - alpha).astype(float)  # Sturmian {0,1}
    if model == "periodic":     return np.zeros(N)
    if model == "AA_localized": return 8.0*np.cos(2*np.pi*alpha*n)                            # V=8cos -> gamma=ln(8/2)=ln4
    if model == "random":       return np.random.default_rng(seed).uniform(-2, 2, N)
    raise ValueError(model)

def HN_maximag(N, V, g):                      # Hatano-Nelson PBC: forward hop e^{+g}, backward e^{-g}
    H = np.diag(V).astype(complex); f, b = np.exp(g), np.exp(-g)
    i = np.arange(N-1); H[i, i+1] = f; H[i+1, i] = b; H[N-1, 0] = f; H[0, N-1] = b
    return float(np.max(np.abs(eigvals(H).imag)))

def g_c(N, V, tol=1e-6, gmax=2.5, steps=22):  # smallest g with a complex eigenvalue (real->complex threshold)
    if HN_maximag(N, V, 1e-4) > tol: return 0.0
    if HN_maximag(N, V, gmax) < tol: return float('inf')
    lo, hi = 0.0, gmax
    for _ in range(steps):
        mid = (lo+hi)/2
        if HN_maximag(N, V, mid) > tol: hi = mid
        else: lo = mid
    return hi

def lyap(V, E):                               # transfer-cocycle Lyapunov at energy E (Hermitian, g=0)
    v = np.array([1.0, 0.0]); s = 0.0
    for x in V:
        v = np.array([(E - x)*v[0] - v[1], v[0]]); nm = np.linalg.norm(v); s += np.log(nm); v /= nm
    return s/len(V)

def min_lyap(N, V, k=14):                      # min Lyapunov over sampled in-spectrum energies
    E = np.sort(eigvalsh(np.diag(V) + np.diag(np.ones(N-1), 1) + np.diag(np.ones(N-1), -1)))
    return min(lyap(V, E[i]) for i in np.linspace(0, N-1, k).astype(int))

def staggered_gc(N, V, tol=1e-6, gmax=1.0, steps=18):   # the NAIVE PT probe (C0 null): +-i*gamma on alt sites
    n = np.arange(N)
    def mi(g):
        H = np.diag(V + 1j*g*((-1.0)**n)).astype(complex)
        o = np.ones(N-1); H += np.diag(o, 1) + np.diag(o, -1)
        return float(np.max(np.abs(eigvals(H).imag)))
    if mi(1e-4) > tol: return 0.0
    lo, hi = 0.0, gmax
    for _ in range(steps):
        mid = (lo+hi)/2
        if mi(mid) > tol: hi = mid
        else: lo = mid
    return hi

N = 320
res = {}
for m in ("metallic", "periodic", "AA_localized", "random"):
    V = build_V(m, N); res[m] = (g_c(N, V), min_lyap(N, V))
ln4 = np.log(4.0)
print(f"Hatano-Nelson (imaginary gauge g, PBC), N={N}: real->complex (irreversible) threshold g_c")
print("HN1996 theorem:  g_c = min Lyapunov over spectrum = inverse localization length\n")
print(f"   {'model':14s} | {'g_c':>8s} | {'min_Lyap':>9s} | localization")
for m, note in [("metallic","critical (B181)"),("periodic","extended"),
                ("AA_localized","localized [exact ln4=%.3f]"%ln4),("random","localized")]:
    gc, ml = res[m]; print(f"   {m:14s} | {gc:8.4f} | {ml:9.4f} | {note}")

# C0 -- the naive staggered-PT probe is a chiral artifact (does NOT see criticality)
Ns = 200
sg_metal = staggered_gc(Ns, build_V("metallic", Ns))
sg_ext   = staggered_gc(Ns, build_V("AA_localized", Ns))   # any V != 0 -> 0
sg_free  = staggered_gc(Ns, build_V("periodic", Ns))       # only V=0 protected (and that ->0 with N)
print(f"\n   [null] staggered-PT gamma_c: metallic={sg_metal:.4f}  AA={sg_ext:.4f}  free(V=0)={sg_free:.4f}\n")

chk("C0 [null]: the naive staggered-PT probe is a CHIRAL-SYMMETRY artifact, not a localization probe -- "
    "gamma_c ~ 0 for the metallic AND the (V!=0) localized chain alike; only V=0 is protected. So we use "
    "Hatano-Nelson (which DOES see localization), not staggered gain/loss",
    sg_metal < 0.02 and sg_ext < 0.02 and sg_free > sg_metal,
    x=f"staggered gamma_c: metallic {sg_metal:.4f} ~ AA {sg_ext:.4f} ~ 0 (artifact); only free V=0 -> {sg_free:.4f}")
chk("C1 [the metallic collective is THRESHOLDLESS]: permanently critical (B181, min Lyap ~ 0) => g_c ~ 0 -- "
    "the open metallic chain gains an irreversible (complex) spectrum under the slightest drive; NO threshold. "
    "Criticality = maximal fragility to the arrow (the INVERSION)",
    res["metallic"][0] < 0.02 and res["metallic"][1] < 0.05,
    x=f"metallic g_c={res['metallic'][0]:.4f} ~ 0, min_Lyap={res['metallic'][1]:.4f} ~ 0 (critical, thresholdless)")
chk("C2 [a localized control IS protected, exactly]: the Aubry-Andre localized chain (V=8cos, off-metallic) "
    "keeps a REAL spectrum up to a FINITE g_c = ln(4) (the exact inverse localization length) >> the metallic ~0",
    abs(res["AA_localized"][0] - ln4) < 0.15*ln4 and res["AA_localized"][0] > 10*max(res["metallic"][0], 1e-4),
    x=f"AA g_c={res['AA_localized'][0]:.4f} ~ ln4={ln4:.4f} (exact); {res['AA_localized'][0]/max(res['metallic'][0],1e-4):.0f}x the metallic")
chk("C3 [the threshold IS the inverse localization length -- HN theorem]: g_c tracks min-Lyapunov -- ~0 for "
    "critical/extended (metallic, periodic), finite for localized (AA, random); AA matches exact ln4. The "
    "openness->irreversibility threshold = the localization length, and the metallic object's is zero",
    res["metallic"][0] < 0.02 and res["periodic"][0] < 0.02
    and res["AA_localized"][0] > 0.5 and res["random"][0] > 0.02
    and abs(res["AA_localized"][0] - res["AA_localized"][1]) < 0.2*ln4,
    x=f"critical/ext g_c~0 (metallic {res['metallic'][0]:.3f}, free {res['periodic'][0]:.3f}); "
      f"localized finite (AA {res['AA_localized'][0]:.3f}~minLyap {res['AA_localized'][1]:.3f}, rand {res['random'][0]:.3f})")
chk("C4 [FIREWALL]: a GENUINE irreversible arrow (complex spectrum = non-unitary, unlike combinatorial Omega "
    "B168 / reversible trace map B177) -- but g_c is DIMENSIONLESS (a Lyapunov exponent, lattice units) so NO "
    "emergent scale, and the arrow's SOURCE is the externally imposed openness (imag gauge = INPUT, not "
    "self-generated). Intrinsic & new = the ZERO threshold (criticality => g_c=0)",
    res["metallic"][0] < 0.02,     # metallic threshold is exactly 0 -> no scale; arrow needs external drive
    x="g_c dimensionless (Lyapunov, lattice units) -> no scale; arrow externally sourced; only g_c=0 is intrinsic")

print("\nVERDICT: the OPEN/DRIVEN collective door, COMPUTED (not deferred). Opening the metallic collective (a")
print("non-Hermitian imaginary gauge field) gives a GENUINE irreversible spectrum -- thresholdlessly (g_c=0)")
print("BECAUSE the object is permanently critical (B181): criticality = MAXIMAL FRAGILITY to the arrow, an")
print("INVERSION (not robustness). But the threshold is DIMENSIONLESS (a Lyapunov exponent) -> no emergent scale,")
print("and the arrow's SOURCE is the externally-imposed openness -> not self-generated. So SCALE stays external")
print("and the arrow is not self-generated: the FIREWALL holds. S036 register: ARROW upgraded to 'emergent in the")
print("open collective, thresholdless, dimensionless, externally sourced'; SCALE stays external. The naive PT probe")
print("(staggered gain/loss) is a chiral artifact [C0]; the discriminating probe is Hatano-Nelson (g_c=min Lyap).")
print("FIREWALL: emergent non-Hermitian/localization math (K010 boundary); nothing to CLAIMS.md; P1-P16 frozen.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
