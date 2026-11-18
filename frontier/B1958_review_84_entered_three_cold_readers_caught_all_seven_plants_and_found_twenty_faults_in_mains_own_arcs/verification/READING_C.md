# Review 84, reader C: frontier/B1957_the_seats_claims_register/

### F-R84-C1
**File:** frontier/B1957_the_seats_claims_register/FINDINGS.md, line 348
**Verbatim quotation:** `subregular sl₂ fixes no vector of the 27: 15 + 7 + 5). The relay's theorem stands for the simpler reason main`
**What is wrong:** The decomposition of the 27 under the subregular sl2 is 13 + 9 + 5, not 15 + 7 + 5. The check script, its run file, the record web-sr-01, the lock test and the commit text all give 13 + 9 + 5. The page's figure sums to 27 but is wrong.
**How checked:** checks/web_session_relay_f4_run.txt: "subregular ...: {12: 1, 8: 1, 4: 1}, dimensions [13, 9, 5]"; script docstring "27 = V_12 + V_8 + V_4 (dimensions 13 + 9 + 5)"; test_b1957_checks.py line 399 asserts {12: 1, 8: 1, 4: 1}. `grep "15 + 7 + 5"` finds only FINDINGS.md line 348.
**Confidence:** high

### F-R84-C2
**File:** frontier/B1957_the_seats_claims_register/FINDINGS.md, line 478
**Verbatim quotation:** `Six findings are about agy-exp's sources, which main has harvested in full: nothing is held.`
**What is wrong:** agy-exp's lane is not harvested in full. SUMMARY.json gives agy-exp 88 files, 5 read at source, 2,027 of 2,099 statements pending. The record physical-as-01 says the opposite of the page: its note reads "about agy-exp's X-CLOSURE sources, which main has not yet harvested (2,027 statements pending in that lane); ... main's own verdicts on that lane's claims are still owed". The commit message for the same state also says six findings are "held for that".
**How checks:** verification/SUMMARY.json lanes["agy-exp"] (read 5, PENDING 2027); verification/records/physical-as-01.json field "note".
**Confidence:** high

### F-R84-C3
**File:** frontier/B1957_the_seats_claims_register/arc_verdict.json, line 23 (field claim_one_line; also line 18, field scope.frame)
**Verbatim quotation:** `14,878 statements (agy-exp 2,040; agy-002 978; the physical lane 10,781; the web seat 955; the agy audit lane 124)`
**What is wrong:** The arc's machine-readable claim and scope are stale. They say 275 files and 14,878 statements. SUMMARY.json, which the lock holds equal to the state, gives 406 files and 20,863 statements (agy-exp 2,099; physical 10,952; web 6,710). The claim line also describes the register as having every statement "pending until a record gives its verdict", while 17,360 are settled and the page says the window was widened several times.
**How checked:** sum of SUMMARY.json lanes: files 406, statements 20,863, PENDING 3,503. No lock compares arc_verdict.json with SUMMARY.json.
**Confidence:** high

### F-R84-C4
**File:** frontier/B1957_the_seats_claims_register/FINDINGS.md, line 462 (rule), against verification/records/ (violations)
**Verbatim quotation:** `a verdict of VERIFIED may not sit over a note that says "not recomputed",`
**What is wrong:** The page states this as the rule main learned, but no test enforces it and the records break it. These records are VERIFIED and carry "not recomputed" or "not rerun" or "not checked" or "taken as cited" in their own text. web-wc2-03: note begins "Not recomputed: the 240 roots found in dP9's complement ... the weights are the seat's". web-wf17-04: "Not recomputed: the degrees of the space curves ... completeness tests"; its own note says the claim is "partial in its completeness". web-wc3-01: "not rerun on main". web-wc2-02: "other three conventions are not rerun". web-wf4-01: "The plants P1 and P2 ... were not rerun". web-wf24-05: verified by reading, classical theorem "taken as cited", theorem number "not checked". web-wz1-04: "the standard result, not recomputed". Many more VERIFIED records carry a not-recomputed clause, 92 of 238 by a keyword scan. The lock test_b1957_register.py does not read records' how or note fields.
**How checked:** Python scan of verification/records/*.json for verdict VERIFIED and the phrases; the individual records read in full.
**Confidence:** medium (some of these notes may refer to statements not in the record's unit list; the unit text is not in the reading copy, but the page's own rule says the note decides)

### F-R84-C5
**File:** frontier/B1957_the_seats_claims_register/verification/test_b1957_register.py, line 28 (test_no_lane_is_called_complete_while_a_statement_is_pending)
**Verbatim quotation:** `assert "HARVEST COMPLETE" not in page or all(L["PENDING"] == 0 for L in lanes.values())`
**What is wrong:** The test cannot fail. `page` is REGISTER.md, which build.py generates and which never contains the words (grep count 0, and the generator has no such string), so the first disjunct is always true. The name says "no lane", but the second disjunct is a whole-register test. The seat pages, where HARVEST COMPLETE would be written, are not read. In the same file, test 1 contains the tautology `len(U["files"]) == sum(1 for f in U["files"])`. Its next line, comparing the statement count of the units with the sum of the lanes' counts, uses numbers build.summary derives from the same units.
**How checked:** `grep -c "HARVEST COMPLETE" REGISTER.md` gives 0; read build.py (the page template has no such text); ran both lock files: 51 passed.
**Confidence:** high

### F-R84-C6
**File:** frontier/B1957_the_seats_claims_register/verification/records/web-p783-03.json (field how)
**Verbatim quotation:** `the least scaled singular value never falls below 0.67 in any of the four classes at either height`
**What is wrong:** The check does not give a per-height bound. P5 reports `max(ls(...,0), ls(...,1))`, the larger of the two heights, and the run prints that its minimum over t is 6.69e-01 for class (-1, 1), which is below 0.67. So "at either height" is not computed, and "never falls below 0.67" is false by the printed value (0.669). The page builds "there is no exceptional eigenvalue" on this.
**How checked:** checks/web_p783_spectrum.py line 67 text "(the larger of two heights)" and the loop `vals_.append(max(ls(0.0, c, 0), ls(0.0, c, 1)))`; checks/web_p783_spectrum_run.txt P5: "(-1, 1) 6.69e-01".
**Confidence:** medium-high

### F-R84-C7
**File:** frontier/B1957_the_seats_claims_register/FINDINGS.md, line 105 to 106
**Verbatim quotation:** `24 points orthogonal, 9 inside a degenerate pair, none aligned) and lift-dependent; with one Higgs mode the`
**What is wrong:** The run gives orthogonal 10, degenerate-outside 5 and degenerate-inside 9, and 4 aligned under the lifts a+1 and (a+1, b+1). The 15 is 10 orthogonal plus 5 "degenerate, outside". The record agy002-g5-04 says "outside ... at 15 of the 24 points", but the page and record agy002-g5-07 say "15 of 24 orthogonal". "None aligned" holds only for the seat's representatives, and the page itself calls the count lift-dependent.
**How checked:** checks/agy002_g5_run.txt, first B line: "degenerate, inside 9, degenerate, outside 5, orthogonal 10"; the lift lines: "aligned 4".
**Confidence:** medium

### F-R84-C8
**File:** frontier/B1957_the_seats_claims_register/verification/records/web-wtau-01.json (field how)
**Verbatim quotation:** `y |eta|^4 has a saddle at i (Hessian -1.298, 0.298) and its maximum at omega (-0.667 twice)`
**What is wrong:** The Hessian eigenvalues -1.2982, 0.2982 and -0.6667 twice in the run are for log(y|eta|^4), not for y|eta|^4. The Hessian of y|eta|^4 at a critical point is that of its logarithm times the function's value there, so the numbers differ. The type of critical point is unchanged, but the record attributes printed figures to the wrong function.
**How checked:** checks/web_weave_action_on_tau_run.txt: "S1, S2: log(y |eta|^4): i: ... Hessian eigenvalues ['-1.2982', '0.2982']; omega: ... ['-0.6667', '-0.6667']".
**Confidence:** high

### F-R84-C9
**File:** frontier/B1957_the_seats_claims_register/FINDINGS.md, line 386 to 387
**Verbatim quotation:** `**Every computed figure of the seat's` (line 386, continuing "reproduces.**" on line 387)
**What is wrong:** "Every" is wider than the records. In the same card group, web-wc2-03 says the 240 roots in dP9's complement and the E8 grading weights were not recomputed. web-wf17-04 says the degrees of the space curves, the point counts on kappa = 2 and the completeness tests were not recomputed. web-wf4-01 says the plants P1 and P2 were not rerun. 34 and 12 statements were moved to PARTIAL on that account in the same record notes.
**How checked:** records web-wc2-03, web-wf17-04, web-wf4-01, field note.
**Confidence:** medium

### F-R84-C10
**File:** frontier/B1957_the_seats_claims_register/verification/records/agy002-g1-01.json (field how)
**Verbatim quotation:** `the closed form (23/134, 109/201, 506/201) from the slopes, 22 (23/3)/67 = 506/201 (also B1956)`
**What is wrong:** The cited check computes and prints only 506/201. Neither agy002_g0_g1.py nor its run file contains 23/134 or 109/201; they appear in this record and in RELATIONS.md only. The record is VERIFIED for a three-coefficient closed form of which two were not derived in this arc's check. It leans on "also B1956", which is outside the arc.
**How checked:** `grep -n "134\|109\|201\|506" checks/agy002_g0_g1.py` gives nothing. The run file has only "22 delta_b / 67 = 506/201".
**Confidence:** medium

### F-R84-C11
**File:** frontier/B1957_the_seats_claims_register/verification/records/agy002-g5-03.json (fields verdict and note)
**Verbatim quotation:** `vacuous: one matrix compared with itself`
**What is wrong:** The record is marked VERIFIED while its own note says the statement is empty. It is "true, and empty": a claim the record itself shows says nothing. Under the page's own table, VERIFIED means "recomputed on main's own code, and it holds". The sibling records g5-07 and g5-04 are PARTIAL for the same material, so the register disagrees with itself on one fact.
**How checked:** read agy002-g5-03, g5-04 and g5-07 together with checks/agy002_g5_run.txt line "C: ... (its script evaluates the same expression twice)".
**Confidence:** low

## Read and found sound

- FINDINGS.md read in full (491 lines). Counts reconcile with SUMMARY.json: agy-002 30-file figures (197, 9, 47, 53, 158, 14), agy-002 verify (284, 3, 52, 161), P-C3 (129+187+114=430), P-C3b-d (204+252+129=585), P-C3f (40+50+60=150), F01-F17 (57+11+96=164), physical own material (10,952 - 7,649 = 3,303), and all-lane totals 20,863 / 17,360 settled / 3,503 pending, which match the latest commit.
- The 51 lock tests (both files) ran and pass. The 23 test bodies I read by eye each assert what their names say, apart from F-R84-C5.
- Run files checked against page and record figures and found right: sm_rge_matrix (4.4e-16, 8.7e-15, 7.578626559316), web_section9_items (I3 to I7), web_wz1_c3_indices, web_wz1_other_discriminants (the G versus E normalisation is consistent), web_wc8_part2a_duality, web_wc8_part4_on_main, web_wc8_part1_on_main, web_wf12/wf19/wf8/wf11/wf22/wf26/wf3/wf9, agy002_m40, agyexp_ur345, physical_c3e_roster, physical_cyclic_mass, web_wc6_part2, web_first_row_bound, web_posthoc_closure, web_session_relay_three and _f4 (except C1), physical_seal_ledger (the 7,645 + 4 = 7,649 split is consistent), agy002_g6, web_zero_free_directions, web_wb2_d1.
- Records sampled (more than 40 VERIFIED across prefixes): web-wz1-01/02/04, web-wc1-01, web-wc2-02/03, web-wc3-01, web-wc8p5-01, web-st8-03, web-wa3-02/07, web-wb2-d1-01/04, web-wf4-01, web-wf6-01, web-wf17-04, web-wf18-01, web-wf21-01, web-wf22-01, web-wf23-01, web-wf24-05, web-wf25-02/03, web-wh1-01, web-scale-01, web-p783-02/03/04/06, web-st6-01, web-wc6p2-01, web-zf-01, web-wa1-02; agy002-g5-01 to 09, agy002v-m34-06/09, agy002v-m40-02, agy002v-r83-05, agy002v-view-02; agyexp-ur345-01; agyaudit-p753-07; physical-as-01, physical-join-01, physical-pen-02, physical-harm-02, physical-ij-01, physical-seal-01/02.
- Check scripts read at script level: web_first_row_bound, web_posthoc_closure, web_session_relay_f4, web_session_relay_three, physical_seal_ledger, web_wz1_other_discriminants, web_p783_spectrum (P5), agy002_g0_g1, web_wc8_part4_on_main (S2's determinant term `(m*m*0 - m*m) == -m*m` is a typed identity that cannot fail; trivial), plus the run files above.
- Minor, not reported as findings: physical_seal_ledger says "the base's 9,411 lines are the head's first 9,411", but the code compares 9,410 real lines (it counts the empty trailing element). web_session_relay_three docstring says "64 standard Levi" while the run says 63 non-empty.

## Not read or not run

- Check scripts that call git (physical_seal_ledger, web_posthoc_closure main, custody, figures, others): not run, per the rules. Their saved run files were read.
- Check scripts of other arcs named by records (wa3_on_main.py, class_is_a_choice.py, second_computations.py, wa2_on_main.py, etc.): not in this arc or the reading copy path I was permitted to check, so figures that rest on them were not checkable.
- The unit text of each statement (stored at the seat's source commits) is not in the reading copy, so I could not check which statements each record covers. Verdict-versus-note findings (F-R84-C4, C9) rest on the record text alone.
- Most of the 665 records and about 50 check scripts were not read line by line; the many sampled run files used a number-presence scan against the records' "how" fields. Where a figure was absent I opened the specific records (those listed above); the remaining mismatches in the scan were format differences (rounding, units).
- RELATIONS.md and REGISTER.md body rows were not read beyond spot checks.
