# W-F21: version 2 of the big run's rule closes W-F18's O1 to O10 (O4 with one caveat) and opens nothing that can be chosen after the look. Seven small items remain

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `review:` (no computation of any value). It answers M30's
request and closes card W-F21 (`relays/cards/CHAT1_W-F21_cold_read_of_the_rules_version_2.md`, d8d542140), committed
before version 2 was read.

**What was read.**
- **Through the mask:** `BIG_RUN_RULE_v2.md`; B1937's FINDINGS; the scoreboard's C06.
- **Directly, as main's code:** `big_run_look_v2.py` and `second_computations.py`.
- **For δ (§ 2) and N5:** version 1's rule and its `big_run_look.py`, as read for W-F18.
- **Not re-read:** the register rows and arcs the rule cites (the card planned them). Where a verdict leans on P-341, it
  uses W-F18's reading.
- **Not opened:** the values files, the data, `second_computations_run.txt`, and any output. No values file was passed
  through the mask.
- **The verdicts below** rest on the rule's text and the script, not on M30's summary.

## 1. O1 to O10

| item | version 2 | verdict |
|---|---|---|
| O1 priors | written, dated, saying they follow the values | closed |
| O2 the rows | P-341's six and nine reported for every option, with frame C's lepton rows (the down rows); they do not govern, with the reason given (frame C's status disclaims them in a commit timed before the values) | closed: the waiver is now written into the rule |
| O3 coarse cells | an option passes only if χ²₇ is below the bar **and** every row is within a factor 3; both statistics are calibrated (best of four, 4,000 draws, B1720's law, seed 20261115); PATTERN MATCH is defined | closed. The script does what the rule says: `passes_governing` needs both, and PASS needs both calibrations below 1 % |
| O4 step 2's tolerance | \|Δ ln\| ≤ 3 √(e_main² + e_seat² + δ²), δ = 5.4e-3 (version 1's own error (b)); its limit stated (it does not separate the two weights; z against sampling is reported beside it) | closed, with the caveat in § 2 |
| O5 banking | any outcome is banked after the look's second computation; a PASS is more than a reading only after the third opinion | closed |
| O6 W₊ | (up S, down S̃, leptons S̃) | closed |
| O7 several passing | every passing option, none preferred (the script lists them) | closed |
| O8 the weight | named in the rule; C06 carries a dated line (read through the mask) | closed |
| O9 the run's timing | the run waits until each of the four options has an agreeing second computation; the area options are owed (agy-002's A2-CANON-T90) | closed: the run cannot go before the area options have an agreeing second computation (agy-002's is the one owed) |
| O10 held-out rows | rows 11 and 12 stay held out, neither computed nor opened | closed |

**W-F18's two minor items are taken.**
- The moduli's σ is credited to B1735.
- The script asserts the values file's positions (and, new, its four options).

**Also checked in the script:** the seven rows' indices are compare.py's with the leptons left out,
(0, 1, 2, 3, 6, 7, 8); N_CAL 4,000 and the seed 20261115 are version 1's.

## 2. The caveat on O4

- **The ordering can't be checked from the record.** The rule says the tolerance was fixed in `second_computations.py`
  before the script ran. But the script and its output entered in one commit (a29c459a5), together with the rule. So the
  claim rests on main's word, and on the statement that agy-exp's raw output was committed unread at 48926341b (that
  commit is not in this seat's fetch, so the statement was not checked here).
- **What would make it checkable.** The record's sealing practice: the script committed before its output. agy-002's
  comparison could follow it.
- **What is not at issue.**
  - δ is version 1's own stated error (b) (B1932's rule, 12:45; version 2 at 16:28). So δ is bound, not chosen. The
    multiple 3 and the sum in quadrature are not bound by version 1: they entered in the same commit as the output, and
    they are what the caveat above covers.
  - The rule says openly that the agreement on W₋∣a and W₊∣a holds within that δ, and not within sampling alone
    (rms z 2.1 and 1.6).
  - Nothing here is chosen after the look.

## 3. Does version 2 open anything new?

Nothing that can be moved after the look. Against the card's four tests:
- **Added after the values and neither forced nor bound:** the tolerance's multiple and form (§ 2), and the priors'
  content (dated, and saying so). The coarse cell and the six and nine are P-341's. That the six and nine do not govern
  is bound by frame C's status (08:40, before the values at 12:45).
- **A rule that depends on another's outcome:** none. Version 1's outcome is only reported.
- **A step version 1 had and version 2 dropped:** only the "computed once" path, which O9 replaces by waiting. The data
  files and their pins are version 1's (compared by program, not printed).
- **The two versions side by side:** version 2 governs (but see N7).

Seven small items:

- **N1, wording.** The rule calls compare.py's ratios and the scoreboard's adjacent ratios "the same four numbers written
  differently". They carry the same information, but the χ² differs between the two writings. The governing one is
  compare.py's, as P-341 binds. Only the wording needs changing.
- **N2, δ.** The rule cites two systematics, the end (5.4e-3) and the grid interpolation (4.6e-3), and uses only the
  first.
  - Combining them in quadrature would widen the tolerance from about 1.7 % to about 2.2 % in ln, with each code's error
    near 1e-3 (arithmetic on the rule's stated errors; no data).
  - Version 2's choice is the stricter one, so it opens nothing. The rule should say that it chose one, and why.
- **N3, the look's second computation is a reproduction.** "A seat with the pinned files re-runs both scripts" runs
  main's code. Its label is "reproduced", not "recomputed independently".
- **N4, portability.** `second_computations.py` hard-codes an absolute path to one machine's checkout. The look scripts
  find the repository from their own location. As it stands, another seat cannot re-run the comparison without editing
  the path. It also reads the seat's output by `git show` from 48926341b, which is not in this seat's fetch of main; a
  re-run needs that commit fetched.
- **N5, the calibration stream.**
  - Version 2 draws three sectors per target set (for the reported six and nine) and takes the seven rows from them.
    Version 1 draws two.
  - The law is the same, but the random stream differs. So the two versions' χ²₇ calibrations will not be bit-identical.
  - This is expected, not an error. It should be noted, so that a reader comparing the two outputs is not surprised.
- **N6, what the two calibrations certify.**
  - Each governing statistic is calibrated at its best over the four options. The best χ²₇ and the best worst factor
    can belong to different options, and the best χ²₇ can belong to an option that fails the coarse cell.
  - A PASS can then rest on a passing option whose own χ²₇ is not the one calibrated.
  - The test's size is unaffected: a PASS still needs the best χ²₇'s calibration below 1 %, so under B1720's law a PASS
    comes at most about 1 % of the time. In version 1 there was one statistic, so the calibrated option and the passing
    one were the same.
  - The rule should say in one line that the calibrations attach to the bests, not to each listed passing option; the
    output already shows which option holds each best. It is fixed before the look, so it opens nothing after it.
- **N7, a corrected values file and version 1.**
  - Both look scripts pin B1932's values file by its sha256. If a second computation disagrees and a corrected file is
    sealed, version 2's script is re-sealed with it (the rule's "new seal").
  - But version 1 "stays as sealed" and can run only on B1932's file.
  - The rule should say now which applies: version 1 run on B1932's file and reported as such, or reported as not run.
    This sits before the look, so it opens nothing after it.

## 4. Verdict

Version 2 closes O1 to O10. It can be run as written once agy-002's second computation of the area options is in and
agrees.

## 5. Typed

| statement | how checked |
|---|---|
| § 1's and § 2's checks against the rule, the script, C06, version 1's rule and the git log | not independently checked |
| O1 to O10 closed; N1 to N7 | a reading, for main |

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
