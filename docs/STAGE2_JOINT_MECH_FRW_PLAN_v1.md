# Stage 2: Joint mech–FRW analysis — Plan v1

## 0. Context and scope

This document defines a Stage 2 analysis spine that will *jointly* inspect:

- Phase 3 mechanism / measure tables, and
- Phase 4 FRW corridor / viability masks,

without modifying any Phase 3–5 workflows or papers.

The intent is to understand how candidate **measures** from Phase 3 behave
across the FRW families identified in Phase 4 and Stage 2 FRW analysis, *not*
to introduce new physical claims or preferred parameters at this stage.

All work here is **Stage 2 only**:
- downstream of the phased program,
- reproducible from existing artifacts,
- fully reversible and non-binding.

Promotion of any result into the phased program (e.g. Phase 5 or a future
Phase 6) will be handled separately with explicit rungs and contracts.

---

## 1. Inputs and artifacts

### 1.1 Phase 3 / Stage 2 mech–measure inputs

Core Phase 3 tables (already tracked and used):

- `phase3/outputs/tables/mech_baseline_scan.csv`
- `phase3/outputs/tables/mech_binding_certificate.csv`
- `phase3/outputs/tables/phase3_measure_v1_hist.csv`
- `phase3/outputs/tables/phase3_measure_v1_stats.json`
- `phase3/outputs/tables/phase3_instability_penalty_v1.json`

Stage 2 mech/measure outputs (rungs 1–6):

- `stage2/mech_measure_analysis/outputs/tables/`:
  - `stage2_mech_rung1_phase3_table_inventory_v1.csv`
  - `stage2_mech_rung2_phase3_column_stats_v1.csv`
  - `stage2_mech_rung3_phase3_probability_like_candidates_v1.csv`
  - `stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`
  - `stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv`
  - `stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`

These define:
- which columns are probability-like,
- which are treated as **measure** vs **flag** candidates,
- and which subset is currently marked as preferred (Stage 2 shortlist).

### 1.2 Phase 4 / Stage 2 FRW corridor inputs

Core Phase 4 FRW tables (already tracked and used):

- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_corridors.json`
- `phase4/outputs/tables/phase4_F1_frw_*_diagnostics.json`

Stage 2 FRW corridor outputs (rungs 1–9):

- `stage2/frw_corridor_analysis/outputs/tables/`:
  - `stage2_frw_corridor_rung1_sources_v1.csv`
  - `stage2_frw_corridor_rung2_bool_census_v1.csv`
  - `stage2_frw_corridor_rung3_families_v1.csv`
  - `stage2_frw_corridor_rung4_family_overlap_v1.csv`
  - `stage2_frw_corridor_rung6_contiguity_v1.csv`
  - `stage2_frw_corridor_rung7_stride_robustness_v1.csv`
  - `stage2_frw_corridor_rung8_smoothing_v1.csv`
  - `stage2_frw_corridor_rung9_segments_v1.csv`
  - `stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`

- `stage2/frw_corridor_analysis/outputs/figures/`:
  - `stage2_frw_corridor_family_theta_hist_v1.pdf`
  - `stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`

These define:
- FRW families F1–F6 (viable, LCDM-like, toy corridor, intersections, data_ok),
- their occupancy, contiguity, stride/smoothing robustness,
- and their relation (or lack thereof) to the current θ* ≈ φ^φ anchor.

---

## 2. High-level questions (Stage 2 only)

The joint mech–FRW analysis is allowed to ask only questions of the form:

1. **Association:**  
   How do candidate Phase 3 measures behave on different FRW families  
   (e.g. F1_FRW_VIABLE vs F5_CORRIDOR_AND_LCDM)?

2. **Regularity:**  
   Are there measures whose θ-profiles are especially regular, monotonic,
   or sharply structured *within* the FRW corridors compared to outside?

3. **Stability:**  
   Do any candidate measures remain “well behaved” (e.g. bounded, smooth,
   non-pathological) across the intersection of:
   - FRW viability,
   - LCDM-likeness,
   - and toy-corridor structure?

4. **θ* context (non-privileging at this stage):**  
   How do these behaviours look **near** θ* compared to the rest of the grid,
   without asserting that θ* is selected or special?

Forbidden at this stage:

- Declaring a unique or “true” measure.
- Claiming that θ* is physically selected by FRW constraints.
- Modifying or re-interpreting Phase 3–5 claims.

All conclusions must be phrased as:
- “Given the current toy FRW grid and toy mechanisms, we *observe that* …”

---

## 3. Proposed Stage 2 joint spine

We anticipate a new directory:

- `stage2/joint_mech_frw_analysis/`
  - `src/`
  - `outputs/tables/`
  - `outputs/figures/`

### Rung J1 — Build joint θ-grid dataset

**Goal:**  
Create a per-θ table that aligns:

- Phase 3 preferred measure candidates (from Rung 6), with
- Phase 4 FRW masks and families (F1–F6).

**Inputs (read-only):**

- `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`
- Underlying Phase 3 tables referenced there (e.g. `mech_baseline_scan.csv`, etc.)
- `phase4/outputs/tables/phase4_F1_frw_*_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_corridors.json`

**Output (Stage 2 only):**

- `stage2/joint_mech_frw_analysis/outputs/tables/joint_theta_grid_v1.csv`

with columns along the lines of:

- `theta`, `theta_index`
- FRW booleans / flags (viable, lcdm_like, in_toy_corridor, etc.)
- candidate measure columns (one per preferred measure)
- optional diagnostics (e.g. which family each row belongs to)

The main purpose is to define a **single, canonical dataset** on which all
later joint rungs operate.

### Rung J2 — Basic association diagnostics

**Goal:**  
Quantify simple associations between FRW families and measures.

Examples:

- Conditional summaries:
  - `E[measure | FRW_VIABLE]` vs `E[measure | ~FRW_VIABLE]`
  - `E[measure | CORRIDOR_AND_LCDM]` vs complements
- Simple correlation-like diagnostics:
  - correlation between measures and FRW booleans (treated as 0/1)

**Outputs:**

- `stage2/joint_mech_frw_analysis/outputs/tables/joint_family_measure_summaries_v1.csv`

No modelling, no regression claims yet — just descriptive statistics.

### Rung J3 — Family-level shape comparison

**Goal:**  
Compare the θ-profiles of selected measures *within* each FRW family vs
the complement.

Outputs might include:

- A table of simple shape descriptors per (measure, family):
  - e.g. approximate monotonicity flags, support width, number of “bumps”.
- Optional figures:
  - per-family θ-profiles for a small number of key measures.

All figures would be `*.pdf` under:

- `stage2/joint_mech_frw_analysis/outputs/figures/`

Again, Stage 2 only; these are *diagnostic* plots.

### Rung J4 — θ* neighbourhood diagnostics

**Goal:**  
Assess how candidate measures and FRW families behave in a small θ-window
around θ* ≈ φ^φ (in radians), without asserting any selection.

Steps:

- Define a local θ-window (e.g. a small band in θ or a fixed number of
  nearest grid points).
- Record how:
  - FRW families populate that window, and
  - measures behave there vs the global grid.

Outputs:

- `stage2/joint_mech_frw_analysis/outputs/tables/joint_theta_star_neighbourhood_v1.csv`
- Optional small summary figure (e.g. θ-zoom panels).

### Rung J5 — Promotion criteria (Stage 2 verdicts only)

**Goal:**  
Derive *Stage 2* meta-conclusions of the form:

- “These measures remain stable and interpretable across the FRW corridors.”
- “No FRW family currently singles out θ* in any strong way.”
- “Candidate X could *in principle* be promoted as a scalar diagnostic
  in a future phase, provided further physics-facing scrutiny.”

Outputs:

- `stage2/joint_mech_frw_analysis/outputs/tables/joint_mech_frw_promotion_candidates_v1.csv`
- A short summary doc:
  - `docs/STAGE2_JOINT_MECH_FRW_RUNG1_5_SUMMARY_v1.md`

No promotion into Phase 3–5 happens here; we only tag candidates as
“interesting enough to consider later” vs “probably not worth promoting”.

---

## 4. Relationship to the broader roadmap

- **Upstream:**
  - Uses only existing Phase 3 and Phase 4 artifacts and Stage 2 spines.
  - Respects all current contracts: no rewrites of mechanism, FRW toy
    model, or Phase 5 summaries.

- **Sideways:**
  - Provides a concrete playground where:
    - the non-cancellation mechanism (Phase 3),
    - FRW viability corridors (Phase 4),
    - and Stage 2 exploratory analysis
    can interact in a controlled, reversible way.

- **Downstream:**
  - If strong, robust patterns appear (e.g. certain measures behaving
    cleanly across FRW corridors), they can motivate:
    - a future Phase 6 (“corridors + measure”) paper, or
    - a carefully scoped extension to Phase 5.

Any such promotion would be governed by new rungs and explicit contracts.

---

## 5. Status

- This document is a **plan only**.
- No `stage2/joint_mech_frw_analysis` code exists yet.
- When we start implementing, each rung (J1–J5) will:
  - live under `stage2/joint_mech_frw_analysis/src/`,
  - write outputs under `stage2/joint_mech_frw_analysis/outputs/`,
  - and be logged in `PROGRESS_LOG.md` with explicit Stage 2 labels.

