# The big run: the rule, version 2 (amended before the look)

*Main, 2026-11-14, after the web seat's cold read W-F18 of version 1. Version 1 (B1932's `BIG_RUN_RULE.md` and
`big_run_look.py`) stays as sealed and is run beside this one. Version 2 governs. Every amendment below was written
after main's values were computed (B1932), with the data files unopened by main. None of it is chosen after a
comparison: no comparison with measured values has been made.*

## What is compared (unchanged)
- **Frame C's seven claimed rows** (docs/total_inputs_scoreboard.json, frame C, claims 1, 2, 3, 4, 7, 8, 9):
  - up m₂/m₃ and m₁/m₃, set against c/t and u/t;
  - down m₂/m₃ and m₁/m₃, set against s/b and d/b;
  - ∣V₁₂∣, ∣V₂₃∣ and ∣V₁₃∣, set against ∣V_us∣, ∣V_cb∣ and ∣V_ub∣.
- **How the rows are written.** The scoreboard names the four mass numbers as adjacent ratios. The statistic uses B1720
  compare.py's rows (c/t, u/t, s/b, d/b), as P-341 binds; these are the same four numbers written differently.
- **The pairing of positions with particles** is the dictionary's (identification I-26, unearned).
- **The values:** B1932's `BIG_RUN_VALUES.json` (sha256 df1c9bee…), unchanged.
- **The four declared options:**
  - **W₋** = (up S̃, down S, leptons S), the record's practice;
  - **W₊** = W₋'s mirror, (up S, down S̃, leptons S̃) (P-847; B1932's `assemble_values.py`);
  - each with the measure (a) move count or (b) area.

## The statistics: what governs and what is reported (W-F18's O2, O3)
- **Governing, on the seven claimed rows:**
  - **χ²₇** as in version 1: the bar 22.04, the 1 % tail of χ²(7) after the four options.
  - **The coarse cell (new, O3):** B1720's, every row within a factor 3 (the worst factor ≤ 3).
  - **Both are calibrated.** For each, the best of the four options is calibrated against 4 000 random target sets
    drawn by B1720's law. The seed is 20261115, one stream for every statistic.
- **Reported, as P-341 binds (O2):**
  - **χ²_six and χ²_nine** at compare.py's rows, with P-341's bars as written (16.75 and 21.67), their coarse cells and
    their calibrations.
  - **The lepton rows are frame C's own:** at level 5 the lepton coupling is the down coupling transposed (B1934). The
    leptons take the same Higgs reading as the down quarks in both worlds, so μ/τ and e/τ equal the down m₂/m₃ and
    m₁/m₃. agy-exp's X-EXACT-W read-out has its lepton ratios equal to its down ratios to 3.5e-11.
  - **These rows do not govern.** Frame C does not claim them: the scoreboard's status for frame C says so, in a commit
    of 2026-11-14 08:40, before the values (12:46). The record already notes that the measured split between the
    leptons and the down quarks forbids the copy (B1839's arc).
  - The four cells are reported for every option and stand beside the governing outcome.
- **σ:**
  - masses: both masses' relative errors in quadrature, plus 0.10²;
  - moduli: the data's own error with 0.10 in quadrature (B1735's definition; compare.py has no χ² on the moduli).

## The outcome, fixed now (O5, O7)
- **An option passes** if its χ²₇ < 22.04 and every one of its seven rows is within a factor 3.
- **PASS:** at least one option passes, and both calibrations of the governing statistics are below 1 %.
  - **Every passing option is reported, none preferred.** The inputs of each stay inputs.
- **PATTERN MATCH:** no PASS, but some option meets the coarse cell and the coarse cell's calibration is below 1 %. As
  P-341 says, this is a pattern match, not a value match.
- **FAIL:** otherwise. Nothing is refitted.
- **Banking:**
  - Any outcome is banked only after the look's second computation: a seat with the pinned files re-runs both scripts on
    the committed values.
  - A FAIL's page says what the wall teaches.
  - A PASS is banked as more than a reading only after the third opinion (P-339, P-342).
- **Version 1's outcome** is reported beside version 2's, as version 1 defines it.

## Not compared (O10)
- **The firewalled cross-sector rows.** Frame C holds out rows 11 and 12 (m_b/m_t, m_τ/m_b); they stay held out. This
  run does not compute or open them.
- **J's sign:** it needs the hand.
- **Anything not in the values file:** it is not part of this run and cannot be added after it.

## The weight (O8)
- **The switch.** The run uses the exact channel weight: N = 2πL₂ + c_s − π∣a₀∣²e^{−2L₂}, Theorem 90's leading form,
  which matches the exact horoball norm to about 1e-5 (B1838's note; B1932).
- **The scoreboard's C06** declared the truncated √(2πL + c_s), with the exact norms not used.
- **When and why.** The switch was made after the values were first computed with the truncated weight, which moved
  four values by about 1 %. Its reason, Theorem 90, is dated before.
- **Its reach.** At most about 1.6 % in ln. Against the σ floor of 0.10, no pull moves by more than about 0.16.
- C06 carries a dated line naming this departure.

## Priors (O1)
*Written 2026-11-14, after main's values were computed, with the data files unopened by main.*
- **Governing outcome:** PASS 0.05, PATTERN MATCH 0.10, FAIL 0.85.
- **No option is preferred.** The four share each probability equally.
- **The reported P-341 cells:** main expects χ²_six and χ²_nine to fail on the lepton rows (B1839's note). Prior that
  any option passes either cell: 0.02.

## The second computations, and when the run may go (O4, O9)
- **The tolerance** was fixed in `second_computations.py` before that script first ran:
  - per value, ∣Δ ln∣ ≤ 3 √(e_main² + e_seat² + δ²);
  - each code's stated relative error, with δ = 5.4e-3 (the record's bound on the read-out's systematics: the end
    above Im τ = 6, 5.4e-3; the grid interpolation, 4.6e-3).
- **Agreement** means every value of an option within the tolerance.
- **What the tolerance can and cannot tell.**
  - Its width (about 1.7 % in ln) is small against the statistic's 10 % floor.
  - It does not separate the exact weight from the truncated one.
  - So the comparison also reports z against the two codes' sampling errors alone, for the seat's exact-weight values and
    for its truncated-weight values.
- **The run waits** until each of the four options has at least one agreeing second computation.
  - If a second computation disagrees beyond the tolerance, the run waits until the difference is found.
  - Any corrected values file is committed beside B1932's with a new seal; both stay in the record.
- **Labels.** An option with one agreeing second computation carries "recomputed independently (one seat)". The other
  seat's computation, if it arrives later, is compared, and its result is entered beside the look.
- **Blindness is not assumed.** The values file is public on main, so a second computation is a recomputation on
  independent code. It is not a blind one.
- **State at this writing:**
  - **W₋|a and W₊|a:** recomputed independently by agy-exp's X-EXACT-W, in agreement (worst 0.34 of the tolerance).
    Against the sampling errors alone, the residual is rms z 2.1 (W₋) and 1.6 (W₊). The seat's truncated-weight values
    sit further away, at rms z 4.9 and 3.4.
  - **W₋|b and W₊|b (area):** owed. agy-002's A2-CANON-T90 covers them (its expectations are committed at 0e08a8953).

## The order of operations
1. **Now:** this rule, `big_run_look_v2.py` (its sha256 in FINDINGS), the comparison script and its output are committed
   and pushed.
2. **Before the run:**
   - every option has an agreeing second computation, as above;
   - agy-002's comparison is added to `second_computations.py`'s output under the same tolerance.
3. **The run:**
   - `python3 -B big_run_look.py` (version 1, in B1932), then `python3 -B big_run_look_v2.py` (version 2, here);
   - both outputs are committed before anyone reads them;
   - then they are read and banked as above.

## Amendments before the look (2026-11-14, evening; the sweep of 2026-11-14, P-851)

*Written after the sweep listed 21 points that bear on the run (`docs/THE_SWEEP_OF_2026-11-14.md`, S1 to S21). Each is
met below or made a condition. The script `big_run_look_v2.py` is unchanged; its seal stands.*

**A1. What the run is (S1).**
- **Not the programme's final comparison.** The run is a reading of frame C, made at the author's word (P-850). It is
  not the programme's sealed card (WP-5.3, WP-6.1), and it does not rest on:
  - the clean-up packages still open (WP-5.1 started; WP-5.2, WP-5.3, WP-5.4 and WP-6.1 not started);
  - the debts not yet joined to the map (P-773);
  - the spine's upstream audit and an independent challenge (milestone M3).
- **Its outcome stays a reading** until those are done, whatever it is.
- **The programme's conditions stand unchanged for its final comparison:** P-773, P-776 and P-782 (B1861). Each of
  those rows carries a dated note saying so.

**A2. The calibration's windows (S2; audit finding V1).** B1720's windows for the random targets are a declared choice,
and their price is not known. A companion script reports the governing calibrations with each window's ends moved
half a decade out and half a decade in. It is reported, not governing, and is sealed before the look beside this rule
(`big_run_windows.py`).

**A3. The acceptance test of P-776, applied to frame C's read-out (S3; harvest row 1683, R1 to R8).**

| | condition | frame C's read-out |
|---|---|---|
| R1 | every ingredient listed and typed | met: frame C's nine joints, each typed (the scoreboard) |
| R2 | a state of the whole | met: the average over all threads of the weave (B1928) |
| R3 | existence and uniqueness | met: the limit exists and is the same at every point of order 5 (B1928) |
| R4 | symmetry computed first | met in part: the modular group on the channels (B1935); no move exchanges the two Higgs worlds; the gauge group of the flat line invisible (B1938) |
| R5 | what counts as a place | does not apply: the read-out places no point of the modulus (τ-free, B1928) |
| R6 | survives its own choices | not met as a selection: the measure moves the values by 10 to 80 %, so it is carried as two options; the end is fixed by B1927's convention; the weight has two forms (B1932) |
| R7 | the vacuity control at other levels | not run for frame C's read-out. An open premise of the reading |
| R8 | no measured number in design or run | met until the look |

By the test's own typing, the read-out is **a result given its listed ingredients, not a selection.** The run reads it
so.

**A4. The frozen list (S4; P-767, R6).**
- **The list.** The seven claimed rows of this rule, as committed at a29c459a5 and pushed in 2bdfc498a, are the frozen
  second list for this comparison.
- **How the outcome is printed.** The seven claimed rows come first with the governing outcome. P-341's reported rows
  stand apart. The headline's ruled form (P-767's R6) is applied when the outcome is written, with WP-0.12's status
  stated beside it.

**A5. The end (S5).** Frame C uses B1927's canonical end, the length-2 horocycle that analyticity selects, as a stated
regularity condition (C05). So V4's continuous family of ends is answered in frame C by one declared choice, not by a
free parameter.

**A6. The scale (S6, S7).**
- **The data.** The data are running masses in MS-bar at the common scale M_Z (the pinned HZ2021 file) and the PDG
  mixing moduli. A ratio of two masses at a common scale is scheme-independent to leading order, and the moduli run only
  weakly (the SM seat's inventory SM-C4).
- **Frame C's values** are tree-level ratios with no running (C09, chosen), set beside the data at M_Z, as in every
  earlier sealed look.
- **Open premise.** Whether M_Z at tree level is the right expectation is an open premise (P-590, P-722 (3)).

**A7. The conditions before the run (S8, S10, S11, S12, S14, S16).** The run waits for every one of these:
- **The area options' values.**
  - Main found that the frame's double-precision singular-value decomposition loses the singular vectors high in the
    cusp: above about Im τ = 11, the identity F̄(τ + 1) = F̄(τ) fails by up to 12 % at height 12, and more above it.
  - B1932's area options (W₋∣b and W₊∣b) integrate F̄ up to height 45, and the area measure gives the region above
    height 11 about 9 % of its weight. Their mixing values carry that noise.
  - The move-count options do not: their read-out grid stops at height 6.
  - A corrected values file for the area options is computed with a precision that passes the τ → τ + 1 check at every
    height used. It is committed beside B1932's file with a new seal, and both stay in the record (P-853).
- **The area options' second computation.** agy-002's A2-CANON-T90 or agy-exp's X-MEASURE (whose pre-registration
  treats the cusp in extended precision) must agree with the corrected file under this rule's tolerance.
- **The S* exclusion.** B1922's negative half removes S* from the options: S* does not repeat along a thread. It was
  computed once, so it is PROVISIONAL (P-842). The run waits for its independent second computation (asked of the web
  seat).
- **Two cold reads.** The web seat's cold read of this rule's version 2 and of these amendments.
- **The suite.** The fresh-clone suite on the run's commit is green, or each failure is shown off the value path.
- **The look's own second computation and the third opinion.**
  - The SM seat re-runs both look scripts, and `big_run_windows.py`, on the pinned files, with its expectations
    committed first.
  - If any option passes, agy-002 gives the third opinion (P-339, P-342).
- **The next frames' definitions are frozen now,** so that none is shaped after the look:
  - the order-10 lepton read-out: SM-C13b, as sealed at a036eba44;
  - frame D: card W-B1 as stated in main's message M29 (docs/seats/chat1.md at b9875dc3a), with the five refuters of
    W-F20 (harvest row 1813) as its tests;
  - the amplitude read-out: card A2-AMP;
  - the measure from principle: card X-MEASURE, as pre-registered by agy-exp at 2a67770de.
  - Any definition a seat commits after the look is marked as written after it.

**A8. Rows 11 and 12 (S18).** Frame C gives no value for m_b/m_t or m_τ/m_b.
- Its outputs are ratios within each sector. The matter's normalisation is one factor per sector, and no claimed output
  depends on it (B1938 § 5).
- So the two cross-sector rows stay out because frame C does not compute them, not because of a hold. The hold itself
  was lifted (P-840).

**A9. The record's earlier looks (S19).**
- **Earlier looks.** The record has looked at the same data before: docs/LOOK_LEDGER.md lists 36 sealed decisive cells
  and 32 post-hoc scans before B1753's seal, and the later point-based value looks B1790, B1814, B1825, B1838, B1839 and
  B1841.
- **What the calibration covers.** This run's calibration covers its own four options only. The outcome is read with
  the ledger's count beside it, and the ledger gains this run's row at the look.
- **The earlier tests** are other frames. They are not superseded by this run, and their thread-averaged versions are
  leads after it (P-852).

**A10. The masks (S13).** The check of the agy lane's pushes for a held-out value needs the held-out values, which the
firewall opens only at the look. Rows 11 and 12 are not compared in this run, so their exposure cannot bias it. The
check runs after the look, before anything else is read. The web seat's mask is the seat's own tool; it has stopped
passing value files through it.

**A11. The second computations read so far (S9, S21).**
- **X-CANON.** agy-exp's X-CANON reproduces B1928's truncated-weight read-out of W₋ by the move count: rms z 2.7
  against the sampling errors, worst 0.69 %. It is an independent second computation of B1928, not of this run's
  exact-weight values or of the area options.
- **agy-exp's later pushes,** to 3f30d4a46, are its closing reports and X-MEASURE's pre-registration and verifier. They
  are registered (harvest rows 1816 and 1817).

**A12. X-SURVIVAL's S4 (S17).** agy-exp's claim that a modular-invariant fermion weight prefers W₋ is recomputed on
main's code before the look, or this rule records that it was not. No option is preferred either way.
