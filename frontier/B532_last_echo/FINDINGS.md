# B532 — THE LAST ECHO: Interaction Grammar Campaign

## Cell I1 — Fixed-Point Dimension + Period-3 Spectral Test

### Part B: Period-3 spectral test — ABSENT

The F₂⁴ phase map decomposes as period 6 = 2 × 3: a period-2 induction-power clock
(q=1 on even, q=2 on odd) and a period-3 binary-ambiguity clock. B531 found the
period-2 spectral shadow: gap-3 slope alternates 0.124 (even) / 0.154 (odd), caused
by the negative contracting eigenvalue λ₂ ≈ −0.440.

**Does the period-3 have a spectral shadow?**

Four independent tests across depths 5–12:

1. **Fourier phases arg(V̂(α)):** converge monotonically with no period-3 modulation.
   Phase differences Δarg(d) − Δarg(d−3) are small (< 0.3) and inconsistent in sign.
   VERDICT: no period-3 signal.

2. **Quadratic correction c₂(d):** c₂(gap 3) = 0.265 (even) / 0.384 (odd) — a
   PERIOD-2 alternation, not period-3. The apparent "period-3" spread (0.23) is an
   artifact of d mod 3 bins mixing even/odd depths unequally.

3. **Gap-slope ratios:** s₁/s₃ = 1.54 (even) / 1.24 (odd), pure period-2 at all
   depths 6–11. The period-6 data {d%6: s₁/s₃} shows two clean plateaus
   (d%6 ∈ {0,2,4} → 1.54; d%6 ∈ {1,3,5} → 1.24) with no period-3 fine structure.

4. **Complex eigenvalue argument:** λ₃ has arg = −0.7879π, implying period 2.538.
   This is IRRATIONAL — there is no period-3 eigenvalue over ℝ. The algebraic
   period-3 comes from x² + x + 1 ≡ 0 (cube roots of unity over F₂), which does
   not lift to a period-3 over ℝ.

**VERDICT: Period-3 is ABSENT from the spectrum.** The six-phase clock's two factors
have fundamentally different natures:
- Period-2 (induction power): SPECTRAL, from λ₂ < 0 (real negative contracting eigenvalue)
- Period-3 (binary ambiguity): COMBINATORIAL, from F₂ algebra (x² + x + 1 mod 2),
  no spectral shadow

The two clocks are algebraically interleaved (LCM = 6) but physically decoupled.

**Lock:** `tests/test_b532.py::test_i1_period3_*`

### Part A: Fixed-point dimension — RESOLVED

Chat1 claimed: σ*-fixed points on X(F₄, SL₂C) are isolated (dim=0) at irreducible
representations, with a golden FP at tr(a)=1, tr(b)=1/φ, κ=1.

**Independent analysis** at 10 irreducible FPs (seeds 2, 7, 11, 19, 31, 37, 41, 53,
67, 83), computing the numerical Jacobian rank of the 40-equation / 34-parameter
fixed-point system:

**Two components found:**

1. **Trace-zero component (κ = −2):** seeds 2, 37, 41. All four traces = 0.
   Jacobian rank 30, kernel dim 4. After subtracting 2-real-dim diagonal gauge
   (the residual SL(2,C) gauge after fixing T diagonal), geometric dim = 2 real
   = 1 complex. These form a **1-complex-dimensional family**.

2. **Generic component:** seeds 7, 11, 19, 31, 53, 67, 83. Diverse traces (some
   real, some complex). Jacobian rank 32, kernel dim 2. After subtracting the
   same 2-real-dim gauge, geometric dim = 0. These are **isolated (dim=0)**.

**Corrected verdict:** Irreducible FPs split into TWO components:
- A 1-dimensional family at the trace-zero locus (κ = −2)
- Isolated points scattered across the character variety

Chat1's dim=0 claim is **PARTIALLY CONFIRMED**: correct for the generic component,
incorrect for the trace-zero component.

**Golden FP:** NOT FOUND after 3100 seeds across 3 strategies (trace-seeded Newton,
random full SL(2,C), conjugation-varied). The golden traces tr(a)=1, tr(b)=1/φ, κ=1
were never hit. Status: **UNVERIFIED** — the golden FP either does not exist for this σ
or requires a parameterization we haven't tried.

**Lock:** `tests/test_b532.py::test_i1_fp_*`

## Cell I2 — The Projection Algebra

Every binary partition {X}|{Y} of {a,b,A,B} defines a "measurement" — a projection
from the 4-letter word to a 2-letter sequence. There are 7 non-trivial partitions
(up to complement): 4 single-letter partitions + {ab}|{AB} + {aA}|{bB} + {aB}|{bA}.

### Result: σ is irreducibly 4-letter

**NONE** of the 7 binary projections are substitutive. Every partition has at least one
class whose letters map to different projected images under σ. This means: the projection
does NOT commute with σ — you cannot first project then substitute, nor first substitute
then project. σ is an **irreducibly 4-letter** substitution; no binary coarsening is
dynamically compatible.

### The true projected frequency ratios (from Perron eigenvector)

| Partition | True freq ratio | Identified as | Pisot | Primitive |
|-----------|----------------|---------------|-------|-----------|
| {aA}\|{bB} | **1.618034** | **φ** (exact) | NO (|λ₂|=1.47) | YES |
| {ab}\|{AB} | **0.786151** | **1/√φ** (exact) | YES | YES |
| {aB}\|{bA} | 0.945027 | √φ/(1−√φ+φ) | NO (|λ₂|=1.0) | YES |
| {A}\|{abB} | 0.529086 | — | YES | YES |
| {a}\|{bAB} | 0.373663 | — | YES | YES |
| {B}\|{abA} | 0.272020 | = freq(a) | YES | YES |
| {b}\|{aAB} | 0.202093 | — | YES | YES |

**Two projections read golden values:**
1. **{aA}|{bB}** (the "structural" partition pairing each letter with its case-partner):
   frequency ratio = **φ** exactly. This is the golden ratio from the original Perron
   eigenvector: freq(a) + freq(A) = (φ + φ√φ)/S, freq(b) + freq(B) = (1 + √φ)/S,
   ratio = φ(1+√φ)/(1+√φ) = φ. NOT Pisot (contracting eigenvalue = 1.472 > 1).

2. **{ab}|{AB}** (lowercase vs uppercase, "old letters vs new letters"):
   frequency ratio = **1/√φ** exactly. This is freq(a)+freq(b) = (φ+1)/S = φ²/S,
   freq(A)+freq(B) = √φ(φ+1)/S = √φ·φ²/S, ratio = 1/√φ. IS Pisot (|λ₂| = 0.873).

3. **{aB}|{bA}** (the "cross" partition): ratio = √φ/(1−√φ+φ) ≈ 0.945. NOT a simple
   golden expression. NOT Pisot (|λ₂| = 1.0 exactly — the induced matrix [3,4;4,3]
   has eigenvalues 7 and −1).

### Grammar compatibility

All 7 projections realize their full set of allowed 2-letter transitions (each projected
word uses all transitions predicted by the grammar). No partition loses transitions under
projection. But this is a weak condition — the grammar alone doesn't distinguish the
projections.

### The one-measurement test

If we fix φ as the value of the {aA}|{bB} projection, the question is: how many
4-letter substitutions with the same 7/16 grammar and the same Pisot property produce
this frequency ratio? The answer is OPEN — computing this requires enumerating
substitutions, which is a hard combinatorial problem. But the irreducibility result
(no projection commutes with σ) means φ is NOT derivable from a 2-letter system
that "sits inside" σ. The four letters are entangled: measuring φ requires all four.

**Lock:** `tests/test_b532.py::test_i2_*`
