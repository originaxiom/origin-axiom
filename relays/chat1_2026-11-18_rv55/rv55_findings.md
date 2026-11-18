# The seat's own reading of main's second reading (M55), 2026-11-18

Every unit of this seat's lane that was VERIFIED before M55's landing (1,961: the 1,101 still verified and the 860 that
M55 narrowed) was read against its record's ground, in eight packets built by `rv55_packets.py` (committed before it
was run), one reader per packet. Each reader read main's Markdown pages, run files and commit messages through the
mask, read main's scripts and JSON directly, and ran none of main's scripts. Two readers disclosed a slip of the mask,
each recorded under its packet; no unmasked figure enters a finding.

Kinds: UNDERSTATED, a narrowed unit whose figures and clauses a script or banked arc of main's does compute;
OVERSTATED, a unit held VERIFIED with a figure or clause its record's ground does not cover; MISFILED, a verdict of the
wrong kind under M55's own rule order, or a record's "how" or note that misdescribes the line or main's run.

Each row gives its evidence, in most rows a file and line of main's, read as the reader states. These are the readers' findings,
not yet each checked here: this seat checked twelve of them at source and the referee read sampled 31 more
(status page, § 16.2).

| packet | read | fine | understated | overstated | misfiled | undecided |
|---|---|---|---|---|---|---|
| 1 | 246 | 189 | 15 | 3 | 39 | 0 |
| 2 | 245 | 202 | 24 | 4 | 15 | 0 |
| 3 | 245 | 215 | 10 | 1 | 17 | 2 |
| 4 | 245 | 183 | 41 | 4 | 17 | 0 |
| 5 | 245 | 205 | 23 | 5 | 12 | 0 |
| 6 | 245 | 188 | 38 | 4 | 13 | 2 |
| 7 | 245 | 200 | 26 | 5 | 14 | 0 |
| 8 | 245 | 217 | 15 | 8 | 5 | 0 |
| all | 1,961 | 1,599 | 192 | 34 | 132 | 4 |

Packets 2, 5, 7 and 8 also name units they could not decide and counted them as fine. Packet 4 also has two findings
on records' own notes. Three units reached the readers cut at 1,200 characters by the packet builder (web-r80-01's lines
39 and 192; the first W-B2 note's line 1).

**Corrections after this list's referee read** (the status page, § 16):
- About 70 rows name no file and line of main's, giving reasoning, a record or a page instead. Among the UNDERSTATED
  rows: STATUS_CHAT1's 467, 509, 1045 and 1176; st8-05's 644, 649 and 650; and the R2S rows, which cite pages verbatim.
- Six UNDERSTATED rows hold only in part:
  - W-C3's line 101: its full-move and inversion clause is not run;
  - W-C3's lines 14 and 114: "exact", where B1675 works in floats;
  - THE_SCALE's line 148: to length 12 only;
  - st8-05's line 650: "M46 names" not checked;
  - STATUS_CHAT1's line 843: the hand reason is not run.
- Packet 2's row on STATUS_CHAT1's line 1231 is struck. It contradicts the status page's § 15.2, item 1.
- Packet 8's W-F22 line 38 row holds: the seat's line has 2.1 to 5.1, main's run's range; the record's 2.3 to 5.1 is
  no reading of the run.
- W-C3's n = 5 lines: see the status page's § 16.4.

## Packet 1
Units read 246 in 17 parent records; fine 189; not fine 57 (UNDERSTATED 15; OVERSTATED 3; MISFILED 39; of these 11 marked "low", a judgement call under M55's order).

Structural findings:
1. Deleted parents: web-wz1-01, web-r80-02, web-st-lists-02 are gone at 4921ee923; their companions say "the parent record's computation stands for what it names", so the register no longer says what main computed (wz1-01: Hecke at D = 5, volume to 3.9e-31; r80-02: main's planted cases of 2026-11-12, P-820, P-833; st-lists-02: main's closure check with "only at Higgs charge 0" — STATUS_CHAT1:68 went to NOTED).
2. Text printed as if computed: web_scale_census.py C4 prints the residue norm, |dz/z| = L/2 and the pointwise norm as fixed text (only the two Hitchin residuals computed); scale-01's how says horocycle 4 pi/L and K4e reproduce, in no script (nor B1650's). web_wf20_parity.py E3 prints a constant, but its record says "by hand" (fine).
3. Rule order applied unevenly: "rests on the referee or a cited result" (C) applied to THE_SCALE:180, :218 but not FINDINGS:78/88, THE_SCALE:60/62/182.

| unit | now | finding | evidence | suggested |
|---|---|---|---|---|
| the_scale/FINDINGS:27 | scale-01-r2p P | MISFILED (reason) | main residual 4.1e-14 (web_scale_census.py l.34, run l.1) beats 1e-9, 1e-6; only "SnapPy's own orientation reversal agrees" uncovered | P, that reason |
| the_scale/FINDINGS:32 | scale-01 V | MISFILED (how misdescribes) | horocycle 4 pi/L in no script/run; C4 l.46-49 computes eq1, eq2 only; norms l.49 fixed text; B1650 lacks it; same THE_SCALE:176 | V by hand, how says so |
| the_scale/FINDINGS:34 | scale-01 V | MISFILED (how misdescribes) | no script has K4e; C4 and B1650 nilpotent only | V by hand stated; else P |
| the_scale/FINDINGS:78 | scale-01-r2p P | MISFILED P->C | uncovered part Simpson's estimates (cited; THE_SCALE:180 is C) | C |
| the_scale/FINDINGS:82 | scale-01-r2p P | MISFILED (reason) | "1/2 everywhere" is b = 0 of run l.5; only uniformising-field clause uncovered | P, that reason |
| the_scale/FINDINGS:88 | scale-01-r2p P | MISFILED P->C | "the referee's catch, checked by hand" | C |
| the_scale/THE_SCALE:60 | scale-01-r2p P | MISFILED P->C | main's own reason: Simpson's estimates cited | C |
| the_scale/THE_SCALE:62 | scale-01-r2p P | MISFILED P->C | main's own reason names the referee's symbolic check | C |
| the_scale/THE_SCALE:116 | scale-01-r2n N | UNDERSTATED (lead) | "The weave sees k": 690 of 745 CS != 0 (l.32/35, run l.1); same at :47 kept V | V |
| the_scale/THE_SCALE:148 | scale-01-r2p P | UNDERSTATED | C2 checks 2n v3 on 745 (run l.3 "4.7517 (4 v3 = 4.0598)", 2.0299, 2.6667); e^{-0.034c} = (2.6667-2.0299)/(6 pi) = 0.0338 | V to length 12 |
| the_scale/THE_SCALE:177 | scale-01-r2p P | MISFILED (reason) | "dz/z grows like L/2" in run l.5; only "whatever the residue's normalisation" uncovered | P, that reason |
| the_scale/THE_SCALE:182 | scale-01-r2p P | MISFILED P->C | "(the referee, checked symbolically)" | C |
| the_scale/THE_SCALE:217 | scale-01 V | MISFILED (low) | G/l = 3/(2c) Brown-Henneaux cited; :218 same source is C | C |
| the_scale/THE_SCALE:290 | scale-01-r2n N | UNDERSTATED (lead) | T-ROOT run l.2-4 (0.2737/0.5019/0.6601; 32.4/6.6/4.7), l.11 footprint | V |
| the_scale/THE_SCALE:313 | scale-01-r2p P | MISFILED (low) | coset identification is literature cited at :315 (C); main computes arithmetic (C5) | C |
| the_scale/T_ROOT_FINDINGS:28 | scale-01 V | OVERSTATED | "Gueritaud-Futer holds, 0 violations" on 31,040: web_scale_troot_tsign.py has no GF check; census checks 745 only | P |
| the_scale/T_ROOT_FINDINGS:58 | scale-01 V | OVERSTATED | 0.024 (LLLLR/LRRRR), 0.017 (LLLRR/LLRRR) not in main's run (top six only, l.53/55, run l.11) | P |
| W-C1_REAUDIT:15 | wc1-02-r2p P | MISFILED (low) | no-commit check is the referee's; re-audit 7 another seat's run | C |
| W-C1_REAUDIT:128 | wc1-02-r2n N | MISFILED | finding is in the ground (three copies of Review 43's summary); only last sentence a proposal; lines 208/283/286 not named | P |
| W-C1_REAUDIT:133 | wc1-02-r2p P | MISFILED (low) | provenance line | N (or C) |
| W-C1_REAUDIT:137 | wc1-02-r2p P | MISFILED (low) | rests on the advisor seat's re-audit 7 sweep and plant | C |
| W-C1_REAUDIT:164, :167, :169 | wc1-02 V | MISFILED | requests ("For main"), answered in the parent; main notes 26 of 30 such lines | N |
| STATUS_CHAT1:748 | st9-01-r2p P | UNDERSTATED | web_wc8_part5_bronze.py l.26-37 (run l.1-6): b1 = 1, cusp rank 1, twisted duality, both ticks, levels 1-3 | V |
| STATUS_CHAT1:750 | st9-01-r2p P | UNDERSTATED | same run: failures without w golden 0/0/6, bronze 4/0/70 | V |
| STATUS_CHAT1:752 | st9-01-r2c C | MISFILED | review statement about main's record; right and acted on (web-wc8p5-01 note; web_section9_items.py I3, 56 of 56) | V |
| STATUS_CHAT1:772 | st9-01-r2p P | MISFILED | review statement; main acted (web-sel-05 holds 338, 357) | V |
| STATUS_CHAT1:782 | st9-01-r2p P | MISFILED | both clauses in main's records (web-sr-01 note; own note) | V |
| W-C5:45 | wc5-02-r2c C | MISFILED | "the ratio is 1" is the identity the ground verifies by hand (:41, :43 kept) | V |
| W-C5:53 | wc5-02 V | MISFILED (low) | bare lead-in | N |
| W-C5:70 | wc5-02-r2p P | UNDERSTATED | web_wc5_on_main.py l.32-34 (run l.4) exact on -40..40: finite at even a -8..0, infinite 2..8, control differing at even a >= 2 | V |
| W-C1(E2):45 | wc1-01-r2c C | MISFILED (reason) | image order 160 of 1920 in main's lock (tests/test_b734_m004_congruence.py l.113-120) and wz1 run l.6 | C, citing the narrative only |
| W-C1(E2):46 | wc1-01-r2p P | MISFILED (low) | rests on the seat's plant E2-1 and referee's spine check; lead in lock l.286-293 | C |
| W-C1(E2):47 | wc1-01-r2c C | UNDERSTATED | main's lock covers every shape: l.236-262, ROOT_PAGES l.157 incl. README | V |
| W-C1(E2):48 | wc1-01-r2p P | UNDERSTATED | lock l.296-300 asserts the withdrawn gloss in all three files | V |
| W-F20:23 | wf20-01-r2p P | MISFILED | provenance row; E1-E3 held by main's run | N |
| VIEW:184 | view-01-r2p P | UNDERSTATED | B1943 (PROVED): LR fixes exactly the four points of one order-5 line up to sign | V |
| VIEW:314 | view-01-r2p P | UNDERSTATED | "the act fixes two" is B1943; cusps are the ground's item (4) | V |
| W-F12:21 | wf12-01-r2p P | MISFILED | definition plus provenance; |T| column = part 2a's E2 in web_wc8_part2a_duality run l.7 | N |
| W-F12:23 | wf12-01-r2p P | UNDERSTATED | part 2a's G2, G3 (index 0 on 64, 2,662; gaps 4+4/3+3, 11+11/10+10) = web_wf12_on_main run l.1-2 | V |
| W-F12:29 | wf12-01-r2p P | UNDERSTATED | web_wf6_on_main.py G1 (run l.1) gap law levels 1-8; wf12 run l.1-3 extension characters 1 + (|T|-1), doublets = |T| x characters | V |
| STATUS_CHAT1:668, :669, :670 | st8-02-r2p P | MISFILED (low) | 0.15, 0.149, 2.959 are the seat's samples; current runs 0.123 (wb1 l.1), 0.0566 (wb1 l.3), 2.465 (wf5 l.5) | C |
| STATUS_CHAT1:714 | st8-02-r2n N | MISFILED | § 8.2 review finding, right and acted on ("both are seeded today"); like line :762 kept V | V |
| W-Z1:22 | wz1-01-r2p P | MISFILED (deleted ground) | parent web-wz1-01 gone; ground only in git at c458df8ce | P; restore ground |
| W-Z1:24 | wz1-01-r2p P | UNDERSTATED | web_section9_items.py I5 (run l.3): vol 2.029883212819307250042, ratio - 12 = -4.2e-45, beats seat's 4e-41 | V |
| W-Z1:44 | wz1-01-r2p P | UNDERSTATED | C1 at D = 5 in web_wz1_other_discriminants run l.1, l.6; B1917, B1920 carry Hecke twisted and shifted | V |
| W-Z1:89 | wz1-01-r2c C | MISFILED | nothing rests on the seat's run; main computed the period with constant 1 (run l.1, l.6); wb2-d1-04:95 kept V | V (or N) |
| W-Z1:91 | wz1-01-r2c C | MISFILED | main computed it: I5 (-4.2e-45), B1955 (3.9e-31) | V (or N) |
| REVIEW_81:36 | r81-01 V | OVERSTATED | "With '16 of 16' planted there, it passes" is the seat's plant; B1898 test l.269 checks "14 of 14" in STATUS_OF_THE_57.md; "15 lines of quotation" not in ground | P (or C) |
| REVIEW_81:37 | r81-01-r2p P | UNDERSTATED | 1,525 and 1,408 at 896cae025: frontier/B1898_.../verification/checks/sm_rows_probe.json, SM-18 | V |
| REVIEW_80:40, :42, :43 | r80-02-r2p P | MISFILED (deleted ground) | parent web-r80-02 gone; ground only in git at de4cec662 | P; restore ground |
| STATUS_CHAT1:68 | st-lists-02-r2n N | MISFILED | web_posthoc_closure.py run l.2, 4, 6-7: (2, 2, 1) closes for down and leptons in both models; deleted parent verified it with "only at Higgs charge 0" | V with qualification (or P) |

Mask: web_wb2_d1_run.txt's D1 residual hidden; wb2-d1-01:30 (kept V) judged on the record's 1.2e-33.

## Packet 2
Units read 245 in 17 records; fine 202; not fine 43 (UNDERSTATED 24: 20 now P, F25:101 and C8b:46 C, D1:92 and D1:93 N; OVERSTATED 4; MISFILED 15: 5 V by the review-section bullet, 5 wrong kind, 5 reason wrong with P standing).
Extra read: git show 34d71a24e:.../SUMMARY.json (main's JSON), confirming unit 1165's counts.

Stems: ST = STATUS_CHAT1; A3 = W-A3_THE_COVER...; F25 = W-F25_FRAME_CS_CUSP_EXPONENTS; F26 = W-F26_THE_CUSPS_MIXING...; C8a = W-C8_PART_2A...; C8b = W-C8_PART_5_THE_BRONZE_RIVAL; D1 = W-B2_FRAME_D1_IS_FRAME_C_AT_SHIFTED_CHARGES; C7 = W-C7_B1913...; F17 = W-F17_SECOND....

| unit | now | finding | evidence | suggested |
|---|---|---|---|---|
| ST:1176 | st13-01-r2p P | UNDERSTATED | review statement; every clause in web-wb2-d1-05r ("exactly (8.5e-32; the seat's 3e-8)", "a principle chosen, not a uniqueness proved"); siblings 1170-1178 V | V |
| ST:1221 | st13-01-r2p P | UNDERSTATED | every figure main's: web_wa2_readout.py l.1-5, 27-31; run l.1-8 (1.1e-15 to 1.7e-15); B1953 weyl_operator.py l.17 (BASES), l.58 (U_R from Y0^dag Y0) | V |
| ST:1227 | st13-01-r2p P | UNDERSTATED | seat's 3e-15 beaten: web_wa2_readout.py l.35; run l.1-8 |U_L - c U_R| 6.3e-16 to 2.2e-15 | V |
| ST:1228 | st13-01-r2p P | UNDERSTATED | main reran "real signed" (U_L(T)) in 8 cases (l.34; run l.1-8 True); run l.9 "orders (4, 2, 3): True; group order 24: True" | V |
| ST:1255 | st13-01-r2p P | UNDERSTATED | main's own record says it: web-p783-06p note; web_p783_spectrum_run.txt l.8-9 | V |
| A3:101 | wa3-05-r2p P | UNDERSTATED (moderate) | B1955 FINDINGS l.44-46; web-wa3-03r how "Verified on main (B1955): X Z = zeta Z X is the pairing" | V |
| A3:106 | wa3-05-r2p P | UNDERSTATED (moderate) | B1955 class_is_a_choice.py l.50-56, 64-65; run l.3 "a shear by 2"; web_review.py R2 run l.3 | V |
| A3:115 | wa3-05-r2p P | UNDERSTATED | R3 (cited): web_review.py l.7, 56-64; run l.6 (zeta^(j^2) under tau + 2, 8.0e-16), l.7 | V |
| A3:119 | wa3-05-r2p P | UNDERSTATED | B1955 wa3_on_main_run.txt l.4-5 rho(-I) = P both classes; FINDINGS l.68-70 | V |
| A3:121 | wa3-05-r2p P | UNDERSTATED | web_review.py docstring l.4-6, code l.40-52; run l.3 [[1, 0], [0, 3]]; web-st5-02 | V |
| F25:48 | wf25-02-r2p P | UNDERSTATED (lead) | B1945 FINDINGS l.31 "rates depend only on the point's first coordinate a"; table l.33-37 | V |
| F25:53 | wf25-02-r2p P | UNDERSTATED | web_wf24_wf25.py l.43-48 (asserts the +-2/5 row) | V |
| F25:55 | wf25-02-r2p P | UNDERSTATED | B1943 fixed_lines_run.txt l.1-2 (four points listed) | V |
| F25:101 | wf25-02-r2c C | UNDERSTATED | claim main's (parent how "up (3/5, 8/5) in S~, down (2/5, 13/10)"); provenance column as l.103, A3:168/173 (V) | V |
| C8a:30 | wc8p2a-01-r2p P | UNDERSTATED | web_wf6_on_main_run.txt l.1-2; B1926 odd_ticks_no_modules.py l.2-6, run l.2-9 | V |
| C8a:32 | wc8p2a-01-r2p P | UNDERSTATED | web_section9_items.py l.48-54 (run l.2); B1926 run l.2-9; same verdict C8b:21 V | V |
| C8a:33 | wc8p2a-01-r2p P | UNDERSTATED | B1926 run l.2-3; web_wf4_on_main_run.txt l.2 | V |
| C8b:22 | wc8p5-01-r2p P | UNDERSTATED | web_wf4_on_main_run.txt l.11; web_wc8_part5_bronze_run.txt l.4 | V |
| C8b:28 | wc8p5-01-r2p P | UNDERSTATED | B1926 run l.2-4; bronze run l.1-3 | V |
| C8b:46 | wc8p5-01-r2c C | UNDERSTATED | reason "levels 5 and 7 not covered" wrong: web_wf6_on_main_run.txt l.2 (golden 1, 3, 5, 7), l.6 (bronze) | V |
| D1:35 | wb2-d1-02-r2p P | UNDERSTATED | seat's residuals 1.2e-15 to 7.8e-15 beaten by main's 4.7e-16 (D2; web_wb2_d1.py l.61); lines 43, 52 kept by same rule | V |
| D1:36 | wb2-d1-03-r2p P | UNDERSTATED | seat's bound "above 1e-3" met by main's D5 (l.82-84): distance 0.70, at least 8 % | V |
| D1:92 | wb2-d1-02-r2n N | UNDERSTATED | ledger row's claim is main's D3 (1e-15 beats 6e-15; run l.5); row 96 V | V |
| D1:93 | wb2-d1-02-r2n N | UNDERSTATED | ledger row's claim is main's D2 (l.61) | V |
| F26:30 | wf26-01 V | OVERSTATED | "at heights 6 and 8" not in ground; main compares at 8 and 12 only (web_wf26_on_main.py l.37) | P |
| F26:45 | wf26-01 V | OVERSTATED | "5e-6 to 2e-5 at the mark" at 12: main 2.6e-6 to 2.0e-5 (run l.1-4) | P |
| C8a:35 | wc8p2a-01 V | OVERSTATED | "and every recipe module" not covered: duality on characters only (web_wc8_part2a_duality.py l.6-7; run l.1-6); I3 bronze level 2 only | P |
| D1:71 | wb2-d1-03 V | OVERSTATED | its W-B1 clause is the clause M55 narrowed in the first W-B2 note's line 85; ground (D5) names only that the sign does not act as the reading | P, or restore line 85 |
| ST:1167 | st13-01-r2p P | MISFILED | the seat's own recut and hash check: rests on the seat's run (as F26:42, C8a:67) | C |
| ST:1231 | st13-01-r2n N | MISFILED | item 3's conclusion about main's record; right and acted on (web-st13-01 how; web_section13_run.txt l.2) | V |
| ST:1243 | st13-01-r2p P | MISFILED | every clause in main's note; figures quoted from the seat's lines 48, 64 (web-wb2-first-02p) | V |
| ST:1251, :1252 | st13-01-r2p P | MISFILED | main's half is its run (l.8, l.9); seat's half quoted from P-783 lines 80, 81 | V |
| ST:1256 | st13-01-r2p P | MISFILED | every clause in main's note (web-p783-06p) | V |
| A3:92 | wa3-05-r2p P | MISFILED | a definition (standard Weil representation); B1955 FINDINGS l.25-26 | N |
| F25:49 | wf25-02-r2p P | MISFILED (reason) | reason misreads E = 2k (line's 1 and 2 are the ground's 1/2 and 1); only 1.85-1.92 not main's | P, reason corrected |
| F26:44 | wf26-01-r2p P | MISFILED | the referee's comparison on its own run, as line 42 (C) | C |
| C8a:59 | wc8p2a-01-r2p P | MISFILED (reason) | 4 + 4, 36 + 36, 244 + 244 in web_wf9_on_main_run.txt l.1, 3, 5; only firing law and the h1 gap +-2 at level 4 not main's | P, reason corrected |
| C8b:23 | wc8p5-01-r2p P | MISFILED (reason) | "8 of 54" in web_wf6_on_main_run.txt l.6, bronze run l.5; "sum to 0" arithmetic; only the firing law on 56 not main's | P, reason corrected |
| C8b:25 | wc8p5-01-r2p P | MISFILED (reason) | cone points run at golden 1, 3, 5 and bronze 1 (web_wf4_on_main.py l.7-8, 14; run l.4, 7, 10, 13); level 2 and bronze 3 not covered | P, reason corrected |
| C7:16 | wc7-01-r2p P | MISFILED (reason) | |cz + d|^4 law in B1913's run (l.4-5, 7-8); only the seat's 2.8e-30 not beaten | P, reason corrected |
| ST:333 | st5-03-r2p P | MISFILED | provenance about W-A3 lines 76, 86, correct by reading; line 323 same kind V | N (or V as 323) |
| F17:156 | wf17-06-r2p P | MISFILED | main's own reason calls it a "provenance claim"; its r2n rule files those N | N |

Could not decide: ST:1324 (C, 8e-28): agyexp_x_foundation.py F5 prints a worst residual, run l.8-14 masked. D1:126, 127 (V, unit-weight controls 5.3e-15, 1.1e-15): left fine; D4 run lines masked.

## Packet 3
Units read 245 in 18 parent records; fine 215; not fine 28 (UNDERSTATED 10; OVERSTATED 1 minor; MISFILED 17); undecided 2.

| unit | now | finding | evidence | suggested |
|---|---|---|---|---|
| wa2-08:122 | -r2p P | UNDERSTATED | old ground cites B1935 § 3 and B1952 part F; channels level 2 and Higgs level 8 on B1952 FINDINGS 13-14; part D eighths wa2_on_main.py:104-105 (run line 5: 0.125, 0.375, 0.875) = B1935 higgs_triplet_level_run.txt line 1; blocks level 2 or 4: wa2_on_main.py:103 (run line 4), :148 (run line 12); B1952 FINDINGS 40-41; web_wa2_readout.py:38 (run 1-9) | VERIFIED |
| wf19-02:64 | -r2p P | UNDERSTATED | web_wf19_on_main.py:56-65, run line 9: golden level 4, formula on all 12 record modules, I = +1, 0, -1 on 4 each; in web-wf19-01's ground | VERIFIED |
| wf19-02:80 | -r2n N | UNDERSTATED | bold lead "Restriction is injective in degree 1" held as heading; parent ground names injectivity among proof steps main read; sibling lead 84 kept | VERIFIED |
| wh1-01:54 | -r2p P | UNDERSTATED | scripts/checks/harvest_debt.py:591 ages only new unrowed seat-index ids; 852-861 fail on unrowed relays only under --strict; file changed by comments only f2f019621..4921ee923 | VERIFIED |
| rv-06:228 | -r2n N | UNDERSTATED | bold lead states § 3.3 item; item right and acted on (B1955 FINDINGS 80-84); review rule keeps; headings 244, 254 kept on same rule | VERIFIED |
| p783-04:44 | -r2p P | UNDERSTATED | golden state R0 is B1912 banked (FINDINGS 10-15, 51: R0 = pi/(2 ln phi) = 3.2642513026 in (sine, -1)); cell is web_p783_spectrum.py P2, run line 2 | VERIFIED |
| p783-04:47 | -r2p P | UNDERSTATED | pi/ln phi is B1912's own control (FINDINGS 44-45, 53: 2R0 = 6.5285026 in (cosine, +1)); scan2.py:2; P2 run line 2 | VERIFIED |
| rv-05:210 | -r2n N | UNDERSTATED | lead "'0.17 to 0.72' mixes two measures" states a finding; web-wa1-03's ground says the same; web_wa1_h2.py:16 (run 1-4) computes both | VERIFIED |
| rv-05:220 | -r2p P | UNDERSTATED | passing triples (2, 1, -1), (3, -1, -1): web_wa1_reps.py:34-35, run lines 1-2; web-wa1-11's ground names both | VERIFIED |
| wf14-01:18 | -r2p P | UNDERSTATED | parent ground: "the non-abelian factors are untouched"; shared SU(2) action web_wf13_algebra.py:18, run line 2 (H2 1.3e-15), web-wf13-01's ground | VERIFIED |
| wc4-02:27 | VERIFIED | OVERSTATED (minor) | "81 elements a + b sqrt-3, |a|, |b| <= 4" is the seat's enumeration, not in ground nor web_wc4_theorem_c.py; ground holds the claim by |Gal| = 2 | PARTIAL |
| wh1-01:16 | -r2c C | MISFILED | status label; nothing rests on a run | NOTED |
| wh1-01:17 | -r2c C | MISFILED | main's reason calls it a scope line; its claim is in the parent ground | NOTED |
| wh1-01:12 | -r2p P | MISFILED | seat's procedure; method lines 7, 10 are C | CONDITIONAL |
| wh1-01:41, 42 | -r2p P | MISFILED | per-seat rows of the seat's 114 (main 116); same figures at 23, 36 are C | CONDITIONAL |
| wh1-01:46 | -r2p P | MISFILED | pointer to a seat file (file list) | NOTED |
| wh1-01:47, 48, 49, 51, 52 | -r2p P | MISFILED | rest on the seat's lookups through its mask (the ground making line 10 C) | CONDITIONAL |
| wh1-01:56 | -r2p P | MISFILED | dates from the seat's run; the 114 is C at 36 | CONDITIONAL |
| rv-06:246, 248 | -r2p P | MISFILED | main's reason "about outside preprints" = cited result; B1955 FINDINGS 104 "Not verified by main: the preprints" | CONDITIONAL |
| p783-04:64 | -r2p P | MISFILED | wholly about the seat's run (failed second refinement, +-0.004 bracket) | CONDITIONAL |
| wf13-01:12 | VERIFIED | MISFILED (minor) | a convention (definition); wf19-02's definitions 30-32 NOTED | NOTED |
| thr-01:162 | VERIFIED | MISFILED (minor) | definition or provenance line of the sealed run | NOTED |

Undecided:
- wa2-05:28 (PARTIAL): if "the triplet's permutation parts generate S3" means the generation blocks, web_wa2_readout run lines 1-9 compute it (UNDERSTATED); in the card's cell "the triplet" is the Higgs-direction stand-in, for which main has only T (B1724 covariance.json part_a); no main computation of S on it found.
- p783-04:54 (PARTIAL): 3 pi/(2 ln phi) = 3R0 matches 9.7927539079 to ten digits (reader's arithmetic); web-p783-04r's ground calls the three single values dihedral; no script of main's names 3R0.

Observations (verdicts unchanged):
- thr-01:40 rightly PARTIAL; the seat's "run of five" is not exact: 14 threads of length 2 to 8 have a run of five or more equal letters; 10 above height 3 (main's ten, web_thread_table_run.txt line 3); four below 3 (LLLLLRR, LLRRRRR at 2.958; LLLLLRRR, LLLRRRRR at 2.814).
- st6-01:376 ("0.40 in every case") visible for two rows only of web_review_run.txt; st6-01:380 ("exactly") on masked lines 1-2 of wb2_stage3_on_main_run.txt; counted fine since grounds name the run files.

## Packet 4
Units read 245; fine 183; not fine 62 (UNDERSTATED 41: wc3-01 22, st8-01 6, st10-01 4, sel-01 3, rv-02 2, wa3-04 2, wf25-03 1, r79-01 1; OVERSTATED 4; MISFILED 17) plus 2 record-level findings.

Short names: W-C3 = W-C3_THE_SM_SEATS_ITEMS_UNDER_BANKED_ARCS; ST = STATUS_CHAT1; SEL = chat1_2026-10-14_selection/THE_SELECTION_PRINCIPLE; R79 = REVIEW_79_CHAT1. B1675mc = frontier/B1675_.../verification/main_check/v2_w34_independent.py (+ _run.txt). B1679r = frontier/B1679_.../verification/received/ (the SM seat's W108, W109 scripts, rerun by main from extracted copies, "reproduce exactly", B1679 FINDINGS l.14). B1690v = frontier/B1690_.../verification/.

| unit | now | finding | evidence | suggested |
|---|---|---|---|---|
| W-C3:14 | wc3-01-r2p P | UNDERSTATED | B1675mc l.122, 131-137, 166; run l.1 table (3,3,3,0), (5,7,3,4), (7,8,6,2); l.6-8 joint actions keep 0; l.9-11 L 1, R 1, P 2 at rank 3, P 3 at rank 4; l.13 0 threads; "exact" is the seat's method (main in floats) | V |
| W-C3:20 | wc3-01-r2p P | UNDERSTATED | B1690v/main_w81_w83.py l.21-33, 54-57; json 72, 30, A5 true, Y dims 0/1/8 | V |
| W-C3:57 | wc3-01-r2p P | UNDERSTATED | B1676 tick_on_the_weave_main.py l.50, 54; run l.4 0.0799 and 3.1 % | V |
| W-C3:58 | wc3-01-r2p P | UNDERSTATED | B1676 FINDINGS l.39; main_w81_w83.py l.50, 68-69 commutant dim 1, order 96, norm 1.0 | V |
| W-C3:69 | wc3-01-r2p P | UNDERSTATED | B1679r/the_icosahedral_common_point.py l.313-319; run l.1 order 120, centre 2, 76 subgroups, maximal 10x12, 6x20, 5x24, |Aut| 120, |Inn| 60 | V |
| W-C3:72 | wc3-01-r2p P | UNDERSTATED | same, run l.2 (Q8, n = 2): 1 fixed class under full and LR, traces (0,0,0) | V |
| W-C3:73 | wc3-01-r2p P | UNDERSTATED | same, run l.4: three move sets, fixed 0/0, orbits [40, 36] | V |
| W-C3:74 | wc3-01-r2p P | UNDERSTATED | same, run l.5: full and trans, 0 classes, 0 characters fixed | V |
| W-C3:75 | wc3-01-r2p P | UNDERSTATED | same, run l.3: 0 fixed, one orbit [14] | V |
| W-C3:76 | wc3-01 V | OVERSTATED | "and the R_ij alike" not covered: W108 run l.5 has the orbit under full and trans only | P |
| W-C3:78 | wc3-01-r2p P | MISFILED (low) | the seat's implementation detail (Hamilton-product ordering) | C |
| W-C3:83 | wc3-01-r2p P | UNDERSTATED | B1679r/the_record_count_for_every_n.py C3 (l.206-227, sympy), run l.3 [(0,0,0), (2,2,2)]; main_search.py l.41-43, run l.2; B1679 FINDINGS l.33 | V |
| W-C3:101 | wc3-01-r2p P | UNDERSTATED | B1682 main_kept_words.py l.131-158, 183-190; run l.2 six classes [a,b]^{+-1,+-2,+-3}, kept by R, L and 4 transvections; "full moves up to inversion only" is B1682 theorem (ii) (FINDINGS l.35), stated not run | V |
| W-C3:102 | wc3-01-r2p P | UNDERSTATED | B1689 main_w24.py l.28-29 (main_w24.json: only critical point at kappa = -2 is (0,0,0)); B1682 FINDINGS l.36 | V |
| W-C3:114 | wc3-01-r2p P | UNDERSTATED | B1675mc l.122, run l.1 | V |
| W-C3:115 | wc3-01-r2p P | UNDERSTATED | B1675mc l.131-133, run l.6-8 | V |
| W-C3:116, :117 | wc3-01-r2p P | UNDERSTATED | B1675mc l.135-137, run l.9-11 | V |
| W-C3:119 | wc3-01-r2p P | UNDERSTATED | B1675mc run l.14: block 1 718 + 40 = 758, block 2 450 + 132 + 40 = 622, block 3 758 | V |
| W-C3:121 | wc3-01-r2p P | MISFILED (low) | random SL(2, Q) control is the seat's planted control | C |
| W-C3:126 | wc3-01-r2p P | UNDERSTATED | B1689 main_w24.py l.18, 30, 39, 66: L's linear part (x, z, -y); K1 group of order 24 | V |
| W-C3:128 | wc3-01-r2p P | UNDERSTATED | B1675mc run l.14 (all 758 keep a line in block 1); web-wc3-02's ground cites this | V |
| W-C3:129 | wc3-01-r2p P | UNDERSTATED | B1675mc run l.14 718 and 40; FINDINGS l.40-43 corrected (web-wc3-02) | V |
| W-C3:142 | wc3-01-r2p P | UNDERSTATED | main_w81_w83.py l.21-33; json 72, 30, 5 simple roots, A5 true | V |
| W-C3:143 | wc3-01-r2p P | UNDERSTATED | main_w81_w83.py l.54-57; Y dims 0, 1, 8 | V |
| W-C3:145 | wc3-01-r2p P | MISFILED (how) | two of three controls main's (main_w76.json LR not LLR; main_w81_w83.json order 96, norm 1); only "126" uncomputed | P, reason "126" |
| ST:983 | st11-01-r2p P | MISFILED | provenance row (cf. W-C3:110, W-F17:206) | N |
| ST:986 | st11-01-r2p P | MISFILED | every figure in the named output relays/chat1_2026-11-18_rv49/rv49_checks_out.txt l.2, 3, 7; ST:985 same footing kept | V |
| ST:613 | st8-01-r2p P | UNDERSTATED | UNITS.json 24 web files at 5dec726d6, 136 at c458df8ce (112 new); 108 in web-st7-04's note | V |
| ST:615 | st8-01-r2p P | UNDERSTATED (how wrong) | ground names "87 files read"; "about 4,370" in web-st7-04's note (4,369 at c458df8ce) | V |
| ST:619 | st8-01-r2p P | UNDERSTATED | web_wz1_c3_indices_run.txt l.4-10: 6, 1, 12, 6, 1, 12, 12 | V |
| ST:622 | st8-01-r2p P | UNDERSTATED | records at c458df8ce: nine -p splits totalling 34 units | V |
| ST:625 | st8-01-r2n N | MISFILED (low) | item 6 of ten, right and acted on; items 1-5, 7-10 kept; only the last sentence is the seat's acceptance | V |
| ST:629 | st8-01-r2p P | MISFILED (how) | counts 6, 1, 6 and two out-of-order pairs main's (custody_chat1_web_seat_run.txt l.1-3); only the explanation the seat's | P, reason narrowed |
| ST:657 | st8-01-r2p P | UNDERSTATED | web_wf19_on_main_run.txt l.2 (64), l.8 (54942) | V |
| ST:659 | st8-01-r2p P | UNDERSTATED | web_wf22_on_main.py l.33, run l.4 (7.7e-11, 8.2e-10, 5.7e-05; 3.2, 1.8, 4.9); B1922 FINDINGS l.36 | V |
| SEL:130 | sel-01-r2p P | UNDERSTATED | B1646 FINDINGS l.1, 39: D4 holds (cone or real locus, never between) | V |
| SEL:131 | sel-01-r2p P | MISFILED | lead-in to a list | N |
| SEL:243 | sel-01-r2p P | UNDERSTATED (moderate) | ground and web_selection_exact.py E2 (l.5-7, run l.2): residual act is W mod 2's own action | V |
| SEL:244 | sel-01-r2p P | MISFILED (low) | a definition (the monodromy) | N |
| SEL:245 | sel-01-r2p P | UNDERSTATED | B366 FINDINGS l.12-14; web_selection_exact.py E2, run l.2 | V |
| ST:33 | rv-02-r2p P | MISFILED | status row recording the seat's withdrawal of a figure | N |
| ST:41 | rv-02-r2c C | UNDERSTATED | web_review.py R3 (l.56-64), run l.6: zeta^(j^2) under tau + 2 at 8.0e-16; main acted (as ST:38, :48 kept); how mislabels it "the other seat's own script" | V |
| ST:43 | rv-02-r2c C | UNDERSTATED | same R3, run l.6: psi(-jk)/sqrt 5 at 1.9e-15 | V |
| ST:523 | st7-04 V | OVERSTATED (minor) | "six-cell", "of 2026-10-06" not in ground; hold on the ledger at 7022a9dae (rows 879-885) | widen ground, or P |
| ST:524 | st7-04-r2p P | MISFILED | right when written (24 web files at 7022a9dae); main acted by taking in 108 files | V |
| W-A3:66 | wa3-04-r2n N | UNDERSTATED (lead) | states the computed result the ground names (wa3_on_main.json frame_lines 0.2) | V |
| W-A3:76 | wa3-04-r2c C | MISFILED | main recomputed it: R4, run l.8-9; only the seat's corrected sign differs | P (sign) |
| W-A3:79 | wa3-04-r2p P | UNDERSTATED | web_review.py R2, run l.1-5: four Weil classes, a linear map, identification unique up to a scalar | V |
| W-A3:81 | wa3-04-r2n N | MISFILED | content is the ground verbatim plus R2 (diag(1, 3) inverse of the seat's diag(1, 2)); web-wa2-05v keeps [J] lines main computes | V |
| W-A3:84 | wa3-04-r2c C | MISFILED (low) | as :76: R4/R5 (run l.8-15) with opposite signs | P (signs) |
| W-F11:21, :23, :24 | wf11-01-r2p P | MISFILED | definitions main's script adopts (web_wf11_on_main.py l.4-6, 43-54) | N |
| W-F25:42 | wf25-03 V | OVERSTATED | held ends 1.5/2.25/3.0, "four digits", the referee's 0.2 are the seat's; same kind :122 made P | P |
| W-F25:126 | wf25-03-r2p P | UNDERSTATED | web_wf24_wf25.py F3 l.43-49: B1945's rate 4/5 gives 8/5; run l.5 "True" | V |
| ST:923 | st10-01-r2p P | UNDERSTATED | UNITS.json at 5d4fd32fe: 28 units; web-cold-01 N with 26; web-st7-06's note | V |
| ST:927 | st10-01-r2p P | UNDERSTATED | B1937 FINDINGS l.114 ("byte for byte") | V |
| ST:928 | st10-01-r2p P | UNDERSTATED | UNITS.json at 5d4fd32fe: 7,294 web units | V |
| ST:933 | st10-01-r2p P | UNDERSTATED | 42 ids changed a5e967af9 -> 5d4fd32fe; 41 held by web-st8-01..06, web-st-log; 42nd is line 1 (no record) | V (note line 1) |
| R79:21 | r79-01-r2p P | UNDERSTATED | B1882 card/v1_null_run.txt l.23, 39, 55 (0.06/0.08/0.08); l.29 (12, 0.0667, 0.18); l.34, 45, 50, 61, 66 (five cells below 0.1); l.46, 51, 62, 67 (2.08-2.36) | V |
| W-A2:110 | wa2-05v V | OVERSTATED | phase e^(i pi/4) not read out (web_wa2_readout.py run l.1-9: "real signed up to one phase" only); B1724/B1935 premise cited, not computed | P (the phase) |

Record-level: web-wc3-01's note says "n = 5 to length 6 in W110 ... not rerun on main", but B1682 main_kept_words.py l.183, run l.5 ran it (102,528 classes, 0 kept): correct the note. web-wa3-04's how puts the trace signature under class_is_a_choice.py; it is wa3_on_main.py part D l.127-132 (floats).

Noted only: W-F11:37 (H3's matrix masked; conjugacy to LR uncomputed; P stands); W-C3:59 (906 in ground and B1676 FINDINGS l.29, no script computes it); W-C3:118 (P right: main ran only the first 200 states, run l.15); web-wa2-05v:187 status row kept V while web-wa3-04:169 same kind N; W-F17:173 (order 4 by hand, no script; P left); W-C3:19, :141 (P right: main's largest |CS| 5.55e-14).

## Packet 5
Units read 245 in 18 records; fine 205; not fine 40 (UNDERSTATED 23, three bold leads; OVERSTATED 5; MISFILED 12).

Mask disclosure (the reader's): before switching to the mask it grepped a few Markdown lines directly: docs/HARVEST_LEDGER.md lines 19, 30 and 1367, and WORKING_RULES.md lines 524-525. The WORKING_RULES lines read the same through the mask; the HARVEST_LEDGER lines hide digits under the mask, and none of those figures is used. No script of main's was run; nothing compared with data.

| unit | now | finding | evidence | suggested |
|---|---|---|---|---|
| W-F18:148 | wf18-01-r2c C | MISFILED | a "Fix:" proposal; nothing rests on the seat's run; ten other Fix lines NOTED | N |
| STATUS:153 | rv-03-r2p P | UNDERSTATED | web_wa1_rest.py l.67-73 (item 6), run l.8-9: |a3|/|a1| = 9.4e-42, S-law 7.4e-39; web-wa1-02's ground names it | V |
| STATUS:170 | rv-03-r2p P | UNDERSTATED (lead) | B1955 wa3_on_main.py l.51-53 (no map onto D25, run l.1); l.125 (det 1); l.138-143 part F; run l.8 masked; B1955 FINDINGS § 3 l.73-84 | V |
| STATUS:159 | rv-03 V | OVERSTATED | status row "H2 is PARTIAL (web-wa1-03)"; web-wa1-03 is SUPERSEDED | N |
| R2S:33 | r2-01-r2p P | UNDERSTATED | B151 FINDINGS l.35 has the Dimofte row verbatim; ground: "quotations of main's record are exact" | V |
| R2S:40 | r2-01-r2p P | UNDERSTATED | u = sqrt(1 - l^2) in ground; B1012 dated note l.73-75; B1851 relay_facts.py l.28-33, run l.1 | V |
| R2S:41 | r2-01-r2p P | UNDERSTATED | B1012 l.75, l.79-80 verbatim; TERMINOLOGY l.317-320 | V |
| R2S:43 | r2-01-r2c C | MISFILED (low) | same absence claim as l.23 (V); B151's reading "is the record's"; P-719 adopts | V, or l.23 C too |
| R2S:56 | r2-01-r2p P | UNDERSTATED | THE_SCALE_CARD_DESIGN_P722.md l.89, 91, 95-96, verbatim | V |
| R2S:68 | r2-01-r2p P | UNDERSTATED | same page l.86-88 verbatim | V |
| R2S:86 | r2-01-r2p P | UNDERSTATED | B1034 dated note l.84-85; P-731 (POINT_REGISTER l.944); B1851 part A | V |
| R2S:87 | r2-01-r2p P | UNDERSTATED | B1034 l.82-88 "in tension, and neither is derived ... sigma = t ... P-731 carries them" | V |
| R2S:88 | r2-01-r2p P | UNDERSTATED | B1034 l.1, l.49 (UNDECIDED); l.46 ("a ratio") | V |
| R2S:92 | r2-01-r2p P | MISFILED | the seat marks the clause "a pointer and not a claim" | N |
| R2S:96 | r2-01-r2p P | UNDERSTATED | P-719's row (POINT_REGISTER l.932) and its S306n dated note | V |
| W-A1:35 | wa1-01 V | OVERSTATED (low) | "m = 2" not in main's run; web_wa1_rest.py run l.1 gives k in [3] for c = 1; reader's own check: m = 2 at c = 4 | P, or run c = 4 |
| W-A1:44 | wa1-01 V | OVERSTATED | exp(2 pi i Y) = diag(...), det 1, Z6 clause printed nowhere; D4 prints only 9 + 4 - 1 = 12 (run l.5); main narrowed Z6 at l.61 | P, or add to D4 |
| W-A1:46 | wa1-01 V | OVERSTATED (ground gap) | D6 prints only sum Y, sum Y^3; SU(3)^2 Y, SU(2)^2 Y in B1952 wa2_on_main.py l.123 (run l.7), not named in this ground | V once named |
| W-A1:65 | wa1-01-r2p P | UNDERSTATED | B1951 FINDINGS l.18-19; D5 counts 1 + 10 + 5 (run l.6-11); B1936 § 1 l.26 | V |
| W-A1:76 | wa1-01-r2p P | UNDERSTATED | D5; B1951 l.70 | V |
| W-A1:77 | wa1-01-r2p P | UNDERSTATED | web_wa1_rest.py l.46, run l.3: FS +1, image of order 60 on the 3; D4; B1951 l.71-72 | V |
| W-A1:81 | wa1-01-r2p P | MISFILED (how) | how says the triplet's -2 "only partly covered"; D7 prints [-2, 3] (run l.13); only Lambda^3 + Lambda^5 uncovered | P for those, how corrected |
| STATUS:1059 | st12b-01-r2p P | UNDERSTATED | web_section9_items.py l.47, run l.1 "56 modules ... on 56 of them"; same run backs l.1062 (kept) | V |
| ZERO_FREE:25 | zf-01-r2p P | UNDERSTATED | B1700 FINDINGS l.10-15 (the_units_sheaf.py), run l.1-2: R and dR line orders [1, -1, 3]; v+- are D3 | V |
| ZERO_FREE:15 | zf-01-r2p P | MISFILED (low) | rests on the seat's W133 check of another seat's rule | C |
| FRAMING:87 | zf-01-r2p P | MISFILED | points to § 5 "[READING, informed]"; note typed "A READING" (l.3) | N |
| FRAMING:106 | zf-01-r2p P | MISFILED | § 1 "[READING, from the code]"; first sentence is D5 | N |
| FRAMING:241 | zf-01-r2p P | MISFILED | row of § 5 "[READING, informed]" | N |
| W-C6P2:18 | wc6p2-01-r2p P | UNDERSTATED | 4.9e-7 on 24 cases: B1919 FINDINGS l.18-20 (seat_formula_24.py); ground names 1.4e-11 | V |
| W-C6P2:20 | wc6p2-01-r2p P | UNDERSTATED | B1921 FINDINGS l.3, l.16 ("1.9 x 10^-9", nine cases); l.21 kept | V |
| W-C6P2:40 | wc6p2-01-r2p P | MISFILED (low) | wholly the seat's C1 and post hoc 3 | C |
| W-A2:26 | wa2-03-r2p P | UNDERSTATED | web_review.py R2 l.40-54, run l.1-5 print diag(1, 4) and the swap; M_-I = M_S^2 = -1 | V |
| W-A2:46 | wa2-03-r2n N | UNDERSTATED (lead) | B1952's banked title and part B: wa2_on_main.py l.62, run l.2; FINDINGS l.45-47 | V |
| W-A2:182 | wa2-03-r2c C | MISFILED | web_review R2 (run l.1-5) recomputes four classes and both orderings; rows 180, 185, 186, 188 V | V (or N like W-A3:165) |
| W-A3:49 | wa3-02-r2n N | UNDERSTATED (lead) | B1955 banked title; wa3_on_main.py B, run l.2 | V |
| W-A3:28 | wa3-02 V | OVERSTATED (low) | phi([a,b]) = (aba)[a,b](aba)^-1 and meridian (aba)^-1 t are the seat's presentation; main narrowed l.26 | P |
| W-F1:29 | wf1-01-r2p P | UNDERSTATED | ground has chi = 1/k - 1/2, negative from 3; web_wf1_on_main.py l.47, run l.8 | V |
| W-F1:28 | wf1-01-r2p P | MISFILED (how) | how says "A1 to A5"; script has no A3 (run l.1-9: A1, A2, A4, A5); fact holds by hand | P stands; how corrected |
| REVIEW_79:69 | r79-02-r2p P | UNDERSTATED | WORKING_RULES.md l.524-528 (masked read): "111 rulings" and Review 79's note the parts "did not add to the 111"; 81 + 16 + 11 = 108 | V |
| W-B2_FIRST:1 | wb2-first-01-r2p P | MISFILED | withdrawal banner (status row); "referee results not sealed here" out of date: web_wb2_d1.py D1, D3 (run l.5; l.4 masked), D5, D6 recompute | N, or restore naming web_wb2_d1.py |

Undecided, left to main: W-F18's 17 kept lines under O1-O10 (typed "a reading, for main"; kept under rule 6 since B1937 confirmed each; quotes exact through the mask); W-C2:114 (in § 5's requests; figures B1939's torsion_census_run.txt l.5; N defensible); typed-table rows inconsistent (W-A2:188 V; W-A3:165, W-F24:86 N; W-A2:181, 182, 184 C); STATUS:174-175 premise rows N while siblings V (defensible).

## Packet 6
Units read 245 in 18 records; fine 188; not fine 55 (UNDERSTATED 38; OVERSTATED 4; MISFILED 13: 11 kind, 2 reason); undecided 2.

| unit | now | finding | evidence | suggested |
|---|---|---|---|---|
| wf21-01 L32 | r2p P | UNDERSTATED | B1937 FINDINGS l.31-33 (masked) lists both minor items (the ground's "B1937's table"); W-F18 l.150-153 names them | V |
| wf21-01 L33 | r2p P | UNDERSTATED | moduli sigma credited to B1735: B1937 FINDINGS l.32; BIG_RUN_RULE_v2.md l.40; big_run_look_v2.py l.50 | V |
| wf21-01 L34 | r2p P | UNDERSTATED | big_run_look_v2.py l.83-84; FINDINGS l.33 | V |
| wf21-01 L36 | r2p P | UNDERSTATED | indices (0,1,2,3,6,7,8), N_CAL 4,000, seed 20261115: big_run_look_v2.py l.31, 33-34; B1932 big_run_look.py l.21 same | V |
| wf21-01 L41 | r2p P | UNDERSTATED | ground names the caveat on O4 (A15); rule l.150 names a29c459a5; git file list of a29c459a5 has rule, script, run together; "committed unread at 48926341b" is main's (FINDINGS l.55) | V |
| wf21-01 L62 | r2p P | UNDERSTATED | v1 rule l.55; v2 rule l.89, FINDINGS l.28; DATA/SHA pins identical v1 l.14-17, v2 l.20-23 | V |
| wf21-01 L78 | r2p P | UNDERSTATED | second_computations.py l.10-15 (CHANGED for "W-F21, N4, second part"); web-st8-05's ground (3) | V |
| wf21-01 L86, L94, L100 | V | MISFILED | requests answered by A13/A14; identical L75 moved to N | N |
| wf17-04 L125 | r2p P | MISFILED (reason) | counts in main's run (l.11-16: vertical parts 0, 1, 1, 1, 2, 5; m = 5 pair four lines over C by the ground); only gcd(S_{m-1}, S_m - 1) not main's | P, naming the gcd formula |
| wf17-04 L136 | r2p P | UNDERSTATED | web_wf17_on_main.py l.87, 93-99; run l.16 (5 vertical Q-components); l.19 (axis lines only at m = 4, 8, 12) | V |
| wf17-04 L237 | r2p P | UNDERSTATED | script l.90-91 builds this construction; run l.11-16; sibling L236 kept | V |
| wf17-04 L253 | r2c C | UNDERSTATED | vertical part computed exactly by Groebner (l.91-98), not by the randomised test; run l.15; l.100; ground "two components of lines at m = 5" | V |
| wf17-04 L139 | V | OVERSTATED | Q3 computes main's projections, not agy-exp's text; heading L138 moved to N | C |
| r79b-01 L20 | r2p P | UNDERSTATED | B1882 lock (test_b1882...py l.186-191) computes both ranges from v1_null.json and asserts them; B1882 FINDINGS l.23-24 (masked) | V |
| r79b-01 L22 | r2p P | UNDERSTATED | B1886 lock at 896cae025: l.113 asserts (29, 19), l.115 compares, l.120-121 the plant; today l.141 asserts, l.120-123 the B1904 mend | V |
| wa1-04 L96 | r2p P | UNDERSTATED | web_wa1_rest_run.txt l.14 "GENESIS SE3 (POSTULATED, main's entry, counted in the budget)"; GENESIS l.222 | V |
| wa1-04 L99 | r2p P | UNDERSTATED | B1943 PROVED (fixed_lines_run l.1-2); wa1_rest run l.14 | V |
| wa1-04 L102 | r2p P | MISFILED (reason) | H1, H3 computed: web_wa1_part3.py l.57, 66; json H1 [0, 0], H3 2.8e-33; B1941, B1936 main's; only the postulate-D clause the seat's | P, naming that clause |
| wa1-04 L104 | r2p P | UNDERSTATED | BIG_RUN_RULE_v2.md A7 l.179-181, A14 l.243-252; web_wf22_on_main.py | V |
| wa1-04 L106 | r2p P | UNDERSTATED | web_wa1_part3.py l.70; json H4 ratios 0.209/0.162, |V| 0.0195/0.0167 (run line masked, json not) | V |
| wa1-04 L107 | r2p P | UNDERSTATED | B1932 t90_run.txt l.1-3 (gaps 7e-6 to 9e-6); wa1_rest run l.18 (C06 CHOSEN) | V |
| st8-05 L639 | r2p P | UNDERSTATED | SUMMARY.json at c458df8ce web files 136; extract.py l.149 added the 137th; status-page rule | V |
| st8-05 L643 | r2p P | UNDERSTATED | extract.py l.20-21; web-st7-06's how (2) | V |
| st8-05 L644 | r2p P | UNDERSTATED | web-st7-06's how verbatim | V |
| st8-05 L647 | r2p P | UNDERSTATED | SUMMARY.json at c458df8ce: files 136, read 87, PENDING 2571 | V |
| st8-05 L649 | r2p P | UNDERSTATED | same SUMMARY lists REVIEW_79, 79B, 80, 81 unread; ground (4) all settled | V |
| st8-05 L650 | r2p P | UNDERSTATED | same SUMMARY (the October and early-November notes); "M46 names" not checked | V |
| st8-05 L682 | r2p P | UNDERSTATED | BIG_RUN_RULE_v2.md A14 l.258-264 | V |
| fr-01 L56 | r2p P | UNDERSTATED | Jacobi isotropy gives theta2^4 + theta4^4 = theta3^4, hence 1/2 on tau = iy; web_first_row_bound.py l.13; run l.4-5 | V |
| wf2-01 L18 | r2p P | UNDERSTATED | web_wf2_on_main.py l.5, 32; record's note names the thrice-punctured sphere | V (or N) |
| wf2-01 L20 | r2p P | UNDERSTATED | web_wf1_on_main run l.7 (A2: a[x, y]a = (abc)^-2), l.8 (chi -1/2) | V |
| wf2-01 L35 | r2n N | UNDERSTATED (lead) | same as the ground's last sentence; run l.1-3 | V |
| wf2-01 L54 | r2c C | MISFILED | nothing rests on the seat's run: six permutations main's M2; M4 computes a mixed-face step | P |
| wf17-02 L44 | r2n N | UNDERSTATED (lead) | both checks follow from main's Q1 run l.1-9 | V |
| wf17-02 L45 | r2p P | UNDERSTATED | Q1 run l.1-9: all nine quotients integers; L46 kept | V |
| wf17-02 L32, L42, L43, L47 | r2p P | MISFILED | each rests on the seat's own run; main builds only the matrix groups and words | C |
| wf17-02 L49 | V | OVERSTATED | Q1 computes main's counts, not agy-exp's; note only implies the comparison | C |
| wa3-07 L139 | r2p P | UNDERSTATED | B1955 wa3_on_main.py l.141-143 ((1+4), (9+36), (1+16)); B1953 FINDINGS l.29 | V |
| wa3-07 L149 | r2p P | UNDERSTATED | an invariant cyclic subgroup of order 25 is an eigenline mod 25, needing a root mod 25; none (json F roots_mod_25 []) | V |
| wa3-07 L140 | r2c C | MISFILED | nothing rests on the seat's run; B1953 main's; condition equals q1^2 + q2^2 = 0 mod 5 | V |
| r80-01 L142 | r2p P | UNDERSTATED | web_wz1_c3_indices_run.txt l.9 (web-r80-03) | V |
| r80-01 L45 | r2n N | MISFILED | ground names finding 7 right and acted on (P-825; foundation v1.67), as kept findings 1, 3, 6, 8, 10, 11 | V |
| r80-01 L39 | V | OVERSTATED | not in ground: check_test_vacuity.py puts "X or True" in no class; error-ledger lines 182, 236; "no row names the seven files"; the seat's V0-V4 probes (sorter's copy cut) | P |
| r80-01 L192 | V | OVERSTATED | "18 lines ... in ten files" the seat's count (part Q), not in ground (sorter's copy cut) | P |
| wf7-02 L56 | r2p P | UNDERSTATED | web_wf7_on_main_run.txt l.11 (and l.2, l.10) | V |
| wa2-02 L25 | r2p P | UNDERSTATED | B1952 wa2_on_main run l.1 (every prime below 2000); B1884 arc verdict | V |
| wa2-02 L37 | r2p P | UNDERSTATED | B1884 PROVED: one line at N = 5, none other to 200; GENESIS l.222 cites it | V |
| wa2-02 L42 | r2p P | UNDERSTATED | B1943 fixed_lines_run l.2 | V |
| wz1-02 STATUS L64 | r2c C | MISFILED | status pointer; nothing rests on the seat's run; answered by web-wz1-02's recomputation | N (or V) |
| wa1-08 L159 | r2p P | UNDERSTATED | deleted parent (git 55fcbe008) had web_wa1_star.py as ground, run l.2 3.24; mirror covariance wa1_rest run l.6 (3.3e-16); G1 part3 json; parent deleted at 4921ee923 | V; restore the parent's ground |

Undecided: r79b-01 L29 (81, 16, 14 entries; WORKING_RULES.md l.525-526 masked; no script; P by the letter); wa2-02 L35 (GENESIS l.222 true through the mask; GENESIS not a banked arc; P by the letter). Not checkable through the mask: 12:45 in wf21-01 L48, L58 (git dates match; P stands).

Themes: the record kept as ground (main judged against its record's ground alone where its own scripts or arcs compute the clause: B1937, SUMMARY.json at c458df8ce, web_wa1_part3.json, B1943, B1952, web_wf7_on_main); text the sorter never saw (r80-01 L39, L192: sorter's copy cut); a deleted parent (web-wa1-08) leaving its companion with no parent.

## Packet 7
Units read 245 in 18 records; fine 200; not fine 45 (UNDERSTATED 26; OVERSTATED 5; MISFILED 14: 9 wrong kind, 3 wrong reason with verdict standing, 2 about a record's how).

Mask disclosure (the reader's): it once grepped B1940's FINDINGS.md directly, which showed lines 16, 17 and 46; 16 and 17 it had already seen through the mask; line 46 (a planted 15-digit run) is used in no finding.

| unit | now | finding | evidence | suggested |
|---|---|---|---|---|
| STATUS_CHAT1:467 | st7-03-r2n N | UNDERSTATED (lead) | item 4's lead states the finding; siblings 454, 459, 478, 481, 490, 497, 502 kept V; ground (4): nine -p companions exist | V |
| STATUS_CHAT1:509 | st7-03-r2n N | UNDERSTATED (lead) | item 10's lead "Two references are off."; main found both right and corrected them; ground (10) | V |
| STATUS_CHAT1:459 | st7-03 V | MISFILED (how) | how (2) says "web-wz1-05 is VERIFIED"; that record is gone, its lines P and C | unit V; dated pointer in how |
| W-F6:46 | wf6-01-r2c C | UNDERSTATED | web_wf6_on_main.py l.66, 70, 76; run l.1, 3, 5, 7, 9 "gap computed against V* w ... True"; lines 48, 49 V | V |
| W-F6:52 | wf6-01-r2p P | UNDERSTATED | l.70, 74, 76; run l.2, 4, 6, 10; part 2a's G4 V on main (web-wc8p2a-01) | V |
| W-F23:27 | wf23-01-r2p P | UNDERSTATED | B1940 double_precision_fails_run.txt l.2-3; rule A7 l.170-171 "above about Im tau = 11" (mask) | V |
| W-F23:32 | wf23-01-r2p P | UNDERSTATED | B1940 assemble_values_v2.py l.23; test_b1940_corrected_values_and_v3.py l.109; rule A13 l.229 | V |
| W-F23:53 | wf23-01-r2p P | UNDERSTATED | web_wf22_on_main_run.txt l.3 (S* does not repeat in one turn; S, S~ do) | V |
| W-F22:38 | wf22-01 V | MISFILED (how) | how gives "2.3 to 5.1"; run l.5: S* 2.7, 2.1, 5.1 | unit V; how 2.1 |
| W-F22:37 | wf22-01-r2p P | UNDERSTATED | every figure in ground and run; 1e-6 the seat's bound; main's 5.7e-5 shows "not met" (run l.4) | V |
| W-F22:53 | wf22-01-r2p P | UNDERSTATED | web_wf22_on_main.py l.2, l.18 (action (a - b, 2b - a)); run l.1 two non-trivial fixed classes among 266 | V |
| W-F22:58 | wf22-01-r2p P | UNDERSTATED | run l.1: up to sign exactly one other non-trivial line | V |
| W-F23:64, 65, 66, 67, 70, 71 | wf23-01-r2p P | UNDERSTATED | main took N1-N6 in A14 (BIG_RUN_RULE_v2.md l.258-264, mask), as N8 (73, 76 kept V) | V; how names A14 l.258-264 |
| W-F23:69 | wf23-01-r2p P | MISFILED | A14 l.262 mends only N4's absolute path; git show part unanswered; note types N1-N6 "a reading, for main" (l.109) | N (or P naming l.262) |
| W-F23:16, 17, 18, 22, 23, 24, 26, 49 | wf23-01-r2p P | MISFILED | readings or restatements of main's rule, typed "a reading, for main" (l.109); l.26 a judgement; main's text A7 l.177-181, A13 l.229-236, A15 l.266 | N |
| STATUS_CHAT1:1360 | st14-01 V | OVERSTATED | includes the seat's recut of 7,531 units, which the record's note calls the seat's run; same clause at st12-01 l.1037 is C; web_section14_run.txt l.1 totals only | C |
| W-F19:155 | wf19-01-r2p P | UNDERSTATED | E0 computed in web-wf6-01 on character sets of the table's sizes (web_wf6_on_main_run.txt l.1, 3, 5) | V |
| W-F19:158 | wf19-01 V | OVERSTATED | "(n(V), h1(G; V)) is the table's on every doublet, row by row": n(V) per doublet, h1 only through census totals (web_wf19_on_main.py l.37-41; run l.1-7) | P |
| STATUS_CHAT1:1042 | st12-01-r2p P | UNDERSTATED | review statement right and acted on; siblings 1044-1050 kept; four records' notes cite web_section9_items.py | V |
| STATUS_CHAT1:1045 | st12-01-r2p P | UNDERSTATED | as 1042; web-sel-04 N holds 65, 354, 356 | V |
| W-B2 s3:73 | wb2-s3-01-r2c C | UNDERSTATED | lead whose content main's S3 computes (wb2_stage3_on_main.py l.73-76; ground "3e-16") | V (at least N) |
| W-B2 s3:97 | wb2-s3-01-r2c C | UNDERSTATED | main's S3; line 75 and row 94 kept V | V |
| STATUS_CHAT1:56 | st-lists-01 V | OVERSTATED | "0.58 to 7.3" is the seat's measure, PARTIAL in web-wb2-d1-04p | P |
| STATUS_CHAT1:62 | st-lists-01-r2c C | UNDERSTATED | main's D4 8.5e-32 against the seat's 3e-8 (web_wb2_d1.py l.81; web-wb2-d1-05) | V |
| STATUS_CHAT1:161 | st-lists-01-r2p P | UNDERSTATED | E at residue level (D2), norm-level answer depends on metric (D4): web_wb2_d1.py l.61, l.81; web-wb2-d1-02, -05 | V |
| W-A3:58 | wa3-03-r2p P | UNDERSTATED | B1955's act's class: non-central trace-3, det-1 maps (-U), none a scalar times P (wa3_on_main.py l.115-116, 138; run l.4-5); line 166 kept V with same clause | V |
| W-A3:32 | wa3-03-r2p P | MISFILED (reason) | reason lists 3e-15, 6e-15; B1955's 3e-16 beats both; P stands for "three distinct eigenvalues" only | P, reason narrowed |
| W-A3:39 | wa3-06 V | OVERSTATED (minor) | wedge residual 9e-16 not computed by B1955; its det residual 4e-15 does not beat it | P |
| W-F4:20 | wf4-01 V | OVERSTATED (minor) | "i = 0, 1, 2" but N1 checks h0, h1 and interior classes only, not h2 (web_wf4_on_main.py l.9, l.136; cohom l.92-111) | P, or restore via chi(G) = 0 |
| W-F4:22 | wf4-01-r2p P | MISFILED (reason) | N3 computes deck pairing and closure (l.148; run l.3, 6, 9, 12); missing is h2 of Ind psi | P, reason h2 |
| W-C2:95 | wc2-03-r2p P | MISFILED (reason) | 330 in run l.6; P stands for 1160 and "half of one" | P, reason narrowed |
| W-C4:41 | wc4-03-r2p P | UNDERSTATED | facts (b), (c) computed: web_wc4_theorem_c.py C3, C4 (run l.3-4), cited by web-wc4-02 (V) | V |
| W-Z1:92 | wz1-05-r2c C | UNDERSTATED | "level exactly 4" computed on main (web_wz1_c3_indices_run.txt l.4, 6); "again by the referee" is provenance main keeps V elsewhere; main's result on the seat's item 2 has no V line left | V |

Undecided: W-F6:57 (B1438's recipe not read; left P); W-F6:20, 60, 62, 80 and W-F23:54 (uncovered clause is the seat's or referee's run: C by rule order rather than P; not reported; the referee's root 9471113 is a root of x^2 - x - 1 mod 9646561); W-F23:56, 73, 76 stay V (typed readings, adopted in A14; strict rule 2 would make them N with 64-71).

## Packet 8
Units read 245 in 18 parent records; fine 217; not fine 28 (UNDERSTATED 15; OVERSTATED 8, five minor; MISFILED 5). Parents gone: web-tube-02, web-st-lists-03, web-p783-06 (read at 4921ee923^).

| unit | now | finding | evidence | suggested |
|---|---|---|---|---|
| WEAVES_OWN_ACTION_ON_TAU:45 | wtau-03-r2p P | UNDERSTATED | W1-W4 are B1600 (docs/THE_WEAVE.md 60-69); WM1 is B1601 (75-80) | V, naming B1600, B1601 |
| WEAVES_OWN_ACTION_ON_TAU:48 | wtau-03-r2p P | UNDERSTATED | B1684 M1 "three parity sectors multiply to #" at five tau (FINDINGS 29); line 61 kept V on same cell | V (B1684 M1) |
| WEAVES_OWN_ACTION_ON_TAU:49 | wtau-03-r2p P | MISFILED (how) | B1684 M3: two critical points, i a saddle, omega the max of log(y|eta|^4) (FINDINGS 31); web_weave_action_on_tau.py S2 agrees; only e1, e2 and T's norm uncomputed (row 1075) | P, how narrowed |
| WEAVES_OWN_ACTION_ON_TAU:95 | wtau-03-r2p P | UNDERSTATED | B990's PROVED law word for word (FINDINGS 29-30) | V, naming B990 |
| WEAVES_OWN_ACTION_ON_TAU:134 | wtau-03-r2p P | UNDERSTATED | W2 is B1600 (THE_WEAVE.md 64): only point fixed by the Fricke maps of L and R is (0, 0, 0) | V naming B1600; at most P on "carries no tau" |
| WEAVES_OWN_ACTION_ON_TAU:136 | wtau-03 V | OVERSTATED | "End rho_Q = 1 + ad (WM1)" not in ground; main narrowed 45 for it; B1601 holds it | V once B1601 named; else P |
| WEAVES_OWN_ACTION_ON_TAU:132 | wtau-03 V | OVERSTATED (minor) | W1, W2 not in ground; main narrowed 134 for W2; B1600 holds both | name B1600, or P |
| WEAVES_OWN_ACTION_ON_TAU:80 | wtau-03 V | OVERSTATED (minor) | "W170 reads at that state" not in the ground's quotes of rows 1438, 1440 (masked) | P on that clause |
| WEAVES_OWN_ACTION_ON_TAU:42 | wtau-03 V | OVERSTATED (minor) | "named 2026-10-07", "binding in WORKING_RULES", "clause of 2026-10-24" not in ground; main narrowed 37; all stand on main (WORKING_RULES 425, 435; THE_WEAVE.md 56) | name them |
| STATUS_CHAT1:827 | st9-03-r2p P | UNDERSTATED | web_session_relay_three.py S2 (l.78; run l.2 "E6 2 ... gcd(3, 2) = 1"); web-sr-02's ground; sibling 824 kept | V |
| STATUS_CHAT1:843 | st9-03-r2p P | UNDERSTATED | web_section9_items.py I4 (l.54; run l.2) cusp rank 1 at golden 1-8; web_wc8_part5_bronze.py R3 at 1-3; only the hand reason unrun | V (or P, how corrected) |
| STATUS_CHAT1:848 | st9-03-r2p P | UNDERSTATED | web_wz1_c3_indices.py l.49 (run l.9 "N = 8: ... 10240 elements of 122880: index 12"); ground item (5) | V |
| STATUS_CHAT1:839 | st9-03 V | OVERSTATED | "every level", the Wang step and det(J^n - 1) = (-1)^n - L_n + 1 are the seat's hand argument; I4 covers 1-8; main narrowed the Wang argument at web-wc8p2a-01-r2p:45 | P |
| STATUS_CHAT1:833 | st9-03 V | OVERSTATED (minor) | "golden has none at levels 1 to 3" cites the seat's wc8_part5_out.txt; I3 runs bronze level 2 only (l.33 m, n = 3, 2; run l.1); web-wc8p5-01's note credits I3 with golden | P, or run golden 1-3 and correct the note |
| STATUS_CHAT1:308 | st5-01-r2p P | UNDERSTATED | status statement about main's register, right: SUMMARY.json at df0ce17a5 lanes/web files 16, statements 1167, V 156, S 5, N 85, pending 921 | V |
| W-C8_PART_1:24 | wc8p1-01-r2p P | UNDERSTATED | docs/handoffs/MAIN_TO_WEB_2026-11-13/tick_parity.py l.36-40; run l.4 "(-1)^(n+e): True" | V |
| W-C8_PART_1:25 | wc8p1-01-r2p P | UNDERSTATED | same, l.41; run l.5 "J alone ... exchanges the mark's pairs: True"; chat1.md 963-966 | V |
| W-C8_PART_1:27 | wc8p1-01-r2p P | UNDERSTATED | tick_parity run l.4-5; web_wc5_on_main.py C1 (run l.1) det X e = (-1)^(n+e) on eight classes; chat1.md 962 | V |
| W-F8:28 | wf8-01-r2p P | UNDERSTATED | GL(n-1, Z) is the ground's "matrix of determinant +-1"; control h h^-1 = id web_wf8_on_main.py l.39 (run l.1-7) | V |
| W-F8:44 | wf8-01-r2p P | MISFILED (how) | run l.9-11 "x_3 -> [-1, -1, 1]" and x_k fixed k >= 4; only growth/word-length remark uncovered | P, how corrected |
| STATUS_CHAT1:443 | st7-02-r2p P | UNDERSTATED | web_posthoc_closure.py run l.2, 4, 6 "with the conserving charge: M1 False, M2 False"; l.2 up at "Higgs charge none"; l.3 down's -3; leptons' -3 (l.5) masked; l.7 fixed text | V |
| STATUS_CHAT1:178 | st-lists-03-r2p P | UNDERSTATED | how says level is "B794's, not recomputed"; web_wz1_c3_indices.py run l.4, 6 (index 6 at (2), 12 at (4)); web-wc1-01 V; web_section9_items.py I5 run l.3 | V |
| W-C5:26 | wc5-01-r2p P | UNDERSTATED | main's 104 maps banked B1914 FINDINGS 26-28; seat's 44, 8 classes, letter swap in ground | V |
| W-C5:31 | wc5-01-r2p P | MISFILED | only reason is the sorter's 700-character cut; ground covers D(1, 2) = (1, 3), label swap, pairings, B1915 dated note (wc5 run l.3; B1915 FINDINGS 86-95) | V |
| W-A2:184 | wa2-04-r2c C | MISFILED | row's claim (W, split 3 + 2) is the ground's (B1952 C, R3); row 185 same kind kept V | V (or N for 184 and 185) |
| W-F24:84 | wf24-03-r2p P | MISFILED | provenance row on the referee's run (3,000 words; 0.0075); main files such rows C (wz1-01-r2c 89, 91; wa2-04-r2c 184) | C |
| W-A1:152 | wa1-02 V | OVERSTATED (minor) | "about 0.3 %" is the seat's estimate; 4.4e-3 is main's M37 / P-864 (chat1.md 698-700), ground does not cite | P on estimate, or name M37 |
| W-H1:70 | wh1-02 V | OVERSTATED (minor) | dates 2026-11-14, 2026-11-15 not in ground (main narrowed 72); both right | name them |

Not decided or masked: wa1-02 154, 156-158 (masked figures; ground names checks; left fine); STATUS_CHAT1:443 leptons' charge masked; wtau-03:80 masked; wf3-01:45 (C; V defensible); wc5-01:84 (C; left fine); wh1-02:75 (left fine); wf5-01:27 (P defensible).

Errors in main's scripts: web_section9_items.py I4 docstring (l.7-8) swaps odd and even (code right); web_wf5_on_main.py F1 prints H1 ranks from a hard-coded h1_group (not computed; F3 does compute, wf5-01:24 stands).

