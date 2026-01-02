# Phase 0 — PROGRESS_LOG

This log tracks Phase 0 (contracts): definitions, claim taxonomy, corridor schema, reproducibility requirements, and failure modes.
Phase 0 is the governance layer for all subsequent phases.

## 2026-01-01
- Confirmed repo cleanup: Snakemake cache and LaTeX artifacts removed from tracking; outputs/runs ignored going forward.
- Locked `.gitignore` policies for reproducible outputs vs ephemeral runs.
- Began Phase 0 completion:
  - Added `phase0/paper/main.tex`, `phase0/paper/macros.tex`, `phase0/paper/references.bib`, and `.latexmkrc` so Phase0 paper compiles.
- Next:
  - Compile Phase0 paper and commit the generated `phase0/paper/main.pdf` (or decide an `phase0/artifacts/` convention).
  - Add repo-wide documentation spine: `ROADMAP.md`, `CLAIMS_INDEX.md`, root `REPRODUCIBILITY.md`.
