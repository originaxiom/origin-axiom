# Phase 2 Paper Contract (P2-S1)

This file is the single source of truth for Phase 2 paper structure.
Phase 2 is claims-disciplined: every claim must map to auditable artifacts and must remain within Phase 2 scope.

## Canonical spine (order is invariant)

`phase2/paper/main.tex` MUST include sections in exactly this order:

1. `sections/00_abstract.tex`
2. `sections/01_introduction.tex`
3. `sections/02_model_definition.tex`  (model + constraint + mapping definitions)
4. `sections/03_claim_C2_1_existence.tex`
5. `sections/04_claim_C2_2_robustness.tex`
6. `sections/05_claim_C2_3_frw_viability.tex`
7. `sections/06_reproducibility_and_provenance.tex`
8. `sections/07_limitations_and_scope.tex`
9. `sections/08_conclusion.tex`

Appendix block (after `\appendix`):
- `appendix/A_run_manifest.tex`   (artifact/run mapping table; may be brief but must exist)
- `sections/A_provenance.tex`     (computational provenance appendix)

## Invariants (must remain true)

### I1 — Single spine
- No alternate spines, no duplicate `\input{...}` blocks, no parallel “draft” section sets.
- If a section is replaced, the old file is deleted or moved to `_paper_backups/` and is not referenced.

### I2 — Claims mapping
- The only phase-level claims in the paper are Claim C2.1–C2.3.
- Each claim section must state:
  - The claim statement
  - The evidence artifacts (figures + run IDs)
  - The non-claim / limitation boundary

### I3 — Provenance required
- Any referenced figure must have an auditable provenance pointer:
  - `outputs/figures/<fig>.run_id.txt` OR explicit run id paths in Appendix A_run_manifest.
- The paper should never rely on “trust me” evidence.

### I4 — No physics drift during structural work
- Structural rungs may reorder, relabel, and clarify references/labels only.
- Any change that modifies claims, equations, or numerical results requires a separate rung.

## Deprecations / legacy section names

The following are legacy names and must not be reintroduced into `main.tex`:

- `sections/03_model_and_constraint.tex` (replaced by `02_model_definition.tex`)
- `sections/04_numerical_protocol.tex`   (replaced by claim-oriented narrative + reproducibility)
- `sections/05_results_scaling.tex`      (replaced by `04_claim_C2_2_robustness.tex` narrative)
- `sections/06_frw_implications.tex`     (replaced by `05_claim_C2_3_frw_viability.tex`)

If any of these exist on disk, they are considered archival-only unless explicitly restored by a dedicated rung.

## How to add a section (rare)

1) Propose a new filename and exact insertion point in this contract.
2) Update `main.tex` in one commit.
3) Add labels/refs discipline and ensure clean build.
4) Log the change in `phase2/PROGRESS_LOG.md` with the rung id.

