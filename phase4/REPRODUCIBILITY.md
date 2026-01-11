# Phase 4 Reproducibility Plan (Draft)

Status: **DRAFT – no gate implemented yet.**

This document sketches how Phase 4 is expected to meet the reproducibility
standards set by Phase 0. It will be updated once the concrete workflows
and gates are defined.

## 1. Expected directory and workflow structure

Phase 4 is expected to mirror the structure of earlier phases:

- `phase4/src/` – implementation of mappings, FRW modules, diagnostics.
- `phase4/outputs/` – tables, figures, theta-filter artifacts (if any).
- `phase4/artifacts/` – canonical Phase 4 PDF (paper) and key artifacts.
- `phase4/paper/` – LaTeX source for the Phase 4 paper.
- `phase4/workflow/` – Snakemake `Snakefile` for Phase 4 gate.
- `scripts/phase4_gate.sh` – shell wrapper for Phase 4 gate, similar to
  other phases.

These paths are indicative and may be refined when Phase 4 is
implemented.

## 2. Gate levels (anticipated)

We anticipate a Phase 4 gate with at least:

- **Level A (paper only)**:
  - Rebuilds the Phase 4 paper PDF from source.
- **Level B (paper + core artifacts)**:
  - Regenerates any tables, figures, and θ-filters declared as binding
    outputs of Phase 4.

Exact definitions will be added once the phase is implemented.

## 3. Run manifests and logs

Phase 4 should:

- Maintain a `phase4/PROGRESS_LOG.md` with rung-style entries.
- Maintain any run manifests required to track heavy runs or parameter
  sweeps.
- Clearly separate:
  - light, deterministic runs (rebuild easily at gate levels); and
  - heavy or optional runs (documented, but possibly not required at
    gate time).

## 4. Interaction with the Phase 0 ledger

If Phase 4 produces a θ-filter artifact, it must:

- Have a clear schema;
- Be ingestible by the Phase 0 ledger without invoking Phase 4 internals;
- Be accompanied by documentation that states precisely:
  - how the filter was derived;
  - which runs / configurations it depends on.

This file will transition from **draft** to **locked** once the actual
Phase 4 implementation and gate are in place.

---

Doc status: Draft Phase 4 reproducibility plan; describes how FRW tables and figures are to be generated once Phase 4 is locked; current FRW reproducibility is effectively governed by Phase 3 contracts, Phase 4 code, and Stage 2 FRW/joint verdicts as summarised in `phase4/PHASE4_ALIGNMENT_v1.md` and `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`.
