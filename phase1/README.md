# Phase 1: Minimal Origin Axiom Core

This folder contains the Phase-1 deliverable: θ*-agnostic minimal axiom + toy proofs + reproducible figures + paper.

## Quickstart (Phase 1)
From repo root:

```bash
uv venv
source .venv/bin/activate
uv pip install -e ".[phase1]"
snakemake -s phase1/workflow/Snakefile -c1 all
