### F-R84-B1
**File:** frontier/B1955_the_knots_dihedral_cover_supplies_the_weil_space_and_the_parity_with_no_flux/FINDINGS.md, line 36
**Verbatim quotation:** `An element in the act's class is never a scalar times P (least distance 0.535)`
**What is wrong:** The arc's run gives the least distance as 0.553 (0.5527864...), not 0.535 (digits transposed). The stored json and the lock (> 0.5) agree with 0.553.
**How checked:** verification/wa3_on_main_run.txt lines 4-5 "(least distance 0.553 over 12 such maps)"; wa3_on_main.json "LR_distance_to_scalar_P": 0.5527864045000422.
**Confidence:** high

### F-R84-B2
**File:** frontier/B1956_agy_exps_ten_campaigns_read_at_their_result_notes_and_checked_where_exact/FINDINGS.md, line 44
**Verbatim quotation:** `E₈'s roots under its Q: 46 neutral, 32 singlets of charge ±1, 164 coloured`
**What is wrong:** The script, its run, the lock and the arc's own arc_verdict.json give 162 coloured (46 + 32 + 162 = 240); 46 + 32 + 164 = 242 exceeds the 240 roots of E8. The page also says this "agrees with B1954's count", but B1954 (line 39) states a different partition (colour singlets 40 + 16 + 16, coloured charges including ±4/3) and never gives 46 / 162.
**How checked:** verification/agy_exp_checks_run.txt line 4 "E8: 240 roots = 46 neutral + 32 colour singlets of charge +-1 + 162 coloured"; test asserts (240, 46, 32, 162); arc_verdict.json claim_one_line "E8's 46 + 32 + 162"; B1954 FINDINGS.md line 39.
**Confidence:** high

### F-R84-B3
**File:** frontier/B1956_agy_exps_ten_campaigns_read_at_their_result_notes_and_checked_where_exact/FINDINGS.md, line 45
**Verbatim quotation:** `the two-body sum cannot close for both sectors at level 5, in either convention (X-FOUNDATION-4) | agrees with B1953 and B1955, which main computed`
**What is wrong:** This row sits in the table "What main checked (verification/agy_exp_checks.py)" under the header "main's exact check", but the script and lock contain no check of it (the script's item 5 only prints a sentence). Also B1955 does not simply agree: B1955 section 3 says the up coupling as the top wedge does close (is invariant) at level 5, and its correction says this closure is generic and not a gain; B1953 calls the up sector only "a specification" and scopes its failure to a phase table, not to all constructions. "Cannot close ... in either convention" is stronger than either page.
**How checked:** agy_exp_checks.py has no code for it (line 63 prints text only); B1955 FINDINGS.md lines 72-85; B1953 FINDINGS.md lines 112-117 ("Scope, added 2026-11-17").
**Confidence:** medium

### F-R84-B4
**File:** frontier/B1955_the_knots_dihedral_cover_supplies_the_weil_space_and_the_parity_with_no_flux/FINDINGS.md, line 37
**Verbatim quotation:** `On the frame's 25 lines it is +1/5`
**What is wrong:** The script computes this "signature" on the frame's lines only as a count of lines with n*a = 0 mod 5 (5 for n=1, 5 for n=2, ratio 5/25); no operator, phase or trace on the lines is computed. The code comment itself assumes "a phase that is 1 on its fixed lines". The lock repeats the same count. So the stated value for "tr R(T^2)/tr R(T)^2 on the frame's lines" rests on an assumed phase, not a computation.
**How checked:** wa3_on_main.py line 130 (lines_tr is a bare fixed-point count, comment states the phase assumption); test_b1955_wa3_on_main.py line 54-55 same count.
**Confidence:** medium

### F-R84-B5
**File:** frontier/B1955_the_knots_dihedral_cover_supplies_the_weil_space_and_the_parity_with_no_flux/FINDINGS.md, line 3
**Verbatim quotation:** `**Verdict: PROVED** (the computed statements; exact group theory, SnapPy for the covers' homology;`
**What is wrong:** Several headline statements are floating-point numerics with tolerances (det = 1 to 4e-15, 120 elements by rounding-to-8-digits dedup, "never a scalar times P" by a 360-phase grid, T-spectrum to 2e-15), not exact group theory; arc_verdict.json likewise says "exact finite group theory". The words "exact" and "never" are stronger than the numerics.
**How checked:** wa3_on_main.py lines 87, 100, 116, 122 (np.round key, tolerances, 360-point phase grid); run lines 4-5 print residuals 4e-15, 2e-15.
**Confidence:** low

### F-R84-B6
**File:** frontier/B1956_agy_exps_ten_campaigns_read_at_their_result_notes_and_checked_where_exact/FINDINGS.md, line 15
**Verbatim quotation:** `a line bundle of degree k on a torus has ∣k∣ sections (standard)`
**What is wrong:** A holomorphic line bundle of degree k on an elliptic curve has k sections for k > 0 and none for k < 0 (|k| is the dimension of the zero-mode space of one chirality of the Dirac operator, not "sections"). The same sentence is in the script (item 5 print) and run file.
**How checked:** reading only (Riemann-Roch on a genus-1 curve); agy_exp_checks.py line 63.
**Confidence:** low

## Read and found sound
- B1955 FINDINGS.md: all other figures held against wa3_on_main_run.txt/json, class_is_a_choice_run.txt, wz1_checks_run.txt (20 homomorphisms not on page; cusp degrees 1,2,2; deck group orders 1 and 5; homology Z/5+Z, Z^3, volume ratio 5; det -5, signature 0, q = x^2/5, b = 2x^2/5; roots mod 5 and 25; T-phases 0,1/5,4/5 vs 0,2/5,3/5; c = 2,3 unit shears; signatures +-1/5; 1.5e-6 and 4e-31 matches); sweep counts add up (15 = 2+1+12; 3 = 1+2); citations to B1733, B1884/B1943/B1952, B794, THE_FRAMEWORK, B1953 (correction text) say what is claimed.
- B1955 arc_verdict.json: consistent with the page apart from F-R84-B5 wording.
- B1955 scripts (wa3_on_main.py, class_is_a_choice.py, wz1_checks.py) read in full; test_b1955_wa3_on_main.py read; ran pytest on both arcs' verification folders: 7 passed.
- B1956 FINDINGS.md: one-loop numbers (23/134, 109/201, 23/6, -111/10, 109/15), 506/(201 pi), 45 points split 1+8+4+32, Smith (3,15), campaign table counts (rows 1868-1877, ten campaigns, six/fifteen defects consistent with B1954/verdict), sweep sums (16 = 3+13; 27 = 13+14) all hold.
- B1956 test file and script read in full; lock checks all arithmetic claims except the X-FOUNDATION-4 row (F-R84-B3).

## Not read or not run
- wa3_on_main.py itself (needs SnapPy) not re-run; its saved run and json were read instead. wz1_checks.py not re-run (long lattice sum); saved output read. The 1.5e-6 attribution "the sum's cut" is not tested by any run (quadrature with 48 nodes also contributes); not reported as a finding.
- B1956's claims about agy-exp's notes (41 notes, 85,000 lines, rows 1844-1877, X-FOUNDATION chosen-minimum, UR-3 content) cannot be checked in the reading copy; B915's 15.97 sigma is quoted as pinned.
- B1955's cited web-seat commit lines and B1951 not opened.
