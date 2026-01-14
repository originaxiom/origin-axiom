# Phase 4 – FRW toy host-alignment design

This document describes how the **Phase 4 FRW toy** interacts with various **host layers** without violating the Stage I / Phase 0 contract. It focuses on:

- how FRW-style “toy backgrounds” are constructed over the θ-grid,
- how empirical anchor information and external FRW / ΛCDM hosts are allowed to touch those toys,
- and what is **explicitly out of scope** in Phase 4 (no fitting, no extra cosmology claims).

The goal is to give a clear, reproducible design that later papers and dashboards can reference without ambiguity.

---

## 1. Objects in play

We distinguish four classes of objects:

1. **θ-grid and mechanism bundle (Phase 3 outputs)**

   - The θ-grid and mechanism measures (`mech_baseline_A0`, `mech_binding_A`, corridors, etc.) are taken as **given** from Phase 3.
   - They are not re-fitted or reinterpreted here; Phase 4 treats them as an input “field” over θ.

2. **FRW toy background (Phase 4 internal)**

   - A set of FRW-like quantities defined on the θ-grid:
     - `Omega_lambda_repo(theta)` and derived `Omega_m_repo(theta)` (under simple flatness assumptions),
     - `age_Gyr_repo(theta)` as computed by the Phase 4 FRW toy integrator.
   - These are **toy constructs**, used to:
     - define FRW-viable subsets of θ,
     - inspect qualitative FRW behaviour (e.g. age vs `Omega_lambda`),
     - and build internal masks (FRW-viable, toy corridors, etc.).

3. **Empirical anchor boxes (Phase 4 / Stage 2)**

   - Pre-declared “boxes” in FRW-parameter space that stand in for **observationally-inspired** targets,
     - e.g. an `Omega_lambda` range and an `age_Gyr` window around a Universe-like age.
   - In Stage I these are treated as **synthetic targets**, not as live data-fits.
   - They induce masks such as:
     - `in_empirical_anchor_box` on the θ-grid,
     - and later host-age anchor masks.

4. **External FRW / ΛCDM hosts (Stage 2 overlays)**

   - Separate FRW/ΛCDM background computations that live under `stage2/`:
     - `stage2/external_frw_host/` – analytic FRW age integrator with fixed cosmological parameters,
     - `stage2/external_cosmo_host/` – a simple ΛCDM parameter grid and age computation.
   - These are **diagnostic overlays**:
     - they do not feed back into the mechanism,
     - they do not produce new claims,
     - they only check how the Phase 4 FRW toy and masks behave when seen from “outside”.

---

## 2. FRW toy construction over θ

### 2.1 Inputs from Phase 3

Phase 3 exports a joint grid (via Stage 2) with columns such as:

- `theta_index`, `theta`,
- `omega_lambda` (toy FRW cosmological constant proxy),
- mechanism columns:
  - `mech_baseline_A0`,
  - `mech_baseline_A_floor`,
  - `mech_binding_A0`,
  - `mech_binding_A`,
  - and their associated bound flags,
- masks:
  - `frw_viable`,
  - `in_toy_corridor`,
  - `in_empirical_anchor_box` (Phase 4 / Stage 2 anchor).

The **design requirement** is that Phase 4:

- does *not* re-define θ,
- does *not* re-define the mechanism columns,
- and only adds FRW-specific quantities to the same table(s).

### 2.2 FRW toy equations (pointer only)

The detailed equations live in `PHASE4_FRW_TOY_EQUATIONS_v1.md`. For design purposes, we only need to note:

- The FRW toy assumes a simple flat FRW background with:
  - `Omega_lambda_repo(theta)` imported from the joint grid,
  - `Omega_m_repo(theta) = 1 - Omega_lambda_repo(theta)` or a similarly simple relation, depending on the chosen toy,
  - a fixed `H0` for Stage I.
- `age_Gyr_repo(theta)` is computed by integrating the FRW age integral with these parameters.
- The outputs are stored in Phase 4 tables (and mirrored into Stage 2 tables where needed).

**Key design constraints:**

- No dynamic fitting of FRW parameters to data.
- No hidden dependence on θ beyond what is declared in the joint grid and FRW toy equations.
- All FRW quantities must be computable from:
  - θ,
  - the mechanism bundle,
  - and a small set of fixed FRW toy hyperparameters.

---

## 3. Host-alignment logic (design, not promotion)

The central design question is:

> How do we let FRW toys “touch” host-like or data-inspired structures **without** silently promoting Phase 4 into a data-fitting phase?

The answer is to enforce a strict separation between:

- **Masks and boxes** – which can overlap in interesting ways,
- **Claims** – which stay at the level of “there exists a θ-subset with properties X, Y, Z,”
- **Interpretation** – which is deferred to later phases and explicit gates.

### 3.1 Internal FRW toy masks

The FRW toy defines internal masks such as:

1. `frw_viable`:

   - A Boolean column on the θ-grid:
     - `True` where the FRW toy background is numerically and structurally acceptable,
     - `False` where it is unstable, unphysical, or otherwise rejected.
   - The exact criteria are specified in `PHASE4_FRW_TOY_HEALTHCHECK_v1.md`.

2. `in_toy_corridor`:

   - A Boolean column that marks θ where the mechanism and FRW toy jointly behave “nicely”:
     - e.g. where mechanism measures fall in a certain band,
     - and FRW ages stay within a chosen range.
   - This corridor is a **toy construct**:
     - it is allowed to be tuned internally,
     - but tuning decisions must be recorded and justified.

3. `in_empirical_anchor_box`:

   - A Boolean column indicating whether a θ lies inside a pre-declared box in `(Omega_lambda, age_Gyr)` space.
   - The box is specified in a JSON config (e.g. `empirical_anchor_box_v1.json`) under `stage2/frw_data_probe_analysis/config/`.
   - For design purposes:
     - the box is “inspired by” observed cosmology,
     - but in Stage I it is treated as a **fixed target** rather than something to be fitted.

### 3.1.1 What “alignment” means here

Alignment in Phase 4 means:

- **Overlap of masks**, not matching of data.

Examples of allowed statements:

- “There exists a subset of θ that is FRW-viable, in the toy corridor, and in the empirical anchor box.”
- “The FRW toy age over that subset sits in the interval `[13.3, 14.3] Gyr`.”

Examples of *disallowed* statements (in Phase 4):

- “Therefore the axiom explains the observed age of the Universe.”
- “Therefore we have measured `Omega_lambda` to be X.”

The design keeps this separation explicit.

### 3.1.2 FRW toy + host age windows (conceptual)

Phase 4 FRW toy ages can be compared to **host age windows** defined in Stage 2. Conceptually:

- A host (external) FRW or ΛCDM age computation defines:
  - a column `age_Gyr_host(theta)` on the joint grid,
  - and a host-age anchor window `[age_min, age_max]`.
- We can then define host masks:
  - `in_host_age_anchor_box` where `age_Gyr_host` lies inside the window,
  - and intersections with existing masks:
    - `FRW_VIABLE_AND_HOST_AGE_ANCHOR`,
    - `CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR`, etc.

In Phase 4, these intersections are **descriptive diagnostics**:
they show how robust the FRW toy corridor is under a given host age window.

### 3.1.3 Host-alignment corridor kernel (conceptual object)

Stage 2 contains code to extract a compact θ-subset where:

- the FRW toy is FRW-viable,
- θ lies in the toy corridor,
- and the host age lies in a Universe-like age window.

This subset is referred to as a **kernel** (e.g. a 12-point band in θ).

Design-wise:

- Phase 4 is allowed to:
  - refer to the existence and basic statistics of such a kernel,
  - inspect its mechanism profiles (e.g. mean and spread of `mech_baseline_A0`),
  - and describe its FRW toy ages and `Omega_lambda` band.
- Phase 4 is *not* allowed to:
  - rebrand this kernel as a measurement,
  - or make any statistical significance claims about it.

### 3.1.4 What this host-layer *does not* do

The host-alignment layer does **not**:

- change the Phase 3 mechanism definitions,
- change the FRW toy equations,
- introduce any dynamic feedback loop where host results tune the mechanism or FRW parameters.

It is a **one-way diagnostic overlay**:
from θ → mechanism → FRW toy → host age checks → descriptive masks and kernels.

---

## 4. External ΛCDM host overlays (Stage 2, non-claiming)

Although the *design* of Phase 4 is internal to the repo, Stage 2 now provides two explicit host overlays that this document must treat carefully:

1. **External FRW host (analytic age integrator).**

   - Implemented under `stage2/external_frw_host/`.
   - Uses a flat-FRW age integral with fixed `H0` and `Omega_m`, and `Omega_lambda(theta)` imported from the joint grid.
   - Produces:
     - a host-age cross-check table,
     - age-contrast summaries on the FRW-viable and corridor subsets,
     - a host *age-anchor* mask that identifies theta where the host age lies inside a pre-declared window around the observed Universe age.
   - In the current Stage-2 snapshot this window is approximately `[13.3, 14.3] Gyr`, leading to a small set of FRW-viable theta that are also host-age consistent.

2. **External cosmology host (ΛCDM background grid).**

   - Implemented under `stage2/external_cosmo_host/`.
   - Maps each theta to a simple cosmological parameter triplet `(Omega_m, Omega_lambda, H0)` and computes an independent FRW age `t0_host(theta)`.
   - Defines the same kind of host-age anchor window and extracts a **12-point theta-kernel** where:
     - the Phase-4 FRW toy is FRW-viable and lies in its toy corridor,
     - the external ΛCDM host age sits in the `[13.3, 14.3] Gyr` window,
     - the mechanism measures occupy a narrow, non-pathological band.
   - A comparison helper in `stage2/external_cosmo_host/src/build_external_host_kernel_comparison_v1.py`
     summarises this kernel against the broader host and toy sets.

### 4.1 How these overlays may be used in Phase 4

Within the **Phase-0 contract**, these external host overlays are allowed to support only:

- descriptive statements like:
  - “there exists a small theta-band (12 points in the current grid) where the FRW toy, the joint mechanism corridor, and a simple external ΛCDM host all assign Universe-like ages within a pre-declared window,”
- checks of internal consistency between:
  - FRW-viable masks,
  - corridor masks,
  - and host-age windows,
- design of future promotion gates (for Phase 5) that might require joint satisfaction of these masks.

They **may not** be used, at Phase-4 level, to:

- fit cosmological parameters,
- claim empirical support for the axiom,
- or interpret the 12-point kernel as a measurement of any real-world quantity.

Any such promotion would require an explicit future gate outside this document and a Phase-0-compatible update to `PHASES.md`.

