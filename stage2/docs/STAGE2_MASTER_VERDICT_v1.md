# Stage 2 master verdict (FRW, mechanism, joint, data probes, and θ★)

Status (2026-01-11): This document provides a compact, program-level verdict for the current Stage 2 diagnostic belts. It synthesises the FRW corridor, mechanism/measure, joint mech–FRW, FRW data-probe, and θ★ diagnostics into a single snapshot. It is descriptive and diagnostic-only and does not introduce new claims beyond those already present in Phases 0–5 and existing Stage 2 docs.

## 1. What Stage 2 is and is not

Stage 2 is a **diagnostic belt** downstream of locked Phases 0–3 and the Phase 4 FRW stub. It consists of:

- FRW corridor belt (`stage2/frw_corridor_analysis/`) – families and robustness checks built on Phase 4 FRW masks.
- Mechanism/measure belt (`stage2/mech_measure_analysis/`) – diagnostics of Phase 3 mechanism-derived scalars and measure/flag candidates.
- Joint mech–FRW belt (`stage2/joint_mech_frw_analysis/`) – a shared θ-grid and correlation structure between Phase 3 amplitudes and Phase 4 FRW scalars.
- FRW data-probe belt (`stage2/frw_data_probe_analysis/`) – audit of FRW data probes and the aggregate `frw_data_ok` flag.
- θ★ alignment rung (`stage2/theta_star_analysis/`) – θ★ position within FRW families and corridors.
- Doc/repo audit belt (`stage2/doc_repo_audit/`) – non-physics doc and archive diagnostics.

Stage 2:

- **reads** Phase 3 and Phase 4 artifacts,
- **writes** its own tables, figures, and docs under `stage2/`,
- and **never mutates** canonical Phase claims or artifacts.

Any promotion of Stage 2 results into Phase 4/5 text must go through explicit promotion gates and Phase 0–style governance; this has not yet happened in the current snapshot.

## 2. FRW verdict: toy viability bands and a closed data gate

The Stage 2 FRW belts (summarised in `STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`, `STAGE2_FRW_DATA_PROBE_AUDIT_v1.md`, and `STAGE2_FRW_VERDICT_v1.md`) support the following FRW verdict:

- The Phase 4 FRW construction, as implemented and sampled on a 2048-point θ-grid, admits a **broad, contiguous FRW-viable band**: viability occupies roughly half the grid and forms extended bands in θ rather than isolated spikes.
- Corridor-style families built from FRW scalars (viable band, LCDM-like subsets, toy corridors, and their intersections) are **structurally robust** under contiguity, stride, and smoothing tests. The FRW toy world is nontrivial but not pathological.
- Structural probes such as `has_matter_era` and `smooth_H2` are effectively **always true** in the current configuration and act as sanity checks rather than selective filters.
- The aggregate FRW data flag `frw_data_ok` is **identically false** in the present snapshot; the intersection `FRW_VIABLE ∧ DATA_OK` is empty. This is interpreted as “data gate not yet open”, not as physical exclusion.

FRW verdict (current snapshot): there is a clean, structurally nontrivial **pre-data FRW viability band** on the θ-grid, but the **data gate is closed**; no data-conditioned corridor exists yet in the canonical pipeline.

## 3. Mechanism verdict: rich diagnostics, no canonical θ-measure

The Stage 2 mechanism/measure belt (summarised in `STAGE2_MECH_MEASURE_SUMMARY_v1.md` and `STAGE2_MECH_VERDICT_v1.md`) supports the following:

- Phase 3 mechanism tables under `phase3/outputs/tables/` form a **small, well-behaved family** of CSVs: scalar columns are finite, bounded, and non-degenerate across the θ-grid.
- A **short list of probability-like columns** can be isolated: bounded, nontrivial distributions that naturally split into:
  - **measure-like** candidates (smooth, graded behavior over θ),
  - and **flag-like** candidates (near-Boolean, mask-like behavior).
- θ-profiles of measure-like candidates are **smooth and numerically well-controlled** on the current grid; there are no signs of instability or unresolved spikes.
- A small set of **preferred mechanism-derived diagnostics** can be identified based on numerical stability and profile quality; these are ideal as Stage 2 diagnostic axes and for future interface summaries.

At the same time:

- The mech/measure belt **does not identify a unique, physically motivated θ-measure**. Preferred candidates are excellent diagnostics but remain numerically redundant and lack an independent physical principle that would elevate one to “the” measure.
- Mechanism-only diagnostics do **not** single out θ★ in a nontrivial way; θ★ behaves like a typical viable-point in terms of mechanism scalars.

Mechanism verdict (current snapshot): Phase 3 provides a **rich, well-controlled diagnostic scalar field over θ**, but in the current toy setup these scalars act as diagnostics only; there is **no canonical θ-measure** and no mechanism-only selection of θ★.

## 4. Joint mech–FRW verdict: strong redundancy, no extra θ★ structure

The Stage 2 joint mech–FRW belt (summarised in `STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md` and `STAGE2_JOINT_VERDICT_v1.md`) finds that:

- Phase 3 mechanism tables and Phase 4 FRW tables are **θ-consistent** on the 2048-point grid; a joint θ-table can be built with strict alignment checks.
- FRW families (viable band, LCDM-like subsets, toy corridors, and intersections) are **faithfully reproduced** in the joint grid, with mechanism scalars attached pointwise.
- Simple joint correlations show that **mechanism-derived scalars are highly redundant with FRW scalars**:
  - |r| is close to 1 for several pairs of FRW and mechanism scalars,
  - FRW vacuum-sector scalars and mechanism amplitudes share nearly identical correlation patterns,
  - effective age `age_Gyr` anti-correlates with vacuum-like scalars as expected, and mechanism scalars mirror this.

This supports a precise qualitative verdict:

- In the current toy configuration, Phase 3 amplitudes are effectively a **reparameterisation of the FRW vacuum sector** on the joint θ-grid.
- The combined mech–FRW space exhibits **no additional structure beyond FRW** that would, by itself, support a special θ★ or a canonical θ-measure.

Joint verdict (current snapshot): the mechanism and FRW sectors are **tightly coupled and redundant** on the sampled grid; there is **no joint signature** that elevates θ★ or breaks the redundancy into a new axis of variation.

## 5. θ★ verdict: inside the band, not selected

The dedicated θ★ rung (together with FRW, mech, and joint belts) establishes that:

- θ★ (numerically close to φ^φ) lies **inside the FRW-viable band** on the current grid; the toy FRW universe at θ★ is viable in the structural sense defined by Phase 4.
- θ★ is **not excluded** by any present FRW sanity or data-like probes (the data gate is closed for all θ, not selectively).
- In both FRW and mechanism marginals, and in the joint mech–FRW space, θ★ behaves like a **typical viable point**, not an outlier or an extremum of any currently tracked scalar.

θ★ verdict (current snapshot): the current mechanism+FRW machinery **does not select or rule out θ★**; θ★ remains a live hypothesis that is neither favoured nor disfavoured by the present toy setup. This is recorded explicitly as a **negative-result sanity check**, not as a hidden prediction.

## 6. Program-level interpretation of Stage 2

Taken together, the Stage 2 belts support the following program-level interpretation:

- The Origin-Axiom non-cancellation mechanism (Phase 3) and FRW toy stub (Phase 4), as currently implemented, produce a **coherent toy universe** on a 2048-point θ-grid with:
  - a broad FRW-viable band,
  - robust corridor-style structure,
  - smooth, well-behaved mechanism-derived scalars,
  - and a clean, tightly redundant joint mech–FRW structure.
- Stage 2 shows that the current setup is **internally consistent** and numerically disciplined: there are no hidden pathologies or contradictions between mechanism outputs and FRW behavior at this level of resolution.
- Stage 2 also shows that, in this snapshot, the setup is **non-committal** about θ★ and about any canonical measure over θ:
  - no populated data-conditioned FRW corridor,
  - no unique mechanism-derived θ-measure,
  - no special θ★ signature in FRW or joint mech–FRW diagnostics.

From a Phase 5/interface perspective, Stage 2 currently backs an **Option A “non-contradiction / redundancy” story**:

- The mechanism and FRW sectors can be made to live together without obvious internal conflict.
- They generate a structurally nontrivial but still redundant toy universe.
- θ★ is not singled out by present machinery, so any future θ★ claim must come from genuinely new structure or data contact, not from reinterpreting existing Stage 2 diagnostics.

## 7. How Stage 2 should be cited and used

Until explicit promotion gates are passed:

- Phases 4 and 5 should cite Stage 2 artifacts as **diagnostic infrastructure** and **nontrivial-but-negative results**, not as discovery claims.
- When summarising the current status of the program, Phase 5 and external-facing summaries can safely say:
  - there exists a broad toy FRW viability band and nontrivial corridor structure,
  - mechanism-derived scalars are smooth, robust diagnostics and tightly correlated with FRW scalars,
  - current diagnostics do not produce a canonical θ-measure or a special θ★ selection,
  - and the FRW data gate is not yet open.

Any future change to this picture (e.g. a populated data-conditioned corridor, a canonical measure, or a nontrivial θ★ signature) must come from **new rungs and new code**, under explicit Phase 0 gates, and should be compared back to this Stage 2 master verdict as a baseline.


### Obstruction-program interpretation

Viewed through the obstruction program described in `docs/OBSTRUCTION_PROGRAM_OVERVIEW_v1.md`, the current Stage 2 belts form an initial testing spine for the idea that the universe sits near, but not on, a perfectly cancelling vacuum configuration. The FRW corridor belt shows that a broad, structured FRW-viable band exists on the θ grid; the mech/measure and joint belts indicate that mechanism amplitudes behave as smooth reparameterisations of FRW scalars at the present resolution; the empirical FRW anchor rungs exhibit small but non-empty kernels where corridor, viability, and conservative empirical boxes overlap; and the external host belts demonstrate that similar kernels can survive coarse cross-checks against independent FRW machinery. None of these results promote θ\* or the obstruction picture to a Phase-level claim, but together they summarise how far the current numerical infrastructure goes in testing that interpretation.

---

### External-style corridors: status after age band v2 (2026-01-21)

Using the external-style age band v2 helper (`external_age_corridor_v2`) we applied a genuinely constraining age-like corridor on top of the static FRW pre-data kernel. The helper operates on `age_Gyr` and selects grid points with ages in [12.0, 15.0] Gyr, interpreted as a toy external-style interval compatible with a late-time universe of order fourteen billion years old.

On the 2048-point θ grid:

- The pre-data kernel contains 1016 points (≈ 49.6% of the grid).
- The external age band v2 selects 358 points (≈ 17.5% of the grid), of which 356 lie inside the kernel (≈ 35% of the kernel).
- All 63 LCDM-like points lie inside the age band (the LCDM island is compatible with the chosen age interval).
- The intersection of the FRW toy corridor with the age band contains 156 grid points (≈ 15% of the kernel).
- The 40-point “sweet subset” that lies in the intersection of {kernel, LCDM-like band, FRW toy corridor} survives unchanged under the age band v2: `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2` = 40.

Interpretation for the obstruction program:

- Age band v2 is non-trivial: it removes a substantial fraction of both the kernel and the toy corridor, so it acts as a real filter rather than a no-op.
- Nonetheless, it does not yet provide an obstruction in the strict sense: the static FRW kernel remains non-empty and the 40-point sweet subset persists under Phase 4 viability, LCDM-like behaviour, toy FRW corridor, and external-style age band v2 simultaneously.
- At this rung, the obstruction verdict is therefore that gentle external-style age cuts of this form constrain but do not eliminate the current toy kernel or its sweet subset. Stronger or more realistic age corridors, or combinations with structure-friendly proxies, will be required before a sharper obstruction statement can be made.

This section is diagnostic and interpretive only. No Phase 0–5 contracts, FRW masks, or Stage 2 promotion gates are altered by the introduction of `external_age_corridor_v2`; any future use of age-based constraints in phase-level claims will require separate, tightly scoped promotion rungs.
