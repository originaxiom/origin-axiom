# W145 — the third opinion on main's B1741 (P-348): the re-run, the χ² calibration on own code, the apex points and the lines on own code, the best rows on own instrument, the line and the lepton–down relation at the best row, and the sensitivity (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **Main's B1741** (sealed acd2fec77; read out at S201, a74c9cd6f) put τ at each of the 75 apex points of B1720's
  thread classes, with no continuous number fitted, and the line free over all 266.
  - The six are reached at value level: χ²_six 14.93, below 16.75, with 0.60% of random hierarchies as low under the
    seat's menu.
  - The best row is the apex 3.4 + 2.993i of L⁵R²LR and L²R⁵LR, on the line (2/5, 9/10), L_max, (S̃, S, S), c = 3.
  - Main grades it a READING, not passed under THE_BAR's look correction (1.2–3.6%). Its hostile referee estimates
    the true p at about 1–7%, with 0.60% a lower bound.
- **The owner's rule of 2026-08-21:** a positive value match is not banked as more than a reading without a third
  opinion. Main's P-348 asks the seats to:
  - re-run compare.py on census.jsonl;
  - recompute the best row on their own instrument;
  - check the 75 apex points and the line count;
  - apply THE_BAR's correction their own way.
- **The owner said "start it"** (2026-10-24) to this as the next step.

## The objects

- **Main's committed files at a60430b46**, read with `git show`:
  - B1741's PREREGISTRATION, census.py, compare.py, census.jsonl, control.json, comparison.json and FINDINGS;
  - the files its ARTIFACT_HASHES pins (B1726's census.py and census.jsonl, B1720's the_thread_census.json, b1656_funcs
    and its dependencies, the two data files).
- **The pins:** census.jsonl sha256 8fadff8b…388d (19 950 lines) and comparison.json 6217857…e248, as fetched for this
  rule; the rest as ARTIFACT_HASHES states.
- **The own code:**
  - W142's direct-sum χ² (`configs`, `direct_min`), σ from the pinned files, and its nine;
  - W138's draws (`own_draws`), census loader and own instrument (`own_point`: W93's residues × κ, W89's norms, the
    Higgs ∂R from direct theta sums, so no principal nome root enters at Re τ = 3.4);
  - W141's Smith rule and fixed lines;
  - W140's 266 lines.
  The script imports nothing of B1741's or B1726's code, except main's compare.py, which A1 runs in a temporary tree.
- **The best rows:** the best six-row; the next four by χ²_six under the seat's menu, as the own calibration ranks
  them; and the best nine-row under the seat's menu.

## Weave or thread

**A check of main's census over every thread class's apex.** The input set spans the threads, but the positive sits
at one thread pair's point: **a thread result.** The claims are about main's code, census and statements.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| A0 | **The inputs.** census.jsonl and comparison.json match the pins above; census.jsonl has 19 950 distinct (line, Re τ, Im τ); every file ARTIFACT_HASHES pins matches | 95% |
| A1 | **The re-run.** Main's compare.py, run once in a temporary tree at a60430b46, exits 0 and reproduces comparison.json: every cell identical, every per-seed fraction exact, every minimum to 10⁻¹² relative | 90% |
| A2 | **The χ² calibration on own code** (direct sums; the seat, covariant and free menus; seeds 1741–1760, 4 000 targets each; own draws). Every per-seed fraction equals comparison.json's exactly, the minima agree to 10⁻¹⁰ relative at the same row, and χ²_nine is 204 (seat) and 1 410 (the Standard Model's reading), to 10⁻⁶ relative of comparison.json's | 85% |
| A3 | **The apex points on own code.** Each of B1720's 121 stored class words gives a matrix A whose apex ((a − d)/2c, √(t² − 4)/2∣c∣) equals the stored τ to 10⁻⁹, up to an integer translate in Re τ (a read-out). The 121 give exactly 75 distinct points, and they are census.jsonl's 75 | 85% |
| A4 | **The lines.** W140's 266 lines up to sign equal, as a set, the 266 that B1726's lines() lists (in A1's tree), and census.jsonl's line indices are 0–265 at every apex | 90% |
| B0 | **The own instrument's controls at the best six-row.** Residues match the re-implemented bilinear to 10⁻¹⁰ relative, and W96's J1 holds to 10⁻¹⁰‖Y‖³. B1724's law on own code: (3.4 + 2.993i, (2/5, 9/10)) equals (0.4 + 2.993i, (2/5, 1/10)) to 10⁻⁸ in log | 80% |
| B1 | **The six rows on the own instrument.** Every stored ratio and ∣V∣ above 10⁻¹⁰ is reproduced to 10⁻⁶ in log, and J to 10⁻⁵ relative where ∣J∣ > 10⁻¹⁰ | 75% |
| B2 | **The best six-row from own values:** χ²_six 14.932 to 10⁻⁴ relative, the six pulls to 10⁻³, and D = 11.047 to 10⁻⁴ relative | 75% |
| C1 | **The line.** Line 153 at Re τ 3.4 is (2/5, 9/10) and maps by b → b + 3α to (2/5, 1/10), B1726's line 149 (B1735's line). It is not fixed up to sign by A of L⁵R²LR or of L²R⁵LR (the Smith rule on own code). tr A = 30, A² ≡ −I mod 10, and A² fixes all 12 lines of order 5 and all 36 of order 10 | 90% |
| C2 | **The lepton–down relation at the best six-row.** The lepton ratios (reading S) differ from the down ratios (reading S): the row is not a Georgi–Jarlskog copy, D/9 = 1.227, and the six there are six numbers, not four (P-355). A read-out, no prediction: on how many of the 266 lines, at each apex, the lepton ratios equal the down ratios to 10⁻⁸ for every reading | 95% |
| D1 | **Sensitivity** (labelled; the seat's menu; seeds 1741–1760). At allowance 0.05 the minimum χ²_six rises above 16.75 (by hand about 43 at the best row). With the lepton factor over {1, 2, 3, 4, 5} the fraction rises above 1%, where main's referee gave 1.0–1.1% on two seeds. With a uniform σ of 0.10 the minimum is 19.61, above the bar, and the fraction at most 1% | 75% |

## The look count (stated now, by hand from the record)

- **Inside B1741:**
  - six sealed specificity looks give 0.60% × 6 = 3.6%;
  - eleven fractions computed give 6.6%.
- **The apex rule's tests:** B1720, B1734 and B1741, so × 3 = 1.8%.
- **Both together:** 6 × 3 = 18 looks, 10.8%.
- **The post-selection, not countable as looks.** The tested point is B1735's fitted line at the apex height nearest
  the fitted optimum, and main estimated χ² 10–20 there by eye before the seal. The lepton factor 3 and the reading
  were chosen from the data. This seat counts the result as **a reading whose specificity is at best marginal**,
  whatever the arithmetic count.

## What the outcomes mean (fixed now)

- **A1, A2 and B1 hold.** B1741's χ² minimum and calibration are reproduced by main's own code and by a second code,
  and its best row by a second instrument. 14.93 and 0.60% stand as computed.
- **A3 and A4 hold.** τ is placed by the thread rule as stated, and the line is one of the stated 266.
- **C1 holds.** The line is B1735's own, and the thread supplies no rule for it.
- **C2 holds.** At this row the six are genuinely six numbers. The match is not P-355's four-number lines in disguise.
- **D1 holds.** The match needs the 10% allowance, where B1735's survived 5%. The integer lepton factor's menu blunts
  its specificity.
- **This seat's opinion (fixed now).** If A1, A2 and B1 hold, B1741 is a value-level READING. It is the first sealed
  six at the precision bar with no continuous number fitted, but:
  - τ is placed by a rule at a post-selected point, and the line is chosen from 266, being B1735's fitted line;
  - both ingredients are by hand;
  - the match needs the 10% allowance (if D1 holds);
  - the nine fail, with ∣V_ud∣ 0.12.
  It can be banked as that and no more. It is not a derivation.
- **Any cell fails:** the failure is the finding, and it is diagnosed before anything else is said.

## What stays out

- B1741's nine and its J beyond A2's minima; the web seat's reading test (P-360); P-357 (W146, next); the frame
  itself.

## Seen before the rule (disclosed)

- **Read on main:**
  - B1741's PREREGISTRATION, FINDINGS (including its referee's section), census.py and compare.py;
  - compare_run.txt's last five lines (the ∣V_ud∣ table and the best six);
  - ARTIFACT_HASHES;
  - the commit messages from S201 to S210;
  - P-352 to P-360 in POINT_REGISTER.
- **Not read:** no value of census.jsonl or comparison.json beyond what FINDINGS and those five lines print. Their
  sha256 was computed from `git show` output.
- **By hand:**
  - the row's χ² 14.93 from FINDINGS' ratios and W142's σ;
  - the estimate of about 43 at allowance 0.05;
  - D/9 = 1.227;
  - b → b + 3α (9/10 + 6/5 ≡ 1/10);
  - the look counts.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed part is a failed launch of that part: kept, disclosed, fixed, and only that part relaunched.
- Any later check is labelled post hoc.

0 of 19.
