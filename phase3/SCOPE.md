
---

## Companion docs: mechanism contract, role, reproducibility, and paper

For readers who want more detail on how this Phase 3 scope is realised in the
code, diagnostics, and paper, the following documents are relevant:

- `README.md` (in `phase3/`) provides a Phase 3–specific overview of the
  mechanism module and how it sits between the Phase 2 bounded vacuum-floor
  implementation and the Phase 4 FRW-facing diagnostics.

- `MECHANISM_CONTRACT.md` records the Phase 3 mechanism contract, including the
  non-cancellation floor, amplitude diagnostics, and binding regimes that define
  the canonical Phase 3 module.

- `ROLE_IN_PROGRAM.md` explains how Phase 3 fits into the broader Origin Axiom
  ladder, and which questions the mechanism module is allowed to ask (and not
  ask) relative to Phase 2 and Phase 4.

- `PHASE3_RUNG2_MECHANISM_A_INSTABILITY_PENALTY.md` is a rung-level design note
  for the Phase 3 mechanism A instability penalty. It refines the internal
  design and diagnostics but does not extend the Phase 3 scope or claims on its
  own.

- `REPRODUCIBILITY.md` (in `phase3/`) records the Phase 3 reproducibility
  contract, including how to run the mechanism workflows and how the tables
  under `phase3/outputs/` are generated.

- `artifacts/origin-axiom-phase3.pdf` (at the repo root) is the consolidated
  Phase 3 paper built from `phase3/paper/main.tex` and the Phase 3 outputs. This
  scope document should be read together with that paper and `phase3/CLAIMS.md`
  to understand what Phase 3 does and does not assert.

---

Alignment memo: For a current alignment between Phase 3 scope, mechanism contract, claims, reproducibility docs, the Phase 3 mechanism paper, and Stage 2 mechanism/joint diagnostics, see `phase3/PHASE3_ALIGNMENT_v1.md`.
