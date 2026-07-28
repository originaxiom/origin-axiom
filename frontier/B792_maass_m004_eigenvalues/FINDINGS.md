# B792: THE MAASS EIGENVALUES OF m004 — COMPUTED IN-SANDBOX

cc3 audit seat, 2026-07-28. Gate 5-Q. Receipt on B788 (the external
Gates 0–9R bank). Renumbered from B788 per cc's numbering ruling
(CC_TO_CC3_2026-07-28_MAASS_numbering_and_replication).

## HEADLINE

**B790's Step-3 verdict "blocked — Hejhal-on-H³ not in-sandbox,
NEEDS-SPECIALIST" is overturned by computation.** A Hejhal/Then
collocation solver built on the campaign's own Riley holonomy produced
the first six discrete eigenvalues of m004 at ~8 digits, verified at
two independent collocation systems, with the old/new decomposition
confirmed by direct Bianchi-invariance of the eigenfunctions, and
cc's load-bearing UNVERIFIED Gate-8R2 value (λ = 51.014) independently
confirmed and sharpened.

| n | r | λ = 1 + r² | mult | type (S-inv dev) |
|---|---|---|---|---|
| 1 | 3.93891686 | 16.515066 | 2 | NEW (1.2) |
| 2 | 4.90008537 | 25.010837 | 1 | NEW (1.1) |
| 3 | 5.67072003 | 33.157066 | 2 | NEW (1.1) |
| 4 | 5.91291788 | 35.962598 | 1 | NEW (1.1) |
| 5 | 6.63280230 | 44.994066 | 2 | NEW (1.2) |
| 6 | 7.07200419 | 51.013243 | 1 | **OLD = parent ground state (7e−10)** |

Convention: λ = 1 + r², continuous spectrum [1, ∞). No eigenvalues
below λ₁ = 16.515 (fine scan dr = 0.002 over r ∈ (0.8, 4.0)); no
exceptional eigenvalues λ < 1 (ν-scans at both windows). Spectral gap
enormous; Luo–Rudnick–Sarnak λ₁ ≥ 3/4 satisfied with margin 22×.

## STEP 3 (Method A): the solver

`hejhal_m004.py`. Ingredients, all verified in `groundwork.txt`:
- Riley holonomy A = [[1,1],[0,1]], B = [[1,0],[−ω,1]] — the banked
  geometric point. Relator `aBAb` verified (= B789's relator, 1e−16).
- Cusp lattice Λ = Z + Z·τ, τ = 2√−3, found by brute-force parabolic
  word search; matches SnapPy cusp shape to 12 digits.
- K_{ir}(x) = ∫₀^∞ e^{−x cosh u} cos(ru) du by trapezoid: EXPONENTIALLY
  convergent (Poisson summation), 32–34 nodes give ≤1e−12 relative
  error against mpmath even at the e^{−πr/2} scale. Small-eigenvalue
  sector (λ < 1) via real order ν = s−1, cosh weights.
- Steepest-ascent pullback with 91 (c,d)-distinct moves (words ≤ 5,
  |c| ≤ 2.2): Γ-invariance of reduced height 1.4e−14; the Ford floor
  of m004 sits at t ≈ 0.87, so the Y = 0.75 horosphere raises 100% of
  sample points. Collocation rows are exact for ANY Γ-translate.
- Truncated cusp expansion, collocation matrix V(r), column-normalized;
  σ_min(V) dips ~9 orders of magnitude at eigenvalues.

Verification protocol:
1. **Two-system stability**: each eigenvalue refined independently at
   Y = 0.75 (516 modes/705 pts) and Y = 0.62 (774 modes/1044 pts,
   different seed): agreement ~1e−9 on every eigenvalue. Spurious
   dips would move; none did.
2. **Multiplicity from σ-tails**: doubles (n = 1, 3, 5) show TWO
   singular values at ~1e−10 with the third at ~0.2.
3. **Old/new by direct invariance**: reconstructed eigenfunctions
   tested under S = [[0,−1],[1,0]] ∈ PSL(2,O₃)∖Γ₄₁ at 24 random
   points: the n = 6 form is S-invariant to 7e−10, all others break
   S-invariance at order 1. NINE orders of separation — no threshold
   ambiguity. (An earlier O₃*-Fourier-weight heuristic was scale-
   confounded and is superseded by this test.)
4. **The blind cross-check**: the solver, told nothing but the Riley
   matrices, produced a dip at r = 7.0720 — the Bianchi orbifold
   ground state seen through the index-12 restriction (Step 2).

## GATE-8R2 VERIFICATION (cc's ask §4, discharged computationally)

cc's external calibration rests on λ₁(parent) = 51.014 (r = 7.072058),
sourced from a SECONDARY report of Grunewald–Huntebrinker 1996 Table 3,
flagged UNVERIFIED. This computation gives the parent ground state — 
through m004, by an entirely independent method (collocation vs FEM),
with the eigenfunction's Bianchi-invariance verified at 7e−10 —

    r = 7.07200419,  λ = 51.0132434

|Δr| = 5.4e−5 vs the secondary value: agreement at 1996-FEM accuracy.
**The transcription is VERIFIED as correct to its precision** (no
wrong-object or wrong-magnitude error), and the value is sharpened by
~4 digits. Note 51.014 rounds the true 51.0132 up at the 4th decimal —
anyone comparing at 5+ digits should use 51.0132434 (r = 7.07200419).

## WEYL BUDGET (B791 cross-reference)

Count to T = 7.072: 6 distinct parameters, 9 with multiplicity. Bare
Weyl main term 12.1 — the deficit is the (negative) cusp/Eisenstein
correction; with φ(s) = Λ_K(s−1)/Λ_K(s) exact (B737/B739) the
correction is computable in-sandbox: registered follow-up.

**Empirical input to B791's sector criterion**: observed m004
multiplicities are {1, 2}, not {1, 5, 6}. If the E = E₁⊕E₅⊕E₆
decomposition is to predict multiplicities, the relevant count is
dim V_i^H (H = point stabilizer, Frobenius: 12 = 1·1 + 5·1 + 6·1),
which predicts multiplicity 1 per sector — the observed doubles must
then come from a symmetry OUTSIDE the coset action (orientation /
complex conjugation), not from the sector structure. B791's "generic
multiplicity" phrasing should be scoped accordingly.

## LENGTH SPECTRUM AT CUTOFF 6.0 (B790 follow-up (a), in progress)

m004: 370 distinct complex lengths (7513 geodesics with multiplicity)
at cutoff 6.0 vs 134 at B790's 5.0. Systole 1.0870701449957387 =
B790's banked value. ALL traces 2cosh(ℓ_C/2) in Z[ω] to 2.4e−10 —
B790's L2 algebraicity extends to the raised cutoff. The mod-4/odd
split test awaits the m003 cutoff-6 run (in progress);
`trace_norm_split.py` is the checker.

---

# STEP 2 (original arc content): THE BIANCHI INDEX

Chat-1 handoff (MAASS_SPECTRUM_HANDOFF, 2026-07-25), Step 2, owner CC3.
cc's independent re-derivation banked first (B790/B791); this Step 2 is
logged as accidental independent replication in B791 §5.

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
