# Stage 2 Obstruction Testing Spine (v1)

This document summarises how the existing Stage 2 belts and rungs act as tests of the obstruction-program reading of the Origin Axiom stack. It does not introduce new claims or promotion rules; it organises already-implemented analyses as a coherent diagnostic spine for the idea that the universe sits near, but not on, a perfectly cancelling vacuum configuration.

The obstruction program itself is documented at a conceptual level in `docs/OBSTRUCTION_PROGRAM_OVERVIEW_v1.md`. Here we stay strictly within Stage 2's downstream remit: every rung described below reads Phase 3 and Phase 4 artefacts and, where relevant, compares them to simple empirical boxes or external hosts, without changing any Phase 0–5 contracts.

## 1. FRW corridor belt as geometric test

The FRW corridor belt treats the Phase 4 FRW toy pipeline as a geometry for the non-cancelling sector. It constructs FRW viability and related masks over the θ grid and asks how robust they are under stride, contiguity, and smoothing changes. From the obstruction-program perspective, this belt tests whether a non-cancelling floor can support a broad, structured set of FRW-like backgrounds rather than forcing a single fine-tuned θ value.

Key qualitative outcomes are:

- a non-trivial FRW-viable band that occupies a substantial fraction of the θ grid;
- corridor families that remain contiguous and robust under reasonable variations in sampling and smoothing;
- θ\* lying inside the broad viable band but not being singled out by the current corridor machinery.

These facts are compatible with the obstruction picture: the non-cancelling floor admits a flexible FRW-like geometry, but the present constructions do not yet select a unique θ.

## 2. Mech/measure and joint belts as redundancy tests

The mech/measure and joint mech–FRW belts study how Phase 3 mechanism amplitudes relate to Phase 4 FRW scalars on the θ grid. In obstruction terms, they ask whether the residual structure that prevents perfect cancellation can be treated as a reparameterisation of the vacuum sector or whether it injects new, unexpected structure.

The belts show that:

- certain Phase 3 amplitudes behave as smooth, well-controlled diagnostics over θ, suitable for use as weights or measures in downstream analyses;
- strong correlations exist between FRW scalars such as vacuum-sector parameters and the mechanism amplitudes, indicating a high degree of redundancy at the current resolution;
- no hidden anomaly or special feature emerges at θ\* in these diagnostics.

For the obstruction program, this is a negative-result sanity check: the current toy implementation behaves like a consistent reparameterisation of the FRW sector rather than a source of surprises. It suggests that any deeper obstruction structure, if present, would have to show up in more refined settings or in contact with data.

## 3. Empirical FRW anchor as coarse data contact

The empirical FRW anchor rungs introduce conservative empirical boxes for FRW quantities and ask whether there exist θ points that are simultaneously:

- FRW-viable in the toy pipeline,
- inside the obstruction corridor defined on the θ grid,
- and compatible with the selected empirical box.

The key qualitative result is the existence of a small but non-empty kernel of θ points that satisfy all three sets of constraints. This kernel is structured rather than accidental: it lives in narrow ranges of the FRW and mechanism scalars and typically occupies more than a single θ point while still being a tiny fraction of the full grid.

In obstruction language, this says that the non-cancelling corridor is not immediately ruled out by rough contact with large-scale expansion data as encoded in the chosen empirical box. The kernel is not yet treated as a prediction or as evidence for θ\*; it is an existence proof that the obstruction corridor has room to survive first contact with observation.

## 4. External FRW and cosmology hosts as cross-checks

The external FRW and cosmology host belts treat the Origin Axiom FRW and mechanism pipelines as proposal generators and compare them to independent background solvers and parameterisations. They construct host-side grids, define simple age-based and vacuum-sector anchors, and check whether non-empty kernels appear when the Origin Axiom proposals are passed through these hosts.

The results show that:

- the toy FRW pipeline is not trivially calibrated to any particular external host; there are clear quantitative differences in age and related quantities;
- nonetheless, under conservative mapping choices, small but non-empty kernels can appear that are compatible with both the Origin Axiom corridor and simple host-side constraints;
- these kernels are again structured and occupy specific regions of the θ grid.

For the obstruction program, these belts test whether the notion of a non-cancelling corridor is robust under changes of language: if the obstruction picture is merely an artefact of one particular toy FRW implementation, it should fail quickly under external hosts. The current belts suggest that the picture survives at least coarse cross-checks, while still leaving ample room for refinement.

## 5. Status and non-claims

Interpreting these belts as an obstruction testing spine is deliberately modest.

- No belt currently promotes θ\* to a unique or preferred value.
- No belt claims that the present empirical kernels are sufficient to declare success; they are treated as existence proofs and sanity checks.
- No belt promotes its findings into Phase 3, 4, or 5 claims; all results remain Stage 2 diagnostics unless and until they pass through explicit Phase 0 gates.
- Negative results, such as empty masks or strong redundancies between mechanism and FRW quantities, are recorded as valuable information about how the obstruction picture must evolve if it is to remain viable.

The purpose of this document is purely organisational: to make it clear how the existing Stage 2 machinery already bears on the obstruction program and where future Stage II work will need to sharpen or challenge that picture.
