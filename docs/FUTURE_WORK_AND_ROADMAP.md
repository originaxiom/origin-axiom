# Future Work and Roadmap

This document sketches how the current **Stage I (Phases 0–5)** scaffold can
support future work. It is intentionally high-level and non-committal on
specific physics claims: it focuses on **process and structure**, not promises.

---

## 1. Stage I recap: what is “done enough”

At Stage I completion, we have:

- a clear **governance layer** (Phase 0),
- toy ensembles and corridors (Phases 1–2),
- a **baseline mechanism** with diagnostics (Phase 3),
- FRW-style **toy background mappings** with viability masks (Phase 4),
- a **cross-phase interface and sanity layer** (Phase 5),
- a reproducible build path to canonical Phase PDFs and core tables.

This is sufficient to treat Stage I as a **fixed reference experiment**:
later work should be able to say “we used the Stage I program as defined by
commit X and generated the following additional results”.

---

## 2. Possible Stage II directions

Note: **Stage II** (future phases beyond Stage I) is distinct from the
existing **Stage 2** diagnostic belts under `stage2/`, which are already
implemented and remain non-canonical.

### 2.1 Data-aware FRW probes (Phase 6?)

One natural next step is to use the existing **FRW toy infrastructure** more
fully:

- populate `phase4/data/external/frw_distance_binned.csv` (or a successor
  structure) with real or mock data,
- define a new phase (e.g. **Phase 6**) that:
  - takes the Stage I viability masks and FRW summary as input,
  - performs toy comparisons or constraints using the distance data,
  - clearly separates “data-aware toy results” from the baseline Stage I
    outputs.

Key design constraints:

- Stage I should remain valid and reproducible **without** the data.
- The data-aware phase must not silently rewrite the meaning of the Stage I
  artifacts.

### 2.2 Richer mechanism diagnostics (Phase 3.x / 7?)

Another direction is to push the **mechanism-side analysis** further:

- spectral diagnostics of the ensembles,
- stability under more complex perturbations,
- exploration of alternative but related mechanisms that still respect the
  Phase 0 governance.

This could be done as:

- additional rungs within Phase 3, or
- a new Phase 7 that consumes Phase 3 artifacts and publishes its own
  diagnostics and paper.

The exact packaging can be decided later; the important thing is to maintain
the “claims + artifacts + reproducibility” triad.

### 2.3 Toward microphysics or field embeddings

Longer-term, one could explore:

- toy field-theory embeddings where the non-cancelling residue appears as an
  effective parameter,
- many-body or condensed-matter-style constructions that mirror some aspects
  of the mechanism.

These should be treated as **experiments built on top of Stage I**, not as
retroactive justifications. Any successes or failures here would be logged as
new phases with their own claims tables and artifacts.

---

## 3. Software and infrastructure evolution

On the software side, future work might include:

- a more ergonomic **Python package** structure for the mechanism and FRW
  mapping routines,
- simple **CLI tools** that wrap common tasks (e.g. building all phases,
  generating sanity tables, checking compatibility with external data),
- CI/CD to automatically run gates and checks on new commits.

Any such changes should preserve the ability to:

- clone the repo,
- install dependencies,
- run a small number of documented commands,
- regenerate the Stage I artifacts.

---

## 4. Governance evolution

If the program grows, Phase 0 may need extensions:

- clearer versioning of “Stage” boundaries (Stage I, II, …),
- explicit rules for deprecating or superseding earlier phases,
- guidelines for external contributions.

These changes should be documented as **Phase 0 updates** with their own
claims / non-claims and migration notes.

---

## 5. How to propose and implement new work

A suggested cookbook:

1. **Write a short design note** under `docs/` describing:
   - what you want to add,
   - which existing phases or artifacts you need,
   - what new artifacts you plan to publish.
2. Choose whether it belongs as:
   - a new phase (e.g. `phase6/`), or
   - an extension rung within an existing phase.
3. Implement the code and artifacts under the appropriate `phaseN/` directory.
4. Add or update:
   - a gate script,
   - a Phase paper,
   - a claims table and reproducibility appendix.
5. Ensure the Stage I gates still pass, or write a clear migration note if
   something necessarily changes.
6. Update this roadmap document if the new work significantly alters the
   program’s structure.

---

## 6. Summary

Stage I provides a **stable backbone**: a non-cancelling mechanism, corridor
language, FRW toy mappings, and an interface layer.

Future work should:

- treat Stage I as a **fixed base experiment**,
- respect the same **claims + artifacts + reproducibility** discipline,
- extend via **new phases or rungs**, rather than by silently changing what
  existing artifacts mean.

This way, the origin-axiom program can grow without losing its internal
coherence or auditability.

---

### Stage 2 – FRW corridor axis (Rungs 1–9, doc rung)

- Implemented `stage2/frw_corridor_analysis` as a downstream axis that
  consumes Phase 4 FRW masks and corridors, defining a small set of FRW
  “families” (F1–F6) and testing their geometric properties on the θ-grid.
- Rungs 1–9 establish:
  - basic inventory of Phase 4 FRW sources,
  - boolean census of masks,
  - family definitions (viable, LCDM-like, toy corridor, intersections),
  - overlap matrix between families,
  - contiguity, stride robustness, and smoothing robustness,
  - θ\* alignment diagnostics.
- A local README documents this axis:
  - `stage2/frw_corridor_analysis/README_FRW_CORRIDORS_v1.md`
- Promotion of any FRW corridor result into phase papers is gated by:
  - `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`
  and is **not yet permitted** as of 2026-01-09.

### Stage 2 – Mechanism/measure axis (Rungs 1–6)

- Implemented `stage2/mech_measure_analysis` to inventory Phase 3 tables,
  flag measure-like candidates, and produce diagnostic summaries.
- This axis is strictly downstream and does **not** modify Phase 3/5 claims.

### Stage 2 – Joint mech–FRW axis (Rungs 1–4)

- Implemented `stage2/joint_mech_frw_analysis` to align Phase 3 mechanisms
  with Phase 4 FRW masks on a shared θ grid and compute joint diagnostics.

### Stage 2 – FRW data-probe audit (Rungs 1–2)

- Implemented `stage2/frw_data_probe_analysis` to audit the current
  data-probe hooks without promoting any data-driven claims.
