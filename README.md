# Origin Axiom

A disciplined, multi-phase attempt to see whether a single **non-cancelling phase twist** (θ\* or a closely related structure) could sit at the root of vacuum, fields, and large-scale structure – and if not, to learn *precisely why not* in a way that is reusable for future work.

This repo is the **Stage I** program: a gated, reproducible ladder of phases, each with:

- a clearly declared scope and *non-claims*,
- explicit, versioned artifacts (papers, tables, figures),
- and a governance layer (Phase 0) that constrains what we are allowed to say.

The goal is *not* to hand-wave a “theory of everything”. The goal is to build a **testable, falsifiable narrative** from:

> axiom → toy ensembles → mechanisms → FRW-style diagnostics → interfaces & sanity checks

and to do so in a way that an external collaborator could clone, run, and audit.

---

## 0) Phased program at a glance

Each Phase is a rung with its own paper, gates, and claims discipline. Phase 0 is the governance/specification layer; Stage 2 belts sit downstream of Phases 3/4 as diagnostics.

- **Phase 0 – Governance & Specification (Locked)**  
  - Define what “claims” even mean in this program.
  - Specify locking, gating, and reproducibility standards.
  - Declare how we handle legacy work, retired ideas, and “tempting but under-evidenced” patterns.

- **Phase 1 – Toy Ensembles (Locked)**  
  - Build controlled toy ensembles where a residue can be computed.
  - Quantify existence, robustness, and scaling in toy settings only.
  - Produce the Phase 1 paper and canonical figures.

- **Phase 2 – Mode-Sum + Bounded FRW Viability (Under Audit)**  
  - Implement the residue in a stricter mode-sum model.
  - Encode corridor/filter language and bounded FRW-style diagnostics.
  - Keep claims explicitly toy/diagnostic.

- **Phase 3 – Mechanism Module (Active)**  
  - Lock a baseline non-cancellation floor on a global amplitude.
  - Provide binding-style diagnostics and mechanism-level tables.
  - No flavor calibration or corridor narrowing in the canonical Phase 3.

- **Phase 4 – FRW Toy Diagnostics (Diagnostic Stub)**  
  - Map Phase 3 outputs into FRW-style toy backgrounds and viability masks.
  - Provide a data-probe hook without claiming real-data contact.

- **Phase 5 – Interface & Sanity Layer (Rung 0–1)**  
  - Read locked Phase 3/4 outputs and emit interface summaries/sanity tables.
  - No new mechanism or cosmology claims.

- **Stage 2 – Diagnostic Belts (In Progress)**  
  - Downstream analyses over Phase 3/4 outputs: FRW corridor analysis,
    mechanism/measure analysis, joint mech–FRW analysis, FRW data-probe audit, and a documentation audit belt.
  - Non-canonical until promoted.

Flavor-sector calibration work lives under [`experiments/phase3_flavor_v1/`](experiments/phase3_flavor_v1/) and is **archived/non-canonical**. The canonical Phase 3 is the mechanism module described above.

---

## 1) What this is *about*

**Core question:**  
Is there a *single*, structurally inevitable way for the vacuum not to fully cancel – a tiny, disciplined “phase twist” – that can be made mathematically precise and interrogated across toy models, mechanisms, and FRW-style backgrounds?

We are not trying to “fit the universe” in one shot. We are trying to:

- formulate a **coherent axiom** about non-cancellation,
- **stress-test** it in toy ensembles (Phase 1),
- encode it as a **mechanism** with explicit diagnostics (Phase 2/3),
- and **map** that into FRW-style toy cosmology (Phase 4),
- while maintaining a *strict ledger* of what is claimed, what is merely suggestive, and what has been falsified or retired.

In parallel, Phase 0 enforces:

- honesty about what we do *not* know,
- reproducible gates (how to regenerate each artifact),
- and a clear separation between canonical phases, downstream diagnostics (Stage 2), and historical experiments.

---

## 2) Repository structure (Stage I + Stage 2)

Top-level layout (canonical Phases, Stage 2 belts, and archived experiment):

- [`phase0/`](phase0/) – Governance & specification (locked)  
  - Claims ledger, contracts, and method declarations.  
  - Defines how phases lock, how claims are phrased, and how evidence is tracked.

- [`phase1/`](phase1/) – Toy ensembles (locked)  
  - [`paper/`](phase1/paper/) – Phase 1 toy-domain paper.  
  - [`outputs/figures/`](phase1/outputs/figures/) – Canonical toy figures.

- [`phase2/`](phase2/) – Mode-sum model + bounded FRW diagnostics (under audit)  
  - [`paper/`](phase2/paper/) – Phase 2 paper.  
  - [`src/`](phase2/src/) – Mode-sum + FRW-style diagnostic code.

- [`phase3/`](phase3/) – Mechanism module (active)  
  - [`paper/`](phase3/paper/) – Phase 3 mechanism document.  
  - [`outputs/tables/`](phase3/outputs/tables/) – Mechanism-level tables and diagnostics.  
  - [`ROLE_IN_PROGRAM.md`](phase3/ROLE_IN_PROGRAM.md) – How the mechanism module fits into the overall program.

- [`phase4/`](phase4/) – FRW toy diagnostics (stub)  
  - FRW-like background construction and viability masks.  
  - Shape/data/viability masks live under [`outputs/tables/`](phase4/outputs/tables/).

- [`phase5/`](phase5/) – Interface + sanity layer (rung 0–1)  
  - Interface summaries and sanity checks over locked Phase 3/4 outputs.

- [`stage2/`](stage2/) – Diagnostic belts (downstream, non-canonical)  
  - [`frw_corridor_analysis/`](stage2/frw_corridor_analysis/) – FRW viability/corridor belts.
  - [`mech_measure_analysis/`](stage2/mech_measure_analysis/) – Mechanism/measure belts over Phase 3 tables.
  - [`joint_mech_frw_analysis/`](stage2/joint_mech_frw_analysis/) – Joint mech–FRW θ-grid analysis.
  - [`frw_data_probe_analysis/`](stage2/frw_data_probe_analysis/) – Toy FRW data-probe audit (no real data claims).
  - [`doc_repo_audit/`](stage2/doc_repo_audit/) – Documentation inventory, ref checks, and open-thread tracking.

- [`experiments/phase3_flavor_v1/`](experiments/phase3_flavor_v1/) – Archived flavor-sector add-on (non-canonical)  
  - Historical attempt at flavor-sector calibration, explicitly archived.  
  - See [`experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md`](experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md) for status.

Support and meta:

- [`docs/`](docs/) – Global docs:  
  - [`PROJECT_OVERVIEW.md`](docs/PROJECT_OVERVIEW.md) – High-level Stage I overview.  
  - [`PHASES.md`](docs/PHASES.md) – Phase-by-phase definitions.  
  - [`STATE_OF_REPO.md`](docs/STATE_OF_REPO.md) – Current status and claims indexing.  
  - [`CLAIMS_INDEX.md`](docs/CLAIMS_INDEX.md) – Map of claims across phases.  
  - [`FUTURE_WORK_AND_ROADMAP.md`](docs/FUTURE_WORK_AND_ROADMAP.md) – Stage II / future directions.  

- [`stage2/docs/`](stage2/docs/) – Stage 2 specific docs:  
  - [`STAGE2_OVERVIEW_v1.md`](stage2/docs/STAGE2_OVERVIEW_v1.md) – Overview of Stage 2 belts.  
  - [`STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`](stage2/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md) – FRW corridor belt summary.  
  - [`STAGE2_MECH_MEASURE_SUMMARY_v1.md`](stage2/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md) – Mechanism/measure belt summary.  
  - [`STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`](stage2/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md) – Joint mech–FRW belt summary.  
  - [`STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md`](stage2/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md) – FRW data-probe audit summary.  
  - [`STAGE2_DOC_AUDIT_SUMMARY_v1.md`](stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md) – Documentation audit CSVs and how to use them.  
  - [`STAGE2_ARCHIVE_STATUS_v1.md`](stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md) – Map of canonical vs archived areas.

- [`PROGRESS_LOG.md`](PROGRESS_LOG.md) – Chronological log of work.  
  - Early entries may reference legacy paths (`src/`, `data/`, `figures/`); see the note at the top.  
  - New entries should reference the current Phase/Stage structure.

---

## 3) How to interact with this repo

### 3.1 If you just want to *read the story*

Start with:

1. [`docs/PROJECT_OVERVIEW.md`](docs/PROJECT_OVERVIEW.md) – Stage I overview and how the phases fit.  
2. [`docs/PHASES.md`](docs/PHASES.md) – Per-phase scope and non-claims.  
3. The Phase papers, in order:
   - [`phase1/paper/`](phase1/paper/) (toy ensembles),
   - [`phase2/paper/`](phase2/paper/) (mode-sum + FRW diagnostics),
   - [`phase3/paper/`](phase3/paper/) (mechanism module),
   - [`phase4/paper/`](phase4/paper/) (FRW toy diagnostics stub),
   - [`phase5/paper/`](phase5/paper/) (interface/sanity layer, rung 0–1).

Phase PDFs live under [`artifacts/`](artifacts/): Phase 0 – [`origin-axiom-phase0.pdf`](artifacts/origin-axiom-phase0.pdf), Phase 1 – [`origin-axiom-phase1.pdf`](artifacts/origin-axiom-phase1.pdf), Phase 2 – [`origin-axiom-phase2.pdf`](artifacts/origin-axiom-phase2.pdf), Phase 3 – [`origin-axiom-phase3.pdf`](artifacts/origin-axiom-phase3.pdf), Phase 4 – [`origin-axiom-phase4.pdf`](artifacts/origin-axiom-phase4.pdf), Phase 5 – [`origin-axiom-phase5.pdf`](artifacts/origin-axiom-phase5.pdf).

Use [`docs/CLAIMS_INDEX.md`](docs/CLAIMS_INDEX.md) and [`phase0/CLAIMS.md`](phase0/CLAIMS.md) to see how claims are registered and what they depend on.

### 3.2 Running phase gates individually

Each Phase has a gate / reproducibility path, usually documented in:

- the Phase paper (appendix),
- local README files,
- and sometimes dedicated scripts.

Examples (schematic, not guaranteed commands):

- Phase 1 toys:  
  - scripts to regenerate toy ensembles and figures.

- Phase 2 diagnostics:  
  - scripts for mode-sum scans and FRW-style viability checks.

- Phase 3 mechanism:  
  - scripts that generate mechanism-level tables in [`phase3/outputs/tables/`](phase3/outputs/tables/).

- Phase 4 FRW diagnostics:  
  - scripts that build shape/data/viability masks in [`phase4/outputs/tables/`](phase4/outputs/tables/).

You can invoke them directly when working on a particular phase. Consult the
script headers and the Phase papers’ reproducibility appendices for exact
commands.

### 3.3 Stage 2 diagnostics (downstream only)

Stage 2 work lives under [`stage2/`](stage2/) and is **strictly downstream** of the
Phase 3/4 artifacts. It does not modify Phase papers or claims. See the
local README or docs within each Stage 2 module for entry points.

Current belts include:

- [`frw_corridor_analysis/`](stage2/frw_corridor_analysis/) – FRW corridor/viability analysis on the Phase 4 masks.  
- [`mech_measure_analysis/`](stage2/mech_measure_analysis/) – Measure-like candidates and mechanism diagnostics over Phase 3 tables.  
- [`joint_mech_frw_analysis/`](stage2/joint_mech_frw_analysis/) – Joint θ-grid diagnostics combining Phase 3 mechanisms and Phase 4 FRW outputs.  
- [`frw_data_probe_analysis/`](stage2/frw_data_probe_analysis/) – Audit of the FRW data-probe hooks (toy-level, no real-data claims).  
- [`doc_repo_audit/`](stage2/doc_repo_audit/) – Inventory of docs, broken references, orphans, and open narrative threads, via CSVs under [`stage2/doc_repo_audit/outputs/tables/`](stage2/doc_repo_audit/outputs/tables/).

Stage 2 results are **non-canonical** until explicitly promoted via Phase 0
governance and a documented gate (e.g. “FRW Corridor Promotion Gate”).

---

## 4) Big questions (and guardrails)

This program is animated by a few big questions, but we treat them as
*questions*, not assumptions:

- **Vacuum non-cancellation:**  
  Can we formalize a single, disciplined way in which the vacuum “fails to cancel”
  that is compatible with known structures and can be traced through toy
  ensembles, mechanisms, and FRW-like backgrounds?

- **Corridors vs needles:**  
  Do we ever get **robust corridors** of θ values that survive multiple filters,
  or are we always chasing single “needle” points that are numerically brittle?

- **Mechanism ↔ FRW mapping:**  
  Can a mechanism-level non-cancellation floor be meaningfully mapped into FRW
  toy backgrounds, or does the mapping itself introduce uncontrollable ambiguity?

- **Flavor and structure (archived for now):**  
  Are there hints that flavor-sector structure (CKM/PMNS, etc.) wants to talk to
  this axiom? Early attempts exist in [`experiments/phase3_flavor_v1/`](experiments/phase3_flavor_v1/) but are
  **archived and non-canonical**. Any revival would need a fresh Phase/Stage
  declaration and a new gate.

Guardrails:

- We do **not** claim a derivation of Standard Model parameters.  
- We do **not** claim predictive power for real cosmological data at this Stage.  
- We do **not** treat any suggestive numerical pattern as a claim without:
  - a registered claim ID,
  - a documented evidentiary path,
  - and a Phase 0–compatible statement.

Everything else lives either in Stage 2 diagnostics or clearly marked experiments.

---

## 5) How to contribute or extend

If you want to extend this program:

1. Decide **where** your contribution lives:
   - canonical Phase (0–5),
   - Stage 2 diagnostic belt,
   - or experiment / legacy area.

2. Declare:
   - scope,
   - allowed claim types,
   - explicit non-claims,
   - expected artifacts (tables, figures, papers).

3. Add or update:
   - a local README in your directory,  
   - entries in [`docs/PHASES.md`](docs/PHASES.md) and/or [`docs/CLAIMS_INDEX.md`](docs/CLAIMS_INDEX.md) if canonical,  
   - and log the change in [`PROGRESS_LOG.md`](PROGRESS_LOG.md).

4. Keep everything:
   - reproducible (scripted gates, pinned seeds where appropriate),
   - inspectable (tables and figures traceable back to code),
   - and honest about what is and is not supported.

If you’re reading this as an external collaborator, you should be able
to:

- clone the repo,
- follow the Phase and Stage docs,
- re-run the canonical gates,
- and check that our claims are exactly as strong (and as modest) as the evidence warrants.

That is the standard we are trying to hold ourselves to.

---

## 6) Why this exists

There is a long history of ambitious ideas about vacuum, constants, and
“hidden structure” in physics. Many are beautiful; many are wrong; most are
impossible to audit.

This repo exists to ask a very specific question:

> Could a single, disciplined non-cancelling phase twist at the root of the vacuum
> survive contact with toy ensembles, mechanisms, and FRW-style diagnostics
> *without* collapsing under its own claims?

If the answer is “no”, we want to know exactly why – in a form that is reusable
for future work. If the answer is “maybe”, the standard only gets *stricter* from
here.

Everything here is in service of that question.
