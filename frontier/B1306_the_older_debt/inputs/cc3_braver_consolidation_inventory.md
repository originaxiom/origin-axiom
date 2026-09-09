# CC3 / Braver-Questions / Consolidation seat inventory

Read-only inventory. All paths relative to repo root. All quotes verbatim from
`git show`/`git grep` output on the stated ref. No grading, no editorializing
beyond the literal MAIN-coverage classification the task specifies.

## Seat identification

- **The cc3 seat**: branch `paper/structure-genesis-first`, present identically on
  `origin` and `codeberg` (both point at commit `a31456d2`). Its `frontier/` contains
  arcs numbered `B8068`–`B8154` (the `B80nn`/`B81nn` band). `docs/CLOUD_ALIAS_TABLE.md`
  on main confirms this identification directly: *"the audit seat mints arcs in
  B8000+"* and *"B1068–B1080 → B8068–B8080, executed 2026-08-18"*.
- **The braver-questions seat**: branch `audit/b775-braver-questions`, present
  identically on `origin` and `codeberg` (both point at commit `53da05f6`).
- **The consolidation seat**: the consolidation branch, present identically on
  `origin` and `codeberg` (both point at commit `3851df2a`). (Its branch name is
  withheld per instruction; referred to only as "the consolidation seat" /
  "the consolidation branch" throughout.)

Current main: `origin/main` = `e324df06`.

---

## Part 1 — The cc3 seat: every `frontier/B80*/` and `frontier/B81*/` arc on its head

87 arcs, `B8068`–`B8154`. Columns: arc id; `FINDINGS.md` first line verbatim (or
note if absent); the arc's own status words (from `arc_verdict.json`'s `verdict`
field, the single field present on nearly every arc — noted separately where
absent); scripts present (`.py`/`.sh` basenames); MAIN coverage per
`git grep -l -E "<id>" -- docs frontier | head -3` classified HARVESTED (a main
arc/ledger row says verified/adopted/re-run/reproduced/harvested about this id),
CITED (mentioned only — alias table, audit-critique TSV, or a still-open/carried
review lead), or ABSENT (no hit).

| id | FINDINGS.md first line | status (arc_verdict.json `verdict`) | scripts | MAIN coverage | hit files (≤3) |
|---|---|---|---|---|---|
| B8068 | "# B8068 — the object's canonical cubic étale algebra IS the charge field" | PROVED | build_j2t.py, cell10_unbiased.py, cell11_compose.py, cell12_sm.py, cell13_forward.py, cell14_lattice.py, cell15_hypercharge.py, cell16_reality.py, cell17_subsets.py, cell18_realforms.py, cell19_control.py, cell20_outer.py, cell29_subalgebra.py, cell2_stabilizer.py, cell30_findB.py, cell3_su5.py, cell4_spinor.py, cell5_spinor_test.py, cell6_pure.py, cell7_field.py, cell8_density.py, e8_build.py, j2t_cubic.py | CITED | docs/CLOUD_ALIAS_TABLE.md ("not yet ported"); frontier/B1240_belt_closure_and_fc_harvest/verification/superseded_unmarked_candidates.tsv (audit-critique row, not a harvest) |
| B8069 | "# B8069 — affine isotropy selects a ray: the object fixes a (3,1) conformal structure" | PROVED | conformal_selection.py | CITED | docs/CLOUD_ALIAS_TABLE.md ("not yet ported") |
| B8070 | "# B8070 — RETRACTED. The rank descent was an artifact of my own script." | RETRACTED | anomaly_rank_descent.py | HARVESTED | docs/CLOUD_ALIAS_TABLE.md; docs/RELAY_LEDGER.md; frontier/B1241_master_identification_priced_and_phase_e_harvest/FINDINGS.md — quote: *"fc R52 — B8070's anomaly cubic reproduced... fc's R52 and B8070 l.84 agree, and so does this bench (verification/r52_anomaly_cubic.py, sympy, REPRODUCES)"* |
| B8071 | "# B8071 — the reality gate: the compact rank-4 algebra exists in e₆(2), on the orbit the object does not reach" | PROVED | orbit_meets.py, reality_gate.py | ABSENT | — |
| B8072 | "# B8072 — the matching-capacity floor: seven nulls are one measurement of an instrument" | PROVED | capacity.py | ABSENT | — |
| B8073 | "# B8073 — the object's `su(5)` is NOT τ-stable: a cross-seat claim that does not reproduce" | NEGATIVE | cell31_B.py | CITED | docs/ERROR_LEDGER.md (unrelated E47 entry, coincidental keyword); frontier/B1240.../superseded_unmarked_candidates.tsv (mentioned only, "B8073 itself is outside this packet and not independently verified by this reader") |
| B8074 | "# B8074 — the rank ceiling's hypothesis is load-bearing: nilpotent centralisers reach rank 4" | PROVED | nilpotent_rank4.py | CITED | frontier/B1098_nonabelian_hatch/FINDINGS.md — named only ("the B1074/B8074 nilpotent gap") |
| B8075 | *(no FINDINGS.md; dir holds only `results.json` + `rung_spectrum.py`)* | *(no verdict field either)* | rung_spectrum.py | CITED | frontier/B1240.../superseded_unmarked_candidates.tsv — audit-critique row: *"this arc's own results.json explicitly frames its 16-subset table as a sample... later shown by B8078/B8079 to have been an under-sample"* |
| B8076 | *(no FINDINGS.md; has `CAMPAIGN.md` instead — "**ALL TWELVE ITEMS ARE GREEN**")* | *(no verdict field; CAMPAIGN.md's own status: "ALL TWELVE ITEMS ARE GREEN")* | item01_weight_field.py, item06_quotients.py | ABSENT | — |
| B8077 | "# B8077 — the cascade's endpoint has a COMPACT home in the object's own real form" | PROVED | compact_home.py | ABSENT | — |
| B8078 | "# B8078 — the rung spectrum is ATTAINED: the paper's eleven-element bound is TIGHT" | PROVED | rung_attained.py | HARVESTED | docs/THEOREM_REGISTRY.md; docs/views/VERDICT_LEDGER.md; frontier/B1140_the_64_organized/FINDINGS.md — quote (VERDICT_LEDGER B1140 row): *"cc3's 2nd grounding: the 14 is the corpus's own 14-locus (cc3 B8078 rung) => 64 forced not chosen"* |
| B8079 | "# B8079 — the rung arrangement EXACT over ℚ: B8078's residue closed, and the 64 Levis deposited" | PROVED | arrangement_exact.py | CITED | frontier/B1240.../superseded_unmarked_candidates.tsv — named only, inside B8075's row |
| B8080 | "# B8080 — the assembly classification is FALSE as stated: all six candidates admit one" | NEGATIVE | assembly.py | CITED | docs/CLOUD_ALIAS_TABLE.md (listed in the B1068–B1080 remap note; no per-row detail) |
| **B8081** ⚑ | "# B8081 — ρ is BUILT: Prop 2880 and the coupling law stop being certificates about an absent matrix" | PROVED | rho_rebuilt.py | ABSENT | — |
| **B8082** ⚑ | "# B8082 — the geodir dimension count is COMPUTED, and one adjective in it is not" | PROVED | geodir_h1.py | ABSENT | — |
| **B8083** ⚑ | "# B8083 — the positivity bridge: why a cyclic-word invariant settles a conjugacy question" | PROVED | positivity_bridge.py | ABSENT | — |
| B8084 | "# B8084 — the cold audit: is there systematic negative bias? (in progress)" | OPEN | audit_b1075.py | ABSENT | — |
| B8085 | "# B8085 — Route A run: the arithmetic obstruction B990 predicted is **ABSENT**" | PROVED | integral_orbits.py | HARVESTED | docs/OPEN_LEADS.md ("THE AUDIT-SEAT HARVEST QUEUE... L169... COMPUTE CLOSED — B1093"); docs/RELAY_LEDGER.md |
| B8086 | "# B8086 — the ℤ/5 Wilson-line menu: every row is rank 6, and B955 is re-derived by a second route" | NEGATIVE | wilson_menu.py | HARVESTED | docs/OPEN_LEADS.md; docs/RELAY_LEDGER.md; frontier/B1079_wilson_menu/FINDINGS.md — quote: *"their B8086 confirms it bit-for-bit independently"* |
| B8087 | "# B8087 — the neutrino selector: ⟨ν^c⟩ is a CONDITION, not a POINT" | PROVED | neutrino_selector.py | HARVESTED | docs/OPEN_LEADS.md ("L168... CLOSED — B1092"); docs/RELAY_LEDGER.md |
| B8088 | "# B8088 — the menu is homogeneous, but ARITHMETICALLY: W alone gives 25 orbits, not 9" | PROVED | row_homogeneity.py | HARVESTED | docs/OPEN_LEADS.md; docs/RELAY_LEDGER.md; frontier/B1079_wilson_menu/FINDINGS.md — quote: *"(their B8088): the rows are single orbits under W × Galois (nine-to-nine, verified)"* |
| B8089 | "# B8089 — door 5 is shut STRUCTURALLY: the anomaly layer over the derived content is identically zero" | NEGATIVE | anomaly_door5.py | HARVESTED | docs/OPEN_LEADS.md; docs/THE_LADDER.md; docs/views/THE_SPINE.md — quote (THE_SPINE): *"B1096 NEGATIVE ... DOOR 5 SHUT STRUCTURALLY (the audit seat's B8089 re-derived entry-for-entry with own exact code)"* |
| B8090 | "# B8090 — COLD AUDIT, FINDING 1: B1076's \"new exact character\" is mis-stated on every summary surface" | PROVED | character_check.py | ABSENT | — |
| B8091 | "# B8091 — what the FIRST STEP throws away: the monodromy is M², and squaring erases the bits" | PROVED | first_step_losses.py | HARVESTED | docs/EDGE_PREREG_SPEC.md; docs/OPEN_LEADS.md ("L170... CLOSED — B1096 + B1097 (2026-08-20); both re-derived stronger than their sources"); docs/THE_ROAD.md |
| B8092 | "# B8092 — THE DESIGN AUDIT: three places the prompts could only remove candidates" | NEGATIVE | *(none)* | ABSENT | — |
| B8093 | "# B8093 — L171: the CLPW crossed-product bridge, typed. **MOOD, not MATCH — and the disanalogy is the finding**" | NEGATIVE | *(none)* | HARVESTED | docs/OPEN_LEADS.md; frontier/B1171_seam_harvest/FINDINGS.md — quote: *"Their 8/8 verification of B8093's CLPW typing against the source"*; frontier/B1171_seam_harvest/b1171_results.json |
| B8094 | "# B8094 — L173: the experimental anchors. **The knob they already turn IS our intercept**" | PROVED | *(none)* | HARVESTED | docs/EDGE_PREREG_SPEC.md; docs/EDGE_PREREG_SPEC_ADDENDUM_B8146.md — quote: *"## The finding (cc3's, adopted)"*; docs/OPEN_LEADS.md |
| B8095 | "# B8095 — L-package lane 6: the paper's related-work armor, five differentiators" | PROVED | *(none)* | ABSENT | — |
| B8096 | "# B8096 — the residue hunt re-run with the guard relaxed: **OUTCOME B, and the negative is now stronger**" | NEGATIVE | relaxed_hunt.py | ABSENT | — |
| B8097 | "# B8097 — THE BURIED-RESULTS HUNT: nineteen, in two catalogues, both already written and neither acted on" | PROVED | *(none)* | HARVESTED | docs/OPEN_PROBLEMS.md; docs/THE_LADDER.md — quote: *"CONFIRMED AND RANKED, STILL UNPAID (B8097, 2026-08-20 ...): independently re-confirms the falsification"* |
| B8098 | "# B8098 — L1 VERIFIED: two of the five selection criteria provably cannot see the difference" | PROVED | verify_l1.py | CITED | frontier/B1240.../superseded_unmarked_candidates.tsv — audit-critique row, own arc flagged SUPERSEDED_UNMARKED |
| B8099 | "# B8099 — the 2+1 theory's completeness audit: **six of eleven present, and the question is ambiguous**" | PROVED | completeness.py | HARVESTED | docs/THE_LADDER.md; frontier/B1088_action_card/FINDINGS.md — quote: *"Corroboration 2026-08-20 (the audit seat's B8099, independent in-sandbox)... verified by the second seat's own build"*; frontier/B1194_existence_audit/verification/audit_cells.json |
| B8100 | "# B8100 — the one-loop GEODESIC factor computed, and the cusp piece located in B739" | PROVED | oneloop.py | HARVESTED | docs/THEOREM_REGISTRY.md ("B1107 (harvesting B8100→B8112)"); docs/THE_ROAD.md; docs/views/THE_SPINE.md — quote: *"THE ONE-LOOP RUELLE IDENTITY HARVESTED... the audit seat's B8100->B8104->B8112 chain"* |
| B8101 | "# B8101 — B739's scattering determinant IS one, verified; `φ(1) = −1`; five of seven ingredients in hand" | PROVED | scattering.py | HARVESTED | frontier/B1107_oneloop_harvest/b1107_NOTES.md — quote: *"(verified in B8101)"*; frontier/B1157_dynamics_null/FINDINGS.md; frontier/B1157_dynamics_null/b1157_results.json |
| **B8102** ⚑ | "# B8102 — the cusped one-loop problem is a LITERATURE GAP, and we hold the input that is usually hardest" | PROVED | *(none)* | ABSENT | — |
| B8103 | "# B8103 — the specialist register revisited: **two of seven were never specialist gates at all**" | PROVED | *(none)* | ABSENT | — |
| B8104 | "# B8104 — the cusped formula EXISTS explicitly: retracting my own NEEDS-SPECIALIST label, two hours old" | PROVED | *(none)* | HARVESTED | docs/THE_ROAD.md; docs/views/THE_SPINE.md ("B8100->B8104->B8112 chain"); docs/views/VERDICT_LEDGER.md |
| B8105 | "# B8105 — R48 PHASE 1 (mechanical): the theorem registry has been violating its own standing rule for 179 arcs" | PROVED | *(none)* | ABSENT | — |
| B8106 | "# B8106 — R48 PHASE 2: a requirements ledger still says the object cannot do what the same window proved it does" | PROVED | *(none)* | ABSENT | — |
| B8107 | "# B8107 — R48 verification: both fixes hold, and the F1 fix created one new instance of F1's own pattern" | PROVED | *(none)* | ABSENT | — |
| B8108 | "# B8108 — R48 PHASE 3: 13 of 36 candidates dissolve on one mechanical test, and the remedy already exists in-corpus" | PROVED | *(none)* | ABSENT | — |
| B8109 | "# B8109 — R48 CLOSE: four findings, zero new in phases 3–4, and the lag scan was the wrong instrument" | PROVED | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md ("B8109's positive-control practice ride this bank"); docs/PRACTICES.md; docs/views/VERDICT_LEDGER.md ("the discipline adopted from the audit seat's B8109") |
| B8110 | "# B8110 — scale factorisation" | PROVED | *(none)* | HARVESTED | frontier/B1152_suite_cost_class/FINDINGS.md; frontier/B1152_suite_cost_class/b1152_results.json — quote: `"harvest_source": "cc3 B8139 (paper/structure-genesis-first @ 1f455266), integrate-don't-merge"` (B8110's own content is discussed in this arc as the drift example) |
| B8111 | "# B8111 — the genericity control BITES, but on **2 of 5 tones** — and my sealed prediction was wrong" | PROVED | genericity_control.py | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/EDGE_PREREG_SPEC.md ("the audit seat's B8111"); docs/LAW_MAP.md ("L178 registered (tone lane, gated, B8111-bound)") |
| B8112 | "# B8112 — the dictionary entry is an **identity**, and the answer to B8104's question is \"none of them\"" | PROVED | dictionary.py | HARVESTED | docs/RELAY_LEDGER.md; docs/STRATEGY_2026-09-05.md; docs/THEOREM_REGISTRY.md ("B1107 (harvesting B8100→B8112)") |
| B8113 | "# B8113 — WHAT-REMAINS item 5 has **three** residues, not one — and B8112 *added* one of them" | PROVED | abscissa.py | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/RELAY_LEDGER.md; docs/THEOREM_REGISTRY.md ("B8113's three residues as scope"); also docs/THE_ROAD.md ("declined (B8113, residue 2)") |
| B8114 | "# B8114 — the paper's related-work armor: five differentiators, each ending in a NON-claim" | PROVED | *(none)* | ABSENT | — |
| B8115 | "# B8115 — C5 closes as a **NEGATIVE**, and the negative names its own boundary" | NEGATIVE | *(none)* | HARVESTED | docs/THE_FRAMEWORK.md — quote: *"(the audit seat's B8115 reading, harvested B1108 with independent source ...)"*; docs/views/VERDICT_LEDGER.md; frontier/B1108_c5_archimedean/FINDINGS.md — quote: *"Harvest arc (integrate-don't-merge): the reading is the audit seat's"* |
| B8116 | "# B8116 — the 4₁ tower: the proven/conjectured split, and a correction to **my own B8115**" | PROVED | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md ("per B8116's pre-bank correction"); docs/THE_FRAMEWORK.md ("B8116's same-day correction"); docs/THE_ROAD.md |
| B8117 | "# B8117 — L172: **there is no Fibonacci-anyon device**, and the negative closes a route" | NEGATIVE | *(none)* | CITED | frontier/B1136_genericity_on_the_wins/FINDINGS.md — named only, in a list of prior instruments (the harvest credit in that arc names B8128, not B8117) |
| B8118 | "# B8118 — the two theories **differ in KIND**: the ambiguity was a category error" | PROVED | two_theories.py | CITED | frontier/B1136_genericity_on_the_wins/FINDINGS.md — named only, same list |
| B8119 | "# B8119 — finishing the 3d theory: **complete as a definition**, and one row was never searched" | PROVED | closure.py | HARVESTED | frontier/B1117_adelic_object/FINDINGS.md — quote: *"Cross-check addendum — two seats, two routes (cc3 B8119, 2026-08-21)... verified from a SECOND seat by a SECOND route"* |
| B8120 | "# B8120 — scrutiny triage" | PROVED | *(none)* | ABSENT | — |
| B8121 | "# B8121 — m4 closed" | PROVED | *(none)* | ABSENT | — |
| B8122 | "# B8122 — constructive items" | PROVED | *(none)* | ABSENT | — |
| B8123 | "# B8123 — scrutiny closed" | PROVED | *(none)* | ABSENT | — |
| B8124 | "# B8124 — phi law sharpened" | PROVED | *(none)* | CITED | docs/OPEN_LEADS.md; docs/progress/REVIEWS.md — quote: *"R48-2: integrate cc3's golden-meridian refinement (B8124 ...)"*, marked `[>]` (carried/pending), later "folded into R50-6" — still an open verify lead, not yet closed as harvested |
| B8125 | "# B8125 — abscissa not the cusp" | NEGATIVE | *(none)* | CITED | frontier/B1136_genericity_on_the_wins/FINDINGS.md — named only, same instrument-list as B8117/B8118 |
| B8126 | "# B8126 — tone axis split" | PROVED | *(none)* | CITED | docs/OPEN_LEADS.md; docs/progress/REVIEWS.md — quote: *"B8126 the Pauli-components split) — VERIFY on-bench, then scope"*, same pending R48-2/R49-5 lead as B8124 |
| B8127 | "# B8127 — regulator omission" | PROVED | *(none)* | CITED | docs/CAMPAIGN_STATUS.md — quote: *"its pushed branch ... survives as a frozen harvest source (B8127, B8148–B8153...)"*; docs/RELAY_LEDGER.md; docs/THE_REMAINING_MATH.md — quote: *"(B8127, B8148–B8153 + the control-defect pair — from the frozen branch, verify-don't-trust as always)"* — explicitly still pending, unlike B8148–B8153 which the same doc later calls "already-harvested" |
| B8128 | "# B8128 — genericity on the wins" | PROVED | wins.py | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/THEOREM_REGISTRY.md; docs/views/THE_SPINE.md; ⇒ frontier/B1136_genericity_on_the_wins/FINDINGS.md — quote: *"Harvest arc — cc3's B8128 (paper branch..., owner-elected), verified TWO-BENCH"* |
| B8129 | "# B8129 — n2 no breakdown" | PROVED | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/OPEN_LEADS.md; docs/THEOREM_REGISTRY.md ("cc3 B8129/B8130... graviton bridge DEAD, confirming") |
| B8130 | "# B8130 — item5 ruelle Lchi" | PROVED | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/OPEN_LEADS.md; docs/THEOREM_REGISTRY.md (same B1140 row, "confirming cc3 B8129/B8130") |
| B8131 | "# B8131 — brief triage" | PROVED | *(none)* | ABSENT | — |
| B8132 | "# B8132 — spin count not separating" | PROVED | *(none)* | HARVESTED | docs/views/VERDICT_LEDGER.md; frontier/B1141_spin_payment/FINDINGS.md — quote: *"Scope clause (cc3 B8132, verified this bench): the spin-structure COUNT is a FAMILY fact, not m004's"*; frontier/B1144_adoption_audit/FINDINGS.md — quote: *"STAND: B8132's spin-count scope clause"* |
| B8133 | "# B8133 — residue2 reframed" | PROVED | *(none)* | ABSENT | — |
| B8134 | "# B8134 — codex branch stale claim" | PROVED | *(none)* | CITED | frontier/B1240.../superseded_unmarked_candidates.tsv — own arc flagged SUPERSEDED_UNMARKED (audit-critique, not a harvest) |
| B8135 | "# B8135 — Paper I is drafted — the period-one locus, and a selection that sees only the trace" | PROVED | *(none)* | ABSENT | — |
| B8136 | "# B8136 — Paper II is drafted — a finite spectrum on an infinite lattice, and C is forced" | PROVED | *(none)* | ABSENT | — |
| B8137 | "# B8137 — Paper III is drafted — and it ships a reproducer the source arc never had" | PROVED | *(none)* | ABSENT | — |
| B8138 | "# B8138 — Paper IV is drafted — three no-gos, each with its exhaustive escape" | PROVED | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md ("cc3 B8138-extended adds the cusp shape as a 2nd object-level separator"); docs/RELAY_LEDGER.md ("harvests cc3 B8138-extended... Verified cc3's cusp-shape second object-level separator... cc3 ACCEPTED"); docs/views/VERDICT_LEDGER.md |
| B8139 | "# B8139 — the FINDINGS.md omission, and why a lock that works caught nothing for five days" | PROVED | *(none)* | HARVESTED | docs/COMPUTE_THE_PROGRAM.md; docs/ERROR_LEDGER.md ("E50 the COST class — a lock never REACHED (harvested from cc3's B8139)"); docs/RELAY_LEDGER.md ("THE COST FAILURE CLASS harvested → B1152") |
| B8140 | "# B8140 — the fast lane reproduced, and two empties that are not the same empty" | PROVED | *(none)* | HARVESTED | docs/RELAY_LEDGER.md; docs/progress/REVIEWS.md; frontier/B1152_suite_cost_class/FINDINGS.md — quote: *"[B8140 correction (cc3, adopted 2026-08-26): ...]"* |
| B8141 | "# B8141 — the artifact class: a lock that reads a gitignored file reports on the machine" | NEGATIVE | *(none)* | HARVESTED | docs/progress/REVIEWS.md — quote: *"the action taken this review — B8141 the artifact class, harvested + fixed"*; docs/views/VERDICT_LEDGER.md; frontier/B1177_instrument_bundle/FINDINGS.md |
| B8142 | "# B8142 — residue 2 reduced twice: the Sym-power Ruelle zeta factors over the twist family" | PROVED | acyclicity.py, bridge.py, reflection.py | HARVESTED | docs/CAMPAIGN_STATUS.md — quote: *"harvesting cc3's fresh B8142/B8142b"*; docs/OPEN_LEADS.md; docs/RELAY_LEDGER.md |
| B8143 | "# B8143 — the anomaly lane: B1160's theorem is right, and its shaping fence is TOO CONSERVATIVE" | PROVED | step1_core.py, step2_shape.py, step3_competitor.py, step4_full.py, step5_robust.py, step6_genericity.py | HARVESTED | docs/CAMPAIGN_STATUS.md — quote: *"cc3 B8143 + codex R019 rescope the charter's G1/E2... Verified three ways"*; docs/RELAY_LEDGER.md ("harvests cc3 B8143 chain"); docs/views/VERDICT_LEDGER.md |
| B8144 | "# B8144 — two ledgers of the same price disagree by two items" | OPEN | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/RELAY_LEDGER.md — quote: *"Caught that B1164's census disagrees with the banked price ledger by two items — verified + adopted (B1164 addendum)"*; docs/progress/REVIEWS.md |
| B8145 | "# B8145 — L171 verified: B8093 is right on every fact and on the typing, and its disclosed gap is now filled" | PROVED | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/OPEN_LEADS.md ("cc3's B8145 verified the B8093 typing against the CLPW source 8/8"); docs/RELAY_LEDGER.md ("harvests ... B8145") |
| B8146 | "# B8146 — L173's precision column, completed as a negative that reshapes the prereg" | NEGATIVE | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/EDGE_PREREG_SPEC_ADDENDUM_B8146.md — quote: *"cc3 credited (B8146)"*; docs/OPEN_LEADS.md |
| B8147 | *(no FINDINGS.md; `arc_verdict.json` + relays only)* | RETRACTED | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/LAW_MAP.md; docs/RELAY_LEDGER.md — quote: *"CC_TO_CC3_2026-08-27_B8147_ADOPTED.md ... harvests cc3 B8147... The family-denominator retraction ADOPTED"* |
| B8148 | *(no FINDINGS.md; `arc_verdict.json` only)* | PROVED | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md — quote: *"already-harvested B8148–B8153 work stays banked under its main numbers"*; docs/THE_REMAINING_MATH.md; docs/progress/REVIEWS.md |
| B8149 | *(no FINDINGS.md; `arc_verdict.json` only)* | PROVED | *(none)* | ABSENT | (literal grep for the exact string "B8149" hits nothing; it is however inside the elided range "B8148–B8153" quoted as already-harvested at docs/CAMPAIGN_STATUS.md — see note below) |
| B8150 | *(no FINDINGS.md; `arc_verdict.json` only)* | PROVED | *(none)* | ABSENT | (same elided-range note as B8149) |
| B8151 | "# B8151 — the verified-vs-used check, run across all four papers" | PROVED | *(none)* | HARVESTED | docs/ERROR_LEDGER.md ("cc3's B8151 verified-vs-used sweep... join the review checklist as VERIFY-THE-VERIFIER"); docs/progress/REVIEWS.md; frontier/B1185_yukawa_three_mechanisms/FINDINGS.md |
| B8152 | *(no FINDINGS.md; `arc_verdict.json` only)* | PROVED | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/ERROR_LEDGER.md; docs/RELAY_LEDGER.md — quote: *"B8152 verified by independent full-census enumeration + corrected... cc3 ADOPTED same-day"* |
| B8153 | *(no FINDINGS.md; `arc_verdict.json` only)* | NEGATIVE | *(none)* | HARVESTED | docs/CAMPAIGN_STATUS.md ("already-harvested B8148–B8153"); docs/ERROR_LEDGER.md ("E52 instance #6... cc3 B8153, self-caught"); docs/RELAY_LEDGER.md |
| B8154 | "# B8154 — the mirror involution IS the Galois generator `c`" | PROVED | involution.py | HARVESTED | docs/CAMPAIGN_STATUS.md; docs/RELAY_LEDGER.md; docs/THEOREM_REGISTRY.md — quote: *"Independently re-reached from the holonomy by cc3 (B8154, verified at B1208)"* |

Note on B8149/B8150: `docs/CAMPAIGN_STATUS.md` line 397 and `docs/THE_REMAINING_MATH.md`
line 53 both say *"already-harvested B8148–B8153 work stays banked under its main
numbers"* — an elided range whose endpoints (B8148, B8153) contain the literal
digit-strings but whose interior members (B8149–B8152) do not, so the literal
`grep -E "B8149"` the task specifies returns nothing even though the prose range
covers it. Reported as ABSENT per the literal grep, with this caveat.

### Flagged arcs — headline claims verbatim (≤40 words)

- **B8081**: "ρ is BUILT: Prop 2880 and the coupling law stop being certificates about an absent matrix"
- **B8082**: "the geodir dimension count is COMPUTED, and one adjective in it is not"
- **B8083**: "the positivity bridge: why a cyclic-word invariant settles a conjugacy question"
- **B8102**: "the cusped one-loop problem is a LITERATURE GAP, and we hold the input that is usually hardest"

All four are MAIN-ABSENT (no hit in `docs` or `frontier` for their bare id).

### Part 1 tally

87 arcs total: **42 HARVESTED**, **15 CITED**, **30 ABSENT**.

---

## Part 2 — The braver-questions seat: arcs not on main's head

`git ls-tree --name-only origin/audit/b775-braver-questions frontier/` has 1032
top-level entries; `git ls-tree --name-only origin/main frontier/` has 1246.
Six directories exist on the branch head and not on main's:

| id | headline verbatim | MAIN coverage |
|---|---|---|
| B775_braver_questions | "# B775 — THE BRAVER QUESTIONS — FINAL REPORT" (from `FINDINGS_FINAL.md`; the arc also carries `FINDINGS_PARALLEL.md` = "# B775 FINDINGS — Parallel Phases (A, C, D, G)" and `FINDINGS_THREE_MOVES.md` = "# B775 — THE THREE NEXT MOVES — FINDINGS") | Hits `docs/CAMPAIGN_STATUS.md`, `docs/CLOSURE_MASTERPLAN.md`, `docs/ERROR_LEDGER.md` — but these are a **NUMBER COLLISION**: main has its own unrelated `frontier/B775_phase2_wave1` and CAMPAIGN_STATUS's "B775" is main's own dark-hyperbola arc ("all four historical misses (quine/B762, stabilizations/B767, locks/B1003, dark-hyperbola/B775-B778)"). The branch's "braver questions" content is **ABSENT** from main under this number. |
| B783_observer_ground_zero | "# B783: THE OBSERVER GROUND-ZERO — FINDINGS" | Hits `docs/progress/REVIEWS.md`, `docs/views/CLOSED_DOORS.md`, `docs/views/THE_SPINE.md` — again a **NUMBER COLLISION**, in fact a double one: main's own spine lists a *different* `test_b783_c23.py` (measurement-torsor topic, THE_SPINE.md:909), and CLOSED_DOORS/THE_SPINE separately reference a *third* "cc3's B783" (reversal/Fibonacci-letter-frequency mechanism, refuted by main's own B802 — THE_SPINE.md:931: *"Independently reproduced the mechanism behind cc3's B783: reversal leaves the Fibonacci letter frequencies unchanged"*). None of the three is the branch's "observer ground-zero." **ABSENT** under this number. |
| B784_trace_map_intertwining | "# B784: THE TRACE-MAP INTERTWINING — FINDINGS" | Hits `docs/CAMPAIGN_STATUS.md`, `docs/ERROR_LEDGER.md`, `docs/LAW_MAP.md` — a third **NUMBER COLLISION**: main's own ERROR_LEDGER documents *"the B784 audit (2026-07-24)"* (an E27 vacuous-verdict sweep over B780/B781/B782/CL-LATIN) and CAMPAIGN_STATUS separately says *"cc3's own B784 refuted"* — neither is the branch's "trace-map intertwining." **ABSENT** under this number. |
| B792_maass_m004_eigenvalues | "# B792: THE MAASS EIGENVALUES OF m004 — COMPUTED IN-SANDBOX" | Hits `docs/ERROR_LEDGER.md`, `docs/INPUT_COMPLETENESS_LEDGER.md`, `docs/LAW_MAP.md` — genuine same-topic coverage, and the arc's own files are vendored verbatim under `frontier/B921_branch_harvest/harvested/frontier/B792_maass_m004_eigenvalues/` on main. LAW_MAP quote: *"UPGRADE PATH REALISED 2026-07-29 (B792/B797): the discrete newform Maass spectrum ... 17 eigenvalues computed in-sandbox ... independently verified 7/7 (B795)"*. **HARVESTED.** |
| B796_coupling_campaign | "# B796 WAVE-1 FINDINGS (interim; prereg sealed 8424a335 before compute)" (from `WAVE1_FINDINGS.md`; no top-level plain `FINDINGS.md` — the arc also nests `2t_base_rate/FINDINGS.md` = "# THE BASE-RATE CONTROL — the 2T atom is generic") | Hits `docs/ATTRIBUTION_BASELINE.json`, `docs/CAMPAIGN_STATUS.md`, `docs/ERROR_LEDGER.md` — genuine same-topic coverage, and the whole arc directory is vendored under `frontier/B921_branch_harvest/harvested/frontier/B796_coupling_campaign/` on main. CAMPAIGN_STATUS: *"B796 (coupling) — launch-approved, falsifier declared"*; ERROR_LEDGER's E32 row discusses the same campaign's premise in detail. **HARVESTED.** |
| tierB_opening | "# PREREGISTRATION — B518 Tier B, the gap-OPENING table, tested properly" (`PREREGISTRATION.md`; the arc's own `P0-0_GENERICITY_CONTROL.md` headline: "# P0-0 — THE GENERICITY CONTROL. Verdict: NOT DESIGNABLE from what is banked...") | Hits `docs/CAMPAIGN_STATUS.md`, `docs/CLOSURE_2026-07-11.md`, `docs/COSMOLOGY_LEDGER.md`, `docs/LAW_MAP.md`, `docs/OPEN_LEADS.md` on the search term `B518`. Main's `LAW_MAP.md` carries a live, THEOREM-grade `B518` row ("THE κ-UNIFICATION... B518: κ is a substrate-independent, scale-free universality class") — the same conceptual family (metallic/Tier-B universality) but no direct evidence the specific bronze/silver-geometricity scripts in this directory were themselves ported. **CITED**, not confirmed HARVESTED. |

### Root relay files (`*_TO_*.md`) present on the braver-questions branch head

151 files (`git ls-tree --name-only origin/audit/b775-braver-questions | grep -E "_TO_.*\.md$"`):

CC3_TO_CC_2026-07-22_p3_complete.md, CC3_TO_CC_2026-07-23_forks_verification.md,
CC3_TO_CC_2026-07-28_gate_items_closed_and_prediction_decided.md,
CC3_TO_CC_2026-07-28_last_door_closed.md, CC3_TO_CC_2026-07-28_m004_eigenvalues.md,
CC3_TO_CC_2026-07-28_rank4_response.md,
CC3_TO_CC_2026-07-29_B796_masterplan_for_gate.md,
CC3_TO_CC_2026-07-29_chat1_review_processed.md,
CC3_TO_CC_2026-07-29_context_sweep_escalations.md,
CC3_TO_CC_2026-07-29_e21_norm_levels_and_b727_prior.md,
CC3_TO_CC_2026-07-29_wave1_closeout.md,
CC3_TO_CC_2026-08-03_HANDOFF_wave1_cell9.md,
CC3_TO_CC_2026-08-05_LOSS_AUDIT_full_report.md,
CC3_TO_CC_2026-08-06_D2_D5_complete.md,
CC3_TO_CC_2026-08-06_D2_gate8r2a_discharge_note.md,
CC3_TO_CC_2026-08-06_D5_m003_mod4_amendment.md,
CC3_TO_CC_2026-08-08_ACCOUNTING_573.md, CC3_TO_CC_2026-08-08_LEADS_TRIAGE.md,
CC3_TO_CC_2026-08-08_RELATIONAL_REREAD.md,
CC3_TO_CC_2026-08-08_RENDER_AUDIT_corrections.md,
CC3_TO_CC_2026-08-09_CORNERSTONE.md, CC3_TO_CC_2026-08-09_CORNERSTONE_PLAN.md,
CC3_TO_CC_2026-08-09_COVER_four_relays.md, CC3_TO_CC_2026-08-09_DAY_LOG.md,
CC3_TO_CC_2026-08-09_FRAMEWORK_DELTA.md, CC3_TO_CC_2026-08-09_GENESIS_STRATUM.md,
CC3_TO_CC_2026-08-09_HARVEST_MANIFEST.md, CC3_TO_CC_2026-08-09_L114_DISCHARGE.md,
CC3_TO_CC_2026-08-09_PATH_BEYOND_THE_WALL.md,
CC3_TO_CC_2026-08-09_PROGRAMME_ASSEMBLY.md,
CC3_TO_CC_2026-08-09_REVIVABLE_rationale.md, CC3_TO_CC_2026-08-09_STEPPING_BACK.md,
CC3_TO_CC_2026-08-09_UNEXPLORED_LEADS.md, CC3_TO_CC_2026-08-10_CAMPAIGN_VERDICT.md,
CC3_TO_CC_2026-08-10_CONTENT_CAMPAIGN.md, CC3_TO_CC_2026-08-10_CONTENT_LEDGER.md,
CC3_TO_CC_2026-08-10_FALSIFIERS_SEALED.md, CC3_TO_CC_2026-08-10_FALSIFIERS_VERDICT.md,
CC3_TO_CC_2026-08-10_FIREWALL_STATUS.md, CC3_TO_CC_2026-08-10_HEDGE_ADJUDICATION.md,
CC3_TO_CC_2026-08-10_K_BLINDNESS.md, CC3_TO_CC_2026-08-10_LINES_AND_BUDGET.md,
CC3_TO_CC_2026-08-10_PREDICTION_REGISTER.md, CC3_TO_CC_2026-08-10_RECOMMENDATION.md,
CC3_TO_CC_2026-08-10_THETA_WITHDRAWN.md, CC3_TO_CC_2026-08-10_THE_WALL_IS_MALFORMED.md,
CC3_TO_CC_2026-08-10_THREE_GENERATIONS.md, CC3_TO_CC_2026-08-10_THREE_SEAT_PROTOCOL.md,
CC3_TO_CC_2026-08-10_Z2_MERGE.md, CC3_TO_CC_2026-08-11_ATRISK_CENSUS_NEGATIVE.md,
CC3_TO_CC_2026-08-11_COMPLETE_PICTURE.md, CC3_TO_CC_2026-08-11_GAUGE_VS_INVARIANT.md,
CC3_TO_CC_2026-08-11_H1_BLOCK_COUNT_CLOSED.md,
CC3_TO_CC_2026-08-11_KAPPA_AND_THE_PI6_CLUSTER.md,
CC3_TO_CC_2026-08-11_L135_L142_AND_THE_FRAME_INSTRUMENT.md,
CC3_TO_CC_2026-08-11_OWED_DISPOSITIONS.md,
CC3_TO_CC_2026-08-11_PACKET_TASKS_2_AND_3.md, CC3_TO_CC_2026-08-11_PI6_ADJUDICATED.md,
CC3_TO_CC_2026-08-11_RETRACTION_L154.md, CC3_TO_CC_2026-08-11_THE_THREE_DISSOLVES.md,
CC3_TO_CC_2026-08-11_TONE_SET_CORRECTION.md,
CC3_TO_CC_2026-08-11_TWO_TESTS_NOT_ONE.md, CC3_TO_CC_2026-08-11_WINDOW_HANDOFF.md,
CC3_TO_CC_2026-08-11_WINDOW_MANIFEST.md,
CC3_TO_CC_2026-08-12_ADVERSARIAL_B1031_B1028.md,
CC3_TO_CC_2026-08-12_CLAIM_DROP_HELDOUT.md,
CC3_TO_CC_2026-08-12_CONSOLIDATION_PASS_3.md,
CC3_TO_CC_2026-08-12_DIGEST_PROTOCOL_RECOMMENDATION.md,
CC3_TO_CC_2026-08-12_ODYSSEY_CODA.md,
CC3_TO_CC_2026-08-12_REVIEW_INPUT_THE_AUDIT_SEAT.md,
CC3_TO_CC_2026-08-12_S034_QUERY.md, CC3_TO_CC_2026-08-12_SLANSKY_27CUBED.md,
CC3_TO_CC_2026-08-12_TASK1_LITERATURE.md,
CC3_TO_CC_2026-08-12_TASKB_FIELD_LITERATURE.md,
CC3_TO_CC_2026-08-12_TASKC_PHASE_B.md, CC3_TO_CC_2026-08-12_TASKC_PHASE_C_VERDICT.md,
CC3_TO_CC_2026-08-12_THE_CUBE_LEAD_SHARPENED.md,
CC3_TO_CC_2026-08-12_THE_FIELD_LADDER.md,
CC3_TO_CC_2026-08-12_THE_FRAMEWORK_CHALLENGED.md,
CC3_TO_CC_2026-08-12_THE_SCALE_FACTORISATION.md,
CC3_TO_CC_2026-08-12_THE_TRIT_CANDIDATES.md, CC3_TO_CC_2026-08-12_X7_PRIOR_ART.md,
CC3_TO_CC_2026-08-13_A2_ALREADY_LANDED_AND_A8_WARNING.md,
CC3_TO_CC_2026-08-13_A8_CONFIRMED_AND_MY_TYPING_WAS_X_ONLY.md,
CC3_TO_CC_2026-08-13_A8_FENCE_CLOSED_M5_COMPLETE.md,
CC3_TO_CC_2026-08-13_A8_PRIMING_CAVEAT.md, CC3_TO_CC_2026-08-13_BLOCKER_SCRUTINY.md,
CC3_TO_CC_2026-08-13_BRIDGE_CELL_V2_INPUT.md,
CC3_TO_CC_2026-08-13_BRONZE_ATTACK_SURFACE_1_KILLS_IT.md,
CC3_TO_CC_2026-08-13_BRONZE_VERIFIED_INVERSION_DEAD.md,
CC3_TO_CC_2026-08-13_CORRECTION_I_AUDITED_A_SEGMENT_AND_CALLED_IT_THE_CHAIN.md,
CC3_TO_CC_2026-08-13_DEBTS_PAID.md,
CC3_TO_CC_2026-08-13_DISCREPANCY_TRIAGE_PRESTATED.md,
CC3_TO_CC_2026-08-13_FULL_FIELD_A2_SURVIVES.md,
CC3_TO_CC_2026-08-13_ITEM4_REOPENS_THE_77.md,
CC3_TO_CC_2026-08-13_ITEM5_BODY_LEVEL_AND_THE_NEAR_MISS.md,
CC3_TO_CC_2026-08-13_ITEM5_PRIOR_ART_UNRESOLVED.md,
CC3_TO_CC_2026-08-13_ITEM5_SLODOWY_NEIGHBOURHOOD_CLEAN.md,
CC3_TO_CC_2026-08-13_ITEM5_THE_THIRD_STATE.md,
CC3_TO_CC_2026-08-13_L161_VS_THE_THREE_DOORS.md,
CC3_TO_CC_2026-08-13_L162_V0_GROUP_MISMATCH.md, CC3_TO_CC_2026-08-13_L164_ATTACK.md,
CC3_TO_CC_2026-08-13_PART0_LINE1_THE_PRICES_ARE_REAL_TWO_ARE_UNLOCKED.md,
CC3_TO_CC_2026-08-13_PART0_LINE2_TWO_CHECKLISTS.md,
CC3_TO_CC_2026-08-13_PART0_LINE3_THE_GATE_IS_AN_OUTPUT_FIREWALL.md,
CC3_TO_CC_2026-08-13_STOP_A5_IS_NOT_CERTIFIED.md,
CC3_TO_CC_2026-08-13_SWEEP_6_7_8_AND_ONE_K.md,
CC3_TO_CC_2026-08-13_SWEEP_ITEMS_0_AND_1.md,
CC3_TO_CC_2026-08-13_SWEEP_ITEMS_4_5.md,
CC3_TO_CC_2026-08-13_SWEEP_ITEM_2_AND_THE_STRUCTURAL_REASON.md,
CC3_TO_CC_2026-08-13_SWEEP_TRIAGE_COMPLETE_19_OF_19.md,
CC3_TO_CC_2026-08-13_THE_NOVELTY_BUDGET_IS_ONE_STEP.md,
CC3_TO_CC_2026-08-13_THE_TYPE_LEGAL_INVENTORY.md,
CC3_TO_CC_2026-08-13_TYPING_IS_COORDINATE_DEPENDENT.md,
CC3_TO_CC_2026-08-13_V0_CLOSED_POSITIVE.md,
CC3_TO_CC_2026-08-13_V2_M1_ARM_IS_FORCED.md,
CC3_TO_CC_2026-08-14_DOORWAY_CORRECTION.md,
CC3_TO_CC_2026-08-14_THE_FORCEDNESS_ARGUMENT.md,
CC3_TO_CHAT1_2026-08-10_GAP1_ACCEPTED.md, CC_TO_CC3_2026-07-25_S_gated_and_direction.md,
CC_TO_CC3_2026-07-25_b784_theta_bridge_correction.md,
CC_TO_CC3_2026-07-25_five_branch_gate.md,
CC_TO_CC3_2026-07-25_full_processing_and_n7n8.md,
CC_TO_CC3_2026-07-25_gate_status.md, CC_TO_CC3_2026-07-25_rank4_gated.md,
CC_TO_CC3_2026-07-28_APPROVED_harvested_B789.md,
CC_TO_CC3_2026-07-28_B792_gate_51014_resolved_and_a_classification_error.md,
CC_TO_CC3_2026-07-28_B793_collision_and_a_logical_error.md,
CC_TO_CC3_2026-07-28_MAASS_numbering_and_replication.md,
CC_TO_CC3_2026-07-28_PREDICTION_r8863_is_parent.md,
CC_TO_CC3_2026-07-28_URGENT_hold_sm_comparison.md,
CC_TO_CC3_2026-07-28_URGENT_provenance_failure_51014.md,
CC_TO_CC3_2026-07-28_hejhal_DONT_STOP_plus_free_control.md,
CC_TO_CC3_2026-07-28_per_cell_falsifiers_are_not_enough.md,
CC_TO_CC3_2026-07-28_q_RETRACTION.md, CC_TO_CC3_2026-07-28_q_defense_gate.md,
CC_TO_CC3_2026-07-28_sm_null_gated.md,
CC_TO_CC3_2026-07-29_CONTEXT_BUILD_and_work_split.md,
CC_TO_CC3_2026-07-29_GATE_VERDICT_and_the_forwardable_problem.md,
CC_TO_CC3_2026-07-29_chat1_masterplan_review_three_items.md,
CC_TO_CC3_2026-07-29_dynamics_gap_NOT_filled_plus_your_falsifier.md,
CC_TO_CC3_2026-07-29_masterplan_gate.md,
CC_TO_CC3_2026-07-29_registered_leads_your_campaign_should_attach_to.md,
CC_TO_CC3_2026-07-29_your_deltas_ACCEPTED_and_D2_overturns_us_both.md,
CC_TO_CC3_2026-08-10_PATH_TRIAGE.md, CC_TO_CC3_2026-08-10_PHASE1B_OPEN.md,
CC_TO_CC3_2026-08-10_PHASE2_CC_RESPONSE.md, CC_TO_CC3_2026-08-10_PIN_V2.md,
CC_TO_CC3_2026-08-10_PROTOCOL_CONFIRMED.md, CC_TO_CC3_2026-08-10_RECOUNT_ACCEPTED.md,
CC_TO_CC3_2026-08-11_HANDOFF_REQUEST.md

---

## Part 3 — The consolidation seat: arcs not on main's head

`git ls-tree --name-only <consolidation branch> frontier/` has 1029 top-level
entries. 30 of them (`B1025`–`B1054`) are absent from main's 1246-entry
`frontier/` listing under the consolidation branch's own directory names — because
main independently minted its own, differently-named arcs at the same numbers.
This exact collision (and its resolution) is already documented on main in
`docs/CLOUD_ALIAS_TABLE.md`, confirmed independently below.

| id (consolidation branch) | headline verbatim | scripts present | main REUSED the number? |
|---|---|---|---|
| B1025_suite_collection_repair | "# B1025 — THE SUITE DID NOT RUN: three unguarded optional imports aborted collection, and the gate that should have caught it measures the wrong thing" | *(none)* | **NUMBER COLLISION** — main's B1025_input_derivability: "# B1025 — L155, the input-derivability audit: three SURVIVE, two NARROW — and the \"Lie-valued input\" dissolves into unique lines" |
| B1026_the_one_involution | "# B1026 — ONE INVOLUTION, SIX NAMES: the substrate record swap IS the sl(n) opposition involution, and its first link is an axiom outside A1–A6" | verify.py | **NUMBER COLLISION** — main's B1026_nomination: "# B1026 — the nomination: T4 at 2.0 bits, and the seal killed its own author's first draft" |
| B1027_kappa_two_faces | "# B1027 — κ = 2 IS THE FREE CHAIN: the founding sentence's \"nothing\" has three banked meanings, and the curated layer carried one" | compute.py | **NUMBER COLLISION** — main's B1027_fourth_crossing: "# B1027 — THE FOURTH CROSSING: ALL-MISS, powered in both sectors — and the leptonic margin is ONE DEGREE" |
| B1028_kappa_absolutely_conserved | "# B1028 — κ = 2 IS ABSOLUTELY CONSERVED: every endomorphism of F₂ scales κ − 2, and the information-losing ones land *inside* \"nothing\"" | compute.py | **NUMBER COLLISION** — main's B1028_freedom_ledger: "# B1028 — FINDINGS: the global freedom ledger" |
| B1029_seam_class_field | "# B1029 — THE SEAM IS NOT A THIRD FACE: its Hilbert class field *is* the two ends" | compute.py | **NUMBER COLLISION** — main's B1029_invariant_ring: "# B1029 — FINDINGS: the invariant ring of the frame action on the coupling data" |
| B1030_input_typing_audit | "# B1030 — the counted input list, audited: **one continuous dimensionless input, not zero** — and the two \"fives\" are different fives" | verify.py | **NUMBER COLLISION** — main's B1030_price_lock_verification: "# B1030 — FINDINGS: the price-lock verification (the trit adopted, with its exact cost)" |
| B1031_generation_rung | "# B1031 — three generations: **structural, not derived** — and the ladder had no rung for it" | verify.py | **NUMBER COLLISION** — main's B1031_two_thirds_meets_the_voice: "# B1031 — FINDINGS: the two-thirds theorem meets the voice" |
| B1032_across_breakings_route | "# B1032 — the across-breakings route: **two sealed cells B307 does not touch** — and B1031's own rung corrected" | verify.py | **NUMBER COLLISION** — main's B1032_type_law: "# B1032 — FINDINGS: the resolution bound verified, amended, and banked as THE TYPE LAW" |
| B1033_register_reconciliation | "# B1033 — the second debt register meets the first, and the gated one **cannot see two-thirds of the corpus**" | verify.py | **NUMBER COLLISION** — main's B1033_generation_adjudication: "# B1033 — FINDINGS: THE GENERATION ADJUDICATION — the flavor reading is CHIRAL, the walls stand, the orbit anchor fails" |
| B1034_two_kappas | "# B1034 — **κ names two quantities**, and one of them is exported by the certified core" | verify.py | **NUMBER COLLISION** — main's B1034_l154_sigma: "# B1034 — FINDINGS: L154 lands UNDECIDED — SAME is unobstructed, unexhibited, and now precisely priced" |
| B1035_shadow_library | "# B1035 — the shadow library, the orphaned core, and one non-finding" | verify.py | **NUMBER COLLISION** — main's B1035_receipts_and_register: "# B1035 — FINDINGS: the two HELD receipts unblocked, verified, and the falsifier register brought to main" |
| B1036_knowledge_room | "# B1036 — the knowledge room: the firewall runs backwards in five places, and nobody could see it" | verify.py | **NUMBER COLLISION** — main's B1036_mirror_double: "# B1036 — FINDINGS: the double gains classes, not the symmetric pairing" |
| B1037_band_B100_dispositioned | "# B1037 — the B100–B199 band dispositioned: **37 rows are 17 statements**" | verify.py | **NUMBER COLLISION** — main's B1037_theta_join: "# B1037 — FINDINGS: the θ-join is DISTINCT — the prior was wrong, and the record holds it" |
| B1038_tower_restored | "# B1038 — the tower cluster restored: **two Sym bands, and the fit is unique at n = 4**" | verify.py | **NUMBER COLLISION** — main's B1038_retrieval_typing: "# B1038 — FINDINGS: the census reproduces exactly; the retrieval instruments install" |
| B1039_phi_fixed_and_metallic_exponent | "# B1039 — two clusters restored, and **re-verifying them found two defects in what was about to be restored**" | verify.py | **NUMBER COLLISION** — main's B1039_v_valued_residual: "# B1039 — FINDINGS: the V-valued sector is EMPTY — the wall is now sector-complete on the double" |
| B1040_isomonodromy_restored | "# B1040 — the isomonodromy cluster restored, and the cluster's own `[exact]` tag does not survive contact" | verify.py | **NUMBER COLLISION** — main's B1040_fl4_observer_battery: "# B1040 — FL-4: THE OBSERVER CONSTRUCTION THROUGH THE BATTERY — the ledger splits every step..." |
| B1041_the_red_locks | "# B1041 — three red locks, and the one reason none of them was seen" | verify.py | **NUMBER COLLISION** — main's B1041_theta_leg: "# B1041 — PM1: THE θ-LEG — EXHIBITED, with a typed obstruction..." |
| B1042_the_error_ledger | "# B1042 — the corpus names its lessons where it finds them, and the register that generalises them stopped 122 arcs ago" | verify.py | **NUMBER COLLISION** — main's B1042_trit_morphism: "# B1042 — PM3: THE TRIT MORPHISM — JOINED: the trit's ℤ/3 is ω's ℤ/3 carried through McKay..." |
| B1043_the_band_is_the_wrong_unit | "# B1043 — the band is the wrong unit, and it made this refresh restore a settled question as open" | verify.py | **NUMBER COLLISION** — main's B1043_triple_assembly: "# B1043 — PM2: THE TRIPLE ASSEMBLY — h¹ = 10 = 7 + 3..." |
| B1044_law_siblings_gated | "# B1044 — the topic search per restoration, made mechanical" | verify.py | **NUMBER COLLISION** — main's B1044_gamma_ledger: "# B1044 — THE Γ-LEDGER: the Γ-column is EMPTY — B803's address closes..." |
| B1045_middle_band_mapped | "# B1045 — the instrument's first measured miss, and why the middle band is MAPPED and not dispositioned" | verify.py | No — `frontier/B1045*` does not exist on main at all (main's `docs/CLOUD_ALIAS_TABLE.md` marks B1045–B1059 "RESERVED — never assigned on main") |
| B1046_the_arc_graph | "# B1046 — the arc graph does not carry what the bodies know" | verify.py | No — same reserved band |
| B1047_the_seam_cluster | "# B1047 — the seam cluster dispositioned from the bodies: the headline is refuted, the mechanism survives" | verify.py | No — same reserved band |
| B1048_the_seam_cluster_closed | "# B1048 — the seam cluster CLOSED, and the scale wall's real proof was sitting uncurated" | verify.py | No — same reserved band |
| B1049_the_wrapped_exclusion | "# B1049 — the full suite found five red locks that 94 targeted tests did not" | verify.py | No — same reserved band |
| B1050_the_projective_wall | "# B1050 — the projective quotient is fully natural, and still not a selector" | verify.py | No — same reserved band |
| B1051_the_band_closed | "# B1051 — B0–B99 closed: the fixed line is Dickson, and two siblings the instrument could not see" | verify.py | No — same reserved band |
| B1052_the_handoff | "# B1052 — the refresh exits through a manual, and the manual is checked against the corpus" | verify.py | No — same reserved band |
| B1053_the_unread_handoffs | "# B1053 — the handoffs I wrote into but had not read" | verify.py | No — same reserved band |
| B1054_review_one | "# B1054 — Review 1: the consolidation seat reviews its own window, and finds its own defect in it" | verify.py | No — main's `docs/CLOUD_ALIAS_TABLE.md` marks B1054–B1059 "RESERVED (buffer)... e.g. their Review 1" — main never minted a B1054 |

All 20 collisions (B1025–B1044) and all 10 non-collisions (B1045–B1054) confirm
exactly what `docs/CLOUD_ALIAS_TABLE.md` already states on main (banked
2026-08-12): *"The cloud consolidation seat's branch (the [consolidation branch —
name redacted per instruction]) forked
from main at B1024's seal commit (3524b889) and numbered its own arcs B1025–B1053
while main independently banked B1025–B1044. Twenty IDs (B1025–B1044) each name
TWO different arcs."*

### `docs/CLOUD_ALIAS_TABLE.md` coverage check

Read the full file on main. It carries a two-way table for B1025–B1044 (both
sides' directory-name suffixes, e.g. "B1025 | input_derivability |
suite_collection_repair"), then a row: *"B1045–B1053 | RESERVED (never assigned
on main) | middle_band_mapped · the_arc_graph · the_seam_cluster ·
the_seam_cluster_closed · the_wrapped_exclusion · the_projective_wall ·
the_band_closed · the_handoff · the_unread_handoffs"* — naming all nine
consolidation-branch suffixes for B1045–B1053 exactly. B1054 is covered by the
adjacent sentence in the same document's "numbering rule" section: *"B1054–B1059
are buffer for their branch's own continuation, e.g. their Review 1"* — which
names "Review 1" directly, i.e. `B1054_review_one`.

**Result: zero consolidation-branch arc ids (of the 30 checked) are absent from
`docs/CLOUD_ALIAS_TABLE.md`.** Every one of B1025–B1054 is named or covered by an
explicit range statement in that file.
