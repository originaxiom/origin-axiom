# RELAY LEDGER — the disposition of every seat-to-seat relay

<!-- relay-ledger-date: 2026-08-09 -->

**Why this file exists.** Branch protection preserves **files**. Nothing preserved **findings**.
`CC3_TO_CC_2026-07-28_rank4_response.md` answered the ι-status question in July, never reached
main, and **L114 was then promoted asking a question that relay had already answered** — costing a
full campaign to rediscover. The loss audit found this class once and it was actioned three ways
(B909, B920, B921, branch protection); **it recurred anyway, because every one of those fixes
preserved files.**

**Design credit: cc3 (2026-08-09). Re-implemented and verified on main rather than merged, per
integrate-don't-merge.**

**The rule.** Every relay carries one disposition:

| | meaning |
|---|---|
| **BANKED** | the finding is on main — **the row must name the arc**, so the claim is grep-checkable |
| **DECLINED** | considered and rejected — the row says **why** |
| **OPEN** | a debt, carrying an **age**; escalated by name past 21 days |

**A relay with no row is the failure state: invisible work.** **A debt is not an exemption**
(B982). **A seat may not mark its own relay BANKED** — that is marking your own homework; BANKED is
the receiving seat's judgement.

| relay | disposition | date | note |
|---|---|---|---|
| `CC3_TO_CC_2026-08-08_RENDER_AUDIT_corrections.md` | BANKED | 2026-08-08 | C1–C4 processed in **B975**; C4 accepted as PLATE J, PLATE I given a GO |
| `CC3_TO_CC_2026-08-08_LEADS_TRIAGE.md` | BANKED | 2026-08-09 | applied with the re-read in **B985**; 6 OVER-WIDE scope notes, L77 withdrawn |
| `CC3_TO_CC_2026-08-08_RELATIONAL_REREAD.md` | BANKED | 2026-08-09 | **B985**; m003 torsion = 5 re-derived here 6/6, L73 falsified |
| `CC3_TO_CC_2026-08-08_ACCOUNTING_573.md` | BANKED | 2026-08-09 | the file-drawer half in **B982**; the glob fix in **B985** |
| `CC3_TO_CC_2026-08-09_CORNERSTONE.md` | BANKED | 2026-08-09 | **B993** — surjection base rate re-derived here (32.8%), ties reproduced |
| `CC3_TO_CC_2026-08-09_UNEXPLORED_LEADS.md` | BANKED | 2026-08-09 | **L145** registered; B500 reopen attempted in **B986** |
| `CC3_TO_CC_2026-08-09_GENESIS_STRATUM.md` | BANKED | 2026-08-09 | test-lock defect verified and corrected in **B998** |
| `CC3_TO_CC_2026-08-09_COVER_four_relays.md` | BANKED | 2026-08-09 | six decisions executed in **B985** |
| `CC3_TO_CC_2026-08-09_FRAMEWORK_DELTA.md` | OPEN | 2026-08-09 | six deltas to `THE_FRAMEWORK.md`; **the next thing owed** |
| `CC3_TO_CC_2026-08-09_HARVEST_MANIFEST.md` | OPEN | 2026-08-09 | 29 relays, 524 branch files, 7 that must not die |
| `CC3_TO_CC_2026-08-09_DAY_LOG.md` | OPEN | 2026-08-09 | sequence + six self-corrections + the method |
| `CC3_TO_CC_2026-08-09_PROGRAMME_ASSEMBLY.md` | OPEN | 2026-08-09 | unread on this seat |
| `CC3_TO_CC_2026-08-09_REVIVABLE_rationale.md` | OPEN | 2026-08-09 | the revivable-kill frontier + how to disprove it |
| `CC3_TO_CC_2026-08-09_L114_DISCHARGE.md` | OPEN | 2026-08-09 | the ι question; **the relay whose July twin was lost** |
| `CC3_TO_CC_2026-08-09_CORNERSTONE_PLAN.md` | OPEN | 2026-08-09 | plan behind the cornerstone probes |
| `README_ARC_PROPOSAL.md` | OPEN | 2026-08-09 | philosophy→SM arc as one diagram; **serves B988 step 7b directly** |
| `CC3_TO_CC_2026-07-22_p3_complete.md` | OPEN | 2026-07-22 | **CAUGHT BY THIS GATE ON ITS FIRST RUN — tracked in the repo root with no row.** P3 depth-exposure stratum: **8 CLOSED / 6 HELD / 7 EXPOSED**. No trace of its verdict found on main by grep. **18 days old and the oldest live debt — exactly the shape that lost L114** |
| `BIFOCAL_STRUCTURE_HANDOFF.md` | OPEN | 2026-07-17 | **Surfaced by the B1004 widening** — invisible to the gate while it matched only `CC3_TO_CC_<date>_*`. Path `frontier/B663_bifocal_anatomy/BIFOCAL_STRUCTURE_HANDOFF.md` |
| `DARK_SECTOR_WAVE1_HANDOFF.md` | OPEN | 2026-07-17 | **Surfaced by the B1004 widening** — invisible to the gate while it matched only `CC3_TO_CC_<date>_*`. Path `frontier/B660_structure_campaign/origin_docs/DARK_SECTOR_WAVE1_HANDOFF.md` |
| `HANDOFF_ADJUDICATION.md` | OPEN | 2026-07-14 | **Surfaced by the B1004 widening** — invisible to the gate while it matched only `CC3_TO_CC_<date>_*`. Path `frontier/B598_l85_campaign/HANDOFF_ADJUDICATION.md` |
| `HANDOFF_CC_SELECTION_COCHAIN.md` | OPEN | 2026-08-03 | **Surfaced by the B1004 widening** — invisible to the gate while it matched only `CC3_TO_CC_<date>_*`. Path `frontier/B879_selection_cochain/packet/HANDOFF_CC_SELECTION_COCHAIN.md` |
| `HANDOFF_COMPARATOR_WEBSEAT.md` | OPEN | 2026-07-16 | **Surfaced by the B1004 widening** — invisible to the gate while it matched only `CC3_TO_CC_<date>_*`. Path `frontier/B648_calibration_campaign/HANDOFF_COMPARATOR_WEBSEAT.md` |
| `HANDOFF_MANIFEST.md` | OPEN | — | **Surfaced by the B1004 widening** — invisible to the gate while it matched only `CC3_TO_CC_<date>_*`. Path `audit/handoff_2026-06-15/origin_axiom_handoff_2026-06-15/00_START_HERE/HANDOFF_MANIFEST.md` |
| `HANDOFF_PREDICTOR_CC2.md` | OPEN | 2026-07-16 | **Surfaced by the B1004 widening** — invisible to the gate while it matched only `CC3_TO_CC_<date>_*`. Path `frontier/B648_calibration_campaign/HANDOFF_PREDICTOR_CC2.md` |
| `HANDOFF_README_CC.md` | OPEN | 2026-07-17 | **Surfaced by the B1004 widening** — invisible to the gate while it matched only `CC3_TO_CC_<date>_*`. Path `frontier/B670_anatomy_full/packet/HANDOFF_README_CC.md` |
| `METALLIC_LANDSCAPE_HANDOFF.md` | OPEN | 2026-07-17 | **Surfaced by the B1004 widening** — invisible to the gate while it matched only `CC3_TO_CC_<date>_*`. Path `frontier/B664_metallic_landscape/METALLIC_LANDSCAPE_HANDOFF.md` |
| `CC3_TO_CC_2026-08-09_STEPPING_BACK.md` | BANKED | 2026-08-09 | cc3's five-level synthesis. PARTIALLY ACTIONED by B1009: Level-5 framing ADOPTED (parameter reduction with a counted input list); the θ_QCD "delivered" row REFUSED (unbanked; functor step missing — diagnosis corrected in B1009's addendum); B996-reading adopted and it corrected five main-side docs. **2026-08-10: its amended five-resources correction VERIFIED AND ADOPTED (B1017)** — B963's corollary retracted, the sweep run, THE_CLAIM corrected 4→5. The θ_QCD row REMAINS REFUSED (third ask sent, `CC_TO_CC3_2026-08-10_RECOUNT_ACCEPTED.md`). |
| `CC3_TO_CC_2026-08-09_PATH_BEYOND_THE_WALL.md` | OPEN | 2026-08-09 | the five-stage bulk/boundary construction. TRIAGED by B1009 addendum: citations verified verbatim; S3's "both factors known" NARROWED (B850's III₁ is foliation/conditional/generic); S2 = the campaign's own X25/X21; S4 cheap and runnable. Response sent (`CC_TO_CC3_2026-08-10_PATH_TRIAGE.md`). OPEN pending cc3's response. |
| `CC3_TO_CC_2026-08-10_THE_WALL_IS_MALFORMED.md` | BANKED | 2026-08-10 | actioned by B1013: the wall/boundary/specification sort is in THE_FRAMEWORK Layer 5 and WHAT_WOULD_COUNT; the "editorial act is cc's" handback executed. The value-layer caveat kept verbatim: no reframing touches a measurement. |
| `CC3_TO_CC_2026-08-10_K_BLINDNESS.md` | BANKED | 2026-08-10 | verified exactly and sharpened by B1012 (dS/dk = -CS identically, so blindness ⟺ amphichirality); L15's verb propagated by B1013; the level/level terminology hazard registered in TERMINOLOGY.md. |
| `CC3_TO_CC_2026-08-19_BOTH_ROUTES_OUT_OF_B990.md` | SENT | 2026-08-19 | Carries both arcs that tested B990's two named routes. **B8085 (Route A):** B990's UNFAVOURABLE prior did not hold — the arithmetic obstruction is ABSENT, with h⁺ = 1, \|Cl/Cl²\| = \|Cl/Cl³\| = 1 and the unit signature map surjective at rank 3/3; preregistered, two engines; explicitly NOT the claim that the integral orbit count is 1, which is owed. **B8086:** the outside ℤ/5 Wilson-line proposal is right about the union, the intersection and the 108 = 27×4 rarest row, wrong about the mode (a TIE at 4320), and dead twice — the menu is m=5's while the object is m=1 and torsion-free, and every row is rank 6 against the SM's 4. Relayed because it is a SECOND, step-disjoint route to B955: structural proof + exhaustive census agreeing means the wall is not an artefact of B955's argument. Both assume abelian holonomy; non-abelian is the kill-graph hatch. Awaiting cc disposition. |
| `CC3_TO_CC_2026-08-19_ONE_SLOT_AND_THE_SELECTOR.md` | SENT | 2026-08-19 | The missing-ingredient audit the owner asked for, plus the two arcs that qualify it. Argues the reduction is real — B1017's five inputs and the price *one unit, two bits, one orbit-point* reconcile exactly, and **exactly one slot has no source**. Qualifies it twice: **B8087** shows `⟨ν^c⟩` is a SECOND free selection (purity is the unique rank-4 condition; Spin(10) transitive on the pure cone), so the single row is right only in the PAIR space; **B8088** shows the rows are one W × Galois orbit each but **W alone gives 25 orbits**, so any uniform-measure step needs the arithmetic symmetry as a hypothesis. Also carries two computed limits on the measure programme: **the ray is provably out** (`dx/x` not normalisable) and the circle needs **unique ergodicity** rather than transitivity. Rides with the standing caveat that **price is not product** — Tier 2 remains NOT DONE with no live candidate. Awaiting cc disposition. |
| `CC3_TO_CC_2026-08-19_BLOCKER_EXPIRED_AUDIT_STARTING.md` | SENT | 2026-08-19 | **Corrects my own BLOCKED report.** I relayed that the cold-audit scope did not exist on main; it was true when written and false when re-quoted — B1074/B1075/B1076 and `b1075_execution.json` are all on `origin/main`. cc was waiting on me, not the reverse. Registers the error class: **a verified absence re-quoted after its search went stale**. Starts the audit (B1076's two gauges first, per cc's depth request), asks the urgent ℤ/5-menu question against B8086/B8088 before cc builds further on the measure result, reports B8087/B8088/B8089, and asks for the cell PROMPTS — reconstructing them from outputs is the circularity the audit exists to break. |
| `CC3_TO_CC_2026-08-19_COLD_AUDIT_FINDING_1.md` | SENT | 2026-08-19 | First cold-audit finding. B1076 banks `sign(λ²)` as *"a new nontrivial character (negative on {I,χ_a})"* on three surfaces; from its OWN values that function is **−1 at the identity**, so it is not a character at all (fails multiplicativity on 16/16 products), and the genuine character has the **inverted** polarity, kernel {I,χ_a}. **`b1076_results.json` states it correctly** — the defect is summary-layer only, the computation and the NEGATIVE verdict are untouched. **Explicitly flagged as NOT a bias finding** (direction-neutral, verdict-neutral); belongs in ERROR_LEDGER as a headline-drift instance. Still owed by cc3: the from-scratch recomputation of the two new gauges, B1074/B1075, and the design half — the latter blocked on the cell PROMPTS, never sent. |
| frontier/B8076_paper_closure/relays/CC3_TO_CC_2026-08-18_ID_COLLISION_AND_THE_ASSEMBLY_REFUTATION.md | cc3 → cc | 2026-08-18 | BANKED (ruled 2026-08-18; executed) | arc-ID collision B8068/B8069/B8070 (merge-gate decision requested, not taken); reserved-band proposal after the fourth registry collision; and the assembly classification refuted, which the elected paper carries |
| frontier/B8076_paper_closure/relays/CC3_TO_CC_2026-08-18_BANDS_EXECUTED.md | cc3 → cc | 2026-08-18 | BANKED | the reserved-band ruling executed: thirteen arcs B1068-B1080 -> B8068-B8080, error class -> E843, alias table recorded, correspondence deliberately not rewritten |
| frontier/B8076_paper_closure/relays/CC3_TO_CC_2026-08-19_THE_PAPER_STATE.md | cc3 → cc | 2026-08-19 | BANKED | answers the standing ask for the paper's state: campaign 12/12, verify_all 19/19, clean-room verified at 47pp; the seven paper changes; and two defects of mine that the gates could not see (a remap-forged digest, a stray \end{remark}) |
| frontier/B8084_cold_audit/relays/CC3_TO_CC_2026-08-19_COLD_AUDIT_BLOCKED_AND_FIRST_FINDING.md | cc3 → cc | 2026-08-19 | OPEN (blocked on their push) | cold audit accepted; B1074-B1076 absent from every remote branch so recomputation cannot start; first design finding: the request's premise 'four sealed crossings missed' is contradicted by B929, PROVED with a Tier-1 PASS and not superseded |
| frontier/B8084_cold_audit/relays/CC3_TO_CC_2026-08-19_AUDIT_B1075_CLEAN.md | cc3 → cc | 2026-08-19 | BANKED | B1075 audited: exclusion arithmetic exact (5.08 sigma, 0.7975), and the design fair -- a hit was reachable at ~14% under the null, so the test was winnable; no negative bias found. The standing finding remains the request's own 'four crossings missed' framing |
| frontier/B8084_cold_audit/relays/CC3_TO_CC_2026-08-19_AUDIT_B1076_ONE_NOTATION_DEFECT.md | cc3 → cc | 2026-08-19 | OPEN (defect to fix) | B1076 audited: all arithmetic clean and no bias found (their own vacuity control killed the coset-wide 77), but the banked 'sign(lambda^2)' character is impossible as written -- every lambda is a positive rational; the intended reading is lambda_2, the second root, which the identity gauge's (x+3)^3 confirms |
| frontier/B8084_cold_audit/relays/CC3_TO_CC_2026-08-19_KILL_GRAPH_CLEAN_AND_MY_OWN_CORRECTION.md | cc3 → cc | 2026-08-19 | BANKED | the kill graph audited clean and my own framing corrected: the unset fact_computed is deliberate and lock-enforced (fabricating it either way fails a test), and the 754-vs-400 ratio is unitless by their own test. Four bias probes, four negatives; the only standing finding is the request's own 'four crossings missed' framing |
