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
| **This ledger presented as *the* consolidation-debt register**, with no mention that a gated one already existed | `docs/consolidation/DEBT_LEDGER.md` v1–v3; `docs/ORIENTATION.md`; the published artifact | **NARROWED — the count stands, the framing does not.** `docs/REPRESENTATION_TRIAGE.md` (L143/B976), swept by `scripts/checks/representation_sweep.py` and enforced by the **failing** `representation-sweep` gate, is the repository's own register of unrepresented arcs — *"an untriaged unrepresented arc is the defect"*. The ledger cited it, the sweeper and the gate **zero times**. The two rules differ (PROVED vs PROVED∪NEGATIVE; no substantiality filter vs `claim ≥ 500`; **5 curated** surfaces vs **9** synthesis surfaces) and answer different questions — **234** rows against **10 live** / 17 triaged, overlapping in **6**. Neither count is withdrawn; publishing one without the other is the defect, and it is the same shape B1030 filed against `THE_CLAIM` vs B1000 — this time against my own deliverable. **Cause: the campaign's own first trap** — *"'we don't have X' is a hypothesis, never a conclusion"* | B1033 (`frontier/B1033_register_reconciliation/`); `DEBT_LEDGER` **§0**; locks in `tests/test_consolidation_coverage.py` |
| **"`docs/ERROR_LEDGER.md` names E1 the programme's most recurrent error class"** | `frontier/B1024_l153_bits/FINDINGS.md`; `frontier/B1026_the_one_involution/FINDINGS.md`; `tests/test_b1026_one_involution.py` | **WRONG SOURCE, right substance.** `ERROR_LEDGER.md` **never uses the phrase** — it registers E1 with 3 known instances, fewer than E4's or E12's. The claim is real and binding, but it lives in **`GOVERNANCE.md` §13** (*"the program's single most recurrent error class is undeclared choice drift"*) and **`WORKING_RULES.md`**. A misattribution, not a false claim; recorded rather than silently repointed, because a citation to a document that does not contain the statement is exactly what the corpus's **E11 (overextended record)** names | B1033; all three loci repointed in place with the correction stated inline |
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

## 2026-08-11 — B1039: B141's *"finite image ⟹ reducible tower"*, narrowed by counterexample

**Asserted** (`frontier/B141_s031_split/FINDINGS.md`, Item 3, tiered SOLID): *"**Finite image ⟹
reducible tower; dense image ⟹ irreducible tower.** This is the conceptual root of the φ-vs-φ²
distinction."* Carried forward as the cluster's one-sentence law.

**NARROWED — the first half is FALSE as a general implication**, and the counterexample is small
enough that it was found while re-deriving the arc for restoration. The **binary tetrahedral group
`SL(2,3)`** is finite (order 24) and its **`Sym²` is IRREDUCIBLE** — algebra dimension **9 = 3²**,
computed exactly over `ℚ(i)`.

**What is true, and is all B141 needs:** the bound is the **maximal irrep dimension `d`** —
`dim Sym^{n−1} = n > d` forces reducibility for every `n > d`. That is **2** for `Q₈` and **3** for
`SL(2,3)`, and *the two groups sit on opposite sides of their own bound at exactly `n = 3`*, so the
bound is **sharp** and **finiteness alone is not the mechanism**. B141's Item 1 conclusion — the
principal φ-fixed tower is reducible at every `SL(n)`, `n ≥ 3` — **is untouched**; only the reason
given for it was too strong.

**A second, smaller correction in the same cluster.** `frontier/B142_klein4_and_magic_cartography`
opens its one-line proof with *"principal eigenvalues `{1,−1,−1}` ⟹ `A² = I`"*, which requires **`A`
semisimple**: `diag(1) ⊕ [[−1,1],[0,−1]]` has the same spectrum and `det 1` and is not an
involution. The hypothesis **does** hold at a φ-fixed point, so the proof is sound — it was never
stated. And **B142's own probe never verified its lemma**: `klein4_lemma_symbolic()` exhibits one
commuting pair. The universally quantified statement — *two involutions whose product is an
involution commute* — is verified for the first time in B1039, by coset enumeration on
`⟨a,b | a², b², (ab)²⟩`.

**Cause:** a slogan that generalised correctly-computed evidence one step past what the evidence
supported — the corpus's **E1** shape (a choice, here of mechanism, made without being declared) —
and **neither defect was reachable by reading claim lines**; both required recomputing the arc,
which is what campaign step 5 exists to force.

**Corrected in:** `frontier/B1039_phi_fixed_and_metallic_exponent/` · the restored `LAW_MAP` row,
which carries the narrowed form and names the counterexample · locks
`tests/test_b1039_phi_fixed_and_metallic_exponent.py::test_finite_image_does_NOT_imply_a_reducible_tower`
and `::test_spectrum_alone_does_not_give_an_involution`.
