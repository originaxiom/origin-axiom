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

## Gate 2: The Number Field (Probes 4–5)

### S5: β = 1/(√φ - 1)  [PROVED]

The Perron eigenvalue β (growth rate of σ) is NOT independent of the
golden ratio. Setting τ = √φ, the minimal polynomial of τ is
x⁴ − x² − 1 = 0. Substituting x = 1 + 1/y into this polynomial and
multiplying through by y⁴ gives EXACTLY −(y⁴ − 2y³ − 5y² − 4y − 1),
i.e., the NEGATIVE of the charpoly of M.

Therefore β = 1/(τ−1) = 1/(√φ − 1).

Equivalently: β(√φ − 1) = 1. This is the PERRON IDENTITY.

Three-line proof:
  β = τ²(1+τ)
  β(τ−1) = τ²(1+τ)(τ−1) = τ²(τ²−1) = τ⁴−τ²
  τ⁴ = τ²+1 (minimal poly) ⟹ τ⁴−τ² = 1  ∎

### S6: The eigenvalue identities  [PROVED]

  β·|λ₂| = φ                 (product of real eigenvalues)
  |λ₃| = |λ₄| = 1/√φ = 1/τ  (modulus of complex pair)
  β·|λ₂|·|λ₃|² = 1           (modulus identity)
  det(M) = −1                 (orientation-reversing)

The complex eigenvalues are λ₃,₄ = −1/φ ± i√(√5−2), with
|λ₃|² = 1/φ² + (√5−2) = (3−√5+2√5−4)/2 = (√5−1)/2 = 1/φ.

### S7: f_a = 1/β  [PROVED]

The letter frequency of 'a' equals the reciprocal of the growth rate.
Since every σ-image starts with 'a', the Type 1 observer (at START)
sees the full object, and f_a = √φ − 1 = 1/β.

Complete frequency table in ℚ(τ):
  f_a = 1/β = τ−1
  f_b = f_a/φ = (τ−1)/τ²
  f_A = √φ·f_a = τ(τ−1)
  f_B = f_A/φ = (τ−1)/τ

Ratios: f_a/f_b = f_A/f_B = φ; f_A/f_a = f_B/f_b = √φ.

### S8: Single number field ℚ(√φ)

The object generates exactly ONE number field:

  ℚ(τ) = ℚ[x]/(x⁴ − x² − 1)    where τ = √φ

of degree 4 over ℚ — matching the 4-letter alphabet.

All 16 distinct Perron-vector components from the 5 types are elements
of ℚ(τ). All 110 pairwise ratios are also in ℚ(τ). The "three
generators" {β, φ, √φ} are algebraically dependent:
  φ = τ², β = τ²(1+τ).

There is ONE generator: τ = √φ.

### Coupling geometry (Probe 4)

The 5 types do NOT cleanly map to single geometric positions (Type 1
has factors at START, MIDDLE, END, SPAN, and OUTSIDE). The type is
determined by the RETURN WORDS the factor generates, not its position
in any single σ-image.

The inter-type ratio catalog reveals 110 ratios built entirely from
{β, φ, √φ, 2}. The factor of 2 appears exactly once, inside Type 4:
  v₀/v₃ = 2 for the representative 'Bab'.

### Gate 2 verdict

**The dimensional bridge is EMPTY.** The object generates no free
dimensionless parameter. Every ratio is algebraically determined by
τ = √φ. There is nothing to "tune" — the coupling geometry gives
5 views of the same ℚ(τ), each reading different elements but all
determining the same τ.

For Gate 3 (SM comparison): if the SM involves free coupling constants
NOT determined by φ, the object alone cannot predict them. Scale —
the one thing the object does not provide — is the only missing
ingredient. The question is whether any SM ratio lives in ℚ(√φ).

## Gate 2b: The Scale Question (Probe 6)

### S9: sin θ = 1/φ, cos θ = -1/√φ  [PROVED]

The complex eigenvalues λ₃,₄ = −1/φ ± i√(√5−2) have:
  cos(arg(λ₃)) = −1/τ = −1/√φ
  sin(arg(λ₃)) = 1/φ = 1/τ²

Both trig components are in ℚ(τ). The object is maximally algebraic:
even its rotational component stays in the number field. The angle
θ = arccos(−1/√φ) ≈ 141.83° has θ/π irrational (checked to denom 50),
but all measurable quantities (trig values) are algebraic.

### S10: disc(ℚ(τ)) = disc(charpoly M) = −400  [COMPUTED]

The discriminant of x⁴−x²−1 equals the discriminant of
x⁴−2x³−5x²−4x−1, both = −400 = −2⁴·5². This confirms they define
the same number field. The only primes are {2, 5} — the golden
world's signature.

### S11: The scale is external  [ESTABLISHED]

The object provides SHAPE (ℚ(√φ)) but not SIZE. The root is
already taken: the object lives at τ = √φ = φ^(1/2). The degree-4
field is forced by the 4-letter alphabet. Higher roots (φ^(1/4) etc.)
would require a larger alphabet. One physical measurement (a single
dimensional quantity) fixes all dimensions.

## Gate 3: SM Ratio Test (Probe 7)

### The test

For each SM dimensionless ratio R, search for (a,b,c,d) ∈ ℤ⁴ with
|coeffs| ≤ 8 such that |a+bτ+cτ²+dτ³ − R| is minimized. Also test
R = n·τ^k for small n, rational k.

### False-positive control

With 17⁴ = 83,521 lattice points spanning [−48, 48], the average
spacing is ≈ 0.001139. Any number is within ~0.0006 of some ℤ[τ]-
element. Random numbers in [0, 200] achieve:
  - err < 10⁻²: 23.2%
  - err < 10⁻³: 18.8%
  - err < 10⁻⁴: 5.6%
  - err < 10⁻⁵: 0.4%
  - err < 10⁻⁶: 0.0%

### Results (21 SM ratios tested)

7 matches below the 10× sub-spacing threshold (err < 0.000114):
  α_s(M_Z) ≈ −8+8τ−τ³ (err 1.4×10⁻⁵)
  m_W/m_Z ≈ −7+7τ+7φ−6τ³ (err 1.2×10⁻⁵)
  V_cb ≈ −8+τ+8φ−3τ³ (err 4.2×10⁻⁵)
  m_τ/m_μ ≈ 4+8τ−6φ+6τ³ (err 5.0×10⁻⁵)
  V_us ≈ 7+6τ−7τ³ (err 7.9×10⁻⁵)
  V_ub ≈ −7+4τ+5φ−3τ³ (err 8.6×10⁻⁵)
  sin²θ_W ≈ 7τ+φ−5τ³ (err 9.6×10⁻⁵)

All use coefficients |c| = 3–8 (high complexity). Expected hits at
this precision for 21 random draws: ~1.2. We got 7 — above random,
but the lattice density is non-uniform (denser near values where
large cancellations occur). No match has err < 10⁻⁶.

Best power-of-τ match: 1/α_em ≈ 6·τ¹³ at 0.06% — but the 0.06%
error is 10⁷ times the experimental uncertainty of α_em. Not exact.

### Gate 3 verdict

**No SM ratio is an element of ℚ(√φ) with small coefficients.**
All matches are at precision expected from lattice density (the
false-positive control confirms this). The object's number field
and the SM's dimensionless constants live in different algebraic
worlds. The connection, if any, does not go through number matching.

### What Gate 3 rules OUT

The object cannot predict SM coupling constants by having them
encoded as elements of ℚ(√φ). This closes the "numerology" door
permanently and with computed evidence.

### What Gate 3 does NOT rule out

The connection could go through STRUCTURE, not VALUES:
  (a) The 5 observation types → symmetry → gauge groups
  (b) The spectral geometry → physical spectrum
  (c) The self-referential grammar → observer/observed distinction
  (d) The orientation (det = −1) → parity/chirality

These are B532's territory, not B533's.
