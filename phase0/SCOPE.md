# Phase 0 – Scope and Non-claims

Phase 0 defines the **governance and method layer** for the Origin Axiom program.

## In scope

- Claim taxonomy and phase contracts.
- Definition and schema of theta-filters and corridors.
- Reproducibility, provenance, and archive/deprecation policies.
- Formalization of Phase 0 claims P0-C01–P0-C07 and their evidence.

## Out of scope (non-claims)

Phase 0 **does not**:

- make any statements about the physical correctness of the residue mechanism,
- fix any specific value of \(\theta_\star\),
- interpret numerical results from Phase 1 or Phase 2.

All physics-adjacent claims are delegated to Phase 1+ under the Phase 0 contracts.
---

## Companion docs: governance, reproducibility, and paper

For readers who want more detail on how this Phase 0 scope is implemented and
governed, the following documents are relevant:

- `README.md` (in `phase0/`) provides a Phase 0–specific overview of the
  governance role of this phase and how it constrains the rest of the program.

- `REPRODUCIBILITY.md` (in `phase0/`) records the Phase 0 reproducibility
  contract, including how Phase 0 artifacts are produced and how future phases
  are expected to reference Phase 0 contracts.

- `docs/ARCHIVE.md` and `docs/GATES_AND_STATUS.md` describe the global archive
  policy, gate semantics, and status labels (canonical vs Stage 2 vs archived)
  that Phase 0 enforces across the repo.

- `docs/THETA_ARCHITECTURE.md` explains how θ-like parameters, admissible
  corridors, and their intersections are treated across the program under the
  Phase 0 contracts.

- `artifacts/origin-axiom-phase0.pdf` (at the repo root) is the consolidated
  Phase 0 paper built from `phase0/paper/main.tex`. This scope document should
  be read together with that paper and `phase0/CLAIMS.md` to understand what
  Phase 0 does and does not assert.
