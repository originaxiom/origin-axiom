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
### 2026-01-03 — Baseline freeze for Phase 2 paper rebuild + rewrite

Action:
- Start alignment pass; Phase 2 paper will be rebuilt to match Phase 1 rigor and Phase 0 governance.
- Confirmed status: Phase 2 computational artifacts + claims mapping exist; paper build currently blocked by mismatched \\input filenames in paper/main.tex (structural issue).

Next:
- Stage 3 will (1) fix paper structure (inputs/duplicates), then (2) rewrite text to be unambiguous and scope-tight, mapping every claim to figs A–E + run provenance.

## 2026-01-04 — Phase 2 Structural Spine Lock (P2-S1): paper contract + invariants
- Added canonical paper contract: `phase2/paper/PAPER_CONTRACT.md` defining the single Phase 2 spine and invariants.
- Confirmed claims-first ordering is the canonical main spine (C2.1–C2.3) with reproducibility + limitations before conclusion.
- Added/confirmed Phase 2 paper `.gitignore` to prevent tracking LaTeX artifacts and draft `main.pdf`.
- Structural-only rung: no new claims, no equation/result changes intended.

## 2026-01-04 — Phase 2 Compactification (P2-C1): hygiene + deterministic build entrypoint
- Added `phase2/.gitignore` to ignore OS junk, Snakemake runtime cache, and temporary sweep config folders.
- Confirmed repo build entrypoint includes Phase 2: `scripts/build_papers.sh` builds `phase2/paper/main.tex`.
- No scientific content changed; organizational/hygiene only.

## 2026-01-04 — Phase 2 Stage 1 (P2-S1): paper contract + spine invariants
- Added `phase2/paper/PAPER_CONTRACT.md` defining the canonical Phase 2 claims-first spine and invariants.
- Locked duplicate-prevention rules (unique section filenames, single appendix entry, run-manifest label).
- No scientific content changed; structural guardrails only.

## 2026-01-04 — Phase 2 Stage 1 (P2-S2): claims map hardening (CLAIMS → paper → artifacts)
- Added `phase2/CLAIMS_TABLE.md` as the canonical claim-to-artifacts map (C2.1–C2.3).
- Added verifier `scripts/phase2_verify_claims_map.sh` enforcing:
  - required paper figures exist,
  - run_id sidecars exist and are non-empty,
  - meta.json exists per run_id and contains provenance hints,
  - appendix run-manifest label is present.
- No scientific content changed; auditability/traceability only.

## 2026-01-04 — Phase 2 Stage 1 (P2-S3): provenance enforcement for paper-referenced artifacts
- Added `scripts/phase2_verify_provenance.sh` enforcing that every paper figure (A–E) has:
  - a non-empty `outputs/figures/<fig>.run_id.txt`,
  - a corresponding `outputs/runs/<run_id>/` directory,
  - required files: `meta.json`, `params_resolved.json`, `pip_freeze.txt`, `summary.json`, and `figures/` folder.
- Auto-generated Appendix run manifest table inside `paper/appendix/A_run_manifest.tex` from current run_id sidecars.
- Rebuilt `phase2/paper/main.tex` and confirmed clean build post-change.
- No new scientific claims; this rung hardens auditability and provenance completeness.

## 2026-01-04 — Phase 2 Stage 1 (P2-S4a): structure-first rewrite pass (abstract + spine invariants)
- Fixed Phase 2 paper spine so the abstract is sourced solely from `paper/sections/00_abstract.tex` (included inside the `abstract` environment).
- Removed redundant `\input{sections/00_abstract}` from the main section spine to prevent duplicate/placeholder abstracts.
- Added `scripts/phase2_paper_lint.sh` to enforce: no TODO/FIXME/XXX/TBD in Phase 2 paper, and clean build log scan.
- Rebuilt `phase2/paper/main.tex`; confirmed clean logs post-change.
- No new claims; structure-only hygiene to prevent drift.

## 2026-01-04 — P2-S5.2: Paper ↔ CLAIMS map pointer (claims-to-artifacts hard link)
- Added a single canonical pointer in `paper/sections/06_reproducibility_and_provenance.tex` directing readers to `phase2/CLAIMS.md` for the Claim C2.1–C2.3 → artifact mapping.
- Kept Appendix run manifest (`appendix/A_run_manifest.tex`) as the per-figure run_id index.
- Rebuilt Phase 2 paper; no new scientific claims introduced.

## 2026-01-04 — P2-S6: Lock prep checklist + commit batching rule
- Added `PHASE2_LOCK_CHECKLIST.md` to define a concrete “Phase 2 locked” bar (build, lint, provenance, claims discipline, hygiene).
- Added an explicit commit policy: commit only per-rung / reproducibility enforcement / lock artifacts, not micro-edits.
