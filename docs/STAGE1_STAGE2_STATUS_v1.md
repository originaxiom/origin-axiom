# Origin Axiom – Stage I + Stage 2 status (January 2026 snapshot)

This document records a concise status snapshot of Stage I (Phases 0–5) and Stage 2 diagnostic belts as of mid-January 2026. It is a navigation and orientation aid, not a replacement for the Phase papers, claims registers, or Stage 2 belt docs. Whenever there is tension between this summary and the primary sources, the primary sources (Phase 0 contracts, Phase papers, Stage 2 belt docs) win.

---

## 1. Phase ladder status (high level)

The canonical Stage I ladder consists of Phases 0–5, with Stage 2 sitting downstream of Phases 3 and 4:

- Phase 0 – Governance and specification  
  - Status: Locked.  
  - Role: defines what a claim is, how locking and gating work, and how archive and Stage 2 diagnostics relate to canonical phases.  
  - Primary sources: `phase0/CLAIMS.md`, `phase0` contracts, and `artifacts/origin-axiom-phase0.pdf`.

- Phase 1 – Toy ensembles  
  - Status: Locked.  
  - Role: construct and stress-test toy ensembles that can support or falsify a non-cancelling phase twist, and show that a residue can exist and be robust/scalable in controlled settings.  
  - Primary sources: `phase1/` contracts and `artifacts/origin-axiom-phase1.pdf`.

- Phase 2 – Mode-sum + bounded FRW viability  
  - Status: Under Audit (forward-looking).  
  - Role: build a finite mode-sum toy model with a non-cancelling floor, demonstrate the existence and robustness of a residual diagnostic inside this sandbox, and show that a chosen mapping into a flat-FRW wrapper is numerically stable as a toy viability check.  
  - Core claims: existence of a non-zero residual, robustness under controlled parameter sweeps within tested ranges, and stability of a toy FRW embedding. All claims are explicitly pre-data and pre-measure.  
  - Audit status: internally coherent and consistent with current Stage 2 FRW diagnostics; “Under Audit” reflects a conservative choice to allow future tightening as FRW and data layers mature, not a detected contradiction.  
  - Primary sources: `phase2/CLAIMS.md`, `phase2/PHASE2_ALIGNMENT_v1.md`, `stage2/docs/STAGE2_PAPER_AUDIT_PHASE2_v1.md`, and `artifacts/origin-axiom-phase2.pdf`.

- Phase 3 – Mechanism module  
  - Status: Active.  
  - Role: implement a mechanism that enforces a non-cancelling floor over θ, provide smooth, well-controlled amplitudes and certificates, and act as the mechanism backbone for downstream FRW and Stage 2 belts.  
  - Scope: mechanism only; flavor calibration lives in `experiments/phase3_flavor_v1/` and is explicitly archived and non-canonical.  
  - Primary sources: `phase3/MECHANISM_CONTRACT.md`, `phase3/ROLE_IN_PROGRAM.md`, Stage 2 mech/measure and joint mech–FRW docs, and `artifacts/origin-axiom-phase3.pdf`.

- Phase 4 – FRW toy diagnostics (stub)  
  - Status: Diagnostic stub.  
  - Role: map Phase 3 outputs into FRW-like toy backgrounds and viability masks, provide a corridor machinery, and expose a data-probe hook, all at a pre-data, toy level.  
  - Primary sources: `phase4/` contracts and design notes, `phase4/outputs/tables/phase4_F1_frw_*_mask.csv`, `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md`, and the FRW-focused Stage 2 belts.

- Phase 5 – Interface and sanity layer  
  - Status: Rung 0–1.  
  - Role: provide interface and sanity summaries over locked Phase 3/4 outputs and Stage 2 diagnostics without introducing new mechanism or cosmology claims.  
  - Primary sources: `phase5/SCOPE.md`, `phase5/NON_CLAIMS.md`, `phase5/ROLE_IN_PROGRAM.md`, `phase5/PHASE5_VISION_RUNG0.md`, and `artifacts/origin-axiom-phase5.pdf`.

For phase-by-phase detail and claims mapping, see `docs/PHASES.md`, `docs/STATE_OF_REPO.md`, and `docs/CLAIMS_INDEX.md`.

---

## 2. Stage 2 belts summary (diagnostic layer)

Stage 2 is a downstream, non-canonical diagnostic belt over Phases 3 and 4. It does not change Phase claims on its own; any promotion of Stage 2 artifacts into Phase 3/4/5 text or figures must go through explicit Phase 0–style gates.

The current belts are catalogued in `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` and include:

- FRW corridor belt (`stage2/frw_corridor_analysis/`)  
  - Defines FRW families on the Phase 4 θ grid (viable band, LCDM-like, toy corridors and intersections).  
  - Checks contiguity, robustness under stride and smoothing, and basic corridor geometry.

- Mechanism / measure belt (`stage2/mech_measure_analysis/`)  
  - Inventories Phase 3 tables, identifies probability-like columns, and classifies them as measure-like or flag-like candidates.  
  - Studies θ profiles of these candidates and selects a small set of numerically well-behaved diagnostics, without promoting any canonical θ-measure.

- Joint mech–FRW belt (`stage2/joint_mech_frw_analysis/`)  
  - Builds a joint θ grid combining Phase 3 amplitudes with Phase 4 FRW scalars and masks.  
  - Computes correlations and family-wise correlations between {E_vac, ω_Λ, age_Gyr} and the mechanism amplitudes.  
  - Finds strong correlations, consistent sign patterns, and no hidden structure or θ\*-special selection beyond what Phase 4 already encodes.

- FRW data-probe belt (`stage2/frw_data_probe_analysis/`)  
  - Audits the Phase 4 FRW data-probe mask, especially the aggregate `frw_data_ok` flag.  
  - Current snapshot: `has_matter_era` and `smooth_H2` are always true, `frw_viable` ≡ “late acceleration present”, and `frw_data_ok` is empty on the 2048-point grid.  
  - Interpretation: all FRW families are pre-data corridors; the data gate is not yet open.

- θ\* diagnostic belt (`stage2/theta_star_analysis/`)  
  - Checks how θ\* ≈ φ^φ sits inside the FRW families.  
  - Current snapshot: θ\* lies inside the broad FRW-viable band but is not singled out by existing corridor families.  
  - Recorded as a negative-result sanity check and kept strictly Stage 2 internal.

- External host / empirical anchor belts (`stage2/external_cosmo_host/`, `stage2/external_frw_host/`)  
  - Provide a home for external FRW host models and empirical anchors.  
  - Clarify which external datasets or reference cosmologies are conceptually in scope, without yet implementing a fully locked data gate.

- Doc/repo-audit belt (`stage2/doc_repo_audit/` + `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`)  
  - Inventories docs, flags broken references, orphan candidates, and explicit TODO/TBD markers.  
  - Used to drive the doc and layout belts that restructured the repository and clarified archive vs canonical status.

- Paper-audit belt (Phase 0–5)  
  - Audits Phase papers against their contracts and Stage 2 diagnostics.  
  - For each Phase, records whether the narrative matches the contracts and what, if any, adjustments are recommended.  
  - For Phase 2, the current verdict is that the paper is coherent and consistent with the contracts and Stage 2 FRW results; “Under Audit” is reserved for future tightening rather than current contradictions.

A Stage 2 master overview and verdict are given in `stage2/docs/STAGE2_OVERVIEW_v1.md`, `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`, and `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`.

---

## 3. Key outcomes so far (positive and negative results)

Across Stage I and Stage 2, the current snapshot can be summarised at a high level as follows.

Positive structure:

- A clean governance and claims framework (Phase 0), with explicit distinction between canonical phases, Stage 2 diagnostics, and archived experiments.  
- A locked toy-ensemble base (Phase 1) showing that non-cancelling-like residues can exist and be robust in controlled toy models.  
- A mode-sum Phase 2 that demonstrates:
  - existence of a non-zero residual in a finite, QFT-inspired toy model,  
  - robustness of this residual to parameter sweeps within tested ranges,  
  - and a stable toy FRW embedding, all explicitly pre-data and pre-measure.  
- A Phase 3 mechanism module that provides smooth, well-behaved amplitudes and certificates, which Stage 2 shows are strongly correlated with FRW scalars on the current θ grid.  
- A Phase 4 FRW stub plus Stage 2 FRW belts that exhibit a broad, contiguous FRW-viable band with non-trivial corridor structure.  
- An early Phase 5 interface/sanity layer that can be fed by Phase 3/4 outputs and Stage 2 summaries.

Negative or “no special selection yet” results:

- The current FRW corridor machinery does not single out θ\* ≈ φ^φ in any privileged way beyond θ\* lying inside the broad viable band.  
- Current FRW data probes leave `frw_data_ok` empty, so no data-conditioned corridor is claimed; all FRW families should be read as pre-data corridors.  
- No canonical θ-measure has been promoted from Stage 2 mech/measure diagnostics; we only have a shortlist of well-behaved candidate diagnostics.

Structural outcomes:

- Stage 2 is now a coherent, modular diagnostic belt with clear belts and docs, and a promotion design that separates internal diagnostics from any eventual Phase 4/5 promotion.  
- The repository layout (design/audit subdirs, alignment memos, doc spines) has been cleaned to make long-term auditing and collaboration easier.

---

## 4. Open threads and future rungs (non-exhaustive)

This status snapshot does not attempt to enumerate every TODO. It highlights a few program-level threads that are explicitly acknowledged in the current docs:

- Phase 2 (Under Audit):  
  - Forward-looking tightening of approximations and FRW-wrapper narrative as more mature FRW/data layers appear.  
  - Possible future rungs connecting the Phase 2 FRW wrapper more explicitly into the Phase 4/Stage 2 FRW belts and any future data gates.

- Phase 3 (Mechanism module):  
  - Further analysis of mechanism amplitudes as potential θ diagnostics or weights, under more realistic FRW or data-aware setups.  
  - Careful separation between canonical mechanism work and any future flavor-sector add-ons.

- Phase 4 (FRW toy stub) and Stage 2 FRW/data belts:  
  - Design and implementation of a first conservative data gate (`frw_data_ok` or successor) with explicit provenance and promotion gates.  
  - Potential refinement of FRW corridor definitions once data-facing probes are properly tuned and validated.

- Phase 5 (Interface):  
  - Expansion from rung 0–1 toward richer interface/sanity summaries, once upstream FRW/data and measure layers are more mature.  
  - Design of external-facing summaries that can be tied directly to Stage 2 diagnostics and Phase claims.

- Stage 2 promotions:  
  - Option A (minimal promotions into Phase 4/5) and Option B (dedicated FRW/measure phase) remain open; current Stage 2 artifacts are internal diagnostics only.  
  - Any future promotions will need explicit gates and PROGRESS_LOG entries, as outlined in `stage2/docs/STAGE2_PROMOTION_DESIGN_v1.md`.

For detailed open threads, see `stage2/doc_repo_audit/` outputs, the Stage 2 belt docs, and the phase-level alignment memos.

---

## 5. How to use this status snapshot

If you are coming into the project fresh or returning after a break:

- Use this document to understand, at a glance, which phases are locked, which are under audit or active, and what Stage 2 currently supports.  
- Use `docs/STATE_OF_REPO.md`, `docs/PHASES.md`, and `docs/CLAIMS_INDEX.md` to see formal statuses and claims mapping.  
- Use `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` and `stage2/docs/STAGE2_MASTER_VERDICT_v1.md` for the detailed Stage 2 picture.  
- Treat Phase 0 as the constitution: any new claims or promotions should be traceable back to Phase 0 rules, Phase papers, Stage 2 diagnostics, and PROGRESS_LOG entries.

This snapshot is meant to be updated rarely, when Stage I or Stage 2 pass significant milestones (new locks, new belts, or major promotions).

### Obstruction program status (interpretive, non-binding)

As of the obstruction-program-v1 branch, the project maintains an explicit interpretive layer in `docs/OBSTRUCTION_PROGRAM_OVERVIEW_v1.md` that reads the locked Phase 0–5 stack and Stage 2 belts as an exploration of an obstruction to perfect vacuum cancellation. This program does not change the lock status of any Phase or Stage: Phase 0–2 remain locked as specified, Phase 3–5 and Stage 2 retain their documented under-audit or diagnostic roles, and Stage II remains a design-only layer. The obstruction program is a way of threading together existing artefacts and early empirical kernels; promotions of any obstruction-flavoured statements into Phase papers must still pass through the usual Phase 0 gates.
