# Stage 2 — FRW, mech, joint, data and θ★ belt overview (v1)

**Scope:** Internal Stage 2 overview of the FRW corridor, mech/measure,  
joint mech–FRW, FRW data probes, and θ★ alignment rungs.

**Status:** Diagnostic / structural. No claims promoted into Phase 4/5 yet.

---

## 1. Purpose of Stage 2

Stage 2 is a **diagnostic and structural belt** that sits between:

- **Phase 3**: local non-cancellation mechanism and “mechanical” measure tables, and  
- **Phase 4**: FRW background scans and masks (viable band, LCDM-like, toy corridor, etc.).

The goal is to:

1. Understand what the existing Phase 3 and Phase 4 tables actually contain,
2. Build **clean, restartable rungs** that relate them (FRW families, mech measures, joint grid),
3. Check for **robust structure vs artefacts**, and
4. Ensure that **θ★ ≈ φ^φ** is not secretly being “tuned in” by any of the constructions.

Nothing in Stage 2 is allowed to silently change the theory;  
it is purely about **reading and organizing** what the existing runs already say.

---

## 2. FRW corridor analysis (Stage2 FRW belt, rungs 1–9)

**Files (representative):**

- Tables:  
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv`  
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv`  
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`  
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung4_family_overlap_v1.csv`  
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung6_contiguity_v1.csv`  
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung7_stride_robustness_v1.csv`  
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung8_smoothing_v1.csv`  
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`

- Figures:  
  - `stage2/frw_corridor_analysis/outputs/figures/stage2_frw_corridor_family_theta_hist_v1.pdf`  
  - `stage2/frw_corridor_analysis/outputs/figures/stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`

**What these rungs do:**

- Rung 1–2: **inventory + boolean census** of the Phase 4 FRW masks on the θ grid.  
- Rung 3–4: define and summarize FRW corridor families:
  - F1: FRW_VIABLE (~1016/2048, ≈ 0.50 of grid),
  - F2: LCDM_LIKE (~63/2048),
  - F3: TOY_CORRIDOR (~1186/2048),
  - F4: CORRIDOR_AND_VIABLE,
  - F5: CORRIDOR_AND_LCDM,
  - F6: DATA_OK (empty in this run).
- Rung 5: **summary figures** (θ histograms and ω_Λ scatter) per family.
- Rung 6–8: **contiguity, stride robustness, smoothing robustness**:
  - F1–F5 are not singleton specks; they form one or two contiguous segments in θ,
  - the families are stable under subsampling (stride 2,4,8) and under small window smoothing.
- Rung 9: **θ★ alignment** within these FRW families (input to the θ★ diagnostic doc).

**Nontrivial outcome (FRW belt):**

- The FRW-viable band is a **broad, contiguous ~50% band** in θ.
- The toy corridor and its intersections with viability/LCDM form **clean segments**,  
  not noise-like salt-and-pepper.
- These families are **robust** under stride and smoothing tests.
- However, nothing in this FRW belt by itself **singles out** θ★;  
  F1–F5 are about global viability / shape, not about the specific axiom value.

---

## 3. Mech/measure analysis (Stage2 mech belt, rungs 1–6)

**Files (representative):**

- `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung1_phase3_table_inventory_v1.csv`
- `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung2_phase3_column_stats_v1.csv`
- `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung3_phase3_probability_like_candidates_v1.csv`
- `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`
- `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv`
- `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`

**What these rungs do:**

- Rung 1–2: inventory and column statistics for Phase 3 tables:
  - `mech_baseline_scan.csv`, `mech_binding_certificate.csv`,
  - histogram/stat JSONs like `phase3_measure_v1_hist.csv`, `phase3_measure_v1_stats.json`.
- Rung 3–4: identify **probability-like columns** (in [0,1], non-negative, etc.)  
  and separate **measure candidates** vs **flag candidates**.
- Rung 5: examine **θ-profiles** of these candidates along the Phase 3 θ grid.
- Rung 6: select a small **preferred subset** of measure candidates  
  whose θ-profiles are reasonably well-behaved.

**Nontrivial outcome (mech belt):**

- The Phase 3 outputs do contain **plausible measure-like scalars** (e.g. bounds/penalties) that:
  - have support across the θ grid, and
  - change in a structured way rather than pure noise.
- Stage 2 identifies a **shortlist** of these as “preferred measure candidates”  
  without yet turning them into promoted physical claims.

---

## 4. Joint mech–FRW analysis (Stage2 joint belt, rungs 1–4)

**Files (representative):**

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung2_family_summaries_v1.csv`
- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung3_correlations_v1.csv`
- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung4_family_correlations_v1.csv`
- `stage2/joint_mech_frw_analysis/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`

**What these rungs do:**

- Rung 1: build a **joint θ grid**:
  - align Phase 4 FRW tables and Phase 3 mech tables on the same θ indices,
  - attach FRW flags (viable, LCDM-like, corridor, etc.) and mech columns  
    (`mech_baseline_*`, `mech_binding_*`) into one 2048×17 table.
- Rung 2: recompute **FRW family sizes** on this joint grid (sanity check).
- Rung 3: compute **global correlations** between:
  - `{E_vac, ω_Λ, age_Gyr}` and
  - `{mech_baseline_A0, mech_baseline_A_floor, mech_baseline_bound, mech_binding_A0, mech_binding_A, mech_binding_bound}`.
- Rung 4: **family-restricted correlations** (per FRW family) to check whether  
  these relationships persist inside subsets like FRW_VIABLE or TOY_CORRIDOR.

**Nontrivial outcome (joint belt):**

- There are **very strong linear-like correlations**:
  - E_vac and ω_Λ track the mech amplitude/floor very closely (|r| ≈ 0.94–0.98),
  - age_Gyr anticorrelates for the same reason.
- This is not yet a *claim* about the real universe, but it is **structural evidence** that:
  - the Phase 3 mechanism and Phase 4 FRW scans are **not independent knobs**;
  - the mechanism-derived scalars behave like **structured functions of the FRW vacuum sector**.

---

## 5. FRW data probes (Stage2 FRW–data belt, rungs 1–2)

**Files (representative):**

- `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_data_probe_rung1_column_stats_v1.csv`
- `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_data_probe_rung2_viability_cross_v1.csv`
- `stage2/frw_data_probe_analysis/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md`

**What these rungs do:**

- Rung 1: basic statistics on the FRW data probe mask:
  - `has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, `data_ok`.
- Rung 2: cross-tabulate each probe column vs the FRW viability flag.

**Nontrivial outcome (FRW–data belt):**

- The current **placeholder “data_ok” mask is empty**:
  - `data_ok` is false for all θ in this run.
- The diagnostic tells us:
  - we *cannot yet* make any FRW+data corridor claims,
  - future work must either:
    - improve the probe implementation, or
    - plug in actual observational constraints.

In other words, **Stage 2 proves that the present “data_ok” flag is not useable**,  
which is itself an important negative result for gating.

---

## 6. θ★ ≈ φ^φ vs FRW families (diagnostic rung)

**Files:**

- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`
- `stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md`

**What this rung does:**

- For each FRW family (viable band, LCDM-like, toy corridor, intersections), it:
  - finds the θ in that family closest to θ★ ≈ φ^φ,
  - measures the distance |θ − θ★|,
  - records whether θ★ lies inside each family.

**Nontrivial outcome (θ★ diagnostic):**

- θ★ lies **inside the broad FRW-viable band** and behaves like a typical viable θ.
- The toy corridor and LCDM-like sets, as implemented here, **live elsewhere** in θ-space;  
  they do **not** pick θ★.
- Thus, in this run:
  - nothing “mysteriously snaps” to θ★,
  - we have a clear **negative-result baseline** against which future, richer corridors  
    (e.g. with real data or refined mechanisms) must be compared.

---

## 7. Gating and roadmap position

### 7.1. What is **not** promoted (yet)

At this Stage 2 belt v1, **no new artifacts are promoted into Phase 3/4/5**.  
Specifically:

- FRW families, robustness checks, and corridor plots:  
  **Stage 2 internal diagnostics** only.
- Mech measure candidates and θ-profiles:  
  **shortlisted** but not yet declared “the” measure in the main narrative.
- Joint mech–FRW correlations:  
  kept as **internal evidence** that the pieces talk to each other.
- FRW data probes:  
  explicitly documented as **not yet ready** for physical claims.
- θ★ alignment:  
  locked in as a **negative-result sanity check**, not as a claim of selection.

### 7.2. What Stage 2 enables next

Stage 2 belt v1 puts us in position to:

1. Design **Option A** promotions:  
   small, conservative artifacts that could be added to Phase 4/5  
   (e.g. a simple FRW viability fraction table, or a single joint mech–FRW plot)  
   without over-claiming.

2. Design **Option B** promotions:  
   a larger, FRW-focused or measure-focused follow-up phase (Phase 6 or Stage 3)  
   if a richer, data-informed corridor emerges.

3. Re-run FRW and mech belts in future with:
   - improved data probes,
   - refined mechanisms,
   - additional θ grids,
   while still staying within the rung structure defined here.

---

## 8. Status

- **Stage 2 belt v1:** structural and diagnostic, now coherently documented.
- **Next major task (future rung):**  
  a **Stage 2 → Phase 4/5 promotion design** document that:
  - selects a *very small* set of Option A candidates, and
  - leaves more ambitious stories for Option B / later phases.

