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
   - The time above each height y ≥ 1 has a closed form, one term per run (standard; § 2). The sampling agrees with it:
     within 5e-5 pooled, and within the sampling's error bound for each of 130,450 word-heights.
2. **[E] The two clocks' shares of time above modular heights 1.118, 2, 4 and 6.**
   - (a), the move count: 0.737, 0.170, 0.0079 and 0.0004 at 40 letters. The standard errors are 0.0012, 0.0016,
     0.0004 and 0.0001. From 20 to 80 letters the shares move by 0.2 to 1.1 standard errors of the difference.
   - (b), length: 0.853, 0.474, 0.235 and 0.155 at trace 400 (14,690 primitive classes). They rise with the trace
     towards the area's 0.854, 0.477, 0.239 and 0.159.
3. **[E] They agree with the record at both clocks.**
   - Under (a), B1813's computed limit is 0.1676, 0.00754 and 0.00039 at heights 2, 4 and 6. At 40 letters the shares
     lie 1.35, 0.95 and 0.0 standard errors from it, and they fall towards it from 20 to 80 letters at heights 2 and 3.
     This seat's W-F24, X4, gave 0.168 above 2 and 0.007 above 4.
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
  length.

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
| the closed form against the sampling, word by word (E1) | within 2N/DENS in all 130,450 word-heights; the largest ratio to it is 0.50, which is 1.00 of the sharp bound N/DENS |
| the ten worst words at each height, as the sampling grows denser (E2) | the largest differences, over the five heights: 1.5e-2 to 6.3e-2 at 120 points per unit length; 0.7e-3 to 4.3e-3 at 1,200; 0.8e-4 to 3.5e-4 at 12,000. Each falls by a factor of 6.4 to 24 per step; at height 6 the median falls only 1.9 times in the second step |

**The closed form [E, standard].** A run of a letters that starts at rotation k contributes 2 arccosh(ρ/y) to the time
above y ≥ 1 when ρ > y, and nothing otherwise. Here ρ is the radius of Mₖ's axis. For a run of R it is the radius of
the letter-swapped word's axis; the swap is an isometry of the modular surface that fixes the cusp, so it keeps heights.
The argument:
- For y ≥ 1 the horoballs {Im γτ > y} at the cusps are disjoint, and a point inside the one at ∞ is at its reduced
  height. So the time above y is the sum, over the lifts that enter the horoball at ∞ (up to translation), of the arc
  length inside it, 2 arccosh(ρ/y) for a lift of radius ρ.
- A lift of radius above 1 translates to one with endpoints y′ ∈ (−1, 0) and x′ > 1, a reduced lift.
- By Gauss's reduction cycle, which is Series's coding of the modular surface by continued fractions, the reduced
  lifts correspond one to one with the runs. For the run of length aᵢ, x′ = [aᵢ; aᵢ₊₁, …] and −y′ = [0; aᵢ₋₁, …].
- So ρ ∈ (aᵢ/2, aᵢ/2 + 1), which is the bound of card W-P1, § 2.1, and the thread's top is the largest ρ.

E1 and E2 are consistent with this. A referee checked it independently, summing the horoball lengths over the cusps
p/q: it agrees with this seat's closed form to 1.3e-11 per word on all 22,090 words of (a) n = 20 and (b).

**Two failures disclosed.**
- **F0.** F0's condition also asked each word to agree within 5e-3. That failed: the worst word was off by 6.3e-2. By
  the clause written before the run, "neither F3 nor the page's § 4 stands", so both of § 4's tables were withdrawn.
- **The diagnosis (W-P1c-D).** It failed by its own clause.
  - Of its expectations, two were met: the worst difference was at height 1.118, and the denser sampling shrank it
    (6.3e-2 to 4.3e-3).
  - Two failed: at heights 2 to 6 the worst differences were 6.2e-3 to 3.0e-2, against the expected 5e-3, and the
    worst word had no grazing run.
  - Its clause concluded that the closed form is wrong for some words and that F3 is withdrawn.
- **The bound (W-P1c-E) replaced that conclusion.** Its condition was written after the diagnosis's output had been
  read, and committed with it, before its own script and run.
  - Each part of a piece is weighted at most 1/DENS, and only parts that contain a crossing of the level are off.
  - So a word with N excursions can be off by at most 2N/DENS. Sampling at midpoints halves this: at most N/DENS.
  - The 5e-3 was set without this.
  - No word breaks the bound (E1). The largest ratio sits at the sharp limit, and the differences fall with the density
    (E2).
- **What the cause was:** the 5e-3 tolerance, not the closed form and not the sampling. The sampling's per-word error is
  at most N/DENS. The closed form rests on the standard argument above. Both of § 4's tables are reinstated.

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
| B1813's computed limit by moves (§ 2 there) | — | 0.1676 | 0.03462 | 0.00754 | 0.00039 |
| B1813's approximate law, 3.9·4^(−Y)/√Y | — | 0.172 | 0.035 | 0.0076 | 0.00039 |
| B1813's headline by length, trace ≤ 400 | — | — | 0.315 | — | — |

- [E] **(a) settles within its errors.** From n = 20 to n = 80 the shares move by at most 0.003: 0.76, 1.08, 0.78,
  0.16 and 0.74 standard errors of the difference at the five heights. The standard errors are from 1,000 resamples of
  the 2,000 words
  (F2): at n = 20 they are 0.0020, 0.0024, 0.0013, 0.0006 and 0.0001, and at n = 80 they are 0.0010, 0.0011, 0.0006,
  0.0003 and 0.00005.
- [E] **(b) rises with X towards the area at every height.** The limit is the equidistribution of closed geodesics
  ordered by length on the modular surface (standard: Pollicott 1986; Roblin 2003 in general; B1813 cites both).
  - [J] The approach from below comes mostly from the cutoff. Trace ≤ X allows runs of at most X − 2, so heights stay
    below X/2. The area above X/2 is c = 6/(πX). Renormalized, the shortfall above y is c(1 − 3/(πy))/(1 − c). At
    height 6 that is 0.0164, 0.0081 and 0.0040 at X = 100, 200 and 400, against the observed 0.0157, 0.0082 and
    0.0043.
  - It does not explain the low heights fully: above 2 at X = 400 the shortfall is 0.0032 against 0.0025, and above
    1.118 at X = 100 it is 0.0041 against 0.0028.
- [E] **(a) agrees with B1813's computed limit,** its § 2 row (0.1676, 0.03462, 0.00754, 0.00039). At n = 40 the
  shares lie +1.35, +1.07, +0.95 and 0.0 standard errors from it at heights 2, 3, 4 and 6, and at n = 80 +1.13, +0.57,
  +0.63 and −1.0. They fall towards it with n at heights 2 and 3.
  - B1813's law 3.9·4^(−Y)/√Y is approximate at heights 2 to 4, by its own account: its local slope there is 1.5 to
    1.6. Against the law, (a) is 1.6 standard errors low at height 2 (n = 40).
  - This seat's W-F24, X4, gave 0.168 and 0.007, the same measure.
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
  - Under the move count, a run of m equal letters is rare: its probability at each place is about 2^(−m). So above 2
    the time lies over the commoner runs of 4 to 9 (0.83), which rise only to between 2 and 5.5.
- [J] **For card W-P1, § 3.1.** The weight over threads (C01) is not only a weight on heights. It is a choice of which
  words matter at each height.
  - Under the record's principle, (a), the cusp above height 4 is reached only over runs of 7 or more letters and
    holds under 1% of the time.
  - At n = 40, 0.57 of (a)'s time lies between heights 1.118 and 2, and 0.26 below 1.118.
  - Frame C's hierarchy is a height effect (W-F24). It is stronger above 2, where (a) spends 0.17 of its time.
  - This is the record's W-F24 reading, now attributed to runs. How far the read-out leans to low heights depends on
    the frame's ratios along the threads, which this step does not compute.
- [J] **What is new here** is only § 4. § 3 reproduces B1813 and W-F24, and reproduces B1813's approach to the area
  at modular heights by a direct enumeration.

## 6. Typed

- **[E] by the runs:** §§ 2, 3 and 4.
- **[E] by the record:** B1813's computed limit, its law and its length tail; this seat's W-F24, X4.
- **[E] standard:**
  - the equidistribution of closed geodesics ordered by length (Pollicott 1986; Roblin 2003);
  - the closed form, by Gauss's reduction cycle and Series's coding (§ 2), with the bound a/2 < height < a/2 + 1 (card
    W-P1, § 2.1);
  - the arc length above y of a semicircle of radius ρ, 2 arccosh(ρ/y).
- **[J]:** § 0 item 5; § 3's account of the shortfall; § 5.
- **The expectations, each set in its condition before its run.**
  - The run: (a) close to W-F24's X4 and below 1e-3 above 6. Met. X4 was known before the condition and uses the same
    measure, so this is a reproduction.
  - The run: (b) near the area. Met.
  - The run: above 2, (a)'s time carried by runs of three or more. Met. The bound a > 2y − 2 forces it.
  - W-P1c-F: each met. They were not blind: the first read's numbers were known when its condition was written.
  - W-P1c-D: two met and two failed (§ 2), and its failure clause fired.
  - W-P1c-E: met.

## Files

- `relays/chat1_2026-11-18_wp1/`: `wp1c_heights.py`, `wp1c_followup.py`, `wp1c_diag.py` and `wp1c_bound.py`, each
  with `_out.txt` and `_err.txt`; `SCRIPT_SHA256.txt`.
- The conditions: `relays/cards/CHAT1_W-P1_STEPS_conditions.md` (step 3 and its three follow-ups).
- Cited: B1813, W-F24 (this seat's), card W-P1; Gauss's reduction of indefinite forms; C. Series, "The modular surface
  and continued fractions" (1985); M. Pollicott (1986); T. Roblin (2003).

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
errors, and 0.145, 0.544, 0.287, 0.025 and 0.639 in F3.

The corrected version (315778ddd) had a second read, by another referee who had not written it. The verdict was sound
with corrections. The numbers and the closed form held, and the referee reran the bound check byte for byte. Four
items were required:
1. The diagnosis's own failure was not disclosed.
2. The F0 failure withdrew both of § 4's tables, not one.
3. "The closed form is exact" was not established by the runs. The bound check is a necessary condition only, and
   2N/DENS is loose by a factor of 2. The standard argument was missing.
4. B1813's approximate law was used where its computed limit is the comparator.

It also raised eight smaller points of wording:
- the standard errors' spread;
- "derived before its run";
- "fall tenfold";
- the shortfall's renormalization;
- an unargued claim about the unweighted mean, now dropped;
- the missing citations;
- the follow-ups' expectations, which were not scored;
- four minor slips.

Each was checked at its source: B1813's § 2 row, through the mask, and the bound's sharpness by the midpoint argument.
The read's corrections are applied in this version.

0 of 19.
