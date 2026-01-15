# Stage 2 — Belt overview (FRW, mech, joint, data, θ★, hosts, audits) (v1, updated 2026-01-15)

**Scope:** Internal Stage 2 overview of the main diagnostic belts built on top of Phase 3 (mechanism) and Phase 4 (FRW) outputs, including FRW corridor structure, mech/measure summaries, joint mech–FRW correlations, FRW data probes, θ★ alignment checks, empirical background anchors and external FRW hosts, and documentation/paper audit belts.

**Status:** Diagnostic / structural only. No new physics claims are introduced here and no Stage 2 result is, by itself, promoted into Phase 4/5. All belts are downstream views of locked Phase 3/4 artifacts.

---

## 1. Position of Stage 2 in the program

Stage 2 is a diagnostic belt that sits downstream of the canonical phase ladder and is designed to stress-test, summarise, and visualise what Phase 3 and Phase 4 are already doing without silently changing their claims.

- Upstream:
  - Phase 3 provides mechanism-level tables (mech_baseline_scan, mech_binding_certificate, etc.) and any associated diagnostics under phase3/outputs/tables/.
  - Phase 4 provides FRW mask tables and toy-corridor structure under phase4/outputs/tables/ together with FRW-facing design docs and reproducibility plans.
- Downstream:
  - Stage 2 reads these tables and emits its own CSVs, figures, and markdown summaries under stage2/, always tagged as diagnostic and non-canonical.
  - Any promotion of Stage 2 results into Phase 4/5 must go through an explicit promotion design and Phase 0–style gate documented elsewhere.

This document is a map: it lists the main belts, where they live in the tree, and how they are meant to be read.

---

## 2. Belt catalogue (v1)

Stage 2 currently organises its work into the following belts and diagnostic rungs.

### 2.1 FRW corridor belt

- Purpose: describe the structure of FRW-viable regions on the θ-grid, define corridor families, and test contiguity and robustness.
- Location:
  - Code and outputs under stage2/frw_corridor_analysis/.
  - Summary doc: stage2/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md.
- Diagnostics:
  - Grid-level viability masks (FRW_VIABLE, LCDM_LIKE, TOY_CORRIDOR and intersections).
  - Corridor fractions, contiguity tests, stride and smoothing robustness checks.
- Status: downstream-only; provides structure and sanity checks for Phase 4 FRW masks but does not by itself assert a physical corridor.

### 2.2 Mechanism / measure belt

- Purpose: inventory Phase 3 scalar tables, identify probability-like columns, distinguish measure-like vs flag-like behaviour, and propose preferred diagnostic candidates.
- Location:
  - Code and outputs under stage2/mech_measure_analysis/.
  - Summary doc: stage2/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md.
- Diagnostics:
  - Table inventories and column stats for phase3/outputs/tables/.
  - Probability-like and measure/flag candidate lists.
  - θ-profiles and a small set of preferred, numerically stable measure candidates.
- Status: downstream-only; no single θ-measure is promoted to canonical status and no new Phase 3/4/5 claim is introduced.

### 2.3 Joint mech–FRW belt

- Purpose: build a joint θ-grid over FRW and mech quantities and quantify correlations between FRW scalars and mechanism amplitudes.
- Location:
  - Code and outputs under stage2/joint_mech_frw_analysis/.
  - Summary doc: stage2/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md.
- Diagnostics:
  - Joint table stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv.
  - Family-restricted summaries across ALL_GRID, FRW_VIABLE, LCDM_LIKE, TOY_CORRIDOR and intersections.
  - Correlation tables comparing {E_vac, omega_lambda, age_Gyr} with mech_baseline_* and mech_binding_* scalars.
- Status: downstream-only; records strong correlations and redundancies but does not promote any correlation to a physical identification or causal mechanism.

### 2.4 FRW data-probe belt

- Purpose: audit the Phase 4 FRW data-probe mask and clarify how data-facing flags relate to FRW viability.
- Location:
  - Code and outputs under stage2/frw_data_probe_analysis/.
  - Summary doc: stage2/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md.
- Diagnostics:
  - Column-level stats for phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv.
  - Cross-tabs of probes (has_matter_era, has_late_accel, smooth_H2, data_ok, etc.) versus frw_viable.
- Status: downstream-only; in the current snapshot the aggregate data_ok flag is empty and all FRW families should be interpreted as pre-data corridors. Any future data gate design or promotion is handled in separate design docs and gates.

### 2.5 θ★–FRW alignment diagnostic

- Purpose: check where the θ★ candidate (e.g. θ★ ≈ φ^φ in the original motivation) lands relative to FRW corridor families and viability bands.
- Location:
  - Code and outputs under stage2/theta_star_analysis/.
  - Summary doc: stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md.
- Diagnostics:
  - Reads off θ★ from the joint FRW grid and records which FRW families contain it.
  - Explicitly records this as a structured negative-result sanity check in the current snapshot.
- Status: a single diagnostic rung; θ★ lies inside the broad FRW-viable band but is not specially selected by the current toy corridors or LCDM-like families and is not promoted to any canonical role.

### 2.6 Empirical anchor and external FRW host belt

- Purpose: construct and track a small empirical background-cosmology anchor and a set of external FRW “host” configurations that sit inside the FRW-viable band but are still treated as diagnostic scaffolding rather than physical fits.
- Location:
  - Anchor docs: stage2/docs/STAGE2_EMPIRICAL_ANCHOR_OVERVIEW_v1.md, STAGE2_EMPIRICAL_ANCHOR_STATUS_v1.md, STAGE2_EMPIRICAL_ANCHOR_SUMMARY_v1.md.
  - Host docs: stage2/docs/STAGE2_EXTERNAL_COSMO_HOST_DESIGN_v1.md, STAGE2_EXTERNAL_COSMO_HOST_RESULTS_v1.md, STAGE2_PHASE4_FRW_HOST_SUMMARY_v1.md, STAGE2_PHASE4_FRW_HOST_OPEN_QUESTIONS_v1.md and related FRW host status notes.
- Diagnostics:
  - Defines and monitors small non-empty subsets of the FRW-viable corridor that can act as empirical anchors and host points for future phenomenology.
  - Tracks how these anchors relate to FRW scalars, viability masks and the Stage 2 FRW corridor families.
- Status: diagnostic and design-level only; anchors and hosts are not treated as measurements of the real Universe and are not promoted into Phase 4/5 claims without separate, explicit gates.

### 2.7 Documentation and repo-audit belt

- Purpose: keep the documentation tree, archive status, and open threads aligned with Phase 0 contracts and the actual code and artifact layout.
- Location:
  - Stage 2 doc-audit CSVs and scripts under stage2/doc_repo_audit/.
  - Summary docs: stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md, STAGE2_DOC_OPEN_THREADS_STATUS_v1.md, STAGE2_ARCHIVE_STATUS_v1.md.
- Diagnostics:
  - Doc inventory, broken-reference and orphan-candidate tables.
  - Explicit open-thread lists and archive maps for canonical vs experimental areas.
- Status: governance and hygiene belt only; it does not change any Phase 0–5 claim and is used as a downstream snapshot when preparing publication-grade passes.

### 2.8 Paper-audit belt

- Purpose: audit the Phase 0–5 LaTeX papers and build logs for TODO/TBD/FIXME leakage, build cleanliness, and alignment with Phase contracts and Stage 2 diagnostics.
- Location:
  - Summary and plan docs: stage2/docs/STAGE2_PAPER_AUDIT_OVERVIEW_v1.md, STAGE2_PAPER_AUDIT_PLAN_v1.md.
  - Phase-specific audit docs: stage2/docs/STAGE2_PAPER_AUDIT_PHASE01_v1.md, STAGE2_PAPER_AUDIT_PHASE2_v1.md, STAGE2_PAPER_AUDIT_PHASE3_v1.md, STAGE2_PAPER_AUDIT_PHASE4_v1.md, STAGE2_PAPER_AUDIT_PHASE5_v1.md.
- Diagnostics:
  - Per-phase notes on build cleanliness and residual TODO/FIXME markers.
  - Cross-checks between Phase contracts, paper text, and key Stage 2 diagnostics.
- Status: governance and publication-prep belt only; it does not introduce new physics content and is used to prepare future submission-quality versions of the Phase papers.

---

## 3. How to read this with other Stage 2 docs

For a narrative summary of what we actually found across these belts, see stage2/docs/STAGE2_OVERVIEW_v1.md and stage2/docs/STAGE2_MASTER_VERDICT_v1.md. For promotion design and criteria, see stage2/docs/STAGE2_PROMOTION_DESIGN_v1.md and phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md. For a map of Stage 2 endpoints and tables, see stage2/docs/STAGE2_ENDPOINT_ATLAS_v1.md and stage2/docs/STAGE2_ENDPOINTS_AND_TABLES_MAP_v1.md.

This belt overview is deliberately dry and structural: it tells you where each belt lives, what kind of diagnostics it contains, and which parts of the tree are allowed to change in Stage 2 without touching Phase 0–5 claims. It should be read together with docs/STATE_OF_REPO.md and docs/REPO_MAP_AND_ATLAS_v1.md when you want to audit or extend the Stage 2 layer.
