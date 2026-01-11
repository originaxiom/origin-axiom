# Stage 2: Documentation Audit (Summary, 2026-01-09)

## Scope and intent

This document summarizes a Stage 2 documentation audit over the markdown, LaTeX, and related narrative files in this repository. The goal is to make the doc layer as disciplined as the code and phase gates: every major text should either be clearly canonical, clearly archived, or clearly marked as a live thread.

This audit is **diagnostic only**. It does not automatically change any claims or phase statuses. All edits are applied manually and gated in the same way as other Stage 2 work.

## Inputs and artifacts

The audit produced four primary CSV artifacts (living under the Stage 2 doc-audit outputs):

- `stage2_doc_inventory_v1.csv`: inventory of all scanned narrative documents, with file paths, rough categories, and simple metadata.
- `stage2_doc_broken_refs_v1.csv`: static cross-reference checks (missing files, missing sections, obviously broken links).
- `stage2_doc_orphan_candidates_v1.csv`: documents that appear never to be referenced by any other doc, sorted by likely importance.
- `stage2_doc_open_threads_v1.csv`: lines and sections that look like open TODOs, stubs, or unresolved “future work” notes.

These tables are meant to be **reproducible snapshots**. Re-running the audit with updated scripts will refresh them; this summary remains a human-readable explanation of what those tables mean.

## High-level findings from this run

This particular audit run (2026-01-09) saw on the order of a few hundred narrative files across the repo. At a coarse level:

- The top-level narrative has been largely aligned: `README.md`, `docs/PHASES.md`, `docs/STATE_OF_REPO.md`, `docs/CLAIMS_INDEX.md`, and `docs/PROJECT_OVERVIEW.md` now agree that:
  - Phase 3 is the **mechanism module** (with flavor work archived under `experiments/phase3_flavor_v1/`, non-canonical).
  - Phase 4 and Phase 5 exist as **toy FRW diagnostics** and an **interface/sanity layer**, not as grand “fit everything” pipelines.
  - Stage 2 lives under `stage2/` as a set of **diagnostic belts** that are downstream of Phase 3/4 and non-canonical until explicitly promoted.
- The audit found **no remaining hard broken references** in the scanned doc set at this rung (the broken-refs table is empty for this run). Any future broken links will show up automatically when the audit is re-run.
- A substantial number of files are flagged as **orphan candidates**: internal notes, older sketches, and small design documents that are not obviously linked from the main narrative. Some of these will be:
  - kept but explicitly marked as archived or legacy,
  - integrated by adding proper links from canonical docs,
  - or retired if they no longer reflect the program.

The open-threads table collects scattered “TODO”, “TBD”, “stub”, or “this needs to be checked later” markers into one place, so that Stage 2 work can either resolve them or explicitly park them behind a gate.

## How this ties into the phases and Stage 2

Within the phased program:

- **Phase 0–5** remain the canonical skeleton: governance, toy ensembles, mode-sum and bounded FRW diagnostics, mechanism module, FRW toy diagnostics, and interface/sanity layer.
- **Stage 2** is where repo-wide hygiene and diagnostics live:
  - FRW corridor analysis (`stage2/frw_corridor_analysis`)
  - Mechanism/measure analysis (`stage2/mech_measure_analysis`)
  - Joint mech–FRW analysis (`stage2/joint_mech_frw_analysis`)
  - FRW data-probe audit (`stage2/frw_data_probe_analysis`)
  - Documentation audit (this module)

The documentation audit is **strictly downstream**: it reads files and tables, but it does not modify or reinterpret any physics claims on its own. All changes must be applied manually and logged through the usual git and progress-log gates.

## Recommended usage

- When preparing a publication-grade pass over any phase:
  - consult `stage2_doc_open_threads_v1.csv` for unresolved narrative threads,
  - check `stage2_doc_orphan_candidates_v1.csv` for relevant orphan docs that should be either linked, archived, or retired.
- When changing the repo structure:
  - re-run the doc-audit scripts to regenerate the four CSVs,
  - update this summary only if the **shape** of the audit changes (for example, new categories, new tables, or a qualitatively different status).

The intent is that an external collaborator can read this file plus the four CSVs, and quickly understand where the documentation is tight, where it is loose, and which follow-up Stage 2 rungs should be executed next.

---

## 5. Doc-audit status as of 2026-01-11

As of 2026-01-11, several small, targeted doc-audit rungs have been applied
manually on top of the CSV snapshots described above:

- **Stage 2 belt summaries wired up.**  
  The Stage 2 FRW corridor, mech/measure, joint mech–FRW, and FRW data-probe
  belts now each have a short summary document under `stage2/docs/`:
  `STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`,
  `STAGE2_MECH_MEASURE_SUMMARY_v1.md`,
  `STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`, and
  `STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md`. These close previously broken README
  links and make the belts directly navigable.

- **Repo atlas added and linked.**  
  A high-level repo atlas (`docs/REPO_MAP_AND_ATLAS_v1.md`) now records the
  directory-level layout of phases, Stage 2 belts, experiments, sandbox areas,
  and build/gate scripts. README and `docs/STATE_OF_REPO.md` both point to this
  atlas as a navigation aid.

- **Doc-audit working directory clarified.**  
  References to the git-ignored `stage2/doc_repo_audit/` working directory were
  updated so that readers are directed to
  `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` for instructions, rather than
  into 404-prone paths on GitHub. The audit scratch directory is now clearly
  described as a local, transient workspace.

- **Governance and θ architecture docs promoted.**  
  Previously under-linked governance docs (`docs/ARCHIVE.md`,
  `docs/GATES_AND_STATUS.md`, `docs/THETA_ARCHITECTURE.md`,
  and `docs/LEGACY_MIGRAIONS_PHASE0_MAP.MD`) have been wired into
  `docs/STATE_OF_REPO.md`, `docs/PROJECT_OVERVIEW.md`, `docs/ARCHIVE.md`, and
  the repo atlas so they are treated as first-class companions instead of
  orphans.

- **FRW promotion gate and Phase 5 roadmap surfaced.**  
  The FRW corridor promotion gate (`docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`)
  and the Phase 5 roadmap (`docs/phase5_roadmap.md`) are now linked from
  `docs/STAGE2_PROMOTION_DESIGN_v1.md` and
  `docs/FUTURE_WORK_AND_ROADMAP.md`, clarifying the governance context for any
  future Stage 2 → Phase 4/5 promotions.

- **Stage 2 overview and joint plan connected.**  
  Higher-level Stage 2 design docs (`docs/STAGE2_OVERVIEW.md`,
  `docs/STAGE2_JOINT_MECH_FRW_PLAN_v1.md`, and
  `docs/STAGE2_MECH_MEASURE_RUNG1_6_SUMMARY_v1.md`) are now referenced from the
  Stage 2 belt overview and the repo atlas, so readers can find the conceptual
  Stage 2 top layer from both the global docs and the belt-level docs.

The remaining work implied by the CSVs includes:

- further cleanup of broken references in less central docs,
- decisions about genuinely orphaned or superseded documents (promote vs archive),
- and selective closure or relocation of open TODO/TBD-style threads in
  Phase/Stage docs.

Those future rungs will be logged in `PROGRESS_LOG.md` and, where appropriate,
reflected back into this summary document.

---

## 6. Jan 2026 Stage 2 doc-audit sprint (snapshot)

Between 2026-01-09 and 2026-01-11 a focused Stage 2 documentation and repo-audit
sprint was applied, using the doc-audit CSVs as guidance. At a high level this
sprint:

- **Strengthened navigation and mapping.**  
  - Introduced `docs/REPO_MAP_AND_ATLAS_v1.md` as a directory-level map and
    wired it into `README.md`, `docs/STATE_OF_REPO.md`, and
    `docs/INTERACTING_WITH_REPO.md`.
  - Added a README “Where to start reading” section aligned with the atlas,
    Stage 2 overviews, and Phase PDFs.
  - Surfaced the root `REPRODUCIBILITY.md` as a reproducibility entrypoint.

- **Clarified Stage 2 belts and doc-audit role.**  
  - Ensured `docs/STAGE2_OVERVIEW.md`, `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`,
    and `docs/STAGE2_PROMOTION_DESIGN_v1.md` all explicitly describe Stage 2 as
    a downstream diagnostic layer with a dedicated documentation/repo-audit belt.
  - Linked the belt overview to the repo-audit checklist in `docs/REPRODUCIBILITY.md`
    and recorded the doc/audit belt in `docs/STATE_OF_REPO.md` and
    `docs/ARCHIVE.md`.

- **Phase-local companion docs and design notes.**  
  - Added companion-doc sections to `phase0/`–`phase5/` SCOPE files and to key
    Phase 3/4 docs so that scope/overview pages point directly to their local
    contracts (SCOPE/CLAIMS/NON_CLAIMS/REPRODUCIBILITY), papers under
    `artifacts/`, and relevant Stage 2 belts.
  - Marked Phase 4 design documents (`PLANNING.md`, `HARD_NOVELTY_ROADMAP.md`)
    as draft, non-binding planning notes that do not override Phase 4 scope or
    claims and are governed by the FRW promotion gate and Phase 4 promotion
    design.

- **Archive and experiment boundaries.**  
  - Tightened archive labelling by connecting `docs/ARCHIVE.md` with
    `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`.
  - Marked `experiments/phase3_flavor_v1/SCOPE.md` explicitly as archived and
    pointed readers back to canonical Phase 3 mechanism documents under
    `phase3/`.

- **Audit process visibility.**  
  - Added a Stage 2–aware repo-audit checklist to `docs/REPRODUCIBILITY.md`.
  - Recorded these rungs in `PROGRESS_LOG.md`, so the evolution of the
    documentation surface is itself auditable.

This sprint should be treated as a snapshot: future structural changes (new
phases, new belts, significant reshuffling) may require re-running the Stage 2
doc-audit scripts and adding further rungs. The CSVs in this directory capture
the state at the time they were generated; `PROGRESS_LOG.md` records subsequent
manual documentation rungs that build on them.
