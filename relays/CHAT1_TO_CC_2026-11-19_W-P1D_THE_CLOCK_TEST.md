# W-P1d: the clock test. Frame C's own read-out converges under both clocks. Length sets it at 0.61 to 0.65 of the move count's, nearly alike for every sector ratio. The geometric read-out converges under the move count only. Under length, if the frame's ratios keep falling above height 6, it falls as a power of the cutoff, about X^(−1.5) for σ₂/σ₁ and X^(−3.7) for σ₃/σ₁: the cutoff takes the place of W-F25's open scale. Every plant and expectation held

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. It is W-P1's step 4, at the author's
word of 2026-11-19, after card W-P1's three steps had closed
(`relays/CHAT1_TO_CC_2026-11-18_W-P1_THE_PROCESS_READING.md`).

**The ruling it runs under.** The author's ruling of 2026-11-15 lets this seat compute and print frame C's outputs. It
may not open the data or compare any output with data. No frame value is computed here: the run reads W-F24's committed
fibre table. Nothing is set beside a measured number.

**Order of work.**
- the condition: `relays/cards/CHAT1_W-P1_STEPS_conditions.md`, step 4 (e61768f5c);
- the script: `relays/chat1_2026-11-19_wp1d/wp1d_clock.py` (789f6ef84), with `SCRIPT_SHA256.txt`;
- its output: `wp1d_clock_out.txt`, `wp1d_clock_err.txt` (empty) and `wp1d_summary.json` (ecb14a3b9). A partial output
  was committed unread mid-run (6b14d91a1). Both were committed before the output was read.
- Before its commit, the script was smoke-tested once at small sizes with the frame replaced by random numbers. No frame
  value entered that test.

**Not blind.** These were known: W-F24's read-outs under (a), W-P1c's height shares under both clocks, and W-F25's cusp
exponents. D0 and D3 follow from them, so they check the computation. No read-out under (b) had been computed.

**Typing.** [E] marks what the run or the record establishes; [J] marks this seat's judgement.

---

## 0. In short

1. **[E] Every plant and control holds.**
   - W-F24's read-outs are reproduced with its own sampler and seed to 8.9e-15 (PL4).
   - The clock's mean of (height − 1)⁺ matches its closed form to 1.1e-5 at every setting (PL2).
   - The cusp law's path is exact on a linear test field to 7.9e-7 (PL5).
   - Constants come back to 1.4e-14 (PL1), and the table's points to 1.1e-16 (PL3).
2. **[E] Frame C's form, A_read, converges under both clocks.** How the frame is treated above height 6 changes it by at
   most 0.5%.
   - Under length, at X = 800, it is 0.609 to 0.654 of the move count's, for every sector ratio.
   - Within each sector and reading, A_read(σ₃/σ₁)/A_read(σ₂/σ₁) moves by +1.6% to +6.2% between the clocks.
3. **[E] The geometric form, G_read, converges under the move count.** There the two treatments above 6 differ by less
   than 1e-3 in log.
   - Under length, clamped at height 6, it converges slowly (at most 3.1% from X = 400 to 800). It settles at 0.020 to
     0.13 of the move count's.
   - Under the cusp law it falls at each doubling of X: by 2.5 to 2.8 for σ₂/σ₁, and by 11 to 13 for σ₃/σ₁. The law
     predicts the fall from 100 to 800 to within 4.3% (D3).
4. **[E, standard] Why.** Under length the mean height grows without bound, like (3/π) log X. The run gives 0.62 to 0.65
   per doubling, against 0.66. So the geometric mean of a ratio whose log falls linearly with height tends to 0 (§ 5).
5. **[J] What it means.** The clock decides which read-outs exist, not only where the weight lies.
   - Frame C's form exists under both clocks.
   - The geometric form exists under the move count only.
   - Under length, the geometric form becomes W-F25's exponent reading averaged over the fibre, with the cutoff for its
     scale. The net count of card W-P1 stays zero (§ 6).

---

## 1. The run

The condition fixes every definition. In brief:
- **The frame.** W-F24's table gives A(τ) (frame C's fibre average) and G(τ) (the geometric one) for 12 sector ratios at
  154 points, heights 0.876 to 6. Values at a node are interpolated linearly, by W-F24's rule.
- **Above height 6,** where the table and the end's tables (B1927) stop, three treatments:
  - **T1** clamps at height 6 (W-F24's rule).
  - **T2**, the cusp law, continues log A and log G linearly. Its slope is fitted per column over heights 4, 5 and 6.
  - **T2b** fits the slope over heights 2 to 4. It is reported only.
- **The clocks.** Threads are sampled as in W-P1c, at 30 points per unit length (at least 8 per piece), each word
  weighted by its length.
  - **(a)**, the move count: 2,000 random words of 20, 40 and 80 letters.
  - **(b)**, length: every primitive class with trace at most X, for X = 100, 200, 400 and 800. There are 1,214, 4,186,
    14,690 and 52,091 classes (31 million nodes at 800).
- **The read-outs.** A_read = E[A], and G_read = exp E[log G].

## 2. Plants and controls

| line | result |
|---|---|
| PL1, constants (A = 0.3, G = 0.2) | returned to at most 1.4e-14, all clocks and treatments |
| PL2, E[(height − 1)⁺] against its closed form | within 1.1e-5 relative at every setting (bound 1e-3) |
| PL3, the table's 154 points | within 1.1e-16 |
| PL4, W-F24 with its own sampler, seed and 1,000 words, under T1 | its 12 A_read and G_read within 8.9e-15 relative |
| PL5, log G replaced by −Im τ, under T2 | equals −E[height] within 7.9e-7 relative (bound 5e-3) |
| the run radii from the thread's own ends, against W-P1c-F's `closed` | equal (difference 0) on 1,414 words |

PL2 checks the clocks without the frame. Its term is the integral over y ≥ 1 of W-P1c's closed form 2 arccosh(ρ/y),
taken over each run. The radii of runs of R come from the same axis's ends (y, x) as (1/x − 1/y)/2, since the letter
swap acts as z ↦ 1/z. The control's agreement with W-P1c-F's `closed`, which computes them from the swapped word,
confirms this.

## 3. The read-outs

Nothing here is set beside a measured value. The leptons equal the down sector to every printed digit, as in W-F24.

**A_read, frame C's form.**

| sector ratio | (a) n = 40 | (b) X = 100, T1 | (b) X = 800, T1 | (b) X = 800, T2 | (b)/(a) |
|---|---|---|---|---|---|
| up, S, σ₂/σ₁ | 0.3588 | 0.2245 | 0.2205 | 0.2202 | 0.614 |
| up, S, σ₃/σ₁ | 0.03881 | 0.02482 | 0.02439 | 0.02439 | 0.628 |
| up, S̃, σ₂/σ₁ | 0.3730 | 0.2398 | 0.2357 | 0.2346 | 0.632 |
| up, S̃, σ₃/σ₁ | 0.05516 | 0.03667 | 0.03608 | 0.03608 | 0.654 |
| down, S, σ₂/σ₁ | 0.3533 | 0.2195 | 0.2155 | 0.2154 | 0.610 |
| down, S, σ₃/σ₁ | 0.03193 | 0.02102 | 0.02069 | 0.02069 | 0.648 |
| down, S̃, σ₂/σ₁ | 0.3495 | 0.2167 | 0.2127 | 0.2127 | 0.609 |
| down, S̃, σ₃/σ₁ | 0.02395 | 0.01507 | 0.01481 | 0.01481 | 0.618 |

The last column is T1's.

**G_read, the geometric form.**

| sector ratio | (a) n = 40 | (b) X = 800, T1 | (b) X = 100, T2 | (b) X = 200, T2 | (b) X = 400, T2 | (b) X = 800, T2 |
|---|---|---|---|---|---|---|
| up, S, σ₂/σ₁ | 0.2145 | 0.02598 | 4.57e-3 | 1.74e-3 | 6.50e-4 | 2.36e-4 |
| up, S, σ₃/σ₁ | 0.01620 | 3.61e-4 | 4.43e-6 | 4.03e-7 | 3.48e-8 | 2.77e-9 |
| down, S, σ₂/σ₁ | 0.2140 | 0.02634 | 4.62e-3 | 1.76e-3 | 6.58e-4 | 2.39e-4 |
| down, S, σ₃/σ₁ | 0.01598 | 4.29e-4 | 5.34e-6 | 4.93e-7 | 4.31e-8 | 3.48e-9 |

- Under (a), T1 and T2 differ by at most 9.7e-4 in log G_read (n = 20, 40 and 80), and by 2.6e-6 relative in A_read
  (n = 40).
- E[(height − 6)⁺] is 2.5e-4 at n = 40. Under (b) it is 1.18 at X = 100 and 3.04 at X = 800.
- The standard errors at n = 40 are 0.0009 or less on A_read and 0.0086 or less on log G_read. All twelve ratios are
  in the output.

**Where the geometric read-out comes from** (T2). This is the share of log G_read from above heights 2, 4 and 6.
- Under (a) at n = 40: 0.27 to 0.43, 0.026 to 0.037, and 0.002 to 0.003.
- Under (b) at X = 800: 0.90 to 0.93, 0.80 to 0.82, and 0.73 to 0.76.

## 4. The expectations, as written before the run

Each line was set in the condition before the run. Each was met.
- **D0, the clocks' heights.**
  - Under (a), E[height] was to move by less than 0.02 from n = 40 to 80. It went from 1.5424 to 1.5393.
  - Under (b), it was to rise by (3/π) log 8 = 1.99 from X = 100 to 800, within 25%. It rose by 1.906, which is 0.96
    of that.
- **D1, (a) settles.** From n = 40 to 80 every read-out stayed within 3 standard errors. T1 and T2 agree under (a): to
  2.6e-6 relative in A_read and 9.7e-4 in log G_read.
- **D1b, two samplers.** This run's sampler and W-F24's agree at n = 40 within 3 combined standard errors. The largest
  distances are 0.83 (A_read) and 1.09 (log G_read).
- **D2, (b) clamped converges.** Under T1, every change from X = 400 to 800 is smaller than from 100 to 200.
- **D3, (b) under the cusp law falls.** Under T2, log G_read falls at every step. From 100 to 800 it falls by 0.957
  to 0.963 of (3/π) s̄ log 8, for every ratio (bound 25%).
- **D4.** A_read under (b) changes by at most 0.28% from X = 400 to 800, under T1 and T2 (bound 2%).
- **D5.** A_read under (b) at X = 800 is below (a)'s, for every ratio, under T1 and T2.
- **D6, the exponent ratio.** Under T2, log G_read(σ₃/σ₁)/log G_read(σ₂/σ₁) lies closer to the slopes' ratio at
  X = 800 than at 100, in all six sector-readings. For example, up S goes 2.288, then 2.359, towards 2.505.
- **D7.** Every column slope over heights 4 to 6 is negative: none of 264 is above zero.

[J] D3's shortfall of 4% matches the cutoff. Trace ≤ X keeps heights below X/2, and the expected (height − 6)⁺
grows by (3/π)(log 8 − 0.105) rather than (3/π) log 8, which is 0.95 of it.

## 5. Why the clocks part [E, standard, and the run]

**Under length, the mean height grows without bound.**
- Closed geodesics ordered by length equidistribute in the hyperbolic area (Pollicott 1986; Roblin 2003). W-P1c and
  B1813 cite the same, and W-P1c's shares approach it.
- Equidistribution applies to bounded continuous functions. Take f_M = min(height, M), which is continuous and bounded
  on the modular surface. Its area average is at least (3/π) ∫₁^M dy/y = (3/π) log M, because above height 1 the domain
  has width 1 and the area is (3/π) dx dy/y².
- So E_X[height] ≥ E_X[f_M], which tends to at least (3/π) log M, for every M. Hence E_X[height] → ∞.
- The run gives 3.83, 4.45, 5.08 and 5.74 at X = 100, 200, 400 and 800: steps of 0.62, 0.63 and 0.65, against
  (3/π) log 2 = 0.66.

**Under the move count it does not grow.**
- A word of n letters stays below height n/2 + 1 (W-P1c).
- E[height] is 1.545, 1.542 and 1.539 at n = 20, 40 and 80.
- B1813's tail, 4^(−Y), has a finite mean.

**So a geometric read-out of a ratio that falls exponentially in the cusp tends to 0 under length.** Suppose
log G ≤ C − c·height with c > 0. Then E_X[log G] ≤ C − c·E_X[height], which tends to −∞. Under T2, c is at least 1.49
for σ₂/σ₁. Clamping (T1) stops the fall at height 6 by fiat, so under T1 G_read converges.

**[E] The arithmetic read-out hardly depends on what lies above 6.** A is bounded: it is a mean of ratios of singular
values, each at most 1. So equidistribution gives A_read a limit under length, the area average of A. Above height 6
A is small, and T2 and T2b move A_read from T1 by at most 0.48% at any X.

## 6. What it means [J]

**The cusp law against the record's exponents** (post hoc).
- W-F25 writes each ratio at one point as C·ε^E, with ε = e^(−π Im τ). So a slope s in log means E = −s/π.
  - A's fitted slopes give 0.20, 1.00, 0.39 and 1.09 (up σ₂/σ₁, up σ₃/σ₁, down σ₂/σ₁, down σ₃/σ₁, in S).
  - Those are near the smallest exponents over the fibre in W-F25: 1/5, 1, 2/5 and 11/10. An arithmetic mean follows
    its slowest-falling point.
  - G's fitted slopes give 0.493 and 1.235 (up), and 0.493 and 1.229 (down). A geometric mean follows the fibre's mean
    exponent.
- **The mean exponents, by W-F25's table** over the 24 points:
  - 4 points have first coordinate 0, with exponents near 1 and 2. Those are W-F25's referee's extended-precision fits;
    they are not settled in double precision.
  - 10 points have first coordinate ±1/5: up (1/5, 6/5), down (2/5, 11/10).
  - 10 points have first coordinate ±2/5: up (3/5, 1), down (2/5, 11/10).
  - For σ₂/σ₁: up (4 + 2 + 6)/24 = 1/2, and down (4 + 4 + 4)/24 = 1/2.
  - For σ₃/σ₁: up (8 + 12 + 10)/24 = 5/4, and down (8 + 11 + 11)/24 = 5/4.
  - The run's slopes sit 1.4% below these for σ₂/σ₁, and 1.2% (up) and 1.7% (down) below for σ₃/σ₁. That is
    consistent with the points (0, j/5), whose slopes W-F25 found still rising.
- **So under length, G_read ≈ const · X^(−3Ē)**, with Ē the fibre's mean exponent. The area's 3/(πy) times the π in ε
  gives the 3.
  - With W-F25's exponents that is X^(−3/2) for σ₂/σ₁ and X^(−15/4) for σ₃/σ₁. In the S reading the run's laws are
    X^(−1.48) and X^(−3.69) to X^(−3.71).
  - The log ratio tends to 5/2 for up and down alike, in the S reading. The run gives 2.505 and 2.493 for the slopes'
    ratio.
  - The 24-point average does not see the sector difference that W-F25 found at the mark (5/3 against 11/4). Over
    the 20 points with first coordinate ±1/5 or ±2/5, up and down have the same exponent sums: 8 for σ₂/σ₁ and 22
    for σ₃/σ₁.
  - This reading rests on W-F25's exponents, two of them unsettled. The run's fitted slopes are its own evidence.

**For C01, the measure over histories.**
- W-P1c showed that the clocks differ in which words they count. This step shows they differ in which read-outs exist.
  - Frame C's own form has a limit under both. Length moves it by a factor of 0.61 to 0.65, nearly uniform across the
    sector ratios, so ratios of read-outs move by only 2% to 6%.
  - The geometric form has a limit under the move count only.
- C01 stays a counted choice: the record's principle names the move count (P-845, D3), and nothing here names it.

**For card W-P1, § 4.2.** No test the iteration imposes separates the clocks here.
- "The read-out composes, and it has a limit" would pass the move count alone.
- But composition is this seat's principle, not the iteration's (W-F24's theorem). And W-F24 refuted the geometric
  form as a fix for the hierarchy.
- The net count stays zero.

**For W-F25's proposal.**
- Under length, the geometric read-out is W-F25's exponent reading averaged over the fibre. The cutoff takes the place
  of its open scale: log G_read ≈ const − 3Ē log X.
- The scale stays open, because X is a choice. It also loses the sector difference, because the average runs over the
  whole fibre and not the act's line.
- This supports W-F25's reading at the act's line and not over the fibre. It does not select a scale.

**For the hierarchy.**
- Under the move count both read-outs sit in the bulk, where W-F24 found the hierarchy weak.
- Under length, frame C's form stays in the bulk. Its hierarchy is unchanged within 6%, at 0.61 to 0.65 of the level.
- Under length, the geometric form's hierarchy grows without bound with the cutoff.

## 7. Typed

- **[E] by the run:** §§ 2, 3 and 4; § 5's numbers; the slopes in § 6.
- **[E] by the record:**
  - W-F24's table and read-outs;
  - W-P1c's sampler, closed form and height bound;
  - W-F25's exponents, two of them not settled in double precision;
  - B1813's tail; P-845, D3.
- **[E] standard:** the equidistribution of closed geodesics ordered by length (Pollicott 1986; Roblin 2003), and the
  truncation argument of § 5.
- **[J]:**
  - T2 and T2b. They model the frame above height 6, where neither the table nor the end's tables reach; they do not
    compute it.
  - § 4's account of D3's shortfall.
  - § 6.

## Files

- `relays/chat1_2026-11-19_wp1d/`: `wp1d_clock.py`, `SCRIPT_SHA256.txt`, `wp1d_clock_out.txt`, `wp1d_clock_err.txt`
  and `wp1d_summary.json`.
- The condition: `relays/cards/CHAT1_W-P1_STEPS_conditions.md`, step 4.
- Cited:
  - this seat's W-F24, W-F25 and W-P1c, and card W-P1;
  - B1813, B1927 and P-845;
  - M. Pollicott (1986) and T. Roblin (2003).

This relay is pushed before its referee read finishes, following the author's word of 2026-11-15 on untracked notes.
Its read's corrections are not yet applied in this version.

0 of 19.
