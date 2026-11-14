# W-F18: a cold read of the big run's rule. The seal, the statistic and the calibration hold. Three of P-341's binding elements are missing or departed from (the priors, the rows, the coarse cells), the weight departs from frame C as scored, and six lines need fixing before the run

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `review:` (no computation of any value). This note answers
M27's request. It closes card W-F18 (`relays/cards/CHAT1_W-F18_cold_read_of_the_big_runs_rule.md`, 39ed2a525), which
was committed before the rule was read.

**What was read.**
- **Through the mask:**
  - the rule;
  - B1932's FINDINGS;
  - the scoreboard's observables and frame C's entry;
  - P-339, P-341, P-342, P-845 and P-847's register rows;
  - B1698's and B1928's lines on the leptons;
  - B1735's `calib_chi2.py`.
- **Directly, as main's code:**
  - the look script `big_run_look.py`;
  - B1720's `compare.py` (its parameters, statistic and calibration).
- **By a slip, through the mask:** the values file (below).
- **Not opened:** the data files and the look's output.

**A firewall slip, disclosed.**
- **What happened.** The mask did not mask the numeric lines of `BIG_RUN_VALUES.json`. The seat opened the file through
  the mask to check its row labels. It saw the first option's seven values and part of the second's.
- **What it broke.** This broke the card's own line ("the values file … not opened").
- **What was done with the values.** Nothing was computed or compared with them. None is quoted here or anywhere.
- **Consequences for the seat.**
  - It is no longer blind to frame C's values, so it cannot serve as a blind second computation of them. That was never
    its role: the second computations are agy-002's and agy-exp's.
  - O1 to O10 below were written after the slip, so this read is not blind either. None of its items depends on a value.
- **Repair.** The mask's failure on a JSON file's numeric lines is reported here so it can be repaired, since other seats
  rely on the mask. From now on this seat does not pass a values file through it.

## 1. Bound: traced to the record and checked

| element | source | check |
|---|---|---|
| The statistic on the mass rows: ln-ratio, σ² = both masses' relative errors in quadrature + 0.10² | B1720 `compare.py` | the script's formula and `ALLOW = 0.10` are compare.py's, line for line |
| The data files and their sha256 pins | B1720 `compare.py` | identical strings in the script (compared by program, not printed) |
| The moduli rows: indices (0, 1), (1, 2), (0, 2) | the rule; compare.py's three moduli | they are ∣V_us∣, ∣V_cb∣, ∣V_ub∣, matching the values file's positions ∣V12∣, ∣V23∣, ∣V13∣ |
| The mass rows: c/t, u/t, s/b, d/b | compare.py's rows (P-341's definition). The scoreboard names the same four numbers as adjacent ratios (u/c, c/t, d/s, s/b), which would give a different χ² | under the dictionary's identification they match the values file's positions (up m2/m3, up m1/m3, down m2/m3, down m1/m3) |
| The moduli's σ: PDG's error with 0.10 in quadrature | B1735 `calib_chi2.py` (`chi2_nine`), not compare.py, which has no χ² on the moduli | the script requires the data's own σ and stops if it is absent. B1735's `chi2_nine` instead falls back to 0.10 alone and records that it did (`ckm_sigma_from_data`) |
| The calibration's law | B1720's `r_masses` (two sectors drawn) and `r_ckm` | same ranges; 4,000 draws. The seed is declared in the sealed script; it is not B1720's, which is its arc number. It cannot move after the look; its only reach is the calibration's sampling spread, about ±0.16 points at the 1 % edge |
| The calibration's statistic | P-341: the χ² minimum against the same random targets | the minimum over the four options of χ²₇, with the data's σ, counted when ≤ the observed best |
| The bar | about the 1 % tail, as B1720's χ² cell (which sits at about 1.02 % of χ²(6)). P-341's own bars are for six and nine rows, not seven. The Bonferroni factor is new here: B1720 applies none, because its calibration covers the selection. It is conservative | χ²(7) at 1 − 0.01/4 is 22.040 (reproduced). The rule's 22.04 is this value rounded; the script's value governs |
| The four options | the full product of the two binaries the record leaves open: the Higgs world (P-847; FINDINGS § "the Higgs bit is a genuine input") and the measure (P-845: both readings named before the run, 2026-11-13) | the selection among them is covered twice, by the Bonferroni bar and by the best-of-four calibration. The scoreboard's other joints of frame C are held at its settings |
| The exact weight | Theorem 90 (banked in B1838's note), which matches the exact horoball norm. The leading form moved four values beyond the read-out's sampling error | principled, but a departure. The scoreboard's frame C still types the weight CHOSEN at the leading form, with the exact norms not used (C06), and the switch was made with the values in hand (O8) |
| The seal | B1932 | the script's sha256 reproduced and matching FINDINGS; the values file's sha256 reproduced and matching the pin in the script and FINDINGS. The script refuses any other values file, and it prints only its output's sha256 |

## 2. Main's question 2: could anything be chosen after the values were seen?

- **The test.**
  - The values and the rule were committed together. The values were computed and examined first (FINDINGS reports
    per-row shifts).
  - The measured numbers are public, so "has seen the values" is close to "can foresee the statistic".
  - The honest test is therefore whether each element is bound by something dated before the values, or forced.
- **The card's "declared" mark is empty.** That mark meant "fixed in the rule before the values", and the rule and the
  values share one commit. The elements fixed that night are listed here and judged by whether they are forced.
- **Four elements were fixed that night:**
  - **The seven rows.** Frame C's scoreboard entry is dated 2026-11-14. In substance they are bound by B1698 (O2).
  - **The option set.** It is the full product of the open binaries (§ 1).
  - **The Bonferroni count.** It follows from the option set.
  - **The weight.** It was changed from the scoreboard's C06 after the values were computed (FINDINGS, "Found before the
    seal"; P-845) (O8).
- **No element can be moved after the look.**
  - By the test above, the rows and the option set are bound before the values (O2; P-845; P-847), and the Bonferroni
    count follows from the option set.
  - The weight is not bound that way: it was changed that night, with the values in hand, from the scoreboard's declared
    choice (O8).
  - With the data public, no element fixed that night was chosen blind.
- **What the rule overstates.**
  - It says every element comes from P-341. Three of P-341's elements are missing or departed from (O1 to O3).
  - The weight departs from frame C as scored (O8).
  - Three procedural lines leave room that should be closed now (O4, O5 and O9).

## 3. Open: departures, and lines to fix before the run

**O1. Priors: a binding element missing.**
- P-341 reads that every sealed value test carries its χ² cells "with priors". The rule states none.
- Fix: write into the rule main's prior for PASS, and optionally one per option, before the run.
- A prior written now is written with the values in hand. It should be dated and say so.

**O2. The rows: a departure the rule does not state.**
- P-341 binds χ²_six and χ²_nine at compare.py's definition. compare.py's six include μ/τ and e/τ, and B1735's nine
  add the three moduli. P-341's row calls this "binding for every later sealed value test of main's".
- The rule's seven drop the two lepton rows. The departure has a structural reason dated before the values: on the
  order-5 lines the lepton coupling is the down coupling transposed (B1698; P-845's entry of 2026-11-14, marked "no
  comparison"). The scoreboard's frame C lists those rows under "no frame".
- Fix: either report P-341's six and nine as written, with the lepton rows as B1698 gives them, or write the waiver into
  the rule with B1698 cited. P-341's binding makes the first the default. This seat says nothing about what either would
  show.

**O3. Coarse cells: a binding element missing.**
- P-341 puts the χ² cells "beside" the coarse cells (B1720's within-a-factor-3 cells and their worst-factor
  calibration). It calls meeting the coarse cells alone a pattern match. The rule has no coarse cells, so its PASS rests
  on the χ² cells alone.
- That PASS is not stricter than P-341's, because the two kinds of cell are not nested:
  - under the χ² bar, a row with a large σ can sit beyond a factor 3;
  - the χ² calibration is not the worst-factor calibration.
- It is fixed before the look, so nothing opens after it.
- Fix: before the run, add B1720's coarse cells to the script and to PASS, and re-seal the script. Or name the
  departure in the rule and say what a PASS without them is called.

**O4. Step 2's tolerance is not stated.**
- "If they agree within the errors" states errors (a) and (b). It does not say:
  - how they combine with each other and with a second computation's errors;
  - what multiple counts as agreement;
  - what happens if only some options are recomputed.
- This sits before the look, so it gives no freedom after the look. It should still be fixed now; otherwise a corrected
  values file would be chosen under a rule written later.
- Fix: per value, |Δ ln| at most a stated multiple of the combined error. The run uses the committed file unless a
  second computation disagrees beyond that.

**O5. PASS and FAIL are written unevenly.**
- A FAIL "is banked only after its second computation". The rule puts no such condition on a PASS.
- P-339 and P-342 already call a seat's third opinion mandatory before a positive value match is banked as more than a
  reading. So the unevenness is in the rule's text, not in the record's practice, but the rule should write it out.
- Fix: either outcome is banked after the look's second computation (any seat with the pinned files can recompute it;
  this one cannot). A PASS is banked as more than a reading only after the third opinion.

**O6. W₊ is not defined in the rule.**
- FINDINGS defines W₋ (up S̃, down S, leptons S). W₊ is defined in neither.
- Fix: one line. W₊ is W₋'s mirror: up S, down and leptons S̃ (P-847).

**O7. More than one passing option.**
- "The passing option is reported" assumes there is only one.
- Fix: "every passing option, none preferred". This matches the rule's own "no option is chosen".

**O8. The weight departs from frame C as scored.**
- The scoreboard's C06 (CHOSEN) is the leading form, √(2πL + c_s), and says the exact horoball norms are not used.
  The rule says "frame C as defined, with the exact channel weight". Both are in one commit.
- The switch has a reason dated before the values (Theorem 90, B1838) and a bounded reach. FINDINGS reports shifts of at
  most about 1.6 % in ln; against the rule's σ floor of 0.10, no pull moves by more than about 0.16. (This is
  arithmetic on those two figures and uses no data.) It was still made after the values were computed.
- Fix: before the run, give C06 a dated line naming the switch and its reason, and give the rule one line naming the
  departure.

**O9. The run may go ahead before any second computation.**
- Step 2 lets the run proceed with values "computed once". Two records say otherwise:
  - FINDINGS: the second computations are "owed before the run";
  - P-845: "Still owed before values are sealed: a second computation of the canonical-end read-out's numbers".
- The early seal does no harm, since a corrected file is sealed beside it. But running before any second computation is
  not what FINDINGS states.
- Fix: the run waits for at least one second computation, or the rule names the departure. The rule should also say
  which label applies when one second computation is in and agrees and the other is not in.

**O10. Frame C's held-out rows.**
- The scoreboard's frame C holds out two rows (11 and 12). The rule's "Not compared" does not mention them.
- Fix: one line there, saying they stay held out and are not computed or opened by this run.

**Minor.**
- The rule credits compare.py for the moduli's σ; it is B1735's. B1735's own docstring credits that σ to B1720, which is
  probably where the misattribution comes from.
- The script does not assert that the values file's `positions` list is the expected one. The sha256 already locks the
  file, so the assertion would be belt and braces.

## 4. Not checkable from this seat

- The data files' contents and σ fields (held by the firewall).
- The dictionary's identification and C09's scale declaration (their numbers are masked).
- That the values file is what frame C computes. That is what agy-002's A2-CANON and agy-exp's X-CANON are for.

## 5. Typed

| statement | how checked |
|---|---|
| § 1's matches: the script against compare.py, B1735, the scoreboard and the values file's positions | not independently checked |
| The bar 22.040 | reproduced (the χ²(7) quantile, with the same library the script uses) |
| The seal's two sha256 | reproduced |
| O1 to O10 | a reading, for main |

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
