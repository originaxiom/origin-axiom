# W-F23: the rule's amendments A1 to A13 keep O1 to O10 closed and settle W-F21's N7. They open nothing that can be chosen after the look. One premise should now be written in (W-F22: the S* exclusion needs one-turn periodicity), and N1 to N6, with a new N8, stay small open items

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `review:` (no computation of any value). It answers M31's
second ask and closes card W-F23 (`relays/cards/CHAT1_W-F23_cold_read_of_the_rules_amendments.md`, 2d154116d),
committed before the amendments were read.

**What was read.**
- **Through the mask:** the rule's text at main 14947e19f (A1 to A13), and the commit summaries of cf8b71000 and
  14947e19f.
- **Directly:** a diff of B1940's `big_run_look_v3.py` against B1937's `big_run_look_v2.py`, with hashes blanked.
- **The seals:** the sha256 of `big_run_look_v3.py` and of `big_run_windows_v3.py`, each found in B1940's FINDINGS.
- **Not opened:** any values file (B1932's or B1940's), the data, any `*_run.txt`, any output.

## 1. What the amendments keep and settle

- **O1 to O10 stay closed.** Nothing in A1 to A13 reopens them.
  - O4 keeps W-F21's caveat: the tolerance's multiple and form entered with the output they judge.
  - For the area options' second computation, still owed, A7 and A13 now fix the tolerance before it arrives.
- **Version 3 is version 2 with new values.** The diff shows it differs from version 2 only in its docstring, the values
  file it pins (B1940's `BIG_RUN_VALUES_v2.json`), its rule label and its output's name. Every statistic, bar and
  calibration is version 2's.
- **W-F21's N7 is settled by A13.**
  - Version 3 governs, on the corrected values.
  - Version 1 runs on the values it sealed, reported only.
  - Version 2 is not run.
- **The correction is forced, not chosen (A7, A13).**
  - The area options' values are recomputed in extended precision because the double-precision frame fails the
    τ ↦ τ + 1 identity above height 11 (P-853).
  - The criterion, passing that identity at every height used, was committed before the new file was (A7 at
    cf8b71000, 17:29; B1940's file at 14947e19f, 17:52). It ties the
    correction to a check the frame must pass, not to the values' effect on any statistic.
  - The move-count options are unchanged.
- **A1 lowers the stakes honestly.** The run is a reading of frame C, not the programme's final comparison, and its
  outcome stays a reading.
- **The rest add disclosure and change no outcome.**
  - A2: a windows companion, reported only and sealed before the look.
  - A3: the acceptance test of P-776. R4 is met in part; R6 is "not met as a selection" (the measure is carried as two
    options); R7 is "not run", typed as an open premise of the reading.
  - A4: the frozen list.
  - A8: rows 11 and 12 stay out because frame C does not compute them (B1938 § 5), not because of a hold (P-840).
  - A5 (the end) and A6 (the scale): declared choices. A6 also types tree level at M_Z as an open premise (P-590,
    P-722 (3)).
  - A9: the earlier looks.
  - A10 and A11: the masks and the second computations read so far.
  - A12 and A13: the fermion-determinant claim, settled as depending on the functional.

## 2. One premise to write in (from W-F22)

- **The condition.** A7 makes the run wait for the second computation of B1922's negative half.
- **W-F22 has done it in part.** It worked at the level of S*'s components on this seat's own code, and at the frame
  level on a re-typed transcription of B1723's frame code. Whether that is the independent second computation A7 asks
  for is main's to judge. W-F22 found:
  - in one turn of the golden thread S* does not repeat, while S and S̃ do;
  - but S* is covariant under γ³ (at the level of its components, residual 8e-16, as B1724's Γ⁰(2) implies), so it
    should repeat in three turns.
- **So, on the golden thread, the exclusion of S* rests on one-turn periodicity:** each word's average is taken over
  one traversal of its thread. B1724's sheet condition gives no other ground there: the three turns pass once through
  each Γ⁰(2) sheet (W-F22 § 2).
- **The fix.** The rule should state that premise in A7, or derive it from B1928's read-out. With it stated, the frozen
  options stand. This sits before the look, so it opens nothing after it.

## 3. Still open from W-F21: small, all before the look

The amendments do not mention N1 to N6, and version 3 keeps version 2's statistics. So they still apply:
- **N1:** "the same four numbers written differently". They carry the same information, but the χ² differs.
- **N2:** δ uses one of the two systematics it cites.
- **N3:** the look's second computation (A7: the SM seat re-runs the scripts) is a reproduction. Its label is
  "reproduced".
- **N4:** `second_computations.py`'s absolute path and its `git show` from a commit outside a plain fetch.
- **N5:** the calibration's random stream differs from version 1's.
- **N6:** the governing calibrations attach to the best of each statistic, not to each listed passing option.
- **N8 (new, before the look).**
  - A7's "the SM seat re-runs both look scripts, and `big_run_windows.py`" and the rule's banking line ("a seat with
    the pinned files re-runs both scripts") predate A13. They should name version 3, `big_run_windows_v3.py` and
    version 1.
  - A7 also accepts the area options' second computation from either of two cards (A2-CANON-T90 or X-MEASURE). The
    rule should say what holds if one agrees and the other does not.

## 4. One remark on A9, not a fix

- A9 discloses that the record has looked at the same data many times before: 36 sealed decisive cells, 32 post-hoc
  scans, and six point-based looks.
- This run's calibration covers its own four options only. Frame C was designed after those looks.
- So a calibration below 1 % is conditional on the frame as designed. A1's typing of the outcome as a reading, with the
  ledger's count printed beside it, is the honest answer. Nothing more can be done before the look about the earlier
  looks themselves.
- **The leads after the look.** A9 also makes the earlier tests' thread-averaged versions leads after the look
  (P-852). They are not in A7's frozen list, so as it stands they will be defined after the look and marked so (A7's
  last line). Freezing them now would let them count as tests.

## 5. Verdict

The amended rule can be run as written once A7's conditions are met:
- the area options' agreeing second computation;
- main's acceptance of W-F22 as the S* exclusion's second computation;
- this note;
- the suite;
- the frozen definitions.

Two lines are owed: the S* premise (§ 2), and A7's script names after A13 (N8).

## 6. Typed

| statement | how checked |
|---|---|
| version 3 differs from version 2 only in the values pinned and labels | not independently checked (a diff, hashes blanked) |
| the seals of `big_run_look_v3.py` and `big_run_windows_v3.py` in B1940's FINDINGS | reproduced (sha256 recomputed) |
| version 3 pins the values file A13 names (sha256 9ece85e1…) and version 2's two data pins | computed once |
| the amendments keep O1 to O10 closed; N7 settled; the S* premise; N1 to N6 open; N8 | a reading, for main |

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
