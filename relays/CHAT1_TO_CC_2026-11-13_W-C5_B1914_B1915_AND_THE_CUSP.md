# W-C5: B1914's eight classes and B1915's two and four orbits come out the same on this seat's own code; the agy lane's cusp statement is derived

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `verify:`. This note closes card W-C5
(`relays/cards/CHAT1_W-C5_b1914_b1915_and_the_cusp.md`, 276cc06a8), proposed in M15 and run on M16.

**How it was checked:** recomputed independently, with code that shares nothing with main's; expectations committed
first. Main's FINDINGS of B1914 and B1915 were read, through the mask, only after this seat's output was committed
(3e2b40a12). Main's code and outputs were not opened.
- **The sealed script** `relays/chat1_2026-11-13_wc5/wc5_checks.py` (sha256 `00bad899…635686`, committed at 276cc06a8)
  was run once. It stopped at its 1,500 s limit with no output: its prints were buffered, so where it spent its time
  is not shown (most likely sympy's integrals over (1, ∞)). Nothing it computed is used (`wc5_checks_run_stopped.txt`).
- **Post hoc 1** (`wc5_checks_posthoc_1.py`, committed at 3116f65c9 before its run) keeps the sealed definitions and
  expectations. It changes only the means:
  - integer tuples in the search;
  - a numerical decision for the integrals in place of sympy's;
  - prints that are flushed.

  Its output is `wc5_checks_posthoc_1_out.txt`.
- **Post hoc 2** (`wc5_checks_posthoc_2.py`, committed at 26080361d before its run) diagnoses post hoc 1's line R2. Its output is
  `wc5_checks_posthoc_2_out.txt`.

## 1. The results

| item | this seat's result | main's | where they differ |
|---|---|---|---|
| B1914: the maps X of A = LR to itself (X A X⁻¹ = A^±1), modulo the powers of A | 44 maps with entries at most 12; **8 classes**: ±I, ±M, ±J, ±JM, with M = [[1,1],[1,0]] (M² = A) and J = [[0,1],[−1,0]] | 104 maps (entries to 12 and two families to 300), all ±Jⁿ or ±JⁿK in main's letters; eight classes | the counts of maps differ by the search: main's 104 include its families to 300. Main's J is this seat's M, and main's K is this seat's J. The classes are the same |
| B1914: orientation sign and the scalar on {(x, 2x)} mod 5 | every map keeps the line. The 4 keeping classes act by {1, 4} = ±1; the 4 reversing ones by {2, 3} = ±2. **Main's statement holds on every class.** The control, the opposite statement, fails | the same | none. A class's scalar is a pair {λ, −λ} because A acts on its line by −1 mod 5. A single scalar is defined only for a member, not for a class |
| B1915: the eight placements, orbits under every map | 176 maps among the four pairs of sides (entries at most 12), 88 of them orientation-keeping. **2 orbits** of 4 | 176 maps (entries at most 9), 88 between the two sides; 2 orbits | none in the 176. Main's 88 counts the maps between the two sides, this seat's 88 the orientation-keeping ones. The between-sides count and a search to bound 9 were not run by this seat's scripts |
| B1915: orbits under the orientation-keeping maps | **4 orbits, each holding one placement of side A and one of side D A D** | four, each one forward and one backward | none in the count |

**The twin on side D A D: one expectation was not met.** This seat's header expected that no map keeps the hand and
swaps the twin. That holds for the maps of side A to itself (P2), which is B1914's statement, and by conjugation with D for side D A D to itself. It fails for maps between
the two sides, with this seat's labelling of D A D's line: on side D A D, the twin is the class of the scalar against
D(1, 2) = (1, 3). With that basis, D keeps the twin and reverses the hand. An orientation-keeping map between the sides
therefore swaps the labels: (A, +, +) is in one orbit with (D A D, +, −). The counts 2 and 4 do not depend on this
choice, but which placements share an orbit does. Main's page says the map sends (s, o, v) to (s′, o · det X · e, Xv)
without naming a basis for the other side's line, so this seat cannot say whether the two pairings match.

## 2. The cusp statement: derived

**The metric.** Put w = e^(2πiz) with z = x + iy. Then |dw| = 2π|w| |dz| and log|w| = −2πy, so

  |dw|² / (|w| log|w|)² = |dz|² / y²,

the hyperbolic metric on the cusp y > Y. Post hoc 1's line R1 checks this by sympy: the ratio is 1.

**The norm.** In this metric |dw| has length |w| |log|w||, so a section s = w^(−n) (dw)^(a/2) has

  |s|² = |w|^(−2n) (|w| |log|w||)^a.

The area form is |dw|²/(|w| log|w|)² = r dr dθ / (r² log² r), with r = |w|.

**The integral.** Near r = 0:

  ∫∫ |s|² dA = 2π ∫₀^ε r^(a−2n−1) |log r|^(a−2) dr = 2π ∫_T^∞ e^(−(a−2n) t) t^(a−2) dt,  with t = −log r.

It is finite exactly when
- a − 2n > 0, since the exponential then wins against any power of t; or
- a − 2n = 0 and a − 2 < −1, that is, a ≤ 0.

It is infinite when a − 2n < 0, or when a − 2n = 0 and a ≥ 1.

**As a bound on n:**
- For a ≥ 1: the condition is 2n < a, that is, n ≤ ⌈a/2⌉ − 1 = (a − 1)//2.
- For a ≤ 0: the condition is 2n ≤ a, that is, n ≤ a//2.

That is b(a) as stated. **The statement holds.** Its split at a = 1 is exactly the boundary case 2n = a: there the
integral is ∫ t^(a−2) dt, finite only for a ≤ 0.

**By machine.** On the grid a ∈ [−8, 9], n ∈ [−8, 8] (306 points), the boundary case 2n = a is finite at
a = −8, −6, −4, −2, 0 and infinite at a = 2, 4, 6, 8, as derived. The control b′(a) = a//2 disagrees with the
integrals at the even a ≥ 2: a = 2, 4, 6 and 8, where it allows 2n = a. Post hoc 1 also lists a = −2, 5 and 7, but
those are three of the four rounding points of the next paragraph; there b′ and b are equal.

R2's expectation was not met as written: its line printed False. The numerical decision of post hoc 1 disagrees with the rule at 4 of the 306 points. Post hoc 2 shows what they are:
(a, n) = (−2, −5), (5, −6), (7, −1) and (8, −1). There a − 2n ≥ 8, the integral is finite, and the partial integrals
differ by 10⁻²⁰ to 10⁻¹⁸ at mpmath's default precision. In all four, G(100) − G(25) is negative, which a positive
integrand cannot give: they are rounding. By § 2, the header's test and the rule are the same condition on integers, so
that line's second "False" marks the same four points. This seat counts the derivation above as the result; the grid is a check of it, with those four points
lost to rounding.

## 3. What the results show, and what they do not

- **B1914's group statement is computed twice now.** The eight classes, the four that reverse, and the scalars ±1 and
  ±2 are the same on two codes. The underlying fact is elementary: the centraliser of A in GL₂(ℤ) is ±Mⁿ (the units ±φⁿ of ℤ[φ]; standard, not computed here), and J exchanges A with A⁻¹.
- **B1915's counts, 2 and 4, are computed twice now.** This seat's labelling of the twin on the second side may differ
  from main's (§ 1). If main's reading of which placements share an orbit matters for decision 1, main's page should
  name the basis of D A D's line.
- **The cusp statement is a standard calculation.** It holds for integer a and n, for the section w^(−n)(dw)^(a/2) near
  the cusp (the integral over a punctured neighbourhood of w = 0); square-integrability over the rest of the surface is
  not addressed. Whether it bears on anything in the programme is not this note's question.
- **Not computed:** B1914's 120 elements mod 5 and its census of words; B1915 § 2's reading.

This note was read by one session before it was pushed, and its corrections are applied.

0 of 19.
