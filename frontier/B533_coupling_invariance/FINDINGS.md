# B533 — Coupling Invariance: Findings

## Gate 1 Verdict

**The coupling is NOT a gauge choice. It carries exactly 5 discrete
algebraic fingerprints.**

## The 5 Types (stable across depths 8–11)

34 observation points (factors u of length 1–4) cluster into 5 types,
determined by the Perron eigenvector of the induced return-word
substitution. The classification is STABLE: identical at depths 8, 9,
10, 11 (counts 9/7/2/2/1 for length ≤ 3).

### Type 1 (14 points) — THE IDENTITY

Self-recovery: 7/14 reconstruct σ itself (canonical codes match).
Return words from u='a' are exactly the substitution images:
  R₀ = abAB = σ(A), R₁ = aA = σ(B), R₂ = abAAB = σ(a), R₃ = aAB = σ(b)
Perron vector = **(f_A, f_a, f_B, f_b)** — the global letter frequencies.
Gap labels: f_A, 1/φ, 0.832.

### Type 2 (10 points) — THE λ₂ TYPE

Perron vector components (as ℤ-combinations of letter frequencies):
  v₀ = **f_a + f_b** = |λ₂| = 0.440137
  v₁ = **f_a** = 0.272020
  v₂ = **f_B** = 0.213849
  v₃ = **f_A − f_a** = 0.073995
Gap label 1 = |λ₂|: the second eigenvalue appears as a return-word frequency.

### Type 3 (4 points) — THE CROSS-MIXING

  v₀ = **f_a − f_b + f_B** = 0.317751
  v₁ = **f_b + f_A − f_B** = 0.300283
  v₂ = **f_B** = 0.213849
  v₃ = **f_b** = 0.168117
Pair sum f_a + f_A = 1/φ is preserved; f_b, f_B are preserved individually.

### Type 4 (3 points, rc=5) — THE EXTENDED TYPE

5 return words (extra zero eigenvalue). Components:
  v₀ = **−f_a + f_A + f_B** = 0.287843
  v₃ = **2f_a + f_b − f_A − f_B** = 0.152294
  v₄ = **−f_a − f_b + f_A + f_B** = 0.119726

### Type 5 (3 points) — THE IRRATIONAL MIXING

v₁ = f_a (preserved), but v₀, v₂, v₃ are NOT ℤ-linear combinations of
letter frequencies (best error ~5×10⁻⁴). This type involves irrational
mixing coefficients within ℚ(√5, √(2+√5)).

## Structural Theorems

### S1: Eigenvalue universality
All 34 observation points give the SAME eigenvalue spectrum
{β, λ₂, λ₃, λ₄} = {3.676, −0.440, −0.618, −0.618} (rc=4 types) or
{β, 0, λ₂, λ₃, λ₄} (rc=5 type). The spectral identity is intrinsic.

### S2: Q-conjugacy, non-GL(4,ℤ)-conjugacy
The charpoly x⁴−2x³−5x²−4x−1 is irreducible over ℚ (Galois group D₄).
All 5 incidence matrices are ℚ-conjugate (same rational canonical form)
but are NOT GL(4,ℤ)-conjugate (the conjugating matrices have non-integer
entries, residual ≈ 0.5). They are genuinely different over ℤ.

### S3: ℤ-mixing law
For Types 1–4, every Perron eigenvector component is a ℤ-linear
combination of the 4 global letter frequencies (f_a, f_b, f_A, f_B),
with error < 4×10⁻⁷. The transformation between types preserves pair
sums:
  T1 → T2: preserves (f_a, f_B), mixes (f_A, f_b) with Δ = f_a+f_b−f_A
  T1 → T3: preserves (f_B, f_b), mixes (f_A, f_a) with Δ = f_b−f_B

Type 5 partially breaks this: 3 of 4 components involve irrational
coefficients within the number field.

### S4: Self-recovery
7 of 34 observation points reconstruct σ's canonical codes exactly.
All 7 are in Type 1. All 7 factors contain the substring 'AA' or
are the single letter 'a' (which sees σ's images directly because
every image starts with 'a').

## What the Coupling Carries

| Quantity | Verdict | Notes |
|---|---|---|
| Perron eigenvalue β | **UNIVERSAL** | Same for all u |
| Full eigenvalue spectrum | **UNIVERSAL** | {β, λ₂, λ₃, λ₄} same |
| Charpoly | **UNIVERSAL** | x⁴−2x³−5x²−4x−1 always |
| Letter frequencies | **UNIVERSAL** | By partitioning (trivial) |
| Return count (rc) | **VARIES** | 4 or 5 (2 values) |
| Perron eigenvector | **VARIES** | 5 distinct types |
| Return-word gap labels | **VARIES** | 5 distinct sets |
| Canonical codes | **VARIES** | self vs non-self (2 classes) |
| GL(4,ℤ) class of A_u | **VARIES** | 5 distinct classes |

## Implications for the SM Question

1. **Letter-level physics is coupling-free.** The 5 forced ingredients
   (time, randomness, matter, continuity, thermodynamics) survive all
   34 observation points. They don't depend on how you observe.

2. **Return-word-level physics is coupling-dependent.** The effective
   "species frequencies" at the return-word scale depend on which of
   the 5 types your observation selects.

3. **The coupling is algebraically constrained.** It's not a free
   parameter — it selects from exactly 5 options, 4 of which are
   ℤ-mixing of the global frequencies. The coupling PRESERVES pair
   sums (conservation laws) while redistributing within pairs.

4. **The coupling space is finite but non-trivial.** 5 types, each
   with a specific algebraic fingerprint. Whether these 5 fingerprints
   map to physical observables is Gate 2 (the dimensional bridge),
   which requires specifying what physical measurement corresponds
   to which observation type.

## Gate 2 Preview

The natural next question: what IS the dimensional bridge? The 5 types
give 5 sets of dimensionless ratios. If any of these ratios matches a
known physical ratio, that constrains which type corresponds to which
measurement. But this requires:
  (a) A specific physical coupling to test against
  (b) A way to assign dimensions (the object has none)
  (c) A discriminating fact — not just "this number is close to that"

The firewall stands: no numerology, no SM-matching without a derivation.
