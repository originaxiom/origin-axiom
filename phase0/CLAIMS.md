# Phase 0 — Claims Ledger (Governance & Method)

Phase 0 does **not** make physics claims about the value of \(\theta_\star\), cosmology, or particle phenomenology.  
Its role is to define the **governance, bookkeeping, and reproducibility contracts** that all subsequent phases must obey.

Each claim below has:
- a **stable ID** `P0-Cxx`,
- a short **statement**,
- a list of **evidence pointers** (files / sections),
- an explicit **non-claim boundary**.

Where relevant, sections of the Phase 0 paper are referenced as:
- `Phase0-paper: <section>` (e.g. `Phase0-paper: 03_corridor_method`).

---

## P0-C01 — Corridor & Filter Artifacts Are First-Class, Schema-Governed Objects

**Statement**

Phase 0 defines the theta corridor and phase filter objects as **first-class artifacts** represented in JSON, with explicit JSON Schemas. Any admissible \(\theta\)-corridor used in later phases must be encoded through these artifacts (or documented extensions), not through ad hoc conventions.

**Evidence**

- Schemas  
  - `phase0/schemas/phase_theta_filter.schema.json`  
  - `phase0/schemas/theta_corridor.schema.json`

- Instantiated artifacts  
  - `phase0/phase_outputs/phase_00_theta_filter.json`  
  - `phase0/phase_outputs/phase_01_theta_filter.json`  
  - `phase0/phase_outputs/phase_01_theta_filter_TOY.json`  
  - `phase0/phase_outputs/phase_02_theta_filter.json`  
  - `phase0/phase_outputs/theta_corridor_current.json`  
  - `phase0/phase_outputs/theta_corridor_history.jsonl`

- Documentation  
  - `phase0/paper/main.tex`  
    - `Phase0-paper: 02_axioms_and_definitions`  
    - `Phase0-paper: 03_corridor_method`  
    - `Phase0-paper: Appendix B_phase_theta_filter_schema`  

**Non-claim boundary**

- Does **not** assert that the current corridor is unique, correct, or physically privileged.  
- Does **not** assert that any particular \(\theta\) value inside the corridor is physically realized.  
- Only asserts that a **schema-governed representation** exists and is used consistently.

---

## P0-C02 — Corridor Bookkeeping Discipline (History, Not Just Snapshots)

**Statement**

Phase 0 requires that corridor evolution be tracked as an append-only **history**, not just through overwritten snapshots. Any update that tightens or modifies the admissible \(\theta\)-corridor must be recorded in a machine-parseable log.

**Evidence**

- History and current state  
  - `phase0/phase_outputs/theta_corridor_history.jsonl` (append-only log)  
  - `phase0/phase_outputs/theta_corridor_current.json` (latest state)

- Phase 0 progress log  
  - `phase0/PROGRESS_LOG.md`  
    - Entry `2025-12 (initial Phase 0 integration)`  
    - Entry `2026-01-01` (Phase 0 completion & repo cleanup)

- Conceptual description  
  - `phase0/paper/main.tex`  
    - `Phase0-paper: 03_corridor_method`  
    - `Phase0-paper: 07_discussion_candidate_origins` (how corridor history constrains future phases)  

**Non-claim boundary**

- Does **not** guarantee that all early exploratory corridors exist in this history (legacy exploration may predate Phase 0 discipline).  
- Does **not** constrain the specific update rule; it only requires that updates be **recorded** and **schema-valid**.

---

## P0-C03 — Claims Taxonomy & Global Registry

**Statement**

Phase 0 defines a **claims taxonomy** (existence, robustness, scaling, bounded viability, etc.) and a global registry mechanism. Every future claim must:
1. Have a stable ID (e.g. `P1-C03`),
2. Declare its **phase owner**,
3. Provide evidence pointers,
4. Explicitly declare its **non-claim boundary** (what it does *not* assert).

**Evidence**

- Global registry  
  - `docs/CLAIMS_INDEX.md` (top-level index of claims across phases)  
  - `docs/PHASES.md` (phase roles, allowed claim types, canonical artifacts)

- Phase-local claim files  
  - `phase0/CLAIMS.md` (this file)  
  - `phase1/CLAIMS.md`  
  - `phase2/CLAIMS.md`

- Conceptual description  
  - `phase0/paper/main.tex`  
    - `Phase0-paper: 04_phase_contracts`  
    - `Phase0-paper: 06_falsifiability_and_failure_modes`  

**Non-claim boundary**

- Does **not** assert that existing phases exhaust all meaningful claims.  
- Does **not** assign any level of *truth* to claims; it only enforces **structure, traceability, and scope**.

---

## P0-C04 — Reproducibility Contract & Environment Discipline

**Statement**

Phase 0 defines a minimal reproducibility contract for the repository:  
- Phases must expose **canonical Snakemake workflows** or equivalent automated pipelines.  
- Ephemeral artifacts (per-run outputs, caches, LaTeX build files) are excluded from git, while **canonical figures and papers** are committed as artifacts.  
- The repository documents a recommended approach to environment creation and reuse.

**Evidence**

- Repository-level documentation  
  - `docs/REPRODUCIBILITY.md`  
  - `docs/PHASES.md` (canonical build commands for each phase)  

- Phase 1 / Phase 2 workflows  
  - `phase1/workflow/Snakefile`  
  - `phase2/workflow/Snakefile`

- Canonical artifacts  
  - `phase1/artifacts/origin-axiom-phase1.pdf`  
  - `phase1/outputs/figures/*.pdf`  
  - `phase2/outputs/figures/*.pdf`  

- Git tracking policy  
  - `.gitignore` (excludes `.snakemake/`, `**/outputs/runs/`, LaTeX build artefacts)  
  - `phase0/PROGRESS_LOG.md` (2026-01-01 entry documenting cleanup and policy)

- Phase 0 paper  
  - `phase0/paper/main.tex`  
    - `Phase0-paper: 05_reproducibility_contract`  

**Non-claim boundary**

- Does **not** mandate a specific package manager or exact pinned dependency set at this stage (these may be refined in later phases).  
- Does **not** guarantee that all historical exploratory runs are reproducible; it guarantees that **Phase-level canonical results** have a documented path to regeneration.

---

## P0-C05 — Archive & Deprecation Policy

**Statement**

Phase 0 enforces an explicit **archive and deprecation policy**:  
- Exploratory notebooks and heavy experimental data live in a **separate legacy archive** unless promoted into a phase as canonical artifacts.  
- Promotion follows a clear path:  
  *Exploration → Phase candidate → Bounded claims → Canonical figures → Reproducibility contract → Merge into main.*

This keeps the main repository lean, reviewable, and focused on defensible claims.

**Evidence**

- Policy document  
  - `docs/ARCHIVE.md`  

- Phase 0 progress log  
  - `phase0/PROGRESS_LOG.md`  
    - Entries noting removal of legacy artifacts from git and reliance on external archives.

- Git history  
  - Deletion of legacy `lab/`, `paper/`, `notes/`, and old scripts in favor of Phase 0/1/2 structure.

**Non-claim boundary**

- Does **not** assert that every exploratory artifact is perfectly catalogued in an external archive.  
- Does **not** forbid future re-imports of legacy content; it requires that any re-import be done via Phase governance (scope, claims, reproducibility).

---

## P0-C06 — Phase Contracts & Allowed Claim Types

**Statement**

Phase 0 specifies that each phase must:
1. Declare its **purpose** and **non-claims**,
2. Enumerate its **allowed claim types**,
3. Identify its **canonical artifacts** (papers, figures, key outputs),
4. Provide its own `CLAIMS.md` file that obeys the global registry rules.

Phase 1 and Phase 2 are the first concrete realizations of this contract.

**Evidence**

- Phase overview  
  - `docs/PHASES.md`  
    - Phase 0: governance & corridor  
    - Phase 1: lattice toy models, existence/scaling in toy domain  
    - Phase 2: mode-sum model, FRW comparison with bounded viability claims

- Phase-local governance  
  - `phase1/README.md`, `phase1/CLAIMS.md`, `phase1/SCOPE.md`, `phase1/ASSUMPTIONS.md`, `phase1/REPRODUCIBILITY.md`  
  - `phase2/README.md`, `phase2/CLAIMS.md`, `phase2/SCOPE.md`, `phase2/ASSUMPTIONS.md`, `phase2/REPRODUCIBILITY.md`, `phase2/APPROXIMATION_CONTRACT.md`, `phase2/PHASE2_WORKFLOW_GUIDE.md`

- Phase 0 paper  
  - `phase0/paper/main.tex`  
    - `Phase0-paper: 04_phase_contracts`  
    - `Phase0-paper: 08_conclusion`  

**Non-claim boundary**

- Does **not** assert that Phase 1 or 2 are “complete” with respect to all possible toy models or cosmological tests.  
- Does **not** rank phases by physical importance; it only enforces that each phase **declares its contract**.

---

## P0-C07 — Falsifiability & Failure Modes Are First-Class

**Statement**

Phase 0 requires that each phase describe **how it can fail**. For every family of claims, the corresponding phase must:
- Specify data, calculations, or counterexamples that would invalidate the claim, and
- Distinguish between “claim fails, method survives” and “method itself is invalidated”.

**Evidence**

- Conceptual template  
  - `phase0/paper/main.tex`  
    - `Phase0-paper: 06_falsifiability_and_failure_modes`  

- Phase-level implementations  
  - `phase1/CLAIMS.md` and `phase1/LIMITATIONS.md` / `phase1/ASSUMPTIONS.md`  
  - `phase2/CLAIMS.md` and `phase2/APPROXIMATION_CONTRACT.md`, `phase2/REPRODUCIBILITY.md`, `phase2/SCOPE.md`

**Non-claim boundary**

- Does **not** assert that all failure modes have been exhausted at this stage.  
- Does **not** assign probabilities to different failure modes; it only requires that they be **explicitly named** and tied to specific claims.

---

## Non-Claims of Phase 0 (Global)

For clarity, Phase 0 **explicitly does not claim**:

- Any specific numerical value of \(\theta_\star\) or its physical interpretation.  
- Any correctness of the toy models, lattice constructions, or mode-sum models used in later phases.  
- Any statement about the true cosmological constant, FRW dynamics, or observational cosmology.  
- Any claim that the current corridor \(\mathcal{C}\) is final; it is an explicitly revisable object, subject to the bookkeeping rules above.

Phase 0 is solely the **governance, encoding, and reproducibility layer**.  
All physics content lives in later phases and must **opt in** to these contracts.
