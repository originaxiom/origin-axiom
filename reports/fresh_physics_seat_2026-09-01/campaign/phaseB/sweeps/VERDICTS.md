# W-E absence sweep — the seat's verdicts

Distinct claims swept: 1094 of 1535 in synthesis/absence_claims.tsv (sweep rows 1535; 441 rows are duplicates caused by the index shift, see `sweep_index_map.tsv`). Status by claim: DOC_ECHO 37, GENERIC 129, LEAD 784, NO_HIT 102, UNSWEEPABLE 42.

Verdicts (per distinct claim): 826 — CONSISTENT 381, REGISTRY_ECHO 207, NOISE 127, SUPERSEDED 67, GENERIC 19, STANDS 12, OPEN_LATER 10, CONTRADICTED 3.

Verdict key: CONTRADICTED = the repo already holds what the claim says is absent (the claim is wrong as written); SUPERSEDED = a later arc supplied it (the claim was true when written, stale now); OPEN_LATER = supplied only on an unmerged head, or the later work is unverified; STANDS / CONSISTENT = the sweep found nothing that supplies it (STANDS when the seat also checked directly); NOISE = co-occurrence only; GENERIC = terms too common for the sweep to say anything; REGISTRY_ECHO = only index/ledger files echo the claim. DOC_ECHO / NO_HIT rows carry no verdict: the sweep found no text outside catch-all files, so the claim stands as far as the repository text goes.

Index note: `i` is the sweep index (VERDICTS.tsv key). `sweep_index_map.tsv` maps it to the row of the current absence_claims.tsv and marks duplicates; when duplicates disagree the more informative verdict is the claim's (order NOISE < GENERIC < REGISTRY_ECHO < CONSISTENT < STANDS < OPEN_LATER < SUPERSEDED < CONTRADICTED).

## CONTRADICTED (3)

- **#311 B778_cleanup** (frontier/B778_cleanup/FINDINGS.md:21-24): B778_cleanup's own FINDINGS l.21-24 lists CL-W4115 and CL-LATIN under 'Pending the next pass — Never ran', but frontier/B778_cleanup/cells/CL-W4115/ holds a completed run (compute.py, output.txt, results.json: chord '1,5,19,71' REAL True, wall re-verified as field-disjointness). The FINDINGS was not updated after the cell ran; test_b778_cleanup locks the FINDINGS text
- **#1243 B1191_close_loop_batch3** (ication/batch3_cells.json GC-15 evidence): tests/test_b279_spin_structure_bit.py exists on main, so "F3 ... has ZERO test coverage anywhere in the repo" is false as stated; whether that file locks the spin-vs-orientation bit is a separate question
- **#1498 B8141_artifact_dependence** (DINGS.md:Deliberately not in the finding): both files exist on the structure-genesis head: frontier/B8084_cold_audit/relays/CC3_TO_CC_2026-08-19_AUDIT_B1076_ONE_NOTATION_DEFECT.md and frontier/B8090_cold_audit_f1/relays/CC3_TO_CC_2026-08-19_I_WAS_WRONG_THE_REAL_DEFECT.md; "absent" held only on the head B8141 looked at

## SUPERSEDED (67)

- **#20 B58_phaseA** (B58_phaseA/B62_STATUS.md:16): B742/B745 (2026-07-21) computed the ambient SL(4) Jacobian and reproduce B59's factorisation; B58's 'not derived here' is negated by its own correction header
- **#25 B58_sl4_tower_test** (ower_test/FINDINGS.md, 'Verdict' section): B58_sl4_tower_test correction header: headline negated by B742+B745
- **#26 B58_sl4_tower_test** ( 'Why The Prediction Is Not Tested Here'): as #25
- **#44 B75_metallic_degree_rank** (5_metallic_degree_rank/FINDINGS.md:50-51): B78/B88 pursue the same search; B88 reports Dehn-filling components at rank 4 (degrees 3,4) — B75's n=3 null is superseded to the extent B88 covers it (rank 4), the m=3/n=3 cell itself not re-run there
- **#60 B85_tower_lynchpin** (ier/B85_tower_lynchpin/FINDINGS.md:34-35): 'numerical routes are DEAD' is negated by B742/B745 (B58_sl4 correction header): the pinv-ratio route converges at SL(4)
- **#61 B85_tower_lynchpin** (ontier/B85_tower_lynchpin/FINDINGS.md:51): as #60
- **#86 B123_arithmeticity_m1** ( / honest scope', and probe.py docstring): as #87: W3-067 / B590 / B123 later compute invariant trace fields (a classifier in effect)
- **#87 B126_ladder_to_physics** (py docstring / FINDINGS.md sec 'Floor 1'): a trace-field classifier was later built: B771 cell W3-067 recovers invariant trace fields from scratch (b++ bundles), B590 s031_m3_sealing.py, B123 probe
- **#140 B204_metallic_wrt_period** (): B204's 'normalization unresolved' is resolved by B771 cell OI-063 (RESOLVED-A: all-t symbolic Gauss-sum proof of P(gamma) = lcm(t-2,t+2)/content(gamma))
- **#161 B265_e6_integrability** (FINDINGS.md:~67 (Correction section)): B273 computed the e6 cup-product obstruction (vanishes identically; test_b273) — the 'not computed' sentence is stale in B265/B270
- **#164 B270_integrability_cup_product** ( recurs in B265's FINDINGS.md correction): as #161 (B273)
- **#166 B272_verification_and_gaps** (cation_and_gaps.py:1046-1049 (GAPS dict)): hypercharge/breaking chain later addressed (B862 global form, B1160 hypercharge forced; seat R10)
- **#173 B289_cp_sign_law** (): B855 wrong_null.py and B995 census recompute the m003/m136/m135 extensions (B855 corrects m003 amphichirality)
- **#185 B306_principal_grading_cascade** (principal_grading_cascade/FINDINGS.md:29): B892 later exhibits a dim-14 centraliser su(3)+su(2)+u(1)^3 by a different construction (two measurements), B932 chain selection — B306's 'no clean centralizer' is scoped to principal gradings
- **#338 B786_torsor_theta_iota** (FINDINGS.md lines 35-36): B787 later makes the 4th involution (iota) UNCONDITIONAL, removing the dependence on the corrected S
- **#345 B790_maass_adjudication** (FINDINGS.md verdict table, Step 1 row): m004 Maass eigenvalues later computed: 17 on main (B797/B795); LMFDB statement is about the literature
- **#352 B791_weyl_completeness** (FINDINGS.md §6): B797 later banks 17 m004 eigenvalues on main; Gate 9's blocker statement predates it
- **#366 B796_coupling_campaign** (loss_audit/THE_LOSS_LEDGER.md:14-16 (L1)): frontier/B909_frame_arc exists on main now (R38 read it)
- **#367 B796_coupling_campaign** (cell9_sec16_verdict3.md:26 (charge 6)): B921 harvested cell9_sec16_verdict2.md to main
- **#384 B800_habiro_integrality** (encing the door B685 that B800 addresses): B800 (2026-07-29) is the in-sandbox Habiro recompute B799 said was not attempted
- **#390 B804_dirac_spectrum** (FINDINGS.md:64): B1007 arb_maass and B797's harvested spectrum exist later on main
- **#495 B921_branch_harvest** (udit/THE_LOSS_LEDGER.md L1 (line ~13-16)): frontier/B909_frame_arc exists on main now (R38 read it); the loss-ledger line was true when written (as #628/#757)
- **#699 B855_wrong_null_audit** (FINDINGS.md line 33): as #519 (m009 used as the non-commensurable null in B850/B855)
- **#744 B909_frame_arc** (PROGRESS_LOG.md 2026-08-08 (B958 entry)): B978: the frame WAS built (B911) and the definitions were in CMT_DRAFT §2; B958's 'no frame or M12 construction anywhere' was found false
- **#768 B924_involution_couplings** (FINDINGS.md 'Honest gaps'): locks were later written: tests/test_b924_rigidity.py exists on main
- **#779 B928_d2_decode** (28_d2_decode/FINDINGS.md, Honest gaps #4): tests/test_b928_decode.py exists on main
- **#806 B952_gut_ledger_rank** (FINDINGS.md section 1): B951/B962/B970 addressed the exotics (B993: 'never addressed is false')
- **#812 B958_presence_scope** (FINDINGS.md:19): B978 (log 2026-08-08): 'the definitions were in CMT_DRAFT.md section 2, and B911 had already built the frame' — the 'never independently constructed' premise of B958 was found false
- **#813 B958_presence_scope** (ce_scope/arc_verdict.json claim_one_line): as #744
- **#814 B961_frame_instrument** (FINDINGS.md:10): as #744
- **#824 B970_L134_exotics** (PRIOR_ART_EXOTICS.md sec 1.1 table): as #806
- **#837 B973_L135_frame** (e/FINDINGS.md:19 (quoted in SCOUT.md §5)): as #812
- **#838 B973_L135_frame** (INDINGS.md:60-62 (quoted in SCOUT.md §5)): as #744 (B978)
- **#841 B974_phaseA_synthesis** (ted and refuted in SYNTHESIS.md §3.5(i))): as #812 (B978 corrects B974/B958's premise)
- **#842 B974_phaseA_synthesis** (ed and refuted in SYNTHESIS.md §3.5(ii))): as #744
- **#868 B993_cornerstone_verified** (FINDINGS.md): B994 then asked the rule-variation axis (R27 audited it)
- **#877 B1006_lambda2_pslq** (B1009 not B1006 -- correction, see below): B1019_l149_silver_cascade later runs the cascade on the silver (m=2) grammar
- **#879 B1009_verification_pass** (FINDINGS.md line ~34): as #877
- **#998 B1067_rayclass_harvest** (ults.json, claim 'unharvested-flag-cmbc'): B921 harvested harvest/second_round_cm_bost_connes.md to main (frontier/B921_branch_harvest/harvested/frontier/B796_coupling_campaign/harvest/)
- **#1041 B1107_oneloop_harvest** ( since B1107's verifier ran cleanly here): B1207_slow_lane_discharge later executed the slow-lane verifiers (its title and log entry); the 'never executed' line predates it
- **#1045 B1113_tmeter** (ternal to this arc's own committed files): as #1041
- **#1048 B1119_anomaly_resolved** (FINDINGS.md Fences): B1125_compact_color answered it: NO-COMPACT-HOST (typed negative, PROVED) — the object supplies the colour algebra, compactness is external
- **#1109 B1054_review_one** (GS.md 'What it found in the advancement'): docs/LAW_MAP.md now has "## G. The programme's method-laws (findings about the record-machine itself)" (l.247); B1181 registers a method-law row there
- **#1197 B1155_seam_a** (frontier/B1155_seam_a/FINDINGS.md header): B1162 claim_one_line: the height-308 witness is "now DUAL-HOMED (codex off-branch + main-sage)"; the provenance debt as of B1155 is discharged for the witness, the codex construction itself stays cited
- **#1212 B1165_gravity_terminal** (ty_terminal/FINDINGS.md (Fences section)): B1181 closes it: 83/83 amphichiral by the mirror-isometry method, "deliberately NOT the isometry_signature route"
- **#1214 B1167_seat_harvest** (/B1167_seat_harvest/b1167_results.json:8): as #1197 (B1162 dual-homing of the witness)
- **#1225 B1177_instrument_bundle** (B1177_instrument_bundle/FINDINGS.md:24): B1207: the first-ever complete OA_SLOW run finished (4 h 45 min; 9 failed / 5702 passed / 5 skipped) and the nine are triaged there
- **#1226 B1177_instrument_bundle** (nt_bundle/ADDENDUM_measurements.md:10-12): as #1225 (B1207 records the completed run)
- **#1236 B1190_close_loop_batch2** (fication/batch2_cells.json GC-7 headline): B1191 GC-7 "now closed in this arc" (#1242)
- **#1338 B8076_paper_closure** (.md item 4 row, quoting Scope (assembly)): B8080 deposits the code (assembly.py; check_assembly.py in papers/structure_paper/verify) and finds the classification FALSE AS STATED: all six candidates admit a 27-dim assembly
- **#1339 B8076_paper_closure** (3_TO_CC_2026-08-19_THE_PAPER_STATE.md:26): B8081 builds rho from Kac-Peterson data (rho_rebuilt.py; check_rho.py)
- **#1348 B8078_rung_spectrum_attained** (NDINGS.md:95 (also rung_attained.py:423)): B8079 closes the Qbar residue by an independent exact construction (#1349)
- **#1351 B8080_assembly_classification** (quoting the paper's own Scope (assembly)): as #1338: B8080 is the deposited code and refutes the classification
- **#1354 B8081_rho_rebuilt** (-8, quoting the paper's own Scope (2880)): as #1339
- **#1356 B8082_geodir_h1** ( quoting the paper's Scope (geodirscope)): B8082 computes the H^1 dimension count (first half); unobstructedness stays owed (#1357)
- **#1359 B8084_cold_audit** (B8084_cold_audit/FINDINGS.md:75): frontier/B1074_residue_hunt, B1075_moduli_crossing, B1076_coboundary_sweep all on main now; B8084 own relay AUDIT_B1075_CLEAN
- **#1360 B8084_cold_audit** (LD_AUDIT_BLOCKED_AND_FIRST_FINDING.md:13): as #1359
- **#1368 B8093_L171_clpw** (results.json lanes_2_to_6_started: false): lane 6 started: B8095_related_work_armor (L6 THE ARMOR relay); lanes 3-5 not found
- **#1369 B8094_L173_anchors** (B8094_L173_anchors/FINDINGS.md:52): B8146 completes the precision column as a negative (anchor paper reports no error bars)
- **#1372 B8094_L173_anchors** (-20_L173_THE_KNOB_IS_OUR_INTERCEPT.md:54): as #1368
- **#1438 B8099_3d_completeness** (pleteness.py CHECK list; FINDINGS.md:414): B8119: "E6 AS A DYNAMICAL GAUGE is CLOSED NEGATIVE (B262 wall #2)" -- the MISSING row is closed negative, not supplied
- **#1439 B8099_3d_completeness** (FINDINGS.md:415): B8119: "the E6 STATE INTEGRAL DISSOLVES (no dynamical E6, no such object)"
- **#1440 B8099_3d_completeness** (FINDINGS.md:415): B8119: the 4d lift is OUT OF SCOPE by owner ruling; B277 is the earlier obstruction
- **#1467 B8110_scale_factorisation** (-08-21.md 'What has NOT changed' section): B8111_genericity_control ran Phase-0 item 0 (sealed prereg; bites on 2 of 5 tones; sealed prediction wrong)
- **#1500 B8144_price_reconciliation** (FINDINGS.md): B1164 ADDENDUM_price_reconciliation l.15: "time's arrow ... absent ... B1164 MISSED it" -- registered as a residue, so the absence is now acknowledged in B1164 itself
- **#1506 B8153_b500_accounting** (arc_verdict.json:claim_one_line): B8153 own hunt_d5_finish.py (structure-genesis head, 2026-08-28) runs the nine never-reached words; B1187 addendum confirms no AIRLOCK anywhere in the banked logs
- **#1508 P3_depth_exposure** (d:Stabilization needed for the 7 exposed): B767 (R28-10) ran 6 of the 7 exposed kills and stabilized two (B1187 finding, #1230)

## OPEN_LATER (10)

- **#10 B16_record_swap_status** (er/B16_record_swap_status/FINDINGS.md:63): B1026_the_one_involution exists only on origin/claude/new-session-qor5up (never on main); until harvested, 'exchange symmetry not derived from A1-A6' stands on main
- **#11 B19_exchange_half_step_axiom_audit** (nge_half_step_axiom_audit/FINDINGS.md:33): same as #10 (B1026 on an unmerged head); B1050 projective wall does not derive it
- **#39 B73_sl4_apoly** (frontier/B73_sl4_apoly/probe.py:20): an SL(4) symbolic family exists later (B89_sl4_symbolic_M4L, B58/B742 ambient Jacobian); whether it is 'the SL(4) trace map' B73 lacks is a definitional question
- **#57 B83_sln_apolynomial** (ntier/B83_sln_apolynomial/FINDINGS.md:24): B742/B745's eps-extrapolated pinv route reached SL(4) (15x15); SL(5) principal component still not located numerically as far as the sweep shows
- **#134 B199_metallic_exponent_law** (): B1039_phi_fixed_and_metallic_exponent and B1043/B1045 exist on another head (not on main); may supply the F_p point — unharvested
- **#154 B253_chirality_capability** (lity_capability.py:118 (Part B reason 2)): later cascade arcs (B565/B570 selection rules, B1145/B1146 fermion seat) build charge/fermion bookkeeping; none exhibits a dynamical 27 — claim stands, tracked
- **#158 B262_t41_theory** (NDINGS.md:9 (also t41_theory.py:724-726)): B488/B489 later claim T[A_m]=U(1)^(2m-1) 'verified for m=1..8' (DGG-abelian) — whether computed or asserted there is what R36 could not tell; H1 laws verified
- **#894 B1025_input_derivability** (FINDINGS.md, meta-deliverable): contradicted on an unmerged head: B1030_input_typing_audit (origin/claude/new-session-qor5up) finds ONE continuous dimensionless input remains (A2 = c = 6σ); on main B1025's 'none remains' stands uncorrected
- **#908 B1030_input_typing_audit** (FINDINGS.md section 2): B1030 lives on origin/claude/new-session-qor5up; on main B1025's 'zero' stands (as #894)
- **#1207 B1162_mssm_debt_closure** (r/B1162_mssm_debt_closure/FINDINGS.md:54): check_charge_bracket.py exists on origin/codex/seat-r001 (certificates/r006_e6_invariants/paper/verify/) and origin/paper/structure-genesis-first (papers/structure_paper/verify/); the "deeper stack" is on two heads, so the breaking_chains/susy_test re-run is now possible and was not done

## STANDS (12)

- **#14 B24_anyon_quantum_bridge** (er/B24_anyon_quantum_bridge/README.md:19): 5 -> k+2 identification is a numerology B24 itself declines; no arc derives it
- **#15 B24_anyon_quantum_bridge** (/B24_anyon_quantum_bridge/FINDINGS.md:16): as #14
- **#21 B58_phaseA** (B58_phaseA/B62_STATUS.md:37): no explicit f(n,d), d != 2, anywhere (B62 status doc); the later B742/B745 work is the SL(4) Jacobian, not f(n,d)
- **#99 B143_interaction_feasibility** (3_interaction_feasibility/FINDINGS.md:24): Regina still not importable on this bench (ModuleNotFoundError)
- **#114 B162_kappa_sweep** (FINDINGS.md 'Honest scope' section): B186 adds numerical hyperbolicity certification, not a theorem off-axis
- **#116 B163_kappa_sweep_resolved** (FINDINGS.md Result (3a) closing sentence): as #114
- **#157 B259_gravity_brick_wall_map** (FINDINGS.md:41): B271 characterises wall #4 precisely and states no theorem closes it
- **#163 B268_e6_bridge_consolidation** (p_v2.py:78 (SKIPPED dict, wall4_4d_lift)): B271: no theorem closes wall #4
- **#1002 B1067_rayclass_harvest** (FINDINGS.md, census gap-list): never computed in the repo; checked here: PARI bnfinit(x^2-x-1).no = 1, qfbclassno(5) = 1
- **#1003 B1067_rayclass_harvest** (FINDINGS.md, census gap-list): no Dedekind-zeta special value of Q(sqrt5) anywhere; not computed here either
- **#1004 B1067_rayclass_harvest** (FINDINGS.md, census gap-list): checked here: PARI bnfinit(x^2-x-1).fu = -phi (a fundamental unit up to sign); the repo never proves minimality
- **#1489 B8135_paper1_drafted** (FINDINGS.md SCOPE): the 2-vs-3 primitive-class count at m=12 is UNRESOLVED on both heads; nothing later resolves it (a live discrepancy for the relay)

## CONSISTENT / NOISE / GENERIC / REGISTRY_ECHO

In `VERDICTS.tsv` (one row per sweep index).
