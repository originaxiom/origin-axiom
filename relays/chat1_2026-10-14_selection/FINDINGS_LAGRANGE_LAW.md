# The Lagrange law: in the thread frame a vacuum's hierarchy is fixed, to 0.3 e-folds over 20, by one number, its thread's Lagrange value; the golden root (Hurwitz's √5) is the least hierarchical vacuum

chat1, 2026-10-14, evening. An out-of-sample test of the height law found on the thread frame's 12 threads.
- **Sealed** at `3887230a7` (sha256 91bfe0f8…). **The script** `lagrange_law.py` was committed before its one run
  (378 s). It copies `thread_frame.py`'s construction verbatim. Output: `lagrange_law_run.txt` and `lagrange_law.json`
  (`8c2000ae7`).
- **0 of 19. No arc number claimed. Nothing to CLAIMS.md, GENESIS or the ledgers.**

## Scored

| | prediction | prior | outcome |
|---|---|---|---|
| Q0 (control) | the 12 old threads reproduce to 10⁻⁶ | 97% | **FAILS as worded, at 1.14·10⁻⁶** (LRRRR's m₁/m₃, the ill-conditioned K of the earlier run). Every other old ratio agrees to better |
| LL1 | Spearman(y_max, ln m₂/m₃) < −0.9 over all admitted | 80% | **HOLDS: ρ = −0.996** over 59 admitted threads |
| LL2 | the sealed 12-thread fit predicts the new threads with RMS < 1.0 | 55% | **HOLDS: RMS 0.30** over the 47 new admitted threads, out of sample |
| LL3 | the golden root has the largest m₂/m₃ | 85% | **HOLDS:** LR, 0.369 |
| LL4 | the Markov threads (y < 1.5) have m₂/m₃ > 0.01, and every thread with y > 2 has m₂/m₃ < 10⁻³ | 60% | **HOLDS.** Six Markov threads give 0.027 to 0.369. All 31 threads above y = 2 are below 10⁻³ |
| LL5 | the sealed m₁/m₃ fit predicts the new threads with RMS < 1.5 | 45% | **HOLDS: RMS 0.61** |

**Admission.** 59 of 69 threads were admitted. The 10 excluded (y > 3, or N = 256 against N = 384 above 10⁻⁵) are
the words with a run of five or more letters: L⁵R, L⁶R, L⁷R and their kin.

## The law and its spectrum

- **The fit over all 59 admitted threads:**
  - ln(m₂/m₃) = 7.289 − 7.332·y_max (RMS 0.26);
  - ln(m₁/m₃) = 6.979 − 8.538·y_max.

  Here y_max is half the thread's Lagrange value.
- **The bottom of the spectrum is Markov's.**

  | Lagrange value | thread | CS | m₂/m₃ | m₁/m₃ |
  |---|---|---|---|---|
  | √5 = 2.236 (golden, the root) | LR | 0 | **0.369** | 9.6·10⁻³ |
  | √8 = 2.828 (silver) | LLRR | 0 | 0.0357 | 5.9·10⁻³ |
  | √221/5 = 2.973 (Markov 5) | LLRRLR, LLRLRR | 0 | 0.0267 | 3.0·10⁻³ |
  | √1517/13 = 2.996 (Markov 13) | LLRRLRLR, LLRLRLRR | 0 | 0.0310 | 2.7·10⁻³ |
  | 3.130 | LLRLLRR, LLRRLRR | ±0.42 | 0.0143 | 2.0·10⁻³ |
  | 3.240 | LLRLRLR, LRLRLRR | ±0.43 | 0.0176 | 9.1·10⁻⁴ |
  | 3.266 | LLRLR, LRLRR | ±0.43 | 0.0118 | 7.7·10⁻⁴ |
  | 3.359 | LLRLLRLR, LRLRRLRR | ±0.84 | 0.0066 | 5.0·10⁻⁴ |
  | √12 = 3.464 | LLR, LRR | ±0.41 | 0.0034 | 3.3·10⁻⁴ |

- **The scatter has a second variable.**
  - Distinct threads at equal height differ by up to a factor 2.5: LLLLRRRR and LLLRLLR, both at y = √5, give 4.9·10⁻⁵
    and 1.2·10⁻⁴.
  - The residuals correlate with the syllable count (Spearman +0.62), |CS| (+0.47) and Vol (+0.43).
- **The heaviest state is F₊ in every admitted thread** (weight ≥ 0.9996), as in the 12-thread run.

## What it shows

1. **A law with one variable.** **[MATH, given H-thread; 59 threads, 47 out of sample]**
   - In the thread frame a vacuum's hierarchy depth is fixed by its thread's Lagrange value, to 0.3 e-folds over 20.
   - The Lagrange value measures how far the thread's closed geodesic climbs toward the modular cusp. Equivalently it
     is governed by the largest partial quotient: the longest run of one letter.
2. **Hurwitz is B990's law in Diophantine form.** **[READING]**
   - The golden root, with the worst-approximable axis (√5, the minimum of the Lagrange spectrum), is the least
     hierarchical vacuum.
   - The symmetric points give no hierarchy because hierarchy is a Diophantine excursion toward the end, and the
     symmetric thread makes the smallest one.
3. **The Markov spectrum makes the mild hierarchies discrete.**
   - Below Lagrange value 3 only the Markov threads exist, so a single-thread vacuum has m₂/m₃ ∈ {0.369, 0.036, 0.027,
     0.031, …}, accumulating near 0.02–0.03.
   - **The band between about 0.04 and 0.37 is forbidden.** The charged leptons' 0.059 lies in it.
4. **The observed quark hierarchies sit just past Markov's threshold.**
   - Through the fit, the up sector's 0.0037 maps to a Lagrange value of 3.52, near LLR's √12 = 3.46 (which gives
     0.0034). The down sector's 0.0187 maps to 3.07.
   - **Post hoc, and stated with its base rate.** The chiral thread LLRLRLR gives (0.0176, 9.1·10⁻⁴), and the down
     quarks are (0.0187, 9.4·10⁻⁴): within 6% and 4%.
     - Counting the threads in that region and the three sectors as targets, a match this close arises by chance at
       p ≈ 0.02 to 0.05. The tolerance was chosen after seeing.
     - Not significant by the record's bar. The up sector's m₁/m₃ misses by 45×, and the leptons sit in the forbidden
       band.
5. **What it says about which thread.** **[READING]**
   - At large c the weave becomes its root, which has no hierarchy to speak of (0.37).
   - The observed band holds 21–32% of the weave's weight at L154's c = 6 (thread-frame read-out).
   - So, given H-thread, the observed hierarchy prefers the plural weave of small c over the classical reading.

## Fence

- **H-thread** (a hypothesis); W72's forms at one weight (matter 3/2, Higgs mode 5/2); B1644's coupling. Lyndon words to
  length 8 with y ≤ 3. Reach: *members*.
- **Not tested.**
  - Other weights or representations: the natural place for sector differences and a second slope.
  - Sectors; mixing; the thread selection; the derivation of H-thread.
- No value. **0 of 19.**
