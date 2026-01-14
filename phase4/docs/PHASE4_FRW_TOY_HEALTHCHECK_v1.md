# Phase 4 FRW Toy Healthcheck (v1, 2026-01-13)

This note records the current status of the Phase 4 FRW “toy universe” layer, how it is wired into Stage 2,
and what we have learned from the first external FRW host cross-checks. It is deliberately descriptive and
non-claiming: its job is to prevent over-interpretation of the existing FRW tables, not to force agreement.

---

## 1. What the Phase 4 FRW toy currently does

The Phase 4 FRW-facing code produces a stylised background cosmology grid over a 1D θ-axis. The key artefact
for this discussion is:

- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`

Conceptually, this table contains:

- `theta` and `theta_index` – the 1D parameter we scan.
- `E_vac` – a vacuum scale exported from the Phase 3 mechanism (or an equivalent vacuum-side quantity),
  evaluated on the θ-grid.
- `omega_lambda` – an effective dark-energy density parameter derived from the vacuum scale.
- `age_Gyr` – a toy “age of the universe” in Gyr units, computed by the Phase 4 FRW integrator.
- a collection of Boolean flags encoding coarse FRW behaviour, in particular:
  - `has_matter_era`, `has_late_accel`, `smooth_H2`,
  - `frw_viable` – a summary “background is sane” flag,
  - additional masks used downstream in Stage 2 FRW corridor analysis.

Important:

- This is **not** a full Einstein–Boltzmann code.
- The FRW integrations and cuts are deliberately simplified. They are meant as:
  - a laboratory for “vacuum → FRW background” interactions,
  - not as a precision ΛCDM pipeline.

The Phase 4 paper and alignment docs already treat this layer as a **toy FRW diagnostic**. However, as we
start touching real numbers (e.g. age ~ 13.8 Gyr, Ω\_Λ ~ 0.7), it becomes crucial to document what happens
when we compare this toy to an explicit FRW host.

---

## 2. Stage 2 FRW empirical anchor (internal FRW space)

Stage 2 extends the FRW toy with a first empirical anchor in the (`omega_lambda`, `age_Gyr`) plane.

Configuration:

- Anchor config: `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`
  - defines a central point and half-widths in:
    - `omega_lambda` (roughly centred near a ΛCDM-like ~0.7),
    - `age_Gyr` (around a target age ~13–14 Gyr),
  - all interpreted purely at the **toy FRW** level.

Computation:

- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py` reads:
  - the Phase 4 FRW table,
  - the anchor config,
  - and produces:
    - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
      with a Boolean `in_empirical_anchor_box` column.

Summary:

- On the current θ-grid (2048 points), this defines:
  - `EMPIRICAL_ANCHOR`: 18 θ-values (~0.9% of the grid) with:
    - FRW-viable background (`frw_viable = True`),
    - and (`omega_lambda`, `age_Gyr`) inside the chosen toy anchor box.
- Stage 2 joint analysis confirms:
  - all 18 anchor points lie **inside** both:
    - the Phase 4 FRW-viable set,
    - and the Phase 4 toy corridor set (as defined in FRW corridor belts),
  - but they form two disjoint 9-point segments in θ that do **not** contain the current θ★ reference value.

So, at the level of the Phase 4 toy alone, we do have a small internal corridor where:

> vacuum → toy FRW → (Ω\_Λ, age\_toy) lands inside a plausible “empirical” box.

At this point, all of this is still **toy-level**: the “empirical anchor” is an internal dial, not yet checked
against an external FRW standard.

---

## 3. External flat-FRW host: age cross-check

To understand whether the toy `age_Gyr` is numerically compatible with a more standard FRW background, Stage 2
implements an independent “FRW host” computation:

- Script:
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
- Output:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`

Mechanics (schematic):

- Treats each θ as defining an effective flat FRW model via its `omega_lambda`.
- Integrates a standard background age functional (dimensionless), then:
  - calibrates a global Gyr scale factor against the FRW-viable subset to get `age_Gyr_host`.
- Joins back to the θ-grid with columns:
  - `age_Gyr_host`,
  - `age_Gyr_diff = age_Gyr_host - age_Gyr`,
  - `age_Gyr_rel_diff = (age_Gyr_host - age_Gyr) / age_Gyr`,
  - and the familiar FRW viability masks.

Key findings (qualitative summary; see Stage 2 tables for exact numbers):

- On **all 2048** grid points:
  - host and toy ages differ substantially (as expected, since the toy is crude).
- Restricting to the **FRW-viable** subset (~50% of grid):
  - the mean relative difference |Δage| / age\_toy is of order ~20%.
  - So for most FRW-viable points, toy ages are within a factor-of-few of the host ages.
- Restricting to `CORRIDOR_AND_VIABLE` and especially
  `CORRIDOR_AND_VIABLE_AND_ANCHOR`:
  - the age disagreements become large:
    - the 18-point empirical anchor kernel sits in a region where
      |age\_host – age\_toy| / age\_toy is of order ~80%.

In other words, the region that looks most tempting from the **internal** FRW toy point of view is also a
region where the toy’s age calibration departs significantly from a simple external FRW host.

---

## 4. Host-calibrated age-consistency mask

To make the “how bad is the disagreement?” question precise, Stage 2 defines a host-calibrated consistency mask:

- Script:
  - `stage2/external_frw_host/src/flag_age_consistent_subset_v1.py`
- Output:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`

Definition:

- `age_consistent_rel_le_20pct = True` if
  - `abs(age_Gyr_host - age_Gyr) / age_Gyr <= 0.2`.

Results:

- On the full θ-grid:
  - 778/2048 points (~38%) pass this 20% age-consistency cut.
- All of these are FRW-viable (by construction of the calibration).
- Crucially:
  - **none** of the 18 empirical anchor points lies in this age-consistent subset.

Stage 2 then propagates this mask into the joint θ-grid and summarises the sets in:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_corridor_summary_v1.csv`

which confirms:

- there exists a reasonably large **host-calibrated FRW corridor** (FRW-viable and age-consistent),
- but the present empirical anchor kernel does **not** intersect it at the chosen 20% threshold.

---

## 5. Host-side empirical anchor box

To separate “toy anchor” and “host anchor” clearly, Stage 2 defines a host-side empirical box:

- Script:
  - `stage2/external_frw_host/src/analyze_external_frw_host_anchor_v1.py`
- Output:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv`

Construction:

1. Join the FRW anchor mask table with the host cross-check table on θ.
2. Read off the min/max of `omega_lambda` and `age_Gyr_host` over the 18 anchor points.
3. Define a host-side empirical box in (`omega_lambda`, `age_Gyr_host`) using those extents.
4. Mark `in_host_empirical_anchor_box` for θ values falling into this box.

This yields:

- a host-side mask that selects the **same 18 θ-values**,
- now viewed through host ages instead of toy ages.

Intersections with FRW and toy corridor sets, recorded in:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_anchor_intersections_v1.csv`,

confirm:

- `HOST_ANCHOR` = 18 points,
- all inside `FRW_VIABLE` and the toy corridor,
- still outside the host age-consistent corridor (≤20% relative difference).

---

## 6. How we interpret this in Phase 4 (v1 stance)

Given the above, the current Phase 4 stance is:

1. **Toy ages are diagnostic, not calibrated observables.**
   - The `age_Gyr` column in `phase4_F1_frw_shape_probe_mask.csv` is:
     - a *toy* FRW background age,
     - convenient for internal scans and qualitative comparisons,
     - but not numerically calibrated to a standard FRW host across the whole θ-grid.
   - Statements about age must therefore be phrased as:
     - “toy age behaves like X as θ varies,”
     - not “we match the observed age of the universe.”

2. **The internal empirical anchor is informative but not yet an empirical success.**
   - The 18-point anchor kernel is:
     - internally coherent (FRW-viable, inside toy corridor, contiguous in θ),
     - and sits in a narrow band of mechanism amplitudes.
   - However:
     - when checked against an external FRW host, this region fails a simple 20% age-consistency test.
   - So the honest statement is:
     - “Given the current toy FRW implementation and empirical box, the internally attractive anchor region
        is *not* age-consistent with a simple flat-FRW host.”

3. **We treat the tension as a diagnostic, not as a reason to retune history.**
   - We do **not** retroactively modify Phase 4 or Stage 2 runs to enforce agreement.
   - Instead, we record:
     - the current implementation,
     - the precise diagnostics,
     - and the fact that the first contact with a host FRW throws up a tension.
   - Future belts may:
     - refine the FRW toy (e.g. better age mapping, clearer separation of “toy” vs “host” columns),
     - adjust the empirical box,
     - or explore different host models,
     - but those will be **new rungs**, not edits to this one.

---

## 7. Concrete implications for Phase 4 claims

Within Phase 4 (and any narrative that leans on Phase 4 outputs), this document implies:

- Allowed:
  - using FRW toy masks and ages to *classify* θ regions (e.g. “FRW-viable,” “late acceleration,” “toy age
    between X and Y Gyr”),
  - referring to Stage 2 belts as “diagnostic explorations of whether the axiom’s θ-corridors can coexist
    with simple FRW-inspired constraints.”

- Not allowed (until further gated belts demonstrate otherwise):
  - claiming that the current implementation “predicts the observed age of the universe,”
  - treating the 18-point empirical anchor kernel as a successful fit to background cosmology,
  - or using the toy ages as inputs to any data-level likelihood pipeline.

This healthcheck is therefore a **guardrail**: it preserves the value of the current FRW toy and Stage 2 belts
as an honest worked example, while keeping the door open for more refined, host-calibrated FRW layers in
future phases and stages.


---

## 3. Stage 2 healthchecks on the FRW toy (2026-01-14 snapshot)

This section records the current Stage 2 diagnostics that directly probe the FRW toy background and its alignment with a simple external FRW host model.

All tables and scripts referenced here are reproducible from the repo; see `stage2/docs/STAGE2_RUNBOOK_AND_INTERPRETATION_v1.md` and `stage2/docs/STAGE2_ENDPOINTS_GLOSSARY_v1.md` for details.

### 3.1 Internal FRW toy corridor and empirical anchor

Internal toy diagnostics (no external host) are based on:

- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- Stage 2 FRW corridor outputs in:
  - `stage2/frw_corridor_analysis/outputs/tables/*.csv`
- Empirical anchor mask:
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
- Joint intersections and profiles:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_*_v1.csv`

Snapshot of what the FRW toy passes:

- **FRW-viable set (`frw_viable == 1`):**
  - ~50% of the θ–grid (≈ 1016 / 2048) produce a FRW background that passes the internal viability checks (Big Bang, matter era, late acceleration, smooth \(H^2\), etc).
- **Toy corridor (`in_toy_corridor == 1`):**
  - ~58% of the grid (≈ 1186 / 2048) lie in the Phase 4–defined FRW toy corridor.
- **Intersection (`CORRIDOR_AND_VIABLE`):**
  - ~7.5% of the grid (154 / 2048) are both FRW-viable and in the toy corridor.

Empirical anchor box (toy-only):

- Defined as a small box in (`omega_lambda`, `age_Gyr`) (see `PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md`).
- Stage 2 finds:
  - `EMPIRICAL_ANCHOR`: 18 points (18 / 2048 ≈ 0.9% of grid).
  - All 18 lie in:
    - `FRW_VIABLE`,
    - `TOY_CORRIDOR`,
    - so also in `CORRIDOR_AND_VIABLE`.
  - These 18 points form **two disjoint contiguous θ–segments** of length 9 each, both at O(1) distance from θ★.

Mechanism behaviour in this toy-anchor kernel:

- Mechanism amplitudes (`mech_baseline_A0`, `mech_binding_A0`, etc.) cluster tightly around ~0.046 with very small spread.
- This contrasts with the broader FRW-viable and corridor-wide distributions.

**Healthcheck conclusion (toy-only):**

- The FRW toy is capable of producing a small kernel of θ values that:
  - pass the internal FRW viability conditions,
  - lie in the Phase 4 FRW corridor,
  - and sit inside a simple background-consistency box.
- However, this kernel:
  - is small (18 points),
  - is disconnected in θ (two segments),
  - and does **not** contain θ★.

### 3.2 External FRW host age cross-checks

Stage 2 also compares the toy ages to a simple analytic flat-FRW “host” model, using:

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
- Summary:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`
  - age-consistency mask:
    - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`

Key findings (current snapshot):

- On the full grid:
  - mean age difference (host − toy) is large and negative (toy universes are typically older).
- On the FRW-viable subset:
  - mean relative age difference is ~18–20% in magnitude.
- On the FRW corridor ∧ viable:
  - toy ages can be significantly older than host ages (differences O(10 Gyr)).

A host-age anchor window is defined as:

- `age_Gyr_host ∈ [13.3, 14.3]` Gyr
  - implemented in:
    - `flag_external_frw_host_age_anchor_v1.py`
    - with outputs:
      - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
      - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`

Stage 2 finds:

- Host-age anchor:
  - 34 points (34 / 2048 ≈ 1.7% of grid), all FRW-viable in the host model.
- Intersection with the **current** FRW toy corridor:
  - `CORRIDOR_AND_HOST_AGE_ANCHOR`: 0 points.
  - `CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR`: 0 points.

**Healthcheck conclusion (host age):**

- With the current toy equations and mapping, the Phase 4 FRW corridor does **not** intersect the simple host-age anchor band at all.
- This is a **tension**, not yet a proof of failure:
  - it may be resolved by:
    - changing the toy age normalisation,
    - adjusting the mapping from mechanism outputs to \(\Omega_\Lambda\),
    - or revisiting the toy corridor definition.
  - but it must be treated as a concrete red flag for Phase 4/5 to discuss.


### Rung X5: Age monotonicity vs \`omega_lambda\` (Stage 2)

**Script:** \`stage2/external_frw_host/src/check_frw_toy_age_monotonicity_v1.py\`  
**Table:** \`stage2/external_frw_host/outputs/tables/stage2_external_frw_rung5_toy_age_monotonicity_v1.csv\`

- Input: \`phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv\`.
- Restrict to the FRW-viable subset (\`frw_viable == 1\`; 1016 rows).
- Sort that subset by \`omega_lambda\`.
- Compute finite-difference slopes \`d(age_Gyr)/d(omega_lambda)\` on this sorted sequence.

**Result (current repo state):**

- \`n_theta = 1016\`, \`n_steps = 1015\`.
- Sign structure of gradients:
  - \`n_pos = 0\`, \`n_neg = 1015\`, \`n_zero = 0\`.
- So on the FRW-viable set, \`age_Gyr\` is **strictly decreasing** as \`omega_lambda\` increases.
- Gradient statistics:
  - \`grad_min ≈ -4.92\` Gyr per unit \`omega_lambda\`,
  - \`grad_max ≈ -1.44\` Gyr per unit \`omega_lambda\`,
  - \`abs_grad_p95 ≈ 4.11\` Gyr per unit \`omega_lambda\`.
- Value ranges on the FRW-viable set:
  - \`omega_lambda ∈ [0.3027, 1.6898]\`,
  - \`age_Gyr ∈ [11.46, 14.97]\`.

**Interpretation:**

- The Phase 4 FRW toy age is **internally well-behaved**: no wiggles or backtracking in \`age_Gyr(omega_lambda)\` over the FRW-viable band.
- This supports using narrow joint windows in \`(omega_lambda, age_Gyr)\` as empirical anchors, and interpreting the resulting \`theta\`-corridors as slices of a smooth trade-off curve (larger \`omega_lambda\` → younger universe), rather than artifacts of numerical noise.

