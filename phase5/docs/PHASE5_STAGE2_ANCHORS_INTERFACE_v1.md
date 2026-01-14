# Phase 5 – Stage 2 anchors and corridors interface (v1)

**Scope.** This note is a bridge between Stage 2 diagnostics and the future Phase 5 interface narrative.  
It does **not** introduce new claims; it organises and interprets what Stage 2 already computed, so Phase 5 can:
- talk about the θ–landscape in a disciplined way, and
- know which Stage 2 artifacts to lean on (and which not to).

It should be read together with:
- `stage2/docs/STAGE2_RUNBOOK_AND_INTERPRETATION_v1.md`
- `stage2/docs/STAGE2_CODE_AUDIT_AND_HEALTHCHECK_v1.md`
- `stage2/docs/STAGE2_ENDPOINTS_GLOSSARY_v1.md`
- `phase4/docs/PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md`
- `phase4/docs/PHASE4_FRW_TOY_EQUATIONS_v1.md`
- `phase4/docs/PHASE4_FRW_TOY_HEALTHCHECK_v1.md`
- `phase4/docs/PHASE4_FRW_TOY_HOST_ALIGNMENT_DESIGN_v1.md`
- `phase4/docs/PHASE4_FRW_TOY_TIGHTENING_DECISION_v1.md`

---

## 1. Objects Phase 5 can safely treat as “inputs”

This section lists the main Stage 2 outputs that Phase 5 may treat as *given diagnostics* on the current θ–landscape. All of these are reproducible from the repo.

### 1.1 Joint θ–grid

- Table:  
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- Built by:  
  - `stage2/joint_mech_frw_analysis/src/build_joint_theta_grid_v1.py`
- Key columns (see `STAGE2_ENDPOINTS_GLOSSARY_v1.md` for full list):
  - `theta_index`, `theta`
  - Mechanism outputs:
    - `E_vac`
    - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`
    - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`
  - FRW toy outputs:
    - `omega_lambda`, `age_Gyr`
    - `frw_viable`, `lcdm_like`, `shape_and_viable`, `shape_and_lcdm`
  - Corridor / data flags:
    - `in_toy_corridor` (Phase 4 toy corridor flag)
    - `in_empirical_anchor_box` (FRW toy empirical anchor)
    - age-consistency / host flags added downstream in external-host tables.

For Phase 5, this is the **main θ–axis data frame**.

---

## 2. Stage 2 FRW & anchor diagnostics – what they actually say

This section compresses the Stage 2 findings that are relevant for Phase 5. Numerical values are for the current repo state and can be regenerated.

### 2.1 FRW corridor structure (toy-only)

From the FRW corridor belt:
- Tables:
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`
- Interpretation:
  - There exists a **toy FRW corridor**:
    - fraction of grid in `TOY_CORRIDOR`: ~0.58 (≈ 1186 / 2048).
  - FRW viability:
    - `FRW_VIABLE` fraction: ~0.50 (≈ 1016 / 2048).
  - Intersections:
    - `CORRIDOR_AND_VIABLE`: ≈ 154 / 2048 (≈ 7.5% of the grid).
  - This corridor is defined purely by **internal FRW toy masks**, not by external data.

Phase 5 can say:
- “There is a non-trivial toy FRW corridor where the mechanism and FRW toy behave well.”
- But **must not** treat this as empirically anchored yet.

### 2.2 FRW toy empirical anchor (background box)

Defined in `phase4/docs/PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md` and implemented via:

- Stage 2 tables:
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
- What the current anchor box encodes (approximate summary):
  - A small **background box** in:
    - `omega_lambda` and `age_Gyr` (FRW toy age)
  - Chosen to be roughly consistent with a Λ-like vacuum fraction and an age near the observed Universe.
- Key Stage 2 findings:
  - `EMPIRICAL_ANCHOR`:
    - n ≈ 18 / 2048 ≈ 0.9% of the grid.
  - Intersections:
    - `FRW_VIABLE_AND_ANCHOR`: same 18 points.
    - `CORRIDOR_AND_ANCHOR`: same 18 points.
    - `CORRIDOR_AND_VIABLE_AND_ANCHOR`: same 18 points.
  - These 18 θ–points break into **two disjoint contiguous θ–segments** (size 9 each).
    - From `stage2_joint_mech_frw_anchor_kernel_v1.csv`.
    - Both segments lie **away from θ★**, with min |θ–θ★| ~ O(1).

Mechanism behavior in this kernel:
- From `stage2_joint_mech_frw_anchor_profiles_v1.csv` and `stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`:
  - Mechanism amplitudes (`mech_baseline_A0`, `mech_binding_A0`, etc.) in the 18-point kernel:
    - Cluster tightly around ~0.046 with standard deviation ~2.7×10⁻⁴.
  - This is *distinct* from the broader FRW-viable band and from the full toy corridor.

**Phase 5 compatible takeaway:**

> There exists a very small θ–kernel (18/2048 points) where:
> - the FRW toy is viable,
> - the internal FRW empirical box is satisfied,
> - and the mechanism amplitudes cluster tightly.
>
> This kernel does **not** contain θ★ but provides a concrete empirical-like “box” our toy passes.

Phase 5 can treat this as a **worked example** of:
- what it means for the axiom + mechanism + FRW toy to survive a simple empirical background filter,  
without claiming that it “matches the real Universe”.

### 2.3 External FRW host age and host-age anchor

External host belt tables:

- Age cross-check and background bridge:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv`
- Age contrast summary:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`
- Age consistency mask (relative error ≤ 20%):
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`
- Host age window & anchor:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung4_age_window_summary_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_summary_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`
- Intersections:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_corridor_summary_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`

Compressed interpretation:

1. **Host vs toy age (FRW-viable band).**
   - On `FRW_VIABLE`:
     - Mean |age_host − age_toy| ~ few Gyr.
     - Relative difference ~ 0.18 (≈ 18%) on average.
   - On the **toy corridor** ∧ viable:
     - Differences are larger (toy ages can be much higher than host ages).
2. **Host age anchor window.**
   - A host age window around the observed age:
     - `age_Gyr_host ∈ [13.3, 14.3]`.
   - Host-age anchor:
     - n ≈ 34 / 2048 ≈ 1.7% of the grid.
     - All host-age anchor points lie inside `frw_viable`.
   - Mechanism at host-age anchor:
     - Mechanism amplitudes again cluster near a narrow value (~0.051 with small spread).
3. **Corridor overlap with host-age anchor.**
   - From `stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`:
     - `CORRIDOR_AND_HOST_AGE_ANCHOR`: 0 points.
     - `CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR`: 0 points.
   - So:
     - The Phase 4 toy corridor currently **does not intersect** the host-age anchor band at all.

**Phase 5 compatible takeaway:**

> Under a simple flat-FRW host model, there is a narrow θ–band whose ages match the observed age window (host-age anchor), with well-behaved mechanism amplitudes, but this band does **not** overlap the current toy FRW corridor.

This is **not** automatically a “disproof”, but it is a **tension** that Phase 5 can:
- highlight,
- and use as a case study of how the axiom might fail or survive in different background choices.

---

## 3. How Phase 5 can use these results

Phase 5 is meant to be an **interface / narrative phase**, not a new mechanism or a full data pipeline. Within that remit, it can use Stage 2 as follows.

### 3.1 Allowed narrative patterns

Phase 5 can say things of the form:

1. **Landscape summaries.**
   - “On our θ–grid, the following subsets appear:
     - FRW-viable: ~50% of points,
     - toy corridor: ~58% of points,
     - their intersection: ~7.5% of points,
     - toy empirical anchor kernel: 18 points (~0.9%),
     - host-age anchor (external FRW model): 34 points (~1.7%).”
2. **Overlap / non-overlap statements.**
   - “The empirical toy anchor kernel lies fully inside the toy corridor and FRW-viable sets but does not contain θ★.”
   - “The host-age anchor band does not intersect the current toy corridor at all.”
3. **Mechanism-profile comparisons.**
   - “In the empirical anchor kernel, mechanism amplitudes cluster in a narrow band (~0.046–0.047), in contrast to the broader FRW-viable set.”
   - “In the host-age anchor band, mechanism amplitudes cluster near ~0.051, again with small spread.”

All of these must be clearly labeled as:
- statements **about the current implementation** of:
  - the axiom + mechanism + FRW toy + simple FRW host model,
- **not** universal theorems about cosmology.

### 3.2 Explicit non-claims

Phase 5 must *not* say:

- “We have measured the real Universe’s parameters from first principles.”
- “The axiom predicts the observed value of Λ or the exact age of the Universe.”
- “The toy corridor (or any anchor band) is uniquely selected by data.”

Instead, Phase 5 should frame this as:

> “Given this axiom + mechanism + toy FRW implementation, and a simple FRW host model, we can *mechanically* map out which θ–regions survive different families of filters (FRW viability, toy-corridor, empirical-box, host-age window).”

That is already nontrivial.

---

## 4. Hooks for later, more ambitious work

If later phases or Stage II want to move towards **real cosmology pipelines** (CLASS, CCL, Cobaya, etc.), this interface doc already points to:

- The **θ → {E_vac, omega_lambda, age_Gyr, …}** map in the joint grid.
- The existing **anchor concepts**:
  - FRW toy empirical anchor (background box).
  - External FRW host-age anchor.
- The logic of:
  - corridors,
  - anchors,
  - intersections,
  - and mechanism profiles.

Future work can then:

- Replace the simple analytic host with a proper Boltzmann / CCL pipeline.
- Generalise the anchor from (ΩΛ, t₀)-box to:
  - a set of weak data-consistency conditions,
  - still under strong Phase 0 governance.

---

## 5. Summary

For Phase 5, the main message of Stage 2 is:

- We now have a **mechanical map** of how:
  - the axiom and mechanism,
  - the FRW toy background,
  - and a simple FRW host model,
- jointly carve up the θ–axis into:
  - broad corridors,
  - small anchor kernels,
  - and regions of tension.

Phase 5 can use this as a **worked, reproducible case study** of what “non-cancelling twist meets cosmology” looks like *in practice*, without over-claiming connection to the actual Universe.

