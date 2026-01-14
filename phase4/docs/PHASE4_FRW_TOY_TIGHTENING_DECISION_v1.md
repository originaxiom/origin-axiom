# Phase 4 – FRW toy tightening decision (v1)

**Scope.** This note records the decision space for “tightening” the Phase 4 FRW toy background in light of the Stage 2 FRW host age diagnostics. It is a design / decision card, not a claims register.

It should:
- Keep Phase 0 discipline front and center.
- Make explicit what we are and are not doing to the FRW toy.
- Provide a clear hook for any future re-tuning rung.

---

## 1. Inputs and current situation

### 1.1 FRW toy backbone (Phase 4)

The current FRW toy:

- Lives primarily in Phase 4 code and tables:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
  - FRW equations and diagnostics described in:
    - `phase4/docs/PHASE4_FRW_TOY_EQUATIONS_v1.md`
    - `phase4/docs/PHASE4_FRW_TOY_HEALTHCHECK_v1.md`
    - `phase4/docs/PHASE4_FRW_TOY_HOST_ALIGNMENT_DESIGN_v1.md`
- Provides, on a fixed θ-grid:
  - `theta`
  - `omega_lambda` (toy vacuum fraction)
  - `age_Gyr` (toy FRW age)
  - `frw_viable` and related masks

The toy was originally designed as an **internal FRW backdrop**, not as a precision cosmology engine.

### 1.2 External FRW host diagnostics (Stage 2)

Stage 2 now adds:

- **Analytic FRW host age** at the same `omega_lambda`:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
  - Built by `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
- **Background bridge:**
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv`
  - Built by `build_frw_background_bridge_v1.py`
- **Host age anchor:**
  - Mask + summary:
    - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
    - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_summary_v1.csv`
  - Profiles:
    - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`
  - Intersections:
    - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`
- Status summary:
  - `stage2/docs/STAGE2_FRW_HOST_AGE_ANCHOR_STATUS_v1.md`

### 1.3 What the diagnostics actually showed (compressed)

From `STAGE2_FRW_HOST_AGE_ANCHOR_STATUS_v1.md`:

- The **host age anchor** (analytic age in [13.3, 14.3] Gyr):
  - Exists and is non-empty: 34 / 2048 θ-points (~1.66% of the grid).
  - Lies entirely inside `frw_viable` for the toy.
- At those θ:
  - Host age ≈ 13.6 Gyr.
  - Toy FRW age ≈ 12.6 Gyr.
  - → ~1 Gyr systematic offset between toy and host.
- Mechanism amplitudes in that band cluster around ≈ 0.0513 with tiny spread.
- **No overlap** between:
  - the current Phase 4 θ-corridor and
  - the host age anchor band.

So we have a clean, reproducible fact:

> The current Phase 4 FRW toy corridor is a **toy corridor**, not yet host-age anchored, and the toy ages are systematically offset from a simple FRW host model in the host age-anchor band.

---

## 2. Decision space

We explicitly frame two main options.

### Option A – Keep the FRW toy as-is, host as external diagnostic

**Description**

- Do **not** modify the Phase 4 FRW toy equations, mappings, or age normalization.
- Treat the analytic FRW host and age anchors as:
  - a **Stage 2 diagnostic bench**,
  - not as a source of constraints baked back into the Phase 4 toy.
- Preserve the current Phase 4 FRW toy as an internal, self-consistent mechanism-testing environment.

**Pros**

- Minimal risk to Phase 4 stability:
  - No retroactive changes to existing FRW toy behavior.
  - All current Phase 4 / Stage 2 results remain literally reproducible.
- Clean governance:
  - Phase 4 stays “toy-first,” Stage 2 hosts remain clearly external.
- Good for historical clarity:
  - We keep a sharp distinction between:
    - internal FRW toy evolution, and
    - external host-based diagnostics.

**Cons**

- The θ-corridor continues to be **purely toy-defined**:
  - It is not age-anchored.
  - We cannot yet claim any “empirically age-consistent corridor” even in a very weak sense.
- Any future move towards real data contact must:
  - either re-interpret the corridor,
  - or build a new corridor on top of the host-anchor sets.

### Option B – Mildly re-tune the FRW toy toward host age alignment

**Description**

- Introduce a controlled adjustment in the Phase 4 FRW toy so that:
  - in some chosen calibration band (e.g. in or near the host age-anchor region),
  - the toy FRW age better tracks the analytic FRW host age.
- Examples of allowed adjustments (to be designed in a separate rung):
  - A single global scaling of the FRW time variable.
  - A refined mapping from mechanism output → `omega_lambda`.
  - A small shift or rescaling of the age integral, documented and justified.
- Any such adjustment would be:
  - fully documented in:
    - `PHASE4_FRW_TOY_EQUATIONS_v1.md`
    - `PHASE4_FRW_TOY_HOST_ALIGNMENT_DESIGN_v1.md`
  - validated by new Stage 2 checks:
    - updated age cross-check,
    - updated host age-anchor analysis.

**Pros**

- Moves the FRW toy closer to a standard FRW background:
  - especially near the host age-anchor band.
- Makes it easier to later define:
  - a corridor that is both toy-viable **and** approximately age-anchored.
- Reduces the gap between “internal toy” and “external host,” which may simplify future Stage II work.

**Cons**

- Introduces new moving parts into Phase 4:
  - any mistake in calibration could contaminate both toy diagnostics and host comparisons.
- Requires a compact but nontrivial derivation:
  - to justify the chosen mapping / scaling and its range of validity.
- Risks blurring the conceptual line between:
  - “toy as a sandbox”
  - and “toy as a surrogate for real cosmology,”
  - which must be tightly policed by Phase 0 rules.

---

## 3. Governance constraints for any re-tuning

If Option B is ever pursued, the following conditions must be met:

1. **Separate rung + design doc.**
   - Introduce a dedicated Phase 4 rung:
     - e.g. “Rung F4.T (Toy FRW host-alignment calibration)”.
   - Create a specific design note:
     - `phase4/docs/PHASE4_FRW_TOY_HOST_ALIGNMENT_CALIBRATION_v1.md`
     - with:
       - exact equations,
       - calibration band,
       - intended scope and limitations.

2. **Stage 2 verification belt.**
   - Extend or add Stage 2 scripts to:
     - recompute age cross-checks,
     - recompute host age-anchor masks and intersections,
     - compare pre- and post-calibration behavior.

3. **No retroactive claims.**
   - Any claims or narratives based on the pre-tuning toy remain:
     - historically tied to the pre-tuning code,
     - not silently upgraded.
   - New claims must explicitly reference the calibrated version and its gate.

4. **Explicit statement of what is *not* being done.**
   - No full data likelihoods (CMB, BAO, SN) are introduced by this calibration step.
   - The calibration targets background ages only, not the full observable zoo.

---

## 4. Interim decision (v1)

For the **current repo state** and Stage 2 belt:

> **Decision v1:**  
> We adopt **Option A** as the default stance.
>
> - The Phase 4 FRW toy remains **unchanged**.
> - The analytic FRW host and host age anchors are treated as:
>   - external diagnostic benches,
>   - places where we measure how the toy behaves relative to a simple host model.
> - The θ-corridor defined so far is explicitly a **toy FRW corridor**, not an age-anchored corridor.

This decision is:

- **Binding for Phase 4 v1**:
  - No FRW toy equations will be modified without a dedicated calibration rung.
- **Open to future revision**:
  - If, later on, we decide that a mild calibration is needed for clearer empirical contact, we will:
    - add the calibration design doc,
    - add a dedicated rung,
    - and re-run all Stage 2 FRW host diagnostics.

---

## 5. Hooks for future work

If/when we revisit this decision, we already know where to plug in:

- Phase 4 code / docs:
  - `PHASE4_FRW_TOY_EQUATIONS_v1.md`
  - `PHASE4_FRW_TOY_HEALTHCHECK_v1.md`
  - `PHASE4_FRW_TOY_HOST_ALIGNMENT_DESIGN_v1.md`
  - a potential new calibration note:
    - `PHASE4_FRW_TOY_HOST_ALIGNMENT_CALIBRATION_v1.md`
- Stage 2 belts:
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  - `stage2/external_frw_host/src/build_frw_background_bridge_v1.py`
  - `stage2/external_frw_host/src/flag_external_frw_host_age_anchor_v1.py`
  - `stage2/external_frw_host/src/analyze_external_frw_host_age_anchor_profiles_v1.py`
  - joint analysis in:
    - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_age_anchor_intersections_v1.py`

Until such a calibration rung is explicitly declared, **Option A** stands.

