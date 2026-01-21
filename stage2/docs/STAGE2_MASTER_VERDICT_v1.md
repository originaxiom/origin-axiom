# Stage 2 – Master Verdict (FRW, mechanism, and obstruction lens)

**Status:** Stage 2 diagnostic synthesis.  
**Scope:** Summarise what the current Stage 2 belts and obstruction helpers
actually say – and do *not* say – about the Phase 3 mechanism, the Phase 4
FRW toy, and simple external–style corridors on the θ grid.

This document is interpretive and diagnostic only. It does **not** modify any
Phase 0–5 contracts, FRW masks, or Stage 2 promotion gates.

---

## 1. Inputs and belts considered

This verdict uses the following ingredients:

- **FRW corridor belt** (Stage 2):
  - Masks and families built from
    `phase4_F1_frw_viability_mask.csv`,
    `phase4_F1_frw_lcdm_probe_mask.csv`,
    `phase4_F1_frw_shape_probe_mask.csv`,
    `phase4_F1_frw_data_probe_mask.csv`.
  - Viability corridor on the 2048–point θ grid:
    about half the grid (1016 points) satisfy the internal FRW checks.
  - Data–gate flag `frw_data_ok` is currently empty (no point passes all
    data probes in the present snapshot).

- **Mechanism belt** (Stage 2):
  - Summary tables over Phase 3 outputs
    (`mech_baseline_scan.csv`, `mech_binding_certificate.csv`, and
    related diagnostics).
  - Smooth, monotone–ish mechanism amplitudes as functions of θ, with a
    non–trivial “floor” enforced by the non–cancelling penalty but no
    unique preferred value of the amplitude itself.

- **Joint mech–FRW belt**:
  - `stage2_joint_theta_grid_v1.csv` combines FRW scalars
    (`E_vac`, `omega_lambda`, `age_Gyr`) with Phase 3 amplitudes on a
    common θ grid, revealing strong correlations but no extra hidden
    structure beyond the FRW scalars.

- **θ★ alignment diagnostic**:
  - θ★ ≈ φ^φ lies inside the broad FRW–viable band but is not singled
    out by the current FRW corridor / LCDM–like families.

- **Obstruction helpers** (this branch):
  - Static pre–data FRW kernel:
    `stage2_obstruction_static_frw_kernel_v1.csv` (1016 points).
  - Toy and external–style corridors on that kernel:
    - toy LT corridor from the LCDM box,
    - external LT corridor v1 (LCDM–shaped),
    - external age corridor v2 (12–15 Gyr),
    - age / expansion / structure proxies (broad and tight bands),
    summarised in
    `stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv`,
    `stage2_obstruction_external_lt_corridor_summary_v1.csv`,
    `stage2_obstruction_external_age_corridor_summary_v2.csv`,
    `stage2_obstruction_external_age_expansion_summary_v1.csv`;
  - Kernel with attached Phase 3 amplitudes:
    `stage2_obstruction_kernel_with_mech_v1.csv`;
  - Mech–vs–external summary:
    `stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`.

All of these are downstream helpers: they *read* Phase 3 and Phase 4, but do
not change the upstream code or claims.

---

## 2. What Stage 2 shows (internal view)

From the **internal FRW and mech belts** alone:

1. There is a **non–trivial FRW–viable band** on the θ grid
   (≈ half the points satisfy the internal viability checks).

2. Within that band, Phase 3 mechanism amplitudes form **smooth, bounded,
   non–degenerate profiles** over θ:
   - amplitudes are neither forced to zero nor to their hard bounds,
   - the non–cancelling penalty enforces a floor but does *not* yet
     pick a unique θ or amplitude.

3. The **joint mech–FRW analysis** confirms that, on the current grid,
   mechanism amplitudes are essentially **re–parameterisations of the FRW
   scalars**:
   - strong correlations between {E_vac, ω_Λ, age_Gyr} and the mech
     amplitudes,
   - no extra hidden structure in the amplitudes once FRW scalars are
     known.

4. The **FRW data gate** in this snapshot is effectively **closed**:
   - `frw_viable` provides an internal pre–data corridor,
   - but `frw_data_ok` is empty, so all FRW results should currently be
     read as *pre–data diagnostics*.

5. θ★ lies inside the viable band but is not singled out by any existing
   internal FRW family.

Taken together, the original Stage 2 verdict was:

- The Phase 3 mechanism and Phase 4 FRW toy are **mutually consistent**,
  with a broad pre–data corridor.
- Stage 2 does **not** yet provide a canonical θ–measure or a decisive
  data–conditioned corridor.

---

## 3. What the obstruction helpers add

The obstruction lens asks: *if we start from the pre–data FRW kernel and add
simple external–style corridors, does anything robust survive without
asking the mechanism to “cheat” (e.g. collapse to zero or a bound)?*

The current helpers show:

1. **Static pre–data kernel**  
   The kernel (1016 points) already lives in a **moderately high, non–zero
   mechanism plateau**:
   - the mean baseline amplitude A₀ over the kernel is higher than over
     the full grid,
   - the Phase 3 bound flags are *not* triggered inside the kernel
     (no bound saturation is required to keep the kernel alive).

2. **External age corridor v2 (12–15 Gyr)**  
   Applying this age band cuts the kernel down to a few hundred points, but:
   - the surviving set still sits on a **well–behaved amplitude plateau**
     (no forced collapse to zero, no need to hit the penalty bound),
   - the amplitudes remain comparable in scale to the broader kernel.

3. **Toy LT and external LT corridors**  
   Corridors built from the internal LCDM–like island and its box in
   (E_vac, ω_Λ) carve out:
   - a modest number of *LCDM–like* kernel points,
   - still with regular, non–extreme mechanism amplitudes.

4. **Tight age + expansion + structure proxies**  
   Combining the tight age, expansion, and structure–proxy bands leaves:
   - a small but non–empty set of kernel points,
   - mechanism amplitudes that remain well inside their allowed ranges,
     again without being forced to zero or to bounds.

5. **The 40–point “sweet subset”**  
   The intersection of:
   - pre–data kernel,
   - LCDM–like band,
   - toy LT corridor,
   - external age corridor v2,
   yields ≈ 40 θ–grid points. On this subset:
   - all external–style filters are simultaneously satisfied,
   - the mechanism amplitudes still form a **narrow, regular plateau**,
     numerically similar to the tight–band subsets above.

In other words:

> With the current toy external corridors, the obstruction lens *does not*
> find a trivial obstruction where “nothing survives” or where the
> mechanism is forced into an obviously pathological regime.

---

## 4. What is **not** yet shown

Equally important is what the current Stage 2 + obstruction stack **does not**
yet establish:

1. **No canonical θ or amplitude.**  
   Neither the internal belts nor the external–style helpers (so far) pick
   out a unique θ or a unique mechanism amplitude. We have non–empty,
   regular corridors and plateaux, not a sharp selection.

2. **No data–fitted external corridors.**  
   The age and expansion bands used here are **toy external–style cuts**:
   - they are numerically compatible with a late–time universe of order
     14 Gyr old and a ΛCDM–like expansion history,
   - but they are *not* fitted to particular datasets or detailed
     observational bounds.

3. **No claim that the 40–point subset is preferred.**  
   The existence of a 40–point sweet subset is a **sanity check**, not a
   claim of physical optimality. At this stage it is simply:
   - a small, non–empty region where internal and toy external filters
     agree,
   - with mechanism amplitudes that look healthy rather than fine–tuned.

4. **No promotion into phase papers.**  
   None of the obstruction–flavoured statements are currently promoted
   into Phase 3–5 papers. They live entirely inside Stage 2 docs and
   helper tables. Any promotion would require separate, tightly scoped
   rungs and Phase 0–style gates.

---

## 5. Stage 2 verdict (with obstruction lens)

Given the above, the Stage 2 master verdict is:

1. The Phase 3 mechanism and Phase 4 FRW toy jointly support a **broad,
   internally consistent pre–data FRW kernel** on the θ grid.

2. When we overlay this kernel with **simple external–style corridors**
   (age bands, late–time expansion boxes, basic structure proxies), the
   kernel is **cut but not destroyed**:
   - non–empty subsets survive even under fairly tight toy cuts,
   - mechanism amplitudes on these subsets remain regular and bounded,
     well away from trivial zero or bound–saturation regimes.

3. Within this setup, there is **no obvious obstruction** to the
   non–cancelling mechanism from the simplest external–style corridors we
   have tested so far.

4. At the same time, the current stack **does not yet select** a unique
   θ, a canonical θ–measure, or a single preferred sweet subset; the
   obstruction tests are still at the “sanity–check corridor” stage.

Stage 2 is therefore **ready but not yet decisive**:

- ready, in the sense that:
  - the mechanism, FRW toy, and obstruction helpers form a coherent,
    reproducible diagnostic belt,
  - there exist non–empty kernel subsets that satisfy non–trivial FRW and
    toy external filters without breaking the mechanism;
- not yet decisive, in the sense that:
  - we have not run data–fitted external corridors,
  - we have not promoted any particular subset or θ–measure into the phase
    claims.

---

## 6. Next steps (beyond this verdict)

The natural next steps, outside this doc, are:

1. **Sharpen external corridors.**  
   Replace toy age / expansion bands with corridors tied to explicit
   external arguments (e.g. observational bounds, well–motivated w₀–wₐ
   boxes) and repeat the obstruction analysis.

2. **Host–level questions.**  
   Design Stage II “cosmology hosts” that ask:
   - how the pre–data kernel and candidate sweet subsets behave under
     richer structure / formation proxies,
   - whether any kernel subset is robust across hosts.

3. **Promotion gates (if warranted).**  
   Only after sharpened external corridors and host–level tests are in
   place should any obstruction–flavoured statement be considered for
   promotion into the phase papers, under explicit contracts and gates.

For now, this verdict locks in Stage 2 as a **diagnostic, obstruction-aware
belt**: strong enough to show that there is no trivial obstruction, but
deliberately short of claiming a unique, data–selected θ corridor.
