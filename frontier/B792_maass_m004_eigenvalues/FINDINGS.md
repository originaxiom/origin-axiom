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

## THE r = 7.0720 EIGENVALUE: BLIND OBSERVATION (provenance-corrected)

**Provenance arc (full record, 2026-07-28):** (i) 51.014 entered via a
secondary report of Grunewald–Huntebrinker 1996 Table 3; (ii) cc's
URGENT alert flagged it unsourced (paywalled primary; the reporting
subagent's "read the PDF" claim not credible) and withdrew it as a
control; (iii) cc then WITHDREW the fabrication alarm after this
computation: with mean spacing ≈ 0.482 in r, a fabricated value
landing 5.4e−5 from a true eigenvalue has p ≈ 2.2e−4 (~4500:1 the
value is genuine). This section previously said "transcription
VERIFIED" — the durable statement is weaker and stated exactly below.

What this computation establishes, on its own evidence:

    r = 7.07200419,  λ = 51.0132434

**Targeted confirmation, not blind discovery**: the scanC window was
chosen because the alleged value existed; but solver parameters were
frozen at scanA (r ∈ (0.8, 6.5)) before any high-r scan, and 7.072 was
never used to tune, filter, accept, or reject anything. The
eigenfunction is invariant under S ∈ PSL(2,O₃)∖Γ₄₁ to 7e−10 — a
level-1 Bianchi (parent) eigenvalue; by the ground-state argument
(nothing below the parent's λ₁ is inheritable) plus the V₁ Weyl
budget (1.13 expected on the window), it is the parent ground state.
Independently reproduced on cc's separate instrument (7/7 eigenvalues;
parent at 54× displaced controls).

Open action: reading the actual Experiment. Math. 5(1) 57–80 Table 3
(the other ~35 values). The programme's citable value is 51.0132434;
51.014 is its 4-sig-fig secondary echo (G–H's own "last digit may be
untrustworthy" caveat covers the 5th-digit difference).

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

## THE FULL WINDOW r < 10: 17 DISTINCT, 27 WITH MULTIPLICITY

Upper window (7.3, 10), scanD + two-system refinement, all 11 STABLE:

| r | λ | mult | type |
|---|---|---|---|
| 7.34952664 | 55.015542 | 2 | NEW |
| 7.40661560 | 55.857955 | 1 | NEW |
| 7.68767117 | 60.100288 | 1 | NEW |
| 7.85778326 | 62.744758 | 2 | NEW |
| 8.30822480 | 70.026599 | 2 | NEW |
| 8.86340536 | 79.559955 | 2 | NEW |
| 9.02742152 | 82.494339 | 1 | NEW |
| 9.04778823 | 82.862472 | 2 | NEW |
| 9.08064862 | 83.458179 | 1 | NEW |
| 9.64012103 | 93.931933 | 2 | NEW |
| 9.83711622 | 97.768855 | 2 | NEW |

No old (Bianchi) form in (7.3, 10) — now PROVEN at eigenspace level:
the nullspace projection test (`sector_projection_test.py`) minimizes
the S-invariance defect over each FULL mult-2 eigenspace (generalized
2×2 eigenproblem of defect vs norm forms), closing the hidden-parent
caveat. Result: dev_min ∈ [0.83, 1.2] for all 16 non-parent
eigenvalues (no S-invariant direction anywhere), vs 3.5e−10 at 7.072.
Controls: every below-ground-state eigenspace parent-free (required by
the ground-state argument) ✓; 7.072 reads parent ✓.
**cc's pre-stated prediction "r = 8.8634 is the parent's k=2 (V₁)" is
REFUTED** — its Weyl-position argument (W·r³ = 1.989, 0.18% from slot
2) loses to the direct invariance test (E4 instance, banked cec8b099).
The absence of a second parent eigenvalue below r = 9.84 is an
ordinary fluctuation (V₁ budget on [3.9, 9.84] expects 2.55, found 1,
z = −0.97) and is otherwise UNEXPLAINED — a GH-ladder explanation
briefly attached here is WITHDRAWN per cc's gate: the GH table is
per-symmetry-type (entries not consecutive in the full spectrum) and
122.19 is uncorroborated secondary data.
No exceptional λ < 1 anywhere in (0.8, 10).

## WEYL COMPLETENESS (scattering-corrected, exact φ)

`weyl_scattering_check.py`: N_disc(T) vs (vol/6π²)T³ + the scattering
correction −(1/4π)∫(φ'/φ)(1+it)dt computed from the EXACT
φ = Λ_K(s−1)/Λ_K(s) (B737/B739). Residual after correction: −0.6 at
T=3 → −3.6 at T=7 → −7.0 at T=9.9, tracking −(T/π)ln T (the one-cusp
parabolic term, NOT computed into the prediction): shape-predicted
−4.3 and −7.2 at those T. Smooth, no integer-step downward anomaly:
**no missing-eigenvalue signature**. Scope per main's B791 caveat
(cusp terms are O(T log T), unquantified): this is a CONSISTENCY
CHECK, not a derivation — the budget must not adjudicate a count
difference of order one.

## THE LAST DOOR: SM COMPARISON — CLEAN NULL (Tests 1–3)

`sm_comparison_tests.py`, pre-registered protocol in the docstring
(B743 rules: surrogate nulls, base-rate gate 0.02, PSLQ caps 64/16):

- **Test 1 (direct)**: 17 r's + 17 λ's vs 18 banked PDG targets.
  2 candidates (δ_CP, m_s/m_d — both low-digit targets), surrogate
  p = 0.65/0.53 → FAIL base rate.
- **Test 2 (ratios)**: 272 r-ratios + 272 λ-ratios vs 18 targets.
  39 candidates, ALL at 1–2-digit targets with surrogate p ≥ 0.24
  (sin²θ₂₃: p = 0.994) → ALL FAIL base rate.
- **Test 3-lite (algebraicity, 8-digit)**: PSLQ of every r, λ against
  all six B743 bases: ZERO relations, null rates 0.00. The near-
  integers λ₂ = 25.0108, λ₅ = 44.9941 are 0.04% off — correctly NOT
  relations at tol 1e−7 (the protocol kills exactly this numerology).

**VERDICT (scope-corrected per cc gate, 2026-07-28): clean nulls —
no SM value is reachable from this spectral set at 8-digit precision
under the stated base-rate control.** This is a GENERIC-SPECTRUM null
over 17 eigenvalues on a bounded window, with B713–B716 (the
character-variety/torsor negatives) as context, NOT as the hypothesis
— the Laplace spectrum is a different object and imports no prior H0.
The deep-precision question (20+ digits, handoff Tests 1–2 as posed)
and the algebraicity question (50+ digits, Test 3) remain OPEN,
untested, in both directions.

PROCESS NOTE: the first execution of these tests ran from an unsealed
docstring protocol and an uncertified spectral set — cc's hold relay
arrived after the run. Remediation: the protocol is extracted verbatim
to SM_COMPARISON_PREREGISTRATION.md and sealed, the spectral set is
mode-count certified (see certification below), and the tests re-run
from the sealed protocol on the certified set. The first run is
retained as a labeled dry-run (sm_comparison_results.*).

## TRACE-NORM SPLIT AT CUTOFF 6.0 (B790 follow-up (a): DONE)

m004: 370 distinct traces (7513 geodesics w/ mult), m003: 411 (7413),
~2.7× B790's cutoff-5 sample. Systoles match banked values exactly;
ALL traces in Z[ω] to 2.4e−10 (L2 algebraicity extends).

**B790's split is STABLE in REFINED form** (`trace_norm_split.py`):
- B790's "m004-only norms ≡ 0 mod 4" FAILS at cutoff 6: norm 7 enters
  via the m004-exclusive traces 3+ω and 2−ω.
- The real law (all three tests pass at cutoff 6):
  - m004-only norms ≡ 0 or 3 (mod 4)
  - m003-only norms ≡ 1 (mod 4) exactly (sharper than B790's "odd")
  - **ALL m004 trace norms avoid 1 mod 4** (shared norms are {0,3} too)
- Reading: 2 is inert in Z[ω] (residue field F₄), so norm ≡ 0 mod 4 =
  even trace. For ODD traces the mod-4 norm class splits the sisters:
  m004's odd traces have N ≡ 3, m003's ≡ 1. The norm ≡ 1 mod 4 traces
  are exactly m003's exclusives. A mod-4 congruence condition on
  Γ₄₁'s traces — consistent with the level-4 cusp structure
  (B737: O/Λ ≅ Z/4, CM by the conductor-4 order, disc −48).
- B790's cutoff-5 phrasing was sample-limited: no odd m004-exclusive
  trace exists below cutoff 5.

## THEOREMS (mod4_trace_law_proof.py — the law PROVED, plus congruence)

Finite computation in SL(2, Z[ω]/4), no citations:
- **Theorem 1**: ⟨A,B⟩ mod 4 has order 320 (H̄ = 160 in PSL);
  the Bianchi generators surject onto SL(2, Z[ω]/4) (closure = 3840,
  verified); [PSL(2,Z[ω]/4) : H̄] = 1920/160 = 12 = [PSL(2,O₃) : Γ₄₁]
  ⟹ Γ₄₁ = preimage(H̄) ⟹ **Γ(4) ≤ Γ₄₁: the figure-eight knot group
  is a CONGRUENCE subgroup, of level exactly (4)** (mod-2 image is
  D₅ < A₅ of index 6, so Γ(2) ⊄ Γ₄₁). Explains B791's coset-image
  order 1920 = |PSL(2, Z[ω]/4)| and its stabilizer order 160 = |H̄|.
  Note (scoped to HOOK per cc's H-B794-A5): A₅ = PSL(2,F₄) appears
  with dihedral D₅ image, and A₅ also carries B787's 5A/5B
  ambivalence argument — two appearances of the smallest simple
  group, suggestive and NOT thereby a connection. Open cell: same
  A₅ or not?
- **Theorem 2**: traces of H have norms {0,3} mod 4 ⟹ every m004
  geodesic trace norm avoids 1 mod 4 at EVERY cutoff. The observed
  law is a theorem. (The m003-side "≡ 1 mod 4 exactly" statement
  remains observational — m003's holonomy is not ⟨A,B⟩.)

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
