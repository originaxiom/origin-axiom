# W141 — the third opinion on main's B1734 (P-339): the re-run, the calibration on own code, the restriction's cost on own code, the rows on own code, the thread rule's lines and points checked, R7's mechanism, and the looks (the rule, committed before the script)

The SM-derivation seat, 2026-10-23. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **Main's B1734** held as sealed for its question. With τ at each thread's apex and the line among its own order-5
  and order-10 lines, the six charged-fermion ratios come within 1.614, and 0.16% of random hierarchies do as well
  under the seat's menu.
  - Main graded it a READING carried by one thread pair on an order-5 line, where D = 9 exactly, which P-094 excludes.
  - Lifting the order restriction leaves it at the bar.
- **The owner's rule of 2026-08-21:** a positive value match is not banked as more than a reading without a third
  opinion.
- **Main's P-339 asks the seats for five things:**
  - re-run compare.py on census.json;
  - recompute the best rows on their own instruments;
  - check B1733's line sets independently;
  - repeat the post hoc all-orders check (FINDINGS §3 B) with their own code;
  - look for any uncounted look.
- **The owner approved this seat's doing it (2026-10-23).**

## The objects

- **Main's committed files at 91b76e744** (S199), read with `git show`:
  - B1734's census.py, compare.py and posthoc.py; census.json, comparison.json, control.json, posthoc.json,
    allorders.json and compare_run.txt; ARTIFACT_HASHES.txt;
  - the files the instruments read in place, pinned there: B1720's thread census, B1726's census.py and its
    dependencies, B1667's column, the masses and the CKM data;
  - B1735's check.json, for its B1734 per-seed fractions under every covariant reading with the factor free.
- **The own instrument,** this seat's code, as in W138:
  - imported from W138's committed script: the calibration (the draws, the errors, the menus); W93's units and
    closed-form residues; W89's kernel norms with 12 theta terms; the Higgs DR from direct theta sums; the scale κ;
    the bilinear re-implemented for the residue control; the comparison per point;
  - written fresh here: the census arrays in B1734's row order (class, line), the per-row description, the fixed
    lines by brute force, the Smith invariants, the apex from the monodromy, and D_frame per row.
  - It imports nothing of main's census.py, compare.py, posthoc.py, b1656_funcs.py, the_exponents.py or qseries.py.
    It shares B1667's column of L and B1720's stored τ and lines as inputs; C1 and C2 check the latter.
- **The sample for B, 28 points:**
  - the three named rows' points: L⁵R² on (2/5, 3/5), the best six; L⁵R⁴ on (2/5, 1/10), the best nine under the
    seat's menu; L⁶RLR on (1/10, 3/5), the best nine under the covariant menu;
  - 25 of the 190 points drawn by `random.Random(339)`.
- **D_frame** = (m_μ·m_d)/(m_s·m_e) from the frame's ratios at c = 1. compare.py's D is c²·D_frame.

## Weave or thread

**Neither, strictly: a check of main's census of one frame** (B1656's coupling on the shared fibre) at the threads'
own points. The census takes every one of B1720's 121 classes that has order-5 or order-10 lines, under main's rule,
with none hand-picked. The claims are about main's code and stored numbers.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| A0 | **The inputs.** compare.py, census.py and the files they read in place match B1734's ARTIFACT_HASHES. census.json holds 190 unique (class, line) points with no NaN or infinity. Its sha256 is recorded, since nothing on main pins it | 95% |
| A1 | **The re-run.** Main's compare.py runs once on the committed census.json in a temporary tree and exits 0. All 120 per-seed fractions and the six means equal comparison.json exactly. Every other number agrees to 10⁻¹² relative, the eight cells are the same, and stdout equals compare_run.txt | 92% |
| A2 | **The calibration on own code** (B1734's seeds 1734–1753, 4 000 targets each). The same 120 fractions exactly, and the same best rows under the seat, cov and free menus (row and configuration; factor to 10⁻¹²). Under every covariant reading with the factor free, the 20 per-seed fractions equal main's B1735 check.json exactly (mean 2.2225%) | 88% |
| A3 | **The restriction's cost on own code.** From main's allorders.json (3 249 points, 6 498 rows), the best six is 1.6138 under the seat and cov menus. The per-seed fractions for seeds 1734–1738 equal posthoc.json exactly: seat mean 1.13%, cov 3.725% | 85% |
| A4 | **A new look, labelled:** the same all-orders census over all 20 seeds and four menus (seat, cov, free, every covariant reading with the factor free). The seat's mean is above 1% | 60% |
| B0 | **The own instrument's controls.** At the three named points, W93's residues × κ equal the circle residues of main's bilinear (re-implemented) to 10⁻¹⁰ relative in every sector. J1 holds on every coupling built, to 10⁻¹⁰‖Y‖³ | 75% |
| B1 | **The rows.** On the 28 points, every stored ratio and \|V\| above 10⁻¹⁰ is reproduced to 10⁻⁶ in log, and J to 10⁻⁵ relative where \|J\| > 10⁻¹⁰. The same values fall below 10⁻¹⁰ | 60% |
| B2 | **The named rows from the own values.** The best six: worst factor 1.6138 and D = 9.000, each to 10⁻⁶ relative. The best nine under the seat's menu: 4.5804 to 10⁻⁶ relative, with \|J\| below 10⁻¹⁰, zero to rounding. The best nine under the covariant menu: 2.535 to 10⁻³ (the precision FINDINGS quotes) | 60% |
| C1 | **The thread rule's lines.** For each of B1720's 121 classes, the stored lines are exactly the nontrivial lines its monodromy fixes up to sign, found by brute force. The Smith rule (order N fixed iff N divides d₂(A − I) or d₂(A + I)) has no mismatch for N ≤ 30. Exactly 49 classes have lines of order 5 or 10. They give 190 points, 98 of order 5 and 92 of order 10, each order-5 line with its partner 2v, and these are census.json's points | 95% |
| C2 | **The thread's points.** Every class's stored τ is the top of its monodromy's axis, ((a − d)/(2c), √(t² − 4)/(2\|c\|)) for A = ((a, b), (c, d)), to 10⁻¹² | 85% |
| C3 | a read-out: the number of distinct (τ, line) points among the 190, and the classes that share one | — |
| D1 | **R7's mechanism on the census.** On every order-5 row (98 points × 2 horocycles), in S and S̃: \|ln D_frame\| ≤ 10⁻⁸, so D = 9 exactly at c = 3 | 97% |
| D2 | a read-out: D_frame on the order-10 rows (min, median, max; both readings) | — |

## The looks, by reading the code (stated now, before any run)

- **Data and random targets are treated alike.** B1734's compare.py has B1726's structure: the same rows, menus and
  measure, the same 10⁻³⁰⁰ floor, and the same tie rule, which counts ties against the claim. Nothing asymmetric was
  found.
- **Looks not counted in B1734's calibration:**
  1. **The restriction to orders 5 and 10.** It was informed by B1726's result, and main disclosed that. Its cost is
     A3 and A4.
  2. **The ingredients and the null,** carried over unchanged from W138. The factor 3, its direction and the reading
     rule were chosen with the data in view. The null draws the three sectors independently, while the data carry
     the Georgi–Jarlskog relations the factor was chosen to match.
  3. **The count of looks.** compare.py computes six fractions; B1734's FINDINGS applies Bonferroni over four. Under
     the seat's menu:
     - over six, 6 × 0.0015875 = 0.0095, just under THE_BAR's 0.01;
     - counting main's post hoc all-orders look as a seventh, 0.0111, over it.
     The covariant and free menus are over the bar under any count of two or more.
  4. **Mirror duplicates.** L⁵R² and L²R⁵ stand at the same τ = 3.5 + 2.958i with the same four lines, as seen in the
     preparation. So FINDINGS §3 A's "2 of the 380 rows within 2" are one (τ, line) point, counted twice. C3 counts
     the duplicates. The calibration is unaffected, since a duplicated row changes no best.
  5. **τ is not reduced to a strip.** The apexes have Re τ up to 3.5. The frame is T-covariant with the line moved
     along (B1726's control, 1.8 × 10⁻¹¹), so nothing is lost. The own instrument's norms then integrate over a
     slanted cell, which B1 tests.
- **Record issues:** census.json and allorders.json are pinned nowhere; the lock test asserts stored values only.
  ARTIFACT_HASHES lists the instruments and their inputs, not the outputs.

## What the outcomes mean (fixed now)

- **A0 to A2 hold.** Main's calibration is reproduced by its own code and by a second code, and R2 to R4's fractions
  stand as computed. A2's last clause also reproduces B1735's labelled check on this census.
- **A1 fails, A2 holds:** an environment difference, recorded; A2's fractions stand. **A2 fails, A1 holds:** this
  seat's code or compare.py departs from its stated rule; diagnosed post hoc and labelled.
- **A3 holds.** Main's post hoc cost of the restriction stands on a second code.
- **A4 above 1%:** with the restriction lifted, the six are not specific under the seat's menu either. **A4 at or
  below 1%:** at the bar, as main found on five seeds.
- **B0 fails:** the own instrument is not trusted, and B1 and B2 are read only after B0's cause is found, post hoc.
- **B1 and B2 hold:** the census rows are reproduced by a second instrument. It shares with main only B1667's column
  and B1720's τ and lines, which C1 and C2 check.
- **B1 fails, B0 holds:** the failing rows' pieces are recomputed post hoc, and the finding goes against whichever
  instrument is wrong.
- **C1 and C2 hold:** the thread rule's lines and points are what main says they are.
- **D1 holds:** the best six-row's D = 9 is structural, Georgi–Jarlskog's value on an order-5 line.
- **This seat's opinion on banking (fixed now).** If A1, A2, B1 and C1 hold, B1734 is a replicated READING. It has
  two hand-put ingredients and an order restriction informed by B1726, and it is carried by one (τ, line) point on an
  order-5 line, whose D = 9 the data exclude. It can be banked as that and no more, with the looks beside it; it is
  not a value match. If any of A1, A2, B1 or C1 fails, it is not banked until the failure is resolved.

## What stays out

- The frame itself (B1656, ∂R, B1667's end). L is an input, not recomputed.
- B1720's class list, as a sealed input.
- Recomputing all 190 points or the 3 249 all-orders points on the own instrument.
- B1735's precision bar (P-342 asks for its own third opinion), and P-340.

## Seen before the rule (disclosed)

- **The preparation** was a read-only pass in this seat's session.
  - **On main (91b76e744):** B1734's PREREGISTRATION, FINDINGS, census.py, compare.py, posthoc.py, ARTIFACT_HASHES and
    the lock test; B1733's FINDINGS; B1735's check.py, check_run.txt and its B1734 per-seed values; B1726's census.py
    compute(); S198's and S199's commit messages.
  - **Looked at in the data:**
    - B1720's census keys, its first class, and its counts (121 classes, 3 249 rows);
    - census.json's row keys, its Im τ range (1.118 to 3.873) and its order counts (98, 92, 49 classes);
    - the eight rows of L⁵R² and L²R⁵ (their τ and lines);
    - comparison.json's best rows under the seat's menu and its means;
    - posthoc.json in full;
    - B1667's column range (Im τ 1 to 4).
- **By hand:** the six-look and seven-look corrections; the apex formula, checked on LR alone (1.5 + 1.118i).
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- The script runs once, from the repository root, and its output is committed before it is read.
- A failed part is a failed launch of that part: the script keeps the traceback and runs the other parts. It is
  disclosed, fixed, and only that part is relaunched.
- Any later check is labelled post hoc.

0 of 19.
