# Phase 3 documentation layout (Stage 2 snapshot)

Status (2026-01-11): This note classifies Phase 3 Markdown docs into canonical contracts, design and planning notes, and historical or audit material. It does not change any claims.

## 1. Canonical contracts

These files define Phase 3 as the mechanism module and specify what it claims:

- `phase3/MECHANISM_CONTRACT.md` — Phase 3 mechanism contract and status; primary description of the mechanism phase.
- `phase3/SCOPE.md` — Phase 3 scope.
- `phase3/ROLE_IN_PROGRAM.md` — Phase 3 role in the overall program.
- `phase3/REPRODUCIBILITY.md` — reproducibility and provenance for Phase 3 pipelines.
- `phase3/PHASE3_ALIGNMENT_v1.md` — alignment memo connecting contracts, code, and global docs.
- `phase3/PROGRESS_LOG.md` — append-only Phase 3 progress log.

The detailed mechanism claims live partly in `phase3/MECHANISM_CONTRACT.md` and partly in the Phase 3 paper (`artifacts/origin-axiom-phase3.pdf`), which is audited in `stage2/docs/STAGE2_PAPER_AUDIT_PHASE3_v1.md`.

## 2. Design and planning notes

These files provide internal design structure and rung-level detail for Phase 3:

- `phase3/design/PHASE3_NEXT_RUNG.md` — Phase 3 next-rung design and planning.
- `phase3/design/PHASE3_RUNG2_MECHANISM_A_INSTABILITY_PENALTY.md` — rung-level design for the instability penalty and related diagnostics.

Design documents spell out how the mechanism is explored and extended but do not themselves change the mechanism contract or claims unless reflected in `MECHANISM_CONTRACT.md` and the alignment memo.

## 3. Historical or audit material

Historical and audit-oriented material related to Phase 3 includes:

- Archived flavor experiment (lives under `experiments/`, not `phase3/`):
  - `experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md` and related Phase 3 flavor files.

These preserve the history of Phase 3 exploratory flavor work and audits but are non-canonical. Changes to these areas are logged through their own status docs and global archive maps (`stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`).
