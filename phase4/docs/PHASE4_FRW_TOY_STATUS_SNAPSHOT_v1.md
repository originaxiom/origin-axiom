# Phase 4 FRW Toy Status Snapshot (Stage 2 – early anchor era)

_Last updated: 2026-01-14 (Stage2 FRW/anchor belt + external host diagnostics).  
This is a STATUS SNAPSHOT, not a claims paper._

---

## 1. FRW toy backbone and grid

**Grid + basic structure**

- θ-grid: 2048 points on \[0, 2π), evenly spaced.
- FRW quantities are computed on this grid and stored in:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- Key FRW-derived columns there:
  - `theta`, `E_vac`, `omega_lambda`, `age_Gyr`
  - Boolean FRW flags: `frw_viable`, `lcdm_like`, `shape_and_viable`, `shape_and_lcdm`
  - Downstream Stage2 uses these as the FRW “background lab bench”.

**Mechanism → FRW mapping (very brief)**

- Phase 3 / Stage2 mechanism maps θ to a vacuum‐like scale:
  - θ ↦ `E_vac(θ)`
- Phase 4 FRW toy then maps `E_vac` into an effective cosmological constant sector:
  - `E_vac` ↦ `omega_lambda` (toy Ω_Λ-like parameter)
  - FRW background integrator ↦ `age_Gyr` (toy age of the Universe)
- H₀ and unit conversions in the FRW toy are deliberately coarse:  
  it is a **diagnostic FRW background**, not a precision ΛCDM pipeline.

---

## 2. Internal FRW toy structure (Stage2 corridor recap)

Using Stage2 FRW corridor analysis on the Phase 4 tables:

- Total grid: **2048** points.
- FRW_viable set:
  - `FRW_VIABLE`: **1016** points (≈ 0.496 of grid).
- Toy corridor (the internally defined “good θ-strip”):
  - `TOY_CORRIDOR`: **1186** points (≈ 0.579 of grid).
- Intersection of toy corridor and FRW viability:
  - `CORRIDOR_AND_VIABLE`: **154** points (≈ 0.075 of grid).

These sets are encoded and summarized in:
- `stage2/frw_corridor_analysis/outputs/tables/…`
- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

At this snapshot level, the message is:

> The FRW toy has a fairly broad toy corridor (≈ 58% of θ)  
> and about half the grid is FRW_viable. Their intersection is a
> **moderately narrow band** (≈ 7.5% of θ) where the toy corridor and FRW
> viability both hold.

---

## 3. Empirical FRW anchor box (Ω_Λ & age)

We introduced a **first empirical anchor** in Stage2:

- Define a small “data-inspired” box in FRW observable space using:
  - Ω_Λ‐like parameter (`omega_lambda`)
  - toy Universe age (`age_Gyr`)
- This box is configured via:
  - `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`
- Stage2 anchoring script:
  - `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`
  - Output mask:
    - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`

**What the anchor box hits**

On the θ-grid:

- `EMPIRICAL_ANCHOR`: **18** points (≈ 0.0088 of grid).
- All 18 satisfy:
  - FRW viability: they are inside `FRW_VIABLE`.
  - Toy corridor: they are inside `TOY_CORRIDOR`.

From Stage2 joint analysis:

- `FRW_VIABLE_AND_ANCHOR`: **18** points.
- `CORRIDOR_AND_ANCHOR`: **18** points.
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`: **18** points.

So:

> The empirical FRW box carves out a **tiny kernel (18/2048 points)** that
> lies fully inside both the FRW_viable set and the toy corridor.

**Segments & θ-geometry**

Using Stage2 kernel analysis, those 18 anchor points:

- Split into **two contiguous θ-segments** (each 9 points) on the grid.
- Both segments are **far from θ\*** in θ-space (closest distances ≳ O(1) radians).
- The anchor kernel is therefore:
  - small,
  - multi-segment,
  - and **not centered on θ\***.

Mechanism profiles on this kernel (from
`stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`):

- Mechanism amplitudes (`mech_baseline_A0`, `mech_binding_A0`) in the kernel are:
  - tightly clustered around ≈ 0.0461 with very small scatter.
- On the **full FRW_viable set**, the same measures are:
  - ≈ 0.0533 with broader support.

Interpretation:

> The empirical FRW anchor is sitting in a **mechanism “shoulder region”**:
> lower than the FRW_viable mean, tightly clustered, but not at any obvious
> extreme or boundary. It is inside the toy corridor but not special in an
> obvious extremal sense.

---

## 4. External FRW host: age cross-check

To avoid being trapped in our own toy, we added an **analytic FRW host**:

- Host age calculator:
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  - Reads joint grid and computes an “external” FRW age (`age_Gyr_host`) from
    an analytic flat FRW background with a more standard H(a) integral.
- Cross-check table:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
- Age-contrast summaries:
  - `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`
  - Output:
    - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`

Key numbers (at this snapshot):

- Over the **FRW_viable** set:
  - Mean |age_host − age_toy| / age_toy ≈ 0.18 (≈ 18% relative difference).
- Over `CORRIDOR_AND_VIABLE`:
  - Mean relative difference ≈ 0.84 (≈ 84%).
- Over `CORRIDOR_AND_VIABLE_AND_ANCHOR` (the 18-point empirical kernel):
  - Mean relative difference ≈ 0.80 (≈ 80%).

So:

> The toy FRW ages agree with the analytic host at the **O(20%) level**
> on the broad FRW_viable set, but the specific toy corridor + empirical
> anchor region is quite misaligned (≈ 80% relative age mismatch).

This is consistent with the design: the FRW toy is “quick and diagnostic,”
not tuned to match a precision FRW host.

---

## 5. External FRW host: age anchor vs toy corridor

We also defined a **host-based age anchor** directly in the host age:

- Host age anchor window:
  - `age_Gyr_host ∈ [13.3, 14.3]` Gyr (roughly 1 Gyr around ≈ 13.8 Gyr).
- Flagging script:
  - `stage2/external_frw_host/src/flag_external_frw_host_age_anchor_v1.py`
- Outputs:
  - Mask: `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
  - Summary: `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_summary_v1.csv`
  - Profiles: `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`

Host age anchor set:

- `HOST_AGE_ANCHOR`: **34** points (≈ 0.0166 of grid).
- All 34 are **FRW_viable**.
- **None** of the 34 lie in the toy corridor:
  - `CORRIDOR_AND_HOST_AGE_ANCHOR`: **0**.
  - `CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR`: **0**.

Mechanism + FRW summary for these 34 points (from the profiles table):

- `omega_lambda_mean` ≈ 1.05 with modest spread.
- `age_Gyr_host_mean` ≈ 13.6 Gyr (by construction of the window).
- `age_Gyr_toy_mean` ≈ 12.6 Gyr (toy age underestimates host age by ≈ 1 Gyr here).
- Mechanism measures:
  - `mech_baseline_A0_mean` ≈ 0.0513 with very small std.
  - Similar for `mech_binding_A0_mean`.

Interpretation:

> The host FRW age anchor picks out a **narrow FRW-viable band** that:
> - sits **entirely outside** the current toy corridor, and
> - lives at slightly higher mechanism amplitude (~0.051) than the empirical
>   FRW anchor kernel (~0.046), but still below the FRW_viable mean (~0.0533).

So at this snapshot:

- There exists a **host-age-consistent FRW band** (≈ 1.7% of θ) that is:
  - FRW_viable and host-age-correct,
  - but incompatible with the current toy corridor definition.

---

## 6. Monotonicity check on toy FRW ages

To sanity-check the FRW toy background itself, we added a monotonicity diagnostic:

- Script:
  - `stage2/external_frw_host/src/check_frw_toy_age_monotonicity_v1.py`
- Output:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung5_toy_age_monotonicity_v1.csv`

Method:

- Restrict to FRW_viable rows.
- Sort them by `omega_lambda`.
- Look at discrete gradients of `age_Gyr` along that ordering.

Snapshot result:

- On the FRW_viable set (1016 points):
  - `n_steps = 1015`
  - `n_pos = 0`, `n_neg = 1015`, `n_zero = 0`
  - So age is **strictly decreasing** with increasing `omega_lambda` on the viable set.
- Gradient stats:
  - `grad_mean` ≈ −2.02 (Gyr per unit θ-step, in this ordering)
  - `grad_min` ≈ −4.92, `grad_max` ≈ −1.44
  - No sign flips.

Interpretation:

> The FRW toy age behaves qualitatively as expected:
> higher Ω_Λ-like values correspond to **younger toy universes** in a strictly
> monotonic way on the FRW_viable set. Whatever its absolute calibration, the
> internal FRW toy structure is coherent and well-behaved.

---

## 7. Status summary (what this snapshot tells us)

At this point in Stage2 / Phase4:

1. **Internally:**
   - The FRW toy background is structurally coherent:
     - FRW_viable, toy corridor, and shape/lcdm masks behave in an orderly way.
     - Age vs Ω_Λ-like parameter is monotonic on the viable set.

2. **Empirical FRW anchor box (Ω_Λ & age_toy):**
   - Defines a **tiny kernel** (18/2048 θ-points).
   - That kernel lies fully inside both FRW_viable and the toy corridor.
   - Mechanism amplitudes there are tightly clustered but not extremal;
     θ\* is not inside this kernel.

3. **External FRW host (age cross-check):**
   - On the full FRW_viable set, the host ages and toy ages differ by O(20%).
   - On the toy corridor + empirical anchor kernel, the mismatch is much larger (O(80%)).
   - A host-age anchor window around the observed Universe age picks out 34 FRW-viable θ-points that:
     - are **not** in the current toy corridor,
     - live at moderately high mechanism amplitude (~0.051),
     - and have host ages ≈ 13.6 Gyr vs toy ages ≈ 12.6 Gyr.

4. **High-level takeaway:**

> The current θ → E_vac → FRW mapping supports **internally consistent** toy
> FRW structure and a small FRW-empirical kernel inside the toy corridor,
> but when we ask for **host-calibrated ages near the real Universe**, the
> allowed θ-band lies **outside** the present toy corridor.

This is exactly the kind of “early empirical friction” Phase0 wanted:
it tells us that any future attempt to tune the toy corridor toward
real-world FRW behavior will have to either:

- adjust the θ → E_vac → Ω_Λ mapping, or
- revise the definition of the toy corridor itself, or
- accept that this particular corridor implementation may be in tension
  with basic FRW age constraints.

No such tuning or revision is done at this snapshot; this file only records
where the **current implementation** stands.

