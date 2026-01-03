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
