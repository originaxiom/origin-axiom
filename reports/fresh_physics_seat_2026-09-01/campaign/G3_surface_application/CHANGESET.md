# G3 — SURFACE APPLICATION CHANGESET (2026-09-01)

**Cell:** G3_surface_application · **Seat:** fresh physics seat, owner-elected live-surface
application ("T5, T4 green. act"). Every edit carries the date 2026-09-01 and the marker
*(fresh-seat application of the owner's T4/T5 election; sources:
reports/fresh_physics_seat_2026-09-01/campaign/)*. All edits land on this branch for the
owner's merge review; nothing here is a merge.

## Files touched

### Change-set A — T5 adoption (the A6 relabeling)

| file | edit |
|---|---|
| `TERMINOLOGY.md` | NEW dated row appended to the overloaded-symbol registry: **RL vs LR** — the two-convention collision on [[2,1],[1,1]] (UNIQUENESS_THEOREM's word-order "A = LR" vs the GC-3 clock adjudication's matrix-product "A₁ = RL"). **Pointer correction, declared:** T5's PROPOSAL cites "LAW_MAP GC-3"; the GC-3 row actually lives in `docs/GRAND_COMPUTATION_LEDGER.md` (B1189) — the registry row cites the real location and notes the mislabel. |
| `docs/THEOREM_LEDGER.md` | Dated in-place annotation appended to the C5/orientation row: ADOPTED RE-TYPING per the owner's election — orientation = the observer's closing #0 (B717 act-type; object cannot self-orient, B1163); evidence cited: T5 audit's axiom-consumer class EMPTY over 1394 files, and the T3 theorem (deck involution + Mostow ⇒ every orientation double cover amphichiral; mirror-odd invariants 2-torsion), making deck-involution corollaries theorems-of-the-construction. The **[AXIOM] label is retained on the surface** (annotation records the re-typing) so the `chain-locks` gate semantics (AXIOM rows need a price, not a lock) are not silently changed by a relabel — the ledger-wide relabel is the owner's merge-time call. |
| `papers/P3_THE_PAPER/main.tex` (axioms section, after the "bridge from the word to the manifold" paragraph) | NEW scopenote "A relabeling this axiom admits": states the relabeling OPTION (orientation as the observer's first closing; audit found no orientation-consumer before the object exists; axiom count drops by one under it; the paper keeps the axiom labeling in its counts). No restructuring. |
| `papers/P3_THE_PAPER/main.tex` (observer section, the obstruction paragraph) | ONE added sentence + comment-note upgrading the 83-cover amphichirality census to the a-priori theorem: deck involution is orientation-reversing (descent argument) + Mostow (\cite{mostow}) ⇒ amphichirality a priori, mirror-odd invariants 2-torsion; "the 83-member sweep is the theorem's census shadow rather than its evidence." Consistent with the later withdrawn-support scopenote (2-torsion ≠ mirror-even; m003 stays a counterexample to the stronger reading). |

### Change-set B — T4 propagation (the 12 corrections; PROPAGATION_LIST items A1–A12)

| file | edit | list items |
|---|---|---|
| `docs/THE_CLAIM.md` | ℤ₆ global-form table row: grade **DERIVED → REPRODUCED *(was DERIVED)***, arc column B862 · B1221, with the dated in-row note (path-independent kernel, KNOWN since 1980, Tong 1705.01853; contribution is upstream). The test-locked phrase "a choice the SM cannot make about itself" is preserved verbatim (tests/test_b1014_proof_form.py asserts it). | A1 |
| `README.md` | "**derives** the global ℤ₆ form" → "**reproduces** the known global ℤ₆ form" with the B1221/known-since-1980 anchor; termination sentence anchored to the survival hypothesis (Georgi 1979, Barbieri–Nanopoulos 1980, Fonseca 1504.03695) with the claimable residue stated as terminality **plus** rule-independence (B863+B994). Dated marker appended. | A2, A3 |
| `papers/P3_THE_PAPER/main.tex` ("global form" paragraph) | Header "derived" → "reproduced"; "**This is the clearest positive result in the paper**" → "**the clearest \emph{reproduced} structural statement**, and we no longer present it as a novelty" (path-independent kernel, known since 1980, \cite{slansky} added); "What is not standard is that anything here \emph{selects} the embedding" RETRACTED and replaced with the B1221 reading (nothing needs to select; the embedding was never doing the work). | A4, A5 |
| `papers/P3_THE_PAPER/main.tex` ("not on this list" paragraph, Recognition section) | The selects-the-SU(5)-embedding clause DELETED from the not-standard list and moved to the moved-off-during-revision count ("Four items" → "Five items", the fifth named with its reason); the termination clause NARROWED to the conjunction (terminality + rule-independence), with the survival-hypothesis prior art cited \cite{georgi1979,barbierinanopoulos,fonseca}. | A6, A7 |
| `papers/P3_THE_PAPER/main.tex` (bibliography) | Three NEW bibitems: georgi1979, barbierinanopoulos, fonseca (each cited in prose — the citation gate's furniture check passes). | supports A5–A7 |
| `frontier/B862_global_form/ADDENDUM_2026-09-01.md` | NEW addendum-beside: scopes "for free" (literally true — exactly why not new) and "outperforms the SM's own data" (contrast is the literature's) per B1221; notes the 2026-08-12 addendum's selection half is superseded. Original FINDINGS untouched. | A8, A9 |
| `frontier/B1080_global_form/ADDENDUM_2026-09-01.md` | NEW addendum-beside: strikes "new" from "the paper's cleanest new line" per B1221; residual value re-stated as the uniformity/MB12 sweep. | A10 |
| `frontier/B863_termination/ADDENDUM_2026-09-01.md` | NEW addendum-beside: the missing prior-art anchor supplied (Georgi 1979 / Barbieri–Nanopoulos 1980 / Fonseca 2015, KNOWN); claimable residue = computed terminality (incl. the conformal case, absent from prior art found) + B994 rule-independence, jointly; T4's search bound declared. | A11 |
| `frontier/B994_rule_variation/ADDENDUM_2026-09-01.md` | NEW addendum-beside: "never asked before" scoped to *in this corpus* (B869 varies the starting group, not the rule); world-novelty collides with the survival-hypothesis literature. | A12 |

**Skipped, per the cell brief (the 2 borderline items, left un-edited with reasons):**
- **B1** `docs/LAW_MAP.md:330` — internal scope is already stated in the same breath ("B869 varies the *starting group*") and the row itself carries "REPRODUCED, not DERIVED — textbook GUT"; an edit would restate what the row already says, on an append-only-adjacent law surface, for a reader-inference risk the row's own grade clause already fences.
- **B2** `docs/CAMPAIGN_STATUS.md:240` — a forcedness claim, not a novelty claim; the same file already carries the full B1221 KNOWN entry (lines 158–172), so the E53 gap is internal to one file whose corrective entry exists; adding a cross-reference is cosmetic and CAMPAIGN_STATUS is the campaign's own dated log (editing an old dated entry would violate the append-only ledger discipline).

### Change-set C — terminality draft placement

| file | edit |
|---|---|
| `papers/P3_THE_PAPER/TERMINALITY_SECTION_CANDIDATE.md` | NEW file: verbatim copy of `campaign/T8_terminality_draft/DRAFT.md` **including its scope correction** (part (ii) quantifier restricted to the regular-maximal menus; su(3)+g2 in Fence F1), under a header marking it an owner-elected CANDIDATE section **pending the G1 cell's su(3)+g2 outcome**; adopted only by the owner. |

## Gate and test status

- `python3 scripts/gates/gates.py`: **31 PASS, 2 FAIL — both FAILs pre-existing and not from this cell's edits** (verified by stash/re-run: identical failure lists with this cell's working-tree edits removed):
  - `attribution`: vendor tokens in OTHER cells' files (`campaign/G2_t1_unblock/g1_out.txt`, `internalization/S2b`, `S3b`) + the branch's own last-commit author (the campaign branch's commits; owner-side identity, not a file edit) — none of G3's files.
  - `retraction-sweep`: retracted phrases quoted in OTHER cells' internalization digests (`S2c`, `S7`) — none of G3's files.
  - Also reported: `review-due` (56 merges since last review) — a standing campaign-level notice, not an edit failure.
- `pytest tests/test_paper_citations.py tests/test_paper_provenance.py tests/test_the_road.py -x -q`: **14 passed** (citation gate green with the three new bibitems — each cited; provenance and road locks unaffected).
- Nothing was reverted; no gate failed on a G3 edit.

## Notes for the owner's merge review

1. The THEOREM_LEDGER C5 row keeps its `[AXIOM]` bracket with the adopted re-typing recorded in the annotation — flipping the bracket to `[CLOSING #0]` changes `chain-locks` gate semantics for that row and is left as an explicit merge-time decision.
2. The T5 proposal's typed residual stands and is NOT discharged by this cell: the GL(2,ℤ)-level uniqueness computation (UNIQUENESS_THEOREM A3 → closing #0 restatement) remains the one new computation the adoption wants.
3. `frontier/B1003`'s FRAGILE table (T5 bookkeeping consequence 2) was NOT edited — the cell brief's change-set A names TERMINOLOGY, THEOREM_LEDGER, and main.tex only; the B1003 F5-row retirement is registered here as a remaining adoption step.
4. A parallel orchestrator checkpoint (commit dd8c2e6) captured change-set A mid-flight; the remainder of the change-set is in the working tree of this branch.

**VERDICT: APPLIED-WITH-GATE-NOTES** (all elected edits applied; gates green on this cell's files; two pre-existing failures from sibling cells' artifacts, documented above).
