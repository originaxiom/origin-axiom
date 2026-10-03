# B1527 — THE CUSP DECIDES: near the hyperbolic point of every word state, no finite-volume projective vacuum carries a reductive count; the mirror-broken states have three type-one curves like the symmetric ones, found on all ten states computed, golden included

cc (the SM-derivation seat), 2026-10-03. Sealed at `4f802f15` before `run.py` read any word state but m004
(`PREREGISTRATION.md`, sha-256 `ebb8c34e…`, SEAL_LEDGER).
- **The run.** 51 minutes on four cores (07:00:48Z to 07:52:19Z), ten manifolds, as sealed. Part H, the two scans and the
  polish are `run.py`'s; the predictions are read by `read_out.py`.
- **Verdict: PROVED, with a kill record.** Item 8 is answered no. The answer is a theorem (§2) on all 758 word states to
  length 12, and was computed on ten of them. Near the hyperbolic point, every finite-volume convex projective structure
  with a generalized cusp has I(ν ⊗ ρ) = I(ν ⊗ Λ²ρ) = 0, for every character ν. That holds on the mirror-broken states too.
- **As sealed: one prediction of eight held.** The priors expected 6.4.
  - P1 held: Part H has I = 0 on all 3,740 rows, and route W agrees on the 1,664 it reads.
  - P2–P8 failed. The sealed type-one scan found points only on +LR (two frames of six), and on no other manifold. Its
    solver's iteration budget had been checked only from a seed already on the solution (E31; §1.2).
  - `read_out.py` returns **outcome C**: by the sealed rule P4 failed, and C means a contradiction is suspected. Here P4
    failed on the nine manifolds with no points to read (it held on +LR's two), not on a non-zero index. No index computed
    anywhere in the arc is non-zero.
- **After the run (disclosed; §4).**
  - X1 pins the frame and reads b as a function of it.
  - X1c does the same at 60 digits on the one manifold where float64 failed.
  - X2 re-polishes every point at 100 digits.
  - Together they find the three type-one curves on all ten manifolds, and I = 0 on every index row at all sixty type-one
    points. After the run the content of P2–P8 holds, except P5's tracking clause, which X1's pinned frame does not test.
    None of this is sealed.
- **A correction to the seal (E53; §2).** Proposition Π is stated for the generalized cusps of types 0–2, the ones
  Ballas' slice parametrizes. Diagonalizable (type-3) cusps also occur near the hyperbolic point (Ballas–Danciger–Lee Thm
  4.1 with Cooper–Long–Tillmann Thm 0.2). They have infinite volume, so the finite-volume answer stands.
- **Prior work: EXTENDS.**
  - Lemma C is sm:B1509 T1 and the audit lane's R44 §1, taken from m004 to every word state and every representation.
  - The two-dimensional intersection is Ballas' (arXiv:1805.09274, §4).
  - What is added: the three type-one curves without symmetry, the class index on them, and the census of ten states.
- **0 of 19 stays 0.**

## 0. What was found

- **Item 8: no count near the hyperbolic point in finite volume.** sL-10 item 8 asked whether a vacuum ν ⊗ ρ_s of a projective
  deformation of a mirror-broken word state, near its hyperbolic point, has a non-zero class index (main's B1297). B1455's
  symmetry argument cannot force it to zero there (sm:B1523's Lemma T). The answer is no for every finite-volume
  structure, i.e. cusp types 0 and 1 (Ballas–Cooper–Leitner Thm 0.6), on every word state to length 12:
  - at the hyperbolic point itself, Part H: I = 0 for every ν, for the projective four and for Λ²;
  - on the three type-one curves through it, Part A with Lemma C: the fibre boundary's holonomy has no eigenvalue 1, the
    cusp is acyclic, and I = a0 − b0 = 0.
  So near the hyperbolic point the mirror's breaking does not make a count, mirror-broken or not.
- **The cusp decides (Lemma C).** ν(ℓ) = 1 for every character, because the fibre boundary ℓ = abAB is a commutator.
  Wherever ρ(ℓ) has no eigenvalue 1, the cusp is acyclic for ν ⊗ ρ and its dual, and I(ν ⊗ ρ) = a0 − b0. So on a word
  state an index can appear only where ρ(ℓ) acquires the eigenvalue 1, or through a0 ≠ b0.
- **The mirror-broken states have finite-volume deformations as the symmetric ones do.** On all ten states there are six
  type-one frames, 60° apart. Their unipotent lines β lie on three lines, which are the zero lines of the family's cusp
  class (sm:B1523's Lemma S):

  | states | class (sm:B1523) | type-one frames α (mod 60°) | lines β (mod 180°) |
  |---|---|---|---|
  | ±LR | reflective | 0° | 30°, 90°, 150° |
  | ±LLRLRR | swaprev-only, mirror-broken | 0° | 30°, 90°, 150° |
  | ±L³RLR² | chiral | 8.2555° | 38.2555°, 98.2555°, 158.2555° |
  | ±L⁴RL³R² | chiral, golden | 20.1143° | 50.1143°, 110.1143°, 170.1143° |
  | ±L⁴RLR³LR² | chiral, golden | 0.9500° | 30.9500°, 90.9500°, 150.9500° |

  - On the symmetric states the lines sit on sm:B1523's coset (30°, 90°, 150°).
  - On the chiral states the three lines turn together, by an angle each state fixes; it is the same for both signs.
  - The golden states behave as the chiral ones, which is P8's content (after the run). Their field does not enter.
- **What stays open** (§7). The infinite-volume part near the hyperbolic point carries I = 0 by Lemma C, except where ρ(ℓ)
  has the eigenvalue 1. That part is type two, plus the type-three cusps. Those eigenvalue-one curves are the next arc,
  registered and to be sealed first. Also open: the non-split extensions on the type-one curves, and the deformations
  far from the hyperbolic point.
- **The experiential question.** GENESIS FK12 holds it under Gate 5-Q, and nothing in this arc bears on it. Per the owner's
  instruction of 2026-10-02 (nothing load-bearing ignored, the experiential question included), that is recorded here.

## Seen first (the repo, then the literature)

**At the seal** (PREREGISTRATION §0, the PRIOR ART section). The repo sweep (`scripts/checks/prior_work.py`) ran on twelve terms
over ten heads.
- No head computed the cusp type of a projective deformation off m004, or the class index on one.
- "type-one" appeared only in the audit lane's R44 and R48, about m004's Ballas curve.
- The literature read was Ballas (1805.09274), Ballas–Cooper–Leitner (1710.03132), Ballas–Danciger–Lee (1508.04794, for
  Thm 3.2), Heusener–Porti (0908.2863), Bobb (1808.02779) and Daly (2411.04431, 2408.08405).

**Refreshed at banking** (2026-10-03, after `git fetch --all`, twice). Main moved to `bad64d34` and then to `7ccae5a2`; the
other heads had not moved.
- Main's B1461 (governance: the review-fires, carry-age, gate-controls and review-core gates) does not bear on this arc.
- Main's B1462 (S45, the seats harvested) re-derives two of this seat's arcs and adopts GENESIS v1.7. It registers main's
  **L242 (e)**: a blind second-route run of main's class index on ±LLRLRR and ±L³RLR², after this seat's seal. It has not
  run, and nothing in B1462 computes a class index on a projective deformation. This arc's points are exported for it
  without readings (§4.7).
- The terms were run again with the post-run vocabulary: "type two", "weight-3", "eigenvalue-one", "acyclic cusp",
  "Cooper-Long-Tillmann", "Deforming convex projective", "item 8".
  - "Cooper-Long-Tillmann" and "Deforming convex projective" are absent on every head.
  - The audit lane's "eigenvalue-one" hits (SOURCE_SCALAR_PROOF, UPSTREAM_3_DESIGN) are about a Laplacian's spectrum and a
    G₂ check. They are unrelated.
  - The seat lanes' "acyclic cusp" hits are copies of this branch's sm:B1368, sm:B1372 and sm:B1513.
  - At `7ccae5a2` the run was repeated with "type-one", "generalized cusp" and "mirror-broken" added. Main's new hits are
    its harvest rows: of the audit lane's R44 (HARVEST_LEDGER row 703, B1457's readers) and of this seat's arcs (B1453,
    B1462, GENESIS v1.7). Main's "type two" (B1189) and "weight-3" (an outside-bench memo on theta functions) mean
    other things.
- **The literature, read at banking** (texts in the seat's scratchpad, from the arXiv PDFs):
  - **Ballas–Cooper–Leitner**, *The moduli space of marked generalized cusps in real projective manifolds*, arXiv:2008.09553,
    Thm 1.7 and the paragraph after it (p. 4). The three-dimensional cusps are (w, h, r) with ∣r∣ ≤ 3∣h∣, and the cubic is
    Re(hz³) + Re(rz∣z∣²). The interior of the cone is diagonalizable, the cone point standard. The paper is about cusps
    alone and says nothing about a manifold's deformations.
  - **Cooper–Long–Tillmann**, *Deforming convex projective manifolds*, arXiv:1511.06206 (Geom. Topol. 22, 2018), Thm 0.2
    (p. 1): the holonomies of properly convex structures whose ends are generalized cusps form an open set among the
    representations whose peripheral images are virtual flag groups. Also p. 2: a cusp's type can change along a
    deformation.
  - **Ballas–Danciger–Lee**, arXiv:1508.04794, §4, Thm 4.1 (p. 18): on a manifold infinitesimally projectively rigid rel
    ∂M, there is a path from ρ_hyp whose peripheral holonomy is diagonalizable over ℝ for t ≠ 0. The seal had read this
    paper for Thm 3.2 only. With Cooper–Long–Tillmann, this gives type-3 cusps near ρ_hyp, and corrects Π's first
    sentence (E53; §2).
  - No source read states the type-one curves near ρ_hyp without a symmetry, or computes cusp types on punctured-torus
    bundles. Ballas obtains type one only through a symmetry (Thm 5.8 and the introduction).

## 1. The run (as sealed)

### 1.1 Part H: 3,740 rows, none non-zero

`run.py` read Part H on every character of every manifold: D = 1, 5, 13, 17, 18, 22, 45, 49, 121, 125 characters. Each
character was read at λ_c and at each of 1, 1.7, e^{0.9i} and −1 that differs from it, for the four and for Λ².

| | rows | I ≠ 0 | identities failing | route W rows | route W disagreeing |
|---|---|---|---|---|---|
| Part H | 3,740 | 0 | 0 | 1,664 | 0 |

- The data are as sealed: at λ_c, t0 = s0 = 1 for the four (the null vector) and 2 for Λ² (the translations); 0 elsewhere.
  a0 = b0 = 0 on every row.
- The margins: route Fox kept ≥ 3.6 × 10⁻¹⁴ against dropped ≤ 1.1 × 10⁻⁴⁵; route W kept ≥ 1.9 × 10⁻⁸ against dropped
  ≤ 2.2 × 10⁻⁵².
- The banked identity (PREREGISTRATION §8). The controls (`controls.py`, C1–C6) were re-run at 06:58Z, after the hashes were
  taken and before the seal's commit (07:00:15Z) and the run (07:00:48Z). Their output was identical to the previous run's line
  for line, and every sealed hash still holds at banking.

### 1.2 The scans: the solver's budget (E31)

| manifold | type-one scan, converged of 72 | b-free scan, converged of 72 |
|---|---|---|
| +LR | 2 | 72 |
| −LR | 0 | 72 |
| +LLRLRR | 0 | 64 |
| −LLRLRR | 0 | 56 |
| +L³RLR² | 0 | 58 |
| −L³RLR² | 0 | 11 |
| +L⁴RL³R² | 0 | 2 |
| −L⁴RL³R² | 0 | 0 |
| +L⁴RLR³LR² | 0 | 0 |
| −L⁴RLR³LR² | 0 | 0 |

- Every seed that failed had exhausted the 80-iteration budget at ∣F∣ ≈ 10⁻³. None stalled early.
- **Why** (`post_run_diagnosis.py`, +LR, a = 0.002). At a ≠ 0 the type-one frame is pinned only at order a. From a seed
  off the frame, the solver has to turn the frame along a direction the equations barely see.
  - At the frame 300°: 7 iterations from the frame itself, 74 from 0.32°, 258 from 1°, 471 from 2.5°.
  - At the frame 0° (Ballas' axis): 7, 120, 303 and 458.
  - The grid's nearest seeds sit 0.32° from +LR's frames. So the two at 120° and 300° converged within the budget, and the
    four at 0°, 60°, 180° and 240° did not.
  - The design had checked the solver only at Ballas' axis, where the seed sits on the frame (C5 and the smoke test:
    7 iterations).
- The b-free scan's failures on the longer words have a second cause: the system's condition number is about 10⁹ there.
- What the sealed scans did show:
  - +LR's two points read β = 150.0000019° at a → 0, on sm:B1523's coset.
  - At both, P4's and P7's conditions hold: 12 index rows with I = 0, nullities 4 and 5.
  - b changes sign across both frames (P5's third clause).
  - The eigenvalue-one crossings P6 asks for are present on the five manifolds where the b-free scan converged on 56 or more
    seeds: 30, 30, 27, 18 and 14 crossings.

### 1.3 The read-out

`read_out.py` (`read_out.json`, `read_out_run.txt`): P1 YES; P2, P3, P4, P5, P6, P7, P8 NO; outcome C. By manifold:

| manifold | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|---|---|---|---|---|---|---|---|
| +LR | Y | n | n | Y | Y | Y | Y |
| −LR | Y | n | n | n | n | Y | n |
| +LLRLRR | Y | n | n | n | n | Y | n |
| −LLRLRR | Y | n | n | n | n | Y | n |
| +L³RLR² | Y | n | – | n | n | Y | n |
| −L³RLR² | Y | n | – | n | n | n | n |
| +L⁴RL³R² | Y | n | – | n | n | n | n |
| −L⁴RL³R² | Y | n | – | n | n | n | n |
| +L⁴RLR³LR² | Y | n | – | n | n | n | n |
| −L⁴RLR³LR² | Y | n | – | n | n | n | n |

Every "n" is a manifold where the scan produced no point, or not enough points, to read. None is a reading that
contradicts a prediction.

## 2. The theorems

As sealed (PREREGISTRATION §3), with two changes.
- Part A's one-line step is spelled out and checked exactly.
- Π's first sentence is narrowed to the cusps its proof covers.

- **Lemma C (the cusp decides).** If ρ(ℓ) has no eigenvalue 1, then H*(Δ; ν ⊗ ρ) = 0 = H*(Δ; (ν ⊗ ρ)*), and I(ν ⊗ ρ) = a0 − b0.
  ν(ℓ) = 1 since ℓ = abAB is a commutator. On m004's family this is sm:B1509 T1 and the audit lane's R44 §1.
- **Lemma E (the index through h¹).** I(V) = h¹(Γ; V*) − h¹(Γ; V) + 2(a0 − b0) + s0 − t0. It is the identity route W uses.
  It held on every reading of the arc, 3,740 rows in Part H and every post-run row.
- **Part H.** I = 0 at ρ_hyp for every ν, for both modules.
  - Off λ_c the cusp is acyclic.
  - At λ_c, ν is unitary and V* ≅ conj(V).
- **Part A (type one near ρ_hyp).** On a smooth path in Ballas' slice with b ≡ 0, through ρ_hyp with non-zero tangent, ρ_s(ℓ)
  has no eigenvalue 1 for small s ≠ 0. So I(ν ⊗ ρ_s) = I(ν ⊗ Λ²ρ_s) = 0.
  - The step the seal states in one line ("a non-zero tangent with c = 0 would have a pure so(3,1) tangent … outside S")
    rests on a fact about the slice: at a = b = 0 its a- and b-directions take values in v, not in so(3,1).
    - Exactly: D_a = X(E22 − I/4) + (X²/2)(E12 − E24) − (X³/3)E14 satisfies Q D_aᵀ Q = D_a, where Q = E14 + E41 − E22 − E33
      is the form whose so(Q) contains N_a and N_b at a = b = 0. Likewise D_b.
    - Checked in exact arithmetic, with a numerical cross-check against mpmath's expm (`verification/part_a_lemma.py`,
      ten checks, all pass).
  - So the slice's so(3,1)-directions are the translations alone. A tangent class whose v-part vanishes on the cusp
    restricts there to a parabolic so(3,1) class.
  - The complete structure has no non-zero first-order deformation with parabolic cusp: the restriction to the cusp is
    injective, and the meridian's complex length is a local coordinate (Thurston; Weil, Garland). So that class is zero.
  - Hence a non-zero tangent has a non-zero v-part. Then ℓ being a rigid slope (sm:B1523, all 536 manifolds) and rigidity
    rel cusp give 0 ≠ c(ℓ) = ȧ D_a(ℓ). So ȧ ≠ 0, and X_ℓ ≠ 0 at the limit frame, since D_a(ℓ) = 0 exactly when X_ℓ = 0.
    Then ψ(ℓ) = aX_ℓ ≠ 0, and the eigenvalues e^{−ψ/4} and e^{3ψ/4} are not 1.
- **Proposition Π, corrected (E53).**
  - The seal says the representations near ρ_hyp "whose cusp is a generalized cusp" form the two-dimensional set L = S ∩ I.
    Its proof covers the cusps conjugate into Ballas' slice S, which are types 0, 1 and 2. The proposition holds as
    stated for those:
    - the type-0, 1 and 2 cusps near ρ_hyp form L;
    - the type-one points are three smooth curves through ρ_hyp, 60° apart;
    - their unipotent lines tend to the zero lines of the family's cusp class;
    - the rest of L, away from ρ_hyp, is type two.
  - **Type 3 is also there.** Diagonalizable (type-3) generalized cusps occur near ρ_hyp. Ballas–Danciger–Lee Thm 4.1 gives
    a path from ρ_hyp whose cusp is real-diagonalizable for t ≠ 0, on every manifold rigid rel cusp. Cooper–Long–Tillmann
    Thm 0.2 makes those holonomies of convex structures with generalized-cusp ends. They lie outside S. For n = 3 they
    have infinite volume (Ballas–Cooper–Leitner Thm 0.6). Lemma C applies to them off their eigenvalue-one locus.
- **The corollary (unchanged).** Every finite-volume convex projective structure near the hyperbolic one with a generalized
  cusp has I(ν ⊗ ρ) = I(ν ⊗ Λ²ρ) = 0 for every ν. Finite volume means types 0 and 1. Type 1 lies in S, so by Π those
  structures are ρ_hyp and the three type-one curves. Part H covers ρ_hyp, and Part A covers the curves. Cooper–Long–
  Tillmann Thm 0.2 makes every point of L near ρ_hyp the holonomy of such a structure.
  - Scope: the 758 word states to length 12, where rigidity rel cusp and the rigid fibre boundary are established
    (sm:B1523). Part H needs neither and holds on every word state.

## 3. The predictions

| | prediction | prior | as sealed | after the run (X1, X1c, X2; not sealed) |
|---|---|---|---|---|
| P1 | Part H: I = 0 on every row, data as stated, route W agrees | 97% | **YES** (3,740 rows, 1,664 W) | — |
| P2 | six frames, three lines 60° ± 1° apart, on every manifold | 80% | NO (two frames, on +LR only) | six frames, exactly 60° apart, on all ten |
| P3 | reflective lines at 30°, 90°, 150° ± 0.3°, and the 90° family's lattice slope exactly unipotent | 85% | NO | on the four reflective manifolds the lines lie at 30°, 90°, 150° (within 10⁻⁶ degrees at a = 10⁻⁵), and the 90° line carries an exactly unipotent lattice slope (∣X∣ ≤ 10⁻⁵⁰) |
| P4 | Part A at every polished type-one point: no eigenvalue within 10⁻⁶ of 1, acyclic cusp, I = 0, margins | 97% | NO (points on +LR only) | at all 60 points (X2, 100 digits): I = 0 on all 1,656 rows, the cusp acyclic, a0 = b0 = 0, route W agreeing on its 240, identities and the sealed margin bar holding; min ∣eigenvalue − 1∣ = 1.04 × 10⁻⁶ |
| P5 | b-free scan: half converge, 90% track, b changes sign across every frame | 70% | NO | b changes sign across every frame on all ten; the tracking clause is not tested (X1 pins the frame) |
| P6 | eigenvalue-one crossings on every manifold | 75% | NO (five of ten) | crossings on all ten manifolds (8 to 30 each, X1) |
| P7 | nullities 4 and 5 with gap > 10⁶ at every point | 85% | NO | at all 60 points (X2, 100 digits): nullities 4 and 5, gaps ≥ 2.4 × 10⁸³ and 9.1 × 10⁸⁷ |
| P8 | the golden manifolds behave as the chiral ones (P2, P4) | 90% | NO | yes |

The last column reads each prediction's content on the post-run points (X1, X1c, X2). It does not change the sealed reading.
- P2's tolerance (60° ± 1°) and P3's (± 0.3°) are met by wide margins (§4.2, §4.4).
- P4's eigenvalue bar (10⁻⁶) was set for the sealed scale a = 0.002. At X1's a = 10⁻⁵ the smallest distance of an eigenvalue of
  ρ(ℓ) from 1 is 1.04 × 10⁻⁶, which is still above it.

## 4. Post-run checks (written after the run; disclosed)

All of these were written after the sealed run had been read. None changes a sealed prediction's reading. Where a check's
first form failed, that is said, and its replacement is described.

### 4.1 The diagnosis (`post_run_diagnosis.py`)

The sealed solver, from +LR's hyperbolic seed at a = 0.002, with the budget raised to 600, at offsets from two type-one frames:

| frame | from the frame | 0.32° | 1° | 2.5° |
|---|---|---|---|---|
| 300° | 7 | 74 | 258 | 471 |
| 0° (Ballas' axis) | 7 | 120 | 303 | 458 |

Every probe converged to the frame it started near, to within 4 × 10⁻⁶ degrees. The sealed budget was 80. ERROR_LEDGER, E31.

### 4.2 X1: the frame pinned (`post_run_x1.py`)

- **The method.** X1 adds two equations to the b-free system: ℓ's translation at angle α₀ and length R0, its value at the
  hyperbolic point. It then reads b as a function of α₀ on the 72 frames 0°, 5°, …, 355°, at a = 10⁻⁵, by float64
  Gauss–Newton. Each zero of b (a sign change with ∣b/a∣ < 10, not a pole) is bisected. The type-one system is solved
  there, and the sealed `polish_point` reads the point at 60 digits, with its polisher replaced by Gauss–Newton with an SVD
  pseudo-inverse.
- **Why a = 10⁻⁵.** A first form used the sealed a = 0.002. It worked on m004 (66 of 72 frames converged), but on −L⁴RL³R² it
  converged on 2 of 72 and found no frame. On the long words the pinned Jacobian's condition number is about 10⁹, and float64
  Gauss–Newton converged from the hyperbolic seed only at small a.
- **The frames.**
  - On nine manifolds: six frames, at α₁ + 60°k exactly (the table of §0).
  - On −L⁴RLR³LR²: four. Its grid converged on 40 of 72 frames and missed the brackets at 120.95° and 300.95° (§4.4).
  - The grid's other non-converged frames all lie within 10° of a pole of the law, where ∣b/a∣ ≥ 1.7 and b has no zero.
- **The weight-3 law.** b/a = −tan(3(α₀ − α₁)) holds on the converged grid to 3 × 10⁻⁸ (±LR), 5 × 10⁻⁸ and 1.5 × 10⁻⁷
  (±LLRLRR), 3 × 10⁻⁷ and 1.5 × 10⁻⁶ (±L³RLR²), 2 × 10⁻⁶ and 1 × 10⁻⁵ (±L⁴RL³R²), and 0.02 and 0.04 (±L⁴RLR³LR²). The
  last two are float64's floor on the longest words. The law's maximum deviation is read where ∣cos 3(α₀ − α₁)∣ > 0.3.
- **The eigenvalue-one crossings** (P6's content): on all ten manifolds, 12, 12, 12, 12, 30, 30, 12, 12, 12 and 8. They are sign
  changes of ψa + ψb, 3ψa − ψb or 3ψb − ψa at ℓ between neighbouring converged frames.
- **The lattice slopes** (P3's content). On the four reflective manifolds the 90° line carries an exactly unipotent lattice
  slope, with ∣X∣ ≤ 10⁻⁵⁰ after the polish:
  - t′ on +LR (m004's section) and on +LLRLRR;
  - −ℓ + 2t′ on −LR and on −LLRLRR. The seal wrote −LR's as (1, 2) in sm:B1523's (μ, λ) basis; in this arc's (ℓ, t′) basis
    it is (−1, 2).
- **The 58 points.**
  - All were polished at 60 digits to ∣F∣ < 6.6 × 10⁻⁴⁹.
  - 1,596 index rows, 232 of them also in route W: I = 0 on every row, every identity holding, the cusp acyclic, a0 = b0 = 0,
    min ∣eigenvalue − 1∣ ≥ 1.04 × 10⁻⁶.
  - 18 of the rows miss the sealed margin bar: the largest dropped singular value is up to 4.1 × 10⁻³⁹, against 10⁻⁴⁰. The
    smallest kept is ≥ 5.9 × 10⁻²⁰. X2 shows the cause (§4.5).
- **X1's nullities do not test P7.** It reads them in float64 at a = 10⁻⁵. There the frame's soft singular value, about
  10⁻⁸ of the top and proportional to a, is not separable from float64's floor on the longer words. The type-one nullity read 4
  on ±LR and 5 elsewhere, with gap ratios below 10⁶. X2 reads them at 100 digits.

### 4.3 X1b: the type-one system at the predicted frames, in float64 (`post_run_x1b.py`)

- **The method.** At the six frames α₁ + 60k, X1b solves the type-one system itself from the hyperbolic seed in that frame. It
  uses no pin and no bracket. As a control it also starts 3° to either side of each frame.
- **On nine manifolds:** all 54 frames were solved, and agree with X1's to ≤ 3.3 × 10⁻⁴ degrees. No control converged (0 of 108).
- **On −L⁴RLR³LR² it is void.** Float64 cannot separate a type-one point from the hyperbolic seed there: 3 of its 12 controls
  "converged". The one new point it passed to the 60-digit polish diverged (∣F∣ = 5.85 × 10²¹⁰). X1b's summary counted that
  point as new without checking the polish. This was caught on reading its record, before anything used it (ERROR_LEDGER, E52).

### 4.4 X1c: the two missing frames at 60 digits (`post_run_x1c.py`)

- **Why.** On −L⁴RLR³LR² float64 cannot separate a type-one point from the hyperbolic seed, and X1's grid had no converged
  neighbours around 120.95° and 300.95°.
- **The method** (its third form). X1's pinned system is solved at 60 digits, always warm-started.
  - The bracket: X1's float64 pinned solutions at α_k + d are polished on the same system at 60 digits, and b(α) is read
    there.
  - The zero of b is found by the Illinois method at 60 digits, to ∣b∣ < 10⁻⁴⁵. Each step is warm-started from the nearer
    endpoint, rotated to the new frame.
  - The type-one system is then polished, and the frame and β are read from the polished point.
  - The four frames X1 had are the positive controls.
- **The result: six frames, all at 60 digits.**
  - The four controls were found again, within 1.2–5.7 × 10⁻⁴ degrees of X1's float64 frames. b at the zero is ≤ 3 × 10⁻⁴⁶,
    and the type-one polish reaches ∣F∣ ≤ 5 × 10⁻⁵³.
  - The two new frames are at 120.94992710° and 300.94992710°, both on the line β = 30.9499°, with polished ∣F∣ = 2.7 × 10⁻⁵³ and
    2.9 × 10⁻⁵⁴.
    - At 300.95° the first pass's seven float64 solves did not converge, so it found no bracket. A second pass with float64
      offsets every 0.025° in ±0.5° found 9 of 41 converged and bracketed it (`--fine 5`; merged into the same record).
- **The weight-3 law at 60 digits.**
  - The three lines are at 0.9499271020°, 60.9499271026° and 120.9499271014° (mod 180°). They are 60° apart to within
    1.2 × 10⁻⁹ degrees.
  - The two branches of each curve, α and α + 180°, carry opposite ψ(ℓ): ±2.2920 × 10⁻⁵, ±1.1131 × 10⁻⁵ and ±1.1789 × 10⁻⁵.
    These equal a·R0·cos α.
  - The 60-digit b(α) read in the brackets follows −tan(3(α − α₁)) to about 10⁻⁹. For example, b/a = ∓0.0052 at ±0.1°.
- **Index rows at the two new points** (60 digits, as `polish_point` reads them): 60 rows, 8 also in route W. I = 0 on every
  row, every identity holding, the cusp acyclic. min ∣eigenvalue − 1∣ = 2.95 × 10⁻⁶ at both.
- **Earlier forms, disclosed.**
  - The first form solved the type-one system from the hyperbolic seed with the pseudo-inverse cut at 10⁻⁴⁰. It stalled after
    one step at every seed: the type-one curve's near-null direction, about 10⁻²¹ of the top singular value 3 × 10⁸, carries a
    residual component there.
  - The second form solved the pinned system from the hyperbolic seed. At 40° it made no progress in 40 steps; a diagnosis
    found the hyperbolic seed outside the Newton basin of this ill-conditioned system. It also failed to bracket the known
    frame 240.95°, a positive control. It was stopped.
- **Not re-measured.** X1's grid gaps away from the frames. On this manifold "exactly six" rests on two things: X1's forty
  converged frames, which follow the weight-3 law to 0.04, and the 60-digit brackets above.

### 4.5 X2: every point at 100 digits (`post_run_x2.py`)

- **The method.** X2 takes every type-one point: X1's 58, rebuilt from their banked frames with X1's own functions, and X1c's
  two new ones, from their banked 60-digit solutions. It polishes each at 100 digits to ∣F∣ < 10⁻⁸⁸.
  - It recomputes every index row the 60-digit reading computed there, with the same characters, twists and modules, and
    route W on the same rows. The thresholds are cusp_lib's and wang_lib's own.
  - It compares each row with its 60-digit reading: I, every dimension of V and V*, and route W's readings.
  - It reads the two Jacobian nullities at 100 digits: the type-one system's, and the b-free system's.
- **The points.** All 60 were polished, to ∣F∣ ≤ 6.3 × 10⁻⁸⁹. The smallest distance of an eigenvalue of ρ(ℓ) from 1 is
  1.04 × 10⁻⁶ (on ±L⁴RL³R²).
- **The rows: 1,656, of which 240 are also in route W.**
  - I = 0 on every row. Every identity holds, the cusp is acyclic, and a0 = b0 = 0. Route W agrees on all 240 of its rows.
  - No row differs from its 60-digit reading.
  - The sealed margin bar is met on all 1,656 rows. At 60 digits it was met on 1,638.
  - The smallest kept singular value is 4.7 × 10⁻²⁰, on −L⁴RLR³LR² at the trivial character with λ = 1. It is the same,
    to the three digits recorded, at 60 and 100 digits on every row, so it belongs to the point, not to the precision.
    This is the row whose cusp is not acyclic at ρ_hyp (for the trivial character λ_c = 1, where t0 = 1; §1.1), and at
    a = 10⁻⁵ the point is close to ρ_hyp.
  - The largest dropped singular value is 2.0 × 10⁻⁷⁹. On every row it is at least 5 × 10³³ times smaller than at 60
    digits.
  - So X1's 18 misses were precision, not rank: the kept values stay, and the dropped ones fall with the digits.
- **The nullities (P7's content).** Type one: 4 at all 60 points. b free: 5 at all 60 points.
  - Type one: the null singular values are ≤ 9.7 × 10⁻⁹⁸ of the top. The frame's soft value lies between 1.4 × 10⁻¹⁵ and
    1.4 × 10⁻⁸ of the top. The gap is ≥ 2.4 × 10⁸³.
  - b free: the null singular values are ≤ 1.4 × 10⁻⁹⁷ of the top, and the gap is ≥ 9.1 × 10⁸⁷.
  - P7's sealed gap bar is 10⁶.
  - The soft value scales with a. The equations see the frame only through b, which moves at order a (the weight-3 law).
    `post_run_soft.py` reads it at a = 10⁻⁵, 4 × 10⁻⁵ and 1.6 × 10⁻⁴ on +LR and +L³RLR². The ratios are 4.000 and 16.000
    (`post_run_soft_run.txt`), and the nullity is 4 at every reading.
- **Time.** 553–1,427 s per manifold, on four cores, from 08:40:22Z to 09:31:15Z. The last manifold, −L⁴RLR³LR², ran after
  X1c (`x2_log_last.txt`).

### 4.6 Part A's step, exactly (`part_a_lemma.py`)

At a = b = 0 the slice's a-direction is D_a = X(E22 − I/4) + (X²/2)(E12 − E24) − (X³/3)E14. It satisfies Q D_aᵀ Q = D_a for
Q = E14 + E41 − E22 − E33, whose so(Q) contains N_a and N_b at a = b = 0, so D_a lies in v. Likewise D_b. D_a(γ) = 0 exactly
when X_γ = 0. The script checks this in sympy, and against a central difference of mpmath's expm to 10⁻²⁵: ten checks, all pass.

### 4.7 The points for main's L242 (e) (`export_points.py`; written at banking)

- **Why.** Main's B1462 registers L242 (e): a blind run of main's class index on the first mirror-broken word states, after
  this seat's seal, as a second route. Main's code needs the representations, and nothing read from them.
- **What it writes** (`points_for_l242e.json`). For each manifold: its presentation (generators a, b, t; relators t g T = φ(g))
  and its cusp words. For each type-one point: the matrices of a, b and t at 60 digits, the frame, the line and the residual.
  It writes no index, cohomology, eigenvalue or margin.
- **How.** X1's points are rebuilt from their banked frames as X2 rebuilds them, and X1c's two start from their banked 60-digit
  solutions. Each is polished at 60 digits with X1's `polish_gn`.
- **The result.** All sixty points (09:47Z to 09:58Z on four cores, `export_points_run.txt`). Every frame is within 10⁻³ degrees
  of its banked value, and every point is polished to ∣F∣ ≤ 6.6 × 10⁻⁴⁹.
- **Checked by the lock, live:** the file holds no reading; each point's relators hold to < 10⁻⁴⁰ and its cusp words commute,
  read from the exported matrices.

## 5. Item 8 and the kill record

- **Item 8 is answered.** On the ten states, and by the theorems on all 758 word states to length 12, no vacuum ν ⊗ ρ or
  ν ⊗ Λ²ρ of a finite-volume projective deformation near the hyperbolic point has a non-zero class index. The mirror-broken
  states (±LLRLRR, the chiral and the golden ones) are no exception. Their type-one curves exist without any symmetry and
  carry I = 0, as on m004.
- **Kill record** (frame F-HE, reach class): `the-cusp-decides`. The character is trivial on the fibre boundary, which is a
  commutator. Off the eigenvalue-one locus of ρ(ℓ) the cusp is acyclic and the index is a0 − b0 = 0. On the type-one
  curves ψ(ℓ) ≠ 0, because the fibre boundary is a rigid slope.
  - Hypotheses: near ρ_hyp; the modules ν ⊗ ρ and ν ⊗ Λ²ρ; finite volume (types 0 and 1); the word states to length 12.
  - Hatch: the eigenvalue-one locus of the infinite-volume part, non-split extensions, far from ρ_hyp, other modules (§7).
- **For the goal.** One more place a count could live is closed: the reductive vacua of the finite-volume projective
  deformations near the hyperbolic point, on every word state to length 12. The places §7 names are not closed. 0 of 19
  stays 0.

## 6. Prior work and standing

- **Standing: EXTENDS.**
  - Lemma C is sm:B1509 T1 and R44 §1 (m004), extended to every word state and every representation.
  - Part H uses main's B1297 (its identity and T5) and the self-duality of ρ_hyp.
  - Part A and Π rest on Ballas §4 (S ∩ I two-dimensional), Heusener–Porti's rigid slopes and sm:B1523's census.
- **What is added, as far as swept:**
  - three type-one curves through ρ_hyp on every word state, with no symmetry needed, 60° apart and on the zero lines of
    the cusp class; Ballas' symmetric family is one of them;
  - the class index on them, zero by Part A;
  - the census of ten states and their lines.
  None of this is in the sources read (§ Seen first). Π's confirmation is after the run, not sealed.

## 7. What this arc does not decide (the next questions)

- **The eigenvalue-one locus of the infinite-volume part near ρ_hyp.** These are the type-two curves where ψa + ψb,
  3ψa − ψb or 3ψb − ψa vanishes at ℓ, and the analogous locus on the type-three cusps.
  - There the cusp is not acyclic for one twist λ, and by Lemma E the index is h¹(V*) − h¹(V) + 2(a0 − b0) + s0 − t0.
    It can jump at isolated points.
  - X1 located these crossings on all ten states (8 to 30 per state on its 5° grid).
  - Registered as the next arc, to be sealed first (OPEN_LEADS sL-10 item 9).
- **Non-split extensions** on the type-one curves of the mirror-broken states (sm:B1509's W₁ and W₂, where the index is ∓1).
- **Far from ρ_hyp**, since Part A is local, and representations outside Ballas' slice other than type 3.
- **0 of 19 stays 0.**

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt`.
- `verification/`:
  - sealed: `cusp_lib.py`, `family_lib.py`, `scan_lib.py`, `wang_lib.py`, `controls.py` (`controls.json`,
    `controls_run.txt`), `run.py`, `read_out.py`;
  - the run: `run_<name>.json` (ten), `run_log.txt`, `read_out.json`, `read_out_run.txt`;
  - post-run: `post_run_diagnosis.py` (`.json`, `_run.txt`), `post_run_x1.py` (`x1_<name>.json`, `x1_log.txt`),
    `post_run_x1b.py` (`x1b_<name>.json`, `x1b.json`, `x1b_log.txt`), `post_run_x1c.py` (`x1c_<name>.json`,
    `x1c_log.txt`), `post_run_x2.py` (`x2_<name>.json`, `x2.json`, `x2_log.txt`, `x2_log_last.txt`),
    `post_run_soft.py` (`post_run_soft_run.txt`), `part_a_lemma.py` (`part_a_lemma_run.txt`);
  - for main's L242 (e): `export_points.py` (`points_for_l242e.json`, `export_points_run.txt`).
- Lock: `tests/test_b1527_the_cusp_decides.py`.
