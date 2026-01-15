# Stage 2 / Phase 4 FRW–Host Baseline: Open Questions and Next Rungs
_v1 — checkpointed after tag `stage2_phase4_F1_FRW_baseline_checkpoint_2026-01-15`_

This note sits **on top of** the Stage 2 / Phase 4 bridge docs:

- `stage2/external_frw_host/docs/STAGE2_EXTERNAL_FRW_HOST_DESIGN_v1.md`
- `stage2/external_cosmo_host/docs/STAGE2_EXTERNAL_COSMO_HOSTS_DESIGN_v1.md`
- `phase4/docs/PHASE4_EXTERNAL_HOST_KERNEL_BRIDGE_v1.md`
- `phase4/docs/PHASE4_FRW_F1_BASELINE_CHECKPOINT_v1.md`
- `phase4/docs/PHASE4_EXTERNAL_EYES_BASELINE_SUMMARY_v1.md`
- `stage2/docs/STAGE2_PHASE4_FRW_HOST_SUMMARY_v1.md`

Its job is to **make explicit what remains open** in the FRW–host story and to
list concrete candidate rungs for future work.

---

## 1. Baseline that is now fixed

As of this checkpoint:

- **F1 FRW backbone** (Phase 4)
  - Mapping: `F1_baseline_v1` with `alpha = 1`, `beta = 4`, vacuum
    branch `baseline_v1`.
  - Grid: `n_grid = 2048`, `theta ∈ [0, 2π)` with maximum actually used
    `theta_max ≈ 6.2801`.
  - FRW viability:
    - About half the grid is FRW-viable: `frac_viable ≈ 0.496`.
    - Age window used for a “sane FRW” is wide: `[10, 20]` Gyr, so the
      FRW-viability mask is dominated by FRW structural checks
      (matter era, late acceleration, smooth H²) and not by age cuts.

- **F1 toy shape corridor** (Phase 4)
  - Corridor defined from the baseline vacuum curve as
    `E_vac(θ) ≤ E_vac_min + 1σ` (purely diagnostic).
  - Corridor fraction: `≈ 0.579` of the grid.
  - Corridor `θ` span is essentially the full grid:
    `θ ∈ [0, 6.2801]`.

- **F1 FRW ΛCDM-like window** (Phase 4)
  - Target cosmology used for the internal probe:
    - `Ω_m = 0.3`, `Ω_r = 0`, `Ω_Λ,target = 0.7 ± 0.1`.
    - Target age: `13.8 ± 1.0` Gyr.
  - Resulting LCDM-like subset:
    - Fraction: `≈ 0.0308` of the full grid (63 / 2048 points).
    - `θ` range: roughly `[0.60, 3.36]`.
    - `Ω_Λ` range: roughly `[0.603, 0.798]`.
    - Age range: roughly `[13.19, 13.77]` Gyr.

- **Stage 2 FRW host toy (external FRW host)**
  - Host age-anchor window constructed from the Stage 2 FRW toy, using a
    **host-defined age band** instead of the Phase 4 LCDM band.
  - The host toy and Phase 4 FRW toy are wired by
    `stage2_external_frw_host_rung*` tables and the design doc
    listed above.

- **Stage 2 external flat-ΛCDM host (cosmo host)**
  - A flat-ΛCDM grid is built over `(Ω_m, Ω_Λ, H0)` with age computed by a
    standard FRW integrator.
  - For each θ on the Stage 2 / Phase 4 joint grid, we assign a host
    `(Ω_m, Ω_Λ, H0, age_host)` via an explicit `θ → (Ω_m, Ω_Λ, H0)` map
    (documented in `STAGE2_EXTERNAL_COSMO_HOSTS_DESIGN_v1.md`).

- **12-point external-cosmo host kernel** (Stage 2 ↔ Phase 4)
  - Kernel definition:
    - FRW-viable in the Phase 4 FRW sense.
    - Inside the Phase 4 toy corridor.
    - Near-flat host (|Ω_tot − 1| ≤ 0.05 in the external cosmo grid).
    - Host age-anchor satisfied (host assigns a Universe-like age).
  - Kernel characteristics:
    - Size: **12 points** out of 2048.
    - θ range: `≈ [0.64, 3.32]`.
    - `Ω_Λ` ranges:
      - Toy / repo: `≈ [0.689, 0.723]`.
      - Host: the same band (by construction on a flat-ΛCDM host).
    - Age ranges:
      - Toy / repo: `≈ [13.40, 13.50]` Gyr.
      - Host: `≈ [13.33, 13.77]` Gyr.
    - Mechanism amplitude on the kernel (`mech_baseline_A0`):
      - A narrow band around `≈ 0.0464`.

- **Key structural relation**
  - The 12-point external-cosmo host kernel lies:
    - Inside the Phase 4 FRW-viable region.
    - Inside the Phase 4 toy corridor mask.
    - Inside the Phase 4 LCDM-like window (given its tighter
      `Ω_Λ` and age ranges).
  - Stage 2 host checks therefore **do not rescue a bad FRW**; they
    **tighten an already acceptable FRW window**.

This is the configuration captured by:

- Tag: `stage2_phase4_F1_FRW_baseline_checkpoint_2026-01-15`.
- Docs: the bridge + checkpoint + external-eyes summaries listed above.
- Artifacts: refreshed Phase 4 paper and Phase 4 external-host kernel table.

---

## 2. What is deliberately *not* claimed (yet)

Even with this tidy wiring, several things are **explicitly _not_ claimed** in
the current baseline.

### 2.1. No “unique θ★” or hard selection

- The baseline reports **fractions and bands**, not a single preferred
  θ-value.
- The 12-point host kernel is a **subset** of a broader LCDM-like
  window and a much broader FRW-viable + corridor region.
- Nothing in the current Stage 2 / Phase 4 bridging claims that
  “θ★ must be one of these 12 points” or that the kernel is
  **the** unique survivor of all constraints.

### 2.2. No real external data yet

- The Phase 4 `F1_FRW_DATA_PROBE` explicitly runs on a **stub** dataset:
  - `phase4/data/external/frw_distance_binned.csv` is a placeholder.
  - The current run records `data_available = false`,
    `n_data_points = 0`, and a mask with `data_ok = 0` everywhere.
- Therefore:
  - No fit to supernova, BAO, CMB distance ladders, etc. is attempted.
  - No χ² or likelihood-based constraints are in the chain.
  - The “LCDM-like window” is defined only by our own internal
    `(Ω_m, Ω_Λ, age)` target box, not by external datasets.

### 2.3. No robustness scans over host modeling choices

- The external FRW host and external cosmo host currently use a **single**
  choice of:
  - Flatness prior (|Ω_tot − 1| ≤ 0.05 cut for near-flat).
  - Hubble prior via `H0_km_s_Mpc` grid choices.
  - Age tolerance used to define the “host age-anchor” window.
- We do **not** yet explore:
  - What happens if the flatness tolerance is tightened or loosened.
  - How sensitive the 12-point kernel is to:
    - Different host H0 priors (e.g. “Planck-like” vs
      “local-distance-ladder-like” H0).
    - Slight changes in the age-anchor window (e.g. ±0.2 Gyr vs ±0.5 Gyr).
  - Whether the kernel remains roughly the same, shrinks, or fractures
    into disjoint pieces under such deformations.

### 2.4. No mechanism-level interpretation of the kernel band

- We do report that `mech_baseline_A0` is tightly banded across the
  12-point kernel (around ~0.046).
- However, we do **not** yet claim:
  - That this band has a clean interpretation in terms of the deeper
    mechanism (e.g. “this is the unique allowed amplitude of some
    field”).
  - That this band is stable under different coarse-grainings of
    the mechanism, or slightly different baseline vacuum choices.
- Mechanism-level interpretation is left for later phases, after we
  are certain the FRW + host wiring is as clean and robust as possible.

### 2.5. No scan over alternative F1-like mappings

- The current baseline is tied to the F1 family with
  `alpha = 1`, `beta = 4`.
- We have not yet explored:
  - How the FRW-viable fraction, LCDM-like window, or host kernel
    shift if we change `(alpha, beta)` within the same functional
    family.
  - Whether there is a broader class of F1-like mappings for which
    **some** LCDM-like + host-compatible corridor exists, or whether
    the current mapping is unusually special.
- These questions belong to a **later rung** once the baseline is
  fully stable and documented (which it now is).

---

## 3. Candidate next rungs

Below are concrete options for what to do *next* on the FRW–host front,
now that the F1 baseline + host kernel is clean and checkpointed.

Each rung is designed to be **narrow**, **loggable**, and **reversible**.

### Option A — Robustness scans inside the existing F1 setup

Goal: Probe how brittle or stable the 12-point host kernel and LCDM-like
window are under small deformations of **host-side** assumptions, while
keeping the F1 mapping fixed.

Example subtasks:

- **A.1 — Flatness tolerance scan**
  - Vary the near-flat cut in Stage 2 external cosmo host from
    |Ω_tot − 1| ≤ 0.05 to a few alternatives (e.g. 0.02, 0.10).
  - Rebuild:
    - Near-flat mask.
    - 12-point-like kernel selection.
    - Phase 4 external host kernel bridge tables.
  - Track how many points survive and how the `θ`, `Ω_Λ`, age, and
    `mech_baseline_A0` bands move (if at all).

- **A.2 — Age-anchor window scan**
  - Tighten and loosen the host age-anchor around the current Universe
    age (e.g. ±0.2, ±0.5, ±1.0 Gyr).
  - Recompute the host age-anchor mask and kernel.
  - Compare with F1 FRW LCDM-like window to see whether the kernel
    still nests comfortably inside the internal LCDM probe.

- **A.3 — H0 prior variants**
  - Introduce a couple of simple H0 regimes in the external cosmo host
    grid (e.g. “low-H0” vs “high-H0” bands).
  - For each regime, recompute the host age-anchor and near-flat
    subset, and see whether the 12-point kernel remains present,
    shrinks, or disappears.

Deliverables per subtask:

- New Stage 2 tables (with `_v2` or similar suffixes).
- A short doc per subtask (e.g.
  `STAGE2_EXTERNAL_COSMO_HOST_ROBUSTNESS_v1.md`) summarizing what
  did and didn’t change.
- A short Phase 4 note clarifying that F1 mapping is unchanged; only
  host priors are being wiggled.

### Option B — FRW data-probe design (still data-free)

Goal: Design a **clean, data-ready pipeline** for the FRW distance probe
without actually bundling real external datasets.

Subtasks:

- Specify the exact CSV schema expected in
  `phase4/data/external/frw_distance_binned.csv` (columns, units,
  allowed redshift ranges).
- Clarify, in a doc, which public datasets *could* be plugged in later
  (e.g. SN Ia Hubble diagrams, BAO distance ladders) without naming
  specifics or hardwiring anything.
- Make sure `run_f1_frw_data_probe.py` is fully “plug-and-play” once a
  CSV of that schema appears, and that all diagnostics and masks are
  documented in `B_reproducibility.tex` and a short Phase 4 doc.

This rung would **not** change the baseline physics; it would only
upgrade the readiness level for actual data in a later stage.

### Option C — Phase 4 paper grooming around the host kernel

Goal: Refine the Phase 4 paper text so that the external host kernel
and the F1 FRW baseline are described with the **same clarity** as
the pipeline we just wired.

Subtasks:

- Make sure every quantity used in the host kernel table has:
  - A clear definition in the main text or reproducibility appendix.
  - A clear pointer to the generating script and table.
- Tighten the wording so that:
  - We do **not** over-claim (no unique θ★, no data-driven inferences).
  - We do emphasize the structural fact that the host kernel nests
    inside the FRW LCDM-like window.

This rung is mostly editorial, but it makes the baseline much more
digestible for external readers.

### Option D — Long-horizon exploration of alternative mappings

Goal: Once the baseline is rock-solid, explore whether **other mappings**
(F1-variants, F2, etc.) can produce similar or stronger patterns of
overlap between:

- Toy corridor.
- FRW viability.
- Internal LCDM-like window.
- External host kernel.

This is intentionally **not** a near-term rung, but it is useful to keep
on the horizon so we do not forget why we froze F1 in the first place.

---

## 4. Recommended immediate next rung

Given the current state of the repo and the Phase 0 contract, a sensible
**immediate** next rung on the FRW–host side is:

> **Option A.1 — Flatness tolerance scan**, with all other ingredients
> (F1 mapping, age targets, host age-anchor definition) held fixed.

Why this is a good next move:

- It directly stress-tests one of the most “physics-flavored” knobs in
  the host modeling: near-flatness.
- It is local: it only touches the Stage 2 external cosmo host module
  and the derived masks / kernels, plus short docs.
- It will show quickly whether the 12-point kernel is:
  - A robust feature of the combined FRW + host setup, or
  - A delicate artefact of the very specific |Ω_tot − 1| ≤ 0.05 cut.

If you agree, we can treat this note as the **gating document** for that
rung: we only implement changes that are explicitly called out here, and
we log all new tables, masks, and diagnostics as separate `_v2` (or
similar) artifacts, leaving the baseline checkpoint intact.
