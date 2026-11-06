# Review 75 reader: B1834, B1836, B1838 read in full

Firewall kept: no held-out value read or computed. All re-runs were data-free scripts already committed. Nothing was edited.

## B1834 (total-inputs scoreboard): HOLDS WITH NOTES
Notes:
1. frontier/B1834_the_total_inputs_scoreboard/FINDINGS.md and arc_verdict.json claim_one_line say "frame B ... 45 borrowed joints (18 chosen, 14 ansatz, 6 measured inputs, 3 refuted, 2 unknown, 1 fitted, 1 forced only by the lane's word)" and "frame A: 10 rows claimed, 14 borrowed joints (11 chosen, 2 ansatz, 1 fitted)".
   Live checker (scripts/checks/inputs_scoreboard.py, plain run and --check, rc 0) prints: frame A "6 rows claimed, 14 borrowed joints [11 chosen, 2 fitted, 1 ansatz]"; frame B "23 rows claimed, 44 borrowed joints [18 chosen, 14 ansatz, 6 measured-input, 3 refuted, 2 unknown, 1 fitted]".
   The arc's own test (verification/test_b1834_*.py) asserts "10 rows claimed, 14" and "23 rows claimed, 44", which contradicts its own FINDINGS (45).
   Causes: B47 was verified at B1836 (45 to 44), and S305j (commit efd7fc758) changed frame A. Neither is recorded as a dated note in B1834 FINDINGS or arc_verdict. The "forced only by the lane's word" item has disappeared. The totals of 14 and 0 of 19 are unchanged. This is staleness, not an error at the time of writing.
2. FINDINGS says F7 "is typed VERIFIED-BY-MAIN". The committed build script and the test show F7 is now FORCED-BY-MAIN (T-FRAME-MIRROR, B1836), and the test docstring says so. FINDINGS carries no dated note.
3. verification/build_scoreboard_data.py reads the gitignored audit/scaffold/agy_joints.json, so it cannot be re-run from a clean checkout. The arc's real instrument is the checker plus docs/total_inputs_scoreboard.json, which do reproduce. Raw counts from the JSON (55 B joints incl. 7 FORCED, 1 VERIFIED, 8 measured, 4 refuted) differ from the checker's headline types. The checker evidently dedups or excludes shared joints and its logic was not inspected, so this is a note only. [Review 76, corrected for B1264's census lock: the count of 8 here is the agy lane's measured-input joints in the scoreboard, not B1264's census of measured instances.]
4. "52 in all" (sealed ranges): SEALED_EXHIBITS.json now has 145 entries. The arc test asserts >= 52, so it is fine, but no dated note.
- Checked and fine: "ten joints shared" (10 same_as links in each frame); "feed 16 or 17 of 23 rows" (B01, B02 at 17, B03-B09 at 16); identification price 13; the file contains no decimals; Seen first and Disclosed present and filled.
- Re-ran: checker --check, OK. The build script was not re-run (gitignored input).

## B1836 (seats past S300 verified): HOLDS WITH NOTES
Notes:
1. FINDINGS section 2 is still the placeholder "(filled at landing from its reader's report)". Yet claim_one_line says "the web seat's singlet screen, steepness map and doublet index verified", and the answer section says "THE DOUBLET INDEX: see section 2". No doublet-index result or committed output exists in the arc. The claim on the doublet index has no content behind it.
2. No committed instrument or output for these claims:
   - the web seat singlet screen "re-run once on main ... 1.5e-12, K0 holding";
   - "both [steepness] scripts byte-identical on main";
   - the physical-bridge lane checks (C4 x C8 algebra, Pin2 lattice, "eight controls unrun" is a negative);
   - the counts "Theorems 29-64, six commits", "23 ranges (75 exhibits)", the PMNS exposure listing.
   Reader D's compensator-slice run has no readers/D directory. A related run is readers/A/c_algebra_run.txt, but FINDINGS does not map it.
   The agy-lane facts (Theorem 41 criteria, Theorem 29 refutation, readers/B and readers/A runs) are committed and match.
3. "about 32 of B1834's 45 joints" uses the count that B1836 itself reduced to 44 (B47). Minor, and consistent with note 1 of B1834.
- Numbers all match their committed outputs:
  - Mirror: 0 of 16 violate; control 8 of 16; full identity 2.7e-15; controls 0.377 / 0.591 / 0.0638, so "0.06-0.59" holds.
  - T symmetry: 8.0e-13 over 80 keys.
  - Slope: 1101 slopes; gaps 1/20 versus 3/20 on 2/5 up; only 2/5 not all equal.
  - Theta2 branch: 1e-32 inside, 1.4 outside; the S304 sheet-law note matches p3_misc D3 in the B1838 arc.
  - Cohomology: dim H^1 = 1, H^1_cusp = 0 for k = 0-3.
  - Torsion: |T| = 2, 5, 6 at t = 1, omega, -1; 4/sqrt3 matches.
  - B08: exact L2 2.368751; offset -5.5e-4.
  - 2120 grid points: fermion-sign dV/dy is negative on all 2120 and has no stationary point.
  - P-635: H1 0 / 3 / H1_par 0.
  - P-636: minimal trace 3 is LR.
- Re-ran (outputs identical to committed): main/slope_gaps_exact, t_symmetry_compute, theta2_branch, readers/C c3_f7_mirror_proof_steps (81 s), c5_cuspidal_cohomology. c4_torsion_m004 matches except for a Plink/tkinter warning line on stderr. c2_b1667_l2_at_tau_golden exceeded 3 minutes and was killed (not reproduced).

## B1838 (the end): HOLDS WITH NOTES
Notes:
1. arc_verdict.json claim_one_line ends "next: the agy lane's zeta-regularised end judged, then the six re-read ..." but FINDINGS 2b/3 mark the zeta end as done (judged, not principled). The one-liner is stale.
2. FINDINGS 2b: "e^-L_max ... is between 0.5005 and 0.5257 ... e^-L2 0.062-0.101 ... 4.4e-16" matches s304_checks/p1_zeta_end_run.txt (GEO), which is correct. But "accurate to 0.6% at L2 and 35-38% off at L_max" and "B1667's canonical L2, small-cut: chi2_six 30.6 against L_max's 2.41; P-402" have no committed output in this arc. The S305c dated note concedes the 0.6 and 35-38% come from the web seat's run, not 54 points. The note also concedes that "the norm of no geometric cut" overstates what was shown (the title is not amended).
3. "At the exact norms the down and lepton m2/m3 fall from about 0.019 to about 0.012": the committed rows show small-cut 0.017-0.021 and exact 0.0115-0.0127 across rows A-D. This is approximate but acceptable.
4. "0.91-0.95 for channels 1 and i ... the same in all three sectors": the up sector has no channel i in the output (R1 and R3 up list only 1, j, k). The levels agree across sectors where present.
5. p595_diff_against_the_seats_output.txt: the diff shows only the runtime line (1784 s versus 891 s) and the trailing "exit 0" line, as stated.
6. "Seen first" and "Disclosed" are filled. The agy Theorem 81 and Stage 12-15 notes are dated notes that cite audit/ paths (gitignored, so not checkable from the tree).
- Table matches p595_exact_end_look_rerun_on_main.txt exactly (2.409 / 30.664 / 26.537; 2.658 / 39.149 / 25.868; 4.775 / 53.700 / 36.339; 4.924 / 40.831 / 35.323). The one-liner ranges (2.4-4.9; 31-54; 26-36) hold.
- Zeta numbers match: 72 cases, 2.5e-12, control 9.14, L 1.72 to 1.03, gamma - log 2.
- Spreads 0.1349 and 0.1365 match single_horocycle_test_run.txt.
- Re-ran: single_horocycle_test.py hit my 115 s cap with no output (too slow for the budget). Its committed output was read only. The P-595 look (about 30 min) was not re-run. s304_checks/p1_zeta_end.py was not re-run; it writes a json beside itself.
