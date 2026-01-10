# Stage 2 – FRW corridor belt summary (rungs 1–9, v1)

**Scope.**  
Summarise the Stage 2 FRW corridor analysis built on top of the Phase 4 FRW pipeline. This belt is strictly downstream of Phases 3–4 and does not modify any Phase 3/4 code or claims. It reads Phase 4 FRW masks and probes, defines corridor families over the θ grid, and checks their robustness.

**Status.**  
Diagnostic-only. As of 2026-01-09 no FRW corridor result is promoted into Phase 4/5 text or figures; all outputs are Stage 2 artifacts.

---

## 1. Inputs and data flow

The FRW corridor belt treats the Phase 4 FRW artifacts as fixed inputs:

- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_corridors.json`

All Stage 2 FRW corridor tables live under:

- `stage2/frw_corridor_analysis/outputs/tables/`

Representative outputs:

- `stage2_frw_corridor_rung1_sources_v1.csv`
- `stage2_frw_corridor_rung2_bool_census_v1.csv`
- `stage2_frw_corridor_rung3_families_v1.csv`
- `stage2_frw_corridor_rung4_family_overlap_v1.csv`
- `stage2_frw_corridor_rung5_family_contiguity_v1.csv`
- `stage2_frw_corridor_rung6_stride_robustness_v1.csv`
- `stage2_frw_corridor_rung7_smoothing_robustness_v1.csv`
- `stage2_frw_corridor_rung8_family_fractions_v1.csv`
- `stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`

For a detailed rung-by-rung narrative, see:

- `stage2/frw_corridor_analysis/README_FRW_CORRIDORS_v1.md`
- `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`

---

## 2. Rungs 1–9 at a glance

- **Rung 1 – Sources inventory.**  
  Enumerates FRW masks and probes, records their shapes and basic stats, and checks θ alignment on the 2048-point grid.

- **Rung 2 – Boolean census.**  
  Scans FRW mask columns (e.g. `frw_viable`, `lcdm_like`, data-related flags) and records how many grid points satisfy each, identifying always-true and always-false checks.

- **Rung 3 – Family definitions.**  
  Defines FRW families such as FRW-viable, LCDM-like, toy corridor, and simple intersections, and records their sizes and fractions of the θ grid.

- **Rungs 4–7 – Robustness tests.**  
  Check overlap between families, contiguity of corridor segments in θ, robustness under stride changes, and robustness under small smoothing of FRW quantities.

- **Rung 8 – Family fractions.**  
  Summarises each family by its fraction of the θ grid and by simple scalar diagnostics treated in Phase 4 and Stage 2.

- **Rung 9 – θ★-alignment diagnostic.**  
  Evaluates where θ★ ≈ φ^φ falls relative to the FRW families and records that, in the current toy setup, θ★ lies within the broad FRW-viable band but is not singled out by the corridor machinery.

---

## 3. Takeaways

On the current 2048-point θ grid and Phase 4 FRW snapshot:

- The FRW-viable band is broad and contiguous, covering roughly half of the θ grid.
- Corridor families (viable, LCDM-like, toy corridor, and intersections) are structurally robust under contiguity, stride, and smoothing checks.
- The FRW corridor machinery does not yet pick out a special θ value; in particular, θ★ is a non-special point inside the viable band at this rung.

These results are recorded as Stage 2 diagnostics. Any future promotion into Phase 4/5 text or figures will go through an explicit promotion gate, documented separately in `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md` and in the Stage 2 promotion design docs.
