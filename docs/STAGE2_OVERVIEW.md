# Stage 2 Overview — Exploratory Analysis Lab

Stage 2 is an **exploratory lab layer** that sits *downstream* of the main phased program.

- It **never mutates** `phase3/` or `phase4/` outputs.
- It **does not define new claims** about the real Universe.
- Its job is to:
  1. Stress-test and summarize existing Phase 3 / Phase 4 artifacts.
  2. Identify non-trivial structures (corridors, measures, correlations).
  3. Prepare a shortlist of candidate diagnostics and stories that may
     later be promoted into Phase 5 / a dedicated Stage-2-style paper.

Until explicitly promoted, all Stage 2 results are **exploratory diagnostics only**.

---

## Directory layout

All Stage 2 work lives under:

- `stage2/frw_corridor_analysis/`
- `stage2/mech_measure_analysis/`
- `stage2/joint_mech_frw_analysis/`

Each submodule is organized in **rungs**, with:

- `src/` — scripts named `*_v1.py` (or similar), one rung per script.
- `outputs/tables/` — CSV outputs.
- `outputs/figures/` — plots (for the FRW corridor analysis).

Rungs are designed to be:

- self-contained,
- restartable,
- auditable (inputs and outputs are explicit).

---

## 1. FRW Corridor Analysis

**Path:** `stage2/frw_corridor_analysis/`  
**Inputs:** Phase 4 FRW tables

- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`

**High-level question:**  
> How do the FRW “good behaviour” flags organize themselves over θ?  
> Do we genuinely have corridor-like bands, or just noisy masks?

### Rung 1 — Source table inventory

- **Script:** `src/analyze_frw_corridor_v1.py`
- **Output:**  
  - `outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv`
- **What it does:**
  - Checks that the expected Phase 4 FRW tables exist.
  - Records file sizes and shapes (n_rows, n_cols).
- **What it establishes:**
  - Phase 4 FRW masks are present and structurally consistent
    (2048-point grid, expected columns).

### Rung 2 — Boolean census

- **Script:** `src/analyze_frw_corridor_bool_census_v1.py`
- **Output:**  
  - `outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv`
- **What it does:**
  - Scans the FRW mask tables for boolean-like columns.
  - Counts `n_true`, `n_false`, and optional `n_na` for each.
- **What it establishes:**
  - Key FRW flags (`has_matter_era`, `has_late_accel`, `smooth_H2`,
    `frw_viable`, `lcdm_like`, `in_toy_corridor`, etc.) are:
    - well-behaved 0/1 fields,
    - non-trivial (not identically true or false),
    - consistent across tables.

### Rung 3 — FRW families on θ-grid

- **Script:** `src/analyze_frw_corridor_families_v1.py`
- **Output:**  
  - `outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`
- **What it does:**
  - Defines FRW “families” on the θ grid, including:
    - `F1_FRW_VIABLE`
    - `F2_LCDM_LIKE`
    - `F3_TOY_CORRIDOR`
    - `F4_CORRIDOR_AND_VIABLE`
    - `F5_CORRIDOR_AND_LCDM`
    - `F6_DATA_OK` (currently empty in this toy)
  - Records `n_theta` and `frac_of_grid` for each.
- **What it establishes:**
  - There are genuine FRW bands (corridors) on the θ grid occupying
    non-negligible fractions of the scan, not isolated grid glitches.

### Rung 4 — Family overlaps

- **Script:** `src/analyze_frw_corridor_family_overlap_v1.py`
- **Output:**  
  - `outputs/tables/stage2_frw_corridor_rung4_family_overlap_v1.csv`
- **What it does:**
  - Computes overlap statistics between the families above.
- **What it establishes:**
  - Relations such as:
    - how much of the toy corridor is FRW-viable,
    - how much of the LCDM-like region lies inside the corridor,
    - how disjoint or nested these bands are.

### Rung 5 — Corridor figures (θ and ΩΛ views)

- **Script:** `src/plot_frw_corridor_families_v1.py`
- **Outputs (PDFs):**  
  - `outputs/figures/stage2_frw_corridor_family_theta_hist_v1.pdf`  
  - `outputs/figures/stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`
- **What it does:**
  - θ-histograms of family membership.
  - Scatter of `(omega_lambda, theta)` colored by family ID.
- **What it establishes:**
  - Provides a visual, corridor-like picture of:
    - where the FRW families live in θ,
    - how they map into the `(Ω_Λ, θ)` plane.

*(These figures are candidates for future promotion into a Phase 5/6
appendix, but are currently exploratory only.)*

### Rung 6 — Contiguity of families

- **Script:** `src/analyze_frw_corridor_contiguity_v1.py`
- **Output:**  
  - `outputs/tables/stage2_frw_corridor_rung6_contiguity_v1.csv`
- **What it does:**
  - For each family, finds contiguous segments in θ (in grid index space).
  - Records number of segments and how many θ points each covers.
- **What it establishes:**
  - FRW_VIABLE is one long contiguous band.  
  - Other families live in a small number of segments.
  - The corridor structure is geometrically clean, not a noisy checkerboard.

### Rung 7 — Stride robustness

- **Script:** `src/analyze_frw_corridor_stride_robustness_v1.py`
- **Output:**  
  - `outputs/tables/stage2_frw_corridor_rung7_stride_robustness_v1.csv`
- **What it does:**
  - Decimates the θ grid with strides 1, 2, 4, 8.
  - Recomputes family fractions and segment counts on each subgrid.
- **What it establishes:**
  - Family fractions are essentially invariant under coarse subsampling.
  - Corridor structure is robust to moderate grid thinning.

### Rung 8 — Smoothing robustness

- **Script:** `src/analyze_frw_corridor_smoothing_v1.py`
- **Output:**  
  - `outputs/tables/stage2_frw_corridor_rung8_smoothing_v1.csv`
- **What it does:**
  - Applies small boolean smoothing windows (e.g. sizes 1,3,5) to the
    family masks.
  - Compares pre- and post-smoothing masks via Jaccard index and segment
    counts.
- **What it establishes:**
  - For tested windows, the key families are exactly invariant
    (Jaccard ≈ 1), confirming that they are not fragile single-point spikes.

### Rung 9 — Segments and θ★ alignment

- **Script:** `src/analyze_frw_corridor_segments_theta_star_v1.py`
- **Outputs:**  
  - `outputs/tables/stage2_frw_corridor_rung9_segments_v1.csv`  
  - `outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`
- **What it does:**
  - Tabulates segment-level information for each family.
  - Computes, for each family, the θ in that family closest to θ★
    (≈ φ^φ) and its distance |Δθ|.
- **What it establishes:**
  - θ★ lies inside the broad FRW-viable band but does **not** coincide
    with the tight toy LCDM-like intersection.  
  - This confirms that θ★ is **not hard-wired** as the center of the
    toy corridor; it is a test point inside a larger viable region.

---

## 2. Mechanism / Measure Analysis

**Path:** `stage2/mech_measure_analysis/`  
**Inputs:** Phase 3 mechanism outputs

- `phase3/outputs/tables/mech_baseline_scan.csv`
- `phase3/outputs/tables/mech_baseline_scan_diagnostics.json`
- `phase3/outputs/tables/mech_binding_certificate.csv`
- `phase3/outputs/tables/mech_binding_certificate_diagnostics.json`
- `phase3/outputs/tables/phase3_instability_penalty_v1.json`
- `phase3/outputs/tables/phase3_measure_v1_hist.csv`
- `phase3/outputs/tables/phase3_measure_v1_stats.json`

**High-level question:**  
> Among the Phase 3 outputs, what actually behaves like a **measure** or  
> probability-like weight over θ, rather than arbitrary numbers?

### Rung 1 — Phase 3 table inventory

- **Script:** `src/inventory_phase3_tables_v1.py`
- **Output:**  
  - `outputs/tables/stage2_mech_rung1_phase3_table_inventory_v1.csv`
- **What it does:**
  - Scans `phase3/outputs/tables/` for CSV / JSON files.
  - Records sizes and shapes.
- **What it establishes:**
  - Confirms presence and basic health of Phase 3 tables.

### Rung 2 — Column-level stats

- **Script:** `src/analyze_phase3_table_columns_v1.py`
- **Output:**  
  - `outputs/tables/stage2_mech_rung2_phase3_column_stats_v1.csv`
- **What it does:**
  - Computes per-column statistics: min/max, mean, std, counts of
    non-finite values, etc.
  - Includes both CSV columns and JSON-derived summaries.
- **What it establishes:**
  - Identifies which columns are bounded, non-negative, etc., and which
    are obviously non-measure-like.

### Rung 3 — Probability-like candidate search

- **Script:** `src/analyze_phase3_probability_like_columns_v1.py`
- **Output:**  
  - `outputs/tables/stage2_mech_rung3_phase3_probability_like_candidates_v1.csv`
- **What it does:**
  - Applies heuristics to identify “probability-like” columns:
    - values in [0,1] or bounded non-negative,
    - sums or integrals consistent with a weight distribution,
    - simple shape hints from the stats table.
- **What it establishes:**
  - Produces a shortlist of Phase 3 columns that behave like honest
    weights or measures over θ.

### Rung 4 — Measure vs flag candidates

- **Script:** `src/select_phase3_measure_candidates_v1.py`
- **Output:**  
  - `outputs/tables/stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`
- **What it does:**
  - Splits the Rung 3 candidates into:
    - **measure candidates** (smooth, graded weights),
    - **flag candidates** (more binary / threshold-like behaviour).
- **What it establishes:**
  - Narrows Phase 3 down to a small set of **measure-like** and
    **flag-like** columns worth further study.

### Rung 5 — θ-profiles of candidate measures

- **Script:** `src/analyze_phase3_measure_theta_profiles_v1.py`
- **Output:**  
  - `outputs/tables/stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv`
- **What it does:**
  - Samples each candidate measure/flag as a function of θ index.
  - Records simple shape features (e.g. unimodality, variation,
    non-flatness).
- **What it establishes:**
  - Confirms that several candidates are smooth, non-trivial θ-dependent
    profiles (not flat noise) and thus plausible “mechanism weights”.

### Rung 6 — Preferred mechanism candidates

- **Script:** `src/select_phase3_preferred_measures_v1.py`
- **Output:**  
  - `outputs/tables/stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`
- **What it does:**
  - From Rung 5, selects a small set of **preferred** candidates based on:
    - stability,
    - smoothness,
    - interpretability.
- **What it establishes:**
  - Produces a **shortlist of mechanism measures** that could later be
    promoted as “our preferred θ-measure” in a Phase 5+/Stage-2 paper,
    subject to further scrutiny.

*(At this stage, no single column is declared “the” measure; we only
identify a well-behaved candidate set.)*

---

## 3. Joint Mechanism–FRW Analysis

**Path:** `stage2/joint_mech_frw_analysis/`  
**Inputs:**  
- Stage 2 FRW inputs (Phase 4 tables, as above)  
- Stage 2 mech inputs (Phase 3 tables, as above)

**High-level question:**  
> Once we stitch Phase 3 and Phase 4 onto the same θ grid, how tightly
> are the mechanism amplitudes tied to FRW vacuum behaviour?

### Rung 1 — Joint θ-grid construction

- **Script:** `src/build_joint_theta_grid_v1.py`
- **Output:**  
  - `outputs/tables/stage2_joint_theta_grid_v1.csv`
- **What it does:**
  - Loads:
    - FRW shape/viability/LCDM/data masks.
    - Mechanism baseline and binding tables.
  - Enforces **explicit θ-alignment checks** between Phase 3 and Phase 4
    tables, with a numerical tolerance.
  - Builds a joint table with columns including:
    - `theta_index`, `theta`
    - FRW scalars: `E_vac`, `omega_lambda`, `age_Gyr`
    - FRW flags: `in_toy_corridor`, `frw_viable`, `lcdm_like`,
      `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`
    - Mechanism amplitudes: `mech_baseline_*`, `mech_binding_*`.
- **What it establishes:**
  - There is a **coherent θ grid** on which both FRW and mechanism
    quantities can be compared point-by-point.
  - θ alignment is enforced and documented.

### Rung 2 — Joint family summaries

- **Script:** `src/analyze_joint_mech_frw_family_summaries_v1.py`
- **Output:**  
  - `outputs/tables/stage2_joint_mech_frw_rung2_family_summaries_v1.csv`
- **What it does:**
  - Re-defines families on the joint grid, including:
    - `ALL_GRID`
    - `FRW_VIABLE`
    - `LCDM_LIKE`
    - `TOY_CORRIDOR`
    - `CORRIDOR_AND_VIABLE`
    - `CORRIDOR_AND_LCDM`
    - `FRW_VIABLE_AND_DATA_OK` (currently empty)
  - Records `n_theta` and `frac_of_grid` for each.
- **What it establishes:**
  - Confirms that the joint grid preserves the same FRW family sizes and
    relationships seen in the FRW-only analysis.

### Rung 3 — Mechanism–FRW correlations

- **Script:** `src/analyze_joint_mech_frw_correlations_v1.py`
- **Output:**  
  - `outputs/tables/stage2_joint_mech_frw_rung3_correlations_v1.csv`
- **What it does:**
  - Computes Pearson correlations and covariances between:
    - FRW scalars: `E_vac`, `omega_lambda`, `age_Gyr`
    - Mechanism amplitudes: `mech_baseline_A0`, `mech_baseline_A_floor`,
      `mech_baseline_bound`, and the corresponding `mech_binding_*`.
- **What it establishes (internal toy-level fact):**
  - Mechanism amplitudes are **strongly and smoothly tied** to FRW
    vacuum behaviour:
    - high positive correlations between `E_vac` / `omega_lambda` and
      amplitude-like quantities,
    - strong negative correlation between universe age and amplitudes,
      and the opposite sign for “bound” quantities.
  - This shows that, in the toy construction, the mechanism sector and
    FRW sector are **not decoupled**; they share a coherent structure
    over θ.

---

## 4. Status and Promotion Policy

- All Stage 2 results are currently **exploratory**:
  - They live downstream of Phase 3 / Phase 4.
  - They do **not** change or reinterpret locked Phase 0 / Phase 1 claims.
  - They do **not** yet appear in the main Phase 2 / Phase 3 / Phase 4
    papers.

- Promotion process (future):
  1. Identify particularly robust, interpretable diagnostics
     (e.g. corridor fractions, contiguity, selected measure θ-profiles,
     key correlation summaries).
  2. Decide whether to:
     - promote them into a Phase 5 paper (as appendices or figures), or
     - build a dedicated Stage-2-style methods paper.
  3. When promoted, the corresponding rungs and outputs will be cited
     explicitly in the relevant LaTeX source.

Until such promotion is explicitly decided and documented, Stage 2
remains a **lab for stress-testing the machinery and discovering
structure**, not a source of new published claims.


---

## 5. Documentation and repo-audit belt

In addition to the FRW, mech/measure, joint mech–FRW, FRW data-probe, and θ★
diagnostic belts, Stage 2 also includes a documentation and repo-audit belt.
This belt is responsible for:

- inventorying documentation and structural files across the repo,
- flagging broken references, orphaned docs, and open TODO/TBD-style threads,
- proposing small, manually applied documentation rungs (navigation fixes,
  archive labelling, companion-doc links, etc.), and
- keeping an auditable record of these changes.

The primary interface for this belt is:

- `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` – describes the doc-audit CSVs,
  how they are generated, and which manual doc-audit rungs have been applied so
  far (including a dated status section).

The doc/repo-audit belt does not introduce new physical claims and does not
modify Phase 0–5 numerical artifacts. Its role is to keep the documentation and
repository structure aligned with Phase 0 contracts and the actual Phase/Stage
artifacts, so that external auditors can navigate and evaluate the project
without guessing.
