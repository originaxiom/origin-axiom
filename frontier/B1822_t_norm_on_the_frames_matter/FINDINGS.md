# B1822 — T-NORM ON THE FRAME'S MATTER (P-525, P-510's pre-seal condition; data-free): FR-FIB'S MATTER ZERO MODES GIVE THE GENERATION GRAM MATRIX G = H·‖F_x‖², SO T-NORM HOLDS EXACTLY IN THE CHOSEN METRIC H = I, WHICH IS THE ONE THE CENSUS USES. BUT THE FLAT STRUCTURE LEAVES H FREE — 8 REAL PARAMETERS PER FIELD (2 UNDER THE DIAGONAL SU(2) THE FRAME'S HOLONOMY LIES IN) — AND THE OUTPUTS MOVE WITH IT: "NO NEW FREEDOM" IS FALSE FOR THE FLAT STRUCTURE, AND H = I IS A CHOSEN INPUT. B1654 § 1.11'S ARGUMENT PROVES AT BEST A DIAGONAL H

**Verdict: PROVED** (a theorem and its computation). T-NORM holds in the chosen metric H = I. That metric is FR-FIB's
typing, a counted CHOSEN input on Step B's card, unless a typing that forces it is derived. Data-free; no measured value
is read. cc (main), 2026-10-30. Refereed hostile before landing: PASS WITH CORRECTIONS, four blocking findings applied
(§ 6).

**0 of 19.**

## 1. The modes (read from the frame's code)

- **A field of charge q** (6Y: Q 1, u −4, d 2, L −3, e 6), on the line w = p₁τ − p₂, has twist (a, b) = (q p₁, −2q p₂).
- **Its zero mode is one doublet F_x** = (θ[a,b](z; 2τ)/√θ₁(z; τ), e^{iπb} θ[a,b](z+τ; 2τ)/√θ₁(z+τ; τ)), on a flat
  degree-0 rank-2 bundle with a branch point at the puncture. Its monodromy is quaternion-type (Q₈).
- **The three generations** are F_x times the constant blocks C_p ∈ {QJ, QI, QK}.
- **Sources:** `b1656_funcs.py` (B1691's correction folder); the census evaluator (B1821's folder); B1642's residue
  coupling. The referee's independent implementation confirms that the census's `coupling()` is exactly
  (C_aF_x)ᵀεS(C_bF_y) in this basis (to 1.6 × 10⁻¹⁴). So the census's plain SVD is physical exactly when H ∝ I.
- **The modes are not magnetised-torus thetas.** ∣F_x∣² is doubly periodic, so the physical L² metric is the flat one.

## 2. Computed (`verification/tnorm.py` → `tnorm_results.json`, `refine.py` → `refine_results.json`)

- **In H = I:**
  - 1 170 configurations over 306 twist classes: 9 values of τ (from i to 0.3 + 6i), 26 lines (the zero line, all ten
    (2/5, k/10), six order-4 lines, and lines of orders 2, 3, 7, 9 and 12), and all five fields;
  - the diagonals exactly equal;
  - the off-diagonals over the four-fold cover at most 2.0 × 10⁻¹² at order 32, and 10⁻¹⁵ refined.
- **What this test checks.** Over the cover the Gram matrix is ‖F‖² times the blocks' quaternion Gram, so the test can
  fail only through a code or quadrature error. It is a consistency check of the instrument, not an independent physics
  test. The referee reproduced every stored number from a copy and with an independent implementation sharing no code
  (‖F‖² to 7 × 10⁻¹³).
- **The single-cell 0.99985** is the mode's nearly constant doublet direction over one cell (eigenvalues 7 × 10⁻⁵ and
  0.99993). It is not a kinetic coefficient: it changes sign from cell to cell (to 4 × 10⁻¹⁶).
- **Controls.**
  - Positive: the puncture quadrature against a 30-digit polar reference (7 × 10⁻¹⁶); magnetised-torus modes
    orthonormal on three cells (≤ 1.3 × 10⁻¹⁵).
  - Negative: a basis ψ₁ + 0.3ψ₀ returns 0.287348 as predicted; a rotated block returns sin 0.3. One control's
    prediction label was corrected after the run, and its values did not change (disclosed).

## 3. The theorem, and the freedom it exposes

- **G = H·‖F_x‖²** for any hermitian metric compatible with the flat structure, where H is the metric's positive 3 × 3
  matrix in the intertwiner basis C_p C_q⁻¹. T-NORM holds if and only if H ∝ I. That is a property of the metric, never
  of the modes, τ or the line.
- **The real dimension of the allowed H, by typing** (the referee's computation; the arc's first draft had only the
  first and the last):

  | typing | real dimension of H |
  |---|---|
  | the flat structure alone | 9 |
  | characters imposed on the generation index | 3 |
  | a product metric | 3 |
  | the diagonal SU(2), where the frame's holonomy lies | 2 (it allows democratic mixing) |
  | SU(2) × SO(3) | 1 |
  | characters plus the order-3 automorphism | 1 |
  | the cover typing (generations as the deck components) | 1 |

- **So the flat structure leaves 8 real parameters per field** after the overall scale: 40 across Q, u, d, L, e, or 8 if
  one H serves every field. H = I is forced only by the three one-dimensional typings, and none of them is derived on
  the record.
- **The outputs move with H** (the referee's check):
  - a 10% weight on one mode moves the mass ratios by 0.007 decades;
  - a democratic mixing of 0.1 moves them by 0.045 decades and the CKM moduli by 0.08.

## 4. What it means

- **The census stands, for FR-FIB with H = I.** It computes in exactly that metric. Its outputs are those of the frame
  as typed, and they change if H changes.
- **For P-510's ruling and Step B's card:**
  - "no new freedom" is false for the flat structure;
  - H = I is a CHOSEN input, counted on the card;
  - the null worlds share it, so it cancels in p₂ and p_K but not in the framework's length;
  - a typing that forces it, derived (P-531), would remove the input.
- **B1654's argument** (PREREGISTRATION.md § 1.11, lines 158–164; FINDINGS line 108 restates it) has three steps, and
  they grade differently:
  1. "No invariant pairing" is false for the matter. The generation bundles are isomorphic.
  2. "The discrete charge forbids it" holds only as a typing, and then H is diagonal.
  3. "The diagonal is ‖F‖², since C_p is unitary" assumes the generations share one normalisation. The diagonal typing
     leaves three free scales.

  So it proves at best a diagonal H, not ‖F‖²·I₃. It is true for the Higgs channels, which carry four distinct
  characters.
- **What rests on it,** each to get a dated note at this landing or a row:
  - P-109, P-112 and P-146. P-146's dismissal of the web seat's weight on one mode is refuted: H = diag(1, 1, κ) is
    admitted.
  - B1645's claim line ("T-NORM, by hand at B1654 1.11").
  - I-33.
  - B1643's C2.
  - P-510's ruling, its points 2 and 7 and its consequence line.
  - The two 2026-10-15 relays to all seats: a correction relay is owed, to the web seat first.

## 5. Scope

- FR-FIB's matter as the census evaluator builds it.
- The theorem covers every τ and line; the typing table is computed for the flat structure's symmetries.
- Which typing is physical is the open question (P-531).
- "T-NORM" here is P-510's sense, the generations' kinetic normalisation. An unrelated THEOREM_REGISTRY entry shares the
  name.

## 6. The referee (hostile, read-only; main's verification)

| item | verdict |
|---|---|
| the modes and the census's basis | HOLDS: an independent implementation reproduces the coupling to 1.6 × 10⁻¹⁴ |
| the theorem G = H‖F‖² | HOLDS |
| the numbers | REPRODUCED: every stored number from a copy (difference 0.0), and by independent code |
| the consequence for P-510 (blocking) | CORRECTED: the freedom of H and its effect on the outputs stated; "no new freedom" false; H = I CHOSEN; the census's scope |
| B1654's error (blocking) | CORRECTED: placed at its preregistration § 1.11, its three steps graded; P-146 refuted |
| the dependents (blocking) | CORRECTED: B1645, I-33, B1643 C2, P-510's ruling and the 2026-10-15 relays added |
| "forced only under the cover typing" (blocking) | CORRECTED: the typing table |
| non-blocking | applied: the identity nature of the check; 306 twist classes; W49 (P-087) cited; the name collision noted |

## Seen first

- P-510 and P-525; B1654's preregistration § 1.11 (the hand argument); B1643 C2; B1642.
- The SM seat's W49 (P-087) stated the generation bundles' isomorphism two days before B1654.
- The web seat's P-510 note raised the question (harvest row 1503).
- `VERDICT topic-sweep /T-NORM|kinetic normalisation|Gram matrix of the (matter )?zero modes|generations' metric/: 10 of 1568 arcs on main match (OPEN 1, PROVED 9); 8 register rows match (DONE 5, QUEUED 3)`

**The literature:** the orthonormality of theta functions with characteristics under the bundle's hermitian metric is
classical (the magnetised-torus case; Cremades, Ibáñez and Marchesano). This frame's modes are not of that type, and § 3
replaces it.
