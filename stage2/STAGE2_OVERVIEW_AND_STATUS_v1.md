# Stage 2 — Overview and Status (v1)

This document summarizes the current Stage 2 diagnostics built on top of
Phase 3 (mechanism) and Phase 4 (FRW) outputs.  It is **purely downstream**:
Stage 2 does not change any Phase 3 or Phase 4 artifacts.  It only inspects
them and records patterns that may be useful for later phases.

Stage 2 is currently organized into three blocks:

- `stage2/frw_corridor_analysis/`   — FRW corridor families and robustness,
- `stage2/mech_measure_analysis/`   — candidate measures / flags from Phase 3,
- `stage2/joint_mech_frw_analysis/` — joint behaviour of FRW and mechanism.

The goal is to answer: *“Given the Phase 3 and Phase 4 outputs we actually
have, what does the landscape of θ look like, and how does the mechanism
behave on top of it?”*  This Stage 2 pass deliberately **does not** try to
promote any new claims into the main phased program.

---

## 1. FRW corridor analysis (Stage 2, FRW rungs 1–9)

**Inputs**

All inputs come from Phase 4 tables:

- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`

These live on a nominal θ–grid of 2048 points.  Stage 2 treats these as
**fixed** and only reads them.

**What we defined**

We encoded several FRW “families” as boolean masks over the θ–grid, for
example (names exactly as in the code):

- `F1_FRW_VIABLE`
- `F2_LCDM_LIKE`
- `F3_TOY_CORRIDOR`
- `F4_CORRIDOR_AND_VIABLE`
- `F5_CORRIDOR_AND_LCDM`
- `F6_DATA_OK`

and measured, for each family:

- `n_theta` (how many θ points),
- `frac_of_grid = n_theta / 2048`,
- contiguity in θ (number and sizes of segments),
- behaviour under:
  - stride subsampling (stride = 1, 2, 4, 8),
  - mild smoothing windows (size 1, 3, 5).

**Key structural findings**

From the FRW rungs (1–9):

- Each family covers a **non-negligible but bounded** fraction of the grid
  (e.g. FRW_viable ~ 0.5 of the grid, toy corridor ~ 0.58, etc.).
- Families are **contiguous or almost contiguous** in θ:
  - most have 1–2 connected segments,
  - there is no wild “salt–and–pepper” behaviour.
- Stride and smoothing tests are extremely stable:
  - the fractions are unchanged to the digits we report,
  - segment counts remain the same,
  - Jaccard index between original and smoothed / subsampled masks is 1.0
    in the tests we ran.
- The distinguished θ\* ≈ 2.178458 **lies inside** the overall corridor
  structure, but there is **no single spike or unique feature** at θ\*
  visible at the level of these binary masks alone.

**Status and verdict**

- Stage 2 FRW analysis concludes that the Phase 4 masks define a **clean,
  robust corridor picture** in θ.
- However, **nothing in these masks alone** is enough to select a unique
  θ or a preferred FRW family.
- These results remain **downstream diagnostics** only; no Phase 4 claims
  or parameters are changed.

---

## 2. Mechanism / “measure” analysis (Stage 2, mech rungs 1–6)

**Inputs**

We examined the Phase 3 outputs:

- `phase3/outputs/tables/mech_baseline_scan.csv`
- `phase3/outputs/tables/mech_baseline_scan_diagnostics.json`
- `phase3/outputs/tables/mech_binding_certificate.csv`
- `phase3/outputs/tables/mech_binding_certificate_diagnostics.json`
- `phase3/outputs/tables/phase3_instability_penalty_v1.json`
- `phase3/outputs/tables/phase3_measure_v1_hist.csv`
- `phase3/outputs/tables/phase3_measure_v1_stats.json`

Again, Stage 2 only **reads** these.

**What we did**

Through rungs 1–6 in `stage2/mech_measure_analysis/`, we:

1. Built an inventory of all Phase 3 tables and JSONs and their basic
   shapes (rows, columns, sizes).
2. Computed column-wise stats and flagged “probability-like” candidates:
   values between 0 and 1, not constant, with non-trivial histograms.
3. From those, filtered a set of **measure candidates** and **flag
   candidates**, recording why they were chosen.
4. For each candidate, built a θ-profile:
   - where it is non-zero,
   - whether it is smooth / monotone / unimodal in θ,
   - whether it behaves sensibly on the Phase 3 θ-grid.
5. Selected a shortlist of **preferred** candidates whose θ-profiles are
   smooth and non-pathological enough to be meaningful in later stages.

The resulting CSVs live under:

- `stage2/mech_measure_analysis/outputs/tables/`

and include:

- `stage2_mech_rung1_phase3_table_inventory_v1.csv`
- `stage2_mech_rung2_phase3_column_stats_v1.csv`
- `stage2_mech_rung3_phase3_probability_like_candidates_v1.csv`
- `stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`
- `stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv`
- `stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`

**Status and verdict**

- Stage 2 identifies a **family of reasonable measure-like candidates**
  over θ that come from Phase 3.
- Some candidates are clearly less attractive (e.g. noisy, highly
  multimodal, or too narrow); others have the kind of smoothness we would
  want from a measure.
- **Stage 2 intentionally does not pick a single “final” measure.**
  Instead, it records which candidates are promising so that Phase 5 (or
  a future Stage 3) can make a principled choice.

---

## 3. Joint mech–FRW analysis (Stage 2, joint rungs 1–4)

**Inputs and construction**

In `stage2/joint_mech_frw_analysis/` we:

1. Built a joint θ-grid table
   `stage2_joint_theta_grid_v1.csv` with columns:

   - FRW side: `theta_index`, `theta`, `E_vac`, `omega_lambda`,
     `age_Gyr`, `in_toy_corridor`, `frw_viable`, `lcdm_like`,
     `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`.
   - Mechanism side: `mech_baseline_*` and `mech_binding_*`
     amplitude / bound columns.

   All inputs come from Phase 3 and Phase 4 tables; we enforce strict
   θ–alignment across them.

2. Defined FRW families on this joint grid (ALL_GRID, FRW_VIABLE,
   LCDM_LIKE, TOY_CORRIDOR, CORRIDOR_AND_VIABLE, CORRIDOR_AND_LCDM,
   FRW_VIABLE_AND_DATA_OK) and recorded their sizes and fractions.

3. Computed correlations between:

   - FRW scalars (`E_vac`, `omega_lambda`, `age_Gyr`)
   - and mechanism amplitudes (baseline and binding variants),

   both on the full grid and restricted to each FRW family.

All summary tables live in:

- `stage2/joint_mech_frw_analysis/outputs/tables/`, including

  - `stage2_joint_mech_frw_rung2_family_summaries_v1.csv`
  - `stage2_joint_mech_frw_rung3_correlations_v1.csv`
  - `stage2_joint_mech_frw_rung4_family_correlations_v1.csv`

**Key patterns**

At the level of this Stage 2 pass:

- On the **full grid**, the mechanism amplitudes are:

  - **strongly positively correlated** with `E_vac` and `omega_lambda`,
  - **strongly negatively correlated** with `age_Gyr`,
  - with signs and magnitudes consistent with the intuition that higher
    vacuum energy / Λ → larger mechanism amplitude and smaller cosmic age.

- Within FRW families (e.g. FRW_VIABLE, TOY_CORRIDOR), the same pattern
  largely persists: the mechanism is not destroyed by FRW cuts; it
  continues to track the underlying FRW scales.

- The current `frw_data_ok` flag is extremely restrictive: in the
  snapshot we analyzed, the intersection

  - `FRW_VIABLE_AND_DATA_OK`

  is empty on the grid (zero θ points).

  This is recorded as a **Stage 2 observation**, not a claim about the
  real universe; it indicates that the present Phase 4 `data_ok` logic is
  either a placeholder or still too strict.

**Status and verdict**

- Stage 2 joint analysis confirms that:

  - The mechanism’s amplitude behaves *smoothly and monotonically* with
    FRW vacuum scales.
  - FRW viability and corridor structure do not introduce any obvious new
    pathologies into the mechanism side.

- At the same time, with the current `frw_data_ok` definition there is
  **no θ that is simultaneously FRW_viable and data_ok** in this toy
  pipeline.  This is an important flag for future Phase 4 / Phase 5 work.

- Stage 2 makes **no attempt** to promote a joint “best θ” or a final
  measure from these correlations alone.

---

## 4. Role in the larger roadmap

Stage 2 (FRW corridors, mechanism diagnostics, and joint behaviour) serves
three roles in the overall phased program:

1. **Quality control and robustness checks**

   - Are the Phase 4 FRW masks well-behaved as functions of θ?
   - Do simple robustness tests (stride, smoothing) change the picture?
   - Are there glaring inconsistencies between Phase 3 amplitudes and
     Phase 4 FRW scales?

   Stage 2 answers “yes, things are structurally clean” and “no, we do
   not see catastrophic inconsistencies.”

2. **Negative and non-selection results**

   - The existing FRW masks and toy `data_ok` flag do *not* single out a
     unique θ or even a non-empty FRW_viable∧data_ok region.
   - Nothing in this diagnostic pass alone can be read as
     “Stage 2 proves θ\* is selected.”

   These are valuable constraints on what we are **not** yet allowed to
   claim in Phase 4 or Phase 5.

3. **Input to future phases**

   - The catalogue of measure candidates and their θ-profiles feeds into
     future measure / prior choices in Phase 5.
   - The joint FRW–mechanism correlations inform how we might design
     higher-level criteria (e.g. tradeoffs between vacuum energy,
     cosmic age, and mechanism amplitude).
   - The empty FRW_viable∧data_ok region highlights where Phase 4
     observational logic needs to be revisited.

---

## 5. Status: Stage 2 v1

As of this document:

- Stage 2 FRW corridor analysis (rungs 1–9) is **complete for v1**.
- Stage 2 mechanism / measure analysis (rungs 1–6) is **complete for v1**.
- Stage 2 joint mech–FRW analysis (rungs 1–4) is **complete for v1**.

Any future changes to these diagnostics should:

1. Add new scripts and outputs with a bumped suffix
   (e.g. `_v2`, `_v3`, …), and
2. Update this document with a new section describing the change and its
   impact on the higher-level story.

