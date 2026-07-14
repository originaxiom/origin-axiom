# B581 — THE SIX TORSIONS: the jewel spectrum computed, and the sign of chirality

**Date:** 2026-07-14. **Reproducer:** `six_torsions.py` (~8 min; the trivial-rep control
must reproduce the classical Alexander t²−3t+1 and the (t−1) denominator before any block
runs). **Data:** `six_torsions_results.json` (exact coefficients). **Locks:**
`tests/test_b581_six_torsions.py` (fast, from the committed data + the m=1 analytics) and
the full rerun gated behind OA_SLOW. **Blind protocol:** the six polynomials were computed
and dumped before any jewel comparison; everything below the line "THE SPECTRUM" is the
post-computation comparison phase.

## THE SPECTRUM

The twisted Alexander polynomials Δ_m(t) of the figure-eight at Sym^{2m}(ρ_geo), one per
E₆ exponent m ∈ {1,4,5,7,8,11} (Wada formula on ⟨a,b | aWb⁻¹W⁻¹⟩; exact over ℚ(√−3);
division exact in every block — the Wada invariants are honest polynomials). All six have
INTEGER coefficients (Galois symmetry ρ̄ ≅ ρ∘φ forces ℚ), all are skew-palindromic
(c_k = −c_{deg−k}; Milnor duality), and all vanish at t = 1 (forced by the six deformation
directions, dim H¹ = 1 each). The torsions τ_m = Δ′_m(1):

| m | τ_m | factorization | sign | θ-parity |
|---|-----|---------------|------|----------|
| 1 | **−3** | −3 (**= the banked B425 value — the analytic gate**) | − | even |
| 4 | 260736 | 2⁷·3·7·97 | **+** | **odd** |
| 5 | −165110400 | −2⁷·3⁴·5²·7²·13 | − | even |
| 7 | −3257341296168960 | −2¹²·3⁴·5·7⁵·11·13·19·43 | − | even |
| 8 | 100636318520821923840 | 2¹⁴·3³·5·7³·11·13·31·607·49297 | **+** | **odd** |
| 11 | −6.9081…×10³⁶ | −2²¹·3⁷·5·7⁶·11²·13²·17·19·73·149·151·1471·160453 | − | even |

## THE SIGN LAW (the headline)

> **sign(τ_m) = (−1)^m = −θ(m): the torsion is positive exactly at the θ-odd exponents.**
> B353's grading formula (−1)^{m+1} on H¹ is readable, term by term, in the SIGNS of six
> scalar invariants. The chirality fold has a scalar signature.

Normalization-consistent (all six normalized identically — monic; relative signs
meaningful). Null: 1 of 64 sign patterns (p ≈ 1.6%) — but the law is likely PROVABLE:
dim V_{2m} = 2m+1 ≡ 1 mod 4 exactly for the θ-odd m (9, 17) and ≡ 3 mod 4 for the θ-even
(3, 11, 15, 23), so the sign plausibly follows from duality + dimension parity. Registered
as the proof target (with the honest alternative: a unit-convention coincidence — the
proof or the fence, one of the two).

## The comparison phase (jewels vs the spectrum)

- **m = 1 factors as (t−1)(t² − 5t + 1): the BTZ quadratic** — its root is exactly the
  banked B520 entropy value log((5+√21)/2), and √21 = √(3·7) connects to the apparition
  set (buried item A6). Unforced: found before any comparison was run. (Lit note: the
  adjoint twisted Alexander of 4₁ is known — cross-cite Dubois-Yamaguchi at write-up.)
- **7 saturates the tower**: 7 | τ_m for every m ≥ 4, with exponents (1, 2, 5, 3, 6) —
  the L74 norm-7 vein (N(tr ρ(ab)) = 7 = the sine-kernel modulus) now has a torsion-side
  presence in every window. Pattern registered, mechanism open.
- **The charge 11 enters at m = 7** (then 8, 11 — with 11² at m = 11). The level-1
  modulus 13 enters at m = 5. τ₅ is remarkably smooth ({2,3,5,7,13} only).
- The other listed jewel numbers (2/3, 15/169, the golden and D₄ and ζ₉ polynomials) do
  **NOT** appear as factors or values — honest negatives of the blind comparison; the
  "jewels = torsion ratios" guess is not supported at this level.
- The middle factors form a reciprocal-quadratic family (t²−5t+1 at m=1; t²−26t+1 inside
  m=4; higher reciprocal factors beyond) — the unit-trace ladder {5, 26, …} is a new
  object, unregistered until understood.

## What this is

The first genuinely new jewel-FAMILY since e₃: the object's full torsion spectrum through
the principal embedding — six exact polynomials, six integers, one sign law that reads
the fold. It does not "unify the jewels" in the ratio sense proposed (that guess died
honestly); it does something better: it gives every deformation direction its own
arithmetic fingerprint, with the chirality grading stamped on the sign. The chord program
(B580 L72 phase 1) now has its S₁-layer computed exactly; the DGLZ S₂-ladder sits above it.

Firewalled. Nothing to CLAIMS.md.
