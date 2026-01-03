<<<<<<< HEAD
# Phase 0 � PROGRESS_LOG
## 2026-01-01
- Updated repository hygiene: removed Snakemake cache directories and LaTeX build artifacts from version control; extended ignore rules to prevent re-introduction.
- Completed Phase 0 paper build plumbing: added `phase0/paper/main.tex`, `phase0/paper/macros.tex`, `phase0/paper/references.bib`, and a minimal `.latexmkrc` configuration enabling deterministic compilation with XeLaTeX.
- Generated `phase0/paper/main.pdf` from the Phase 0 LaTeX source.

Impact:
- Phase 0 can be cited as the governance and reproducibility contract for Phase 1+ artifacts.
- Subsequent phases may reference Phase 0 definitions and claim taxonomy directly.
=======
# Phase 0 — Progress Log

Purpose: record governance-level changes that affect how all phases are executed, audited, and “locked”.

Conventions:
- Use UTC timestamps where possible.
- Each entry: what changed, why, and what it affects downstream.

---

## 2025-12 (initial Phase 0 integration)

### Created Phase 0 scaffold (governance + corridor method)
- Added Phase 0 directory structure: paper skeleton, scripts, schemas, and phase outputs placeholders.
- Defined corridor/filter artifacts as first-class objects (JSON + schema).
- Established the idea that Phase 0 makes **method claims only** (no physics claims).

Impact:
- Phase 1 and Phase 2 can now reference Phase 0 as the governance contract.
- Future phases inherit claim discipline and artifact standards from Phase 0.

Notes:
- This log is being written after-the-fact to restore continuity; future entries should be added at time-of-change.

>>>>>>> origin/docs-lock-structure-20251231

### 2026-01-03 — Baseline freeze for Phase 0 compactification

Action:
- Start governed alignment pass (Phase 0–2). No governance rules changed yet.
- Next stage will compactify Phase 0 paper (short constitution), without changing meaning.

Constraints:
- Maintain Phase 0 as method-only (no physics claims).
- Any edits must preserve enforceability: claim taxonomy, evidence contract, phase scope contract, reproducibility, failure modes, corridor governance.

### 2026-01-03 — Stage 1 (Rung 1.1): Rewrite 01_introduction.tex

- Full rewrite of the introduction into a constitution-style contract.
- Clarifies Phase 0 as governance-only; explicitly forbids physics claims in Phase 0.
- Adds an explicit “no dark progress” rule (logging + reproducibility as definition of completed work).

### 2026-01-03 — Stage 1 (Rung 1.1): Rewrite 01_introduction.tex

- Full rewrite of the introduction into a constitution-style contract.
- Clarifies Phase 0 as governance-only; explicitly forbids physics claims in Phase 0.
- Adds an explicit “no dark progress” rule (logging + reproducibility as definition of completed work).


### 2026-01-03 — Stage 1 (Rung 1.2): Rewrite 02_axioms_and_definitions.tex

- Defined the minimal governance vocabulary used across the repo: claims, evidence, canonical artifacts, provenance, phase scope, corridor/filter objects, failure modes, falsifiers.
- Added a single governance "axiom" stating completion criteria (bounded claims + canonical artifacts + reproducibility).

### 2026-01-03 — Stage 1 (Rung 1.3): Rewrite 03_corridor_method.tex

- Defined corridor governance as schema-validated filter/corridor artifacts plus an append-only history log.
- Added explicit update rules: no silent narrowing; narrowing requires canonical evidence and run provenance; reversals require explicit history entries.

### 2026-01-03 — Stage 1 (Rung 1.4): Rewrite 04_phase_contracts.tex

- Defined phase scope contracts (scope + non-claims + primary artifacts).
- Defined claim taxonomy and mandatory claim structure fields (ID, statement, evidence pointers, non-claims, falsifiers, provenance).
- Added in-body Phase 0 compliance checklist as lock condition for later phases.
