# Stage 2 FRW diagnostics verdict (corridors, data probes, and θ★)

Status (2026-01-11): This document synthesises the Stage 2 FRW corridor and data-probe rungs into a compact physics-facing verdict. It is descriptive and diagnostic-only and does not introduce new claims beyond those already present in Phase 2/4 contracts and Stage 2 docs.

## 1. Inputs and scope

This verdict is based on the following Stage 2 FRW-related artifacts:

- `stage2/frw_corridor_analysis/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md` (FRW corridor belt, rungs 1–9).
- `stage2/frw_data_probe_analysis/docs/STAGE2_FRW_DATA_PROBE_AUDIT_v1.md` (FRW data-probe audit, rungs 1–2).
- `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` and `stage2/docs/STAGE2_OVERVIEW_v1.md` (Stage 2 belt overviews, including FRW and θ★ diagnostics).
- `stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md` (θ★ alignment with FRW families).
- Phase 4 FRW tables under `phase4/outputs/tables/` (e.g. `phase4_F1_frw_shape_probe_mask.csv`, `phase4_F1_frw_data_probe_mask.csv`, `phase4_F1_frw_viability_mask.csv`, `phase4_F1_frw_lcdm_probe_mask.csv`) that Stage 2 FRW scripts consume.

The FRW diagnostics operate on a fixed 2048-point θ-grid and are downstream of locked Phase 3 mechanism tables and Phase 4 FRW constructions. They are strictly pre-data diagnostics: no data-conditioned corridor is currently populated.

## 2. FRW viability corridor: existence, shape, and robustness

The corridor belt rungs (as summarised in `STAGE2_FRW_CORRIDOR_SUMMARY_v1.md` and the Stage 2 overviews) establish the following:

- There is a **non-empty, structured FRW-viable band** on the 2048-point θ-grid, as defined by the Phase 4 viability mask. In the current snapshot the viable set occupies roughly half of the grid (1016 viable vs 1032 non-viable points), so viability is neither isolated nor trivial.
- The FRW-viable set is **broad and contiguous** in θ when mapped to corridor-style families: it forms bands rather than sparse spikes, and contiguity checks find extended intervals rather than isolated points.
- The corridor belt defines several FRW-related families (e.g. F1–F5 style families built from viability, LCDM-like masks, and toy corridor masks) and shows that:
  - family fractions over the grid are stable across modest changes in stride or smoothing,
  - corridor definitions built from local conditions do not fragment into pathological patterns at this resolution,
  - and intersections such as “viable ∧ LCDM-like” or “corridor ∧ viable” remain interpretable subsets, even if they are not yet promoted beyond Stage 2.
- Sanity masks such as `has_matter_era` and `smooth_H2` are, in the current configuration, effectively always true on the sampled grid, so the primary nontrivial FRW cut is encoded by a late-acceleration condition (`has_late_accel`) and its equivalence with the Phase 4 `frw_viable` mask.

Taken together, these results support a clear structural verdict: on the current 2048-point grid the FRW construction admits a broad, contiguous viability band and a family hierarchy built on top of it, so the FRW toy world is neither empty nor degenerate, and corridor-style talk is meaningful at the toy level.

## 3. FRW data probes and the `frw_data_ok` gate

The FRW data-probe audit (`STAGE2_FRW_DATA_PROBE_AUDIT_v1.md`) focuses on the `phase4_F1_frw_data_probe_mask.csv` and `phase4_F1_frw_viability_mask.csv` tables and the aggregate data flag `frw_data_ok`. Its key findings are:

- On the 2048-point grid, probes such as `has_matter_era` and `smooth_H2` are **always true** and act as structural sanity checks rather than selective filters in the present snapshot.
- The condition `has_late_accel` is **exactly equivalent** to the FRW viability mask `frw_viable` at this stage: every viable point has late acceleration, and every point with late acceleration is viable, once the always-true sanity checks are accounted for.
- The aggregate data flag `frw_data_ok` is **identically false**:
  - there are no grid points with `frw_data_ok = true`,
  - the intersection `FRW_VIABLE ∧ DATA_OK` is empty,
  - and any potential “data-conditioned corridor” (defined by viability ∧ data_ok) is empty in this snapshot.

The intended interpretation, recorded in the Stage 2 docs and reinforced here, is that:

- the FRW viability corridor is currently a **pre-data structural corridor**,
- the FRW data gate is **not yet open** in the current pipeline,
- and the emptiness of `frw_data_ok` is a statement about pipeline and probe design state, not a physical exclusion of the origin-axiom corridor.

This verdict constrains how Phase 4 and Phase 5 can talk about FRW corridors: they may legitimately discuss pre-data viability corridors and related families but must not claim a populated data-conditioned corridor until the `frw_data_ok` gate is revised and populated under a separate promotion rung.

## 4. θ★ alignment with FRW families

The θ★–FRW alignment diagnostic rung (`STAGE2_THETA_STAR_ALIGNMENT_v1.md`) reads off the position of θ★ (numerically close to φ^φ ≈ 2.178458) relative to the FRW-viable band and related FRW families defined on the θ-grid. Its main conclusions are:

- θ★ lies strictly **inside the broad FRW-viable band** on the current grid. It is not excluded by the toy FRW viability notion; the toy universe defined by θ★ is a member of the viable band.
- θ★ does **not** sit at a distinguished feature or extremum of the current FRW corridor machinery: it is not uniquely singled out by any of the basic FRW families (viable, LCDM-like, toy corridor, or their intersections) defined at this stage.
- When viewed through the Stage 2 corridor and family diagnostics, θ★ is a **typical viable point** in the current band: neither forbidden nor specially selected by the FRW machinery in its present toy form.

This is recorded as a **negative-result sanity check**: the existing FRW corridors and probe definitions do not produce a special “snap” to θ★ in the current configuration. Future refinements of the mechanism, FRW construction, or data probes might change this, but any such changes would require explicit new rungs and gates.

## 5. FRW diagnostics verdict (current snapshot)

Putting the corridor, data-probe, and θ★ results together, the Stage 2 FRW belt supports the following verdict for the current toy setup:

- The Phase 4 FRW construction, as implemented and sampled on a 2048-point θ-grid, admits a **broad, contiguous FRW-viable band** and a hierarchy of corridor-style families that are robust under contiguity and stride tests. At this level, the FRW toy world is structurally nontrivial.
- The **FRW data gate is not yet open**: the aggregate data flag `frw_data_ok` is empty, so all present corridors and families are **pre-data corridors** and must be described as such in Phase 4/5 narratives.
- θ★ lies in the FRW-viable band but is **not singled out** by current FRW families or probes; there is no present evidence, within this toy FRW machinery, that the FRW sector prefers θ★ over other viable points.
- The FRW diagnostics are **consistent with Phase 2 and Phase 4 contracts** when interpreted as toy constructions: they do not overrule any locked claims but sharpen the internal picture that Phase 2/4 are allowed to describe.

This verdict is intentionally conservative: it treats the FRW diagnostics as internal structure in a toy universe generated by the current mechanism and FRW pipeline. Any future claim that a FRW corridor is data-selected or that θ★ is specially preferred would require substantive changes to the FRW data gate and additional phases or promotion rungs.

## 6. Potential future rungs (not executed here)

This verdict suggests, but does not enact, a few future Stage 2 and Phase 4/5 rungs:

- FRW refinement belts that adjust FRW constructions, probe definitions, and sampling resolution to test the robustness of the viable band and corridor shapes (e.g. different grids, alternative probe definitions, or tighter smoothness conditions).
- Data-gate rungs that revisit `frw_data_ok` and its constituent probes to eventually open a controlled data gate; any resulting data-conditioned corridor would need its own promotion gate and Phase 4/5 claim updates.
- Interface rungs in Phase 5 that turn this verdict into explicit interface tables and reader-facing summaries, with clear separation between internal program verdicts and external phenomenology.

Those are left for future work and are not part of this descriptive verdict.
