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

## Cell I3 — Self-Description

σ's image words (abAAB, aAB, abAB, aA) are words in the object's own language.
The substitution describes itself using its own alphabet.

### The return induction of image words

Each image word σ(g) is a factor of the fixed-point word ω. Computing the return
induction for each:

| Image word | |w| | Return count | q | Charpoly core |
|---|---|---|---|---|
| σ(a) = abAAB | 5 | 4 | 1 | x⁴ − 2x³ − 5x² − 4x − 1 |
| σ(b) = aAB | 3 | 4 | 1 | x⁴ − 2x³ − 5x² − 4x − 1 |
| σ(A) = abAB | 4 | 4 | 1 | x⁴ − 2x³ − 5x² − 4x − 1 |
| σ(B) = aA | 2 | 5 | 1 | x(x⁴ − 2x³ − 5x² − 4x − 1) |

All four image words have q = 1 (even). σ(B) = aA has 5 returns (length 2 = bispecial
boundary); the other three have 4 returns. Every induced charpoly contains the original
x⁴ − 2x³ − 5x² − 4x − 1 as a factor.

### Result: σ(a) is SELF-CONTAINING

The canonical induced codes of the factor "abAAB" (= σ(a)) are:

    ((0, 1, 2, 2, 3), (0, 2, 3), (0, 1, 2, 3), (0, 2))

This is **exactly σ itself** — the canonical codes of the original substitution. When
you study how the fixed point ω returns to its own first image word, the return words
form a substitution system isomorphic to σ.

This self-containment persists at depth 2: σ²(a) = abAABaABabABabABaA (length 18) also
has canonical induced codes = σ. But σ(b), σ(A), σ(B) do NOT self-contain — they
produce different canonical codes. Only the image of the seed letter 'a' is a perfect
self-description.

### Two linear orbits on F₂⁴

The Parikh mod 2 vectors of σ^d(g) follow the LINEAR map M mod 2 (no affine shift —
the shift is specific to the bispecial sequence). Under M mod 2 (order 6), the four
standard basis vectors split into TWO orbits of period 6:

- **Orbit 1 (lowercase)**: e_a → e_b (at d=4), both with period 6
- **Orbit 2 (uppercase)**: e_A → e_B (at d=4), both with period 6

The phase offset within each pair is 4 (= −2 mod 6): b is exactly 4 M-steps ahead of a,
and B is exactly 4 M-steps ahead of A. The two orbits are disjoint under M mod 2 — they
cover 12 of 16 F₂⁴ states (plus the trivial fixed point [0,0,0,0] and a separate 3-cycle).

The bispecial sequence (which follows the AFFINE map p → Mp + s) reaches all 16 states.
The image word trajectories are constrained to these two 6-cycles. The bispecial boundary
carries information (the shift s = [1,0,1,1]) that the substitution images do not.

### Return word nesting

Every return word of every image word contains other image words as substrings:
- σ(a)'s 4 return words each contain at least 2 image words; 2 of 4 contain all four
- σ(b)'s 4 return words all contain all four image words
- σ(A)'s return words include one that IS σ(A) itself (the length-4 return "abAB")
- σ(B)'s 5 return words each contain 2–3 image words

The descriptions nest: the object's words about itself contain further words about itself
at every level.

### Summary

The self-description has an asymmetry: σ(a) = abAAB is the unique self-reproducing factor.
The letter 'a' (the seed, the decider with weight φ/S = 0.272) generates a factor whose
return induction IS σ itself. The other three letters produce different induced systems
(same charpoly, different combinatorial structure). The self-description is anchored at a
single point — the seed letter's image — and everything else derives from it.

### Handoff verification: The Observer Gap (cross-seat, UNBANKED)

A cross-seat handoff claimed a "core hierarchy" where different bigrams "see" different
core polynomials (quartic, cubic, Fibonacci, periodic), and the gap label #1 = the
Fibonacci-core fraction ("the spectrum and the observer are one structure").

**Independent verification (CC):**

| Claim | Verdict |
|---|---|
| M_pair has same charpoly as M_orig | **CONFIRMED** ✓ |
| GL(4,Z) conjugacy between M_orig and M_pair | **CONFIRMED** ✓ (handoff's P was wrong; correct P=[[0,1,1,-1],[1,-1,1,-1],[0,1,0,1],[1,0,0,1]], det=-1) |
| Core hierarchy: 5 different polynomials for bigrams | **NOT REPRODUCED** — all 7 bigrams give the quartic under return-word induction |
| Gap label = Fibonacci-core fraction identity | **NOT REPRODUCED** — depends on the core hierarchy |
| Anomalous sector (abA) has charpoly x⁴-3x³-8x²-7x-2 | **WRONG** — charpoly = the standard quartic, disc = -400 |
| Return number = alphabet size (Law 1) | **PARTIALLY WRONG** — aA has 5 return words |
| Gap labels in ℤ-module of frequencies | **CONFIRMED** ✓ (already known) |

The core hierarchy is NOT produced by the standard S-adic return-word induction. It MAY
come from LETTER-DELETION restrictions (projecting to sub-alphabets), which give different
polynomials: {b,A,B} (delete a) → x³-x²-2x-1; {a,A} (delete b,B) → x²-2x-1 (silver
ratio, NOT Fibonacci). But this is a different operation with different mathematical
meaning, and the specific polynomials claimed by the handoff don't match either.

The GL(4,Z) conjugacy between the original and pair substitution IS a theorem (same
charpoly + explicit P with det = -1). The "deep identity" claim is UNVERIFIED — it
rests on a core hierarchy that is not reproduced by independent computation. Status: OPEN,
pending clarification of what "derived substitution" means in the handoff.

**Lock:** `tests/test_b532.py::test_i3_*`

## Cell I4 — The Derivation DAG

### The graph

29 layers organized in a DAG of depth 4. Single source node: σ itself.

**Depth 0 (source):** σ (the four words)
**Depth 1 (immediate):** M, grammar, swap s, symplectic D, return induction,
  + character variety [needs SL₂C], Schrödinger [needs V]
**Depth 2:** charpoly, frequencies, growth rate, M mod 2, Rauzy fractal,
  GL(4,Z) class, 7 types, self-containment, + trace map [needs SL₂C]
**Depth 3:** gap labels, decider/courier, entropy, disc/Galois, spectral type,
  six-phase clock, projection algebra, two linear orbits,
  + FP variety [needs SL₂C]
**Depth 4:** gap widths [needs V], golden section, period-3 absence

### The kernel

The irreducible kernel is **σ itself — the four words** (abAAB, aAB, abAB, aA).
Not the matrix (which doesn't determine the grammar or the Rauzy fractal). Not
the charpoly (which doesn't determine M). Not the grammar (which doesn't determine
the image lengths). The four words carry strictly more information than any single
invariant.

24 of 29 layers derive from σ alone by pure computation. The remaining 5 require
**observer inputs**:

### Observer inputs

1. **SL₂C structure** ("the observer's gauge"): needed for the character variety,
   trace map, and fixed-point variety. This is the observer's choice of how to
   REPRESENT the free group F₄ — it introduces a specific geometry (complex
   2-dimensional) into a purely combinatorial object.

2. **Potential V** ("the observer's measurement"): needed for the Schrödinger
   operator and gap widths. This is the observer's choice of how to COUPLE to
   the word — it turns a sequence of letters into a physical operator.

### The prediction form

Given σ + one observer input, specific layers are forced:
- σ alone → 24 layers (grammar, frequencies, golden section, spectral type, etc.)
- σ + SL₂C → +3 layers (character variety, trace map, fixed points)
- σ + V → +2 layers (Schrödinger operator, gap widths/slopes)

The campaign's thesis: the observer brings the gauge (SL₂C) and the coupling (V).
Given those choices, the 29-layer structure is determined. "Physics" is the
observer's choice of gauge and coupling projected onto the object's grammar.

**Lock:** `tests/test_b532.py::test_i4_*`

## Cell IZ — Synthesis

The interaction grammar is assembled in `GRAMMAR.md` (this directory). It documents:

1. The irreducible kernel (the four words, not M, not the charpoly, not the grammar)
2. The grammar's structure (7/16, deciders/couriers, golden section)
3. The projection algebra (σ irreducibly 4-letter, φ and 1/√φ)
4. The self-description (σ(a) self-containing, two linear orbits, nesting)
5. The spectral clock (period-3 absent, two FP components)
6. The prediction form (σ alone → 24 layers; +SL₂C → +3; +V → +2)
7. Cross-seat verification ledger

**Campaign verdict:** The B532 Last Echo campaign traced the object's interaction
grammar from 28 computed layers to a single irreducible kernel: the four words
(abAAB, aAB, abAB, aA). The object's self-description anchors at σ(a) = abAAB
(the unique self-containing factor). The observer brings gauge and coupling; the
object brings everything else.
