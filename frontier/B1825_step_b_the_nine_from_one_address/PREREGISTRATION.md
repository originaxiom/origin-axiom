# STEP B — THE NINE FROM ONE ADDRESS: the card (main, 2026-10-30, filled 2026-10-31; P-495, P-418, P-520–P-523, P-538, P-551–P-554; data-free)

*Drafted before the census was read and sealed with the pre-seal numbers. **Disclosed:** the plan was to commit the
draft before the vacuity calibration and the controls (§ 9 item 7); it stayed in the gitignored audit room instead, so
the record of its design before the controls is the generator committed in S276 (scripts/stepb, tests/stepb) and the
landings S277–S285, not a committed draft. Every item is fixed before any comparison with a measured value. The generator's fifth pre-seal review
(generator_review_5/: GO WITH FIXES, two blocking) is answered in its MAIN_RULINGS.md and the fixes are tested. The numbers filled before the seal (§ 4) come from committed aggregate-only runs, each refused unless the census's manifest is pushed. **Disclosed:** the calibration's dress rehearsal found its pass side, leg's size and anarchy void (every planted six outside B1741's box, P-551), and those three sections were re-planned and re-run on the box (S284) after that was seen; the certification's determinism tolerance was corrected after its first run (P-553). No measured value had been read when either was done.*

## 1. What is tested

- **The frame:** FR-FIB (B1656) as the refined census computes it, through B1821's committed evaluator:
  - the generations' metric H = I, a CHOSEN input (B1822);
  - the band's ends Im τ ∈ [1, 4] and Re τ ∈ [−½, ½], CHOSEN (B1667's radius column), by the mirror;
  - the 266 lines of orders 1–12 (B1713);
  - twelve distinct directions (B1810's thirteen with a₀ ≡ F₋₂, B1824);
  - both radii, the eight readings, and c in the data's nine-value scan {1/3, 1/2, 2/3, 1, 3/2, 2, 3, 4, 5}.
- **The targets:** the six mass ratios (c/t, u/t, s/b, d/b, μ/τ, e/τ) and the CKM moduli with ∣J∣. Their sources and the
  INPUT_COMPLETENESS rows are in § 6.
- **Not tested here:** Step A's vacua. B1823 is NEGATIVE as a compression, so there is no Step A arm.

## 2. The four legs and the one decisive conjunction (the design's section 5, section 9, and main's rulings on the third and fourth reviews and after the interpolant's diagnosis: generator_review_3/, generator_review_4/MAIN_RULINGS.md, generator_review_5/)

- **c.** Our world is scored at c = 3 only (section 9 item 6). Every null world scans the nine values and keeps its best,
  re-making the data's choice. The c = 1 arm is a read-out at c = 1. The address charges log2 9 for c everywhere.
- **τ is continuous (the frame on continuous τ is DEFINED as the census interpolated cell by cell).**
  - Each row's cell carries the biquadratic Lagrange polynomial through its 3 × 3 stencil of the same choice's rows, in the
    natural logs of the nine positive outputs and J SIGNED; |J| is taken after interpolating.
  - A row whose stencil is incomplete (the mixing undefined at a stencil node) or carries a non-finite value (an m1 = 0
    or an exactly zero modulus) is scored at its node alone.
  - The decisions on the interpolant rest on rigorous enclosures: a Bernstein enclosure of each cell's polynomial bounds
    χ² from below, and S is decided by branch-and-bound. A sub-rectangle smaller than 10⁻⁷ in τ is not split: its
    search is UNDECIDED, counted, and treated conservatively (p2's upper end counts undecided worlds as hits; a NO
    SUPPORT reading names any). The mixtures' windows drop at most 2^−30 of their mass, rigorously bounded.
  - The quadrature: 4 × 4 Gauss points on every window row, 16 × 16 on every row that can carry 2^−34 of the total, and a
    32 × 32 check on the rows carrying all but 2^−20 of the mass (measured: 16 × 16 errs at most 0.004 bits on a choice's
    total at σ = ALLOW).
  - **The certification** measures this frame against fresh evaluator points before the seal: the planted gate (§ 4).
- **S, support.** χ²_ten < 23.21 at a row with the mixing defined, at c = 3, anywhere on continuous τ.
  - The ten are the six, |V_us|, |V_cb|, |V_ub| and |J|.
  - **23.21 is CHOSEN:** χ²_10's 0.99 quantile, keeping B1747's tail; χ²_nine < 21.67 is a read-out.
  - χ² is in natural log, with σ = the relative error in quadrature with 0.10 (B1741), from the σ-only file (§ 6).
- **X2, specificity.** p2 is the fraction of null worlds the same search puts in the support (N = 2 000, not the 10⁶ first
  written: § 4; its two-sided 95% Clopper–Pearson upper end is graded, and its lower end already exceeds the gate).
  - The null worlds' six come from B1741's sealed box.
  - Their mixings and |J| come from the frame's own unconditional marginal (BL1), drawn independently of the six, over the
    frame's PHYSICAL choices: a choice whose |V_us|, |V_cb|, |V_ub| or J is a structural zero (below 10⁻¹² at every τ:
    m1 = 0 where the coupling has rank 2, B1653; J = 0 where the CKM is real) yields no world of our kind. The floor
    10⁻¹² is CHOSEN (on the mini patch the roundoff lies below 10⁻¹³ and the physical values above 10⁻¹¹). The
    restriction is conservative: on the mini patch no non-physical world was ever supported (0 of 4096 and of 1922, against
    physical rates of 0.06% and 1.4%), so it raises p2 by 1/(1 − π) and lowers bits_CKM by log2 1/(1 − π), π the
    non-physical choices' share of the prior: π = 0.214 on the census (40 000 of its 50 880 choices are physical).
  - A null world with a non-finite entry (an exactly zero modulus) is dropped and counted.
- **K, compression of the ten.**
  - C_ten = C_six + bits_CKM exactly.
  - L_raw is the primary null's code: the box for the six, and the frame's physical marginal for the four.
  - L_ours = A + τ's mixture of the six's misfit + the four's code under the six's posterior, with
    A = log2 266 + log2 12 + 1 + 3 + log2 9 = 18.81 bits.
  - **K PASSED** = C_ten > 0 and p_K < 0.01/m.
  - **p_K = 2^−C_ten, the exact likelihood-ratio bound.** C_ten = log2(q/p0) with q a sub-probability (the two-part code
    satisfies Kraft's inequality), so P0(C_ten ≥ c) ≤ 2^−c at every c (Markov). The fourth review's ranking by C
    (F3) is thus evaluated by its exact bound rather than by simulation: conservative, and without Monte Carlo error at the
    gate 0.01/m ≈ 2 × 10⁻⁴. **This departs from the bar's literal "length at most L_ours"**: under the CKM's non-flat
    marginal the length ranking is not a likelihood ratio and has no such bound (F3). The check P0(C ≥ c) ≤ 2^−c is run
    before the seal on the supported null worlds weighted by p2's lower end (§ 4), and it can fail.
  - **K is UNJUDGED** when its quadrature's checks (32 × 32 within 0.01 bit, or 64 × 64 after a switch) or its windows'
    dropped-mass bounds (2^−30) do not hold; the reason is reported.
  - K PASSED is therefore C_ten > gate_bits(m) = log2(m/0.01) (12.37 bits at m = 53).
  - C_six alone is a read-out: it is capped near 2 bits at the data's precision.
- **The CKM leg (BL1).**
  - The statistic is the bits of information the six's posterior gives about the four, against the frame's physical
    unconditional marginal.
  - **p_CKM = 2^−bits_CKM, exact:** under the null the four are drawn from the marginal, and E[p_post/p_marg] ≤ 1 (equal
    when no posterior mass sits on non-physical choices).
  - Its own support clause, on continuous τ: some address the six support (its χ²_six within 13.86 of the least, i.e.
    posterior density within 2^−10 of the top) reaches the four with χ²_4 < 13.28 (decided by branch-and-bound).
  - **The double use, stated:** the leg's bits are K's mixing half, so the two legs are graded on one null and are not
    independent; and J enters S, K and the leg (C7 puts J in S).
- **PASS** = S and X2 and K and CKM.
  - m = the joint look ledger's count at the seal plus one, at least 53.
  - T NEGATIVE under every clock of the menu makes the attempt NEGATIVE. The bar discloses that the bare named clocks
    cannot make T NEGATIVE; the run grades T under area (exact) and stops for the menu's other clocks only if area is
    NEGATIVE.
  - The sixteen readings are pre-written in generator/outcome.py, in THE FINAL ATTACK's words.
- **X1 (exclusion): none claimed.** A NO SUPPORT reading is NOT FOUND within the census's reach (the 266 lines, the twelve
  directions, both radii, the eight readings, Im τ ∈ [1, 4]) and its resolution (§ 4's planted miss rate); it excludes
  nothing beyond them.
- **THE CONJUNCTION CANNOT PASS (stated before the seal).** X2 fails at the sealed N, already computed: p₂ = 3/2000, its
  upper end 4.4 × 10⁻³ against the gate 0.01/m = 1.89 × 10⁻⁴ (§ 4). Random worlds (B1741's box with the frame's own CKM
  marginal) fall in the frame's support about eight times more often than the look-elsewhere-corrected gate allows (the
  point estimate; at least 1.6 times at the interval's lower end, 3.1 × 10⁻⁴, so at 97.5% confidence p₂ exceeds the gate
  and no larger N would be expected to rescue X2). So PASS is unreachable, and Step B's
  decisive cell is **S**: SUPPORT WITHOUT SPECIFICITY if our world is in the support, NO SUPPORT if it is not (outcome.py's
  pre-written readings). **Graded: S and X2 decide the reading; K and the CKM leg are computed and reported with their
  exact bounds and cannot alter it** (they remain part of PASS's definition above, which X2 already rules out).
- **The pass side, before the card** (MB12). A world planted at χ²_ten near 0 must reach C_ten > gate_bits and the CKM
  leg with the real σ. If it cannot, the card says, before the seal, that the conjunction cannot pass and that Step B
  grades S, X2 and the CKM leg. **Measured (§ 4, on B1741's box): it can. At χ² = 0, 7 of 10 planted worlds reach both
  (and S); with noise at σ, 1 of 10 (the CKM leg alone 5 of 10).** K and the CKM leg are not void; the conjunction
  cannot pass for X2's reason alone.
- **Read-outs, never grading:**
  - the c = 1 arm, χ²_nine, C_six and the argmin;
  - at the least-χ² address, χ²_ten by a FRESH evaluation (the evaluator itself, beside the interpolant's value);
  - T1 under each clock of the menu, where computable;
  - the box at ×½ and ×2; B1814's arm N for the CKM; P-538's principled-line mixture code; WP for τ; B1735's χ² on the DR
    slice — each computed after the run if time allows, never grading (anarchy is a pre-seal control, § 4).
  - "J for V" is withdrawn: C7 puts J in S.

## 3. The line's price (P-538, main's ruling)

- The graded code prices the 266 lines uniformly, at 8.06 bits. No principle that selects a line is derived, and the null
  shares the code.
- A zero-line world stays reachable at c = 3 with a reading that splits up from down.
- **Read-out:** the principled-line mixture code.

## 4. Numbers filled before the seal (committed aggregate-only scripts; each refuses a census whose manifest is not pushed)

- **The certification** (scripts/census/rigid_census_certification.py; refused unless the manifest is pushed):
  **13 390 cells, 2 241 262 planted worlds, 4 722 missed: 0.21%; Clopper–Pearson upper end 0.217%, bootstrap 0.226%:
  the planted gate PASSES (≤ 1%).** The ten-output worlds alone: 2 713 of 1 519 322 missed (0.18%). 0 undecided searches;
  14 244 node-only owners; 3 396 591 outputs removed by the floor. Read-outs: the planted worlds' best χ² has median
  3.4 × 10⁻⁵ and q99 5.93; the pointwise |log10| error has q99 0.0091 (q999 0.15), 0.52% of values above 0.0217
  (J 2.2%, the three moduli about 0.8%, the masses 0.05–0.25%).
  - **the planted gate.** At a hash-chosen 5% of the cells, a hash-chosen interior point Q is evaluated fresh; every
    row's outputs there are a planted world, found when the cell's own interpolant reaches χ² < T (node-only rows: their
    node). Other cells could also reach it, so the measured miss rate is an upper bound on the frame's. The gate: the
    larger of the Clopper–Pearson upper end and a 97.5% bootstrap over cells (the design effect of 192 rows sharing one τ)
    is at most 0.01, the threshold's own 1%.
  - **It replaces the fourth review's pointwise gate (F2).** F2 fails wherever the frame has isolated zeros (a log
    singularity no interpolant follows) although the decisions are robust there. On the mini patch F2's q99 is 0.047
    against 0.0217 log10 at the cells' corners (2.0% of points above it; J and |V_ub| the worst), and 0.024 at interior
    points. The pointwise errors per output stay as read-outs.
  - **The floor rule:** an output below 10⁻¹² at Q or at a stencil node is a structural zero, not a value the frame
    produces; the world is planted on its k remaining outputs at χ²_k's 0.99 quantile, and the removals are counted.
    Without the rule the patch's corner miss rate was 12.8%, all of it roundoff; with it, 0.36% (corners, any of four
    cells) and 0 of 1584 at interior points (upper end 0.23%).
  - **determinism** at one node per line (the census must equal a fresh evaluation at its own precision): **PASS**
    (preseal/determinism.json; the committed certification.json still reads "gate": "FAIL", from the first run's
    tolerance alone, and is kept as computed).
    266 nodes, 487 692 values: every one agrees, and none differs by more than the storage bound (the census writes
    8 significant digits, '%.8g', whose rounding error reaches 5 × 10⁻⁸ relatively, 2.171 × 10⁻⁸ in log10; the largest
    difference is 2.159 × 10⁻⁸). **Disclosed:** the certification's first run applied 10⁻⁹ in log10, which 8-digit storage
    cannot meet, and failed its overall gate on this alone; the tolerance was corrected to the census's precision
    (census_io.dup_disagreement) and the check recomputed by a separate committed script (rigid_census_determinism.py,
    S284; P-553), the second post-hoc tolerance correction after S280's. The planted gate does not depend on it.
  - **B1824's duplicate:** a₀ and F₋₂ agree at the census's precision everywhere (largest disagreement 0.0 under
    census_io.dup_disagreement; S279's diagnostic found every disagreement of the plain log10 check to be roundoff
    between two structural zeros or the double-precision limit of a tiny m1/m3: a corrected check, disclosed, S280).
- **p₂ = 3/2000 = 0.0015, two-sided 95% interval [3.1 × 10⁻⁴, 4.4 × 10⁻³]** (0 undecided; the nine's read-out 5/2000,
  [8.1 × 10⁻⁴, 5.8 × 10⁻³]). N is 2 000, not the 10⁶ first written: on the full census the support search costs 2.3 s a
  world (1.9 × 10⁴ candidate cells a world over the nine c), so 10⁶ would take about 27 days, and N = 2 000 decides the leg:
  **X2 fails at N = 2 000, and the interval's LOWER end exceeds X2's gate 0.01/m = 1.89 × 10⁻⁴: at 97.5% confidence p₂
  exceeds the gate, so no larger N would be expected to make X2 pass.** A smaller N only makes X2
  harder to pass; it cannot favour the frame;
- **the vacuity calibration:** among supported null worlds, the fraction with K failing and with the CKM leg failing.
  The design is VOID only if a failing fraction is 0 (K or the leg implied by support); a fraction near 1 is the healthy
  outcome. **Measured (the dress rehearsal, serial; P-552): all 3 supported null worlds p₂ found (M = 3, not the 100
  first written: a judged K costs 3–6 minutes serially and forking the 29 GB index is barred, S283) were judged (1 not
  converged); K fails on 3 of 3 and the CKM leg on 3 of 3 (each [0.29, 1]): NOT VOID.**
- **the Markov check:** P0(X ≥ c) ≥ p2_lo · P(X ≥ c ∣ S) against 2^−c for c = 1 … 16, X = C_ten, bits_CKM and C_six,
  on the supported null worlds (unconditioned worlds rarely reach the frame, so a check on them would have no power).
  **Measured: every bound holds.** Of the 3 supported worlds, C_ten ≥ 1 and ≥ 2 on one, ≥ 3 on none; bits_CKM ≥ 1 on two,
  ≥ 2 … 6 on one, ≥ 7 on none; C_six ≥ 1 on none; 5 unconditioned worlds, none with C_ten ≥ 1. Its power at M = 3: three
  of three supported worlds at X ≥ c would fail it from c = 14 (one of three only from c = 19, beyond the grid c ≤ 16, so
  not testable here): with all three supported worlds that high it can fire just above the
  gate (12.37 bits), where a false pass would matter, and not below;
- **the pass side:** planted worlds off the grid at χ² = 0 and with noise at σ, and on the grid (sanity, S alone: the
  dress rehearsal's 10 of 10 stands, since S needs no box; it was not re-run on the box). **The dress
  rehearsal's planted worlds were drawn from the frame's whole prior, and every one had six outside B1741's box, where K
  is undefined (L_raw = +∞): S held on 10 of 10 at χ² = 0, 10 of 10 with noise and 10 of 10 on the grid, but no K was
  judged, so that section measured nothing for K or the CKM leg (P-551; the tests' synthetic six lie inside the box). The
  pass side is measured on the box instead (scripts/stepb/calibration_inbox.py, S284), where the target lies by the box's
  construction. The frame's mass in the box: 4.74% of its prior (3 790 of 80 000; [4.59%, 4.89%]). At χ² = 0: S 10 of
  10, K 7 of 10 ([0.35, 0.93]), the CKM leg 7 of 10, all three 7 of 10; C_ten's quantiles (10%, 50%, 90%) 6.9, 13.4,
  17.0 bits. With noise at σ: S 10 of 10, K 1 of 10 ([0.003, 0.45]), the CKM leg 5 of 10, all three 1 of 10; C_ten 1.5,
  7.4, 10.2 bits. The design's power is real at an address and low a σ away from one. THE SIX DO NOT COMPRESS: C_six's
  90th percentile is negative in every section (−0.85 bits at χ² = 0, −2.5 with noise): the address's 18.8 bits, τ's
  mixture and the misfit outweigh the six's raw code at σ, so K over the ten passes only through the four's predictive
  bits (bits_CKM's median 15.6 at χ² = 0, 12.2 with noise), and K and the CKM leg are nearly one test here (P-554).
  The scope is the dress rehearsal's (10 worlds a section; P-552);**
- **the leg's size:** unrelated CKMs (the frame's own physical marginal) and, E20's negative control, anarchy CKMs
  (Haar-random unitaries); FN-texture populations are not computed. **On the box: the CKM leg passes 0 of 10 unrelated
  CKMs ([0, 0.31]; bits_CKM's median −132; one of the ten not converged) and 0 of 10 anarchy CKMs ([0, 0.31]; median
  −81).** None of these worlds is in the support (S 0 of 10 each): the leg's size is the CKM leg's rate on worlds whose
  six come from the frame and whose four do not, unconditioned on S, unlike the vacuity calibration. The dress rehearsal's
  0 of 10 each were void (no world judged, P-551);
- **the DR slice (done, data-free):** the census's evaluator reproduces B1726's sealed DR census on 40 random points of it
  (every sector, both radii, both readings, every CKM pair): largest |ln| difference 5.8 × 10⁻¹¹ for the ratios,
  1.3 × 10⁻¹⁰ for the moduli, 1.4 × 10⁻⁹ for J (B1726 writes w = aτ + b, B1821 w = aτ − b: B1726's line (a, b) is the
  census's (a, −b); the coupling module is byte-identical in both). B1735's χ² on the slice uses data: a post-run read-out;
- **the census's structure** (50 612 352 rows; P-543; drivers' census_structure.py): **R and t = −5/288 are structurally
  dead for our world** — every row of both has m1/m3 at the floor in all three sectors and J at the floor (a rank-2
  coupling and a real CKM), so neither can produce our world (the address code still charges them, and the null shares
  it). The other ten directions carry m1/m3 at the floor in 2.7% of rows (up and down) and about 20% (leptons), J in
  9.6–11.0%, |V_us| and |V_ub| in about 6%, |V_cb| in 3.4–3.8%, and undefined mixings in at most 42 394 rows (F₋₁₀); c/t
  never. π, the non-physical choices' share of the prior, is 0.214 (40 000 of 50 880 choices physical; p₂'s count);
- **the integrity**: the manifest pushed before any read (guard.py); the σ-only file (§ 6).

## 5. The priors (the bar's § 6 template; written before the census was read)

| cell | prior | reason |
|---|---|---|
| S IN SUPPORT for the ten at c = 3, continuous τ, the twelve directions | 12% | the bar's 10% for the nine with J (one Higgs fails the CKM, B1747), a little higher for continuous τ and the full menu, against J inside S |
| X2 PASSED (p₂'s upper end below 0.01/m), given S | 10% | the four come from the frame's own marginal, so the null's CKM is the frame's; the six's box is wide, and a frame that reaches our six at c = 3 reaches many boxes' worth (B1798's m·r 0.034–0.082 for the six) |
| K PASSED (C_ten above gate_bits), given S | 5% | the bar's 5%: "reaches the six mass ratios only by spending about as much freedom as they carry"; the CKM half must carry about 10 bits |
| the CKM leg PASSED, given S | 5% | the six's posterior must predict the four sharply against the frame's own marginal; one Higgs fails the CKM (B1747) |
| T NEGATIVE under every clock, given S | under 1% | the bare named clocks cannot (the bar's T2), and the run grades area exactly |
| PASS, unconditionally | about 0.1% | K and the leg share the bits (not independent), so not the product; below THE FINAL ATTACK's ≤ 2% |

## 6. The inputs: sources, σ, and INPUT_COMPLETENESS rows 1–13

- **The targets, read once at the run:** the nine from B1741's sealed comparison (compare.arrays()'s T9: natural logs, in
  σ's order (c/t, u/t, s/b, d/b, μ/τ, e/τ, |V_us|, |V_cb|, |V_ub|)); |J| from the PDG 2024 CKM review's global fit (Phys.
  Rev. D 110, 030001, § 12.3), the same fit whose moduli B1741's σ reproduce.
- **σ: the σ-only file** (sigma/SIGMA_ONLY.json, written once by sigma/extract_sigma.py on 2026-10-30): the nine from
  B1741's compare.sigmas() (its sealed measure; its central values not read), |J|'s relative error 0.0401 (the global fit's
  +0.13/−0.12 symmetrised).
- **J, pinned before the seal:** the PDG 2024 CKM review (§ 12.3, fetched 2026-10-30) reads "the Jarlskog invariant is
  J = 3.12^{+0.13}_{−0.12} × 10⁻⁵"; the run takes J = 3.12 × 10⁻⁵. B1741's compare.py carries J_PDG = 3.08 × 10⁻⁵
  (+0.15 −0.13), the 2022 edition's value under a 2024 label (P-546); B1741's grades did not use J. Natural log: (0.1038, 0.1979, 0.1327, 0.1231, 0.1000, 0.1000, 0.1000, 0.1018, 0.1029,
  0.1077). The pre-seal drivers read only this file; none imports compare.py.
- **INPUT_COMPLETENESS (docs/INPUT_COMPLETENESS_LEDGER.md, its 12 rows, and row 13):**
  1. **Scheme.** Inherited from B1741 unchanged: running masses at M_Z (HZ2021), ratios within a sector; the CKM moduli
     and J from the PDG 2024 global fit.
  2. **Scale.** One scale, M_Z: a convention. The object supplies none.
  3. **Uncertainties.** B1741's σ for the nine unchanged (the measured relative errors with a 10% allowance in
     quadrature); |J|'s 0.0401 with the allowance; the σ-only file. The uncertainties are used, never the values, before
     the seal.
  4. **Multi-modal fits.** None for the masses; the CKM's global fit is quoted unimodal at this precision.
  5. **Convention constants.** None enters any cell. c is an arm: ours at c = 3, every null world scans nine values.
  6. **Fit against direct.** |V_cb| and |V_ub| from the global fit (B1741's σ reproduce its 1.9% and 2.4%); the direct
     determinations' inclusive/exclusive tension is not used.
  7. **Look-elsewhere.** m = 53: the joint look ledger's 52 through B1814, plus this one decisive conjunction. The menu's
     choices and c are charged in A, and every null world re-makes them.
  8. **The matched null.** B1741's log-uniform box for the six; the frame's own physical CKM marginal (BL1) for the four;
     the frame's marginal and anarchy for the leg's size.
  9. **The grep.** The sweep's VERDICT line (Seen first, below).
  10. **The firewall question.** This asks FR-FIB at a rigid address to contain our world's ten and to compress them. The
      dictionary is UNEARNED (I-31, I-32, I-23, I-33 and I-13), so any outcome is a READING until earned. H = I is CHOSEN
      (B1822), and so are the band's ends and the floor.
  11. **Source freshness.** The archived, sha-asserted sources: B1637's HZ2021 JSON through B1741's compare.py (hashed,
      not opened, at the seal), and the PDG 2024 CKM review (fetched 2026-10-30; J pinned above). Nothing is re-fetched at
      the run.
  12. **Sealing.** Inputs pinned by hash (ARTIFACT_HASHES.txt); instruments import-tested and run end to end on a
      synthetic census with stubbed data (tests/stepb); the run's outputs committed unread.
  13. **Reach and resolution (P-521).** The reach: 266 lines, twelve directions, both radii, eight readings, Im τ ∈ [1, 4]
      and Re τ by the mirror. The resolution: the certification's planted miss rate, 0.21% (Clopper–Pearson upper end 0.217%, bootstrap 0.226%). X1: a NO SUPPORT is NOT FOUND
      within them.

## Seen first

- `VERDICT topic-sweep /nine from one address|ten from one address|step b|refined census|continuous tau|bernstein|planted
  miss|likelihood.ratio bound|interpolant/ (full text): 21 of 1570 arcs on main match (NEGATIVE 2, OPEN 1, PROVED 18); 17
  register rows match (DONE 7, QUEUED 10)` (2026-10-30, before the census was read). OPEN_LEADS names Step B as the
  attack's sealed step.

## 7. Disclosed (the design's § 7, and since)

- **The DR slice is B1726's census.**
- **Already seen:** c = 3, the 2/5 family, the menu, the allowances, the box and the thresholds.
- **The census read before the seal as aggregates:** B1819, B1820 and the certification.
- **Since the design:** B1822 (H = I CHOSEN), B1823 (no Step A arm), B1824 (twelve directions), P-538.
- **Seen on 2026-10-30, for σ:** the σ-only file's numbers (relative errors only); and J's PDG 2024 central value, read
  while confirming its relative error from the review's text (public; the census was not compared with it).
- **Seen by the fifth review (an agent of main):** compare.py's source lines 1–75, which carry J_PDG and the down sector's
  target constants (to check the order of T9 and σ); no data file was opened and compare.arrays() was not called.
- **The interpolant's diagnosis** (audit/verify_census_tools/, a 5 × 5 patch of the real evaluator on one line, no measured
  value): isolated zeros and J's zero curves are where interpolation fails; node-only scoring misses 9.2% of planted
  worlds against 0.4% interpolated; the 4 × 4 rule errs up to 6.5 bits. Its rulings are § 2's.

0 of 19.
