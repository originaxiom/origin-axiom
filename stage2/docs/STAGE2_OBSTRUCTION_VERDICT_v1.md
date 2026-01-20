# Stage 2 obstruction verdict (v1, 2026-01-20)

Status.  This memo records a Stage 2–level verdict for the obstruction overlays on branch `obstruction-program-v1` as of 2026-01-20. It synthesises the static FRW kernel, internal families, the toy late-time corridor from the LCDM box, and the first toy external-style age corridor. No Phase 0–5 contracts, FRW masks, or Stage 2 promotion gates are changed by this document.

## 1. Ingredients

The verdict is based on:

- Phase ladder and Stage 2 belts:
  - Phase 0–5 contracts and numerical artifacts as described in the main repo docs and phase papers.
  - Stage 2 FRW corridor, mech/measure, joint mech–FRW, FRW data-probe, and θ* diagnostic belts (all downstream-only).
- Static FRW kernel and families:
  - Static kernel table: `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`.
  - Family summary: `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_families_v1.csv`.
  - Pre-data FRW kernel: 1016 points out of 2048 (`in_pre_data_kernel = 1`).
  - LCDM-like band: 63 kernel points (`lcdm_like = 1`).
  - FRW toy corridor: 1186 grid points (`in_toy_corridor = 1`), 154 in the kernel.
  - Sweet subset: 40 θ points where
    - pre-data kernel,
    - LCDM-like band, and
    - FRW toy corridor
    all agree (≈ 2% of the grid, ≈ 3.9% of the kernel).
- Toy late-time corridor from LCDM box:
  - Construction: `stage2/obstruction_tests/src/build_toy_lt_corridor_from_lcdm_box_v1.py`.
  - Tables:
    - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv`,
    - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv`.
  - Corridor defined as the minimal axis-aligned box in \((E_vac, \omega_lambda)\) enclosing the LCDM-like band.
  - In the current snapshot this box reproduces the 63 LCDM-like points exactly and leaves the 40-point sweet subset unchanged.
- Toy external-style age corridor:
  - Helper: `stage2/obstruction_tests/src/apply_external_age_corridor_v1.py`.
  - Tables:
    - `stage2_obstruction_external_age_corridor_v1.csv`,
    - `stage2_obstruction_external_age_corridor_summary_v1.csv`.
  - Toy age band: `[10, 20]` Gyr (placeholder, deliberately broad).
  - Result: `external_age_corridor_v1 = 1` for all 2048 grid points, so:
    - the pre-data kernel (1016 points) is fully contained in the band,
    - the LCDM-like band (63 points) and FRW toy corridor (1186 points) are preserved,
    - the 40-point sweet subset inside the kernel is unchanged.

## 2. What the obstruction program sees (v1)

Internal consistency.

- The Phase 4 FRW masks and Stage 2 FRW corridor belt define a broad, nonempty pre-data kernel in θ.
- Inside this kernel:
  - a narrow LCDM-like band is clearly identified,
  - the FRW toy corridor overlaps the kernel in a modest but nontrivial way,
  - and their triple intersection defines a small, 40-point sweet subset.
- The toy late-time corridor derived from the LCDM box confirms that the LCDM-like region is already a clean, box-like patch in vacuum scalar space and preserves the sweet subset.

Effect of the first external-style corridor.

- The toy external age band currently acts as a structural no-op filter:
  - it contains the entire pre-data kernel and all previously defined internal families,
  - it leaves the 40-point sweet subset unchanged.
- This is by design: the band is deliberately broad to test the wiring of external-style flags without imposing tuned observational thresholds.

θ-neutrality.

- None of the constructions above hard-wire a special θ value:
  - they define families and subsets at the level of bands and intersections,
  - the 40-point sweet subset is a small region, not a unique grid point.
- The distinguished θ* candidate is treated as a diagnostic test location on this grid, not as an input to the definition of the kernel or corridors.

## 3. Verdict (v1)

From a Stage 2 obstruction perspective, as of this snapshot:

- There is **no internal obstruction**:
  - internal FRW diagnostics, mech/measure correlations, joint FRW–mechanism results, and the static kernel/family structure all cohere;
  - they support a nonempty pre-data kernel with a small, internally consistent sweet subset.
- There is **no external obstruction yet**:
  - the only external-style corridor implemented so far (toy age band) is deliberately too broad to cut the kernel;
  - it demonstrates the corridor machinery but is not a real constraint.
- The current obstruction overlays therefore yield a **non-obstruction verdict**:
  - the present Phase 0–5 + Stage 2 stack is compatible with a small region of θ that passes all internal filters and the first toy external filter;
  - the program has not yet applied sufficiently sharp external corridors or host-style questions to challenge this region.

This is a *diagnostic* verdict, not a physical claim about the real Universe. It says: given the current toy FRW setup and Stage 2 diagnostics, there is room for a small, internally consistent θ band, and nothing in the present obstruction machinery rules it out.

## 4. Roadmap and non-claims

Non-claims.

- No statement is made here about real-world viability, data fits, or host structure; those questions live in future external-style corridors and Stage II host work.
- No promotion is made from Stage 2 into phase-level claims; Phase 4/5 texts remain governed by their existing promotion gates.

Roadmap.

- Short term:
  - Design at least one sharper external-style corridor (for example, a tighter age band or an effective late-time expansion box) under an explicit design rung.
  - Study how the pre-data kernel and the 40-point sweet subset respond to such a corridor (survival, shrinkage, or collapse).
- Medium term:
  - Develop simple Stage II host scenarios and pose explicit host-compatibility questions over θ.
  - Decide whether obstruction-style results deserve tightly scoped promotion into Phase 4/5 text, subject to Phase 0 gates.

This verdict will be revised under new rungs only when:
- additional external-style corridors are implemented and tested, or
- the underlying Phase 4 FRW diagnostics are materially updated.
