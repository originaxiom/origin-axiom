# B908 LEG 3 — DRAFT NOTES: the vanishing mechanism (in progress)

Append-notes for register item B908-leg-3. Computation agent, 2026-08-05.
Script: `leg3_mechanism.py` (phases A/B/C/D/E/K + this session's V/G/R/T/F);
results assembled into `leg3_results.json`. Everything below is exact
(mod-p integers or sympy Rational); nothing floats.

## 0. Pre-computed theory anchors (exact over ℚ, independent of the pipeline)

Three facts established before touching the pipeline, on the ABSTRACT 3×3 grid
(atoms = cells (u,v); couplings = the 3 rows and 3 columns — the two pencils of
AG(2,3) lines the solo seat identified):

1. **Leibniz in grid coordinates.** Relabel the cells of a 3×3 matrix by
   (which even transversal contains the cell, which odd transversal contains
   it) — a bijection. Under it the six determinant transversals become exactly
   the three grid-rows (+1 each, the even permutations) and the three
   grid-columns (−1 each, the odd permutations):
   **det = Σ_rows ∏ − Σ_cols ∏.** A rows+cols-supported cubic is det-type iff
   its pencil-product ratio I := ∏(row couplings)/∏(col couplings) = −1.
2. **The 16-vs-4 dichotomy (the non-circular discriminator).** For a cubic
   supported on rows+cols with all six coefficients nonzero, the stabilizer
   (derivation) algebra in gl₉ has dimension **16** (= sl₃⊕sl₃⊕traceless glue,
   the det-orbit) **iff I = −1**, and dimension **4** (the balanced torus)
   otherwise. Verified exactly over ℚ: det pattern → 16; permanent pattern
   (I=+1) → 4; random rational coefficients (I=64/5) → 4; random coefficients
   forced onto I=−1 → 16.
3. **Invariant cubic is unique.** The 16-dim stabilizer of the det pattern
   annihilates a **1-dimensional** space of cubics in the 165-dim cubic space
   (verified exactly over ℚ). So ANY cubic invariant under such an algebra in
   the grid frame is a scalar multiple of det — the classical FFT statement
   "SL₃×SL₃-invariant cubic on 3⊗3̄ ∝ det", concretely re-verified in our
   coordinates.

Also pinned: the tower first components r at both full-tower primes satisfy
**μ₁₃(x) = 500716339200x³ − 2075673600x² − 4769856x + 2197** (B866's cubic in
the ρ = 13t normalization) — the three labelings are the three conjugate
μ-roots, at 40123 and 40639 alike.

## 1. Verification pass (phase V, all 7 full-tower primes)

At 40123, 40639, 40693, 40897, 40903, 40927, 40939: every atom lies in the
three cells its label names; the 27 colorless cells ↔ 27 atom-slots is a
bijection (each cell in exactly one atom); the full 84-triple support
recomputation equals the stored 6 couplings; the coupling graph is K₃,₃;
I ≡ −1 and v ≡ 0. All re-derived from the pickled states, exact mod-p.

## 2. The grid is canonical (phase G, all 7 primes)

- **The S-line.** Each labeling has exactly one colorless cell in the '1'
  part (tag S). The three S-atoms always form ONE coupling — a pencil line.
  Call its pencil the ROW pencil. The other pencil's lines each contain
  exactly one S-atom (forced by K₃,₃).
- **Columns are labeling-indexed.** Every atom off the S-line contains a
  UNIQUE H-cell; the three atoms of each column draw their distinguished
  cell (S or the unique H) from ONE labeling, and the three columns
  exhaust the three labelings. Since the labelings are the three conjugate
  μ₁₃-roots (phase K, all 7 primes), **the column pencil is root-indexed**.
- **The non-S rows have EQUAL couplings** at every one of the 7 primes
  (e.g. 1861=1861 at 40123, 14962=14962 at 40639, 349=349 at 40693).
- **Zero-sum certificates.** The 9 atoms are joint eigenlines of the 12
  exact torus operators (X1, Ym, W3, combo per labeling). For every one of
  the 159 non-coupling cubic multisets, some operator has a NONZERO
  eigenvalue-sum mod p (159/159 at each prime). Since a nonzero reduction
  certifies a nonzero characteristic-0 eigenvalue-sum, and the cubic is an
  exact invariant, **the char-0 restricted cubic vanishes on all 159
  non-grid multisets** (under the standing reduction assumption); on the 6
  couplings all 12 eigenvalue-sums vanish (consistency). The support is
  exactly the two pencils in characteristic 0, not just mod p.

## 3. Galois preserves the pencils — the swap is NOT a Galois transposition

The design's leg-3 guess named two candidate sources for the involution: a
Galois transposition through B900's twists, or a frame symmetry. The grid
structure decides it: any Galois element permutes atoms, maps couplings to
couplings, and fixes the S-atom set (the S-tag is the Q-rational
multiplicity-structure class), hence fixes the S-line, hence preserves the
row pencil and (K₃,₃ bipartition uniqueness) the column pencil. Galois acts
by permuting the COLUMNS through the μ-root indexing (B900's diagonal
S₃ picture) and at most swapping the two non-S rows — consistent with their
equal couplings. **No Galois element swaps the pencils.** Consequently
∏(rows) and ∏(cols) are each fully Galois-stable, sharpening leg 1
(v ∈ ℚ and u ∈ ℚ, and in fact P_R ∈ ℚ, P_C ∈ ℚ separately).

## 4. The mechanism: det-type cubic, frame involution J, Leibniz parity
   (phase D, re-verified at 40123 AND 40639)

- The gl₉ stabilizer of the restricted cubic has dimension **16** at both
  primes (= sl₃⊕sl₃, the det orbit). Controls at both primes: random
  couplings on the same support → 4; permanent pattern → 4; torus twist of
  the actual couplings → 16.
- **Det-frame:** an explicit atom rescaling takes the six couplings to
  (+1,+1,+1,−1,−1,−1) (rows +1, cols −1). Its existence is equivalent to
  v ≡ 0 (consistency gate ∏(1/c_row) = ∏(−1/c_col)), which holds.
- **The involution J:** in the det-frame, the grid transpose (3 fixed atoms
  = the diagonal, three 2-cycles) satisfies **cub(J·,J·,J·) = −cub on all
  165 multisets** and swaps the two pencils. So J maps each row coupling to
  MINUS a column coupling: ∏(rows) → (−1)³·∏(cols), i.e. **v = 0 is the
  odd orientation count** — three −1's, one per line.
- **Parity source (exact, abstract):** under the Leibniz relabeling
  (phase T, symbolic over ℤ) the row pencil is the three EVEN permutation
  transversals of a 3×3 determinant and the column pencil the three ODD
  ones; det = Σ_rows ∏ − Σ_cols ∏. J is composition with a transposition;
  the −1 is ε(transposition) — the Leibniz sign. Note J maps the S-line
  (3 S-atoms) to a column (1 S-atom): J is frame-level (Weyl-type), not
  induced by any Galois or label symmetry — closing section 3's dichotomy.

## 5. Theory anchors made rigorous (phase T, this session)

- Leibniz relabeling: exact symbolic identity over ℤ.
- det-pattern stabilizer: 16 explicit sl₃⊕sl₃ derivations kill det exactly
  (integer arithmetic), independent (rank 16), and the mod-p nullity is 16
  ⟹ **dim_ℚ = 16 proven** (lower = exact derivations, upper = mod-p).
- permanent-pattern stabilizer: exact torus d_ij = α_i+β_j, Σα+Σβ=0 gives
  4; mod-p nullity 4 ⟹ **dim_ℚ = 4 proven**.
- Uniqueness: the cubics annihilated by the 16-dim algebra form a space of
  mod-p dimension 1, and det is an exact member ⟹ **dim_ℚ = 1 proven**:
  any cubic invariant under an sl₃⊕sl₃ in this frame is a multiple of det.
- Random-coefficient control: I = 12/55, stabilizer 4.

## 6. CRT rationality status (phase R, 7 primes) and what remains

Aligned canonical-frame couplings across all 7 primes (class-pattern
alignment, pivots consistent, v ≡ 0 in the aligned frame everywhere;
c_row1 ≡ c_row2 at every prime). With M ≈ 1.9e32 (bound 9.6e15): the
individual couplings, the pencil symmetric functions, and P_R, P_C do NOT
reconstruct convincingly — every "success" has height at the bound with
spurious-gauge O(0.3–0.6), so we do NOT claim those rationals ("v = 0"
reconstructs trivially; P_C = −P_R is automatic from v ≡ 0 mod M). The
7-prime modulus is simply too small for these heights.

**What remains for full exactness (the honest list):**

1. **The char-0 det-type certificate** — exhibit the sl₃⊕sl₃ inside the E₆
   derivation algebra exactly over K = ℚ[r]/μ₁₃, stabilizing the 9-atom
   space as 3⊗3̄. With section 5's uniqueness this forces cub|₉ ∝ det,
   hence I = −1 and v = 0 EXACTLY — no height bound ever needed. This is
   the registered continuation target.
2. Alternative (brute): more full-tower primes (the leg-2 tower
   derivation) until the CRT modulus clears the coupling heights.
3. The standing assumption that the mod-p pipeline is the reduction of the
   char-0 construction (leg-1 territory); all 7-prime structural
   consistency above corroborates it.

Section-2's zero-sum certificates already lift ONE piece to char 0
unconditionally-modulo-(3): the support is exactly the two pencils. What
mod-p data can never do alone is pin the VALUES; item 1 is the route that
never needs them.
