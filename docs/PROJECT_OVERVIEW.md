# Origin Axiom – Project Overview

This repository is the working tree for the “Origin Axiom” program: a disciplined attempt to see whether a simple, non-cancelling phase condition can serve as a meaningful organizing principle for vacuum, fields, and large-scale structure without over-claiming. The point is not to smuggle in a grand Theory of Everything, but to test whether a particular axiom can survive increasingly sharp scrutiny across well-gated phases.

The project is organized as a sequence of Phases (0–5) plus a downstream Stage 2 “diagnostic belt.” Each Phase has a clearly defined scope, non-claims, canonical artifacts, and reproducibility gates. Stage 2 runs strictly downstream of the canonical Phase outputs and does not modify any Phase claims.

This document gives you a high-level map of that structure so you can understand where you are when you open a file, run a script, or look at a figure.

---

## 1. High-level structure

At the highest level the repo splits into:

- `phase0/` – Governance, contracts, and claim discipline (no physics claims).
- `phase1/` – Toy ensembles: existence/robustness/scaling claims in controlled settings.
- `phase2/` – Mode-sum model and bounded FRW-style viability diagnostics.
- `phase3/` – Mechanism module: toy non-cancellation floor and binding-style diagnostics.
- `phase4/` – FRW toy diagnostics: mapping Phase 3 outputs into FRW-style backgrounds.
- `phase5/` – Interface and sanity layer: cross-phase summaries and dashboards.
- `stage2/` – Diagnostic belts downstream of Phase 3/4 outputs (non-canonical).
- `experiments/` – Archived or exploratory work that is explicitly non-canonical.
- `docs/` – Global narrative and governance files (including this one).
- `scripts/` – Convenience scripts and orchestrators (where they exist).

The canonical Phase tree is `phase0/` through `phase5/`. Stage 2 and `experiments/` are allowed to be creative and exploratory, but they are not allowed to silently change what any Phase claims.

---

## 2. Phase-by-phase snapshot (Stage I)

Stage I is the program currently implemented in this repo. Very roughly:

1. **Phase 0 – Governance and contracts.** Defines how claims are written, what counts as evidence, how to retire bad ideas without erasing them, and how to gate later Phases. Canonical artifacts live in `phase0/` (for example, `phase0/CLAIMS.md` and the Phase 0 contracts).

2. **Phase 1 – Toy ensembles (Locked).** Constructs controlled toy ensembles where a residue can be computed and measured. The Phase 1 paper and its canonical figures live under `phase1/`. Claims here are strictly toy-domain: existence, robustness, and scaling within clearly defined toy models.

3. **Phase 2 – Mode-sum + bounded FRW viability (Under audit).** Implements the residue in a stricter mode-sum model and introduces FRW-style “bounded viability” diagnostics. The outputs live under `phase2/` and are explicitly toy/diagnostic: they are not claims about the real universe, but about how the axiom behaves in that model.

4. **Phase 3 – Mechanism module (Active).** Locks in a baseline non-cancellation floor on a global amplitude and provides binding-style diagnostics at the mechanism level. Canonical artifacts are the Phase 3 paper and tables in `phase3/outputs/tables/`. There is no canonical flavor calibration in `phase3/` at this rung.

5. **Phase 4 – FRW toy diagnostics (Stub).** Maps Phase 3 outputs into FRW-style backgrounds and viability masks under controlled assumptions. The purpose is to create a clean FRW hook without claiming real-data contact. The implementation lives under `phase4/`, with the FRW viability and data-probe tables under `phase4/outputs/tables/`.

6. **Phase 5 – Interface and sanity layer (Rung 0–1).** Reads locked Phase 3/4 outputs and produces interface summaries, sanity tables, and simple dashboards. It does not introduce new mechanisms or cosmology claims; it is an interface for humans (and downstream tools) to understand what the locked Phases are actually saying.

All of this is described at a high level in `docs/PHASES.md` and `docs/STATE_OF_REPO.md`. For detailed claims, see `docs/CLAIMS_INDEX.md` and the per-Phase claims tables or appendices.

---

## 3. Stage 2 – Diagnostic belts (downstream only)

Stage 2 lives under `stage2/` and is intentionally non-canonical. It is a set of “belts” that wrap around the Phase 3/4 outputs and apply additional diagnostics, consistency checks, or bookkeeping. Stage 2 may strongly suggest what is worth promoting, but promotion itself requires explicit, gated changes to the Phase docs and claims ledgers.

Current Stage 2 belts include:

- `stage2/frw_corridor_analysis/` – Rungs that analyze FRW-style corridors and θ-families on the Phase 4 grid (family counts, overlaps, contiguity, robustness, θ* alignment, and figures).
- `stage2/mech_measure_analysis/` – Rungs that inventory Phase 3 tables, identify measure-like candidates and flags, and summarize their θ-profiles.
- `stage2/joint_mech_frw_analysis/` – Rungs that build a joint θ-grid between Phase 3 and Phase 4 and compute correlations and family summaries in the combined space.
- `stage2/frw_data_probe_analysis/` – Rungs that audit the FRW data-probe hooks versus viability masks (for example, checking which probes actually discriminate and how they align with the FRW viability flag).
- `stage2/doc_repo_audit/` – Rungs that inventory documentation, detect broken references, orphan candidates, and open narrative threads. Summarized in `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` and `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`.

The guiding rules for Stage 2 are:

- It reads Phase outputs; it does not silently rewrite or reinterpret Phase claims.
- Any promotion of a Stage 2 result into a Phase paper must go through an explicit gate (for example, an FRW promotion document under `stage2/docs/`) plus ordinary git and `PROGRESS_LOG.md` entries.
- Stage 2 artifacts are useful for understanding and stress-testing the program but are not themselves “Phase claims” unless explicitly promoted.

---

## 4. Stage II – Hypothetical future expansion

Separate from the existing `stage2/` belts, there is a notion of a possible **Stage II**: additional Phases or modules that would only be attempted if Phase 0–5 and Stage 2 all survive an honest audit. Examples might include:

- Structured contact with additional sectors of the Standard Model.
- Deeper field-theoretic or many-body embeddings of the mechanism.
- Societal or ethical deployment layers if the axiom survives as a serious organizing principle.

Stage II is not implemented in this repo. When and if it is, it must obey the same governance discipline: clear scope, explicit non-claims, canonical artifacts, and reproducible gates.

---

## 5. Flavor Phase 3 experiment (archived)

Earlier work attempted a flavor-sector Phase 3 in which the θ-parameter was tied more directly to CKM/PMNS phases. That work is now explicitly archived and non-canonical.

- The archived experiment lives under `experiments/phase3_flavor_v1/`.
- Its status and constraints are documented in `experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md`.
- It may still be mined for ideas, ansätze, and diagnostic patterns, but:
  - It must not be treated as a canonical Phase 3 claim.
  - It must not be wired directly into Phase 2/3/4/5 gates without a new migration note and rung.

Canonical Phase 3 is the mechanism module under `phase3/`, as described in `phase3/ROLE_IN_PROGRAM.md` and the Phase 3 paper.

---

## 6. How to read and run this repo

A good way to approach the repo is:

1. **Start with the global docs.** Read `README.md`, then `docs/PHASES.md` and `docs/STATE_OF_REPO.md`. If you care about claims, skim `docs/CLAIMS_INDEX.md`.

2. **Pick a Phase or belt.** Decide whether you are interested in:
   - Phase 1 toy ensembles,
   - Phase 2 mode-sum viability,
   - Phase 3 mechanisms,
   - Phase 4 FRW diagnostics,
   - Phase 5 interface,
   - or a Stage 2 diagnostic belt.

3. **Read the local README or role doc.** For example:
   - `phase3/ROLE_IN_PROGRAM.md` for the mechanism module.
   - `phase4/OVERVIEW.md` for the FRW diagnostics.
   - `stage2/docs/STAGE2_OVERVIEW_v1.md` for Stage 2 belts.

4. **Locate canonical artifacts.** Each Phase or belt should tell you where its primary tables and figures live (for example, `phase3/outputs/tables/`, `phase4/outputs/tables/`, or `stage2/.../outputs/`).

5. **Follow the reproducibility notes.** Where present, paper appendices or local docs should specify exact commands (often via `oa` and small driver scripts) to regenerate tables and figures.

6. **Use Stage 2 as a diagnostic lens.** When preparing a publication-grade pass or a major restructuring, consult:
   - `stage2_doc_open_threads_v1.csv` for unresolved narrative threads.
   - `stage2_doc_orphan_candidates_v1.csv` for docs that might need linking, archiving, or retirement.

---

## 7. Governance and evolution

The program is designed to evolve without silently rewriting history:

- Claims are registered in Phase-specific ledgers or appendices and indexed via `docs/CLAIMS_INDEX.md`.
- Retired or superseded ideas are archived (for example, in `experiments/`), not deleted.
- Stage 2 audits and belts provide context for future promotions but do not themselves make new claims.
- `PROGRESS_LOG.md` serves as a chronological log of rungs, including when audits are run, when belts are added, and when promotions are considered.

If you add new work, the key questions to ask yourself are:

1. Does this belong in the canonical Phase tree, a Stage 2 belt, or an experiment?
2. What are its explicit non-claims?
3. What are its canonical artifacts, and how are they regenerated?
4. How does it interact with existing claims and gates?

If you can answer those cleanly and wire them into the existing docs, you are helping the program remain coherent, reproducible, and intellectually honest.


## 7. Governance and θ companion docs

For readers who want a deeper view of governance and the θ architecture:

- `docs/ARCHIVE.md` explains the archive and deprecation policy, including how exploratory work is retired or migrated into phases.
- `docs/GATES_AND_STATUS.md` is the central index of gates and status labels across phases, Stage 2 belts, and experiments.
- `docs/THETA_ARCHITECTURE.md` describes how θ-like parameters and corridors are treated across the program, including the role of admissible regions and intersection-style narrowing.

### Obstruction program (interpretive layer)

In addition to the strictly scoped Phase 0–5 contracts, the Origin Axiom stack can be read as an exploration of an obstruction to perfect vacuum cancellation: a configuration space in which exact global cancellation is forbidden and θ controls how the system threads the allowed region. This obstruction program is an optional, non-binding interpretive layer that organises how Phase 1–4 toy ensembles, mechanism diagnostics, FRW masks, and Stage 2 empirical kernels fit together. A first snapshot of this perspective is recorded in `docs/OBSTRUCTION_PROGRAM_OVERVIEW_v1.md`.
