# B788: MAASS SPECTRUM PROGRAMME — STEP 2 (BIANCHI INDEX)

cc3 audit seat, 2026-07-28. Gate 5-Q. Chat-1 handoff
(MAASS_SPECTRUM_HANDOFF, 2026-07-25), Step 2, owner CC3.

## RESULT

**[PSL(2, O₃) : Γ₄₁] = 12, EXACT.**

Derivation (step2_bianchi_index.py): the index equals the volume ratio,
and both volumes are exact closed forms in L(2, χ₋₃):

    Vol(m004)           = 2·Cl₂(π/3) = (3√3/2)·L(2, χ₋₃)
    Vol(PSL(2,O₃)\H³)   = 3^{3/2}·ζ_K(2)/(4π²) = (√3/8)·L(2, χ₋₃)
                          (Humbert's formula; the π² cancels)

    index = (3√3/2)·L / ((√3/8)·L) = 24/2 = **12**

The transcendental L-value cancels EXACTLY — no numerics needed for the
final answer. Numerical confirmation at 60 digits: |ratio − 12| < 4e−60.
Concurs with Riley (1975): the figure-eight group is an index-12
subgroup of PSL(2, Z[ω]).

Caveat stated honestly: the volume ratio determines the index GIVEN the
inclusion Γ₄₁ ⊂ PSL(2,O₃). The inclusion itself is Riley's theorem (the
parabolic holonomy representation has entries in Z[ω]).

PGL note: [PGL(2,O₃) : PSL(2,O₃)] = 2, so [PGL(2,O₃) : Γ₄₁] = 24.
The handoff's restriction step should use PSL (holonomy lands in
PSL(2,C)).

## IDENTITY CHECKS (pitfall 4 antidote)

- H₁(m004) = Z (the knot complement); H₁(m003) = Z ⊕ Z/5 (the sister).
  SAME volume to 60 digits — homology is the ONLY safe discriminator.
- 4_1 exterior isometric to m004: SnapPy verified True.
- 2 tetrahedra, 1 cusp, all positively oriented.
- SnapPy quad-precision volume matches 2·Cl₂(π/3) to 60 digits.
- V_tet = Cl₂(π/3) = 1.0149416064... is the Gieseking constant —
  the Gieseking manifold (m004's parent, B749/F5) is ONE regular ideal
  tetrahedron; m004 is its orientation double cover. Vol ratio 2, as
  the fork chain requires.

## CONSEQUENCES FOR THE PROGRAMME

1. **Spectral inclusion.** Γ₄₁ ⊂ PSL(2,O₃) means every level-1 Bianchi
   Maass form restricts to a Γ₄₁ form with the SAME eigenvalue. The
   Bianchi spectrum embeds in the m004 spectrum.

2. **Old/new split.** Weyl constants: c(m004) = 0.0342784,
   c(Bianchi) = 0.0028565, ratio exactly 12. Asymptotically ~1/12 of
   m004 eigenvalues are "old" (Bianchi level-1); **~11/12 are NEW forms
   invisible to LMFDB level-1 data**. Step 1 (CC2, LMFDB search) can
   at best cover the old 1/12. Step 3 (direct computation) is required
   for the bulk of the spectrum.

3. **Handoff correction (minor).** The handoff states N(T) ~ 0.03434·T³.
   The correct constant is Vol/(6π²) = 0.0342784. Expected counts:
   N(5) ≈ 4.3, N(10) ≈ 34.3, N(20) ≈ 274, N(50) ≈ 4285 (handoff's
   4293 slightly high).

4. **False-failure clause.** The handoff flags index > 100 as the
   trigger for "restriction insufficient, compute directly". Index 12
   does NOT trigger it, but the old/new split above shows direct
   computation is needed anyway for all but ~8% of the spectrum.

5. **Coset structure for Step 3.** |PSL(2,F₃)| = 12 = the index. The
   fundamental domain of Γ₄₁ is 12 copies of the Bianchi domain
   (equivalently SnapPy's 2-tetrahedron Ford domain). The cusp lattice
   for the Fourier–Bessel expansion is (a sublattice of) O₃.

## STATUS

Step 1 (LMFDB search): CC2's assignment, not started here.
Step 2 (this): **DONE**. Index = 12 exact.
Step 3 (compute): SPECIALIST assignment per handoff.

## SEAL

Algorithm: SHA-256 of this file's content excluding the SEAL section.
