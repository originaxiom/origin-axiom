# R27 — B994 rule-variation test: recompute + provenance audit

**Verdict: PARTIAL** (endpoint claim: MATCH under B994's own reading, with a VACUITY note; path exhibit: DISCREPANCY; provenance: two E51-class gaps).

## Blind-first protocol
Read BEFORE coding: B994 FINDINGS.md lines 1-60 (claim, [3,2,1], six chains, named rules) and results.json;
B861 results.json + arc_verdict.json + FINDINGS §1-2 (the committed menus). NOT read before coding: B861's
fused_cascade.py, any B994 code. Read AFTER: rest of B994 FINDINGS + ADDENDUM; grep of B861 solver for menu keys;
repo-wide search for a B994 generating script.

## Menu reconstruction (from frontier/B861_fused_cascade/results.json — committed)
- step1_E6: SO(10)xU(1) 46 ✓ · SU(6)xSU(2) 38 ✓ · SU(3)^3 24 ✓ · Sp(8) 36 ✗
- step2_SO10: SU(5)xU(1) 25 ✓ · Pati-Salam 21 ✓
- step3_SU5: SU(4)xU(1) 16 ✗ · SM 12 ✓
Menus are keyed by PARENT (E6, SO(10), SU(5)). No menu for parents SU(6)xSU(2) or SU(3)^3 exists in any committed file.

## My recompute (recompute_r27.py)
Model A — position-indexed (step-k menu applied whatever the parent, which is evidently what B994 did):
registerable per step [3,2,1]; 6 chains; all 6 end at SM; max-dim = first-listed = SO(10)xU(1)->SU(5)xU(1)->SM;
min-dim = last-listed = SU(3)^3->Pati-Salam->SM. **Banked numbers reproduced exactly.**

Model B — parent-keyed, committed map only: walking E6 with the menus that actually exist gives 4 terminal paths,
endpoints {SM, Pati-Salam, SU(6)xSU(2), SU(3)^3}: only the SO(10)->SU(5) branch reaches a level-3 menu. The other
five "chains" require menus B861 never committed.

Planted-positive control: set SU(4)xU(1) registerable → 12 chains, endpoints {SM, SU(4)xU(1)}: the endpoint
check can fail, so it is not structurally vacuous. BUT given B861's data as banked, "endpoint rule-independent"
is exactly the statement len(registerable at step 3)==1, i.e. it is B861's step-3 uniqueness restated; no new
computation could have moved it. Note as VACUITY-flavored (true; the rule enumeration adds nothing beyond B861).

## Diff
1. Endpoint rule-independence: MATCH (6/6 → SM) under the position-indexed reading; but the reading is the
   discrepancy: B994 applied the SO(10) menu to SU(6)xSU(2) and SU(3)^3 and the SU(5) menu to Pati-Salam.
   Applying the SU(5) menu after Pati-Salam is not a subgroup step (SU(4)xSU(2)xSU(2) ⊅ SU(5)); Pati-Salam→SM
   is real but has its own menu (uncommitted).
2. Path-dependence exhibit: DISCREPANCY. The exhibited alternative chain SU(3)^3 -> Pati-Salam -> SM is not a
   chain of subgroups: su(4) (rank 3) has no nonzero hom into su(3)^3 (each factor rank 2), so Pati-Salam ⊄
   SU(3)^3; likewise SU(5)xU(1) ⊄ SU(3)^3 (embedding_check.txt, exact). Two of the six banked chains are
   group-theoretically void. Path-dependence per se (max-dim vs min-dim give different step-1 choices) is
   genuine, but the banked exhibit is the wrong witness.
3. B994's own quantifier ("menu arithmetic, not the manifold") — confirmed and in fact stronger than stated:
   it is arithmetic over a positional list, not even over the subgroup lattice.

## Provenance audit (E51)
- Every menu ENTRY B994 cites (the 8 options with dims and registerability) exists in
  frontier/B861_fused_cascade/results.json. No entry is prose-only. PASS.
- Menus for parents SU(6)xSU(2), SU(3)^3, Pati-Salam — implicitly relied on by 5 of 6 chains — exist in NO
  committed file. **E51 instance #1.**
- No generating script for B994's results.json exists anywhere in the repo (grep for its keys hits only the
  results file; git history shows no deleted .py). FINDINGS quotes "verbatim from the code", but the code is
  B861's. **E51 instance #2 (results without generator).**

Gate 5: no measured values used. Files: recompute_r27.py, embedding_check.txt, this file.
