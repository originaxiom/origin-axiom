# FINDINGS — B738: the Negative Anatomy Compiler — the kill graph, the face-coverage matrix, the shortlist

cc banking seat, 2026-07-21. Pathfinder Stages 1–2 (docs/handoffs/PHYSICS_PATHFINDER_PROMPT), run as
an INSTRUMENT-BUILD (like the atlas): compiling, not adjudicating — no negative revived or re-killed
here. Workflow wf_be6540b7: 14 compile agents (12 probe-batches + walls + tombstones) → synthesis →
3 sample-auditors (8 samples each, re-read the actual FINDINGS): **0/3 refuted**. Gate 5; nothing to
CLAIMS.

## THE INSTRUMENT (committed)
- `kill_graph.json` — **217 classified negatives** (172 dead/dormant atlas probes + 11 walls + ~30
  tombstones), unique ids, per-record: claim_killed · kill_form · faces_consulted · fact_computed ·
  hatch · priority · revival_score.
- `KILL_GRAPH_SUMMARY.md` — the distributions + the FACE-COVERAGE MATRIX.
- `SHORTLIST.md` — the candidate-lattice seed (~16 cells), headed by the GLOBAL LOOK-ELSEWHERE
  width rule; Candidate Zero (B737) anchored as in-flight cell #1.

## THE HEADLINE EMPIRICAL FINDINGS
1. **The pathfinder's central prediction CONFIRMED at the corpus level:** the emittance columns are
   ~empty — emittance-lengths 2/217, emittance-eigenvalues 3/217 (and those incidental), **the
   Laplace/scattering spectrum proper consulted by ZERO kills** — a fully virgin column. The
   infinite-Hecke column: 4/217 (all recent). Being dominates (112/217). **All 21
   native-continuous-channel hatches point at the two empty emittance columns** — they meet in
   Candidate Zero's cell.
2. **Kill-form census:** kind-mismatch 47 · other 46 · genericity 33 · no-landing-site 30 ·
   value-numerology 24 · method-limit 13 · zero-intertwiner 9 · absence-at-depth 9 ·
   cited-as-sufficient 4 · finite-truncation 2.
3. **Priority census:** P1 9 · P2 54 · P3 20 · P4 47 · LOW 87. Honest: **65% of records score ≤2**
   — the revival mass is LOW, as it should be; the corpus's kills are mostly sound.
4. **The fact_computed=false list (the B525 signature, 12 ids):** B140, B332, B412, B433, B435,
   B579, B668, **B685**, **B720**, B731, W7-rebase, S019. NOTE the two heavyweights: B685 (the
   terminal generation no-go) and B720 flagged as not carrying their discriminating computation
   IN-TEXT — this does NOT mean they are wrong (their facts may live in satellite arcs, e.g.
   B683/W2 for B685; B435's flag was audit-confirmed exactly this way — the fact lives in B437).
   It means the hunt must LOCATE-or-recompute each before treating the kill as B525-clean.
5. **Shortlist top (behind Candidate Zero):** B731 (score 10 — the already-revived E22 exemplar,
   kept as the calibration case), **B500 (score 6 — its own text says REOPEN: the depth-5 child
   kill is PROVISIONAL, 115/150 analyzed, 35 unchecked)**, then B712, B433, B685, B401, B399,
   B183, B111, B252, B477, W11-B706, W10-B660/B666, B619, B107.

## Audit
3 samplers × 8 samples, re-reading the actual FINDINGS (and following cross-references): 0/8, 0/8,
0/8 materially misclassified — the compiler was notably careful with honest fact_computed=false
calls (B435→B437, B361→B367 correctly cross-referenced) and preserved self-corrections (B500's own
provisional flag) instead of overclaiming closure.

## Standing
The instrument is built and audited; the hunt's queue is the SHORTLIST, priced by the global
look-elsewhere ledger (width ~16 cells; every hit must state its width correction). Candidate Zero
(B737) in flight. Next after B737: the B500 reopen (35 unchecked children — cheap, its own text
requests it) and the fact_computed=false locate-or-recompute sweep (12 ids). Compiling a negative
into the graph does NOT weaken its kill — each stays dead unless its named recomputation fires.
Credit: the owner (the hunt directive); cc3's repairs landed mid-run and are reflected. Nothing to
CLAIMS.

---
## KILL-GRAPH DIFF vs cc3's B742 (requested by cc3; run 2026-07-21)
Corpora: mine 217 (atlas dead/dormant + walls + tombstones) vs cc3's 213 (LAW_MAP/RETRACTIONS/
ledgers/B600–735); **overlap 155** (62 mine-only, 58 theirs-only; combined unique corpus ≈ 275).
- **kill_form raw disagreement: 107/155 (69%) — dominantly TAXONOMY, not substance:** the two
  compilers used different enums (mine has no `category-error`/`value-mismatch`; cc3's maps many of
  my `kind-mismatch`/`genericity` calls to those or `other`). Finding: the kill-form classification
  is convention-sensitive; neither taxonomy is canonical. A merged enum would be needed before the
  rate means anything substantive.
- **fact-basis disagreement: 6/155 (3.9%) — SUBSTANTIVE, queued:** B146, B272, B285, B296, **B437**,
  B516 — ids I graded fact_computed=TRUE that cc3 grades ASSERTED. B437 matters most: my B741 sweep
  resolved B435's provenance BY POINTING AT B437 — if B437 itself is asserted, that chain needs
  re-adjudication. All six queued as cheap re-examination cells (width ledger +6 candidates).
- cc3's spectral census (160/162 never consulted emittance; ZERO consulted scattering) independently
  corroborates this compiler's empty-column headline at their corpus.
