# The retractions index (GOVERNANCE §12–§14 companion; instituted 2026-07-16)

*One row per banked-then-corrected statement. This index is DISTINCT from
`docs/ARCHIVE.md` (ideas killed at testing) — these were once asserted in
the record and later corrected, withdrawn, or superseded; a reader of an
old FINDINGS could still act on them. Curated, not exhaustive at
inception; maintenance rule (same-PR, like LAW_MAP): every future
retraction/withdrawal adds its row in the PR that banks the correction.
Rows cite the banked locus and the correcting locus.*

| what was asserted | where banked | the correction | where corrected |
|---|---|---|---|
| **"B575 is cited nowhere, yet `CLAIMS.md` P51 names it as its own evidence"** — offered as a distinct defect shape | `docs/consolidation/DEBT_LEDGER.md` v1/v2; the session report | **WITHDRAWN. B575 IS cited** in `CLAIMS.md` — both as `B575's exact computation` and as the path `frontier/B575_bridge_obstruction`. **The stated cause was itself wrong on a first pass and is corrected here:** it was *not* the path-form regex. It was a **scope widening** — a band note's accurate claim (*absent from `LAW_MAP`/`THE_FRAMEWORK`/`THEOREM_LEDGER`*) was carried into the ledger as *"cited on no surface"* without re-checking `CLAIMS.md`. **A separate, real defect found in the same check:** the bare-id regex misses **49** arcs cited only by path — nearly all promoted P/C/E claims (B239→P48, B264→P50, B354→P55) — so the substantive debt falls **294 → 245** | `DEBT_LEDGER` v3 (the ⚠ banner) · lock `tests/test_consolidation_coverage.py::test_path_form_citations_are_counted__the_v3_correction` |
| **This pass's own coverage headline: "580 of 934 arcs are cited on NO surface a reader navigates by" (62 %)** — asserted as a navigability finding | `docs/consolidation/DEBT_LEDGER.md` v1 (commit `1d720e5`); the published artifact page; the session report to the owner | **WITHDRAWN — FALSE.** Re-run against all thirteen navigational surfaces, **every** one of the 579 is carried somewhere: all by the *generated* `docs/views/VERDICT_LEDGER.md` (a complete index of every verdicted arc) and by the atlas; 356 in `CLOSED_DOORS`, 208 in `OPEN_LEADS`, 179 in `REVIEWS`, 132 in `CAMPAIGN_STATUS`. **Absent-from-everything is 0, not 580.** The repository's architecture is deliberately TWO-TIER — `GOVERNANCE` §12 *"Freeze the substrate; generate the views… Everything a reader or reviewer navigates by is a view"* — and the measurement covered only the curated tier while the prose described both. **What survives, restated correctly: 579 arcs, 353 PROVED, are carried by no CURATED consolidation** — the campaign's actual concern. Not *unreachable*; *not distilled*. Also corrected: 934 → **933** (B58 has three arc directories and was double-counted) | `docs/consolidation/DEBT_LEDGER.md` v2 (the ⚠ CORRECTED banner) · lock `tests/test_consolidation_coverage.py`, which pins BOTH tiers so the metric cannot silently revert · `docs/ORIENTATION.md` row corrected |
| B939's 27-shadow map prose: *"σ₋₁ → D (12 flips) · σ_χ₋ → D₂ (the ELEVEN)"* | `frontier/B939_klein_assembly/FINDINGS.md` + its `arc_verdict` | **TRANSPOSED** — B939's own code builds by CHARACTER (`g_sm1 = inner_gmap(ALL_MINUS)`), and B936's per-character `D_flips` give ALL_MINUS **11** and χ₋ **12**, with B936's `Q_B` coordinates agreeing. Corrected: **χ₋ → D (12, class (1,1)); ALL_MINUS → D₂ (11, class (0,0))**. B939's mathematics is untouched — every check stands and its verdict does not depend on which name the shared element carries; one prose line was wrong, in a place a later sealed cell had to consume it | B1024/L153 (`frontier/B1024_l153_bits/`), which had to clear it before it could run; lock `tests/test_b1024_l153.py::test_b939_prose_is_transposed_against_the_computed_flip_counts` |
| **"B1000's five-closings census (confirmed)"** — asserted by B1017 on adopting its recount, and repeated on the claim page as *"B1000's census of five closings stands"* | `frontier/B1017_recount/FINDINGS.md` + its `arc_verdict`; `docs/THE_CLAIM.md` §1 | **NARROWED — the CARDINALITY is confirmed; the MEMBERSHIP is not, and was never checked.** B1000's five closings include the **4d lift / N=2→N=1 datum** (space sector) and grade **the 6d type an ARTIFACT** — *"a choice of the class-S bridge, not a deficit of the object"*. B1017's own resource table spends the Lie type on **the 6d type J** and assigns **no resource to space at all**; `THE_CLAIM` §1 inherited it and names no space closing anywhere on the page. **Same number, different set.** Nothing in the derivation theorem moves — the count is five either way — but *"confirmed"* claimed an agreement that does not hold at member level. **Error class E1.** Adjudication is *not* attempted by a drafting seat: B1000 itself flags the closing-vs-artifact split as a **judgement** whose different reading would move the count. Registered as **L157** | B1030 (`frontier/B1030_input_typing_audit/`); lock `tests/test_b1030_input_typing.py::test_the_two_fives_have_the_same_size_and_different_membership`; and the same arc repaired the separate drafting defect that `THE_CLAIM`'s quoted one-sentence claim still said *"four typed external data"* against §1's five |
| B519's negative: "no external crossing" (read as sufficient) | B519 FINDINGS | RETRACTED — mixed-chain gap-opening is falsifiable; the discriminating fact was never computed in-sandbox | the B525 audit (3/10 banked negatives cracked); the compute-the-discriminating-fact rule |
| "exponent = rank from Cayley–Hamilton" (SL(4)) | B90/V74 | REFUTED — both SL(4) components satisfy L1b with exponents 4 vs 3; L1a was a tautology | the V75 audit; B90 reclassified as reformulation |
| B95's "forced" principal spectrum read unconditionally; "any 5-dim rep reducible/non-ss 0/120" | B95/V79 | CORRECTED — "forced" is conditional on the mult-(n−2) ansatz; non-ss irreducibles exist (2 certificates); the n=5 absence holds for the finite-order/principal family | B153/V142–V145 (the det-t=0 drift found) |
| PC13's "SL(4) component" claim | PC13 | REPLACED — degree=rank is rank-stratified: component@3, slice@4, absent@5 | B153 |
| The "E₆→SM dictionary" (a cross-seat handoff) | chat-1 handoff, 2026-06 | VERIFIED-AND-REFUTED — G₂⊕A₂ mislabeled as E₆; the numerology killed | B347 (the correct replacement: E₆ tangent = 6; θ = E₆→F₄ split) |
| The trefoil(5,1) trace-field inheritance reading (Tr τ ∈ ℚ(√5)) | the child-transfer thread — frontier/B437_child_abelian_book (+ B438/B440 foreign controls) | RETRACTED as inheritance — numerator-forced, not inherited | PROGRESS_LOG 2026-07 (the (5,1)-filling control) |
| The "entropy log β" reading of the growth rate | the criticality thread — frontier/B523_verdict_reexamination + frontier/B530_natural_history | RETRACTED — primitive subshifts have zero entropy; the quantity is the inflation growth rate | PROGRESS_LOG 2026-07-15 |
| The quadratic-arrow verdict (all forms) | the L85 campaign | RETRACTED IN FULL — the longitude convention corrected AND the re-derived form ALSO retracted by the same arc's erratum (P1_ERRATUM D2: "no map was constructed to have an order"; survives only as a heuristic expectation). [Row corrected 2026-07-21: the earlier "(quadratic stands in corrected form)" contradicted its own cited source — cc2 register crack #3, cc-verified] | B598-P2 + P1_ERRATUM D1–D10 |
| The Kubota–Leopoldt attribution claim | the dictionary thread — frontier/B507_beta_function + the Review 25 sweep (docs/progress/REVIEWS.md, 2026-07-15) | RETRACTED with the discriminating fact computed | REVIEWS (the 2026-07-15 sweep) |
| B609's unit-modulus exploratory note | B609 | SUPERSEDED — the exploratory reading replaced by the exact law | B611; Review 19 (i) |
| A parallel seat's h¹(D_conjθ) = 3 | a cross-seat packet, 2026-07-16 | WITHDRAWN by the originating seat — an assumed λ-sign; the dimension is genuinely open (the object is a fiber pairing, not a rep twist) | B639; L92 re-scoped; the cc2 adjudication note |
| The B615 amplitude suggestion read at p = 0.078 | B615 | DISSOLVED — scheme/scale defect; corrected inputs give 0.145–0.62 across all variants (verdict A) | B615-R (seat 4), integrated B633 |
| "The naive flip acts on the double" (the L93 candidate as first posed) | L93's design | REFUTED — the flip does not act (either J-convention); both outer involution classes broken (partial intertwiner on Sym⁰ only) | B643; LAW_MAP wall 8 |
| *— CATCH-UP BLOCK (2026-08-06, B920; cc3 loss audit A5: the same-PR rule above was broken — no rows since 2026-07-22 despite the events below) —* | | | |
| H-B788-NORMSPLIT ("m004-only trace norms all ≡0 mod 4") — hint retracted 2026-07-28 as "REFUTED by B794's law" | docs/HINT_LEDGER.md row (7); frontier/B794_congruence_level4/FINDINGS.md | TWO-STAGE: the 07-28 retraction itself was then AMENDED 2026-08-06 — the refutation holds only at the TRACE level; at the NORM level (the hint's own level) the hint SURVIVES: norm-level m004-exclusives = 12 norms, all ≡0 mod 4; 103/127/175/367 are shared; B794's theorem is the mechanism | B920 (the cc3 level reconciliation, rerun in-sandbox); reconciling artifact frontier/B794_congruence_level4/trace_norm_split.* ; E28/E33 instance rows |
| B471's Fricke/commutator harvest row read as the programme's own result (the Cohn 1955 attribution omitted at harvest) | docs/LAW_MAP.md (the R32-9 harvest row, first form) | ATTRIBUTION CORRECTED 2026-07-29 — classical territory (Cohn 1955, Markov, Fricke), cited not claimed; the programme's own content is the metallic-body specialisation only | the LAW_MAP B471 row (⚠ block); tests/test_b471_harvest.py |
| "{4₁, 5₂} form a commensurability class" / "the forced child inherits its parent's commensurability class" | B438, B440, B443; docs/CAMPAIGN_STATUS.md | WITHDRAWN (polarity inverted) — no knot complement is commensurable with 4₁ (Reid: the unique arithmetic knot); a property shared with 5₂ is shared across NON-commensurable manifolds, i.e. genericity evidence, the opposite of "commensurability-forced"; what survives is narrower: 4₁(5,1) ≅ −5₂(5,1) at slope 5 only | B855 (the wrong-null audit, 2026-08-02) §2; its carried-forward correction list |
| B790's Maass-adjudication first pass: the "ordinary noise" null verdict + three supporting readings | frontier/B790_maass_adjudication/FINDINGS.md (first pass) | FOUR CORRECTIONS CONCEDED (Chat-1's challenges, all four) — the reported null was never the pre-registered one AND the "Weyl-matched" null was miscoded (e^ℓ for e^{2ℓ}); L3 re-verdicted MISS-earned; tests 1–3 vacuous; the B713–B716 scope reading corrected | the B790 ADDENDUM (2026-07-28, in-FINDINGS); ERROR_LEDGER E29 |
| B225's "2 = octahedral parent REFUTED" verdict carried as PROVED | frontier/B225* (own file); the arc-verdict register | RELABELED PROVED → RETRACTED — the criterion was vacuous (the bad-prime extraction reports 2 for EVERY monic-in-z input; specificity zero); the octahedral-parent question returns to OPEN; the 5-half survives (5 in conductor 40 = the golden branch point x²=5) | B745 (confirmation); B831 (the relabel, R35-4); CHANGELOG 2026-08 |
| The section-LIV septic wall-root instrument (cmt.py), retracted by the solo seat, SHIPPED ANYWAY in solo handoff 6 — a stale pre-retraction artifact (κ mod 40031 has NO wall roots; centralizers there read the generic floor 12) | solo handoff 6 §XLIX–LVIII (the shipped cmt.py) | CAUGHT AT VERIFICATION 2026-08-06 — root-set comparison against κ exposed the phantom roots; the corrected instrument (cmt_correct.py) confirms the ledger at MORE (root,prime) pairs; adopted as the wall-instrument sanity gate; the retraction-propagation failure (a retracted instrument surviving into a handoff) is the sharpest retraction-hygiene datum owned | B909 (frontier/B909_frame_arc/FINDINGS.md, cmt_correct.py); routed to B920 (this catch-up) |

## 2026-08-08 — B964: two VEV claims withdrawn
1. **"The object does not supply a VEV"** (B952, B959, B960, echoed B962) — **FALSE.** An
   adjoint VEV's unbroken group *is* the centralizer of that element, so the measurement
   cascade **is** an adjoint Higgs mechanism. The object supplies the rank-preserving half;
   it lacks the rank-reducing 27 half.
2. **"The 27-VEV route provably stops one step short"** (B962) — **scope error.** True for
   **27-only** breaking; false in general, since the 78 contains a 24.

**Untouched:** B952/B959/B960's rank obstruction (it was always about *centralizer /
adjoint* constructions), the 27 branching, the F₄=generic-VEV unification, and L138.
**Cause:** using "VEV" loosely to mean "27 VEV". **Rule adopted: name the representation
every time.** Caught by the owner's challenge, not by a gate.

## 2026-08-11 — B1032: B1031's "only one route" clause, withdrawn one arc later
**Asserted** (`docs/THE_LADDER.md` rung X33, written by B1031): *"the relational route (B302's
commensurator ℤ/3 → multiplicity) is **the only one B307 leaves open**, and no arc runs it end to
end."*

**WITHDRAWN — the first clause is false.** B307 closes the route through the **trace field of a
single hyperbolic knot**; **nothing in the across-breakings cluster is a trace-field statement**, so
its hypothesis does not apply there. **B885 → B889 → B890 → B891 is a second live route**, and
unlike the relational one it has **two SEALED cells already run on it** — B890 finding the foreign
vacuum lines DISTINCT in all three frames **against its own disclosed prior of EQUAL**, B891
extending it to matter (*"a single observer registers three pairwise-distinguishable matter
sectors"* on one 27).

**What survives:** the second clause, *for both routes* — neither runs to mechanism-hood. It is now
stated **per route**, since route (b) stops at a **fence both sealed cells declare**
(*registerable distinctness is not mechanism-hood; the three 16s overlap and are not direct
summands*) rather than at nothing.

**Cause, and it is the corpus's first-named trap:** *"'we don't have X' is a hypothesis, never a
conclusion"* (`WORKING_RULES` §0) — committed **while writing the rung whose purpose is to prevent
it**, one paragraph after diagnosing the same failure in the file as a whole.

**Corrected in:** rung X33 (rewritten to name both routes and cite the cluster) ·
`frontier/B1032_across_breakings_route/` · lock
`tests/test_b1032_across_breakings.py::test_the_only_one_clause_is_withdrawn_and_two_routes_are_named`.
