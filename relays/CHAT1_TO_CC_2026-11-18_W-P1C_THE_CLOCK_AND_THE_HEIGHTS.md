# W-P1c: the clock and the heights. Under the move count the weave spends 0.74, 0.17, 0.008 and 0.0004 of its time above modular heights 1.118, 2, 4 and 6; under length, 0.85, 0.47, 0.23 and 0.15, approaching the area's 3/(πy) from below. Both agree with B1813's tails. Above height 2 the move count's time lies under runs of 4 to 9 letters (0.83); length's, under runs of 10 or more (0.64)

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. It is step 3 of card W-P1
(`relays/CHAT1_TO_CC_2026-11-18_W-P1_THE_PROCESS_READING.md`, § 5), at the author's word of 2026-11-18.

**Order of work.** Each condition was committed before its script, and each script before its one run.
- The run:
  - the condition: `relays/cards/CHAT1_W-P1_STEPS_conditions.md`, step 3 (522248fe8);
  - the script: `relays/chat1_2026-11-18_wp1/wp1c_heights.py` (98bf1b6d1);
  - its output: `wp1c_heights_out.txt` (637ed8d19).
  - Before the script's commit, its functions were smoke-tested on control inputs only: LR, L³R, and the count of
    primitive classes at trace 30. No share was computed.
- After the referee read, three follow-ups, each with its own condition in the same file:
  - **W-P1c-F**, the read's missing numbers (`wp1c_followup.py`): condition a4e03a9a2, script 808be41b5, output
    874ce547b. The script was smoke-tested before its commit on LR, L³R and two run splits only.
  - **W-P1c-D**, a diagnosis (`wp1c_diag.py`): condition 874ce547b, script 3915039c3, output 5db939dd7.
  - **W-P1c-E**, the bound (`wp1c_bound.py`): condition 5db939dd7, script d088e0869, output 8e3083f3a.

**Typing.** [E] marks what the runs or the record establish; [J] marks this seat's judgement. Nothing here is compared
with a measured value, and no frame is read.

---

## 0. In short

1. **[E] The controls hold.**
   - LR spends no time above √5/2.
   - LⁿR reaches √((n + 2)² − 4)/2.
   - Every word's pieces sum to its translation length.
   - No thread rises above a/2 + 1, where a is its longest run of one letter.
   - A closed form for the time above each height y ≥ 1 agrees with the sampling: within 5e-5 pooled, and within the
     sampling's own error bound for each of 130,450 word-heights (§ 2).
2. **[E] The two clocks' shares of time above modular heights 1.118, 2, 4 and 6.**
   - (a), the move count: 0.737, 0.170, 0.0079 and 0.0004 at 40 letters. The standard errors are 0.0012, 0.0016,
     0.0004 and 0.0001. The shares at 20 and 80 letters agree with these within 0.003, about one standard error of the difference.
   - (b), length: 0.853, 0.474, 0.235 and 0.155 at trace 400 (14,690 primitive classes). They rise with the trace
     towards the area's 0.854, 0.477, 0.239 and 0.159.
3. **[E] They agree with the record at both clocks.**
   - Under (a), B1813's law 3.9·4^(−Y)/√Y gives 0.172, 0.0076 and 0.0004 at heights 2, 4 and 6, and W-F24's X4 gives
     0.168 above 2 and 0.007 above 4.
   - Under (b), above height 3 at trace 400 the share is 0.3147, which is B1813's 0.315 (the area's 0.318).
4. **[E] Under which runs the time above height 2 lies, excursion by excursion.**
   - Under (a), runs of 4 or 5 letters carry 0.54 and runs of 6 to 9 carry 0.29, so 0.83 together.
   - Under (b), runs of 10 or more carry 0.64.
5. **[J] What it means.** The clocks differ in which threads they let count, not only in how much time they spend
   high.
   - Under length, the long-run words that reach the cusp are many and short (LⁿR has trace n + 2), so they dominate.
   - Under the move count, a long run is exponentially rare in its length.

---

## 1. The run

**Definitions** (as the condition fixed them).
- A word is a positive word in L = [[1, 1], [0, 1]] and R = [[1, 0], [1, 1]] containing both letters. Its thread is the
  closed geodesic of its matrix.
- Height is Im τ after reduction to SL(2, ℤ)'s standard fundamental domain: a modular height.
- Time is hyperbolic arc length along one period.
- **(a)** W-F24's measure: uniform random words of n letters, 2,000 for each of n = 20, 40 and 80 (seeds 1, 2 and 3).
  Each thread is weighted by its length, and the time shares are pooled.
- **(b)** Every primitive cyclic word (a Lyndon word, L < R) with both letters and trace at most X, for X = 100, 200
  and 400. Each class appears once. The pooled share is Σ time above / Σ length, so each class is weighted by its
  length. This has the same limit as an unweighted mean of shares.

**Method.**
- One period is cut into one piece per letter.
- For the word A₀ ⋯ Aₙ₋₁ and its rotations Mₖ, each axis crosses the imaginary axis at a point qₖ. On Mₖ's axis the
  points qₖ, Aₖqₖ₊₁, …, Mₖqₖ follow in order and span one period.
- Each piece is sampled uniformly in arc length, with at least 120 points per unit length, and each sample is reduced.
- Endpoints are computed to 60 digits.

## 2. The controls (H0, F0, E1, E2)

| control | result |
|---|---|
| LR's top, against √5/2 = 1.118034 | 1.118024 (the sample nearest the top); time above 1.118: 0 |
| L²R, L³R, L⁵R, L⁸R's tops, against √((n + 2)² − 4)/2 | 1.732036, 2.291269, 3.354102, 4.898937, each within 5e-5 of 1.732051, 2.291288, 3.354102, 4.898979 |
| pieces summed, against the translation length 2 arccosh(tr/2) | equal to the printed digits for every word of (a) and (b) |
| the highest sample, against a/2 + 1 | never above, for every word of (a) and (b) |
| (b)'s shares as X grows | 0.467, 0.472, 0.474 above 2 at X = 100, 200, 400, rising towards 0.477 |
| the closed form against the sampling, pooled (F0) | within 5.0e-5 at every height and setting |
| the closed form against the sampling, word by word (E1) | within the bound 2N/DENS in all 130,450 word-heights; the largest ratio to the bound is 0.50 |
| the ten worst words at each height, as the sampling grows denser (E2) | the largest differences fall from 1.5e-2 to 6.3e-2, to 0.7e-3 to 4.3e-3, to 0.8e-4 to 3.5e-4, at 120, 1,200 and 12,000 points per unit length |

**The closed form.** For y ≥ 1, a point above height y is already at its reduced height, and the part of a thread above y is the
tops of its runs' axes. A run of a letters that starts at rotation k contributes 2 arccosh(ρ/y) when ρ > y. Here ρ is
the radius of Mₖ's axis; for a run of R it is the radius of the letter-swapped word's axis, and the swap does not change
heights.

**A correction disclosed.**
- F0's first condition also asked each word to agree within 5e-3. That failed: the worst word was off by 6.3e-2. By the
  rule written before the run, the attribution by runs (§ 4's second table) was withdrawn.
- The diagnosis's suspect, grazing runs at 1.118, was not the cause; the worst word had none.
- The bound E1, derived from the sampling's scheme before its run, explains it. Each part of a piece is weighted at
  most 1/DENS, and only parts that contain a crossing of the level are off, each by at most its weight. So a word
  with N excursions can be off by up to 2N/DENS. The 5e-3 was set without this.
- No word breaks the bound, and the differences fall tenfold with each tenfold density (E2). So the closed form is
  exact, the sampling's per-word error is its step, and the table stands.

## 3. The shares of time above each height

| clock | 1.118 | 2 | 3 | 4 | 6 |
|---|---|---|---|---|---|
| (a) n = 20 | 0.73768 | 0.17179 | 0.03604 | 0.00781 | 0.00043 |
| (a) n = 40 | 0.73754 | 0.16982 | 0.03556 | 0.00792 | 0.00039 |
| (a) n = 80 | 0.73600 | 0.16889 | 0.03496 | 0.00771 | 0.00034 |
| (a), standard error at n = 40 | 0.0012 | 0.0016 | 0.0009 | 0.0004 | 0.00008 |
| (b) X = 100, 1,214 classes | 0.85005 | 0.46691 | 0.30550 | 0.22459 | 0.14347 |
| (b) X = 200, 4,186 classes | 0.85251 | 0.47174 | 0.31163 | 0.23138 | 0.15094 |
| (b) X = 400, 14,690 classes | 0.85334 | 0.47427 | 0.31467 | 0.23470 | 0.15485 |
| the area, 3/(πy) | 0.85412 | 0.47746 | 0.31831 | 0.23873 | 0.15915 |
| B1813's move-count law, 3.9·4^(−Y)/√Y | (0.78, asymptotic) | 0.172 | 0.035 | 0.0076 | 0.00039 |
| B1813's headline | — | — | 0.0346 (move by move); 0.315 (length, trace ≤ 400) | — | — |

- [E] **(a) settles within its errors.** From n = 20 to n = 80 the shares move by at most 0.003. That is about one
  standard error of the difference at each height. The standard errors are from 1,000 resamples of the 2,000 words
  (F2): at n = 20 they are 0.0020, 0.0024, 0.0013, 0.0006 and 0.0001, and at n = 80 they are 0.0010, 0.0011, 0.0006,
  0.0003 and 0.00005.
- [E] **(b) rises with X towards the area at every height.** The limit is the equidistribution of closed geodesics
  ordered by length. On the modular surface this is the finite-volume form of the result (standard).
  - [J] The approach from below comes from the cutoff. Trace ≤ X allows runs of at most X − 2, so heights stay below
    about X/2 + 1. The area above X/2 is 3/(π·X/2) = 6/(πX): 0.019, 0.0095 and 0.0048 at X = 100, 200 and 400.
  - The shortfall at height 6 is 0.0157, 0.0082 and 0.0043, of that size and falling as 1/X.
- [E] **(a) agrees with B1813's law** at heights 2 to 6, and with W-F24's X4 (0.168 and 0.007). The law is asymptotic
  and is not meant at 1.118. At height 3, (a)'s 0.0356 ± 0.0009 sits beside B1813's computed 0.0346.
- [E] **(b) agrees with B1813's length tail:** 0.3147 above 3 at trace 400, B1813's 0.315 at the same cut.

## 4. Under which runs the time lies (H3, F3)

**By each word's longest run** (H3). Each word's time above a height is binned by the word's longest cyclic run of one
letter, a. Each entry is that bin's share of all the time above the height.

| clock, height | a = 1 | 2 | 3 | 4–5 | 6–9 | 10+ |
|---|---|---|---|---|---|---|
| (a) n = 40, above 1.118 | 0 | 0 | 0.029 | 0.477 | 0.460 | 0.034 |
| (a) n = 40, above 2 | 0 | 0 | 0.007 | 0.399 | 0.546 | 0.048 |
| (a) n = 40, above 4 | 0 | 0 | 0 | 0 | 0.707 | 0.293 |
| (a) n = 40, above 6 | 0 | 0 | 0 | 0 | 0 | 1.000 |
| (b) X = 400, above 1.118 | 0 | 0.005 | 0.029 | 0.117 | 0.227 | 0.622 |
| (b) X = 400, above 2 | 0 | 0 | 0.004 | 0.063 | 0.189 | 0.744 |
| (b) X = 400, above 4 | 0 | 0 | 0 | 0 | 0.057 | 0.943 |
| (b) X = 400, above 6 | 0 | 0 | 0 | 0 | 0 | 1.000 |

**By the run under each excursion** (F3, from the closed form). Each excursion above a height lies over one run. This
table bins the time by that run's length a.

| clock, height | a = 1 | 2 | 3 | 4–5 | 6–9 | 10+ |
|---|---|---|---|---|---|---|
| (a) n = 40, above 1.118 | 0.064 | 0.332 | 0.254 | 0.244 | 0.099 | 0.008 |
| (a) n = 40, above 2 | 0 | 0 | 0.145 | 0.544 | 0.287 | 0.025 |
| (a) n = 40, above 4 | 0 | 0 | 0 | 0 | 0.714 | 0.286 |
| (a) n = 40, above 6 | 0 | 0 | 0 | 0 | 0 | 1.000 |
| (b) X = 400, above 1.118 | 0.029 | 0.116 | 0.107 | 0.148 | 0.165 | 0.436 |
| (b) X = 400, above 2 | 0 | 0 | 0.026 | 0.135 | 0.201 | 0.639 |
| (b) X = 400, above 4 | 0 | 0 | 0 | 0 | 0.075 | 0.925 |
| (b) X = 400, above 6 | 0 | 0 | 0 | 0 | 0 | 1.000 |

- [E] Each row respects the bound: a run rises above y only if it has more than 2y − 2 letters. Above 4 every run has
  7 or more letters, and above 6 it has 11 or more.
- [E] The two tables differ most at low heights. Above 1.118, under (a), runs of 1 and 2 letters carry 0.40 of the
  time, although H3's bins a = 1 and 2 are empty. A word's time high comes from all its runs, not only its
  longest.

## 5. What it means

- [J] **The two clocks differ in which threads they count.**
  - Under length, each primitive class counts once. The long-run words that reach the cusp are many and have small
    trace: LⁿR has trace n + 2. So above height 2, 0.64 of length's time lies over runs of 10 or more.
  - Under the move count, a run of n equal letters is rare: its probability at each place is about 2^(−n). So above 2
    the time lies over the commoner runs of 4 to 9 (0.83), which rise only to between 2 and 5.5.
- [J] **For card W-P1, § 3.1.** The weight over threads (C01) is not only a weight on heights. It is a choice of which
  words matter at each height.
  - Under the record's principle, (a), the cusp above height 4 is reached only over runs of 7 or more letters and
    holds under 1% of the time.
  - At n = 40, 0.57 of (a)'s time lies between heights 1.118 and 2, and 0.26 below 1.118.
  - Frame C's hierarchy is a height effect (W-F24). It is stronger above 2, where (a) spends 0.17 of its time.
  - This is the record's W-F24 reading, now attributed to runs. How far the read-out leans to low heights depends on
    the frame's ratios along the threads, which this step does not compute.
- [J] **What is new here** is only § 4. § 3 reproduces B1813 and W-F24, and confirms the area at modular heights by a
  direct enumeration.

## 6. Typed

- **[E] by the runs:** §§ 2, 3 and 4.
- **[E] by the record:** B1813's law and its headline numbers; W-F24's X4.
- **[E] standard:**
  - the equidistribution of closed geodesics ordered by length, in its finite-volume form;
  - the bound a/2 < height < a/2 + 1 (card W-P1, § 2.1);
  - the arc length above y of a semicircle of radius ρ, 2 arccosh(ρ/y).
- **[J]:** § 0 item 5; § 3's account of the shortfall; § 5.
- **The expectations, set in the condition before the run.**
  - (a) close to W-F24's X4 and below 1e-3 above 6. Met. X4 was known before the condition and uses the same measure,
    so this is a reproduction.
  - (b) near the area. Met.
  - Above 2, (a)'s time carried by runs of three or more. Met. The bound a > 2y − 2 forces it.

## Files

- `relays/chat1_2026-11-18_wp1/`: `wp1c_heights.py`, `wp1c_followup.py`, `wp1c_diag.py` and `wp1c_bound.py`, each
  with `_out.txt` and `_err.txt`; `SCRIPT_SHA256.txt`.
- The conditions: `relays/cards/CHAT1_W-P1_STEPS_conditions.md` (step 3 and its three follow-ups).
- Cited: B1813, W-F24, P-845, card W-P1.

## Provenance

The first version (614bff48d) was read by a referee who had not written it. The verdict was sound with corrections,
and seven items were raised:
1. (b) was not compared with B1813.
2. (a) carried no errors, and "the same at 20, 40 and 80" was said without them.
3. "As equidistribution requires" claimed more than the theorem gives. The approach from below is the cutoff's.
4. A sentence of § 5 attributed time to the run under each excursion, which the run had not computed.
5. "Most of the read-out comes from heights 1.118 to 2, where the hierarchy is weakest" went past the run.
6. "Each is met" did not say that one expectation is forced and one reproduces X4.
7. (b)'s "each counted once" hid the length weighting of the pooled share.

Each item was checked at its source. Items 1, 2 and 4 needed numbers, which this seat computed on its own committed
scripts (W-P1c-F) rather than taking the read's. The read's own numbers agree with them: 0.3147 above 3, the standard
errors, and 0.145, 0.544, 0.287, 0.025 and 0.639 in F3. The read's corrections are applied in this version, with the
follow-up's failure and its settlement disclosed in § 2.

0 of 19.
