# The Lagrange law: in the thread frame a vacuum's hierarchy is fixed, to 0.3 e-folds over 20, by one number, its thread's Lagrange value; the golden root (Hurwitz's √5) is the least hierarchical vacuum

> **Corrected the same evening (see the last section). The sealed cells stand for words of length ≤ 8; the law's
> generalisations fail beyond.** On the same construction, long words with golden blocks dilute the hierarchy, so the
> hierarchy is not fixed by one number. The "forbidden band" is filled by long Markov words, and "Hurwitz is B990 in
> Diophantine form" is withdrawn.
>
> **2026-10-15: the mass formula corrected** to its basis-invariant form (last section). The 18 words that are not
> reflection-symmetric move by at most 3.2·10⁻⁵ relative. Every sealed cell keeps its outcome.

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

## Corrections (2026-10-14, late evening, after the independent referee)

The referee upheld every sealed cell and the seal order: hashes verified, the coefficients are the 12-thread fit, the
RMS is on new threads only, and admission was as sealed. It found that the generalisations fail beyond length 8.

1. **BLOCKER, taken: "fixed by one number" is withdrawn.** The referee re-ran the construction verbatim (reproducing
   `lagrange_law.json` to 1.3·10⁻⁸) on longer words.
   - **Markov threads LLRR(LR)^k:** m₂/m₃ = 0.037 (length 10), 0.043 (12), 0.060 (18), 0.083 (28). It keeps rising
     toward the root's 0.369. The law gives 0.0245.
   - **LLR(LR)^k:** from 0.0034 to 0.055 at length 27, where the law gives 0.0103.
   - **All 501 admitted Lyndon words of length 9–12:** the sealed fit's RMS is 0.44 (mean residual +0.38), growing with
     length. The residual–syllable Spearman is +0.68.
   - **The mechanism.** The heavy mode F₊'s norm accumulates along the geodesic's whole length, while the light modes'
     norms are dominated by the highest point. So the ratio depends on at least two numbers: the height and the length,
     or golden content.
   - **chat1's own labelled post hoc** (`post_hoc_long_words.*`: the sealed construction, unchanged, on five long
     words) reproduces the referee's numbers. All five agree between N = 256 and N = 384 to 2·10⁻⁷ or better.

     | word | length | y_max | m₂/m₃ | the law's m₂/m₃ | m₁/m₃ |
     |---|---|---|---|---|---|
     | LLRR(LR)³ (Markov 34) | 10 | 1.4997 | 0.0369 | 0.0246 | 2.7·10⁻³ |
     | LLRRLLRRLR (Markov 29) | 10 | 1.4996 | 0.0280 | 0.0246 | 3.7·10⁻³ |
     | LLRR(LR)⁷ (Markov 1597) | 18 | 1.5000 | 0.0595 | 0.0245 | 3.1·10⁻³ |
     | LLR(LR)⁴ | 11 | 1.6181 | 0.0265 | 0.0103 | 1.1·10⁻³ |
     | LLR(LR)¹² | 27 | 1.6180 | 0.0553 | 0.0103 | 1.7·10⁻³ |

     - Two Markov threads of length 10 at almost the same height (Markov 29 and 34) differ by a third in m₂/m₃. Height
       alone does not fix the ratio even among Markov threads.
     - Along LLRR(LR)^k (k = 0, 1, 2, 3, 7: Markov 2, 5, 13, 34, 1597) m₂/m₃ runs 0.036, 0.027, 0.031, 0.037, 0.059.
       It rises from k = 1 on, toward the root's 0.369.
2. **"The Markov spectrum makes the mild hierarchies discrete; the band 0.04–0.37 is forbidden; the leptons' 0.059 lies
   in it" is withdrawn.** Long Markov words fill the band: LLRR(LR)^k at length 18 gives 0.0595.
3. **"Hurwitz is B990's law in Diophantine form" is withdrawn.**
   - At the record's symmetric points "no hierarchy" means rank one or degenerate. At the golden thread it means a mild
     0.37. The cusp, a symmetric point too, carries the deepest hierarchies.
   - What stands: **the root has the largest m₂/m₃ of all threads computed.** Long golden-dominated words approach it
     from below.
4. **Numbers corrected.**
   - "0.3 e-folds over 20": the admitted m₂/m₃ span 13.2 e-folds.
   - The excluded words are those with y > 3 or failing the precision rule, not "all words with a run of five".
     LLLLLRR, LLLLLRRR, LLRRRRR and LLLRRRRR were admitted.
   - y_max is a sampled lower bound on half the Lagrange value, off by at most 7.8·10⁻⁵.
   - The table omits LLRLRRLR (√10, 0.0151).
   - The 47 new threads carry 26 distinct values; mirror pairs duplicate.
5. **The base rate was not computed by a script.**
   - The referee's null, jittering the targets by ±0.5 to ±2 e-folds, gives p ≈ 0.01–0.03 with threads to length 8 and
     0.04–0.10 to length 12. So the figure depends on the cutoff.
   - LLRLRLR carries the law's largest residual (+0.55).
   - "Not significant" stands.
6. **"The observed hierarchy prefers the plural weave of small c" is downgraded to a remark.** It rests on weights for
   lengths ≤ 5 (25% of weight (A) uncomputed) and on a band drawn after seeing the data.
7. **Credit.** The Markov heights and LR as the unique lowest thread are main's: B1629, B482 (T-TWOTEETH), B1379.

## Correction (2026-10-15: the mass formula, found by step 3a's pre-seal review)

The sealed form (K^{−½})ᵀ Y K^{−½} is not basis-invariant. Its masses agree with the invariant form's unless K and Y
are both complex. The invariant masses are the singular values of K^{−½} Y (K^{−½})ᵀ (`FINDINGS_THREAD_FRAME.md`, same
date).

The labelled post hoc `post_hoc_invariant_masses.*` recomputes both forms. Its script (`d5cf9f3a9`) was committed
before its one run (339 s), and its output is at `ea0647ffc`.

- **51 of the 69 words are reflection-symmetric:** the reversal or the mirror is a rotation of the word.
  - On these, K is real to 4·10⁻¹⁸ and the two forms agree to 1.05·10⁻¹⁵.
  - Y is not exactly real on them.
    - |Im Y|/|Y| is at most 1.7·10⁻⁶ on the 41 admitted.
    - On the ten not admitted (y > 3) it reaches 0.53, on LLLLLLLR. The quadrature has not converged there: N = 256 and
      N = 384 differ by 17.5% on that thread, and by up to 24% among the ten.
    - Whether the residue on the admitted threads is quadrature error is not shown.
  - Since K is real, the two forms agree regardless.
- **On the other 18, K and Y are both complex.**
  - |Im K|/|K| runs from 1.5·10⁻⁹ to 2.4·10⁻⁵, and |Im Y|/|Y| reaches 1.2%.
  - The two forms differ by at most 3.2·10⁻⁵ relative, on the reversal pair LLRLRR and LLRRLR.
- **Every sealed cell keeps its outcome and its quoted figure.** Admission is unchanged: 59 threads, 47 of them new.

  | cell | invariant form | as sealed |
  |---|---|---|
  | LL1 | ρ = −0.9957183 | the same (ranks are unchanged) |
  | LL2 | RMS 0.297744 | 0.297742 |
  | LL3 | LR, 0.3687747 | the same |
  | LL4 | no violation | no violation |
  | LL5 | RMS 0.610642 | 0.610640 |
- **The figures quoted above all stand.**
  - The Markov 5 and Markov 13 pairs in the spectrum table move by less than 3.2·10⁻⁵ relative.
  - In correction 1's table, the three long words that are not symmetric move by at most 2.2·10⁻⁵ (LLRR(LR)³). The two
    golden words, LLR(LR)⁴ and LLR(LR)¹², are symmetric.
- **The CP read-outs are unaffected.** A reversed or mirrored word carries the conjugate couplings. Both forms then give
  conjugate matrices, hence equal masses. In the two forms, the six chiral words of `post_hoc_reversal` differ by at
  most 3.2·10⁻⁵, by the same amount within each pair.
- **Step 3a's C1 reference is unchanged:** 0.0515 on LLRLRLR, which is reflection-symmetric, in both forms.
- **Disclosed: the recheck's own defects.**
  - The script's `P1` dictionary literal names the key "their worst old-vs-new difference" twice.
    - The JSON therefore keeps only the second value, the 18 words' 3.18·10⁻⁵.
    - That value sits right after "reflection-symmetric words: 53", where it reads as the symmetric words' figure. Their
      own figure is 1.05·10⁻¹⁵.
    - The per-row data are complete, and the figures above are read from the rows.
  - `P1`'s count of 53 reflection-symmetric words is the 51 to length 8 plus the two symmetric long words.
  - The docstring says "seven reversal words", but `P3` holds six reversal words (11 entries with the five long words).
    The seventh, LLR, has length 3 and sits in `P1`'s rows.
- **Refereed.** Step 3a's read-only referee checked every figure in this section against both JSON files. It confirmed
  them and sharpened three wordings: the duplicated key, the 17.5% on LLLLLLLR, and "not shown" for Y's residue.
