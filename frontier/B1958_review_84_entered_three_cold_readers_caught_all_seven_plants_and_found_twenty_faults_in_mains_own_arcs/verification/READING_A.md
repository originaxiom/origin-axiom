# Review 84, reader A: B1945 and B1950

### F-R84-A1
**File:** frontier/B1945_the_frames_cusp_exponents/FINDINGS.md, line 116
**Verbatim quotation:** `On (S̃ up, S down): the 16 points with a = 0 or ±1/5 give |V₁₃| = 1, and the 10 points with a = ±2/5 give`
**What is wrong:** The points with a = 0 or a = ±1/5 number 4 + 10 = 14, not 16 (24 − 10 = 14). The next line itself says 7/12 = 14/24 and 5/12 = 10/24, and 16 + 10 = 26 is more than the 24 points.
**How checked:** verification/cusp_mixing_run.txt lines 7 to 11 (S̃ up, S down): a = 0 gives 4, a = 1/5 to 4/5 give 5 each, so 4 + 5 + 5 = 14 with row 1 = (0,0,1) and 5 + 5 = 10 with row 1 = (0,1,0).
**Confidence:** high

### F-R84-A2
**File:** frontier/B1945_the_frames_cusp_exponents/FINDINGS.md, line 123
**Verbatim quotation:** `- **The lock** checks all 24 points at height 30.`
**What is wrong:** test_the_mixing_in_the_cusp_is_a_permutation_with_v33_zero loops over five points only, (0,2), (1,3), (2,1), (3,4), (4,1), and one reading pair (S̃ up, S down). It does not check "all 24 points" nor both reading pairs. It checks |V33| < 1e-3, that one entry is 1, and that row norms are 1, not that the matrix is a permutation.
**How checked:** verification/test_b1945_cusp_exponents.py lines 94 to 105, the tuple on line 98 has five points.
**Confidence:** high

### F-R84-A3
**File:** frontier/B1945_the_frames_cusp_exponents/FINDINGS.md, line 45
**Verbatim quotation:** `the closed form breaks in all 20 cells it touches.`
**What is wrong:** No script or lock plants the charge in the closed form. The only planted-charge check is the tropical rule (80 cells, tropical_check_run.txt). The lock's closed-form test has no planting. Planting u = -3 in the closed form for m2/m3 breaks 40 cells (20 points with a ≠ 0 times two readings), not 20, so "20" appears from no output.
**How checked:** In scratch, reran the test's closed-form loop with u = -3: `-3 96 40` (96 cells, 40 break at the test's tolerances); with u = -4, 0 break. test_b1945_cusp_exponents.py has no planted case at lines 45 to 55.
**Confidence:** medium

### F-R84-A4
**File:** frontier/B1945_the_frames_cusp_exponents/FINDINGS.md, line 180
**Verbatim quotation:** `Its mass ratios at τ and at τ + 1 differ, by up`
**What is wrong:** The sentence continues "to 80 %", but the run output has larger differences. Down S at 0.13 + 1.7i: the m1/m3 ratio is 0.005094 against 0.010142, which is +99%. Down S̃ gives 0.024113 against 0.044238 (+83%). Up S gives 0.119098/0.065993 = +80.5%, the only one the 80% matches.
**How checked:** verification/amplitude_sum_run.txt lines 1 to 4.
**Confidence:** high

### F-R84-A5
**File:** frontier/B1945_the_frames_cusp_exponents/FINDINGS.md, line 3
**Verbatim quotation:** `every cell, both generations, equal to B1788's closed form and tropical`
**What is wrong:** The closed form e = 1/2 − (‖2q_Lα‖ + ‖2q_Rα‖)/2 is only for m2/m3. The lock's closed-form test asserts n == 96, the second-generation cells only. Only the tropical rule is tested on both generations (192 cells). The same overstatement is in arc_verdict.json claim_one_line ("every cell of both generations given by B1788's closed form ... and its tropical rule").
**How checked:** test_b1945_cusp_exponents.py lines 45 to 55 use `last(k, p, 0)` only; page line 41 says "Every m₂/m₃ cell, all 96, is B1788's closed form".
**Confidence:** medium

### F-R84-A6
**File:** frontier/B1945_the_frames_cusp_exponents/FINDINGS.md, line 85
**Verbatim quotation:** `the largest entry: e(Y) = D² + E′² − ¼;`
**What is wrong:** The four closed forms of § 2 (e(Y), e(adj Y), e(det M), and e(det S) = ¼ on the Higgs side) are said to be "Measured at the three kinds of point", but no script, output or test in the arc computes the exponent of the largest entry, of the adjugate or of det M. The arc's only related outputs are the ratio rates, the tropical check and the determinant law. These forms are unsupported by the arc's own record, and the arc is stated as proved.
**How checked:** Read all scripts and *_run.txt files in verification/. grep for adj, det M and largest entry exponents finds only determinant_law.py, which checks det Y = 4 det S det M tr(εSMᵀ) and does not read exponents.
**Confidence:** medium

### F-R84-A7
**File:** frontier/B1950_review_83_entered_both_readers_caught_all_six_plants/FINDINGS.md, line 35
**Verbatim quotation:** `agy-002 reports 31 and agy-exp 21.`
**What is wrong:** arc_verdict.json says agy-exp's reading has 20 findings ("agy-exp's reading for Review 83 (harvest row 1844): 20 findings, six of them the plants"). The page says 21. The F-R83 numbers the page cites run 05 to 20, consistent with 20 findings.
**How checked:** arc_verdict.json, cites_seat line 20; FINDINGS.md lines 35, 41 to 62 (highest F-R83 number is 20).
**Confidence:** high

### F-R84-A8
**File:** frontier/B1950_review_83_entered_both_readers_caught_all_six_plants/FINDINGS.md, line 37
**Verbatim quotation:** `### Mended in this entry, each recomputed by main (`verification/main_checks.py`)`
**What is wrong:** main_checks.py covers only four of the eight mends: C1 (R83-20 and F-R83-05), C2 (F-R83-07), C3 (F-R83-11), C4 (R83-19). R83-17 (the −0.39 at 1.05i, the heights 1.2 to 9), R83-18, R83-11 and F-R83-14, and R83-26, F-R83-16 and F-R83-17 are not computed by it. The −0.39 and the −0.12 appear only in B1941's note, which says "recomputed by main (B1950)", but no output anywhere in B1950 or B1941's verification has them. The verdict's "eight mended here on main's own recomputation" shares the overstatement.
**How checked:** main_checks.py and main_checks_run.txt (C1 to C4 only); grep for "-0.39" in B1941's verification files: none, only B1941/FINDINGS.md line 42.
**Confidence:** high

### F-R84-A9
**File:** frontier/B1950_review_83_entered_both_readers_caught_all_six_plants/FINDINGS.md, line 18
**Verbatim quotation:** `exact in the reading commit: agy-002's 28 of 28 and agy-exp's 20 of 20.`
**What is wrong:** The arc has no saved output of quote_check.py (only main_checks_run.txt exists), and quote_check.py runs `git ls-tree` and `git show` on commit b35eac607, so it cannot be rerun from the arc's files. The counts 28 of 28 and 20 of 20 are not backed by any committed output. The "could parse" qualifier also hides that the check searches a pooled corpus of many files, not the file each reader cited, so "exact" means present somewhere in the window, not at the cited path.
**How checked:** ls of B1950/verification (plants.json, plants_sha256.txt, main_checks.py, quote_check.py, main_checks_run.txt); quote_check.py lines 7 to 16, 28.
**Confidence:** medium

### F-R84-A10
**File:** frontier/B1950_review_83_entered_both_readers_caught_all_six_plants/FINDINGS.md, line 45
**Verbatim quotation:** `The double and extended frames agree there; the exchange is the real approach to the cusp limits`
**What is wrong:** C4's output shows agreement only on the three mixing moduli at x = 0.13 (0.4282, 0.4169, 0.5832 against 0.42815, 0.41689, 0.58318). In the same lines the double run shows T-check 1.2e-01 and x-variation 1.3e-01 at y = 12 against 7.04e-18, and its fourth value 8.702e-17 against 5.2949e-17. The frames do not agree in general at height 12. The page states agreement without the x = 0.13 and moduli-only scope.
**How checked:** verification/main_checks_run.txt lines 9 and 10.
**Confidence:** low

## Read and found sound

- B1945 FINDINGS.md, whole page: the § 1 table matches pointwise_exponents_run.txt (all 24 points, four columns); closed form recomputed for both sectors at a = 1/5, 2/5 gives 1/10, 3/10, 1/5; § 1b W-F25 conversions (factor 2) are consistent with the table; § 2's S expansion gives det S = 1/4 q^(1/4) by hand; 48 cases and 1.8e-30; 192 cells and 1.2e-3; 80 broken cells; § 3 minima all match the table; 72 and 192 points of exact order; the § 3c table matches levels_mixing_run.txt; § 5 ratios 11/4 and 5/2; the § 6 Gramian table matches gramian_and_sum_run.txt and .json cell for cell; 2.719 and 3.028, 4.4e-3, 1.4e-4, height 0.585; the B1953 citation (ζ^(−a²), ζ^(2ab), ζ^(−ab)) and the B1946 pointer match those pages.
- B1945 arc_verdict.json: agrees with the page except for the overstatement in F-R84-A5.
- B1945 scripts and tests: all read in full. The pytest file ran, 10 passed (24.8 s), and tropical_check.py reran to its saved output.
- B1950 plants.json and plants_sha256.txt: the sha256 of plants.json is b3da3d92…, as stated; the six plants match the table rows.
- B1950 main_checks_run.txt: C1 (LR fixes k(1,2)/5, RL fixes k(1,3)/5), C2 (torsion 1, 5, 1) and C3 (signed swap, i'/i = 1, j'/k = 1, k'/j = −1) match the page. Checked B1943's, B1935's and B1940's notes: they cite what the page says.
- B1950 arc_verdict.json: read; the only disagreement is the 20 against 21 in F-R84-A7.

## Not read or not run

- quote_check.py: needs git and the reading commit, and git is prohibited. Not run.
- The heavy scripts (pointwise_exponents*.py, cusp_mixing.py, levels_mixing.py, amplitude_sum.py, gramian_and_sum.py, determinant_law.py): not rerun, their saved outputs were read. The test file, which runs several of them live, passed.
- B1950's counts (47 of 1691 arcs, 62 register rows, the 28 and 20 quotations) and the readers' own files were not in the copy. B1698's 1.675% was checked against B1698; the W178, W-F25 and agy-exp items are citations to seat records not in the copy.
