# Stage 2 joint mech–FRW diagnostics verdict (redundancy and θ★)

Status (2026-01-11): This document synthesises the Stage 2 joint mech–FRW rungs into a compact verdict about how Phase 3 mechanism-derived scalars and Phase 4 FRW quantities relate on the shared θ-grid. It is descriptive and diagnostic-only and does not introduce new claims beyond those already present in Phase 2/3/4 contracts and Stage 2 docs.

## 1. Inputs and scope

This verdict is based on the Stage 2 joint mech–FRW belt under `stage2/joint_mech_frw_analysis/`, in particular:

- Rung 1: joint θ-grid construction
  - `build_joint_theta_grid_v1.py`
  - Output: `stage2_joint_theta_grid_v1.csv` (2048 rows × 17 columns)
- Rung 2: family summaries on the joint grid
  - `analyze_joint_mech_frw_family_summaries_v1.py`
  - Output: `stage2_joint_mech_frw_rung2_family_summaries_v1.csv`
- Rung 3: joint correlations
  - `analyze_joint_mech_frw_correlations_v1.py`
  - Output: `stage2_joint_mech_frw_rung3_correlations_v1.csv`
- (and, where applicable) Rung 4-style family-wise correlation or refinement outputs if present.

These scripts combine:

- Phase 4 FRW tables under `phase4/outputs/tables/`:
  - `phase4_F1_frw_shape_probe_mask.csv`
  - `phase4_F1_frw_data_probe_mask.csv`
  - `phase4_F1_frw_viability_mask.csv`
  - `phase4_F1_frw_lcdm_probe_mask.csv`
- Phase 3 mechanism tables under `phase3/outputs/tables/`:
  - `mech_baseline_scan.csv`
  - `mech_binding_certificate.csv`
  - and related scalars.

The joint belt is strictly downstream: it does not modify Phase 3/4 artifacts or claims; it reads them into a unified grid to analyse redundancy and structure.

## 2. Joint θ-grid construction and consistency checks

Rung 1 (`stage2_joint_theta_grid_v1.csv`) builds a single 2048-point θ-grid that contains, for each θ:

- FRW scalars such as effective vacuum energy density `E_vac`, dark-energy-like parameter `omega_lambda`, and `age_Gyr`.
- FRW masks and family indicators derived from viability, LCDM-like probes, and toy corridor definitions.
- Mechanism-derived scalars from Phase 3, including baseline amplitude columns (`mech_baseline_*`), binding-related columns (`mech_binding_*`), and preferred diagnostics identified in the mech/measure belt.

Before joining, the script enforces a **strict θ-alignment tolerance** between all input tables:

- It checks that θ-values match across Phase 3 and Phase 4 tables to within a small numerical tolerance for all 2048 rows.
- Any mismatch beyond tolerance would trigger an error rather than a silent join.

The successful construction of `stage2_joint_theta_grid_v1.csv` and the consistency of downstream rungs confirm that, in the current snapshot:

- Phase 3 and Phase 4 artifacts are **internally θ-consistent** on the shared grid,
- and Stage 2 joint diagnostics can legitimately compare and correlate mechanism and FRW quantities pointwise.

This is a nontrivial sanity check tying together the mechanism, FRW, and corridor belts.

## 3. Family summaries on the joint grid

Rung 2 (`stage2_joint_mech_frw_rung2_family_summaries_v1.csv`) defines FRW-related families on the joint grid and computes summary statistics for each family. The families include, for example:

- `ALL_GRID`: all 2048 θ points.
- `FRW_VIABLE`: points where the FRW viability mask is true (the viability band).
- `LCDM_LIKE`: points passing LCDM-like probes on the FRW side.
- `TOY_CORRIDOR`: points in the Stage 2 toy corridor as defined from FRW scalars.
- Intersections such as `CORRIDOR_AND_VIABLE`, `CORRIDOR_AND_LCDM`, `FRW_VIABLE_AND_DATA_OK` (currently empty because `frw_data_ok` is false everywhere).

For each family, Rung 2:

- checks the **family size and fraction** of the grid,
- computes basic summary stats for key FRW scalars and mechanism scalars,
- and cross-checks that the fractions and overlaps match the pure FRW corridor belt (rungs 1–9).

The results show that:

- The family sizes and fractions match the independently computed FRW corridor belt, confirming that the joint grid faithfully reproduces FRW family structure.
- Mechanism-derived scalars behave consistently within each family: their means and spreads follow expectations given their correlations with FRW scalars (e.g. higher amplitudes in FRW-viable regions if tied to effective vacuum strength).

This rung confirms that the **family-level picture from FRW corridors carries over correctly** into the joint mech–FRW space: the joint grid is a faithful embedding of FRW families with additional mechanism scalars attached.

## 4. Joint correlations: redundancy between mech and FRW scalars

Rung 3 (`stage2_joint_mech_frw_rung3_correlations_v1.csv`) computes correlations between:

- FRW scalars such as `E_vac`, `omega_lambda`, and `age_Gyr`, and
- mechanism-derived scalars such as `mech_baseline_*` and `mech_binding_*`.

The key findings are:

- Several pairs of FRW and mechanism scalars exhibit **very strong linear correlations**, with |r| close to 1 across the full grid and within major families:
  - FRW scalars that encode effective vacuum sector strength correlate strongly with baseline mechanism amplitudes.
  - `E_vac` and `omega_lambda` themselves are strongly correlated in the current toy setup and share similar correlation patterns with mechanism scalars.
  - `age_Gyr` tends to anti-correlate with vacuum-like scalars (as expected in a toy FRW setting where stronger effective vacuum typically shortens the age), and mechanism scalars mirror this anti-correlation.
- These patterns are stable across FRW families (e.g. ALL_GRID vs FRW_VIABLE), indicating that the redundancy is not an artifact of a small subset or an edge case.

The central verdict from Rung 3 is that, on the current θ-grid:

- **mechanism-derived scalars are almost perfectly redundant with FRW scalars** as far as simple correlation structure is concerned,
- so, at this level, the mechanism appears to act as a **reparameterisation of the FRW vacuum sector** rather than as an independent source of structure.

This does not make the mechanism trivial – it still provides a structural way of constructing the vacuum floor and associated scalars – but it does constrain what new structure we can expect from Phase 3 amplitudes: they are not yet furnishing an independent axis of variation beyond FRW.

## 5. θ★ and joint structure

While the θ★–FRW alignment rung focuses primarily on FRW families, the joint grid makes it possible to ask whether θ★ appears special in the combined mech–FRW diagnostics. In the current snapshot:

- θ★ sits in the **FRW-viable band** and exhibits mechanism-derived scalar values that are consistent with other viable points at similar FRW scalar values.
- Because mechanism scalars are strongly correlated with FRW scalars, the θ★ point in the joint space is **not an outlier** in either FRW or mechanism marginal distributions.
- Any apparent specialness of θ★ in one scalar would need to show up as a deviation from the observed redundancy pattern; Stage 2 finds no such deviation at this level.

Thus, in the joint setting, θ★ behaves like a typical member of the FRW-viable band under both FRW and mechanism scalars. The joint belt reinforces the FRW verdict: there is **no joint mech–FRW signature that singles out θ★** in the current toy configuration.

## 6. Joint mech–FRW diagnostics verdict (current snapshot)

Combining the joint grid construction, family summaries, and correlations, the Stage 2 joint mech–FRW belt supports the following verdict:

- The mechanism and FRW worlds are **cleanly and consistently joined** on a shared 2048-point θ-grid; Phase 3 and Phase 4 artifacts are θ-consistent at the numerical level required for pointwise comparison and family analysis.
- FRW families defined in the corridor belt are **faithfully reproduced** in the joint grid, and mechanism scalars behave in a manner consistent with their FRW counterparts within each family.
- Mechanism-derived scalars are **highly redundant** with FRW scalars: simple correlation structure indicates that Phase 3 amplitudes essentially reparameterise the FRW vacuum sector in the current toy setup. There is no evidence, at this level, of an independent mechanism axis that carves out qualitatively new structure beyond FRW.
- θ★ lies within the FRW-viable band and **does not exhibit special behavior** in the joint space; it is not singled out by the combination of mechanism and FRW diagnostics currently implemented.

This verdict is intentionally modest and structural:

- It does not claim that the mechanism is unnecessary or trivial; the mechanism is still the source of the vacuum floor and the scalars that FRW uses.
- It does claim that, in the current configuration, **the joint mech–FRW space shows no additional structure beyond FRW that would support a special θ★ or a canonical measure over θ**.

Future work that seeks a nontrivial θ★ signature or a canonical measure will therefore need to go beyond the current mechanism and FRW constructions or refine them in ways that break this redundancy.

## 7. Potential future rungs (not executed here)

This verdict suggests, but does not enact, several possible future joint belts and rungs:

- Mechanism-variation + FRW belts that compare joint redundancy patterns across different non-cancellation ansätze to see whether any variant generates genuinely new joint structure over θ.
- Nonlinear and information-theoretic joint diagnostics (e.g. mutual information, nonparametric dependence measures) to test whether there is any subtle joint structure beyond linear correlations.
- Promotion-design rungs that determine whether any joint mech–FRW figures (e.g. scatter plots or joint family summaries) are worth promoting into Phase 4/5 text under Option A, even if they primarily illustrate redundancy rather than new structure.

These are reserved for later phases of Stage 2 and Phase 5 interface design and are not implemented here.
