# Stage 2 paper audit plan (Phase 0–5 PDFs)

Status (2026-01-11): This document defines the plan and checklist for auditing the Phase 0–5 papers against the current contracts, alignment memos, and Stage 2 verdicts. It does not change any LaTeX or claims; it specifies how future rungs will read and, if needed, adjust the papers.

## 1. Papers and canonical artifacts

The following PDFs are treated as the canonical paper artifacts for the Stage I phases:

- Phase 0: `artifacts/origin-axiom-phase0.pdf`
- Phase 1: `artifacts/origin-axiom-phase1.pdf`
- Phase 2: `artifacts/origin-axiom-phase2.pdf`
- Phase 3: `artifacts/origin-axiom-phase3.pdf`
- Phase 4: `artifacts/origin-axiom-phase4.pdf`
- Phase 5: `artifacts/origin-axiom-phase5.pdf` (Phase 5 stub, if present)

Each paper is connected to:

- Phase contracts and docs under `phase*/` (SCOPE, CLAIMS, NON_CLAIMS, REPRODUCIBILITY, ROLE_IN_PROGRAM, etc).
- Alignment memos `phase*/PHASE*_ALIGNMENT_v1.md`.
- Stage 2 verdict docs where relevant (especially for Phases 2–4 and Phase 5).

The audit belt will check that the papers and these docs tell a coherent story at the current Stage 2 snapshot.

## 2. Audit goals (per phase)

For each phase, the audit has three main goals:

1. **Narrative alignment.**
   - Abstract and introduction should match:
     - the phase SCOPE and ROLE docs,
     - the phase CLAIMS / NON_CLAIMS,
     - and the relevant alignment memo.
   - The paper should not promise results that belong to later phases or that Stage 2 now rules out.

2. **Claims alignment.**
   - The explicit claims or numbered statements in the paper should be compatible with:
     - phase claims registers (e.g. `phase2/CLAIMS.md`, `phase3/CLAIMS` as embedded in the paper),
     - `docs/CLAIMS_INDEX.md`,
     - and Stage 2 verdicts (for Phases 2–4).
   - Negative results and parked items should be clearly labelled as such.

3. **Status and scope language.**
   - The paper should speak about:
     - toy ensembles and internal diagnostics where that is what exists,
     - and avoid implying real-data contact, final θ★ selection, or a canonical θ-measure when those are explicitly not present in the Stage 2 verdict.
   - Any mention of future work or data contact should be framed consistently with `docs/FUTURE_WORK_AND_ROADMAP.md` and Phase 4/5 design docs.

The aim is to make sure that an external reader who only sees the papers plus the core docs receives a story that matches the actual current program status.

## 3. Planned rungs (Phase-by-phase)

The paper audit belt will proceed in small, phase-focused rungs.

### Rung E2 — Phase 2 paper audit (mode-sum + bounded FRW viability)

- Inputs:
  - `artifacts/origin-axiom-phase2.pdf`
  - `phase2/SCOPE.md`, `phase2/CLAIMS.md`, `phase2/NON_CLAIMS.md` (if present), `phase2/REPRODUCIBILITY.md`
  - `phase2/PHASE2_ALIGNMENT_v1.md`
  - Stage 2 FRW verdicts and master verdict
- Tasks:
  - Read Phase 2 abstract, introduction, claims sections, and conclusions.
  - Check for mismatches with Phase 2 contracts and Stage 2 FRW verdicts (bounded viability, pre-data status).
  - Produce a short audit note:
    - what is already aligned,
    - what phrasing might need tightening in a future editing rung,
    - and any explicit “do not yet claim X” notes.
- Output:
  - `stage2/docs/STAGE2_PAPER_AUDIT_PHASE2_v1.md` (descriptive, no edits).
  - If needed, a later separate rung will propose concrete LaTeX patches.

### Rung E3 — Phase 3 paper audit (mechanism module)

- Inputs:
  - `artifacts/origin-axiom-phase3.pdf`
  - `phase3/MECHANISM_CONTRACT.md`, `phase3/SCOPE.md`, `phase3/ROLE_IN_PROGRAM.md`, `phase3/REPRODUCIBILITY.md`
  - `phase3/PHASE3_ALIGNMENT_v1.md`
  - Stage 2 mechanism and joint verdicts
- Tasks:
  - Read Phase 3 abstract, introduction, mechanism definition, and conclusions.
  - Check that Phase 3 is framed as a mechanism module, not as a flavor or measure phase.
  - Ensure the paper does not claim a canonical θ-measure or a θ★ selection that Stage 2 explicitly does not support.
- Output:
  - `stage2/docs/STAGE2_PAPER_AUDIT_PHASE3_v1.md`.

### Rung E4 — Phase 4 paper audit (FRW toy stub and corridors)

- Inputs:
  - `artifacts/origin-axiom-phase4.pdf`
  - Phase 4 SCOPE/CLAIMS/NON_CLAIMS/REPRODUCIBILITY docs
  - `phase4/PHASE4_ALIGNMENT_v1.md`
  - Stage 2 FRW, data-probe, joint, and θ★ verdicts
- Tasks:
  - Read how Phase 4 positions the FRW toy world, corridors, and any references to data or θ★.
  - Check consistency with:
    - pre-data status of the corridors,
    - redundancy with mechanism scalars,
    - and the negative-result θ★ verdict.
- Output:
  - `stage2/docs/STAGE2_PAPER_AUDIT_PHASE4_v1.md`.

### Rung E5 — Phase 5 stub audit (interface stub, if present)

- Inputs:
  - `artifacts/origin-axiom-phase5.pdf` (if available)
  - Phase 5 docs and alignment memo
  - Stage 2 master verdict and Phase 5 interface design docs
- Tasks:
  - Check that any existing Phase 5 text matches the internal verdict skeleton and does not front-run future interface work.
- Output:
  - `stage2/docs/STAGE2_PAPER_AUDIT_PHASE5_v1.md`.

### Rung E6 — Phase 0–1 quick consistency scan

- Inputs:
  - `artifacts/origin-axiom-phase0.pdf`
  - `artifacts/origin-axiom-phase1.pdf`
  - Phase 0–1 docs (claims, contracts, governance)
- Tasks:
  - Spot-check that Phase 0–1 papers are consistent with the Phase 0 contract and the locked Phase 1 toy-ensemble narrative.
  - Focus on obvious contradictions; no deep rewrite is planned at this stage.
- Output:
  - `stage2/docs/STAGE2_PAPER_AUDIT_PHASE01_v1.md`.

## 4. Editing rungs (deferred)

Actual text changes to the LaTeX sources (e.g. `phase2/paper/main.tex`, `phase3/paper/main.tex`, `phase4/paper/main.tex`) will be handled in separate editing rungs after the descriptive audits:

- Each edit rung will:
  - list the specific LaTeX files to touch,
  - propose full-file replacements or minimal but explicit patches via scripts,
  - and be logged in both `PROGRESS_LOG.md` and the relevant `phase*/PROGRESS_LOG.md`.
- No Phase paper will be changed without a clear audit note backing the change.

This document defines the audit belt only; it does not enact any edits.
