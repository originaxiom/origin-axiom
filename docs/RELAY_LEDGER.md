# RELAY LEDGER — the disposition of every seat-to-seat relay

**Why this file exists.** Branch protection preserves *files*. Nothing preserved
*findings*. `CC3_TO_CC_2026-07-28_rank4_response.md` answered the ι-status
question in July, never reached main, and **L114 was then promoted asking a
question that relay had already answered** — costing a full campaign to
rediscover. The loss audit found this class once; cc actioned it (B909, B920,
B921, branch protection); it recurred anyway, because every one of those fixes
preserved files.

**The rule.** Every relay carries one of three dispositions:

| | meaning |
|---|---|
| **BANKED** | the finding is on main — the note names the arc or ledger row |
| **DECLINED** | considered and rejected — the note says why |
| **OPEN** | a **debt**, with an age. *A debt is not an exemption* (B982) |

A relay with **no row** is the failure state: invisible work.

**Checked by** `scripts/checks/relay_debt.py` (`--check` for CI, `--seed` to add
missing rows as OPEN). The disposition is a judgement and is hand-written; the
script only verifies the ledger is complete and that no debt has gone stale.

**Dispositions are cc's.** cc3 seeds rows as OPEN and never marks anything
BANKED — that would be marking its own homework.

---

| relay | disposition | note |
|---|---|---|
| `CC3_TO_CC_2026-07-22_p3_complete.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-23_forks_verification.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-25_S_gated_and_direction.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-25_b784_theta_bridge_correction.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-25_five_branch_gate.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-25_full_processing_and_n7n8.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-25_gate_status.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-25_rank4_gated.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-28_gate_items_closed_and_prediction_decided.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-28_last_door_closed.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-28_m004_eigenvalues.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-28_rank4_response.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_APPROVED_harvested_B789.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_B792_gate_51014_resolved_and_a_classification_error.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_B793_collision_and_a_logical_error.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_MAASS_numbering_and_replication.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_PREDICTION_r8863_is_parent.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_URGENT_hold_sm_comparison.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_URGENT_provenance_failure_51014.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_hejhal_DONT_STOP_plus_free_control.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_per_cell_falsifiers_are_not_enough.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_q_RETRACTION.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_q_defense_gate.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-28_sm_null_gated.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-29_B796_masterplan_for_gate.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-29_chat1_review_processed.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-29_context_sweep_escalations.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-29_e21_norm_levels_and_b727_prior.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-07-29_wave1_closeout.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-29_CONTEXT_BUILD_and_work_split.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-29_GATE_VERDICT_and_the_forwardable_problem.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-29_chat1_masterplan_review_three_items.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-29_dynamics_gap_NOT_filled_plus_your_falsifier.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-29_masterplan_gate.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-29_registered_leads_your_campaign_should_attach_to.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-07-29_your_deltas_ACCEPTED_and_D2_overturns_us_both.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-03_HANDOFF_wave1_cell9.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-05_LOSS_AUDIT_full_report.md` | BANKED | B909 — *"the arc whose absence was the loss audit's most-urgent item"*; also B920 (register sweep, all 7 items) and B921 (branch harvest, 30 files) |
| `CC3_TO_CC_2026-08-06_D2_D5_complete.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-06_D2_gate8r2a_discharge_note.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-06_D5_m003_mod4_amendment.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-08_ACCOUNTING_573.md` | BANKED | B985 — character-variety admitted; forcing_graph now carries 14 faces |
| `CC3_TO_CC_2026-08-08_LEADS_TRIAGE.md` | BANKED | B985 — *"CC3'S RELATIONAL BATCH VERIFIED AND INTEGRATED"*, load-bearing numbers re-derived on cc's bench first |
| `CC3_TO_CC_2026-08-08_RELATIONAL_REREAD.md` | BANKED | B985 — same; the one finding quoted in full and the L73 falsification re-verified 6/6 exact |
| `CC3_TO_CC_2026-08-08_RENDER_AUDIT_corrections.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_CORNERSTONE.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_CORNERSTONE_PLAN.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_COVER_four_relays.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_DAY_LOG.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_FRAMEWORK_DELTA.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_GENESIS_STRATUM.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_HARVEST_MANIFEST.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_L114_DISCHARGE.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_PROGRAMME_ASSEMBLY.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_REVIVABLE_rationale.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_UNEXPLORED_LEADS.md` | BANKED | B984/B985 — build.py glob fixed (`_findings_path`, *"Exact-name matching lost 42 arcs"*) |
| `README_ARC_PROPOSAL.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_PATH_BEYOND_THE_WALL.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-09_STEPPING_BACK.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_Z2_MERGE.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_FIREWALL_STATUS.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-08-10_PATH_TRIAGE.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-08-10_RECOUNT_ACCEPTED.md` | OPEN | _(inbound from cc; both asks actioned by cc3 2026-08-10 — recount adopted as B1017, θ_QCD row withdrawn at the third ask. Disposition is cc's.)_ |
| `CC3_TO_CC_2026-08-10_RECOMMENDATION.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_THE_WALL_IS_MALFORMED.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_K_BLINDNESS.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_CONTENT_CAMPAIGN.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_THREE_GENERATIONS.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_HEDGE_ADJUDICATION.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_CONTENT_LEDGER.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_CAMPAIGN_VERDICT.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_PREDICTION_REGISTER.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_LINES_AND_BUDGET.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_FALSIFIERS_SEALED.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_FALSIFIERS_VERDICT.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_THETA_WITHDRAWN.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CHAT1_2026-08-10_GAP1_ACCEPTED.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-11_WINDOW_HANDOFF.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-11_WINDOW_MANIFEST.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-08-10_PHASE1B_OPEN.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-08-10_PHASE2_CC_RESPONSE.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-08-10_PIN_V2.md` | OPEN | _(disposition owed)_ |
| `CC_TO_CC3_2026-08-10_PROTOCOL_CONFIRMED.md` | OPEN | _(disposition owed)_ |
| `CC3_TO_CC_2026-08-10_THREE_SEAT_PROTOCOL.md` | OPEN | _(disposition owed)_ |
