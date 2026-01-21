# Stage 2 obstruction verdict (v1, obstruction-program-v1 branch)

This memo provides a snapshot verdict for the Stage 2 obstruction program as of 2026-01-21 on the `obstruction-program-v1` branch. It synthesises the existing Stage 2 belts (FRW corridors, mech/measure analysis, joint mech–FRW analysis, FRW data probes) together with the new obstruction helpers (static FRW kernel, toy and external-style corridors, and mechanism amplitude overlays). All statements here are interpretive and remain in Stage 2. No Phase 0–5 contracts, claims, or promotion gates are altered.

## 1. Inputs and diagnostic spine

The obstruction verdict rests on the following components.

Phase 3 and 4 artifacts:

- Phase 3 mechanism tables and amplitudes:
  - `phase3/outputs/tables/mech_baseline_scan.csv`
  - `phase3/outputs/tables/mech_binding_certificate.csv`
- Phase 4 FRW masks and scalars:
  - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`

Stage 2 diagnostic belts:

- FRW corridor analysis (rungs 1–9).
- Mech/measure analysis (rungs 1–6).
- Joint mech–FRW analysis (rungs 1–4).
- FRW data-probe audit (rungs 1–2).
- θ-star alignment diagnostic rung.

Obstruction-specific helpers:

- Static FRW kernel:
  - `stage2/obstruction_tests/src/build_static_frw_kernel_v1.py`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`
- Toy and external corridors:
  - Toy late-time corridor from the LCDM box.
  - External age corridor (v1 and v2).
  - External late-time corridor (LCDM-aligned).
  - External age+expansion+structure corridors (v1) as documented in `STAGE2_OBSTRUCTION_EXTERNAL_AGE_EXPANSION_V1.md`.
- Mechanism overlays and summaries:
  - Kernel with attached Phase 3 amplitudes:
    - `stage2/obstruction_tests/src/attach_mech_amplitudes_to_kernel_v1.py`
    - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv`
  - Mechanism amplitudes under external corridors:
    - `stage2/obstruction_tests/src/analyze_kernel_mech_vs_external_corridors_v1.py`
    - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`

Together these objects form the obstruction testing spine: a static FRW kernel, a family of toy and external-style corridors, and a joined view of FRW quantities and mechanism amplitudes on a common θ grid.

## 2. Static FRW kernel and internal corridors

The static FRW kernel built from the Phase 4 masks contains:

- 2048 grid points in total on the θ grid.
- 1016 points in the pre-data kernel (fraction of grid ≈ 0.496), defined by FRW viability together with always-true sanity checks (`has_matter_era`, `smooth_H2`).

Internal Stage 2 FRW corridors and LCDM-like bands carve this kernel but do not destroy it:

- The FRW-viable band is broad and contiguous in θ and in the vacuum sector (`E_vac`, `omega_lambda`).
- The LCDM-like band isolates a small “island” in the vacuum sector.
- The original toy FRW corridor defines a band in `E_vac`–`omega_lambda` space that intersects but does not collapse the kernel.

From the earlier FRW corridor and θ-star diagnostics:

- θ-star lies inside the broad FRW-viable band.
- The current toy corridors and LCDM-like bands do not single out θ-star; they simply confirm that θ-star is not excluded by the toy FRW machinery.

At this level there is no obstruction: the kernel is non-empty, the FRW corridors are non-trivial, and θ-star sits in a viable region.

## 3. External-style corridors and kernel survival

The obstruction helpers introduce several external-style corridors on top of the static kernel.

Toy and external age corridors:

- An initial trivial age band (v1) is used as a sanity check and has little effect on the kernel.
- A non-trivial age band (v2), `external_age_corridor_v2`, selects:
  - 358 grid points in total (fraction ≈ 0.175),
  - 356 points inside the kernel (fraction of kernel ≈ 0.350).
- The intersection `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2` identifies a 40-point “sweet subset” that lies simultaneously in:
  - the pre-data FRW kernel,
  - the LCDM-like band,
  - the internal toy FRW corridor,
  - and the external age band v2.

External late-time corridor:

- An external-style late-time corridor derived from the LCDM box keeps a subset that is small but non-empty and overlaps with the kernel, toy FRW corridor, and LCDM-like region.
- This corridor is explicitly marked as a mock external helper aligned with the current LCDM-like island, not as a realistic late-time expansion constraint.

Age+expansion+structure corridors (v1):

- The broad age and structure proxies leave almost all of the kernel intact:
  - `AGE_BROAD_V1` and `STRUCT_PROXY_BASIC_V1` include 931 out of 1016 kernel points (fraction of kernel ≈ 0.916).
- The tight expansion and structure bands pick out a much smaller subset:
  - `EXPANSION_TIGHT_V1` and `STRUCT_PROXY_TIGHT_V1` select 51 kernel points (fraction of kernel ≈ 0.050).
- These tight bands are compatible with the age v2 corridor in the sense that they can be intersected with the 40-point age-based sweet subset without killing it outright.

Across all of these corridors the key observation is that:

- The pre-data kernel remains non-empty.
- The 40-point sweet subset survives under more than one external-style demand (age v2, LCDM-like, toy FRW corridor).
- Tightened age+expansion+structure bands carve the kernel but still leave a modest subset alive.

There is no sign, at this level, that reasonable external-style bands force the kernel to vanish.

## 4. Mechanism amplitudes under external corridors

The joined kernel-with-mechanism table attaches six Phase 3 amplitudes to each grid point:

- `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`,
- `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.

The summary `stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv` reports min, max, and mean of these amplitudes for several diagnostic families:

- `ALL_GRID`
- `PRE_DATA_KERNEL`
- `KERNEL_AND_EXTERNAL_AGE_V2`
- `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2` (the 40-point sweet subset)
- `KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT` (the 51-point tight age+expansion+structure subset)

The patterns are:

- Moving from `ALL_GRID` to `PRE_DATA_KERNEL` already narrows the amplitude ranges and raises the means, reflecting the fact that FRW viability correlates strongly with the mechanism amplitudes.
- Restricting to `KERNEL_AND_EXTERNAL_AGE_V2` and `KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT` further narrows the amplitude ranges but does not introduce any sharp discontinuities or pathological behaviour.
- The 40-point sweet subset, `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2`, has amplitude ranges and means that sit comfortably inside those of the broader kernel subsets. There is no sign of the mechanism amplitudes diverging, collapsing, or flipping sign in a way that would signal an obstruction.

In other words, within the current toy setup:

- The Phase 3 amplitudes behave smoothly and monotonically under all of the external-style corridors we have introduced.
- The external corridors carve the kernel in FRW space without revealing any hidden incompatibility in mechanism space.

## 5. Obstruction verdict (v1)

On the obstruction side the current Stage 2 snapshot supports the following verdict.

1. **No obstruction detected at the current toy level.** The static FRW kernel is non-empty, remains non-empty under a range of internal and external-style corridors, and admits small but non-trivial sweet subsets (such as the 40-point kernel ∧ LCDM ∧ toy FRW ∧ external age v2 intersection).

2. **Mechanism amplitudes cohere with the FRW kernel.** Within the kernel and its externally carved subsets the Phase 3 amplitudes are well-behaved, smoothly varying, and strongly correlated with the FRW scalars. There is no internal sign that the mechanism module is incompatible with the FRW toy diagnostics.

3. **No enforced uniqueness or selection of θ-star.** The existing corridors and external-style bands do not single out θ-star. θ-star lies inside the FRW-viable band and within the general kernel structure, but nothing in the current obstruction machinery forces the kernel to pinch down to a neighbourhood of θ-star. The obstruction program currently reads as “no obvious obstruction and no enforced uniqueness” at this resolution.

4. **Status of external corridors.** All external-style corridors used here are toy constructions derived from the current snapshot. They are structured enough to demonstrate that the kernel can survive non-trivial age and expansion demands, but they are not yet anchored to specific observational bounds or host-level metrics. As such they are informative tests of robustness, not final constraints.

5. **Implications for the broader program.** The lack of an obvious obstruction at this level is a necessary but not sufficient condition for the obstruction-motivated θ-ansatz to remain interesting. It tells us that the current Phase 3/4 stack can support non-trivial kernels and sweet subsets under simple external-style demands. It does not tell us that the ansatz is realised in nature, nor that θ-star is preferred.

## 6. Non-claims and next steps

Non-claims:

- No claim is made that the 40-point sweet subset or any other subset is physically realised or preferred. They are diagnostic regions, not detected corridors.
- No mechanism amplitude is promoted to a canonical θ-measure in this verdict. The measure problem remains open.
- No Phase 0–5 contract, claim, or non-claim is modified by this memo. It is a Stage 2 interpretive overlay only.

Next steps:

- Design and implement a small set of sharpened external corridors whose thresholds are tied to explicit external arguments (age bounds, simple effective dark-energy boxes, and structure-friendly proxies) rather than internal distributions.
- Explore how these sharpened corridors behave across different FRW snapshots and mechanism refinements, including whether the sweet subsets persist or fracture.
- Only once such sharpened corridors are in place and tested should an updated obstruction verdict be considered for promotion into Phase 4/5 text, under explicit Phase 0-style gates and with clearly documented provenance.

## 4. Snapshot: mechanism amplitudes under external-style corridors (O2.x)

This section records the current obstruction snapshot from the O2.x helpers. It is
**diagnostic only** and does not introduce any new Phase 0–5 claims.

### 4.1 FRW kernel and external-style corridors

Using the static FRW kernel and the external-style corridors built in Stage 2:

- The full θ grid has 2048 points.
- The pre-data FRW kernel (FRW masks only) contains 1016 points (~50% of the grid).
- The external age corridor v2 selects 358 grid points, of which 356 lie in the FRW kernel (~35% of the kernel).
- The toy late-time corridor derived from the LCDM-like band and the age corridor v2 defines a 40-point “sweet subset” inside the kernel:
  - FRW-viable,
  - LCDM-like under the internal LCDM band,
  - inside the toy FRW corridor,
  - inside the age band v2.
- The joint age+expansion+structure proxies (v1) carve the kernel down to a 51-point subset (~5% of the kernel) while keeping a non-empty, structured set of survivors.

The precise counts and fractions are recorded in:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_summary_v2.csv`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_summary_v1.csv`

These helpers are defined and motivated in the obstruction docs:

- `stage2/docs/STAGE2_OBSTRUCTION_EXTERNAL_AGE_CORRIDOR_V2.md`
- `stage2/docs/STAGE2_OBSTRUCTION_EXTERNAL_LT_CORRIDOR_V1.md`
- `stage2/docs/STAGE2_OBSTRUCTION_EXTERNAL_AGE_EXPANSION_V1.md`
- `stage2/docs/STAGE2_OBSTRUCTION_TOY_LT_CORRIDOR_FROM_LCDM_v1.md`

### 4.2 Phase 3 amplitudes on the kernel and external-style subsets

Attaching the Phase 3 mechanism amplitudes to the FRW kernel and summarising them
under the external-style corridors gives:

- On the pre-data FRW kernel:
  - all six Phase 3 amplitudes sit in a relatively narrow band well above zero
    (in the current toy implementation the minimum values are of order a few×10⁻²),
  - no kernel point approaches “near-perfect cancellation” under the current mechanism.
- On the 40-point sweet subset (kernel ∩ LCDM-like ∩ toy FRW corridor ∩ age band v2)
  and on the 51-point tight age+expansion+structure subset:
  - the amplitudes are even more tightly clustered,
  - the same non-zero floor is present.

These summaries are recorded in:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`
- documented in `stage2/docs/STAGE2_OBSTRUCTION_KERNEL_WITH_MECH_V1.md`.

### 4.3 Interpretation and non-claims

Interpretation:

- The current stack (Phase 3 mechanism + Phase 4 FRW masks + Stage 2 corridors)
  admits a non-empty pre-data FRW kernel.
- Non-trivial age, expansion, and simple structure proxies can be imposed while
  keeping a non-empty, structured subset of kernel points.
- On these subsets the current mechanism exhibits a persistent, non-zero amplitude
  floor; it does not drive the amplitudes towards zero within the present toy.

Non-claims:

- No unique θ-value or narrow θ corridor is singled out by these diagnostics.
- No mechanism amplitude is promoted to a fundamental “forbidden cancellation measure”.
- No Phase 0–5 contract, FRW mask, or Stage 2 promotion gate is changed by this
  snapshot.
- No claim is made that the surviving subsets are physically preferred; they are
  infrastructure for future obstruction rungs.

Future work (O3.x):

- Design sharper, externally motivated corridors (age, expansion, structure) and
  re-run the same diagnostics.
- Explore whether the non-zero amplitude floor persists under those sharpened
  corridors, and whether any robust structural features in θ-space emerge.
- Only after such sharpened tests are in place and audited under Phase 0 style gates
  should any obstruction-flavoured statement be considered for promotion into a
  phase paper (most naturally, as a candidate Phase 5 claim).

