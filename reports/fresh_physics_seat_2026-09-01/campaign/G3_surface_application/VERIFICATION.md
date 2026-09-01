# G3 — CONSISTENCY CHECK (independent checker, 2026-09-01)

**Cell:** G3_surface_application · **Claimed:** APPLIED-WITH-GATE-NOTES · **Checker verdict: CONFIRMED**
(one minor reporting discrepancy, non-substantive, noted in §5; no surface defect found; nothing for the seat to fix on the surfaces).

Method: read `CHANGESET.md`; read the full diff (working tree vs HEAD for tracked files;
`git show dd8c2e6` for the checkpoint-committed change-set A; all five untracked new files
in full); read the sources (T5 `PROPOSAL.md` + `FINDINGS.md`, T8a `PROPAGATION_LIST.md`,
T3 `THEOREM.md`, T8b `DRAFT.md`); re-ran gates and tests myself.

## 1. Traceability — every edit traces to its source; none goes beyond it — PASS

**Change-set A (T5):**
- `TERMINOLOGY.md` RL/LR row = PROPOSAL closing-#0 parenthetical (word-order "A = LR"
  vs matrix-product "A₁ = RL", E23 hazard) restated as a registry row. **Pointer
  correction verified independently:** `docs/LAW_MAP.md` contains no GC-3 row; the
  "ADJUDICATED (B1189/GC-3): ONE generator A₁ = RL" row lives at
  `docs/GRAND_COMPUTATION_LEDGER.md:38`. The registry row cites the real location and
  declares the PROPOSAL's mislabel. Correct.
- `docs/THEOREM_LEDGER.md` C5 annotation: every claim in it is in the sources —
  closing-#0 re-typing (PROPOSAL §Closing #0; B717/B713/B1083/B1163 all cited there),
  axiom-consumer class EMPTY over 1394 files (T5 FINDINGS lines 5, 36, 149 — figure
  verified verbatim), deck involution + Mostow / mirror-odd 2-torsion (T3 THEOREM.md,
  Theorem A). The [AXIOM] bracket retained: LESS than PROPOSAL bookkeeping item 1
  ([AXIOM] → [CLOSING #0]), deliberately, with the chain-locks gate rationale recorded —
  under-application with a declared reason, not over-reach.
- `main.tex` axioms scopenote: states the OPTION only, keeps the axiom labeling in the
  paper's counts — again LESS than PROPOSAL bookkeeping item 4 (the paragraph inversion);
  within source.
- `main.tex` observer-section sentence: exactly T3 Theorem A + its corollary (deck
  involution orientation-reversing by the descent argument, Mostow, mirror-odd invariants
  2-torsion, census = "shadow"). Verified against T3 THEOREM.md §1–2.

**Change-set B (T4/T8a):** all 12 flagged items A1–A12 checked line-by-line against
`PROPAGATION_LIST.md`; each edit implements the listed suggested correction and no more:
A1 THE_CLAIM row (regrade + arc B862·B1221 + dated note), A2/A3 README, A4/A5 main.tex
global-form paragraph (selects-clause replaced with the B1221 reading; \cite{slansky}
added), A6/A7 main.tex not-on-this-list paragraph (clause deleted and named as the fifth
moved-off item; termination narrowed to the conjunction with the three citations),
A8–A12 the four dated addenda (contents match the list's prescriptions, including B863's
conformal-case residue and T4's declared search bound, and B994's in-this-corpus scoping).
Three new bibitems match T4's references (Georgi NPB156 1979; Barbieri–Nanopoulos PLB91B
1980; Fonseca 1504.03695) and each is cited in prose. The 2 borderline items (B1, B2)
are un-edited as claimed, with reasons matching the list's own notes.

**Change-set C:** `TERMINALITY_SECTION_CANDIDATE.md` = 15-line candidate header +
verbatim copy of T8b `DRAFT.md` (diff: only the header lines differ; 289 = 274 + 15).
The SCOPE CORRECTION (part (ii) quantifier restricted to regular-maximal menus;
su(3)+g2 into Fence F1; named open computation) is present at the tail. The header marks
it owner-elected CANDIDATE pending G1; adopts nothing by itself.

No edit found anywhere in the diff that lacks a source in PROPOSAL.md,
PROPAGATION_LIST.md, or the T3 theorem.

## 2. House discipline — PASS

- `append-only` gate: PASS on my run. No append-only ledger row edited: TERMINOLOGY got
  an appended row; THEOREM_LEDGER C5 got a dated annotation appended inside the row
  (bracket untouched — chain-locks gate PASS); CAMPAIGN_STATUS and LAW_MAP untouched.
- No sealed FINDINGS edited in place: `git status` shows the four frontier files as NEW
  `ADDENDUM_2026-09-01.md` files only; no `frontier/*/FINDINGS.md` is modified. Each
  addendum states "the banked FINDINGS are untouched" and it is true.
- The test-locked phrase "a choice the SM cannot make about itself" is preserved verbatim
  in THE_CLAIM.md:23 (tests/test_b1014_proof_form.py:17 asserts it; test passes).

## 3. Gates and tests — re-run by this checker — PASS (with §5 note)

- `python3 scripts/gates/gates.py`: **27 PASS, 2 FAIL** on my run, plus the standing
  `review-due` notice (56 merges). The two FAILs are IDENTICAL in content to the
  CHANGESET's report:
  - `attribution`: `campaign/G2_t1_unblock/g1_out.txt`, `internalization/S2b`,
    `internalization/S3b`, `last-commit author: Claude` — none of G3's files; the
    last-commit component predates G3's checkpoint (8bc4dbf, a112540, 009d9a3 are all
    Claude-authored), so it fails with or without dd8c2e6.
  - `retraction-sweep`: `internalization/S2c` (3 hits), `internalization/S7` (1 hit) —
    none of G3's files.
  Both are sibling-cell artifacts; no gate fails on a G3 edit. Confirmed pre-existing.
- `pytest tests/test_paper_citations.py tests/test_paper_provenance.py -x -q`:
  **9 passed** (citation gate green with the three new bibitems).
- Additionally: `tests/test_the_road.py` 5 passed (9+5 = the CHANGESET's 14),
  `tests/test_b1014_proof_form.py` 5 passed.

## 4. No fence weakened, no caveat deleted — PASS

Every edit moves claims DOWN (derives→reproduces, novelty retracted, prior art added,
"Four"→"Five" moved-off items) or adds scope notes; none deletes a hedge. Specifically
checked: the m003 counterexample caveat survives beside the new amphichirality-theorem
sentence (main.tex:756 — "the sibling m003 is amphichiral, yet its cusp shape is
genuinely [chiral]" — 2-torsion ≠ mirror-even stays stated); the withdrawn-proof
disclosures (main.tex:805, 813, 1031) are untouched; the F5 FRAGILE pricing text in
THEOREM_LEDGER C5 is untouched above the annotation; THE_CLAIM's other rows unedited;
the candidate section carries its scope correction rather than the pre-correction draft.

## 5. Discrepancies (minor, reporting only — no surface fix needed)

1. **Gate PASS count:** CHANGESET says "31 PASS, 2 FAIL"; my run of the same script
   gives **27 PASS, 2 FAIL** (29 gates total + review-due). The FAILURE lists match
   exactly, and no gate fails on a G3 edit either way, so nothing substantive turns on
   it — but the PASS count in CHANGESET.md §"Gate and test status" is not what the
   script prints today. Likely a counting slip (or gates counted from a different
   revision); the seat may correct the number in CHANGESET.md (a cell-report file, not
   a surface).
2. Working tree also carries a modified
   `reports/.../recompute/R09_scale_cluster/r09_recompute.py` — not claimed by G3's
   CHANGESET, not one of its files (sibling R09 cell); noted so the owner's adjudicated
   commit does not attribute it to G3.

## Verdict

**CONFIRMED.** All three change-sets are applied as described, each edit traces to its
source and none exceeds it, house discipline held (append-only respected, addenda
beside, sealed FINDINGS untouched, test-locked phrase preserved, [AXIOM] bracket
retained), gates fail only on sibling cells' pre-existing artifacts, the cited tests
pass, and no fence was weakened nor caveat deleted. The single defect is a numeric
slip in the CHANGESET's own gate tally (§5.1), which does not touch any live surface.
