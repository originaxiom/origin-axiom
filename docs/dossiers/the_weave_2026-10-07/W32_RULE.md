# W32 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. The values below were derived by
hand before this was written and are listed as such. Nothing here is a result.

## Why this route

- **The owner, 2026-10-08:** "do as u recomend on all". The recommendation's third item was the puncture's content
  (GENESIS GAP2's place), the one computational route left on the record for the count.
- **W23:** in F-HE's SU(5) frame the weave's five, W = D ⊕ P, reads (n(10), n(5̄)) = (1, 3) under W22's block rule. It
  is anomalous by −2, so "the puncture must carry +2; two localized 10s would complete three generations, but the
  anomaly alone does not fix that content."
- **The end condition is how the puncture enters a count** (GENESIS GAP2: chiral counts depend on an end condition that
  is chosen rather than derived). W28 found the condition that keeps every symmetry of the bulk problem (naturality)
  gives ±3 on 𝕎. This arc asks what the same principle gives in F-HE's two sectors at once.
- **Main's S87 (B1607, GENESIS v1.29):** the chiral three lives on ⟨L, R⟩ = SL(2, ℤ); the swap and the principle's
  tick σ = L∘P reverse the records' orientation, which the index needs. So this arc's moves are L and R.

## Weave or thread?

- **Weave-type.** The bundles are built from the common point's blocks, which every thread shares. Every bundle the
  moves keep is taken, none hand-picked. The end conditions are those the joint action keeps.
- **F-HE is a frame, a hypothesis** (GENESIS GAP1). Every count here is conditional on it.

## The objects

- **The blocks:** the trivial character χ₀; the three parity characters χ₁, χ₂, χ₃ (exponents (2, 0), (0, 2), (2, 2) of
  i on a, b; the_chiral_triplet's PAR); the spin doublet D = ρ_Q (a ↦ i, b ↦ j; the_spin_room's RHO). χ_p ⊗ D ≅ D, so
  there is one doublet type. P = χ₁ ⊕ χ₂ ⊕ χ₃.
- **The bundles:** every sum of blocks of rank 5 with trivial determinant whose class L and R keep (an intertwiner
  exists for each). Computed by enumeration.
- **The sectors (F-HE; W23):** the 10 of SU(5)_g carries W; the 5̄ carries Λ²W.
- **The local solutions at the puncture:** the fibre, S = ℂ⁵ for W and Λ²ℂ⁵ for Λ²W. The puncture holonomy
  ρ([a, b]) is −1 on doublet-type pieces (α = ½) and +1 on character-type pieces (α = 0). Let r₋ be the dimension of
  its −1 eigenspace.
- **The index (W22, W28):** n = −r₋/2 + dim Λ₊, for an end condition Λ₊ ⊂ S.
- **The end conditions:**
  - **naturality (W28's condition):** Λ₊ is kept by the lifts of L and R and by the bulk commutant End_{F₂}, the
    symmetry of the bulk problem. This does not depend on which lift is chosen, since two lifts differ by the
    commutant;
  - **locality:** Λ₊ is kept by the centraliser of the puncture holonomy, so it is a sum of whole ±1 eigenspaces;
  - **W22's block rule (the control):** Λ₊ is the whole −1 eigenspace, so each doublet block counts +1 and each
    character block 0. This is W23's reading.
  - "The moves alone" is not used for the verdict: on a reducible bundle the lift is fixed only up to the commutant,
    so its invariant subspaces depend on a convention.
- **The anomaly:** SU(5)³ is free when n(10) = n(5̄).

## The cells

The script is `the_puncture_content.py`, writing `.json` beside it.

- **P1, the completion lemma (PROVED; exact).** Localized content with net numbers (a, b) (10s minus 10̄s; 5̄s minus 5s)
  cancels the five's anomaly only if a − b = 2. So the total is (3 + b, 3 + b), and three complete generations need the
  puncture's net 5̄ number b to be zero.
- **P2, the census.** The bundles L and R keep. By hand, five: χ₀⁵; χ₀² ⊕ P; D ⊕ χ₀³; D ⊕ P (the weave's five);
  D² ⊕ χ₀. (L and R permute the three parities transitively, so they must occur equally often.)
- **P3, the control.** W22's block rule gives (0, 0), (0, 0), (1, 3), (1, 3) and (2, 2). That is W23's SU(5) set.
- **P4, naturality.** For each bundle: the structure of the algebra the lifts and the commutant generate on S and on
  Λ²S, the index sets, and the anomaly-free counts. By hand:

  | bundle | n(10) | n(5̄) | anomaly-free |
  |---|---|---|---|
  | χ₀⁵ | 0, 5 | 0, 10 | 0 |
  | χ₀² ⊕ P | 0, 2, 3, 5 | 0, 1, 9, 10 | 0 |
  | D ⊕ χ₀³ | −1, 1, 2, 4 | −3, 1, 3, 7 | 1 |
  | D ⊕ P | −1, 1, 2, 4 | −3, −2, 0, 1, 3, 4, 6, 7 | 1, 4 |
  | D² ⊕ χ₀ | −2, −1, 2, 3 | −2, 1, 2, 4, 5, 8 | −2, 2 |

  - **Never three.**
- **P5, locality.** By hand: 0, 0, 1, 1 and ±2. Never three.
- **P6, what three would need, on the weave's five.**
  - n(5̄) = 3 is natural: 𝕎 = D ⊗ P at +3 (W28), with no +1 local solution of Λ²W kept.
  - n(10) = 3 needs dim Λ₊(W) = 4: one of D's two local solutions, or two of P's three. Neither is natural.
    - D's local solutions are irreducible under the lifts.
    - A natural plane in P's local solutions is spanned by two parity lines, which singles out a parity.
  - The plane x₁ + x₂ + x₃ = 0 is kept by the lifts with permutation-matrix entries (a convention), but not by the bulk
    commutant: it mixes the parity sectors.
  - **So three in the 5̄-sector needs the parities kept apart, and three in the 10-sector needs them mixed.** No one
    principle gives both. The script checks the plane: kept by the permutation lifts, not by the commutant.
- **P7, the verdict (predicted).**
  - **NEGATIVE.** No bundle built from the common point's blocks, with an end condition the weave keeps (naturality
    or locality), gives an anomaly-free three in F-HE.
  - The five's anomaly is cured naturally only at one or four complete generations: b = −2 or +1, never 0.
  - So in F-HE the puncture does not make three; GENESIS GAP2's place does not close the count there.
  - Three complete generations need a frame whose 10-sector holds 𝕎 (rank six), which is W27's six-dimensional
    reading with its link Λ.

## What each outcome means

- **As predicted.** The route through the puncture closes in F-HE for the common point's blocks. The record's best
  statement stays "derived given one stated link" (W27), with Λ as GENESIS FK11's question for main.
- **A natural or local three for some bundle.** The route reopens at once, under that bundle's own forcing question.
- **The control not W23's set.** The code is wrong. Fix it before anything else is read.
- **A different census.** Record it, and read P4 and P5 from the computed list.

## Seen before this was written

- **By hand:** P1; the census; P3–P6's tables, from the block structure (W28's naturality on 𝕎; the commutants of
  sums of distinct characters; Λ²(D ⊗ ℂ²) = χ₀ ⊗ ℂ³ ⊕ P).
- **The record:** W17, W22, W23, W27 and W28; main's S87 (B1607). No cell was computed before this rule.
