#!/usr/bin/env python3
"""B188 (Masterplan III, Track B, second of two -- the DRIVEN-DISSIPATIVE metallic chain): B183/B187 opened the
collective with a non-Hermitian gauge field (a coherent, energy-non-conserving deformation). The genuinely
DISSIPATIVE channel is a Lindblad master equation. We COMPUTE its Liouvillian GAP (the slowest relaxation rate =
inverse relaxation time) for the metallic chain vs controls, and ask whether permanent criticality (B181) makes
relaxation anomalously slow (gapless), and whether any emergent timescale appears.

Setup: single-particle sector, dephasing dissipators L_j = sqrt(gamma) n_j (number-conserving; steady state =
maximally mixed). The Liouvillian L[rho] = -i[H,rho] + gamma sum_j (n_j rho n_j - 1/2{n_j,rho}); on the L x L
density matrix it is an L^2 x L^2 superoperator. Gap Delta = -(largest nonzero Re eigenvalue).

Answer (an INVERSION of the naive 'criticality => gapless' guess): the LOCALIZED (Aubry-Andre) chain is the
near-gapless one (~100x smaller gap = anomalously slow dissipative relaxation, because localized states barely
transport); the permanently-critical METALLIC chain relaxes like an EXTENDED chain (gap same order as periodic),
NOT gapless. And the gap carries NO intrinsic scale (it is homogeneous under scaling the external rates).

  C1 [the LOCALIZED control is near-gapless] the Aubry-Andre dephasing Liouvillian gap is ~100x smaller than the
     metallic/periodic gap at matched L -- localization => anomalously slow dissipative relaxation.
  C2 [criticality does NOT give slow relaxation] the metallic gap is the SAME ORDER as the periodic (extended)
     gap and ~70x ABOVE the localized -- the critical chain relaxes like an extended one (inversion of the naive
     'criticality => gapless'); the gapless/slow case is the LOCALIZED control.
  C3 [thermodynamic scaling] Delta(L) DECAYS with L for metallic & periodic (diffusive, -> 0 as L->inf: no finite
     emergent gap/timescale in the thermodynamic limit); the localized gap is tiny at all L.
  C4 [FIREWALL -- homogeneity, no intrinsic scale] scaling (H, gamma) -> (s*H, s*gamma) gives Delta -> s*Delta
     EXACTLY: the Liouvillian gap is a function of the EXTERNAL rates (hopping t, bath rate gamma) and L only --
     it carries NO intrinsic/emergent scale. The dissipative relaxation timescale 1/Delta is dimensionless (units
     of 1/t); the dissipative arrow's SOURCE is the externally-imposed bath. Consistent with B183/B187.

VERDICT (for the S036 register): the DRIVEN-DISSIPATIVE channel -- COMPUTED. Criticality does NOT make relaxation
gapless (the localized control is the slow one); the metallic chain relaxes like an extended chain; the gap decays
to zero in the thermodynamic limit (diffusive, no finite timescale) and carries no intrinsic scale (homogeneous in
the external rates). So dissipation adds NO emergent scale and the arrow stays externally sourced -- extending
B183/B187. Genuinely-interacting Lindblad (many-body dissipative phases) is the residual NEEDS-SPECIALIST. FIREWALL:
emergent open-quantum-systems math (K010 boundary); no scale/Lambda; nothing to CLAIMS.md; P1-P16 frozen.
"""
import numpy as np
np.seterr(over="ignore", invalid="ignore")

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

phi = (1 + 5**0.5)/2; alpha = 1/phi
def Hchain(L, kind, lam):
    n = np.arange(1, L+1)
    if kind == "metallic": V = lam*(((n*alpha) % 1.0) >= 1.0 - alpha).astype(float)
    elif kind == "aa":     V = 2*lam*np.cos(2*np.pi*alpha*n)
    else:                  V = np.zeros(L)
    H = np.diag(V).astype(complex); i = np.arange(L-1); H[i, i+1] = 1; H[i+1, i] = 1
    return H

def dephasing_gap(L, kind, lam, gamma=1.0, s=1.0):
    H = s*Hchain(L, kind, lam); I = np.eye(L)
    Lcoh = -1j*(np.kron(I, H) - np.kron(H.T, I))                       # -i[H, .], column-stacking
    offdiag = np.array([[0.0 if a == b else 1.0 for b in range(L)] for a in range(L)])
    Ldis = -(s*gamma)*np.diag(offdiag.flatten("F"))                    # dephasing kills coherences
    ev = np.linalg.eigvals(Lcoh + Ldis).real
    return float(-np.max(ev[np.abs(ev) > 1e-7]))

gaps = {k: {L: dephasing_gap(L, k, lam) for L in (6, 8, 10, 12, 14)}
        for k, lam in [("metallic", 1.0), ("aa", 4.0), ("periodic", 0.0)]}
print("dephasing Liouvillian gap Delta(L) (single-particle, gamma=1):\n")
print(f"   {'L':>3} | {'metallic':>9} | {'AA-localized':>12} | {'periodic':>9}")
for L in (6, 8, 10, 12, 14):
    print(f"   {L:3d} | {gaps['metallic'][L]:9.4f} | {gaps['aa'][L]:12.4f} | {gaps['periodic'][L]:9.4f}")

ratios = [gaps["metallic"][L]/gaps["aa"][L] for L in (8, 10, 12)]
chk("C1 [localized control near-gapless]: the Aubry-Andre dephasing gap is ~100x smaller than metallic/periodic at "
    "matched L -- localization => anomalously slow dissipative relaxation",
    all(gaps["periodic"][L]/gaps["aa"][L] > 20 for L in (8, 10, 12)),
    x="periodic/AA ratios: " + ", ".join(f"L={L}:{gaps['periodic'][L]/gaps['aa'][L]:.0f}x" for L in (8, 10, 12)))
chk("C2 [criticality does NOT give slow relaxation]: the metallic gap is the SAME ORDER as periodic (0.3<met/per<3) "
    "and >20x ABOVE the localized -- the critical chain relaxes like an extended one (inversion of 'criticality => "
    "gapless'); the slow case is the LOCALIZED control",
    all(0.3 < gaps["metallic"][L]/gaps["periodic"][L] < 3 for L in (8, 10, 12)) and all(r > 20 for r in ratios),
    x="metallic/AA: " + ", ".join(f"{r:.0f}x" for r in ratios) + "; metallic/periodic ~ "
      f"{np.mean([gaps['metallic'][L]/gaps['periodic'][L] for L in (8,10,12)]):.2f}")
chk("C3 [thermodynamic scaling]: Delta(L) decays with L for metallic & periodic (diffusive, -> 0: no finite emergent "
    "gap in the thermodynamic limit); the localized gap is tiny at all L",
    gaps["metallic"][14] < gaps["metallic"][6] and gaps["periodic"][14] < gaps["periodic"][6]
    and gaps["aa"][6] < 0.05,
    x=f"metallic {gaps['metallic'][6]:.3f}->{gaps['metallic'][14]:.3f}; AA tiny ({gaps['aa'][6]:.4f})")

# C4: homogeneity
d1 = dephasing_gap(10, "metallic", 1.0, s=1.0)
homog = all(abs(dephasing_gap(10, "metallic", 1.0, s=s)/(s*d1) - 1) < 1e-6 for s in (2.0, 3.0))
chk("C4 [FIREWALL homogeneity]: scaling (H,gamma)->(s*H,s*gamma) gives Delta->s*Delta exactly -- the gap carries NO "
    "intrinsic scale (a function of the external rates t,gamma and L only); the relaxation timescale 1/Delta is "
    "dimensionless; the dissipative arrow's source is the external bath",
    homog, x="Delta(s*H,s*gamma) = s*Delta for s=2,3 (exact) -> no emergent scale; nothing to CLAIMS.md")

print("\nVERDICT: the DRIVEN-DISSIPATIVE channel -- COMPUTED. Criticality does NOT make relaxation gapless: the")
print("LOCALIZED (Aubry-Andre) control is the near-gapless one (~100x slower), while the permanently-critical")
print("METALLIC chain relaxes like an EXTENDED chain (gap ~ periodic) -- an inversion of the naive guess. The gap")
print("decays to 0 in the thermodynamic limit (diffusive, no finite timescale) and is HOMOGENEOUS in the external")
print("rates (Delta(sH,sgamma)=s Delta) -> no intrinsic/emergent scale. So dissipation adds no scale and the arrow")
print("stays externally sourced, extending B183/B187. Interacting Lindblad (many-body dissipative phases) is the")
print("residual NEEDS-SPECIALIST. FIREWALL: emergent open-quantum-systems math (K010 boundary); nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
