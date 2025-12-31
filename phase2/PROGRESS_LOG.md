# Phase 2 Progress Log

## 2025-12-26 — Phase 2 initialized
- Phase 2 folder structure created.
- Binding workflow guideline adopted (`PHASE2_WORKFLOW_GUIDE.md`).
- Phase 1 confirmed frozen; Phase 2 treats Phase 1 as interface-only.
- Scope and claims discipline established (SCOPE/CLAIMS/ASSUMPTIONS + reproducibility contract).
- Next: implement Phase 2 computational pipeline (mode-sum + sweeps + FRW wrapper) and canonical artifacts A–E.

## 2025-12-27 — Canonical figures A–E generated via Snakemake
- Implemented and verified canonical figure pipeline:
  - Fig A: residual existence (mode-sum)
  - Fig B/C/D: robustness sweeps (epsilon/cutoff/n_modes)
  - Fig E: FRW wrapper comparison
- Established provenance per run:
  - `outputs/runs/<run_id>/` contains `meta.json`, resolved params snapshot, `pip_freeze.txt`, `summary.json`, and raw arrays.
  - `outputs/figures/<fig>.run_id.txt` points to the run folder used to build the canonical figure PDF.
- Identified initial failure mode: reruns can fail if a run directory already exists (run_id collision).

## 2025-12-28 — Run-id collision hardening + “signature” based reuse
- Hardened Snakemake workflow against accidental reruns / collisions:
  - Introduced per-figure signature tracking (`outputs/figures/<fig>.sig.txt`) to decide whether to reuse an existing run.
  - Enforced strict run_id format required by `utils_meta.assert_run_id_format` (suffix `YYYYMMDDTHHMMSSZ`).
  - Ensured rules either:
    - reuse an existing run (only when signature matches and expected figure exists), or
    - generate a fresh timestamped run_id and run cleanly.
- Confirmed Fig E regeneration works cleanly after explicit cleanup and/or signature reuse.
- Paper compilation currently blocked by mismatched `\input{...}` filenames in `paper/main.tex`.
  - Decision: rebuild `paper/` cleanly after computational freeze is committed.

## Next (immediate)
- Commit the computational + workflow freeze (docs + config + scripts + Snakefile).
- Then rebuild `phase2/paper/` from scratch with filenames aligned to actual section files and canonical figure names A–E.