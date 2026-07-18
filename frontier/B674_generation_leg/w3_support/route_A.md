# ROUTE A — the Galois/eigenvalue derivation of the Φ·τΦ support classes
# (block eigenvalues ONLY; the Nahm state-integral is NOT used)
# Support pre-test of PREREG_W3_RUN (base 83c50a35). Exact arithmetic.

## Setup (fixed by the seal)

Gal(ℚ(ζ₅)/ℚ) = (ℤ/5)* = ⟨σ⟩ ≅ ℤ/4, σ: ζ₅↦ζ₅². Complex conjugation
c = σ² (order 2), subgroup H = ⟨c⟩ = {1,4}. Fixed field ℚ(ζ₅)^H = ℚ(√5).
The two Gaussian periods (H-orbit sums) are
  η₀ = ζ₅+ζ₅⁴ = (−1+√5)/2 = 1/φ     (classes {1,4})
  η₁ = ζ₅²+ζ₅³ = (−1−√5)/2 = −φ      (classes {2,3})
roots of t²+t−1. Block eigenvalues: φ^{4k}, k=−m..m, m∈{1,4,5,7,8,11},
all in ℤ[φ] ⊂ ℚ(√5). (φ = (1+√5)/2 = −(ζ₅²+ζ₅³), verified numerically.)

## Step 1 — the q-power class each block eigenvalue contributes (COMPUTED)

Using φ^j = F_j·φ + F_{j-1} and the reduced cyclotomic basis (constant
1 = −(ζ₅+ζ₅²+ζ₅³+ζ₅⁴)), the fractional-class support of every block
eigenvalue φ^{4k}, over ALL six blocks, is:

  every φ^{4k} (including k=0) occupies ALL FOUR classes {1,2,3,4}.
  e.g. φ⁴ = 2+3φ → coeffs (z¹,z²,z³,z⁴) = (−2,−5,−5,−2); φ⁰ → (−1,−1,−1,−1).

The ONLY powers of φ with clean single-period support are φ^{±1}, and they
sit on OPPOSITE orbits: φ¹=−η₁→{2,3}, φ⁻¹=η₀→{1,4}. The block set uses
φ^{4k} (φ⁰,φ^{±4},φ^{±8},…) and NEVER φ^{±1}. Union over all blocks = {1,2,3,4}.

## Step 2 — the pairing Φ·τΦ (τ: q↦1/q) symmetrizes (COMPUTED)

τ inverts the golden monodromy λ=φ²↦φ⁻², i.e. on eigenvalues φ↦1/φ,
so η₁=−φ ↦ η₀=1/φ: **τ SWAPS the periods {2,3}↔{1,4}.** Φ·τΦ =
Φ(q)Φ(q⁻¹) is τ-invariant by construction, so its support is τ-invariant:
it contains {2,3} **iff** it contains {1,4}. {2,3}-alone is impossible.

## Step 3 — the exact Galois argument (DECISIVE)

Two facts, both computed exactly:

(a) H-invariance. Every φ^{4k} is H-fixed (H fixes ℚ(√5)), so support is a
    union of H-orbits {1,4},{2,3}. This narrows the orbit but does NOT pick one.

(b) FULL-group invariance. σ(φ)=(1−√5)/2=−1/φ ⇒ σ(φ^{4k})=φ^{−4k}, and the
    multiset {φ^{4k}: k=−m..m} is k→−k symmetric ⇒ σ-STABLE. Verified for all
    six m; each block trace Σ_k φ^{4k} is a rational integer
    (8, 2584, 17711, 832040, 5702887, 1836311903 — Fibonacci). The eigenvalue
    data is ℚ-RATIONAL as a whole, hence invariant under ALL of (ℤ/5)*.

A Galois-covariant support determined by full-group-invariant data is a
full-orbit: σ-orbit of 1 is {1,2,4,3} = ALL FOUR. Support = {1,2,3,4} (or ∅).

## VERDICT (two-outcome): all-four — the pre-test does NOT select {2,3}

The ℚ(√5) block structure does **not** project the four-class orbit onto
{2,3}. The eigenvalue data fixes only the FIELD ℚ(√5) (⇒ H-invariance,
support a union of {1,4},{2,3}); it is otherwise ℚ-rational/σ-symmetric and
occupies both periods. The one class-distinguishing datum, η₁ vs η₀
(≡ φ vs φ⁻¹), is (i) not carried by any φ^{4k} — each occupies both periods —
and (ii) SWAPPED by the mandatory S²=c pairing τ. Landing on {2,3} alone
requires the Nahm quadratic-form linear shift (n²+n vs n², the H-side vs
G-side of Rogers–Ramanujan) — a state-integral datum Derivation A is
forbidden to use. The {2,3} that appears if one non-canonically reads the
rational part of φ^j as "class 0" is a basis artifact: the same reading hands
φ⁻¹ a clean {1,4}, and τ regenerates it. Base-rate discipline: near-miss = NO-HIT.

BLOCKER for {2,3}: the map {eigenvalue φ^{4k}} → {formal q-power class mod 5}
is NOT determined by the eigenvalue set alone (that set is k→−k symmetric,
hence full-Galois-stable and ℚ-rational). The {2,3}-vs-{1,4} selection lives
in the exponent/quadratic-form (state-integral) side, not the eigenvalues.
