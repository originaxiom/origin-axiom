# B1937 — The big run's rule amended before the look, and the first second computation of its values

**Verdict: OPEN** (the run has not been made; the area options' second computation is owed). Main, 2026-11-14, after the
web seat's cold read W-F18 of B1932's rule. Register rows P-341, P-845, P-850. **No value is compared with any measured
number here.** 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /big run|precision bar|P-341|coarse cell|second computation of the values|rule amended/: 2 of 1678 arcs on main match (OPEN 1, PROVED 1); 4 register rows match (DONE 4)`.
  The arcs are B1735 (the precision bar) and B1932 (the values and version 1 of the rule).
- **The literature:** the statistic, its bars and its calibration are the record's own precedent (P-341, B1720's
  compare.py, B1735). No outside source is used.

## What the cold read found, and what main did
The web seat's W-F18 (relayed at ded0292cd) traced version 1's seal, statistic and calibration to the record. It found ten
lines to fix before the run. Main took the stricter reading of each:

| W-F18 | the finding | what version 2 does |
|---|---|---|
| O1 | P-341 asks for priors; version 1 states none | priors written, dated, saying they follow the values |
| O2 | P-341's six and nine (with μ/τ, e/τ) are dropped without a stated waiver | reported for every option, with the lepton rows frame C gives (the down rows, B1934); they do not govern, because frame C does not claim them (the scoreboard, 08:40, before the values at 12:46) |
| O3 | B1720's coarse cells are missing | the coarse cell (every claimed row within a factor 3) governs beside χ²₇, both calibrated; a coarse cell met alone is a PATTERN MATCH |
| O4 | step 2's tolerance is not stated | the tolerance fixed in `second_computations.py` before it ran; its limit stated |
| O5 | a PASS has no second-computation condition | any outcome is banked after the look's second computation; a PASS is more than a reading only after the third opinion |
| O6 | W₊ is undefined | W₊ = (up S, down S̃, leptons S̃) |
| O7 | "the passing option" assumes one | every passing option, none preferred |
| O8 | the weight departs from C06 as scored | named in the rule; C06 carries a dated line |
| O9 | the run may go before any second computation | the run waits until every option has one agreeing second computation |
| O10 | the held-out rows are not mentioned | rows 11 and 12 stay held out, neither computed nor opened |

Also from W-F18's minor items:
- **σ's credit:** the moduli's σ is B1735's, not compare.py's.
- **A new check:** version 2 asserts the values file's positions and its four options.

The web seat also disclosed that its mask passed `BIG_RUN_VALUES.json`'s numeric lines, so it saw some values, and that
nothing was computed or quoted from them. The file is public on main, so no second computation is assumed blind.
Version 2 says so.

## The rule and the script
- **The rule:** `verification/BIG_RUN_RULE_v2.md`.
- **The script:** `verification/big_run_look_v2.py`, sha256 `82ed6fa5ee00139c19abf8af22a55e69ec2abb738f6cdb1d6504bc186dde78ab`.
  - It reads B1932's committed values, pinned by their sha256 (df1c9bee…), and the two data files B1720 pinned.
  - It writes `big_run_output_v2.json`.
- **Version 1** (B1932's `big_run_look.py`, sha256 2c5f6774…) stays sealed. It is run beside version 2 and its outcome
  is reported. Version 2 governs.
- **The lock** (`verification/test_b1937_rule_v2.py`, synthetic data only, nine tests), each with a planted case:
  - values equal to the targets pass, and only that option is listed;
  - values a factor 10 off fail;
  - values a factor 2 off are a PATTERN MATCH, not a PASS;
  - lepton rows unlike the down rows fail the reported six and nine and leave the governing outcome a PASS;
  - wrong positions, a missing option and a wrong values hash are refused;
  - the seal stated here is the script's.

## The first second computation: agy-exp's X-EXACT-W, in agreement on the move-count options
- **What was compared.** agy-exp's raw output (committed unread at 48926341b; its expectations at a8c2910b2 and its
  verifier at 685d4f77d) against B1932's file. `verification/second_computations.py` reads the seat's file and prints
  none of its numbers, only differences scaled by the errors.
- **The tolerance,** fixed in the script before it ran: per value, ∣Δ ln∣ ≤ 3 √(e_main² + e_seat² + δ²), with
  δ = 5.4e-3.
- **Results** (`second_computations_run.txt`):
  - **W₋∣a:** every value within the tolerance, the worst at 0.34 of it;
  - **W₊∣a:** every value within the tolerance, the worst at 0.26 of it.
- **What the comparison can tell.**
  - Against the two codes' sampling errors alone, the residual is rms z 2.1 (W₋) and 1.6 (W₊). A systematic of a few
    parts in a thousand separates the codes: of the record's stated size, and a twentieth of the statistic's σ floor.
  - The seat's truncated-weight values sit further away, at rms z 4.9 and 3.4, so the agreement is with the exact
    weight.
  - The tolerance alone would not have rejected the truncated weight: it sits at 0.98 and 0.90 of the tolerance. This is
    stated in the rule.
- **B1934's identity in the seat's read-out:** its lepton ratios equal its down ratios to 3.5e-11, in both worlds.
- **Label:** the move-count options are **recomputed independently (one seat)**.
- **Still owed:** the area options, by agy-002's A2-CANON-T90 (expectations committed at 0e08a8953). Under version 2 the
  run waits for it.

## Scoreboard
Frame C's C06 and its status carry a dated line: the exact weight is used, and why. The status's "NOT sealed … before
any seal" is overtaken by B1932's early seal, and the run waits for the second computations (here).

## Not claimed
- Nothing about any measured value.
- Nothing about whether frame C's values are right. That is the run's question.
- The area options' second computation.
- The lepton rows as a claim of frame C. They are reported because P-341 binds their reporting.
