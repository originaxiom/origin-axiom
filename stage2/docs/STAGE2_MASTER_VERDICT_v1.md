# Stage 2 – Obstruction verdict snapshot (v1)

Status: **Stage 2 diagnostic synthesis – interpretive, non-binding.**  
Scope date: 2026-01-21 (obstruction-program-v1 snapshot).

This memo summarises what the current Stage 2 belts and obstruction helpers
say – and do *not* say – about obstructions to a trivial vacuum / FRW /
mechanism story on the existing θ-grid.

It is **not** a phase-level claims document. It does not change any Phase 0–5
contracts, FRW masks, or Stage 2 promotion gates. Any promotion of
obstruction-flavoured statements into phase papers will require separate,
tightly scoped rungs.

---

## 1. Ingredients

**FRW kernel and families.**

From the locked Phase 4 outputs and Stage 2 FRW corridor belt:

- θ-grid: 2048 points.
- Pre-data FRW kernel (`in_pre_data_kernel`): 1016 points (~50% of grid),
  defined by:
  - always-true sanity checks (`has_matter_era`, `smooth_H2`),
  - late-acceleration / viability mask (`frw_viable`),
  - with the aggregate data gate `frw_data_ok` *currently closed everywhere*.
- Within this kernel we already track:
  - the FRW-viable band,
  - LCDM-like band,
  - toy FRW corridor and intersections, as in the Stage 2 FRW belt docs.

**Static FRW kernel helper.**

The helper:

- `stage2/obstruction_tests/src/build_static_frw_kernel_v1.py`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_families_v1.csv`

collects, on a single θ-grid, the Phase 4 scalars
(`E_vac`, `omega_lambda`, `age_Gyr`) and the existing FRW masks and families,
and makes the pre-data kernel explicit as a reusable testbed.

**Toy and external corridors.**

On top of this kernel we have several Stage 2 obstruction helpers:

- Toy late-time corridor from the LCDM box:
  - `build_toy_lt_corridor_from_lcdm_box_v1.py`
  - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv`
  - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv`
- External-style late-time corridor (LCDM-shaped box):
  - `apply_external_lt_corridor_v1.py`
  - `stage2_obstruction_external_lt_corridor_v1.csv`
  - `stage2_obstruction_external_lt_corridor_summary_v1.csv`
- External-style age corridors:
  - v1 (broad / trivial band) and v2 (non-trivial 12–15 Gyr band),
    with tables and summaries under:
    - `stage2_obstruction_external_age_corridor_v1.csv`,
    - `stage2_obstruction_external_age_corridor_v2.csv`.
- Age + expansion + structure proxies:
  - `apply_external_age_expansion_corridors_v1.py`
  - `stage2_obstruction_external_age_expansion_corridors_v1.csv`
  - `stage2_obstruction_external_age_expansion_summary_v1.csv`,
    defining broad/tight flags for:
    - age,
    - expansion (ω_Λ / E_vac–like proxies),
    - a simple “structure-friendly” proxy combined from the above.

These helpers define a family of *static corridors* living entirely on the
existing θ-grid and vacuum/FRW scalars; they are deliberately simple and
transparent.

**Mechanism amplitudes on the kernel.**

Using the locked joint mech–FRW table:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

we attach the Phase 3 mechanism amplitudes to the static kernel:

- `attach_mech_amplitudes_to_kernel_v1.py`
- `stage2_obstruction_kernel_with_mech_v1.csv`
- `STAGE2_OBSTRUCTION_KERNEL_WITH_MECH_V1.md`

This yields a single θ-grid table carrying:

- FRW scalars and masks,
- pre-data kernel flag,
- toy and external corridor flags (age, LT, age+expansion+structure),
- mech amplitudes:
  - `mech_baseline_A0`,
  - `mech_baseline_A_floor`,
  - `mech_baseline_bound`,
  - `mech_binding_A0`,
  - `mech_binding_A`,
  - `mech_binding_bound`.

Finally, we summarise how these amplitudes behave under the various corridors:

- `analyze_kernel_mech_vs_external_corridors_v1.py`
- `stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`.

---

## 2. What survives? (kernel and external corridors)

Across all helpers, the current snapshot shows:

- **Pre-data kernel:**
  - 1016 / 2048 points (~50% of grid).
- **External age v2 band (12–15 Gyr):**
  - 356 kernel points (`KERNEL_AND_EXTERNAL_AGE_V2`),
  - ~35% of the kernel, ~17% of the grid.
- **LCDM-shaped LT external box (v1):**
  - 63 LCDM-like points on the grid, all lying in the kernel.
- **Toy LT corridor from LCDM box:**
  - a 63-point LCDM-like island reshaped into a toy late-time corridor,
  - overlapping the kernel and existing FRW corridor families.
- **Joint “sweet subset”:**
  - `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2`:
    - 40 points,
    - in the kernel,
    - in the LCDM-like band,
    - in the toy LT box from LCDM,
    - in the external age v2 band.
- **Tight age + expansion + structure proxy:**
  - `KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT`:
    - 51 kernel points,
    - satisfying the tight age band, tight expansion proxy, and tight structure proxy simultaneously.

Interpretation:

- The **pre-data kernel is not fragile**:
  - even after applying a non-trivial age window and simple expansion/structure proxies,
    we retain O(10–30%) of the kernel.
- The **40-point “sweet subset”** is a clean, non-empty intersection of:
  - FRW viability,
  - LCDM-like behaviour,
  - toy LT corridor,
  - external-style age corridor v2.
- A slightly different tight combination (age + expansion + structure) yields
  a comparable 51-point subset.

At this stage, nothing forces the kernel to collapse to zero under these
simple, physically-motivated cuts. That is already an *obstruction* to a
completely trivial picture in which “any reasonable external corridor kills
everything”.

---

## 3. Mechanism amplitudes under the corridors

From `stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`:

- On the **full kernel** (1016 points):
  - the main mechanism amplitudes sit in a narrow mid-band:
    - `mech_baseline_A0_mean ≈ mech_binding_A0_mean ≈ 0.0533`,
    - with min/max ranges roughly `[0.0375, 0.0577]`.
  - binding flags are zero across the kernel in the current snapshot
    (`mech_baseline_bound = mech_binding_bound = 0`).
- On the **40-point sweet subset** `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2`:
  - amplitudes remain firmly in the mid-band:
    - `mech_baseline_A0_mean ≈ mech_binding_A0_mean ≈ 0.0456`,
    - with a narrow range `[0.0446, 0.0467]`.
  - again, binding flags remain zero in this snapshot.
- On the **tight age+expansion+structure subset**
  `KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT` (51 points):
  - amplitudes are similar:
    - `mech_baseline_A0_mean ≈ mech_binding_A0_mean ≈ 0.0462`,
    - range `[~0.0449, ~0.0475]`,
  - binding flags still zero.

Interpretation:

- The current obstruction corridors **do not** drive the mechanism to an
  extreme non-cancelling floor or ceiling:
  - the sweet subset sits comfortably inside the kernel band,
    not at its edges;
  - there is no sign of a “collapse” of amplitudes towards a degenerate
    value when external-style corridors are applied.
- At the same time, the sweet subset is **non-empty and structured**:
  - it occupies a narrow θ-band and a compact region in FRW scalar space,
    with consistent mechanism amplitudes.

In other words, the obstruction we currently see is **topological / structural**
rather than a sharp extremal principle in the amplitudes.

---

## 4. What is obstructed, and what is still open?

**Obstructions already visible.**

Within the locked Phase 3 + Phase 4 + Stage 2 stack:

1. It is *not* the case that:
   - “any reasonable late-time and age-like corridor kills the θ-grid”.
   - The kernel survives multiple, simple, physically-motivated cuts.
2. It is *not* the case that:
   - “the LCDM-like island is isolated from FRW viability”.
   - Instead, LCDM-like and viability coexist inside the kernel and
     participate in the 40-point sweet subset.
3. It is *not* the case that:
   - “the mechanism amplitudes behave wildly under external-style cuts”.
   - On the contrary, they stay in a well-behaved mid-band across
     kernel and subsets.

These are all **obstructions to triviality** of the current θ-grid + mechanism
+ FRW toy.

**Open questions (non-claims).**

This snapshot *does not* establish that:

- any particular θ-value, θ-band, or mechanism amplitude level is singled out
  by realistic external constraints;
- the 40-point sweet subset (or the 51-point tight subset) is preferred or
  stable under sharper, data-calibrated corridors;
- the current mechanism amplitudes define a canonical “measure over θ”.

Those questions are *explicitly deferred* to future work:

- sharper external corridors (better age bounds, expansion histories,
  structure proxies),
- Stage II cosmology hosts,
- and any promotion of obstruction-flavoured statements into phase papers
  under Phase 0-style gates.

---

## 5. How this feeds forward

This verdict snapshot is used as follows:

- As a **reference point** for future external corridors:
  - new corridors must at least be as transparent and auditable as the current
    toy/external helpers;
  - any sharpening must be accompanied by a before/after comparison against
    this snapshot.
- As a **guardrail** for interpretation:
  - obstruction language is kept at the diagnostic level until Stage II
    hosts and data-calibrated corridors justify stronger statements.
- As a **pointer** for future rungs:
  - any attempt to promote an obstruction statement into Phase 4 or Phase 5
    must cite this memo and the underlying Stage 2 tables, and must pass
    a dedicated promotion gate.

This memo will be superseded by later versions (`_v2`, `_v3`, …) when
substantive new external corridors, data contacts, or mechanism refinements
are added.

