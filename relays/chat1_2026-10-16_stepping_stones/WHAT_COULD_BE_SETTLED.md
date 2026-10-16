# Today's computations on three open puzzles: the cusp's readings, the rule that picks no thread on two kinds of quantity, and the thread frame at every depth computed (chat1)

chat1 (the web seat), 2026-10-16, at the owner's "please solve all these crucial puzzles that u can properly deal
with". These are the puzzles from the brainstorm's verdict (`chat1_2026-10-16_verdict/`) and step 1 of main's road
(S_THE_PUSH_BACK §10.1) that a computation could reach today.
- **§1 and §2 use no data.**
- **§3 compares with data that were already seen,** so it is a scoreboard: it can earn negatives, not positives.
- This note was refereed read-only before it left, and a referee recomputed §1's numbers independently.
- 0 of 19.

## 1. The cusp's readings for the surface frame's modes (computed; no data)

**The question.** This is gap (A) of the verdict. The verdict posed it for the traced frame; this answers it for the
surface frame.
- Each of W72's three generations of units grows at the modular cusp. Each has a principal part — q^(−7/8), q^(−1/8)
  or q^(−5/8) — with coefficient 1. So their Petersson norms diverge, and no mass ratio is defined (W72).
- W73 normalised by the units' leading coefficients ("H-end", chosen after W72 was read, in the untwisted frame).
- Is there a regularisation of the norms that needs no cutoff and is a norm?
- This is the modular cusp. It is not B1654's L, which cuts the fibre's puncture (u_r = √(2πL + c_r)·R_r) at the
  other end.

**The scale-free regularisation** (`canonical_cusp_norm.py`).
- Truncate the fundamental domain at y ≤ T and take the Gram matrix's constant term in T.
- For a growing term e^(ay) y^m this is the Hadamard finite part with the growing series median-resummed:
  Re[(−a)^(−m−1) Γ(m+1, −a)]. It is the regularised inner product of Bringmann, Diamantis and Ehlen (BDE, 2017).
- For these weights (m = −½, −5/2, 3/2) no log T term occurs, so it is scale-free.
- **The other regularisations** either give the same real part or are undefined for exponential growth:
  - Zagier's needs polynomial growth;
  - Borcherds' needs at most polynomial growth after averaging over x;
  - Bruinier and Funke's pairing is bilinear across two weights;
  - y^(−s) never converges.
- **Checks:**
  - the integrand is invariant with diag(1, 2, 2) on (e_i, v₊, v₋), the only invariant Hermitian form here (the
    referee's check);
  - two formulas for the finite part agree to 15 digits;
  - the quadrature and the series truncation are stable to 4 × 10⁻¹³;
  - J(T), minus its optimally truncated growing series, converges to the finite part (the referee's check);
  - a referee's own code reproduces every number, and confirms the invariance above under S, T and ST to about
    10⁻¹⁵.
- forms.pkl, the stored series, has sha256 64a40c03… (W72's units; the seals' file). The run prints the full hash.
- BDE remark themselves that their regularised product is "not positive in general".

**Result 1: the scale-free (BDE) regularisation is indefinite in every norm cell,** so it is not a norm and no mass
can be read from it.

| cell | its eigenvalues |
|---|---|
| K32 (weight 3/2: F_i, F₊, F₋) | −1.29, 0.41, 4.83 |
| KM12 (weight −½: the three −½ sections, R among them) | −45.7, 15.3, 114.4 |
| K72 (weight 7/2: E₄ times the −½ sections, and fser) | −0.39, 1.7 × 10⁻⁸, 0.047, 24 294 |

**Result 2: in this family of regularisations, positivity costs a height.**
- After the x-integral, the principal parts are orthogonal to every other term. So every regularisation of this kind
  differs only in the three growing modes' diagonal entries, by a height c:
  K(c) = K_reg − diag(w·FP∫_c^∞ e^(ay) y^m dy).
- K(c) is positive definite only above c* = 0.115 (K32), 0.959 (KM12) and 0.555 (K72).
- At c = 1, the edge of SL(2, ℤ)'s standard maximal cusp neighbourhood, all three are positive, by construction.
  - The smallest eigenvalues are 9.76, 0.63 and 0.026.
  - KM12's margin is thin (c* = 0.959).
  - Other heights, such as √3/2, are also distinguished.

**What it shows.**
- The scale-free (BDE) regularisation of the surface frame's mode norms is not a norm.
- A positive regularised norm of this kind needs a height c > c*, and its values depend on c.
- c = 1 is a geometrically distinguished choice, but it is a choice.
- The only other positive, scale-free normalisation on record is H-end (W73, untwisted, post hoc). It is not a
  regularised integral, and it gives every sector the same ratios, 1 : 0.019 : 0.0004 (χ² = 379).

**An instrument note for the SM seat** (`series_tail_check.py`).
- **What the referee found, re-measured here.** Near the top of the stored range, forms.pkl's coefficients leave
  their expected growth.
  - The departure starts between q^(131/8) and q^(195/8), depending on the series.
  - At q^(239/8), the highest stored exponent, they sit up to e⁶² above trend for the growing forms and up to e⁷⁴ for
    the cusp forms.
  - Their imaginary parts grow with the exponent: from 10⁻³⁷ of the real parts or less at the lowest exponents, to
    about 10⁻² to 10 at the top.
  - The onset criterion (e^0.5 above the trend) is rough: for E4F it partly picks up the trend's missing polynomial
    factor.
- **Why the closure tests cannot see it.** Every instrument here evaluates the series only at y ≥ √3/2: `tlow2.py`
  reduces each point to the fundamental domain first, and the norm integrals start there. A period's start and end
  therefore reduce to the same point.
- **The direct test.** Every series was cut at q^(140/8), and two mid-height classes were recomputed (h = 5.93 and
  4.56, s₁/s₃ down to 2.4 × 10⁻²⁸). Their masses came out bit-identical in double precision.
  - At y = √3/2 the terms the cut removed total up to 7 × 10⁻²³ of each series' largest term. The kept terms'
    imaginary parts total at most 1.3 × 10⁻³⁶.
  - So no result in this note depends on the corrupted coefficients.
- **Provenance.** forms.pkl was built by chat1's `build_forms.py` (mp.dps = 40), from the SM seat's solver at
  87cf7f55. The growth of the noise with the exponent looks like a precision effect.
  - A rebuild at higher precision, before any use at lower height or higher precision, is chat1's.
  - A solver repair, if one is needed, is the SM seat's.

## 2. Step 1 of main's road: the rule that picks no thread, on two kinds of quantity (computed; no data)

Main's step 1 "can fail by no trend toward the equidistributed value (Duke), or the cusp taking over at every
layer". It now has an outcome for each kind of quantity.

- **The units' norms: the cusp takes over** (`chat1_2026-10-16_no_thread_rule/W_TRACE_UNTWISTED.md`).
  - The norms grow at the cusp, so each layer's deepest pair carries its norm integrals, to ≤ 1.5 × 10⁻¹⁴ by
    trace 12.
  - The layer's masses are the pair's, moved by up to 0.38 in C1's ln(m₂/m₃).
  - By §1, the scale-free (BDE) finite part of the surface frame's norms is not a norm. Whether the trace-layer sums
    have a scale-free regularisation is not shown.
- **The matter's defect: it trends toward the equidistributed value** (`w_trace_defect.py`).
  - **The quantity** is main's f = |D|/‖R‖², the defect that sets B1654's first-generation lift. It is bounded, and it
    vanishes on ω's orbit and toward the cusp.
  - **D has a closed form, W87's.** B1654's D = Σ_r c_r R_r², with c_r = −2π ln((π/2)|θ_r(0)|²) (W87; B1657's S0
    checked W87's D against B1654's to 1.3 × 10⁻¹⁴). Jacobi (Σ R_r² = 0) removes the constant, leaving
    D = −4π Σ_r ln|θ_r(0)|·R_r².
  - **Checks:**
    - the closed form reproduces B1654's quadrature values to 6 × 10⁻⁵, the quadrature's own precision;
    - f is invariant to 4 × 10⁻¹⁵;
    - its area average over the modular surface is 0.31500491, main's value to every printed digit.
  - **The layer means.** Over every primitive thread of trace t (3 to 100), ⟨f⟩_t scatters around the area average
    and settles toward it. Averaged over ten consecutive traces:

    | traces | threads | mean − area average |
    |---|---|---|
    | 3–12 | 29 | +0.063 |
    | 13–22 | 59 | +0.027 |
    | 23–32 | 75 | +0.006 |
    | 33–100 | 102–192 per window | within ±0.017 |

  - Single layers still scatter, by −0.09 to +0.06 at traces 80 to 100, where they hold 6 to 36 threads.
  - For a bounded continuous f this trend is expected from Duke's theorem, since every discriminant in layer t grows
    with t. So on f, step 1 could not fail, and the run checks the instrument and the rate.
- **Main's B1666, the same day** (PROVED; main calls it a scoreboard because B1664 and B1665 showed its read-outs
  first), takes these layers to trace 600 (30 674 threads).
  - The top quarter's mean is 0.3144, and the gap closes as t^(−0.51 ± 0.05) (a read-out).
  - On D alone, the coherent rule favours the cusp family L^(4m+1)R, not the root.
  - This note's run to trace 100 is an independent check of the same trend, on a different instrument. Its
    per-trace means agree with B1666's to 4 × 10⁻⁵ on all 98 traces (the referee's comparison).
- **So the rule that picks no thread holds together where the quantity is bounded, and there it returns the typical
  motion's average, 0.315.** That average is parameter-free and of order one. It adds no size: the smallness still
  comes from B1654's L.
- **Which measure the motion takes is itself open.** Along the walk's limit rays the same defect averages 0.517, at
  every pull-back strength (main's B1663): the forward motion's word measure, not the typical motion's (main's
  reading, post-seal).

## 3. The per-field thread frame at every depth computed (scoreboards except T-low; the data were seen)

The question is gap (C) of the verdict: does the per-field thread frame fail at every depth?
- Each row scores the Standard Model's assignment against nulls: T-low's sealed 199 (111 distinct outcomes) on all
  90 configurations (26 classes); the other two rows the 112 distinct nulls, one configuration per class of word
  reversal with the mirror.
- Each uses every closing configuration of its range (lines of exact order N ∈ {9, 11, 12}), in the five cells.
- Each uses S-mass exactly as the low-thread seal defined it (W66's predicate as W88 used it: a = 0.10, six ratios,
  Σz² ≤ 12.592).

| range | heights | classes | S-mass passes | best χ² (SM / nulls) | median ln(pred/obs), SM: up m₁, m₂; down m₁, m₂; leptons m₁, m₂ |
|---|---|---|---|---|---|
| T-low, words to length 12 (**sealed**, 0d83e6981) | 1.54–2.77 | 90 configurations | 0 (SM and 199 nulls) | 983 / 267 | −3.0, −0.16; −7.5, −1.8; −5.8, −3.1 |
| words of length 13–14 (the replication's masses, post hoc) | 1.51–2.96 | 136 | 0 | 578 / 263 | −1.7, −0.10; −6.5, −1.7; −6.0, −2.7 |
| words to length 16 at 3 < h ≤ 6 (`midheight_scan.py`) | 3.01–5.93 | 185 | 0 | 28 281 / 14 483 | −14.0, −6.4; −18.5, −7.9; −17.6, −8.6 |

- **Sources:**
  - T-low's medians are `tlow_direction.py`'s, over its 450 configuration-cells.
  - The other two rows are `score_midheight.py`'s (`score_midheight_on_replication_run.txt`,
    `score_midheight_run.txt`). On the replication's output it reproduces `smass_on_replication_run.txt` exactly.
  - The mid heights: every class computed without error; r_calc ≤ 1.9 × 10⁻⁷.

**Which way the frame misses.**
- **The predicted hierarchies are too strong,** and more so with height.
  - On the shallow threads (h ≤ 3) the SM's median predicted log-ratio is 1.0–2.1 times the observed one. Only the up
    quarks' m₂/m₃ is within tolerance there (−0.16 and −0.10, against S-mass's σ ≈ 0.10).
  - At 3 < h ≤ 4 the multiple is 2.0–3.8, at 4–5 it is 3.3–7.2, and at 5–6 it is 4.2–8.0.
  - Above h = 3, at most 0.97% of the SM's cells are weaker than observed in any one ratio (up m₂/m₃), and 13 of 925
    (1.4%) in at least one.
- **The nulls' masses miss the same way,** so this is the frame, not the Standard Model's charges.
  - Pooled over every assignment, the medians are within 0.4 of the SM's, both on words of length 13–14 and over
    the mid heights.
  - At mid heights the SM ranks 96th of 113 by its best χ².

**The coherent rule's threads.** Ψ = #R − #L ≡ 0 mod 4, main §8.3b's rule for D alone, holds on:
- 78 of T-low's 90 configurations;
- 92 of the replication's 536 (25 of 136 classes);
- 71 of the 185 mid-height classes.

S-mass fails on all of them, for every assignment.
- **Main §10.3 reads road step 4 from T-low's sealed run.** An amplitude closes only on threads that fix their line,
  so any coherent selection is a subset of the closing configurations, and on T-low it keeps none that fit.
- **The two scoreboards above extend that negative, post hoc,** to words of length 13–14 at h ≤ 3 and to length 16
  at 3 < h ≤ 6.
- **The family the coherent rule favours on D** (B1666's L^(4m+1)R) is part of the tower family LⁿR. Its members close
  a line at N = 9 or 11, if at all, only at y ≥ 39.5, inside the 19:41 law's bound below (a reading).

**Beyond the computed range.**
- **The 19:41 law** (not sealed) bounds the failure on the least-volume closing threads at N = 9 and 11 (y ≥ 39.5):
  - by more than 40 orders of magnitude, if its offsets hold;
  - in C1 and the E4 cells (not ORTH), wherever Y is generic.
- **Not covered:**
  - words of length 15–16 at h ≤ 3 (1 592 configurations, by the referee's count), and words longer than 16;
  - 6 < h < 39.5 at N = 9 and 11, the ORTH cells above h = 6, and threads other than the towers above 39.5 (the
    offsets were measured on towers);
  - h > 6 at N = 12, where the law's ties and W92's zero can change its exponents.

**The law's leading order, as orientation only** (`deep_law_pattern.py`).
- **Its exponents are simple.** Per field:
  - Δ₋(d) = ½ for d ≤ ¼, and ¾ − d above;
  - Δᵢ(d) = ¾ + d for d ≤ ¼, and 1 above.

  They match the law's code on 1001 points. So per sector e₂ ∈ [½, 1] and e₁ ∈ [3/2, 2].
- **On its own, each observed ratio would need a depth of:**

  | sector | m₁/m₃ | m₂/m₃ |
  |---|---|---|
  | up | 0.94–1.25 | 0.89–1.78 |
  | down | 0.55–0.74 | 0.63–1.27 |
  | leptons | 0.65–0.87 | 0.45–0.90 |

  - Up's and down's m₁/m₃ ranges do not overlap (0.94–1.25 against 0.55–0.74).
  - The shallowest closing configuration computed is at 1.51. LR, at 1.12, closes no line.
- With one common depth and every field's residue free, W66's χ² is at least 403, at y ≈ 0.75.
- The law's offsets, 2–25 in ln, move these depths by roughly 0.16 to 8. So the leading order decides nothing at
  shallow depth; the computed masses above decide there.

**What it shows.**
- On every closing configuration computed — words to length 14 at heights up to 3, and to length 16 from 3 to 6, at
  N = 9, 11 and 12 — no assignment passes S-mass: not the Standard Model, and none of the nulls.
- The hierarchies are too strong from the shallowest threads on, increasingly with height. That is the 19:41 law's
  direction.
- So the per-field thread frame is excluded as computed. Above h = 6 it is bounded only where the law reaches (N = 9
  and 11 from y ≥ 39.5, if its offsets hold). It is not excluded at every depth.

## 4. What they add up to (a reading)

- **The cusp's readings.** The scale-free (BDE) regularisation of the surface frame's mode norms is not a norm, and a
  positive regularised norm of this kind needs a height.
- **The rule that picks no thread** works on the bounded defect, where it gives the typical motion's average. On the
  norms, the deepest pair takes it over.
- **The thread frame.** Its hierarchies are of the right kind: top-heavy and spread over orders of magnitude. But
  in median they are too strong everywhere they were computed, more so with depth, and no assignment fits.
- **None of this fixes a size.** Every route to a value still needs one more choice: a height c, B1654's L, a thread
  or a depth.

chat1, 2026-10-16. 0 of 19.
