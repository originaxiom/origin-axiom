# W138 — the third opinion on main's B1726 (P-304): the re-run, the calibration on own code, the rows on own code, R7's mechanism, and the looks (the rule, committed before the script runs)

The SM-derivation seat, 2026-10-23. Committed and pushed before the script runs. Nothing here is a result.

## Why

- **Main's B1726** held as sealed: the six charged-fermion ratios come within 1.20 on 23 940 fresh points, and
  0.12% of random hierarchies do as well under the seat's menu. Main graded it a READING with two hand-put
  ingredients: the lepton factor 3 and the reading rule.
- **The owner's rule of 2026-08-21:** a positive value match is not banked as more than a reading without a third
  opinion.
- **Main's P-304 asks the seats for four things:**
  - re-run compare.py on the committed census;
  - recompute a sample of rows, the two best among them, on their own instruments;
  - re-derive R7's mechanism;
  - look for any uncounted look, and any asymmetry between the data and the random targets.
- **The owner approved this seat's doing it (2026-10-23).**

## The objects

- **Main's committed files at 1059939cc**, read with `git show`:
  - census.jsonl, sha256 d67432f0…. ARTIFACT_HASHES.txt has no line for it; the sha256 is pinned only in B1726's
    lock test.
  - compare.py and census.py, pinned in ARTIFACT_HASHES.txt.
  - comparison.json, control.json and compare_run.txt.
  - the two target files, pinned: HZ2021 at M_Z and B1612's CKM moduli.
- **The own instrument**, this seat's code: W93's units, dual basis, coupling and closed-form residues; W89's kernel
  norms, called with 12 theta terms; W96's joint law J1 as a check on every coupling.
  - Written fresh: the Higgs DR from direct theta sums; the scale κ = F_A·F_D/θ₁′(0) between W93's residues and
    main's; the line list.
  - It imports nothing of main's census.py, b1656_funcs.py, the_exponents.py or qseries.py. L comes from main's
    B1667 column, an input shared with main.
- **The sample, 38 points:**
  - the two best points of B1726's FINDINGS, (2/5, 1/2) at 0.55 + 3.05i and (2/5, 1/10) at 0.55 + 2.55i;
  - 30 points drawn by `random.Random(304)`;
  - 6 order-5 points drawn by `random.Random(3045)`.
- **D_frame** = (m_μ·m_d)/(m_s·m_e) from the frame's ratios at c = 1. compare.py's D is c²·D_frame.

## Weave or thread

**Neither, strictly: a check of main's census of one frame** (B1656's coupling on the shared fibre). The census
takes every flat line of order ≤ 12 under B1713's rule, with none hand-picked, and τ on a grid. The claims are about
main's code and stored numbers.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| A0 | **The inputs.** compare.py and census.py match ARTIFACT_HASHES.txt, census.jsonl matches the lock test's sha256, and both target files match their pins. The census holds 23 940 unique points with no NaN or infinity | 95% |
| A1 | **The re-run.** Main's compare.py runs once on the committed census in a temporary tree and exits 0. All 120 per-seed fractions and the six means equal the committed comparison.json exactly. Every other number agrees to 10⁻¹² relative, and the cell booleans are the same | 90% |
| A2 | **The calibration on own code** (the same priors, generator and seeds; compare.py not imported). The same 120 fractions exactly, and the same best rows under the seat, cov and free menus | 85% |
| A3 | **A new look, labelled:** every covariant reading with the lepton factor free, the menu main did not compute. The mean fraction over the 20 seeds is above 1% | 65% |
| B0 | **The own instrument's controls.** W93's residues × κ equal the circle residues of main's bilinear (re-implemented from its definition) to 10⁻¹⁰ relative at the two best points in every sector. J1 holds on every coupling built, to 10⁻¹⁰‖Y‖³ | 75% |
| B1 | **The rows.** On the 38 points every stored ratio and \|V\| above 10⁻¹⁰ is reproduced to 10⁻⁶ in log, and J to 10⁻⁵ relative; the same values fall below 10⁻¹⁰ | 65% |
| B2 | **The two best rows, from the own values:** worst factor 1.2016 with D = 11.008 for the best six; 1.8991 with J = −3.968 × 10⁻⁶ for the best nine; each to 10⁻⁶ relative | 65% |
| B3 | a read-out: B1725's control point (0.4 + 2.7i, (2/5, 1/10)) on the own instrument, against the web seat's stored row | — |
| C1 | **R7's mechanism on the committed census.** On every order-5 row (1 080 points × 2 horocycles), in S and in S̃: \|ln D_frame\| ≤ 10⁻⁸, so D = 9 exactly at c = 3 | 97% |
| C2 | the same on the own instrument's order-5 points | 85% |
| C3 | labelled: orders 1, 2 and 4 (B1728's other d = e orders), on rows not masked by exact zeros: \|ln D_frame\| ≤ 10⁻⁸ | 85% |
| C4 | a read-out: the spread of D_frame on order-10 rows (min, median, max; both readings). The best six-row's D_frame is 11.008/9 = 1.223 | — |

## The looks, by reading the code (stated now, before any run)

- **How data and random targets are treated: nothing asymmetric found.** Both get the same rows, menus and measure,
  the same 10⁻³⁰⁰ floor and the same tie rule, which counts ties against the claim. The factor acts on the model
  only, and the random draws do not depend on the data.
- **Looks not counted in B1726's calibration:**
  1. **The ingredients.** The factor 3, its direction and the seat's reading rule were chosen on the web seat's rows,
     with the data in view. No menu frees both the readings and the factor; A3 adds that menu, labelled.
  2. **The null.** It draws the three sectors independently, while the data carry the Georgi–Jarlskog relations the
     factor was chosen to match. From the pinned masses, (m_μ/m_τ)/(m_s/m_b) = 3.14 and (m_d/m_b)/(m_e/m_τ) = 3.37.
     So the fraction partly re-measures a known feature of the data that was put into the model.
  3. **The count of looks.** compare.py computes six fractions; B1726's FINDINGS applies Bonferroni over four. Over
     six, the six under the seat's menu give 6 × 0.0011875 = 0.0071. That is still below THE_BAR's 0.01, so the
     verdict does not change; the count does.
  4. **The region.** The fresh points interleave with B1725's grid at 0.05 in Im τ, on the same lines.
- **Record issues:**
  - census.jsonl's sha256 is pinned only in the lock test.
  - B1725's census is on the web seat's branch, not in main's tree.
  - The web seat's census script imports main's b1656_funcs.py and the_exponents.py, so B1726's C1 ("against B1725")
    compares main's code with itself.
- **Silent behaviour:** a NaN row would silently drop a configuration for every target, since compare.py does not
  check for NaN. A0 counts non-finite values.

## What the outcomes mean (fixed now)

- **A0 to A2 hold.** Main's calibration is reproduced by its own code and by a second code, and R2 to R5's fractions
  stand as computed.
- **A1 fails, A2 holds:** an environment difference (numpy, platform or run). Recorded; A2's fractions stand.
- **A2 fails, A1 holds:** this seat's code or compare.py departs from its stated rule. Diagnosed post hoc and labelled.
- **A3 above 1%:** with every reading and the factor free, the six are not specific at the bar. The claim then rests
  on the reading rule or the factor's value. **A3 at or below 1%:** the specificity survives the most permissive menu.
- **B0 fails:** the own instrument is not trusted, and B1 and B2 are read only after B0's cause is found, post hoc.
- **B1 and B2 hold:** the census rows are reproduced by a second instrument that shares no code with main beyond numpy
  and mpmath, and shares B1667's column as an input.
- **B1 fails, B0 holds:** the instruments disagree on the sample. The failing rows' pieces are recomputed post hoc, and
  the finding goes against whichever instrument is wrong.
- **C1 holds:** R7's mechanism is confirmed. On order-5 lines with c = 3, D = 9 exactly, Georgi–Jarlskog's value, 14σ
  from P-094's 10.58. **C1 fails:** main's census and B1728's identity disagree; reported.
- **This seat's opinion on banking** (fixed now). If A1, A2 and B1 hold, B1726 is a replicated two-ingredient READING.
  It can be banked as that and no more, with the looks above disclosed beside it. If any of them fails, it is not
  banked until the failure is resolved.

## What stays out

- The frame itself: B1656, ∂R and B1667's end. L is an input, not recomputed.
- Recomputing all 23 940 points.
- Grading under THE_BAR, and whether the factor and the reading can be derived (P-294, P-295).

## Seen before the rule (disclosed)

- **The preparation** was a read-only pass in this seat's session:
  - On main: B1726's PREREGISTRATION, FINDINGS, arc_verdict, census.py, compare.py, posthoc.py, comparison.json,
    posthoc.json, control.json, the run logs, ARTIFACT_HASHES and the lock test.
  - Also on main: b1656_funcs.py (B1723's copy), the_exponents.py, qseries.py, B1720's census, the FINDINGS of B1724
    and B1728, B1725's PROVENANCE, and the priors in B1695's and B1713's calibrations.
  - On the web seat's branch: its two-ingredient census script, read and not run.
- **Looked at in the data:**
  - the first 1 500 bytes of census.jsonl and its line count;
  - the two target files' values (the three ratios above come from them);
  - B1667's Re τ = ¼ column of L.
- **The script was drafted and compiled in that pass, before this rule. It has not been run.** It is committed after
  this rule is pushed, with only its header changed, and runs once.
- **By hand:** κ; R7's mechanism (B1728's steps 1–2, again from the code); the three data ratios; the six-look
  correction.

## Discipline

- This rule is committed and pushed before the script runs.
- The script runs once, from the repository root. Its output is committed before it is read.
- A failed part is a failed launch of that part: the script keeps the traceback and runs the other parts. It is
  disclosed, fixed, and only that part is relaunched.
- Any later check is labelled post hoc.

0 of 19.
