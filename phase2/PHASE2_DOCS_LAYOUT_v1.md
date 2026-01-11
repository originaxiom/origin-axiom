# Phase 2 documentation layout (Stage 2 snapshot)

Status (2026-01-11): This note classifies Phase 2 Markdown docs into canonical contracts, design and planning notes, and historical or audit material. It does not change any claims.

## 1. Canonical contracts

These files define what Phase 2 is allowed to claim and how it behaves:

- `phase2/SCOPE.md` — Phase 2 scope definition.
- `phase2/CLAIMS.md` — Phase 2 claims register (locked).
- `phase2/ASSUMPTIONS.md` — Phase 2 assumptions register.
- `phase2/CLAIMS_TABLE.md` — Phase 2 claims-to-artifacts map.
- `phase2/PHASE2_LOCK_CHECKLIST.md` — lock checklist for Phase 2.
- `phase2/APPROXIMATION_CONTRACT.md` — approximation and limitation contract.
- `phase2/REPRODUCIBILITY.md` — reproducibility and provenance rules for Phase 2 runs.
- `phase2/PHASE2_WORKFLOW_GUIDE.md` — how to run the Phase 2 pipelines.
- `phase2/PHASE2_ALIGNMENT_v1.md` — alignment memo between contracts, code, and global docs.
- `phase2/PROGRESS_LOG.md` — append-only evolution log for Phase 2.
- `phase2/README.md` — local entrypoint for Phase 2.
- `phase2/paper/PAPER_CONTRACT.md` — contract for the Phase 2 paper.

These are the files that global docs (such as `docs/PHASES.md` and `docs/CLAIMS_INDEX.md`) implicitly rely on when they talk about Phase 2.

## 2. Design and planning notes

These files record planning, structural analysis, or internal structure that help explain how Phase 2 was built and how it might be extended. They are non-binding but useful context:

- `phase2/audit/AUDIT_REPORT.md` — structural audit of Phase 2, including TODO/FIXME sweeps and references to paper backups and linting.

Design and audit notes are allowed to contain TODOs and speculative ideas, as long as they do not contradict the canonical contracts. They serve as internal guidance rather than as claims.

## 3. Historical or audit material

Historical and audit-oriented material for Phase 2 includes:

- Backed-up LaTeX sources under `phase2/_paper_backups/` and any related references from `phase2/audit/AUDIT_REPORT.md`.

These files document how the Phase 2 paper and code were audited and evolved over time. They are preserved for provenance and are not meant to be edited except when explicitly updating the audit itself.
