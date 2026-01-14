# PHASE 4 – FRW Toy vs External Host Alignment (Design v1)

This memo records how the **Phase 4 FRW toy pipeline** relates to the new **external FRW host** Stage 2 modules, what we empirically observed from the host cross-checks, and how we intend to *use* both layers going forward without over-claiming.

It is a **design + alignment document**, not a claims register. Phase 0 contracts, the Phase 4 alignment memo, and the Stage 2 belts remain the source of truth for what is and is not being claimed about the Universe.

---

## 1. Objects in play

### 1.1 Phase 4 FRW toy pipeline

The FRW-facing part of the repo currently lives under:

- `phase4/` (contract + design docs)
- `phase4/outputs/tables/` (toy FRW tables)

Key Phase 4 FRW tables include:

- `phase4_F1_frw_shape_probe_mask.csv`
- `phase4_F1_frw_viability_mask.csv`
- `phase4_F1_frw_data_probe_mask.csv`

These carry (among others) the columns:

- `theta` – θ grid
- `E_vac` – mechanism-side vacuum scale (from Phase 3)
- `omega_lambda` – effective Λ-like parameter derived from the mechanism
- `age_Gyr` – a toy FRW “age” quantity
- a family of boolean probes (`has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, `data_ok`, …)

Interpretation:

- This is a **toy FRW background engine**:
  - It takes `E_vac(θ)` and maps it to an effective `omega_lambda(θ)`,
  - integrates a simplified FRW-like background to produce `age_Gyr(θ)`,
  - and tags each θ with viability/data-probe flags.
- It is *not* a validated, high-precision FRW pipeline. Its role is:
  - to provide a coherent *internal* FRW playground,
  - to define masks like `frw_viable` and `TOY_CORRIDOR`,
  - and to serve as a bridge between the mechanism and cosmological-style diagnostics.

### 1.2 Stage 2 joint θ grid

Stage 2 builds a joint θ-grid that aligns mechanism outputs with FRW toy outputs:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

Key columns:

- `theta_index`, `theta`
- `E_vac`, `omega_lambda`, `age_Gyr`
- FRW masks: `in_toy_corridor`, `frw_viable`, `lcdm_like`, `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`
- Mechanism measures: `mech_baseline_*`, `mech_binding_*`

This is the **hub table** that all joint mech–FRW Stage 2 analyses use.

### 1.3 External FRW host

To probe how “physical” the FRW toy ages are, Stage 2 introduces a very simple FRW host under:

- `stage2/external_frw_host/`

The main table is:

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`

Columns include:

- `theta_index`, `theta`
- `omega_lambda`
- `age_Gyr` – Phase 4 toy age
- `age_Gyr_host` – age computed by a **simple analytic flat-FRW host** (using a standard integral for t₀ as a function of Ω_Λ)
- `age_Gyr_diff` – `age_Gyr_host - age_Gyr`
- `age_Gyr_rel_diff` – relative difference
- `frw_viable` – copied mask

Interpretation:

- The host is *not* a full Boltzmann code or cosmology pipeline; it is a **sanity-check FRW background calculator**:
  - It assumes a standard flat FRW form with matter + Λ,
  - computes an age vs Ω_Λ curve analytically,
  - calibrates a global scale factor once,
  - and then compares those ages to the Phase 4 toy ages pointwise on the θ grid.

---

## 2. What we actually observed

### 2.1 Global age discrepancies

From `stage2_external_frw_rung2_age_contrast_v1.csv` we have (schematically):

- **ALL_GRID**:
  - `⟨Δage⟩` ≈ −8.4 Gyr  
  - `⟨|Δage| / age_repo⟩` ≈ 0.53
- **FRW_VIABLE** subset:
  - `⟨Δage⟩` ≈ −2.5 Gyr  
  - `⟨|Δage| / age_repo⟩` ≈ 0.18
- **CORRIDOR_AND_VIABLE** subset:
  - `⟨Δage⟩` ≈ −11.9 Gyr  
  - `⟨|Δage| / age_repo⟩` ≈ 0.84
- **CORRIDOR_AND_VIABLE_AND_ANCHOR** subset:
  - `⟨Δage⟩` ≈ −10.9 Gyr  
  - `⟨|Δage| / age_repo⟩` ≈ 0.80

High-level takeaway:

- The toy FRW ages are **not calibrated** to the host ages, especially in the corridor and empirical-anchor regions.
- Even on the FRW-viable set, the relative age discrepancy is at the ~20% level on average.
- In the toy corridor (and particularly in the corridor ∧ anchor), the relative discrepancy is much larger.

### 2.2 Host-calibrated age-consistency subset

To turn this into a usable mask, Stage 2 defines an age-consistency filter:

- Script: `stage2/external_frw_host/src/flag_age_consistent_subset_v1.py`
- Output:  
  `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`

Key column:

- `age_consistent_rel_le_20pct` – boolean: |age_host − age_repo| / age_repo ≤ 20%

Summary stats (from script output):

- On **ALL_GRID** and **FRW_VIABLE**:
  - `n_age_consistent` ≈ 778 (∼ 0.38 of the grid)
- On **CORRIDOR_AND_VIABLE**:
  - `n_age_consistent` = 0
- On **CORRIDOR_AND_VIABLE_AND_ANCHOR**:
  - `n_age_consistent` = 0

So, under this **host-guided 20% age-consistency gate**:

- There is a substantial host-consistent FRW-viable region,
- but **none** of the current toy corridor ∧ anchor points pass this age-consistency threshold.

### 2.3 Host-side empirical anchor

We also defined a host-side mirror of the empirical anchor:

- Script: `stage2/external_frw_host/src/analyze_external_frw_host_anchor_v1.py`
- Output:  
  `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv`

This:

- infers an Ω_Λ window and a host-age window from the FRW empirical anchor table, and
- flags `in_host_empirical_anchor_box` on the host age cross-check table.

Intersections with the joint θ grid in:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_anchor_intersections_v1.csv`

show that:

- The **host anchor** is the same size (18 points) as the FRW toy anchor,
- and the set labels `HOST_ANCHOR`, `FRW_VIABLE_AND_HOST_ANCHOR`, `CORRIDOR_AND_HOST_ANCHOR`, `CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR` all report the same `n=18` count.

Interpretation:

- The empirical anchor region in (Ω_Λ, age) remains small (`18/2048`), but its image under the host mapping is coherent:
  - host ages in that region form a tight band,
  - and those points remain FRW-viable and in the toy corridor.

However, once we additionally impose the **age-consistency** gate (≤ 20% relative difference), the combination:

- (toy corridor) ∧ (empirical anchor) ∧ (host age-consistent)

is currently **empty**.

---

## 3. How we intend to use toy vs host going forward

Given the above, we adopt the following design stance:

### 3.1 The toy FRW engine remains the *internal* mechanism–FRW bridge

- Phase 4 continues to use the toy FRW pipeline to:
  - map `E_vac(θ)` to an effective `omega_lambda(θ)` and `age_Gyr(θ)`,
  - define internal FRW viability masks and the FRW toy corridor,
  - provide the FRW side of the **joint θ grid**.
- All of this remains under the Phase 4 alignment and Phase 0 contracts:
  - toy, diagnostic, non-data-contact,
  - used to test whether the **structure** of the axiom survives big, coarse constraints (matter era, late acceleration, etc.).

### 3.2 The external host is a **Stage 2 calibration + stress-test layer**

The external FRW host is treated as:

- A **calibration / sanity host**:
  - It instantiates a standard flat FRW background age vs Ω_Λ curve,
  - calibrates once to align with the repo’s notion of Gyr,
  - and then compares the toy FRW ages to this reference.

Its roles are:

1. **Age contrast diagnostics**  
   via `stage2_external_frw_rung2_age_contrast_v1.csv`  
   → “How far are the toy ages from a standard FRW age curve, on each subset?”

2. **Host-consistent masks**  
   via `age_consistent_rel_le_20pct` in `stage2_external_frw_rung3_age_consistency_mask_v1.csv`  
   → “Which θ-values are FRW-viable and age-consistent with an external FRW host?”

3. **Host anchor and corridor**  
   via host anchor and host corridor summaries  
   → “What does the empirical anchor region look like when expressed in host coordinates?”

**Crucially:**

- The host does **not** override or redefine the Phase 4 toy FRW machinery.
- It does **not** feed back into Phase 4 paper-level claims by default.
- It provides **additional Stage 2 gates** that must be explicitly referenced when invoked.

### 3.3 What “no intersection” currently means

The fact that:

- `(toy corridor) ∧ (empirical anchor) ∧ (host age-consistent)` is empty

is interpreted as:

- A **diagnostic observation about this particular implementation** of:
  - the axiom → mechanism → toy FRW map,
  - and the chosen empirical anchor box,
- not yet as a global verdict on the axiom itself.

Design-level reading:

- For the *current* toy implementation and anchor choice, the narrow corridor that is both:
  - FRW-viable,
  - inside the toy FRW empirical anchor box,
- does **not** survive the external age-consistency filter at ≤ 20%.

This is a strong and valuable constraint on the present toy implementation. Future rungs can:

- adjust the toy FRW integrator,
- adjust the mapping from `E_vac` to `omega_lambda`,
- adjust the width or definition of the empirical anchor box,

but any such moves must be explicitly documented and gated.

---

## 4. Proposed future rungs (outline only)

This section just sketches **possible** future rungs; they are not active until promoted.

### Rung H1 – Explicit FRW toy spec

- Goal: write a short technical spec of the current toy FRW integrator:
  - actual formulas used for `omega_lambda(θ)` and `age_Gyr(θ)`,
  - approximations and normalisations,
  - how matter / radiation / Λ are represented (or not).
- Output: `phase4/docs/PHASE4_FRW_TOY_SPEC_v1.md`.

### Rung H2 – Host–toy reconciliation experiments

- Goal: explore whether *simple* modifications could bring toy ages within a moderate relative-error band on the corridor, without breaking other structure.
- Design only for now:
  - identify 2–3 minimal levers (e.g. a rescaling constant, a better integration rule, a different mapping from `E_vac` to Ω_Λ),
  - plan how to test them in Stage 2 without touching Phase 4 claims.

### Rung H3 – Anchor and host gate promotion design

- Goal: specify **exactly** how host-based filters can be used as **promotion gates** for any Phase 4/5 narrative that references:
  - the empirical anchor,
  - FRW ages,
  - or host-consistent corridors.
- Output: a gate design doc under `docs/` or `phase4/docs/`, tightly tied to existing Stage 2 tables.

---

## 5. Summary

- Phase 4’s FRW toy remains the **primary internal model** of how the mechanism’s vacuum story interacts with an FRW-like background.
- The external FRW host is a **Stage 2 calibration and stress-test layer**, not a replacement.
- Current diagnostics show:
  - large age discrepancies in the toy corridor and empirical-anchor region,
  - and an empty intersection once a 20% host age-consistency gate is applied there.
- These facts are recorded as constraints on the current implementation, not as universal no-go theorems.
- Future rungs (H1–H3) will:
  - formalise the toy FRW spec,
  - explore minimal host-aligned refinements,
  - and design promotion gates for any host-based empirical claims.


---

## 3. Status snapshot: what the external host alignment currently shows

This section documents, for Phase 4 and Phase 5, what the **implemented** Stage 2 external-host belt actually reports. It is not a final design, but a snapshot that future revisions must keep in view.

### 3.1 Implemented host belt

The current external FRW host alignment pipeline consists of:

- Analytic host age integrator:
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  - gives `age_Gyr_host` for each θ, based on a flat-FRW model with:
    - fixed \(\Omega_m\),
    - variable \(\Omega_\Lambda(\theta)\) taken from the joint grid.
- Age cross-check and contrast:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`
- Age-consistency mask (relative error ≤ 20% on FRW-viable set):
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`
- Background bridge:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv`
  - aligns host and toy ages in a single table for all θ.
- Host age window and anchor:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung4_age_window_summary_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`
- Intersections with the joint grid:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_corridor_summary_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`

### 3.2 Current alignment pattern (high-level)

With the current toy implementation and mapping:

- The host model identifies a **host-age anchor band**:
  - `age_Gyr_host ∈ [13.3, 14.3]` Gyr,
  - containing 34 θ–points (all FRW-viable in the host sense),
  - with tightly clustered mechanism amplitudes.
- The Phase 4 FRW toy identifies a **toy corridor** and a **toy empirical anchor kernel**:
  - toy corridor: broad, `in_toy_corridor == 1` (~58% of grid),
  - toy empirical anchor kernel: 18 points, all FRW-viable and in the toy corridor.

Alignment / misalignment:

- **Toy empirical anchor vs host model:**
  - The 18-point toy empirical anchor kernel maps to a host-age range well below the observed-age window;
  - it does not coincide with the host-age anchor band.
- **Host-age anchor vs toy corridor:**
  - The host-age anchor band does **not** intersect the current toy corridor at all.
- **Mechanism behaviour:**
  - Both the toy empirical anchor kernel and the host-age anchor band show tightly clustered mechanism amplitudes, but at different θ–locations and parameter values.

### 3.3 Design implications for future revisions

For future Phase 4/5 and Stage II work, this snapshot implies:

1. **Alignment tension is real and quantified.**
   - Any attempt to tighten the FRW toy or re-map the mechanism must keep track of:
     - whether the toy corridor can be made to intersect a host-age anchor band,
     - without destroying the internal FRW viability and mechanism coherence.

2. **We have a concrete “failure mode” to learn from.**
   - The current configuration provides a worked example where:
     - the axiom + mechanism + FRW toy can pass an internal empirical box,
     - but miss a simple external age constraint entirely.
   - Phase 5 can use this to argue both:
     - how the program could fail,
     - and what kind of revisions would be needed to move towards real cosmology pipelines.

Any future changes to:

- the definition of the toy corridor,
- the toy empirical anchor box,
- the host-age window,
- or the mapping from mechanism outputs to \(\Omega_\Lambda\),

must be reflected here, and should be accompanied by updated Stage 2 runs and a clear log entry in `PROGRESS_LOG.md`.

