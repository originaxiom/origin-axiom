# B1804 — SELECTION BY INVERSION, FIRST TEST (P-419; DATA-FREE): FLUXES INVARIANT UNDER THE OBJECT'S MONODROMY LR AND OF HODGE TYPE (1,1) FORCE ONLY CURVES WHEN THE TORUS SPLITS ALONG LR'S INVARIANT SPLITTING, BUT FORCE ISOLATED CM POINTS WHEN LR ACTS HOLOMORPHICALLY (ABELIAN SURFACES WITH REAL MULTIPLICATION BY ℤ[φ]). THE POINT IS CHOSEN BY FREE FLUX INTEGERS, NOT BY LR; ONE FORCED POINT HAS CM BY ℚ(√5, √−3), THE RECORD'S GENUS FIELD; AND THE HOLOMORPHIC FRAME HAS NO LR-INVARIANT KÄHLER CLASS

**Verdict: PROVED,** by exact computation, for both frames' statements:
- **NEGATIVE** for "an LR-invariant (1,1) flux selects τ" in the split frame.
- **POSITIVE but conditional** in the holomorphic frame: isolated CM points, chosen by flux integers, in a frame without an
  invariant Kähler class.

Data-free; none of the 19. cc (main), 2026-10-28, P-419. Corrected before landing at its hostile referee (§ 6): the draft's
unscoped NEGATIVE was overturned.

**0 of 19.**

## 1. The question (P-419)

- **Why it is asked.** The meditation's reading 1 needs a selection principle. The one mechanism tried so far is
  potentials, which are mirror-even and land at fixed points (W51–W176).
- **The inversion.** Does a discrete requirement the object fixes force a modulus onto a special locus, as
  Noether–Lefschetz loci do for flux vacua? Donagi–Wijnholt (arXiv:0904.1218): three-generation local SU(5) models exist
  on that locus, not at generic moduli.
- **The mechanism.** A magnetic flux must be of Hodge type (1,1).
- **The object's condition.** The flux must be invariant under LR.

## 2. The criterion (verified two ways)

- **The form.** On a complex 2-torus with holomorphic 2-form Ω = dz₁ ∧ dz₂, a real 2-form F is (1,1) iff F ∧ Ω = 0.
- **Why one complex equation suffices.** F's (2,0) and (0,2) parts are conjugate (the referee's r1).
- **For a mixed class.** F_N = Σ N_ab da₁ ∧ db₂ on E_τ × E_τ′ has F_N ∧ Ω = (−N_xx ττ′ + N_xy τ + N_yx τ′ − N_yy) vol.
  So F_N is (1,1) iff τ′ = M_N·τ, with det M_N = det N.
- **Determinant −1 is impossible.** F_N ∧ F_N = −2 det N vol, so by the Hodge index a mixed (1,1) class needs det N > 0.
- **The transformation law.** AᵀNB, checked against the other conventions (r2); for LR and RL, which are symmetric, all
  agree.

## 3. The split frame (main's computation, `verification/c1_invariant_fluxes.py` → `c1_run.txt`)

- **The setup.** T⁴ = E_τ × E_τ′ with A ∈ {LR, RL} acting on each factor's H¹, by A on both factors or by A^{−T} on the
  second.
- **The invariant mixed classes** are a 2-dimensional coset of the commutant ℚ[A] ≅ ℚ(√5).
- **The det form on them** has signature (1, 1).
- **Every invariant class with det > 0 is (1,1) on its own curve τ′ = M_N·τ.**
  - Examples: τ′ = τ, τ′ = −1/τ, τ′ = (2τ + 1)/(τ + 1), τ′ = (3τ + 1)/(τ + 2).
  - There are countably many such Hecke-type curves (r4), not two.
- **No point.** Two independent invariant (1,1) classes would make the whole invariant plane (1,1), the det −1 class
  included, which is impossible in ℍ × ℍ.
  - So no integer flux forces a point of ℍ × ℍ. 0 of 28 small curve pairs meet in ℍ (r4).
  - The common solutions of the basis pair are the real golden points.
- **CM points are not singled out here.** (i, i) and (ω, ω) lie on τ′ = τ like every point. The invariant (1,1) lattice
  has rank 1 there, as at generic points.
- **The in-frame criterion is "the commutant has no elliptic element".**
  - Parabolic T gives no point either (r3).
  - The controls, run on the same code (r3): S forces (i, i), ST forces (ω, ω), T forces nothing (E82).
- **Other actions** (r3):
  - A ⊕ I, I ⊕ A and A ⊕ A^{±2} have no invariant mixed class.
  - A_H ⊗ A_W and A^{−T}_H ⊗ A_W have signature (1, 1): curves only.

## 4. The holomorphic frame (the referee's computation, rerun on main)

- **The same lattice action, a different complex structure.** The factor-index action I_H ⊗ LR_W on E ⊗ ℤ² is conjugate in
  SL(4, ℤ) to the split frame's LR ⊕ LR (r6). Only where the complex structure sits differs.
- **The invariant classes there** have det-form signature (2, 2), so points are possible (r3).
- **On the slice τ′ = τ, where LR is holomorphic:**
  - the invariant class with mixed part ε together with a class a dx₁dx₂ + b(dx₁dy₂ + dy₁dx₂) + c dy₁dy₂ (ac − b² > 0)
    forces τ = τ′ = the root of aτ² − 2bτ + c = 0;
  - (1, 0, 1) → i; (2, −1, 2) → ω; (1, 0, 3) → √−3; (1, 0, 12) → 2√3 i;
  - the invariant (1,1) lattice jumps from rank 1 to rank 2 exactly at CM points, which is Noether–Lefschetz behaviour.
- **On the full family:** abelian surfaces with real multiplication by ℤ[φ], parameters (τ₁, τ₂), a Hilbert modular
  surface for ℚ(√5) (r7).
  - 14 pairs of small invariant classes force 9 conjugate pairs of isolated points.
  - All are quartic CM points in ℚ(√5, √−d) for d ∈ {1, 2, 3, 7}.
  - Example: (τ₁, τ₂) = (iφ, i/φ).
  - **One case worth recording.** The pair whose Gram matrix is A₂'s, [[−2, −1], [−1, −2]], forces a point with
    coordinates in ℚ(√5, √−3, √−15), i.e. CM by ℚ(√5, √−3). That is the compositum of the record's forced quadratic
    fields (B730: ℚ(√−3), ℚ(√5), ℚ(√−15)).
  - r7 is a demonstration over chosen pairs, not an exhaustive search.
- **LR does not choose the point. The flux integers do.**
  - The continuous modulus is traded for discrete inputs: P-401's landscape point, and P-418's count.
- **The frame lacks an invariant Kähler class** (r5).
  - The split frame keeps an invariant Kähler class (ω₁ + ω₂), but never an invariant complex structure: the induced
    map τ ↦ (2τ + 1)/(τ + 1) has no fixed point in ℍ.
  - The holomorphic frame keeps the complex structure, but its invariant (1,1) classes are negative definite, so it has
    no invariant Kähler class: LR is a positive-entropy automorphism (McMullen; Cantat).
  - No flat-T⁴ frame keeps both. Supersymmetry's D-term half is therefore not available in the frame where the points
    appear.

## 5. What it means

- **Where selection by inversion works.**
  - It does not work in the split frame: only curves, for every integer flux.
  - It works in the holomorphic frame, at isolated CM points. The flux integers choose the point, so a continuous input
    is traded for discrete ones, and that frame lacks an invariant Kähler class.
- **Withdrawn from the draft:**
  - "never a point of ℍ, never a CM point";
  - "because LR is hyperbolic" (LR's hyperbolicity is what makes the holomorphic action positive-entropy, not what
    forbids points);
  - the comparison with the SM seat's § 320: its curve is a real curve in the τ-plane, while this one leaves τ free.
- **The open question it raises (P-425).** Does requiring CM by the compositum the object forces, K = ℚ(√5, √−3), cut
  the flux-integer freedom to a finite, class-number-sized set of points?
  - Then: what couplings live there, and can the Kähler obstruction be met (a non-flat or non-Kähler frame)?
  - This is speculation until computed.
- **0 of 19.**

## 6. The referee (hostile, read-only; `audit/referee_b1804/`, scripts kept in `verification/referee/`)

**Verified:**
- the 2-dimensional invariant space with det ±1 classes;
- the det −1 class never (1,1);
- the golden points;
- the (1,1) criterion and its signs (r1);
- the transformation law (r2).

r1, r3, r5 and r6 regenerate identically on main.

**One blocking finding, applied.**
- The NEGATIVE was stated universally.
- The same monodromy acting holomorphically forces isolated CM points (r6, r3, r7).
- Everything is now scoped, and the holomorphic frame is reported.

**Corrections applied:**
- the curve list (countably many);
- "never a CM point" replaced by "not singled out";
- the § 320 comparison withdrawn;
- the in-frame reason ("no elliptic element in the commutant") and the signature criterion;
- the "retired as values" non sequitur removed;
- the Kähler half added.

**Notes applied:**
- the argument for every integer flux;
- the positive controls S, ST, T;
- the fixed-point convention (with v ↦ Av and z = x + τy, LR induces τ ↦ (2τ + 1)/(τ + 1), fixed points (1 ± √5)/2);
- "at most a curve";
- B1794, P-401 and P-413 added to Seen first;
- the stale guess in the design note marked.

## Seen first

`VERDICT topic-sweep /flux.{0,40}\(1, ?1\)|\(1, ?1\).{0,40}flux|Noether.?Lefschetz|N[ée]ron.?Severi|Picard (number|rank)/
(full text): 0 of 1550 arcs on main match; 1 register row matches (P-419)`. The neighbouring sweeps are in the referee's
`topic_sweeps.txt`: CM, 16 arcs; attractors and moduli stabilisation, 14; products of tori, 55. None states this.

**Bearing on it:**
- B1791;
- B1696 and B1702;
- B486;
- B730 (the record's three quadratic fields);
- B1794 (no forced hypercharge class);
- B1800 (the one-torus flux frame);
- P-401 (the flux pivot trades inputs for flux integers);
- P-413 (the SM seat's § 320).

**Literature:**
- Cremades–Ibáñez–Marchesano;
- Antoniadis–Maillard and Antoniadis–Kumar–Maillard;
- Donagi–Wijnholt (arXiv:0904.1218, checked at abstract level);
- Moore (attractors);
- Gukov–Vafa;
- for the holomorphic frame, to read at source: Hilbert modular surfaces and Hirzebruch–Zagier cycles, and
  positive-entropy automorphisms of abelian surfaces (McMullen; Cantat).

## Files

- `verification/c1_invariant_fluxes.py` → `c1_run.txt`.
- `verification/referee/`: `r1_hodge_criterion.py`, `r2_conventions.py`, `r3_actions_survey.py`, `r4_combinations.py`,
  `r5_kahler_and_holomorphy.py`, `r6_same_bundle.py` and `r7_holomorphic_frame.py`, with their runs.

The lock: `tests/test_b1804_selection_by_inversion_first_test.py`.
