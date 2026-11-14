# The big run: the rule, fixed before any data is read

*Drafted by main, 2026-11-14 night, for the run the author set for 2026-11-15. Nothing in it is chosen after the values
are seen; every element comes from the record's binding precedent (P-341; B1720's compare.py; B1735).*

## What is compared
- **Frame C's seven rows** (docs/total_inputs_scoreboard.json, frame C):
  - up m₂/m₃ and m₁/m₃, set against c/t and u/t;
  - down m₂/m₃ and m₁/m₃, set against s/b and d/b;
  - ∣V₁₂∣, ∣V₂₃∣ and ∣V₁₃∣, set against ∣V_us∣, ∣V_cb∣ and ∣V_ub∣.

  The pairing of positions with particles is the dictionary's (identification I-26, unearned), stated here once.
- **The values** are in `BIG_RUN_VALUES.json`, committed and pushed before this rule is sealed, with its sha256 in the
  script:
  - frame C as defined, with the exact channel weight (Theorem 90's leading form, checked against the exact horoball
    norm to about 1e-5, at the end where it moved four of the seven values by about 1 %);
  - the canonical end, the horocycle of length 2 (B1927);
  - the read-out on the whole (B1928, proved twice).
- **The four declared options,** all committed with their values: the Higgs world W₋ (the record's practice) or W₊, and
  the measure (a) move count or (b) area.
- **Errors:** (a) jackknife sampling, about 1e-3; (b) the end above Im τ = 6, at most 5.4e-3. Both are far below the
  statistic's 10 % allowance.

## Not compared
- **The leptons:** at level 5 their coupling is the down coupling transposed, so the read-out has no lepton values of
  its own.
- **J's sign:** it needs the hand.
- **Any other frame or option:** anything not in the values file is not part of this run, and cannot be added after it.

## The statistic, the bar, the calibration (P-341, binding)
- **χ²₇** = Σ (ln value − ln measured)² / σ², with σ² = (the measurement's relative error)² + 0.10². B1720's
  compare.py's definition, on the seven rows.
- **The data:**
  - the running masses at M_Z (HZ2021) and the PDG mixing moduli, the files B1720 pinned (sha256 63450365… and
    61ea1565…);
  - the scale is M_Z, as in every earlier sealed look; the frame's values are tree-level ratios (C09, declared).
- **The bar:** χ²₇ < 22.04, the 1 % tail of χ²(7) after the four options (Bonferroni).
- **The calibration:**
  - the fraction of 4 000 random target sets (B1720's law) that the best of the four options fits as well;
  - it must be below 1 %.

## The outcome, fixed now
- **PASS:** the best option is below the bar and the calibration is below 1 %. The passing option is reported with its
  declared inputs named; the inputs stay inputs.
- **FAIL:** otherwise. The four χ²₇, the pulls and the calibration are reported, and nothing is refitted. The negative is
  banked only after its second computation, and its page says what the wall teaches.
- **In either case,** every option's χ²₇ and pulls are reported. No option is chosen after the output is read.

## The order of operations
1. **Tonight (2026-11-14):** the values file, this rule and the script are committed and pushed together. The script
   carries the values' sha256, so the values cannot change without the seal changing visibly.
2. **Before the run:** the second computations of the values (agy-002's A2-CANON, agy-exp's X-CANON) are compared with
   the committed file.
   - If they agree within the errors, the values carry "recomputed independently".
   - If one is not in, the values carry "computed once", and the output says so.
   - If one disagrees beyond the errors, the run waits until the difference is found. Any corrected values file is
     committed beside this one, with a new seal, and both stay in the record.
3. **The run:** `python3 -B big_run_look.py`. Its output is committed before anyone reads it. Then it is read, and banked
   as it reads.
