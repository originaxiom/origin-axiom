# Stage 2 doc open-threads status (TODO / DRAFT / historical markers)

Status (2026-01-11): This document interprets the open-thread markers surfaced by the Stage 2 doc-audit belt (TODO / DRAFT / TBD / FIXME patterns) and classifies them as live, draft-only, or historical. It is descriptive only and does not change any phase contracts or claims.

## 1. Inputs

This status note is based on:

- `stage2/doc_repo_audit/outputs/tables/stage2_doc_open_threads_v1.csv`
- The following families of files:
  - Program-level: `PROGRESS_LOG.md`
  - Phase 2 audit and contracts: `phase2/AUDIT_REPORT.md`, `phase2/PROGRESS_LOG.md`
  - Phase 3 mechanism contract: `phase3/MECHANISM_CONTRACT.md`
  - Phase 4 planning and contracts: `phase4/PLANNING.md`, `phase4/SCOPE.md`, `phase4/PHASE3_INTERFACE.md`, `phase4/CLAIMS_TABLE.md`, `phase4/MAPPING_FAMILIES.md`, `phase4/CLAIMS.md`, `phase4/NON_CLAIMS.md`, `phase4/REPRODUCIBILITY.md`, `phase4/FRW_TOY_DESIGN.md`, `phase4/PROGRESS_LOG.md`
  - Phase 2 backup references inside the Phase 2 audit report.

The goal is to decide which markers indicate live work to be done in Stage I / Stage 2 and which are intentionally preserved as historical or draft context.

## 2. Program-level PROGRESS_LOG markers

The open-threads CSV includes a `TODO` occurrence in the main `PROGRESS_LOG.md`, within a narrative sentence describing past work on physical scaling and “future real data” contact. This marker:

- is part of a descriptive summary of what would be needed in any future data-facing phase,
- does not block any current Stage I or Stage 2 belt,
- and is not an actionable TODO in the sense of “this must be done before the current snapshot is considered coherent”.

Classification: **historical / contextual**. It documents earlier thinking about possible future work but is not a live gate for the current Stage I snapshot.

## 3. Phase 2 audit report TODO cluster

The open-threads CSV flags several `TODO` lines in `phase2/AUDIT_REPORT.md`, including references to:

- an internal TODO/TBD/FIXME sweep section,
- historic copies of `phase2/PROGRESS_LOG.md`,
- historic Phase 2 paper backups under `phase2/_paper_backups/`.

In Belt C / Rung C2 we already tagged `phase2/AUDIT_REPORT.md` as a **historical audit snapshot (P2-A1)**, clarifying that:

- its TODO/TBD/FIXME references are about what was checked at that audit time,
- they are not a live to-do list for the present locked Phase 2,
- and the current Phase 2 status is governed by `phase2/CLAIMS.md`, `phase2/REPRODUCIBILITY.md`, `phase2/PHASE2_ALIGNMENT_v1.md`, and the main `PROGRESS_LOG.md`.

Classification: **historical / audit-only**. The TODO markers in `phase2/AUDIT_REPORT.md` should be read as part of a preserved audit log, not as outstanding tasks for Stage I; no further action is required unless a future Phase 2 re-audit belt is explicitly launched.

## 4. Phase 3 mechanism contract DRAFT marker

The open-threads CSV includes a `DRAFT` marker in `phase3/MECHANISM_CONTRACT.md` stating that it is a draft contract. In practice:

- Stage 2 mechanism and joint belts already treat `phase3/MECHANISM_CONTRACT.md` plus the Phase 3 paper as the effective mechanism contract,
- the Phase 3 alignment memo `phase3/PHASE3_ALIGNMENT_v1.md` interprets this contract as canonical for the current snapshot,
- and any future tightening of the Phase 3 contract will run through an explicit Phase 3 lock rung and PROGRESS_LOG entry.

Classification: **draft-but-operational**. The DRAFT label is accurate (no formal Phase 3 lock rung has been executed yet), but for Stage 2 purposes the mechanism contract is treated as the working contract and is not an open to-do item. It becomes live again only if and when a Phase 3 lock or revision is undertaken.

## 5. Phase 4 DRAFT cluster (planning, claims, mapping, non-claims, reproducibility)

The open-threads CSV shows many `DRAFT` markers across Phase 4 files:

- `phase4/PLANNING.md`
- `phase4/SCOPE.md`
- `phase4/PHASE3_INTERFACE.md`
- `phase4/CLAIMS_TABLE.md`
- `phase4/MAPPING_FAMILIES.md`
- `phase4/CLAIMS.md`
- `phase4/NON_CLAIMS.md`
- `phase4/REPRODUCIBILITY.md`
- `phase4/FRW_TOY_DESIGN.md`
- plus corresponding mentions in `phase4/PROGRESS_LOG.md`.

In Belt C / Rung C2 we explicitly tagged these as:

- **design or planning notes** (PLANNING, HARD_NOVELTY_ROADMAP, FRW_SYNTHESIS, MAPPING_FAMILIES, FRW_TOY_DESIGN, PHASE3_INTERFACE),
- and **draft-but-governed contracts** (SCOPE, CLAIMS, NON_CLAIMS, REPRODUCIBILITY), where:

  - interpretation is governed by `phase4/PHASE4_ALIGNMENT_v1.md`,
  - FRW-related promotions must pass `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md` and `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`,
  - and Stage 2 FRW and joint verdicts currently act as a conservative “Option A” baseline.

Classification: **draft / design, not live blocking work**. The DRAFT markers here correctly indicate that Phase 4 is a stub and its contracts are not yet locked. They do not indicate errors or missing pieces in Stage I; instead, they are guardrails that will become live only when a dedicated Phase 4 lock and promotion belt is run. For the current snapshot, these DRAFT markers are intentionally preserved and interpreted through the Phase 4 alignment and promotion docs.

## 6. Phase 4 FRW toy design DRAFT marker

`phase4/FRW_TOY_DESIGN.md` is explicitly marked as a draft FRW toy design note. Stage 2 FRW and joint belts now provide concrete FRW diagnostics built from the actual Phase 4 pipeline; the design note remains:

- a useful explanation of the intended FRW sandbox and corridor families,
- but not a claims-bearing or gating document.

Classification: **design note**. The DRAFT marker here is informative; it does not represent an unresolved Stage I task.

## 7. Summary of live vs historical open threads

At the current snapshot:

- There are **no open-thread markers that block or contradict** the Stage I / Stage 2 picture.
- All TODO/DRAFT markers surfaced by the doc-audit CSV fall into one of three categories:
  - **Historical / audit-only** (Phase 2 audit report, old PROGRESS_LOG context lines).
  - **Draft-but-operational contracts** (Phase 3 mechanism contract; Phase 4 SCOPE/CLAIMS/NON_CLAIMS/REPRODUCIBILITY interpreted via alignment memos and promotion gates).
  - **Design notes and planning documents** (Phase 4 planning and mapping families; Phase 5 vision).

For future work:

- If a new Phase 2 re-audit, Phase 3 lock, or Phase 4 lock belt is launched, some of these markers will become live checkpoints again under new rungs and PROGRESS_LOG entries.
- Until then, they should be treated as **documented context**, not as a list of outstanding work items that undermine the current Stage I / Stage 2 snapshot.

