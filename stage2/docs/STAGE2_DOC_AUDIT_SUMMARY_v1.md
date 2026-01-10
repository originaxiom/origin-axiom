# Stage 2 Documentation Audit — Summary (v1)

This note records the first Stage 2 documentation audit over the main `origin-axiom` repository after the Codex-assisted doc cleanup in early 2026. It is downstream-only and does not change any Phase claims by itself.

The audit was performed by running a Stage 2 doc-audit belt that produced four CSV inventories under `stage2/doc_audit/outputs/tables/` (or an equivalent location):

- `stage2_doc_inventory_v1.csv` — flat inventory of `.md`, `.tex`, and related doc files, with basic metadata (paths, sizes, type).
- `stage2_doc_broken_refs_v1.csv` — candidate broken references (documents pointing at files, sections, or paths that do not exist in the current repo layout).
- `stage2_doc_orphan_candidates_v1.csv` — candidate “orphan” docs (files that are not referenced from the main documentation graph and may be legacy, experimental, or superseded).
- `stage2_doc_open_threads_v1.csv` — explicit open threads and TODO-style markers discovered in docs (places where the text itself declares missing sections, future work, or stubs).

None of these CSVs are binding by themselves; they are diagnostic snapshots. A given line may be:

- a true discrepancy that deserves a patch,
- a harmless legacy note that should be explicitly archived,
- or an intentional stub (for example, a placeholder section in a future Phase paper).

### How to use this audit

1. Use `stage2_doc_inventory_v1.csv` as a map when deciding where to apply documentation patches or where to move / retire files.
2. For each candidate issue in `stage2_doc_broken_refs_v1.csv` and `stage2_doc_orphan_candidates_v1.csv`, make an explicit decision:
   - **Fix** the reference or wiring,
   - **Archive** the doc (with a banner and a pointer from `docs/LEGACY_MIGRAIONS_PHASE0_MAP.MD`),
   - or **Accept** the discrepancy as intentional and record that acceptance in the relevant doc.
3. Treat `stage2_doc_open_threads_v1.csv` as a queue of explicitly declared TODO threads. When a thread is closed, update the source document and (optionally) annotate that it has been addressed in the log.

### Status

As of 2026-01-10 this audit is:

- Stage 2 / diagnostic only,
- downstream of the main Phase documents,
- and ready to be re-run in future rungs to check that new edits did not reintroduce contradictions.

