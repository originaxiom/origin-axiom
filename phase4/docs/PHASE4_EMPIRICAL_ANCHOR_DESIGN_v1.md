# Phase 4 – Empirical Anchor Design (Background-Only Box)

> **Status:** Design / diagnostic only – non-binding, no direct data claims.  
> This file defines how Phase 4 exposes a *background-only* “empirical anchor”
> to Stage 2. All quantitative work lives in Stage 2; Phase 4 only specifies
> which FRW columns are eligible and what claim shapes are allowed.

---

## 1. Scope and non-claims

**Scope.**

- Define a minimal “empirical anchor” on the Phase 4 FRW toy grid using:
  - an effective vacuum parameter \\\( \omega_\Lambda \\\) and
  - the FRW background age \\\( t_0 \\\) in Gyr.
- Expose this anchor to Stage 2 as a *Boolean mask* on the existing 2048-point
  \\\( \theta \\\)-grid, with no changes to the Phase 4 numerical pipeline.

**Non-claims.**

- The anchor is **not** a full cosmological fit (no Planck likelihoods, no BAO,
  no SN, no perturbation observables).
- The anchor is **not** a proof that any \\\( \theta \\\)-region reproduces
  real-universe parameters; it is a *background-level box cut* only.
- No Phase 4 or Phase 5 claims may depend on this anchor until:
  - the FRW toy implementation is cross-checked and calibrated against an
    external FRW host, and
  - a separate promotion gate explicitly authorises the use of anchor results.

---

## 2. Inputs and FRW interface

Phase 4 provides the following FRW table as the primary interface:

- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`

Key columns used by the anchor:

- `theta`  
  - The \\\( \theta \\\)-coordinate used throughout Phase 3/4/Stage 2.
- `E_vac`  
  - Mechanism-induced vacuum scale as used by the FRW toy.
- `omega_lambda`  
  - Effective dark-energy density fraction used by the FRW toy FRW integrator.
- `age_Gyr`  
  - Background age of the universe in Gyr as computed by the FRW toy integrator.

Additional Boolean columns (not directly used for the anchor box, but relevant
for intersections):

- `frw_viable` (in `phase4_F1_frw_viability_mask.csv`)  
  - “FRW background is internally sane” (Big Bang, matter era, late acceleration, etc.).
- `in_toy_corridor` (or equivalent)  
  - Toy \\\( \theta \\\)-corridor mask defined by Phase 4 / Stage 2.

All anchor work is downstream of these columns; Phase 4 does **not** alter the
FRW computations for the anchor.

---

## 3. Anchor box definition (Phase 4 → Stage 2 contract)

The concrete numerical definition of the anchor lives in Stage 2, in a small
JSON config:

- `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`

Semantics:

- The JSON file specifies a central value and half-width for:
  - `omega_lambda` (effective dark-energy fraction),
  - `age_Gyr` (background age in Gyr).
- Stage 2 then defines a Boolean mask on the FRW grid:

  \\\[
  \texttt{in\_empirical\_anchor\_box}(\theta) = 1
  \\\]

  if and only if the Phase 4 values \\\( (\omega_\Lambda(\theta), t_0(\theta)) \\\)
  lie inside the configured rectangular box.

Implementation (Stage 2 side, documented here for clarity):

- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`
  - Reads the Phase 4 FRW shape table.
  - Applies the box cut from `empirical_anchor_box_v1.json`.
  - Writes:

    - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`

  - This table exposes:
    - `theta`,
    - `omega_lambda`,
    - `age_Gyr`,
    - `in_empirical_anchor_box` (Boolean).

Phase 4’s responsibility is purely:

- to keep the FRW toy outputs stable, and
- to document which columns are used and how.

---

## 4. Allowed claim shapes

Within this design, the **only** allowed claim shapes (even at Stage 2) are:

1. **Occupancy / overlap statements**

   - Examples:
     - “On the 2048-point \\\( \theta \\\)-grid, the empirical anchor box
       selects 18 points (≈ 0.9% of the grid).”
     - “Every anchor point lies inside the FRW-viable band and inside the
       Phase 4 toy corridor mask.”

   - These are *set-theoretic* statements about intersections of:
     - FRW viability,
     - toy corridor,
     - and the anchor box.

2. **Kernel structure statements**

   - Examples:
     - “The anchor points form a small number of contiguous \\\( \theta \\\)-segments,
       not isolated singletons.”
     - “Within the anchor kernel, FRW quantities and mechanism amplitudes vary
       smoothly and occupy a narrow interval compared to the full corridor.”

3. **Sensitivity / robustness statements**

   - Examples:
     - “Scaling the box half-widths by factors 0.5, 1.0, 1.5 yields
       (8, 18, 26) points in the anchor, all still within the FRW-viable band.”

These claims are strictly *diagnostic* and must remain in Stage 2 unless and
until a promotion gate authorises them for Phase 4/5 text.

---

## 5. Forbidden claim shapes (until promotion)

The following claims are **forbidden** under this design, unless a future,
explicit promotion gate says otherwise:

- “The axiom predicts the observed value of \\\( \Omega_\Lambda \\\) or \\\( H_0 \\\).”
- “The empirical anchor shows that the axiom is consistent with Planck data.”
- “The anchor kernel corresponds to the actual Universe’s parameters.”
- Any statement that treats the current FRW toy ages as calibrated to real data.

At this stage, the anchor is **only**:

- a *toy background box* in \\\( (\omega_\Lambda, \text{age\_Gyr}) \\\)-space,
- used to define small, structured subsets of the \\\( \theta \\\)-grid for
  Stage 2 diagnostics.

---

## 6. Relationship to external FRW host

A separate Stage 2 belt (`stage2/external_frw_host/`) compares the Phase 4 toy
ages to an analytic flat FRW host model and finds sizeable discrepancies
(typically \\\( \sim 20\% \\\) on the FRW-viable band and larger on the corridor).

Phase 4 takes the following stance:

- Until the FRW toy vs host mismatch is understood and addressed, the
  empirical anchor remains a **toy diagnostic only**.
- No publication-grade claims will rely on its numerical values; at most,
  the anchor may be used to:
  - illustrate how small kernels can be carved out in \\\( \theta \\\)-space, and
  - motivate future, better-calibrated FRW implementations.

Any future promotion of the anchor to a Phase 4/5 figure or narrative element
requires:

1. A documented FRW toy vs host reconciliation, and  
2. A dedicated promotion gate (e.g. `docs/FRW_ANCHOR_PROMOTION_GATE_v1.md`).

