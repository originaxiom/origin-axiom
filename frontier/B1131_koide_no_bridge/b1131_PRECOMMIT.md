# P-KOIDE — PRECOMMIT (sealed before the Koide-side / bridge numbers are computed)

Written after STEP 0 (det φ's exact meaning, established below by independent
re-derivation from the banked artifact) and before STEP 1's numbers are run and
before any bridge-route numeric test is executed. Default verdict: NO-BRIDGE.
Overturned only by a forced, unfitted derivation of cos²α = 1/2 (45°), never by a
bare numerical equality to 2/3.

## STEP 0 result (established, not a prediction — done first per the seal's order)

`det φ = −2/3` is the determinant of the explicit 78×78 rational change-of-basis
matrix φ: L(𝕆_split,ℂ'_split) → "the build", both concrete bases for the (unique)
78-dim split E₆ Lie algebra (B904, `stage4c_phi.py`). Independently reloaded
`stage4c_phi.pkl` here and recomputed:

- `det(PHI) = -2/3` exactly (sympy exact rationals) — confirms FINDINGS.md.
- **New finding (this probe):** φ is EXACTLY block-diagonal once BS-native
  coordinates are grouped into {6 torus, 72 root} and build-native coordinates
  into {6 Cartan (h₁..h₆), 72 root}: the Cartan-rows × non-torus-cols block is
  the zero matrix, and the root-rows × torus-cols block is the zero matrix
  (checked on all entries). The 72×72 root block is a signed permutation matrix,
  **det = +1 exactly**. The ENTIRE −2/3 lives in the 6×6 block mapping BS's own
  torus basis (4 triality-diagonal so(8) directions + the 2-dim tri(ℂ′)) to the
  build's standard simple-coroot basis {h₁,...,h₆}: `det(6×6 block) = −2/3`
  exactly, and `det(72×72 block) × det(6×6 block) = −2/3` reproduces the total.
- The 6×6 block's characteristic polynomial is `6x⁶−11x⁵−8x⁴+5x³+10x²−2x−4`
  (irreducible-looking, checked numerically), eigenvalues/singular values all
  irrational algebraic numbers (≈ 0.50, 0.61, 0.63, 0.82, 1.09, 3.83 for the
  singular values) — **no eigenvalue or singular value near cos45°=1/√2≈0.7071
  or any other angle-suggestive constant**. Checked explicitly, adversarially,
  before writing this file.

**Conclusion of STEP 0:** det φ is a fact about a 6-DIMENSIONAL basis change on
E₆'s Cartan subalgebra (rank 6) — comparing the object's own "geometric" torus
(from triality) to the textbook "combinatorial" simple-coroot torus. It contains
no 3-dimensional real vector, no inner product with (1,1,1), no cosine, no angle.
This is a STRUCTURAL fact about E₆'s rank-6 root/coroot lattice geometry (the
denominators 2 and 3 are E₆'s own pervasive primes: |Z(E₆_sc)|=3, Coxeter number
12=4·3, |W(E₆)|=2⁷·3⁴·5, dim 78=2·3·13) — unrelated in kind to a mass-vector's
direction cosine to the democratic line in ℝ³. This alone is strong evidence for
NO-BRIDGE, independent of anything about Koide.

## STEP 1 (to run in koide.py): verify Q=2/3 ⟺ α=45° classically with PDG masses
Standard, not in dispute; included for completeness and to anchor the geometry
that any bridge route must reproduce (α=45°, not merely the number 2/3).

## STEP 2 — candidate bridge routes, PRE-COMMITTED (exactly these four; no others
## will be tried; no new object quantity will be reached for once Koide's number
## is in view — this is the fishing guard, per the repo's own BASE_RATE_PRINCIPLE)

**(a) The trit (B897/B1030): the 27 = three 9-blocks, triality-cyclic (order 3).**
The ONLY natural 3-vector this structure supplies without any further choice is
the block-DIMENSION vector (9,9,9) (all three blocks have dimension 9 — B897's
own table). Test: Q and α for (9,9,9). Prediction: α=0° exactly, hence Q=1/3
exactly (the MINIMUM of Koide's Q, since Q∈[1/3,1) for positive reals — the
democratic point is the ANTIPODE of Koide's α=45° point on the same circle,
not a coincidence toward it) — because a bare ℤ/3 permutation symmetry, absent
any further input, forces the fully democratic point, not a 45°-tilted one. Secondary check: the
su(2)′ refinement (3+6 split) applies to only 2 of the 3 blocks (the third is
single-valued) — so no well-defined SECOND 3-vector exists in this data at all.
Casimirs (C_c=C_f=4/9, C_w=3/8) are cross-sector invariants (color vs flavor vs
weak), not a 3-tuple indexed by the three blocks — no natural vector there
either. Predicted verdict: route (a) supplies no candidate that is not either
(i) trivially democratic (α=0) or (ii) not a well-defined 3-vector at all.

**(b) det φ = 1/(3cos²α) read backward.** Solving cos²α = 1/(3|det φ|) for
|det φ|=2/3 gives cos²α=1/2 by pure arithmetic — true for ANY quantity that
equals 2/3, with zero dependence on what det φ actually is. This is the bare
equality the seal explicitly DISQUALIFIES. Predicted verdict: disqualified by
construction, regardless of what the arithmetic shows (it "succeeds" trivially,
which is exactly why it fails as a bridge — it has no discriminating power).

**(c) The 27's Jordan structure — the one sealed, forced, unfitted rank-3
element on record: v0 (B663/B670 arc A1).** N(v0,v0,v0)=−6≠0, sharp(v0)∝v0,
support = 3 of the 27 coordinate indices {12,13,14}, values (1,−1,1). Test:
angle of (1,−1,1) to (1,1,1). Prediction: NOT 45° (arccos(1/3)≈70.5°,
cos²α=1/9). Flagged BEFORE computing: this comparison is likely not even
principled — indices 12,13,14 are raw basis-coordinate slots in whatever
convention B854/B663 used for the 27, not a verified Peirce/eigenvalue
decomposition of v0 (that would need v0's trace + quadratic-invariant
functionals, not banked in a1_results.json — named as the uncomputed datum if
this route is the only thing keeping the verdict open). A failure here is a
DOUBLE failure if so: not principled AND not numerically 45°.

**(c′) φ's own eigen/singular structure (already computed under STEP 0 above,
folded in here since it answers the "any eigenvalue/angle of φ" clause).**
No eigenvalue or singular value of the 6×6 nontrivial block is near 1/√2 or any
other angle-suggestive algebraic number. Route closed.

## STEP 3 — the kill test (applied to whichever route, if any, looks promising)
1. Hidden fitting? — any free choice (which block invariant, which basis
   convention, which normalization) that was steered toward 2/3 disqualifies.
2. Geometry or number? — must reproduce cos²α=1/2 as a forced identity, not
   reproduce "2/3" as a bare value.
3. Base-rate: compute the density of {2,3}-smooth low-height rationals (koide.py)
   as the "how cheap is landing exactly on 2/3" control, consistent with the
   repo's own base-rate-first principle (`BASE_RATE_PRINCIPLE.md`).

## Non-fishing commitment
Only routes (a),(b),(c),(c′) above are tested. If all fail, the verdict is
NO-BRIDGE — no further object-side quantity will be reached for post-hoc.
