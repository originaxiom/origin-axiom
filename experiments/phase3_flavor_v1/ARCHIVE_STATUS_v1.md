# Phase 3 Flavor-Sector Experiment — Archived Status (v1)

This directory contains an **archived flavor-sector experiment** that used CKM/PMNS phases to define a theta filter and corridor. It predates the current canonical Phase 3 mechanism module in `phase3/`.

## Canonical vs non-canonical

- Canonical Phase 3:
  - Lives under `phase3/` (paper, tables, mechanism code).
  - Acts as the **mechanism module**: it locks a baseline non-cancellation floor and provides binding-style diagnostics.
  - Has no flavor calibration or corridor narrowing in its canonical form.

- Archived flavor add-on (this directory):
  - Lives under `experiments/phase3_flavor_v1/`.
  - Is **non-canonical** and does not carry Phase 3 claim IDs.
  - Its outputs and claims are not part of the main Origin-Axiom ledger unless explicitly re-migrated and re-gated.

## Known limitations

- Paths and references in this experiment may still refer to old `phase3/...` locations rather than `experiments/phase3_flavor_v1/...`.
- Some configuration flags (for example, placeholder-mode toggles) may disagree with the emitted metadata in `outputs/tables/`.
- The fit and diagnostic tables here were useful historically but are not considered binding evidence in the current Phase program.

## How to use this directory

- You **may**:
  - Read this experiment as a historical record of flavor-sector attempts.
  - Mine it for ideas, ansätze, or diagnostic patterns.
- You **must not**:
  - Treat any numerical result here as a canonical Phase claim.
  - Wire this experiment directly into the Phase 2/3/4/5 gates without an explicit migration note and a new gated rung.

If a future rung reintroduces flavor-sector structure into the main program, it should:

1. Be documented in `docs/PHASES.md` and `docs/CLAIMS_INDEX.md`.
2. Declare its scope, non-claims, and artifacts.
3. Pass through the same reproducibility and locking discipline as the other Phases.

