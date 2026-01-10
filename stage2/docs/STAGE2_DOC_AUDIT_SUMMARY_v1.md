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
