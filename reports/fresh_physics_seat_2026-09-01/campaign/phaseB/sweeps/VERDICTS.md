# W-E absence sweep — the seat's verdicts

Claims swept: 545 (DOC_ECHO 24, GENERIC 69, LEAD 367, NO_HIT 64, UNSWEEPABLE 21). Verdicts written: 369 — NOISE 117, REGISTRY_ECHO 114, CONSISTENT 97, SUPERSEDED 18, OPEN_LATER 10, STANDS 8, GENERIC 4, CONTRADICTED 1.

Verdict key: CONTRADICTED = the repo already holds what the claim says is absent (the claim is wrong as written); SUPERSEDED = a later arc supplied it (the claim was true when written, stale now); OPEN_LATER = supplied only on an unmerged head, or the later work is unverified; STANDS / CONSISTENT = the sweep found nothing that supplies it (STANDS when the seat also checked directly); NOISE = co-occurrence only; GENERIC = terms too common for the sweep to say anything; REGISTRY_ECHO = only index/ledger files echo the claim. DOC_ECHO / NO_HIT rows (88) carry no verdict: the sweep found no text outside catch-all files, so the claim stands as far as the repository text goes.

## CONTRADICTED (1)

- **#393 B806_lexicon_blindness** (FINDINGS.md table): B806's table says CL-W4115 'Never ran', but frontier/B778_cleanup/cells/CL-W4115/ holds compute.py, output.txt and results.json (chord '1,5,19,71' REAL: True) — it ran; B806's row is stale/wrong (relay)

## SUPERSEDED (18)

- **#20 B58_phaseA** (B58_phaseA/B62_STATUS.md:16): B742/B745 (2026-07-21) computed the ambient SL(4) Jacobian and reproduce B59's factorisation; B58's 'not derived here' is negated by its own correction header
- **#25 B58_sl4_tower_test** (ower_test/FINDINGS.md, 'Verdict' section): B58_sl4_tower_test correction header: headline negated by B742+B745
- **#26 B58_sl4_tower_test** ( 'Why The Prediction Is Not Tested Here'): as #25
- **#44 B75_metallic_degree_rank** (5_metallic_degree_rank/FINDINGS.md:50-51): B78/B88 pursue the same search; B88 reports Dehn-filling components at rank 4 (degrees 3,4) — B75's n=3 null is superseded to the extent B88 covers it (rank 4), the m=3/n=3 cell itself not re-run there
- **#87 B126_ladder_to_physics** (py docstring / FINDINGS.md sec 'Floor 1'): a trace-field classifier was later built: B771 cell W3-067 recovers invariant trace fields from scratch (b++ bundles), B590 s031_m3_sealing.py, B123 probe
- **#140 B204_metallic_wrt_period** (): B204's 'normalization unresolved' is resolved by B771 cell OI-063 (RESOLVED-A: all-t symbolic Gauss-sum proof of P(gamma) = lcm(t-2,t+2)/content(gamma))
- **#161 B265_e6_integrability** (FINDINGS.md:~67 (Correction section)): B273 computed the e6 cup-product obstruction (vanishes identically; test_b273) — the 'not computed' sentence is stale in B265/B270
- **#164 B270_integrability_cup_product** ( recurs in B265's FINDINGS.md correction): as #161 (B273)
- **#166 B272_verification_and_gaps** (cation_and_gaps.py:1046-1049 (GAPS dict)): hypercharge/breaking chain later addressed (B862 global form, B1160 hypercharge forced; seat R10)
- **#173 B289_cp_sign_law** (): B855 wrong_null.py and B995 census recompute the m003/m136/m135 extensions (B855 corrects m003 amphichirality)
- **#185 B306_principal_grading_cascade** (principal_grading_cascade/FINDINGS.md:29): B892 later exhibits a dim-14 centraliser su(3)+su(2)+u(1)^3 by a different construction (two measurements), B932 chain selection — B306's 'no clean centralizer' is scoped to principal gradings
- **#427 B849_order_parameter** (FINDINGS.md:137): m004 Maass eigenvalues were later computed: 17 values harvested to main (B797, re-derived B795, B845 inventory); 'never computed' was true at B849's date
- **#428 B849_order_parameter** (FINDINGS.md:110): as #427
- **#429 B850_length_spectrum_type** (FINDINGS.md:137 (carried forward item 3)): B1007 arb_maass (flint) and the B878/B797 Hejhal-type pipeline exist later; 'Hejhal not in-sandbox' was true at B850's date
- **#434 B852_parabolic_pressure** (FINDINGS.md:97-100): B797 later banks 17 m004 eigenvalues on main
- **#449 B872_coset_leg** (FINDINGS.md sec 6): B872 (08-03) said cell9_sec16_verdict2.md exists nowhere; B921 later harvested it to main at frontier/B921_branch_harvest/harvested/frontier/B796_coupling_campaign/cell9_sec16_verdict2.md
- **#472 B882_magic_square_naming** ( entry ("UNCONFIRMED / not found" claim)): B1007 arb_maass (arb/flint dual-lattice Maass machinery) and B797 exist later on main
- **#519 B931_why_953** (ier/B931_why_953/FINDINGS.md, Headline 2): m009 (arithmetic, non-commensurable with m004 — R33 D) is used as exactly such a null in B850 sec 4a / B855

## OPEN_LATER (10)

- **#10 B16_record_swap_status** (er/B16_record_swap_status/FINDINGS.md:63): B1026_the_one_involution exists only on origin/claude/new-session-qor5up (never on main); until harvested, 'exchange symmetry not derived from A1-A6' stands on main
- **#11 B19_exchange_half_step_axiom_audit** (nge_half_step_axiom_audit/FINDINGS.md:33): same as #10 (B1026 on an unmerged head); B1050 projective wall does not derive it
- **#39 B73_sl4_apoly** (frontier/B73_sl4_apoly/probe.py:20): an SL(4) symbolic family exists later (B89_sl4_symbolic_M4L, B58/B742 ambient Jacobian); whether it is 'the SL(4) trace map' B73 lacks is a definitional question
- **#134 B199_metallic_exponent_law** (): B1039_phi_fixed_and_metallic_exponent and B1043/B1045 exist on another head (not on main); may supply the F_p point — unharvested
- **#154 B253_chirality_capability** (lity_capability.py:118 (Part B reason 2)): later cascade arcs (B565/B570 selection rules, B1145/B1146 fermion seat) build charge/fermion bookkeeping; none exhibits a dynamical 27 — claim stands, tracked
- **#158 B262_t41_theory** (NDINGS.md:9 (also t41_theory.py:724-726)): B488/B489 later claim T[A_m]=U(1)^(2m-1) 'verified for m=1..8' (DGG-abelian) — whether computed or asserted there is what R36 could not tell; H1 laws verified
- **#345 B790_maass_adjudication** (FINDINGS.md verdict table, Step 1 row): Maass eigenvalues were later computed on the audit branch (B792, B878 branch_FINDINGS, B922 receipt) and partially harvested (B797: 17 values); 'absent from B739-B754' was true when written
- **#355 B792_maass_m004_eigenvalues** (FINDINGS.md §'THE FULL WINDOW r<10'): degree-law never run on main; B792/B878 branch work exists unharvested
- **#356 B792_maass_m004_eigenvalues** (FINDINGS.md §'THE FULL WINDOW r<10'): as #355 (B796 Cell 9 prereg names them, execution held)
- **#484 B911_cmt_document** (mod-p) verification of compact wall dims): a CS->theta_QCD dictionary was later examined and refuted (log: 'strong-CP dictionary refutation', B730 cc_q3_cosmo.py, B906) — the lead is registered-and-closed, not absent

## STANDS (8)

- **#14 B24_anyon_quantum_bridge** (er/B24_anyon_quantum_bridge/README.md:19): 5 -> k+2 identification is a numerology B24 itself declines; no arc derives it
- **#15 B24_anyon_quantum_bridge** (/B24_anyon_quantum_bridge/FINDINGS.md:16): as #14
- **#21 B58_phaseA** (B58_phaseA/B62_STATUS.md:37): no explicit f(n,d), d != 2, anywhere (B62 status doc); the later B742/B745 work is the SL(4) Jacobian, not f(n,d)
- **#99 B143_interaction_feasibility** (3_interaction_feasibility/FINDINGS.md:24): Regina still not importable on this bench (ModuleNotFoundError)
- **#114 B162_kappa_sweep** (FINDINGS.md 'Honest scope' section): B186 adds numerical hyperbolicity certification, not a theorem off-axis
- **#116 B163_kappa_sweep_resolved** (FINDINGS.md Result (3a) closing sentence): as #114
- **#157 B259_gravity_brick_wall_map** (FINDINGS.md:41): B271 characterises wall #4 precisely and states no theorem closes it
- **#163 B268_e6_bridge_consolidation** (p_v2.py:78 (SKIPPED dict, wall4_4d_lift)): B271: no theorem closes wall #4

## CONSISTENT / NOISE / GENERIC / REGISTRY_ECHO

In `VERDICTS.tsv` (one row per claim).
