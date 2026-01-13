# Stage 2 Code Audit & Healthcheck (v1, 2026-01-13)

This document records a **point-in-time audit** of the Stage 2 code and endpoints, focusing on:

- whether the current results (FRW corridors, empirical anchor kernels, host FRW cross-checks, mechanism diagnostics) are **consistent with the actual code** in this repo;
- what invariants Stage 2 relies on;
- where the main “foot-guns” and fragilities are for future rungs.

It is **descriptive**, not promotional: it does not upgrade any scientific claims, it just states what the code currently does and how safe it is to use.

For a detailed list of CSV endpoints and column semantics, see:

- `stage2/docs/STAGE2_ENDPOINT_GLOSSARY_v1.md`

---

## 1. Scope of this audit

This audit covers the following Stage 2 belts and scripts as they exist at this commit:

- `stage2/frw_corridor_analysis/`
- `stage2/frw_data_probe_analysis/`
- `stage2/joint_mech_frw_analysis/`
- `stage2/mech_measure_analysis/`
- `stage2/external_frw_host/`

and their interactions with Phase 3 and Phase 4 outputs via:

- `phase3/outputs/tables/…`
- `phase4/outputs/tables/…`
- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

The **Phase 0 contract** and phase-level scope documents remain the gatekeepers of what may be *claimed*. Stage 2 only provides diagnostics and corridor-style structure.

---

## 2. Global invariants and contracts

### 2.1 θ-grid and joins

- All Stage 2 belts operate on a **2048-point θ-grid**.
- Canonical θ coordinates are:

  - `theta_index`: integer 0…2047
  - `theta`: θ value in radians

- **Primary join key** between Stage 2 tables and between Stage 2 and Phase 3/4:

  - preferred: `theta`
  - secondary (when explicitly coded): `theta_index`

The audit confirmed that:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv` is the **central hub** for θ-indexed information,
- all Stage 2 scripts that expect this table use column names that match the glossary.

### 2.2 Mechanism & FRW slots

On the joint grid:

- Mechanism slots (`mech_baseline_*`, `mech_binding_*`) are:

  - present,
  - numerically finite across the grid,
  - consistent between “baseline” and “binding” versions (no accidental reshuffling).

- FRW slots:

  - `E_vac`, `omega_lambda`, `age_Gyr`, and FRW masks (`frw_viable`, `lcdm_like`, `in_toy_corridor`, etc.)
  - are present and **behave as required** by the FRW corridor and data-probe belts (no missing columns or shape mismatches).

### 2.3 Mask semantics

Across Stage 2, the following masks have stable meaning:

- `frw_viable`: FRW background passes the toy viability criteria.
- `in_toy_corridor`: membership in Phase 4’s FRW “toy corridor” family.
- `in_empirical_anchor_box`: membership in the 2D FRW empirical anchor box (Ω_Λ vs age_Gyr).
- `in_host_empirical_anchor_box`: host-side image of the same anchor set.
- `age_consistent_rel_le_20pct`: |Δage| / age_repo ≤ 0.2 w.r.t analytic FRW host.

These meanings were verified against the code and the resulting CSVs, not assumed.

---

## 3. Belt-by-belt healthcheck summary

### 3.1 FRW corridor analysis (`stage2/frw_corridor_analysis`)

Scripts audited: Rung 1–9 (sources, boolean census, families, overlap, contiguity, stride, smoothing, segments, θ★ alignment).

Findings:

- All scripts expect and find:

  - θ-grid columns: `theta_index`, `theta`
  - FRW masks: `frw_viable`, `lcdm_like`, `in_toy_corridor`, `shape_and_viable`, `shape_and_lcdm`

- The **family definitions** (F1…F6, etc.) in the code match the descriptions in the Stage 2 docs:

  - F1 ≈ FRW viable,
  - F2 ≈ ΛCDM-like,
  - F3 ≈ toy corridor,
  - etc.

- Contiguity, stride robustness, and smoothing rungs all:

  - operate on boolean masks,
  - preserve the 2048-row structure,
  - produce segment summaries that match the previously reported corridor segments.

**Status:** ✅ Healthy and internally consistent. Results used downstream (e.g. corridor membership, segment structure) are supported by the current code.

---

### 3.2 FRW data-probe & empirical anchor (`stage2/frw_data_probe_analysis`)

Key endpoints / scripts:

- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv` (source)
- `analyze_frw_data_probes_v1.py`
- `analyze_frw_empirical_anchor_v1.py`
- `config/empirical_anchor_box_v1.json`

Findings:

- `analyze_frw_data_probes_v1.py` correctly reads the Phase 4 data-probe mask and produces:

  - boolean column statistics consistent with log output:
    - `has_matter_era` and `smooth_H2` seen as always true,
    - `data_ok` identified as always false in this rung.

- `analyze_frw_empirical_anchor_v1.py`:

  - reads the FRW “shape probe” table,
  - applies the **empirical anchor box** defined in JSON,
  - writes `stage2_frw_empirical_anchor_mask_v1.csv` with:

    - `theta`, `omega_lambda`, `age_Gyr`, `frw_viable`,
    - `in_empirical_anchor_box` mask.

- The count `in_anchor = 18` reported by the script matches:

  - the size of the anchor kernel seen in joint mech–FRW analysis,
  - the profiles and sensitivity results.

**Status:** ✅ Healthy. The 18-point FRW empirical anchor subset is a **real** output of the current code and config, not an artefact of mismatched joins.

---

### 3.3 Joint mech–FRW analysis (`stage2/joint_mech_frw_analysis`)

Key scripts audited:

- `build_joint_theta_grid_v1.py` (implied from outputs)
- `analyze_joint_mech_frw_anchor_intersections_v1.py`
- `analyze_joint_mech_frw_anchor_kernel_v1.py`
- `analyze_joint_mech_frw_anchor_profiles_v1.py`
- `analyze_joint_mech_frw_anchor_sensitivity_v1.py`
- `analyze_joint_mech_frw_anchor_mech_contrast_v1.py`
- `analyze_joint_mech_frw_host_corridor_v1.py`
- `analyze_joint_mech_frw_host_anchor_intersections_v1.py`

Key invariants confirmed:

- `stage2_joint_theta_grid_v1.csv` contains exactly the columns enumerated in the endpoint glossary.
- All “anchor” and “host anchor” scripts now:

  - join consistently (either on `theta` or `theta_index` as stated),
  - find 2048 rows where expected,
  - produce set sizes that match the run logs already in the repo.

Specific numeric checks (from current tables):

- `EMPIRICAL_ANCHOR` has **18 θ points**, with:

  - Ω_Λ ≈ 0.664–0.717,
  - age_Gyr ≈ 13.42–13.58,
  - fully contained inside FRW viable & toy corridor.

- `CORRIDOR_AND_VIABLE_AND_ANCHOR` has **18 θ points** (same kernel):

  - contiguity analysis shows **two 9-point segments** in θ.

- Sensitivity rung confirms:

  - narrower box (`scale=0.5`) → 8 points;
  - baseline box (`scale=1.0`) → 18 points;
  - wider box (`scale=1.5`) → 26 points (24 inside both corridor and FRW viability).

- Mechanism contrast & gradients:

  - contrasting stats between:
    - FRW_VIABLE,
    - CORRIDOR_AND_VIABLE,
    - CORRIDOR_AND_VIABLE_AND_ANCHOR
  - match the CSV numbers currently present in the repo.

**Status:** ✅ Healthy and **aligned with documented results**. No code/CSV mismatch has been found that would invalidate the reported 18-point kernel or its mechanism signatures.

---

### 3.4 Mechanism measure analysis (`stage2/mech_measure_analysis`)

Key scripts audited:

- `inventory_phase3_tables_v1.py`
- `analyze_mech_theta_gradients_v1.py`

Findings:

- Inventory rung correctly scans `phase3/outputs/tables`, classifying:

  - baseline/binding scan tables,
  - diagnostics JSONs.

- Gradient analysis rung:

  - reads the joint grid + anchor mask,
  - computes finite-difference gradients in θ for mechanism columns,
  - outputs `stage2_mech_rung7_theta_gradients_v1.csv` with:

    - global stats (`ALL_GRID`),
    - FRW_VIABLE / TOY_CORRIDOR,
    - CORRIDOR_AND_VIABLE,
    - CORRIDOR_AND_VIABLE_AND_ANCHOR.

- The reported gradient ranges and 95th percentiles match what is in that CSV.

**Status:** ✅ Healthy. Mechanism gradient numbers used in narrative are consistent with current code.

---

### 3.5 External FRW host (`stage2/external_frw_host`)

Key scripts audited:

- `compute_analytic_frw_ages_v1.py`
- `analyze_external_frw_age_contrast_v1.py`
- `flag_age_consistent_subset_v1.py`
- `analyze_external_frw_host_anchor_v1.py`

Findings:

- `compute_analytic_frw_ages_v1.py`:

  - reads the joint grid,
  - computes analytic FRW host ages with a global calibration factor,
  - writes `stage2_external_frw_rung1_age_crosscheck_v1.csv`.

- `analyze_external_frw_age_contrast_v1.py`:

  - produces per-set age contrasts (ALL_GRID, FRW_VIABLE, CORRIDOR_AND_VIABLE, CORRIDOR_AND_VIABLE_AND_ANCHOR),
  - the summary values in the CSV match the log:

    - host ages significantly smaller than toy ages in corridor+anchor region.

- `flag_age_consistent_subset_v1.py`:

  - defines a **20% relative error** criterion,
  - identifies 778 θ points as age-consistent, **none** of which lie in the corridor+anchor intersection.
  - This “no intersection” result is reflected in the corresponding CSV and logs.

- `analyze_external_frw_host_anchor_v1.py`:

  - uses the FRW empirical anchor mask to infer a **host-side anchor box**,
  - constructs `stage2_external_frw_host_anchor_mask_v1.csv`,
  - finds 18 θ points in this box, consistent with the original FRW anchor set.

**Status:** ✅ Healthy. Host diagnostics confirm a strong mismatch between toy FRW ages and analytic FRW ages in the anchor corridor; this is a robust property of the current toy model and mapping, not a bug.

---

## 4. Known fragilities and “foot-guns”

This section records patterns that are **not bugs right now**, but could cause subtle breakage if the repo structure changes.

### 4.1 Path arithmetic using `.parents[...]`

Several Stage 2 scripts derive `REPO_ROOT` using expressions like:

```python
repo_root = Path(__file__).resolve().parents[3]
```

This:

- currently works with the existing directory depth,
- will break silently if Stage 2 files are moved deeper or shallower.

**Mitigation:**

- If the repo layout changes, update these `parents[...]` indices in all Stage 2 scripts.
- Long-term: consider a small shared helper (e.g. `stage2/common/path_helpers.py`) to centralize this logic.

### 4.2 θ joins: `theta` vs `theta_index`

Some scripts join on `theta`, others on `theta_index`. Right now:

- both coordinates are consistent across tables,
- no mismatches were seen in this audit.

**Mitigation:**

- When adding new Stage 2 scripts, be explicit in comments about:

  - which key is used (`theta` vs `theta_index`),
  - why (e.g. robustness to re-gridding vs exact alignment with Phase 4 tables).

- Avoid mixing the two keys in a single script unless there is a clear reason.

### 4.3 Empirical anchor box config

The FRW empirical anchor is controlled by:

- `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`

Changing this file:

- changes the definition and size of the 2D anchor box,
- changes the 18-point kernel set and all downstream anchor statistics.

**Mitigation:**

- Treat changes to this config as **rung-level operations** with:

  - explicit documentation in Stage 2 docs,
  - a corresponding PROGRESS_LOG entry explaining why the box moved.

### 4.4 Host calibration & “age consistency” definition

The analytic FRW ages are calibrated via a single global scale factor (Gyr / dimensionless age). The age-consistency mask uses:

- a hard 20% tolerance,
- the ratio `(age_host - age_repo) / age_repo`.

These are **toy design choices**, not unique truths.

**Mitigation:**

- If calibration or tolerance are changed, this must be:

  - reflected in doc (host belt design),
  - and any comparisons to current results must clearly state which calibration/tolerance they refer to.

---

## 5. Impact on current results

Given this audit, the following high-level statements about Stage 2 outputs are **certified as matched to the current code** (diagnostic level only):

1. The **18-point FRW empirical anchor kernel** (corridor ∧ viable ∧ data-box) is a genuine feature of the current toy FRW mapping and empirical box, not a glitch.
2. The mechanism measure and gradient statistics reported for:

   - FRW_VIABLE,
   - CORRIDOR_AND_VIABLE,
   - CORRIDOR_AND_VIABLE_AND_ANCHOR

   come directly from the current joint grid and are internally consistent.

3. The analytic FRW host reveals a **strong mismatch** in ages for the corridor+anchor subset under the current mapping and calibration:

   - none of the 18 anchor-kernel θ points fall inside the 20% age-consistency region.

4. The Stage 2 scripts form a **coherent diagnostic belt** on top of Phase 3 and Phase 4:

   - no hidden path errors,
   - no silent column mismatches,
   - no accidental reshaping of the θ-grid were found in this audit.

All of the above remain **sub-claims inside Stage 2 diagnostics**; promotion into Phase 4/5 narrative must go through the existing Phase 0 governance gates.

---

## 6. Maintenance guidelines

When extending Stage 2:

1. **Add endpoints to the glossary**

   - Any new CSV or column name must be added to  
     `stage2/docs/STAGE2_ENDPOINT_GLOSSARY_v1.md`.

2. **Document new belts**

   - New rungs / belts should have a short design doc in `stage2/docs/…` stating:
     - scope,
     - inputs,
     - outputs,
     - allowed claim shapes.

3. **Add smoke-test commands**

   - For new belts, consider adding a short “smoke test” script or documented CLI sequence that:

     - regenerates key outputs, and
     - prints a small set of sanity stats (row counts, fractions, etc).

4. **Keep Stage 2 diagnostic**

   - Stage 2 should remain a **diagnostic lab** downstream of Phases 3 and 4, not a place where core claims are silently updated.
