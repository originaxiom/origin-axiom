# Stage 2 — Obstruction program: mechanism amplitudes under external corridors (v1)

## 1. Scope and inputs

This memo documents how the Phase 3 mechanism amplitudes behave under the current set of external-style corridors used in the obstruction program. It is a **Stage 2 diagnostic document only**: no new claims are promoted into any phase paper, and no Phase 0–5 contracts or promotion gates are changed.

Inputs:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv`
  - FRW pre-data kernel with attached Phase 3 amplitudes:
    - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`,
    - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.
- External-style obstruction corridors:
  - Age corridor v2:
    - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v2.csv`
    - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_summary_v2.csv`
  - External late-time box:
    - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_v1.csv`
    - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_summary_v1.csv`
  - Age/expansion/structure proxy corridors:
    - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_corridors_v1.csv`
    - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_summary_v1.csv`
- Combined summary:
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`.

The helper script:

- `stage2/obstruction_tests/src/analyze_kernel_mech_vs_external_corridors_v1.py`

builds the summary table by:

1. Starting from the kernel-with-mech table.
2. Merging on the external corridor flags (age, expansion, structure, LCDM-derived and toy).
3. Defining a small set of diagnostic families.
4. For each family, recording:
   - counts and fractions relative to the full grid and to the pre-data kernel,
   - min / max / mean of the six mechanism amplitudes.

## 2. Families and sizes

The current v1 helper focuses on the following families (all living on the θ grid):

- `ALL_GRID`  
  All 2048 θ-grid points, independent of FRW viability or external corridors.

- `PRE_DATA_KERNEL`  
  Points with `in_pre_data_kernel = True` (Phase 4 viability band with sanity checks).  
  Size: 1016 points (~50% of the grid).

- `KERNEL_AND_EXTERNAL_AGE_V2`  
  Kernel points that also satisfy the non-trivial external age band v2  
  (age in [12, 15] Gyr in the current snapshot).  
  Size: 356 points (~17% of the grid, ~35% of the kernel).

- `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2`  
  The 40-point “sweet subset” defined earlier:
  - in the pre-data kernel,
  - inside the LCDM-like island,
  - inside the toy FRW corridor,
  - and inside the external age corridor v2.  
  Size: 40 points (~2% of the grid, ~4% of the kernel).

- `KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT`  
  Kernel points that pass a deliberately sharp combination:
  - tight age band,
  - tight expansion proxy band,
  - tight structure proxy band.  
  Size: 51 points (~2.5% of the grid, ~5% of the kernel).

These families are designed to give us three levels of sharpening:

1. Kernel vs full grid (pre-data internal structure).
2. Age-only external corridor vs kernel.
3. Very tight age+expansion+structure filters.

The sweet subset sits at level 2.5: more selective than the age-only kernel slice, but not yet as tight as the triple age/expansion/structure filter.

## 3. Mechanism amplitudes across families

From `stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`:

- On the **full grid**, the baseline amplitudes span a fairly broad range:
  - `mech_baseline_A0` and `mech_baseline_A_floor` lie between roughly 0.009 and 0.058,
    with means ≈ 0.039–0.041.
  - The corresponding binding amplitudes track the same range and means
    (the joint mech–FRW analysis already showed strong correlations).
  - The `*_bound` flags take values in [0, 1] with a mean of 0.25, reflecting the fact
    that the grid includes non-kernel regions where the mechanism can hit its floor.

- On the **pre-data kernel**:
  - `mech_baseline_A0` and `mech_baseline_A_floor` are squeezed into the upper end
    of the global range, with means ≈ 0.053.  
    The kernel discards the low-amplitude tail.
  - Within the kernel, `mech_baseline_A0` and `mech_baseline_A_floor` coincide:
    the floor is not active; the mechanism sits strictly above its nominal floor.
  - The `mech_baseline_bound` and `mech_binding_bound` flags are identically zero:
    no kernel points hit the explicit “non-cancellation bound”.

- On `KERNEL_AND_EXTERNAL_AGE_V2` (356 points):
  - The amplitude range is narrower again (roughly 0.038–0.055, mean ≈ 0.047).  
    The age corridor selects a middle slice of the kernel amplitudes.
  - Bound flags remain zero: the age cut is not forcing us onto the mechanism floor.

- On the **sweet 40-point subset** `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2`:
  - The amplitudes form a tight band around ≈ 0.045–0.046, with means ≈ 0.0456.
  - Both baseline and binding amplitudes share virtually the same narrow band.
  - Bound flags remain zero.
  - In other words, the sweet subset is:
    - a small fraction of the kernel in FRW space,
    - but it lives in a *smooth internal band* of the mechanism amplitudes,
      away from both the floor and the high end.

- On the tight age+expansion+structure family `KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT` (51 points):
  - Amplitudes lie in a similar narrow band slightly above the sweet subset
    (means ≈ 0.0462), again with no bound hits.
  - This confirms that tightening the external proxies does not push us into a
    pathological corner of mechanism space: we remain in a smooth interior band.

At this level of analysis, the external-style corridors reshape the **FRW kernel** substantially (1016 → a few hundred → ~50 points), but they do **not**:

- drive the mechanism amplitudes towards a saturation floor,
- nor isolate any sharp internal discontinuity or cliff in the mechanism.

Instead, all non-trivial external families sit in reasonably smooth, mid-range bands of the Phase 3 amplitudes.

## 4. Obstruction-flavoured reading

Within the obstruction program this v1 snapshot suggests:

- The existing mechanism module is compatible with:
  - a non-empty, broad FRW pre-data kernel,
  - a non-empty subset satisfying age-only and age+expansion+structure prototypes,
  - and a small sweet subset where all current internal and toy external filters agree.

- The mechanism amplitudes on these filtered sets are:
  - strictly above the explicit non-cancellation floor,
  - internally smooth across θ,
  - and not tuned post-hoc to the external corridors.

Thus, **nothing in the current external-style corridors “obstructs” the mechanism** in the sense of forcing it into a contradiction or into a degenerate corner. What we have instead is a **moderately selective, but still comfortable**, intersection between:

- internal FRW viability,
- toy late-time / LCDM-inspired boxes,
- simple age and structure proxies,
- and a well-behaved band of mechanism amplitudes.

From an obstruction point of view this is a **negative result (v1)**:

- The current stack does *not* yet deliver a razor-sharp obstruction that kills most of the pre-data kernel while preserving only a tiny, mechanistically special region.
- But it also does *not* reveal any obvious incoherence between the mechanism and the FRW+external toy corridors.

The verdict at this rung is therefore:

> The v1 obstruction toolkit confirms that the existing mechanism and FRW toy stack can support non-trivial, externally sharpened corridors without obvious tension. A sharper obstruction, if it exists, will require:
> - better-motivated external corridors (age + expansion + structure, possibly data-informed), and  
> - a finer-grained view of mechanism amplitudes (including their derivatives and higher diagnostics).

## 5. Gating and future rungs

Gating:

- This memo is **Stage 2 diagnostic only**.
- It does not:
  - promote any mechanism amplitude to a preferred θ-measure,
  - alter any Phase 4 FRW masks,
  - or update any Phase 0–5 contracts or claims tables.

Future rungs (O3.x and beyond) will:

- introduce better-motivated external corridors (age, w₀–wₐ, structure proxies),
- inspect not just amplitude values but also their θ-gradients and curvature within the filtered sets,
- and assemble a Stage 2 obstruction verdict (`STAGE2_OBSTRUCTION_MASTER_VERDICT_v1.md`)
  that can feed, under separate gates, into any future Phase 4/5 text.

