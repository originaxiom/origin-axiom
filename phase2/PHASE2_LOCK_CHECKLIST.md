# Phase 2 Lock Checklist (P2-S6)

Purpose: define the minimal “Phase 2 is locked” bar, so we stop editing/committing small changes.

## A) Paper build integrity
- [ ] `./scripts/build_papers.sh` builds Phase 2 paper cleanly.
- [ ] `bash scripts/phase2_paper_lint.sh` passes.
- [ ] `rg -n 'undefined references|Warning--empty journal|Citation .* undefined' phase2/paper/main.log phase2/paper/main.blg` returns no matches.
- [ ] `phase2/paper/main.tex` includes the canonical spine and appendices:
  - sections: 01..08 + 06_reproducibility_and_provenance
  - appendix: `appendix/A_run_manifest` and `sections/A_provenance`

## B) Provenance integrity (Claim → Figure → run_id → run folder)
- [ ] `bash scripts/phase2_verify_provenance.sh` passes.
- [ ] `phase2/paper/appendix/A_run_manifest.tex` has the auto table and `\label{app:run_manifest}`.
- [ ] Sidecars exist for all canonical figures:
  - `phase2/outputs/figures/figA_mode_sum_residual.run_id.txt`
  - `phase2/outputs/figures/figB_scaling_epsilon.run_id.txt`
  - `phase2/outputs/figures/figC_scaling_cutoff.run_id.txt`
  - `phase2/outputs/figures/figD_scaling_modes.run_id.txt`
  - `phase2/outputs/figures/figE_frw_comparison.run_id.txt`
- [ ] Each referenced run folder contains at minimum:
  - `meta.json`, `params_resolved.json`, `pip_freeze.txt`, `summary.json`

## C) Claims discipline
- [ ] Each claim section has:
  - `\paragraph{Claim (C2.x).}` one-sentence claim
  - explicit figure refs
  - explicit pointer to Appendix run manifest
  - explicit non-claims boundary sentence
- [ ] `phase2/CLAIMS.md` is the canonical claim→artifact map (paper points to it).

## D) Repo hygiene
- [ ] `phase2/.gitignore` ignores `.snakemake/`, `.DS_Store`, temp cfg sweeps.
- [ ] Paper build artifacts ignored (except policy choice for main.pdf).

## E) Commit policy (to prevent “every fart” commits)
- Rule: Only commit when ONE of these is true:
  1) A rung completed (P2-Sx), logged in `phase2/PROGRESS_LOG.md`.
  2) A script/checker added that enforces reproducibility (lint, provenance, build).
  3) A lock/release artifact added (checklist, bundle index, tag instructions).
- Otherwise: batch locally, then one rung commit.

