# Obstruction program status (v1, 2026-01-20)

Status.  
This memo records the status of the obstruction program overlays on branch `obstruction-program-v1` as of 2026-01-20. It summarises how the existing Phase 0–5 + Stage 2 structure is being used to ask obstruction-style questions about the vacuum sector, static FRW corridors, and θ-families, without changing any locked contracts or promotion gates.

## 1. Inputs and backbone

The obstruction program is an interpretive layer built strictly on top of the existing stack:

- Phase ladder:
  - Phase 0 – governance and specification (contracts, gates, claims machinery).
  - Phase 1 – toy ensembles and existence of a residue in controlled settings.
  - Phase 2 – mode-sum and bounded FRW viability in a toy sense.
  - Phase 3 – mechanism module (amplitudes, non-cancellation floor, binding diagnostics).
  - Phase 4 – FRW toy diagnostics (masks and scalar summaries, no live data corridor).
  - Phase 5 – interface and sanity layer (rung 0–1, no new physics claims yet).
- Stage 2 belts (diagnostic-only, downstream of Phase 3/4):
  - FRW corridor analysis belt (rungs 1–9).
  - Mech/measure analysis belt (rungs 1–6).
  - Joint mech–FRW belt (rungs 1–4).
  - FRW data-probe audit belt (rungs 1–2).
  - θ* alignment diagnostic rung on the FRW grid.
  - Doc-audit belt for global documentation consistency.
- Obstruction-specific Stage 2 docs and helpers:
  - `docs/OBSTRUCTION_PROGRAM_OVERVIEW_v1.md` – high-level obstruction narrative and motivation.
  - `docs/OBSTRUCTION_EMPIRICAL_PROGRAM_v1.md` – scope and standards for empirical obstruction tests.
  - `stage2/docs/STAGE2_OBSTRUCTION_TESTING_SPINE_v1.md` – how the FRW, mech, joint, data, and θ* belts form a diagnostic spine.
  - `stage2/docs/STAGE2_OBSTRUCTION_STATIC_FRW_KERNEL_FAMILIES_v1.md` – static FRW kernel and family decomposition.
  - `stage2/docs/STAGE2_OBSTRUCTION_TOY_LT_CORRIDOR_FROM_LCDM_v1.md` – toy late-time corridor derived from the LCDM-like band.
  - `stage2/docs/STAGE2_EXTERNAL_CONSTRAINTS_DESIGN_v1.md` – design-only menu for future external-style corridors.
  - `docs/STAGEII_COSMO_HOSTS_DESIGN_v1.md` – Stage II host design sketch (where host-style questions will live).

All obstruction-program statements are interpretive: they sit on top of this backbone and do not change any Phase 0–5 contracts, numerical pipelines, or Stage 2 promotion gates.

## 2. Static FRW kernel and families (internal diagnostics)

Static kernel construction.

- Helper: `stage2/obstruction_tests/src/build_static_frw_kernel_v1.py`.
- Inputs: Phase 4 FRW masks and scalars under `phase4/outputs/tables/`:
  - `phase4_F1_frw_data_probe_mask.csv`,
  - `phase4_F1_frw_viability_mask.csv`,
  - `phase4_F1_frw_lcdm_probe_mask.csv`,
  - `phase4_F1_frw_shape_probe_mask.csv`.
- Output: `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`:
  - 2048 θ-grid points.
  - Columns including `theta`, `E_vac`, `omega_lambda`, `age_Gyr`, `frw_viable`, `data_ok`, `lcdm_like`, `in_toy_corridor`, `shape_and_viable`, `shape_and_lcdm`, and a derived `in_pre_data_kernel` flag.

Pre-data kernel and families.

- In the current snapshot:
  - `in_pre_data_kernel = 1` whenever `frw_viable = 1`; this selects 1016 of 2048 grid points (about half the grid).
  - `lcdm_like = 1` selects a small band of 63 points (~3% of the grid, ~6.2% of the kernel).
  - The Stage 2 FRW toy corridor flag `in_toy_corridor = 1` covers 1186 of 2048 points (~58% of the grid), 154 of which also lie in the pre-data kernel.
- Families helper: `stage2/obstruction_tests/src/analyze_static_frw_kernel_families_v1.py`.
  - Output: `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_families_v1.csv`.
  - Summarises families such as:
    - `ALL_GRID`,
    - `PRE_DATA_KERNEL`,
    - `LCDM_LIKE`,
    - `TOY_CORRIDOR`,
    - `KERNEL_AND_LCDM`,
    - `KERNEL_AND_TOY`,
    - `KERNEL_AND_LCDM_AND_TOY`,
    - `SHAPE_AND_VIABLE`,
    - `SHAPE_AND_LCDM`.

Key internal result.

- The triple intersection of:
  - pre-data kernel (`in_pre_data_kernel = 1`),
  - LCDM-like band (`lcdm_like = 1`),
  - FRW toy corridor (`in_toy_corridor = 1`),
  yields 40 θ-points:
  - about 2% of the full grid,
  - about 3.9% of the pre-data kernel.
- This 40-point region is the current “sweet subset” inside the static kernel: internally nonempty but small, and defined purely in terms of existing Stage 2 FRW diagnostics.

Interpretation.

- The static pre-data kernel is broad and contiguous.
- The LCDM-like region is a small, well-defined band inside that kernel.
- The FRW toy corridor overlaps the kernel in a modest but nontrivial way, and the 40-point triple intersection region provides a natural testbed for obstruction-style questions on the current grid.

## 3. Toy late-time corridor derived from LCDM box

Toy corridor construction.

- Helper: `stage2/obstruction_tests/src/build_toy_lt_corridor_from_lcdm_box_v1.py`.
- Input: `stage2_obstruction_static_frw_kernel_v1.csv`.
- Outputs:
  - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv` – kernel table augmented with `lt_corridor_box_from_lcdm`.
  - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv` – small family summary.

Definition.

- The helper:
  - selects LCDM-like points via `lcdm_like = 1` (63 points),
  - computes the minimal enclosing rectangle in the plane \((E_vac, \omega_lambda)\) over those points:
    - `E_vac` in [3.951757e-06, 5.230002e-06],
    - `omega_lambda` in [0.6030812, 0.7981552] (values as read from the current Phase 4 tables),
  - defines `lt_corridor_box_from_lcdm = 1` for θ-points inside this rectangle,
  - records family counts for:
    - `ALL_GRID`,
    - `PRE_DATA_KERNEL`,
    - `TOY_LT_BOX_FROM_LCDM`,
    - `KERNEL_AND_TOY_LT_BOX_FROM_LCDM`,
    - `LCDM_AND_TOY_LT_BOX_FROM_LCDM`,
    - `TOY_CORRIDOR_AND_TOY_LT_BOX_FROM_LCDM`.

Key internal result.

- The toy late-time corridor box selects exactly the same 63 points as the original LCDM-like mask:
  - it does not pull in additional kernel points,
  - it preserves the interpretation of the LCDM-like band as a small island in vacuum-scalar space.
- The intersection of the box with:
  - the pre-data kernel and
  - the FRW toy corridor
  yields the same 40-point region as before:
  - the triple intersection `kernel ∧ lcdm_like ∧ in_toy_corridor` and the intersection `kernel ∧ lt_corridor_box_from_lcdm ∧ in_toy_corridor` coincide in the current snapshot.

Interpretation.

- Geometrically, the LCDM-like region is already a clean, axis-aligned “patch” in the \((E_vac, \omega_lambda)\) plane.
- The toy late-time corridor derived from this patch is a sanity-check corridor:
  - it confirms that the LCDM-like band is box-like and self-contained at this resolution,
  - it shows that the 40-point sweet subset is stable under this simple reshaping of the vacuum sector.

This construction does not introduce new observational input; it repackages existing FRW masks into a form that can later be compared with genuinely external-style corridors.

## 4. Interim verdict (v1)

From the obstruction perspective, as of this status:

- Internal consistency:
  - The Phase 4 FRW masks and Stage 2 FRW corridor belt define a broad, viable band in θ with a well-behaved LCDM-like subset.
  - The static kernel, family summaries, and toy LT corridor all agree on the existence and size of the small, LCDM-compatible sweet subset.
- No internal obstruction yet:
  - There is no internal diagnostic that collapses the pre-data kernel to an empty set or to a unique θ.
  - The obstruction program currently finds a nonempty, small region where all internal filters agree, rather than a contradiction.
- No external-style obstruction yet:
  - No explicit late-time, age-based, or structure-friendly external corridors have been imposed.
  - No host-consistency filters have been implemented; Stage II hosts remain at the design stage.
- θ-neutrality:
  - The constructions so far do not hard-wire any preferred θ value; the 40-point region is a subset, not a singled-out point.
  - The special θ* candidate is treated as a diagnostic location to be tested against these filters, not as an input assumption for their design.

In summary, obstruction-program-v1 currently says: the present Phase 0–5 + Stage 2 stack can support a nonempty, internally consistent sweet subset of θ that passes the FRW kernel, LCDM-like band, and FRW toy corridor simultaneously. No obstruction is yet imposed by internal diagnostics alone.

## 5. Roadmap

Near-term work (within Stage 2 and obstruction-program-v1):

- External-style corridors:
  - Instantiate at least one genuine external-style corridor (for example a conservative late-time expansion band or age-based cut) as a Stage 2 helper over the static kernel, following the design menu in `STAGE2_EXTERNAL_CONSTRAINTS_DESIGN_v1`.
  - Compare how the pre-data kernel and the 40-point sweet subset behave under this corridor (survival, shrinkage, or collapse).
- Host-style questions:
  - Refine `docs/STAGEII_COSMO_HOSTS_DESIGN_v1.md` to describe simple host scenarios and how they would be represented as flags over θ.
  - Prepare for Stage II rungs that ask whether the sweet subset admits plausible host scenarios.

Longer-term work:

- Dynamic extensions:
  - Explore whether the static kernel and its families can be embedded into more dynamic or multi-snapshot diagnostics, still governed by Phase 0 contracts.
- Promotion decisions:
  - If obstruction-style results become stable and interpretable, consider tightly scoped promotion rungs that move a small subset of these findings into Phase 4/5 text or Stage II host narratives, under explicit gates.

Non-claims.

- This status memo does not introduce new numerical pipelines, thresholds, or data; it summarises the obstruction overlays as they currently stand.
- No new claims about the physical Universe are made here; the document is an internal audit-style snapshot for obstruction-program-v1.

---

### Stage 2 obstruction verdict (v1)

For a concise Stage 2–level synthesis of what the obstruction overlays currently show (static FRW kernel, internal families, toy late-time corridor from the LCDM box, and the first toy external-style age corridor), see:

- `stage2/docs/STAGE2_OBSTRUCTION_VERDICT_v1.md`
