# FINDINGS D — CC2 (Cell D: chat1's Q3/Q5, advisory)

Seat cc2, read-only/advisory. Repo untouched (no git operations performed).
Prereg cited: `MASTERPLAN_AND_PREREG.md`, sha256 =
`a06a1b074f22548d5d875baa8845914ca98bb007e5f789d6190df216d24cf6b6`
(verified by local `shasum -a 256` against the file at
`<cc2-seat>/seat-work/metallic_hearing_campaign/MASTERPLAN_AND_PREREG.md`
— matches exactly).

**Firewall (Gate 5), stated up front:** everything below is a σ-distance and a
base-rate count. No claim that Koide's relation is physically true, that
θ₀=2/9 "should" hold, or that 7983360 "is" an E₆ number. Q=2/3 is a tautology
of the parametrization (proved below, not assumed). θ₀=2/9 is a numerology
target being tested for distance only.

---

## Q3 — the Koide θ₀ σ-distance (full error propagation)

### Inputs
PDG/CODATA charged-lepton masses (as given in the cell-D spec):
- m_e  = 0.51099895000 MeV, σ = 1.5×10⁻¹⁰ MeV (frac. 2.94×10⁻¹⁰)
- m_μ  = 105.6583755 MeV, σ = 2.3×10⁻⁶ MeV (frac. 2.18×10⁻⁸)
- m_τ  = 1776.86 MeV, σ = 0.12 MeV (frac. 6.75×10⁻⁵)

### The Q=2/3 tautology (why it's a tautology, shown not asserted)
For ANY three positive reals fit to √m_i = M(1+√2 cos(θ₀+2πi/3)), i=1,2,3, the
three phases are 120° apart, so Σcos(φ_i)=0 and Σcos²(φ_i)=3/2 identically, for
*any* θ₀. That forces Σ√m_i = 3M and Σm_i = 6M² as identities of the ansatz
form itself (not of the physical masses) — hence
Q ≡ Σm_i/(Σ√m_i)² = 6M²/9M² = 2/3 exactly, independent of θ₀, whenever three
numbers exactly fit the ansatz. Real lepton masses only *approximately* fit
the ansatz (2 free params, M and θ₀, vs. 3 data points), so measured Q is
close to but not exactly 2/3 — the closeness of measured Q to 2/3 is the
actual empirical content; that Q=2/3 is forced *given* an exact fit is pure
algebra, not physics.

Measured: **Q = 0.66666051...**, Q − 2/3 = −6.155×10⁻⁶ (Q differs from 2/3 by
about 9×10⁻⁶ relative — matches the well-known "Koide holds to ~5 decimal
places" empirical statement; this is a sanity check on the pipeline, not a new
claim).

### Method
θ₀ is over-determined (2 free params M,θ₀ vs 3 masses); M = (Σ√m_i)/3 is
forced by the ansatz's Σcos=0 identity, then θ₀ is extracted from the
remaining two degrees of freedom via the symmetric (DFT/least-squares)
projection onto the 120°-spaced basis:
x_i ≡ √m_i/M − 1,  cos θ₀ ∝ (2x_e − x_μ − x_τ),  sin θ₀ ∝ (x_τ − x_μ)
(closed-form least-squares fit of all 3 masses simultaneously; symmetric,
does not privilege any one lepton). Index convention used: **i=1,2,3 for
(e,μ,τ) exactly as specified** in the cell-D formula.

Error propagation: (1) analytic Jacobian ∂θ₀/∂m_i via central finite
differences, combined in quadrature; (2) Monte Carlo, N=10⁶ independent draws,
m_e,m_μ,m_τ ~ independent Gaussians at the PDG central/σ above. Both methods
cross-validated (agree to <0.03%); central θ₀ additionally cross-checked at
50-digit precision (mpmath) against the float64 pipeline (agrees to float64
precision).

**Convention note (honesty on an ambiguity):** the parametrization has a
dihedral (order-6) relabeling symmetry — permuting which lepton is assigned
i=1,2,3 shifts/reflects θ₀ by multiples of 2π/3. Using i=0,1,2 instead of the
specified i=1,2,3 gives the *equivalent* raw value θ₀=2.31662473...rad, which
is exactly θ₀(i=1,2,3) + 2π/3 (2.31662473 − 2.09439510 = 0.22222963,
matching below to 8 digits) — same equivalence class, different fundamental
domain, not a cherry-picked fit. We report the value in the convention
literally specified in the prereg (i=1,2,3), which lands near 2/9.

### Results
- **Central θ₀ = 0.222229631 rad** (50-digit check: 0.22222963148971585864...)
- **σ(θ₀) = 8.348×10⁻⁶ rad** (analytic Jacobian) / **8.346×10⁻⁶ rad** (Monte
  Carlo, N=10⁶) — agree to 0.03%.
- **Error budget** (fraction of Var[θ₀]):
  - m_τ: **99.999988%** (∂θ₀/∂m_τ = −6.957×10⁻⁵ rad/MeV, dominant because
    m_τ's fractional uncertainty, 6.75×10⁻⁵, is ~2500× m_μ's and ~2×10⁵× m_e's)
  - m_μ: 0.0000116%
  - m_e: ~6×10⁻¹² % (utterly negligible, despite the largest raw Jacobian
    magnitude, because σ_e is 9 orders of magnitude below σ_τ)
  - **τ mass uncertainty completely dominates σ(θ₀), as anticipated.**
- **|θ₀ − 2/9| = 7.409×10⁻⁶ rad** (θ₀ is slightly above 2/9)
- **σ-distance = |θ₀ − 2/9| / σ(θ₀) ≈ 0.888σ** (0.8876 analytic, 0.8878 MC —
  consistent).

### Verdict on Q3
**θ₀ = 2/9 is CONSISTENT, not excluded** — well inside 1σ (≈0.89σ), nowhere
near the 3σ line. This **corrects chat1's crude ~7σ estimate**: the actual
σ-distance is smaller by a factor of ~8 (chat1's estimate appears to have used
a σ(θ₀) roughly 8× too small — plausibly an incomplete propagation of the τ
mass error, which we find carries essentially all of the variance). No
physics claim follows from this — it is only a statement about how many
combined-PDG-σ separate the measured phase from the numerology target 2/9;
whether that near-coincidence is meaningful is outside this cell's scope.

---

## Q5 — the 7983360 base-rate

### Setup
7983360 = |W(E₆)| × 154, |W(E₆)| = 51840 = 2⁷·3⁴·5, 154 = 2·7·11.
7983360 = 2⁸·3⁴·5·7·11 (verified by direct factorization).
Range: [10⁶, 10⁷], size 9,000,001 integers.

**Note on the "product of E₆ exponents" framing:** E₆ exponents are
{1,4,5,7,8,11}. Checked directly: 154 is **NOT** expressible as an exact
product of these six integers with repetition (their only source of the
prime 2 is via 4=2² or 8=2³, and no non-negative combination of exponents
{2,3} sums to 1, so a bare factor 2¹ — which 154 has — is unreachable). 154
*is* expressible if you relax to "any power of the primes that appear inside
the exponent set" (prime content of {1,4,5,7,8,11} is {2,5,7,11}) — that
weaker, prime-level criterion is what's actually being tested below. Of the
three prime factors of 154, only 7 and 11 are themselves E₆ exponents; the
factor 2 is simply the most common prime there is (present in half of all
integers) and adds no distinguishing power.

### Counting
Multiples of |W(E₆)|=51840 in [10⁶,10⁷]: N=51840·k, k∈[k_min,k_max] with
k_min=⌈10⁶/51840⌉=20, k_max=⌊10⁷/51840⌋=192 (exact integer division: 51840×19
=984960<10⁶; 51840×192=9953280≤10⁷<51840×193=10005120).
**→ 173 multiples of 51840 in range** (173/9,000,001 = 1.922×10⁻⁵ of the range).

Of those 173 cofactors k∈[20,192], how many are smooth under various prime
sets:
| smoothness criterion | primes allowed | # of the 173 k's qualifying | conditional rate |
|---|---|---|---|
| strict literal product of {1,4,5,7,8,11} | (combinatorial, not prime-set) | 23 | 13.3% |
| "E₆-prime" smooth | {2,5,7,11} | 29 | 16.8% |
| 11-smooth (standard) | {2,3,5,7,11} | 64 | 37.0% |
| 20-smooth | {2,3,5,7,11,13,17,19} | 96 | 55.5% |

154 (the actual cofactor) is 20-smooth, 11-smooth, and "E₆-prime" smooth, but
**not** in the strict literal-product set (23 count excludes it — see note
above).

As a fraction of the *whole* range [10⁶,10⁷] (9,000,001 integers), the counts
of N=51840·k qualifying are: 96/9,000,001 = 1.07×10⁻⁵ (20-smooth cofactor),
64/9,000,001 = 7.11×10⁻⁶ (11-smooth), 29/9,000,001 = 3.22×10⁻⁶ ("E₆-prime"
smooth), 23/9,000,001 = 2.56×10⁻⁶ (strict literal product).

### Baseline: density of smooth numbers in [10⁶,10⁷], unconditional
Direct enumeration (heap/Dijkstra generation of B-smooth numbers up to 10⁷,
counted within [10⁶,10⁷]):
| smoothness class | primes | count in [10⁶,10⁷] | density |
|---|---|---|---|
| "E₆-prime" smooth | {2,5,7,11} | 449 | 4.99×10⁻⁵ (1 in 20,044) |
| 11-smooth | {2,3,5,7,11} | 2,089 | 2.32×10⁻⁴ (1 in 4,308) |
| 20-smooth | {2,3,5,7,11,13,17,19} | 11,448 | 1.27×10⁻³ (1 in 786) |

Cross-check: of the 11,448 twenty-smooth numbers in [10⁶,10⁷], 96 are
divisible by 51840 — i.e. a 20-smooth number in this range is ~435× more
likely to be a multiple of 51840 than a uniformly random integer is
(8.39×10⁻³ vs. baseline 1/51840=1.93×10⁻⁵). This enrichment is a **generic
arithmetic fact about smooth numbers clustering with other smooth divisors**
(51840 itself is smooth, 2⁷3⁴5), not evidence of anything E₆-specific.

### Verdict on Q5
**COINCIDENCE, not structural.** The decisive number is the *conditional*
rate: given that N is already fixed to be a multiple of |W(E₆)|=51840 (a
choice made to match the target, 173 candidates in range), the fraction of
those candidates whose cofactor is smooth under any of the tested criteria is
**13%–55%** — a common, unremarkable event, not a rare one. Requiring the
cofactor's primes to lie in {2,5,7,11} specifically (the most E₆-flavored
reading) still hits 16.8% of candidates — better than 1 in 6, far from
statistically distinguished (nowhere near, e.g., p<0.01). The apparent
"E₆-numerology" of 154=2·7·11 further softens under scrutiny: only 7 and 11
(2 of the 6 exponents) actually appear as prime factors beyond what 51840
already forces, and the "2" is the least distinguishing prime available.
**Firewall: the "7983360 is an E₆ number" reading is base-rate-dead** — it is
the kind of match a random ~17–55% event produces routinely, not a
structural signature.

---

## Firewall summary (Gate 5)
- Q=2/3 restated as parametrization tautology (proved above from the 120°
  phase symmetry alone) — not treated as physical content.
- Q3's 0.89σ is reported strictly as a distance between a measured phase and
  a numerology target; no claim that Koide's relation is exact, fundamental,
  or physically meaningful is made or implied.
- Q5's verdict is COINCIDENCE by the base-rate discipline requested: the
  conditional smoothness rate among already-fixed-modulus candidates (13–55%)
  is the operative number, not the superficially small joint/unconditional
  fraction of the full range (which is an artifact of first fixing the
  modulus to match the target — the classic post-hoc-rarity trap).
- Both results are advisory for cc's seat (cell D was addressed to cc2 by
  chat1's request); no repo/git state was touched in producing them.
