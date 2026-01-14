# Phases overview (Stage I)

This document gives a **human-readable map** of the Stage I program.

- It is *not* a claims index and *not* a paper.
- It should stay in **1:1 sync** with:
  - `CLAIMS_INDEX.md`,
  - `PROGRESS_LOG.md`,
  - and the phase-specific design docs under `phaseX/docs/`.

The goal is that a careful reader can understand:

1. What each phase is *trying* to do,
2. What kinds of claims are allowed there,
3. How the phases fit together into a single, reproducible ladder.

---

## Phase 0 — Ground rules, contracts, and scaffolding

**Purpose:** define the **governance, scope, and anti-hallucination contract** for the entire project.

- Fix the **Stage I** boundaries and non-goals.
- Specify what counts as a **claim**, and how it must be backed by:
  - explicit code,
  - explicit data,
  - explicit documents in the repo.
- Nail down:
  - how we log progress (`PROGRESS_LOG.md`),
  - how we manage phases (`PHASES.md`, this file),
  - how we avoid “drift” and invented details.
- Provide a **“red team” lens**: what would convince a skeptical, technically strong outsider that we are *not* just rearranging numerology.

**Allowed claim types:** meta-claims about process, scope, contracts, and governance only.

**Canonical artifacts:**

- `PHASE0_CONTRACT_v1` (PDF + source),
- `CLAIMS_INDEX.md`,
- `PHASES.md`,
- `PROGRESS_LOG.md`,
- any scripts that enforce or check Phase 0 rules.

**Status:** locked for Stage I, except for minor clarifications that improve *legibility* without changing the contract.

---

## Phase 1 — Construction of the θ-grid and baseline numerics

**Purpose:** build a **clean, reproducible θ-grid** and the minimal numerical machinery needed to:

- evaluate candidate mechanisms on that grid,
- and prepare the ground for later FRW / cosmology diagnostics.

Key tasks:

- Define a **θ-grid** (range, resolution, indexing).
- Implement baseline numerical routines that will be reused across phases.
- Fix conventions for:
  - units,
  - index ordering,
  - how θ interacts with other parameters.

**Allowed claim types:**

- purely *numerical* and *structural* statements:
  - e.g. “the θ-grid has N points, with spacing Δθ, stored in file X,”
  - or “routine Y reproduces known integral Z to within ε.”

**Canonical artifacts:**

- Phase 1 paper (PDF + LaTeX in `phase1/paper/`),
- scripts and tables under `phase1/`,
- any θ-grid reference tables used downstream.

**Status:** Phase 1 is **locked** for Stage I. Any changes must go through an explicit gate and be recorded in `PROGRESS_LOG.md`.

---

## Phase 2 — Mechanism prototypes and early filters

**Purpose:** explore and then **discipline** candidate mechanisms on the θ-grid, converging to a small set of well-behaved, reproducible constructions.

Key tasks:

- Implement candidate mechanisms (e.g. proto θ-structures) as code.
- Identify numerical and conceptual pathologies.
- Prune down to a **surviving subset** that is:
  - numerically stable,
  - conceptually coherent enough to justify promotion to Phase 3.

**Allowed claim types:**

- statements about:
  - which prototypes survive basic numerical sanity checks,
  - which prototypes are rejected and why,
  - what parameter ranges remain viable.

No FRW claims, no cosmology claims, and no “fit to data” at this stage.

**Canonical artifacts:**

- Phase 2 paper (PDF + LaTeX in `phase2/paper/`),
- mechanism tables and plots in `phase2/outputs/`,
- any documented rejections / failures (these are as important as the survivors).

**Status:** Phase 2 is **locked** for Stage I, including the final θ-grid and surviving mechanism variants exported to Phase 3.

---

## Phase 3 — Mechanism consolidation and θ-measure

**Purpose:** take the **surviving mechanisms** from Phase 2 and consolidate them into a coherent, well-defined **θ-measure / mechanism bundle** that can be used as input to FRW diagnostics.

Key tasks:

- Define **baseline** and **binding** versions of the mechanism:
  - e.g. `mech_baseline_A0`, `mech_binding_A`, etc.
- Ensure the mechanism is:
  - numerically well-behaved on the full θ-grid,
  - conceptually interpretable as a *measure-like* object.
- Introduce **corridor-style filters**:
  - define which θ lie in a “toy corridor” where the mechanism is especially well-behaved.

**Allowed claim types:**

- statements about:
  - behavior of mechanism columns over θ,
  - presence or absence of pathologies,
  - corridor definitions and their numerical properties.

Still **no FRW or data-fitting claims**: Phase 3 is mechanism-only.

**Canonical artifacts:**

- Phase 3 paper (PDF + LaTeX in `phase3/paper/`),
- mechanism tables in `phase3/outputs/`,
- corridor definitions and masks,
- any code that builds the `stage2/joint_mech_frw_analysis` inputs from Phase 3 outputs.

**Status:** Phase 3 is **near-locked**; minor corrections and clarifications are allowed but must be logged and must not change the core mechanism definitions without an explicit gate.

---

## Phase 4 — FRW toy diagnostics and host-checked corridor

**Purpose:** take the Phase 3 mechanism outputs and embed them into FRW-style toy backgrounds, then stress-test those toys with simple, **explicitly toy-level** diagnostics — including alignment tests against external FRW / ΛCDM hosts — without promoting any new cosmological claims.

**Allowed claim types:**

- purely toy-level FRW diagnostics on the θ-grid:
  - e.g. which θ-bands are FRW-viable, how ages vary with `Omega_lambda`,
- statements about internal consistency of masks and probes on the θ-grid:
  - FRW-viable sets, corridor masks, empirical anchor boxes, etc.,
- statements of the form:
  - “there exists a small θ-band where the Phase-4 FRW toy and a very simple external flat-ΛCDM host (with fixed `H0`) both assign Universe-like ages within a pre-declared window,”
- qualitative description of the associated **12-point kernel** inside the toy corridor:
  - its θ-range,
  - its `Omega_lambda` band,
  - and its narrow mechanism band,
- **no** real-data claims, no parameter estimation, and no reading of host tools as evidence *for* the axiom — they are diagnostics only.

**Canonical artifacts:**

- FRW toy design + alignment docs in `phase4/docs/`, especially:
  - `PHASE4_FRW_TOY_EQUATIONS_v1.md`,
  - `PHASE4_FRW_TOY_HEALTHCHECK_v1.md`,
  - `PHASE4_FRW_TOY_HOST_ALIGNMENT_DESIGN_v1.md`,
- FRW masks and probe tables in `phase4/outputs/tables/`,
- Stage-2 host-check snapshots in `stage2/docs/` which are **inputs/overlays**, not new claim sources:
  - `STAGE2_FRW_HOST_HX_SECTION_v1.md`,
  - `STAGE2_EXTERNAL_COSMO_HOST_RESULTS_v1.md`,
- any figures explicitly referenced by the future Phase 4 paper.

**Status:** diagnostic but non-trivial. Phase 4 is part of Stage I and remains strictly toy-level, but it now includes a concrete, host-checked FRW toy corridor and a 12-point θ-kernel that will later be surfaced as an inspectable object in Phase 5. Any widening of claims beyond this corridor/kernel description must pass through explicit future gates.

---

## Phase 5 — Interface, dashboards, and promotion gates

**Purpose:** build the **interface layer**: how a human, or a future automated system, actually *sees* and *interacts with* the previous phases.

Phase 5 is where we:

- design dashboards and figures,
- expose the θ-mechanism, FRW toys, and host overlays in a legible way,
- and define **promotion gates** for any future claim that might move beyond Stage I.

**Allowed claim types:**

- statements about interface design and visualization,
- meta-statements about what it would *take* to promote a result,
- no new physics claims. Phase 5 wraps Stage I; it does not extend it.

**Canonical artifacts:**

- Phase 5 design docs under `phase5/docs/`,
- interface prototypes and dashboards,
- any “promotion gate” specifications written in Phase-0-compatible language.

**Status:** open and exploratory, but constrained by all previous phases and the Phase 0 contract.

