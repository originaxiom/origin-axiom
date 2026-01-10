# Gates and Status Index

This document is the central index for the status, scope, canonical artifacts, and gates of each layer in the Origin-Axiom program.
It is descriptive, not promotional: it tells you what is currently in play, what is locked, what is under audit, and what is strictly downstream.
For any concrete claim, the phase-local contracts and claims ledgers remain the primary source of truth.

If anything here disagrees with a phase contract, non-claims document, or claims ledger, treat this file as out of date and fix it rather than silently overriding the stricter document.

---

## Summary table

| Layer                            | Scope (one line)                                                                 | Status                                  | Canonical artifacts (where)                                                                                     | Gates / non-claims (where)                                                                                           |
|----------------------------------|----------------------------------------------------------------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Phase 0 – Governance / Method    | Governance, epistemic discipline, contracts, and method claims; no physics.     | Active; effectively locked in spirit    | `phase0/` (contracts, method docs, `phase0/CLAIMS.md`).                                                          | Phase 0 contract and method claims in `phase0/CLAIMS.md`; repo-wide anti-hallucination and gate rules.               |
| Phase 1 – Toy Ensembles          | Toy-domain existence, robustness, and scaling of a residue.                      | Locked                                   | Phase 1 paper and artifacts under `phase1/` (paper, figures, tables, `phase1/CLAIMS.md`).                        | Phase 1 claims ledger `phase1/CLAIMS.md` plus the paper’s reproducibility appendix.                                  |
| Phase 2 – Mode-Sum + FRW Bounds  | Mode-sum implementation and bounded FRW-style viability diagnostics.            | Under audit / repair                     | Phase 2 paper and outputs under `phase2/` (paper, tables, `phase2/CLAIMS.md`).                                   | Claims allowed only as written in `phase2/CLAIMS.md` and the Phase 2 paper; explicitly marked as under audit.        |
| Phase 3 – Mechanism Module       | Mechanism-level non-cancellation floor and binding-style diagnostics.           | Active                                   | Phase 3 paper `phase3/artifacts/origin-axiom-phase3.pdf` and tables in `phase3/outputs/tables/`.                | Claims live in the Phase 3 paper appendix and are indexed in `docs/CLAIMS_INDEX.md`; no flavor calibration in `phase3/`. |
| Phase 4 – FRW Toy Diagnostics    | Toy FRW masks and probes over Phase 2/3 outputs; no real-data contact.          | Stub / partial                           | FRW masks and probe tables under `phase4/outputs/tables/`.                                                       | Non-claims and scope documents in `phase4/` (e.g. FRW toy-only status); any promotion to cosmology claims requires a dedicated gate. |
| Phase 5 – Interface / Sanity     | Cross-phase interface and sanity summaries over locked phase outputs.           | Rung 0–1 only                            | Phase 5 paper skeleton and any interface summary tables under `phase5/`.                                         | Scope and non-claims in `phase5/` restrict Phase 5 to interface/sanity statements; no new mechanism or cosmology.    |
| Stage 2 – Diagnostic Belts       | Downstream diagnostics over Phase 3/4 artifacts (FRW corridors, mech/measure, joint, data-probes). | In progress; strictly non-canonical      | Diagnostic outputs under `stage2/` (FRW corridor, mech/measure, joint mech–FRW, FRW data-probe analysis).        | Belt-specific promotion gates (e.g. FRW corridor promotion gate) are required before any Stage 2 result becomes canonical. |
| Experiments / Archives           | Archived or exploratory work (e.g. flavor-sector Phase 3 add-on).               | Archived; non-canonical                  | `experiments/phase3_flavor_v1/` and any other `experiments/` subtrees.                                           | May inspire future work but do not carry canonical claims; migration requires a note in `docs/` and re-entry via phase or Stage 2 gates. |

---

## Notes

- **Downstream usage of under-audit phases.**
  Stage 2 and Phase 4 are allowed to consume outputs from phases that are still “under audit” (such as Phase 2), but they must never silently upgrade the status of those claims.
  Any downstream table or figure that depends on such outputs should treat them as toy or diagnostic inputs and avoid phrasing that suggests they are settled physics.

- **Promotion from Stage 2 to canonical phases.**
  No result from `stage2/` is canonical by default.
  Promotion requires:
  1) a belt-specific promotion gate document that states the allowed claim types and required evidence, and
  2) an explicit update to `docs/CLAIMS_INDEX.md` and the relevant phase paper or scope docs.
  Until that happens, Stage 2 artifacts are diagnostic-only.

- **Experiments and legacy work.**
  Anything under `experiments/` is treated as archived or exploratory.
  When something is worth salvaging, it should be summarized in a migration note under `docs/` and reintroduced via a clean implementation that passes through the same gating discipline as the rest of the program.

- **If in doubt, prefer stricter documents.**
  When there is any tension between this overview and a phase-local non-claims document, claims ledger, or promotion gate, the stricter one wins.
  This file should then be updated to match that stricter source, not the other way around.
