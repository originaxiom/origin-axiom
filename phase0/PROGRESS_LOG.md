<<<<<<< HEAD
# Phase 0 Ã¢ PROGRESS_LOG
## 2026-01-01
- Updated repository hygiene: removed Snakemake cache directories and LaTeX build artifacts from version control; extended ignore rules to prevent re-introduction.
- Completed Phase 0 paper build plumbing: added `phase0/paper/main.tex`, `phase0/paper/macros.tex`, `phase0/paper/references.bib`, and a minimal `.latexmkrc` configuration enabling deterministic compilation with XeLaTeX.
- Generated `phase0/paper/main.pdf` from the Phase 0 LaTeX source.

Impact:
- Phase 0 can be cited as the governance and reproducibility contract for Phase 1+ artifacts.
- Subsequent phases may reference Phase 0 definitions and claim taxonomy directly.
=======
# Phase 0 - Progress Log

Purpose: record governance-level changes that affect how all phases are executed, audited, and Ã¢ÂÂlockedÃ¢ÂÂ.

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

### 2026-01-03 - Baseline freeze for Phase 0 compactification

Action:
- Start governed alignment pass (Phase 0Ã¢ÂÂ2). No governance rules changed yet.
- Next stage will compactify Phase 0 paper (short constitution), without changing meaning.

Constraints:
- Maintain Phase 0 as method-only (no physics claims).
- Any edits must preserve enforceability: claim taxonomy, evidence contract, phase scope contract, reproducibility, failure modes, corridor governance.

### 2026-01-03 - Stage 1 (Rung 1.1): Rewrite 01_introduction.tex

- Full rewrite of the introduction into a constitution-style contract.
- Clarifies Phase 0 as governance-only; explicitly forbids physics claims in Phase 0.
- Adds an explicit Ã¢ÂÂno dark progressÃ¢ÂÂ rule (logging + reproducibility as definition of completed work).

### 2026-01-03 - Stage 1 (Rung 1.1): Rewrite 01_introduction.tex

- Full rewrite of the introduction into a constitution-style contract.
- Clarifies Phase 0 as governance-only; explicitly forbids physics claims in Phase 0.
- Adds an explicit Ã¢ÂÂno dark progressÃ¢ÂÂ rule (logging + reproducibility as definition of completed work).


### 2026-01-03 - Stage 1 (Rung 1.2): Rewrite 02_axioms_and_definitions.tex

- Defined the minimal governance vocabulary used across the repo: claims, evidence, canonical artifacts, provenance, phase scope, corridor/filter objects, failure modes, falsifiers.
- Added a single governance "axiom" stating completion criteria (bounded claims + canonical artifacts + reproducibility).

### 2026-01-03 - Stage 1 (Rung 1.3): Rewrite 03_corridor_method.tex

- Defined corridor governance as schema-validated filter/corridor artifacts plus an append-only history log.
- Added explicit update rules: no silent narrowing; narrowing requires canonical evidence and run provenance; reversals require explicit history entries.


### 2026-01-03 - Stage 1 (Rung 1.5): Rewrite 05_reproducibility_contract.tex

- Defined the reproducibility contract: deterministic generation of canonical artifacts, required run provenance fields, recommended run bundle structure, and reproducibility failure handling.



### 2026-01-03 - Stage 1 (Rung 1.6): Rewrite 06_falsifiability_and_failure_modes.tex

- Defined falsifiers as mandatory per-claim fields; defined phase failure modes; formalized failure handling (record, quarantine, repair, re-validate, disclose).
- Added speculation policy (must be labeled as non-claim/future work; cannot serve as evidence).

### 2026-01-03 - Stage 1 (Rung 1.7): Rewrite 07_discussion_candidate_origins.tex

- Compressed candidate-origins content into an explicitly non-normative note (hypotheses only).
- Added explicit prohibition against using this section as evidence in later phases.

### 2026-01-03 - Stage 1 (Rung 1.8): Rewrite 08_conclusion.tex

- Replaced conclusion with a short constitution summary: claims must be bounded, evidence must be canonical and reproducible, corridor narrowing must be append-only and provenance-backed, speculation must be labeled.

### 2026-01-03 - Stage 1 (Rung 1.9): Paper spine + appendix policy

- main.tex rewritten as stable spine; normative body + non-normative appendices separated explicitly.
- Abstract rewritten (previous copy had corrupted ellipsis artifacts).
- Added minimal workflow citation to keep references meaningful.
- Added non-normative disclaimers to all appendices.



### 2026-01-03 - Stage 1 (Rung 1.10): Split PDFs (constitution vs non-normative appendices)

- main.tex now builds only the constitution body; appendices moved to appendices.tex.
- Appendix cross-PDF references removed (no undefined refs across separate PDFs).
- Removed appendix bibliography unless citations are explicitly added.

### 2026-01-03 - Stage 1 (Rung 1.10c): Appendices reference cleanup + build verification

- Eliminated remaining undefined reference in appendices (no cross-PDF labels).
- Confirmed citations resolve against references.bib under latexmk.


### 2026-01-03 - Paper build validation
 - Phase 0 paper (`main.tex`) and appendices build cleanly via `latexmk` with BibTeX.
 - Generated `phase0/paper/main.pdf` and `phase0/paper/appendices.pdf` as convenience artifacts (not evidence; sources are `.tex` + referenced artifacts).
 - Cleaned LaTeX build outputs locally via `latexmk -C`.
## 2026-01-03 - Phase 0 Compactification (P0-C1): paper/build hygiene
- Stage 0 baseline freeze tag created and pushed: `stage0-freeze-2026-01-03` (commit `e675e1a`).
- Added LaTeX build artifact ignores for Phase 0 paper directory to prevent tracking `.aux/.toc/.xdv/...`.
- Added canonical build entrypoint `scripts/build_papers.sh` to regenerate Phase 0 + Phase 1 PDFs deterministically.
- No Phase 1 results changed; compactification is organizational/hygiene only.

## 2026-01-03 - Phase 0 Compactification (P0-C2): reproducibility entrypoints
- Linked canonical PDF build entrypoint (`./scripts/build_papers.sh`) from Phase 0 and Phase 1 READMEs.
- Added repo-level `REPRODUCIBILITY.md` pointing to Stage 0 tag `stage0-freeze-2026-01-03`.
- No results changed; documentation/build hygiene only.


## 2026-01-04 — Phase 2 lock promoted to canonical main

- Canonical branch unified: promoted Phase 2 paper + provenance pipeline onto `main` (commit `dd4369c`).
- Phase 2 lock tags:
  - `phase2-lock-2026-01-04` (original lock candidate, commit `e1277e6`)
  - `phase2-lock-2026-01-04-final` (final lock on canonical `main`, commit `dd4369c`)
- Cleanup: merged and removed temporary working branches after unification; `main` is now the single canonical branch.
- Safety snapshot tag created pre-unify: `backup/pre-unify-20260104-1259` (commit `d784429`).

## 2026-01-06 — Rung A: Ledger records git_commit in corridor history

- Updated `phase0/scripts/phase0_ledger.py` so that each entry appended to
  `phase0/phase_outputs/theta_corridor_history.jsonl` is enriched with the current
  `git_commit` hash (via `git rev-parse HEAD` from the phase0 working directory).
- This keeps the corridor history append-only while tying each narrowing step to a
  concrete repository state for audit and comparison with future runs.
