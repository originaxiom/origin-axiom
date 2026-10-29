# B1814 — PREREGISTRATION: THE MEASURED WORLD AS A DRAW FROM THE WEAVE'S OWN MEASURE (P-437, stage 3 of the owner's whole-existence computation; P-091's question in main's frame). Draws from each of B1813's two clocks, each carried with its thread's own line through B1656's frame, and the measured six scored for typicality among the worlds the instrument resolves

## Why

- **The owner (2026-10-29).** He asked for a whole-existence computation of the interaction, to see whether it lands on
  the full Standard Model: "see what program produces when not forced", and "count in both ways and see whether both
  ways interact".
- **Stage 1 (B1813).** Left unforced, the weave's threads produce a measure on τ, and the measure depends on the counting
  rule.
  - By moves: Minkowski's measure, kept out of the cusp.
  - By geometric length: hyperbolic area, the move family's critical point.
- **This test** asks the data side, in today's frame:
  - Is the measured world a typical draw, with nothing put in by hand?
  - With B1726's two ingredients by hand?
  - Do the measured depths separate the clocks?
- **P-091.** It answers P-091's question (W57: is the world a typical draw of the seed's own measure?) in main's frame.
  W57's own frame (the ruled branch), its measure and its ten numbers are not regenerated here.
- **What it is not.** It is not a fit: no parameter is tuned. The model is a distribution, fixed below, and the data's
  place in it is scored.

## The frame card (WORKING_RULES, the rule of 2026-10-29 with the amendment: FORCED / ADMITTED / CHOSEN / FITTED, with scope and evidence)

| item | value | label (scope; evidence) |
|---|---|---|
| frame | B1656's four-channel coupling at B1667's canonical end: B1740's sealed census module, `compute(..., which="DR")` unchanged; the Higgs DR | CHOSEN (the record's frame; B1726, B1740) |
| the clock | **A0** by moves: every primitive positive class with both letters of word length 2–16 (8 798 classes). **A1** by geometric length: every such class of trace 3–400 (14 690) | CHOSEN (B1813: the counting rule is chosen; the two natural members declared, no other run). The limits are FORCED given the rule (B1813 § 2) |
| a thread's mass | its geodesic length ℓ = 2 arccosh(t/2) | CHOSEN (B1813 § 1) |
| the point on the thread | uniform in arclength, reduced to the standard domain | FORCED given the mass |
| the line | one of the thread's own flat lines, uniformly among those of exact order 1–12 up to sign | That the thread fixes these lines is FORCED (B1733). The cutoff 12 and the uniform choice are CHOSEN (B1813 § 2; B1713's range) |
| the line at the reduced point | (α, b) ↦ (α, b)γ⁻¹, with γ the reducing map | FORCED (B1724's covariance; control C1c) |
| the radii | B1667's L_max, L₂ at the reduced point, as B1740 reads them (interpolated in Im τ from the Re τ = ¼ column, held outside [1, 4]) | B1667's radii are ADMITTED (a canonical construction at points of the standard domain). The interpolation and the hold are CHOSEN by inheritance (B1712–B1740); the column is flat near Im τ = 4 (the review) |
| the horocycle | **unforced** and **by hand**: drawn uniformly per draw | CHOSEN. The frame does not fix it, and an earlier look found "the six need L_max" (the web seat's THE HOROCYCLE AND THE HEIGHT, harvest row 1455); read-outs fix it either way |
| the readings | **unforced:** each sector's reading drawn uniformly from {S, S̃}. **By hand:** (S̃, S, S) | CHOSEN, and by hand informed by data in earlier looks (B1726). D1h's null therefore chooses freely (below) |
| the lepton factor c | **unforced:** 1. **By hand:** 3 | CHOSEN (B1726, B1789) |
| the floor and the conditioning | a world is **resolved** when all six of its ratios exceed 10⁻¹²; every reference is the arm's resolved draws, and every target must be resolved | CHOSEN (the review's B3). B1740's module reaches its double-precision floor near 10⁻¹⁶ from Im τ ≈ 12. Floored values form atoms that dominate unconditioned statistics (5.8% of A1's draws at the all-six floor; 8.3% of A0's with a zero m₁/m₃, B1716's zeros). The data's ratios all exceed 10⁻⁶. Read-outs at floors 10⁻¹⁶ and 10⁻⁸, and unconditioned |
| the cap | draws above Im τ = 60 not computed: unresolved | CHOSEN (the module overflows near Im τ = 120; at Im τ = 60 every line's ratios are below 10⁻¹², control C1e) |
| data, sigmas, random hierarchies | B1741's `compare.py`, loaded unchanged (sha256 asserted): its data, s6 and s9, and `draws(seed)` | inherited (B1741's input ledger) |
| anarchy | independent complex Gaussian 3 × 3 Yukawas per sector (W57's null) | a read-out arm |

## The model (no data)

- **The census** (`verification/census.py`): 4 000 draws per arm (seeds 18140 for A0, 18141 for A1). Each draw gives:
  - the thread and its trace;
  - the arclength position, and the reducing γ (exact);
  - the thread's line, the transported line and its order (the lcm of the denominators);
  - τ in the standard domain;
  - B1740's full output: every sector in S and S̃ at both horocycles, and the CKM for each (up, down) reading pair;
  - every numpy warning raised in the call.

  A resume drops a line cut by an interrupted run.
- **Controls in the census** (`control.json`):
  - **C1a:** the class counts match B1813 and its referee: 29, 60, 96, 151 and 14 690 at trace ≤ 12, 18, 24, 30 and
    400; 2 536 move classes of length ≤ 14.
  - **C1b:** the reduction is exact: ∣γz − z′∣ < 10⁻⁹ relative.
  - **C1c:** the transport and the radius law, at fixed radii transformed by B1724's law L ↦ L + log∣cτ + d∣, with
    γ = R and γ = TS. The images stay above Im τ = 0.31 (B1724's bound). Two lines; every key; max ∣log∣ < 10⁻⁹; a NaN
    fails it.

    Before the seal, main computed 1.2 × 10⁻¹² (R) and 5.0 × 10⁻¹³ (TS). The wrong transport, (α, b)γ, gives 3.9, so the
    control discriminates.
  - **C1d:** B1740's module with DR reproduces B1726's stored row at (0.35 + 3.05i, line 149) to 10⁻⁹, with no NaN.
  - **C1e:** at Im τ = 60, Re τ ∈ {0.05, 0.3}, on all 266 lines, every ratio is below 10⁻¹² with no numpy warning.

## The observables and the statistics (`verification/compare.py`)

- **The six:** log(c/t, u/t, s/b, d/b, μ/τ, e/τ) against the frame's [m₂/m₃, m₁/m₃] per sector, as in B1741.
- **The nine** add log∣V_us∣, ∣V_cb∣, ∣V_ub∣ (read-outs only).
- **The configurations.**
  - **Unforced mixture:** per draw, the horocycle and each sector's reading are drawn uniformly (seed 18142, the same
    sequence for both arms), with c = 1.
  - **By hand:** (S̃, S, S) with c = 3, and the horocycle drawn by the same sequence.
- **p_nn (W57's P2, leave-one-out, among resolved draws):**
  - The distance is the max over the numbers of ∣x − t∣/σ, with B1741's s6.
  - The target's nearest-draw distance is set against each reference draw's own nearest distance among the others.
- **p_F (among resolved draws):**
  - Fisher's −2 Σ_k log p_k, with p_k two-sided mid-rank marginal p's.
  - The target's statistic is set against each reference draw's own (leave one out).

## Cells

| cell | prediction | prior |
|---|---|---|
| **D1 — THE UNFORCED WORLD** | A1, the unforced mixture, the six, among resolved draws: **p_nn > 0.05** | 70% (it holds for 98% of random hierarchies on the review's sample, below) |
| **D1h — WITH THE TWO INGREDIENTS BY HAND** | A1, by hand, the six, among resolved draws: **p_nn > 0.05** | 75% |
| **D2 — THE CLOCK** | the unforced mixture, the six, among resolved draws: **p_F(A1) > 0.05 AND p_F(A0) ≤ 0.05** | 45% |
| C1 | the census controls C1a–C1e all hold | 95% |
| C2 | B1735's 3.0945633 is reproduced on B1726's census through the loaded B1741 measure | 99% |

### What the cells can say, measured on the review's sample before the seal (data-free)

The sample is the census's first 400 draws per arm through the real frame (the review's 800 calls). It uses σ = 0.15 in
place of s6, B1741's random hierarchies (seed 1741, the first 1 000) and 1 000 anarchy draws. Main's design check is
`audit/review_b1814/main_d2_design.py`.

| statistic (resolved draws) | random hierarchies typical under A1 | under A0 | the D2 pattern (A1 typical, A0 not) | anarchy: the D2 pattern | held-out calibration at p ≤ 0.05 (A0, A1) |
|---|---|---|---|---|---|
| p_nn | 98.4% | 29.0% | 69.4% | 0.0% | 4.3%, 1.4% |
| p_F | 100% | 60.7% | 39.3% | 1.1% | 4.3%, 2.7% |

- **Resolved shares:** A0 91.8%, A1 74.0%.
- **Unconditioned, as first drafted:** p_F's D2 pattern held for 2.2% of random hierarchies, with 97.8% typical under
  both clocks. Near-automatic: the review's B3.
- **What this means for the readings.**
  - **Under A1, almost any hierarchy of the observed kind is typical.** So D1 and D1h holding say little, and their
    failing would say much. The asymmetry is stated now.
  - **D2's information is in its A0 leg.** The measured world either is, or is not, among the 39% of random hierarchies
    the move clock calls atypical.
- **Resolution.** On the sample, the draws' own nearest-distance q95 (σ = 0.15) was 25.8σ (A1 unforced), 22.3σ (A1 by
  hand) and 13.7σ (A0) at n = 400. About 10σ is expected at N = 4 000. The sealed run reports q95 in s6 units per arm and
  configuration.

**Read-outs, not looks:**
- the unconditioned p_nn and p_F of every cell;
- p_F for D1 and D1h, and p_nn for D2;
- every cell in A0 and in anarchy;
- the nine;
- each number's marginal p;
- the nearest resolved draw (τ, thread, line, order and configuration, and each number's ∣x − t∣/σ);
- W57's P4 shares;
- the horocycle by hand: (S̃, S, S), c = 3, at L_max and at L₂;
- the floors 10⁻¹⁶ and 10⁻⁸ (cells and random-hierarchy shares);
- held-out calibration per arm (half the resolved draws as the model, 500 of the other half as targets);
- power: A1 under A0, A0 under A1, and anarchy under each;
- the heights (B1813's C4, foreknown: A0's 0.041 is a +2.3σ fluctuation of seed 18140, the review's three 100k samples
  giving 0.0344, 0.0351 and 0.0336);
- the capped draws, the warned draws, and the share outside [1, 4].

**Specificity and THE_BAR, fixed now.**
- **r per decisive cell:** the share of B1741's random hierarchies (`draws(seed)`, seeds 1741–1760, 4 000 six-targets
  each; mean over seeds) that pass the same cell.
- **D1h is graded by the free null.** Each random hierarchy (the first 1 000 per seed) takes its best p_nn over the 16
  configurations (8 reading triples × c ∈ {1, 3}, the horocycle drawn), because the by-hand configuration was informed
  by data (the frame-card rule; B1798). The fixed-configuration r is a read-out.
- **m = 53.** The joint look ledger counted 47 at B1811's seal. The review found two missing:
  - the web seat's THE HOROCYCLE AND THE HEIGHT (sealed 1dd36cfba before B1811's seal; harvest row 1455), one look;
  - THE FRAME NULL (P-412; sealed e56a311ce; two cells; harvest row 1469), counted conservatively, since its ruling as a
    look is owed.

  So 50 looks preceded this test; its three decisive cells are looks 51, 52 and 53, and m = 53 is used for all three.
  LOOK_LEDGER is corrected at this arc's landing.
- **PASSED** needs r < 0.01/53 ≈ 1.9 × 10⁻⁴, after the third opinion.
- **A typicality cell that holds with r ≥ 1.9 × 10⁻⁴** reads **CONSISTENT, NOT SPECIFIC**: a non-rejection, not a
  positive. The sample says r_D1 will be near 1.

**The reading, written before the run (every outcome).**
- **D1 holds** (expected). The measured six are not atypical of the unforced weave under the geometric clock. Graded by
  r: CONSISTENT, NOT SPECIFIC (as are almost all random hierarchies).
- **D1 fails.** NEGATIVE as sealed, and informative: with nothing put in by hand, the measured world is atypical where
  almost every random hierarchy is typical. Routed to the kill graph.
- **D1h holds and D1 holds.** CONSISTENT, NOT SPECIFIC. The two ingredients are not needed for typicality at this
  resolution.
- **D1h holds and D1 fails.** The ingredients put by hand are what bring the world within the draws.
  - A READING that the frame's missing forcing is c and the reading, graded by the free null.
  - Conditional on resolution: it stands only if the sealed q95 (s6 units) in A1 is finer than the lepton shift log 3
    expressed in s6 units (log 3/s6 for μ/τ and e/τ). Otherwise it is stated as unresolved.
- **D1h fails and D1 holds.** The two ingredients make the world LESS typical than nothing by hand. A NEGATIVE for the
  ingredients as a forcing in this measure (kill graph). The reading is unresolved if the q95 condition above fails.
- **D1h fails and D1 fails.** NEGATIVE as sealed for both. The world is atypical of the weave's critical-clock measure in
  today's frame, with or without the ingredients.
- **D2 holds.** The measured depths sit where the critical clock is typical and the move clock is not.
  - A READING for the flow clock, conditional on the frame.
  - It is not specific: about 4 in 10 random hierarchies do the same, and the A1 leg is passed by almost all of them.
  - It is not a derivation of the clock.
- **D2 fails, both typical.** The measured depths do not separate the clocks: as for about 6 in 10 random hierarchies.
  The clock is not decided by these numbers.
- **D2 fails, A1 atypical.** The critical clock does not carry the measured world: a NEGATIVE for the stage-1 reading's
  data side (kill graph), whatever A0 says.
- **A control failing** stops the reading until it is resolved post hoc, labelled.

## The input-completeness ledger (docs/INPUT_COMPLETENESS_LEDGER.md, its 12 rows)

1. **Scheme.** Inherited from B1741 unchanged: running masses at M_Z (HZ2021), ratios within a sector.
2. **Scale.** One scale, M_Z: a convention. The object supplies none.
3. **Uncertainties.** B1741's s6 and s9 unchanged: the measured relative errors with a 10% allowance in quadrature.
4. **Multi-modal fits.** None for the masses. The CKM appears in read-outs only.
5. **Convention constants.** None enters any cell.
6. **Fit against direct.** Inherited (B1612's CKM data), in read-outs only.
7. **Look-elsewhere.**
   - Three decisive cells, with m = 53 for each, conservatively (above).
   - Each statistic is calibrated on the model's own resolved draws.
   - r is computed on the same cells, and D1h's r by a null that chooses its configuration freely.
8. **The matched null.** B1741's log-uniform random hierarchies (r₂ ∈ [10⁻³, 10⁻¹], r₁ ∈ [10⁻⁶, 10⁻²·⁵]).
   - The box is narrower than the model's range (down to 10⁻¹²). That is conservative for PASSED: the null's targets
     sit where the model is dense.
   - Anarchy is a read-out arm.
9. **The grep.** The sweep's VERDICT lines (Seen first).
10. **The firewall question.** This asks the object for a distribution of values, not a value. The stage assumption
    under test: the weave's own measure, by the declared clock and restricted to resolved worlds, is the measure the
    world is drawn from.
11. **Source freshness.** The archived, sha-asserted sources: B1637's HZ2021 JSON and B1612's data.json, fetched at those
    arcs and not re-fetched here.
12. **Sealing.** Inputs pinned by hash, instruments import-tested and dry-run on a synthetic census with stubbed data,
    outputs committed unread.

## Seen first

- `VERDICT topic-sweep /typical draw|typicality|p_nn|nearest.{0,10}draw|whole.existence|move clock|geometric clock|seed.s own measure/ (full text): 2 of 1560 arcs on main match (PROVED 2); 3 register rows match (QUEUED 3); 13 other lanes match`
  The lanes' matches are mostly COSMOLOGY_LEDGER's "typicality". The SM seat's lane holds W57
  (`docs/dossiers/the_weave_2026-10-07/the_field_of_maximality*.py`, harvest row 1099).
- `VERDICT topic-sweep /typical draw|typicality|p_nn|nearest.{0,10}draw|whole.existence|unforced|anarchy|move clock|geometric clock/: 5 of 1560 arcs on main match (NEGATIVE 1, PROVED 4); 2 register rows match (QUEUED 2)`
  These are claim lines; the "unforced" matches are other senses.
- **Bearing on it:**
  - B1813 (stage 1);
  - W57 and its post hoc read (the seat's branch at c41660ad7, 98250cfb0): the seed's own measure in the ruled-branch
    frame, the data's nearest draw 36.5σ, p_nn = 0.005;
  - B1643;
  - B1716 (the zeros);
  - B1726, B1741, B1789;
  - B1733;
  - B1724;
  - B1667;
  - B1691;
  - B1798 (the class-choosing null);
  - B1811;
  - the web seat's THE HOROCYCLE AND THE HEIGHT (row 1455) and THE FRAME NULL (row 1469);
  - P-091, P-107, P-437.
- **Literature.** Typicality and anarchy in flavour: Hall–Murayama–Weiner (2000); de Gouvêa–Murayama. Measures on
  the moduli space as priors for modular flavour models. None scores a world against a measure generated by the modular
  group's own closed geodesics. Pointers only, not read on the bench.

## Disclosed

- **Known before the seal (data-free):**
  - Stage 2a's quantiles of the frame's m₂/m₃ and m₁/m₃ at the zero line under both clocks (audit room). D2's direction
    is partly anticipable from them: m₁/m₃ < 10⁻⁵ in 7.5% of zero-line draws at s = 0 against 34% at s = 1.
  - The draw sequence's heights and line orders (the smoke test). C4 is a read-out and foreknown.
  - The frame's behaviour high in the cusp: the floor from Im τ ≈ 12, the overflow near 120, the C1e value at Re τ = 0.3.
  - **The pre-seal review ran the frame on the census's first 400 draws per arm** (800 calls) and the census's
    `control()`. Their model statistics are known: the atoms, the φ tails, the nearest-distance scaling, and the sample
    table above.
  - **The conditioning and the choice of p_F for D2 were made after seeing that sample (data-free),** to remove the
    near-automatic outcome the review found. The statistics' shares on random hierarchies above were computed for that
    purpose.
- **No frame value was compared with any data before the seal.** The data files were not opened, by main or by the
  reviewer.
  - The data's magnitudes are general knowledge.
  - B1726's near-fit rows with c = 3 at Im τ ≈ 3, and row 1455's L_max finding, are on record.
  - A1 was made the decisive arm knowing the data are deep.
- **The one-clock remark (noted, not run).** A0 counts threads by moves but places points by arclength. A pure move clock,
  ticking once per Farey crossing, puts τ on Re τ = 0, since every crossing reduces to the imaginary axis. It is not an
  arm here; it is noted for the theory side of P-437.
- **The instruments.**
  - Both were import-tested.
  - The comparison's `main()` was dry-run end to end on a synthetic census, with B1741's data functions stubbed by a
    synthetic σ and a synthetic target (`audit/review_b1814/main_dryrun.py`, 163 s).
  - The census's `tasks()` and the new C1c were run.
  - The census's 8 000 frame calls were not run, and neither was the comparison on the data.
- **The pre-seal review** (hostile, read-only; `audit/review_b1814/REPORT.md`): GO WITH FIXES. Applied:
  - B1, the features() crash;
  - B2, C1c rebuilt with the radius law, R and TS, and a NaN-safe dev;
  - B3, the conditioning, with the cells' power measured and stated;
  - m = 53;
  - P-091's wording;
  - the floor read-outs;
  - the resolution read-out and the conditional reading;
  - every reading pre-written;
  - D1h's free null;
  - the horocycle read-out;
  - the disclosures;
  - C4 as a read-out;
  - the order as an lcm;
  - held-out calibration;
  - the resume and warnings;
  - input-completeness item 8;
  - anarchy in the power read-out.

## Instruments

- `verification/census.py` → `census.jsonl`, `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- **Run:**
  `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 10 python3 -B census.py --workers 8`, then
  `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 10 python3 -B compare.py`.
- **`ARTIFACT_HASHES.txt` pins** both instruments and this preregistration, and, read in place:
  - B1740's census.py;
  - B1733's the_threads_own_lines.py;
  - B1741's compare.py and census.jsonl;
  - B1726's census.jsonl;
  - B1813's referee check3_trace.json;
  - B1667's the_canonical_cusp.json;
  - B1691's the_exponents.py and qseries.py;
  - B1723's b1656_funcs.py.
