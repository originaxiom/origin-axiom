# Stage 2 – Joint mech–FRW belt summary (rungs 1–4, v1)

**Scope.**  
Summarise the Stage 2 joint mech–FRW analysis that combines Phase 3 mechanism tables with Phase 4 FRW masks on a common θ grid. The belt is downstream-only and does not modify Phase 3/4 pipelines; it quantifies how mechanism-derived scalars and FRW quantities co-vary.

**Status.**  
Diagnostic-only. No new physical claim or preferred θ is introduced at this rung.

For the original design document, see:

- `docs/STAGE2_JOINT_MECH_FRW_PLAN_v1.md`

---

## 1. Inputs and joint grid

Inputs:

- FRW masks and probes from Phase 4 and Stage 2 FRW corridor work:
  - `phase4_F1_frw_shape_probe_mask.csv`
  - `phase4_F1_frw_data_probe_mask.csv`
  - `phase4_F1_frw_viability_mask.csv`
  - `phase4_F1_frw_lcdm_probe_mask.csv`
- Mechanism amplitudes and diagnostics from Phase 3:
  - `mech_baseline_scan.csv`
  - `mech_binding_certificate.csv`

Stage 2 builds a single joint θ grid table:

- `stage2_joint_theta_grid_v1.csv` (2048 rows × 17 columns)

This table aligns all FRW scalars, FRW masks, and mechanism amplitudes on a common θ grid, with strict θ-alignment checks before the join.

---

## 2. Families and correlations

On the joint grid, Stage 2 defines and analyses several FRW families:

- ALL_GRID
- FRW_VIABLE
- LCDM_LIKE
- TOY_CORRIDOR
- CORRIDOR_AND_VIABLE
- CORRIDOR_AND_LCDM
- FRW_VIABLE_AND_DATA_OK

Outputs include:

- `stage2_joint_mech_frw_rung2_family_summaries_v1.csv`
- `stage2_joint_mech_frw_rung3_correlations_v1.csv`

Key findings:

- **Family sizes and fractions.**  
  Family sizes and grid fractions match the corresponding Stage 2 FRW corridor results, validating the construction of the joint grid.

- **Scalar correlations.**  
  FRW scalars such as `E_vac`, `omega_lambda`, and `age_Gyr` show very strong correlations with mechanism amplitudes (`mech_baseline_*`, `mech_binding_*`), with correlation coefficients |r| close to 1 for several pairs and consistent sign patterns (for example `E_vac` and `omega_lambda` correlate, while `age_Gyr` anti-correlates).

- **Family-wise behaviour.**  
  When correlations are recomputed within each FRW family, the same qualitative patterns persist, indicating that the mechanism amplitudes are essentially smooth re-parameterisations of the FRW scalars on the current grid.

---

## 3. Takeaways

- On the current 2048-point θ grid and toy FRW setup, Phase 3 mechanism amplitudes are highly redundant with Phase 4 FRW scalars; no additional hidden structure emerges.
- There is no special anomaly at θ★ ≈ 2.178458 visible at this resolution; θ★ behaves like a generic point inside the broad FRW-viable band.
- Joint mech–FRW results are therefore treated as structural diagnostics and cross-checks rather than as new physics claims. Any future use in Phase 4/5 would be via short textual remarks or figures gated through the Stage 2 promotion design.
