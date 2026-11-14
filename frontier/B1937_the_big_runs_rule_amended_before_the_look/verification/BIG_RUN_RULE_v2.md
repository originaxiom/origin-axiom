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
