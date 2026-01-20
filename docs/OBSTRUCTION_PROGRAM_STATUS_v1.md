# Obstruction Program Status (v1, 2026-01-21)

This memo records the status of the obstruction-style lens on the current Origin Axiom stack as of branch `obstruction-program-v1`. It assumes the canonical Phase 0–5 contracts and Stage 2 belts are already in place and treats obstruction as a diagnostic overlay, not a new set of claims.

## 1. Inputs and backbone

The obstruction program sits on top of the following components.

- Phase 0–5 contracts and papers:
  - Phase 0 governance and claims register (`phase0/` and `phase0/paper/`),
  - Phase 1 toy ensembles and residue existence (`phase1/` and `phase1/paper/`),
  - Phase 2 mode-sum and bounded FRW viability (`phase2/` and `phase2/paper/`),
  - Phase 3 mechanism module (`phase3/`),
  - Phase 4 FRW toy diagnostics (`phase4/`),
  - Phase 5 interface and sanity layer rung 0–1 (`phase5/`).
- Stage 2 diagnostic belts:
  - FRW corridor analysis (`stage2/frw_corridor_analysis/`),
  - mech/measure analysis (`stage2/mech_measure_analysis/`),
  - joint mech–FRW analysis (`stage2/joint_mech_frw_analysis/`),
  - FRW data-probe audit (`stage2/frw_data_probe_analysis/`),
  - doc and repo audit belt (`stage2/doc_repo_audit/`).
- Obstruction design docs:
  - `docs/OBSTRUCTION_PROGRAM_OVERVIEW_v1.md`,
  - `docs/THETA_ARCHITECTURE_v1.md`,
  - `docs/OBSTRUCTION_EMPIRICAL_PROGRAM_v1.md`,
  - `stage2/docs/STAGE2_OBSTRUCTION_TESTING_SPINE_v1.md`,
  - `stage2/docs/STAGE2_EXTERNAL_CONSTRAINTS_DESIGN_v1.md`,
  - `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`.

All obstruction rungs are strictly downstream of the locked Phase 3/4 pipelines and Stage 2 belts. They do not modify Phase contracts, FRW masks, or promotion gates.

## 2. Static FRW kernel and internal families

Using the Phase 4 FRW masks and shape probes, Stage 2 builds a static FRW pre-data kernel and several internal families over the 2048 point θ grid.

- Pre-data kernel: 1016 grid points (≈ 49.6% of the θ grid) satisfy the Phase 4 FRW viability mask and define the static kernel.
- LCDM-like band: a narrow internal band (63 grid points) that satisfies the current LCDM-like mask in the FRW scalar space (`E_vac`, `omega_lambda`, `age_Gyr`).
- FRW toy corridor: a shape and viability based corridor (Stage 2 FRW corridor belt) that slices the kernel and the LCDM-like band.
- Sweet subset: the triple intersection of {pre-data kernel, LCDM-like band, FRW toy corridor} contains 40 grid points. This 40 point region is the current “sweet subset” in the purely internal FRW diagnostic space and is used as a reference set in obstruction-style tests.

These families live in Stage 2 tables, including the FRW corridor outputs and the obstruction static kernel tables.

## 3. External-style helpers: LT and age bands

The obstruction program introduces a small set of Stage 2 helpers that mimic external-style corridors while remaining numerically downstream of the internal FRW masks.

- Static FRW kernel helper:
  - `stage2/obstruction_tests/src/build_static_frw_kernel_v1.py`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`
  - Carries the pre-data kernel flag, LCDM-like band, toy corridor, and FRW scalars on one θ aligned grid.
- Toy late-time corridor from LCDM box:
  - `stage2/obstruction_tests/src/build_toy_lt_corridor_from_lcdm_box_v1.py`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv`
  - Builds an internal toy late-time corridor by boxing the current LCDM-like island in the FRW vacuum scalar space.
- External LT corridor v1:
  - `stage2/obstruction_tests/src/apply_external_lt_corridor_v1.py`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_v1.csv`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_summary_v1.csv`
  - Tags the LCDM-like box as an explicit external-style late-time corridor helper. At this rung the external LT corridor v1 is effectively identical to the internal LCDM-like band.
- External age corridor v1 (machinery test):
  - `stage2/obstruction_tests/src/apply_external_age_corridor_v1.py`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v1.csv`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_summary_v1.csv`
  - Uses a wide age band [10, 20] Gyr as a trivial external-style age corridor; this band acts as a machinery test and does not significantly constrain the kernel.
- External age corridor v2 (constraining band):
  - `stage2/obstruction_tests/src/apply_external_age_corridor_v2.py`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v2.csv`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_summary_v2.csv`
  - Uses a narrower external-style age band [12.0, 15.0] Gyr as a genuinely constraining but still toy external-style age corridor.

All of these helpers are described in Stage 2 docs under `stage2/docs/` and are explicitly marked as diagnostic and interpretive.

## 4. What survives which filters

On the 2048 point θ grid the following picture emerges.

- Pre-data kernel:
  - 1016 points satisfy the Phase 4 FRW viability mask (≈ 49.6% of the grid).
- LCDM-like band:
  - 63 points form the LCDM-like island inside the kernel.
- FRW toy corridor:
  - A non-trivial subset of the kernel and the LCDM-like band lies in the FRW toy corridor; the triple intersection of {kernel, LCDM-like band, toy corridor} contains 40 points.
- Toy LT corridor from LCDM:
  - The toy LT corridor constructed from the LCDM box does not remove the 40 point sweet subset; it acts as a reshaping of the existing LCDM-like behaviour rather than a new independent constraint.
- External LT corridor v1:
  - By construction, the external LT corridor v1 coincides with the LCDM-like box. It selects the same 63 grid points and therefore leaves the 40 point sweet subset unchanged.
- External age corridor v1:
  - The wide [10, 20] Gyr age band leaves the kernel and sweet subset essentially untouched and is treated as a machinery test.
- External age corridor v2:
  - The [12.0, 15.0] Gyr band selects 358 grid points (≈ 17.5% of the grid), of which 356 lie inside the kernel (≈ 35% of the kernel).
  - All 63 LCDM-like points fall inside this age band.
  - The intersection of the FRW toy corridor with the age band contains 156 points.
  - The 40 point sweet subset survives unchanged under the age band v2: the intersection of {kernel, LCDM-like band, FRW toy corridor, external age corridor v2} contains 40 points.

At this rung, gentle external-style late-time and age corridors prune the kernel and the toy corridor but do not annihilate the sweet subset.

## 5. Obstruction verdict (v1) and roadmap

Verdict (v1).

- The current static FRW pre-data kernel is non-empty and remains non-empty under:
  - Phase 4 viability,
  - the LCDM-like band,
  - the FRW toy corridor,
  - the externally tagged LCDM box (external LT corridor v1),
  - and the toy external-style age band v2 [12.0, 15.0] Gyr.
- The 40 point sweet subset survives all of the above filters simultaneously. In the strict obstruction sense, the present stack does not yet exhibit an obstruction: moderate external-style late-time and age corridors constrain but do not eliminate the toy kernel or its sweet subset.
- The obstruction program thus reads the current snapshot as “structured but not yet obstructed”: the FRW viability corridor, LCDM-like band, toy FRW corridor, and gentle external bands produce a non-trivial but still live subset of θ values.

Roadmap.

- Age and expansion:
  - Introduce sharpened age corridors and expansion style constraints that are tied to explicit external arguments (for example more realistic bounds on late-time age and expansion history) rather than broad toy bands.
  - Study whether the kernel and sweet subset survive under these sharpened corridors.
- Structure-friendly proxies:
  - Introduce weak proxies for structure-friendly backgrounds and ask whether they cut significantly into the kernel or sweet subset.
- Hosts and Stage II:
  - Use the Stage II host design notes to define host level questions about corridor survival and kernel structure.
  - Treat the current static FRW kernel and sweet subset as a baseline for host-level and data-facing work rather than as a final object.

Non-claims.

- No obstruction-style statement in this memo is promoted to a Phase 2/3/4/5 claim at this rung. All conclusions are diagnostic and interpretive and live in Stage 2.
- No preference is claimed for any particular θ value; the 40 point sweet subset is tracked as a diagnostic region, not as a candidate for a fundamental θ measure.
- Any future use of obstruction-style statements in phase papers will require separate, tightly scoped promotion rungs and Phase 0 style gates.
