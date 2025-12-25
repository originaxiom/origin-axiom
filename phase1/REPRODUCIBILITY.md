# Phase 1 Reproducibility Contract

Goal: A fresh clone can reproduce all Phase-1 figures and the paper PDF via a single command.

Minimum guarantees:
1) Deterministic runs:
   - All stochastic runs must record a seed in outputs/runs/<run_id>/meta.json
2) Full provenance:
   - meta.json must include git commit hash, python version, dependency snapshot, params
3) Single-command build:
   - From repo root: `snakemake -s phase1/workflow/Snakefile -c1 all`
4) Artifact immutability:
   - outputs/runs/* are never overwritten; each run gets a unique run_id
5) Paper build is part of the pipeline:
   - paper/main.pdf is generated from LaTeX + generated figures
