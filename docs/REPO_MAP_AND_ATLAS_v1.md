# Origin Axiom – repo map and atlas (v1, skeleton)

**Purpose.**  
This document is a high-level atlas of the `origin-axiom` repository. It records how the main phases, Stage 2 diagnostic belts, experiments, build scripts, and auxiliary areas are laid out on disk, so that external auditors can navigate the tree without guessing. It is descriptive only; no new claims are introduced here.

---

## 1. Top-level layout

The repository root contains:

| Path                 | Kind              | Role / scope                                                                                 |
|----------------------|-------------------|----------------------------------------------------------------------------------------------|
| `phase0/`            | Phase             | Phase 0 – governance and specification (contracts, claims ledger, schemas, phase0 paper).   |
| `phase1/`            | Phase             | Phase 1 – minimal non-cancellation toy ensembles and existence tests.                       |
| `phase2/`            | Phase             | Phase 2 – bounded vacuum-floor implementation and FRW-style viability toy diagnostics.      |
| `phase3/`            | Phase             | Phase 3 – mechanism module (non-cancelling vacuum toy, amplitude floor, diagnostics).       |
| `phase4/`            | Phase             | Phase 4 – FRW-inspired diagnostics built on Phase 3 amplitudes (toy FRW, corridors, masks). |
| `phase5/`            | Phase             | Phase 5 – interface and sanity layer (rung 0–1; meta dashboards over Phase 3/4 outputs).    |
| `stage2/`            | Stage 2 belts     | Downstream diagnostic belts over Phase 3/4 outputs (FRW, mech/measure, joint, data, θ★).    |
| `experiments/`       | Experiments       | Archived and non-canonical experiments (currently Phase 3 flavor sector).                   |
| `artifacts/`         | Artifacts         | Published phase PDFs: `origin-axiom-phase0.pdf`–`origin-axiom-phase5.pdf`.                   |
| `docs/`              | Global docs       | Project-level overview, phases, claims index, Stage 2 docs, gates and archive status.       |
| `scripts/`           | Build/gate tools  | Phase build scripts, gate scripts, and archived rung scripts.                               |
| `sandbox/`           | Sandbox           | Phase 5 sandbox notes and scratch explorations.                                             |
| `PROGRESS_LOG.md`    | Log               | Global chronological log of work across phases and Stage 2.                                 |
| `README.md`          | Front page        | High-level narrative, phase descriptions, and key links.                                    |
| `REPRODUCIBILITY.md` | Global reproduc.  | Global reproducibility guidance (complements per-phase reproducibility docs).               |
| `ROADMAP.md`         | Roadmap           | Legacy roadmap; superseded in part by `docs/FUTURE_WORK_AND_ROADMAP.md`.                    |

Each phase and belt has its own internal structure described in the following sections.

---

## 2. Phase directories (phase0–phase5)

### 2.1 Phase 0 – Governance and specification (`phase0/`)

Top-level contents:

- `SCOPE.md` – Phase 0 scope and non-claims.
- `CLAIMS.md` – Phase 0 claims ledger (governance-level claims).
- `ASSUMPTIONS.md` – Assumptions and pre-commitments.
- `REPRODUCIBILITY.md` – Reproducibility contract for Phase 0 artifacts.
- `PROGRESS_LOG.md` – Phase 0 specific log (governance rungs).
- `schemas/` – JSON/YAML schemas for claims, corridors, and artifacts.
- `scripts/` – helper scripts for Phase 0 governance tasks.
- `paper/` – LaTeX sources for the Phase 0 paper (`main.tex`).
- `artifacts/` and `phase_outputs/` – Phase 0 derived artifacts as needed.
- `outputs/` – auxiliary outputs (if any) backing Phase 0 claims.

The canonical Phase 0 paper artifact is `artifacts/origin-axiom-phase0.pdf` at the repo root; `phase0/paper/main.tex` is its LaTeX source.

### 2.2 Phase 1 – Toy ensembles (`phase1/`)

Top-level contents:

- `SCOPE.md`, `CLAIMS.md`, `ASSUMPTIONS.md`, `REPRODUCIBILITY.md`, `PROGRESS_LOG.md`, `README.md`.
- `config/` – configuration for Phase 1 runs.
- `src/` – Phase 1 code (toy phasor ensembles, lattice existence checks).
- `workflow/` – workflow configuration (e.g. Snakefile or equivalent).
- `paper/` – LaTeX sources for the Phase 1 paper (`main.tex`).
- `outputs/` – numerical outputs, tables, and figures (used by the paper).
- `artifacts/` – any Phase 1–specific artifacts beyond the global PDF.

The Phase 1 paper is compiled from `phase1/paper/main.tex`; the consolidated PDF lives at `artifacts/origin-axiom-phase1.pdf`.

### 2.3 Phase 2 – Bounded vacuum-floor implementation (`phase2/`)

Top-level contents:

- Governance and scope: `SCOPE.md`, `CLAIMS.md`, `CLAIMS_TABLE.md`, `ASSUMPTIONS.md`, `APPROXIMATION_CONTRACT.md`, `PHASE2_LOCK_CHECKLIST.md`, `PHASE2_WORKFLOW_GUIDE.md`, `REPRODUCIBILITY.md`, `PROGRESS_LOG.md`, `README.md`.
- Code and workflow:
  - `config/` – configuration for Phase 2 runs.
  - `src/` – Phase 2 source code (vacuum-floor implementation, FRW-like diagnostics).
  - `workflow/` – workflow configuration.
- Paper and artifacts:
  - `paper/` – LaTeX sources (`main.tex` plus figures).
  - `_paper_backups/` – backups of earlier paper drafts.
  - `artifacts/` – Phase 2–specific artifact bundles.
- Outputs:
  - `outputs/` – numerical outputs, tables, and figures used by the Phase 2 paper.

The canonical Phase 2 paper is `artifacts/origin-axiom-phase2.pdf`; it is built from `phase2/paper/main.tex` and fed by tables under `phase2/outputs/`.

### 2.4 Phase 3 – Mechanism module (`phase3/`)

Top-level contents:

- Governance and scope: `MECHANISM_CONTRACT.md`, `PHASE3_NEXT_RUNG.md`, `PHASE3_RUNG2_MECHANISM_A_INSTABILITY_PENALTY.md`, `ROLE_IN_PROGRAM.md`, `PROGRESS_LOG.md`.
- Code and workflow:
  - `src/` – mechanism implementation (non-cancelling vacuum toy model and diagnostics).
  - `workflow/` – workflow configuration for Phase 3 runs.
- Paper and artifacts:
  - `paper/` – LaTeX sources for the Phase 3 mechanism paper (`main.tex`).
  - `artifacts/` – Phase 3–specific artifacts as needed.
- Outputs:
  - `outputs/tables/` – key Phase 3 tables, including:
    - `mech_baseline_scan.csv`
    - `mech_baseline_scan_diagnostics.json`
    - `mech_binding_certificate.csv`
    - `mech_binding_certificate_diagnostics.json`
    - `phase3_instability_penalty_v1.json`
    - `phase3_measure_v1_hist.csv`
    - `phase3_measure_v1_stats.json`
  - `outputs/figures/` – figures used by the Phase 3 paper (if present).

The canonical Phase 3 paper is `artifacts/origin-axiom-phase3.pdf`, built from `phase3/paper/main.tex` using the outputs above. Flavor-sector work is **not** part of canonical Phase 3 and lives in `experiments/phase3_flavor_v1/`.

### 2.5 Phase 4 – FRW toy diagnostics (`phase4/`)

Top-level contents:

- Governance and scope: `OVERVIEW.md`, `SCOPE.md`, `NON_CLAIMS.md`, `CLAIMS.md`, `CLAIMS_TABLE.md`, `FRW_TOY_DESIGN.md`, `FRW_DATA_DESIGN.md`, `FRW_SYNTHESIS.md`, `HARD_NOVELTY_ROADMAP.md`, `MAPPING_FAMILIES.md`, `PHASE3_INTERFACE.md`, `PLANNING.md`, `REPRODUCIBILITY.md`, `PROGRESS_LOG.md`.
- Data and code:
  - `data/` – any Phase 4–specific data inputs.
  - `src/` – FRW toy pipeline code (sanity curve, masks, diagnostics).
  - `workflow/` – workflow configuration.
- Outputs:
  - `outputs/tables/` – FRW tables, including:
    - `phase4_F1_frw_sanity_curve.csv`
    - `phase4_F1_frw_shape_mask.csv`
    - `phase4_F1_frw_toy_mask.csv`
    - `phase4_F1_frw_viability_mask.csv`
    - `phase4_F1_frw_lcdm_probe_mask.csv`
    - `phase4_F1_frw_data_probe_mask.csv`
    - and associated JSON diagnostics.
  - `outputs/figures/` – FRW figures (if present).
- Paper and artifacts:
  - `paper/` – LaTeX sources for the Phase 4 paper (`main.tex`).
  - `artifacts/` – any Phase 4–specific artifact bundles.

The consolidated Phase 4 PDF is `artifacts/origin-axiom-phase4.pdf`.

### 2.6 Phase 5 – Interface and sanity layer (`phase5/`)

Top-level contents:

- Governance and scope: `SCOPE.md`, `ROLE_IN_PROGRAM.md`, `NON_CLAIMS.md`, `PHASE5_VISION_RUNG0.md`, `PROGRESS_LOG.md`.
- Interface and configuration:
  - `config/` – configuration files for Phase 5 dashboards and interfaces.
  - `src/` – Phase 5 code (currently at rung 0–1, providing summaries over Phase 3/4 outputs).
- Outputs:
  - `outputs/` – Phase 5 interface outputs and summary tables (to be expanded).
- Paper and artifacts:
  - `paper/` – LaTeX sources for the Phase 5 paper (`main.tex`).
  - `artifacts/` – Phase 5–specific artifacts.

The consolidated Phase 5 PDF is `artifacts/origin-axiom-phase5.pdf`. At the current rung, Phase 5 is mainly a contract and skeleton for interface work rather than a full physics phase.

---

## 3. Stage 2 diagnostic belts (`stage2/`)

Stage 2 is a set of downstream diagnostic belts built on top of locked Phase 3 and Phase 4 outputs. Stage 2 never mutates Phase 3/4 artifacts in place and does not introduce new canonical claims on its own.

Top-level contents of `stage2/`:

- `STAGE2_OVERVIEW_v1.md` – overview of Stage 2 as a diagnostic belt layer and its sub-belts.
- `docs/` – Stage 2–level docs:
  - `STAGE2_OVERVIEW_v1.md` – Stage 2 overview and verdict.
  - `STAGE2_BELT_OVERVIEW_v1.md` – description of FRW, mech/measure, joint mech–FRW, FRW data-probe, and θ★ rungs.
  - `STAGE2_DOC_AUDIT_SUMMARY_v1.md` – doc-audit CSVs and how to use them as diagnostics.
  - `STAGE2_ARCHIVE_STATUS_v1.md` – map of canonical vs archived/experimental areas.
  - `STAGE2_OVERVIEW_AND_PROMOTION_MAP_v1.md` – promotion map for Stage 2 artifacts.
  - `STAGE2_PROMOTION_DESIGN_v1.md` – Option A/B promotion design (planning only).
- `frw_corridor_analysis/` – FRW corridor belt (rungs 1–9):
  - `src/` – analysis scripts.
  - `outputs/tables/` – Stage 2 FRW family, robustness, and θ★ alignment tables.
  - `README_FRW_CORRIDORS_v1.md` – belt-level description.
- `mech_measure_analysis/` – mech/measure belt (rungs 1–6):
  - `src/` – inventory, stats, probability-like, θ-profile, and preferred-candidate scripts.
  - `outputs/tables/` – Stage 2 mech tables.
- `joint_mech_frw_analysis/` – joint mech–FRW belt:
  - `src/` – joint grid, family summaries, and correlation scripts.
  - `outputs/tables/` – joint θ grid and correlation tables.
- `frw_data_probe_analysis/` – FRW data-probe belt:
  - `src/` – analysis scripts for FRW data probes vs viability.
  - `outputs/tables/` – data-probe stats and cross tables.
  - `docs/STAGE2_FRW_DATA_PROBE_AUDIT_v1.md` – detailed audit doc.
- `theta_star_analysis/` – θ★–FRW alignment diagnostic:
  - `docs/` and `outputs/tables/` for θ★ alignment summaries.

Stage 2 artifacts are treated as diagnostics that can later be cited or plotted under explicit promotion gates; they do not modify Phase 0–5 claims by themselves.

---

## 4. Experiments and sandbox

### 4.1 Experiments (`experiments/`)

The `experiments/` tree is reserved for non-canonical or archived work.

Current contents:

- `experiments/phase3_flavor_v1/` – archived Phase 3 flavor-sector experiment:
  - Governance: `SCOPE.md`, `ASSUMPTIONS.md`, `CLAIMS.md`, `CLAIMS_TABLE.md`, `NON_CLAIMS.md`, `APPROXIMATION_CONTRACT.md`, `REPRODUCIBILITY.md`, `PROGRESS_LOG.md`.
  - `ARCHIVE_STATUS_v1.md` – explicit archive banner marking this work as non-canonical.
  - `src/`, `workflow/` – code and workflows for the flavor-sector phase.
  - `fit/`, `fit/data_frozen/` – flavor fits and frozen data.
  - `artifacts/origin-axiom-phase3.pdf` – legacy flavor-phase paper.

The canonical Phase 3 mechanism module lives under `phase3/`; no flavor-sector results are part of the main claims.

### 4.2 Sandbox (`sandbox/`)

The `sandbox/` directory contains scratch notes and numerology explorations, primarily for Phase 5:

- `PHASE5_SANDBOX_GENERATION_NUMEROLOGY.md`
- `PHASE5_SANDBOX_H0_MPL_SCALING_IDEAS.md`
- `PHASE5_SANDBOX_PHI_PHI_LAMBDA_NUMEROLOGY.md`

These files are explicitly non-canonical and serve as idea scratchpads.

---

## 5. Build scripts and gates (`scripts/`)

The `scripts/` directory contains global build and gate tooling:

- `build_all_papers.sh`, `build_paper.sh`, `build_papers.sh` – helpers to build one or all phase papers.
- `build_phase5_paper.sh` – dedicated helper for Phase 5 paper builds.
- `check_papers_clean.sh` – checks for clean paper builds across phases.
- Phase gates:
  - `phase0_gate.sh`
  - `phase1_gate.sh`
  - `phase2_claims_hardening.sh`
  - `phase2_gate.sh`
  - `phase2_make_release_bundle.sh`
- Archived rung scripts under `scripts/archive/`:
  - `scripts/archive/phase3_rungs/phase3_rung*.py` – automation used in earlier Phase 3 text passes, kept for provenance.

These scripts are used to enforce reproducibility and gate conditions before locking phases or making release bundles. They do not define new physics content; they orchestrate builds and checks.

---

## 6. How to use this atlas

- To understand the **scientific story**, start with:
  - `README.md`
  - `docs/PROJECT_OVERVIEW.md`
  - the Phase PDFs in `artifacts/`
  - `docs/STATE_OF_REPO.md` and `docs/PHASES.md`.
- To find where a **particular claim** is implemented:
  - locate the phase in `docs/PHASES.md` and `docs/CLAIMS_INDEX.md`,
  - follow pointers into `phaseX/paper/`, `phaseX/src/`, and `phaseX/outputs/`.
- To inspect **Stage 2 diagnostics**:
  - read `stage2/docs/STAGE2_OVERVIEW_v1.md` and `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`,
  - then inspect the relevant belt directory under `stage2/`.
- To explore **non-canonical work**:
  - start at `docs/ARCHIVE.md` and `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`,
  - then look under `experiments/` and `sandbox/`.

Future rungs can extend this atlas with machine-readable indices (for example, CSV maps of docs, code, and artifacts) and more fine-grained links between claims, tables, and scripts, but the present version already captures the main structural layout of the repository.

---

## 7. Legacy migrations map

The file `docs/LEGACY_MIGRAIONS_PHASE0_MAP.MD` is a Phase 0–compatible governance
map between this phased repository and the older `origin-axiom-legacy` tree. It:

- lists legacy scripts and outputs,
- proposes Phase ownership for candidate runs, and
- documents how legacy artifacts would need to be migrated to satisfy current
  Phase 0 contracts.

It is part of the archive/provenance layer rather than a new Phase. When in
doubt about a legacy file or run mentioned in `PROGRESS_LOG.md` or older notes,
consult this map and the archive policy in `docs/ARCHIVE.md`.

---

## 8. Stage 2 overview and plans

Beyond the per-belt docs under `stage2/docs/`, two global Stage 2 design docs
live under `docs/`:

- `docs/STAGE2_OVERVIEW.md` describes Stage 2 as an exploratory downstream lab
  layer sitting on top of Phase 3 and Phase 4 outputs, including its role,
  non-claims, and the high-level questions the belts are allowed to ask.

- `docs/STAGE2_JOINT_MECH_FRW_PLAN_v1.md` defines the original design spine for
  the joint mech–FRW analysis, clarifying how Phase 3 measure candidates and
  Phase 4 / Stage 2 FRW masks are combined on a joint θ grid, and which outputs
  are intended to be diagnostic rather than new physics claims.

These documents form the conceptual top layer for Stage 2, with the belt-level
docs in `stage2/docs/` and the tables/figures under `stage2/*/outputs/` providing
their concrete implementations.

## Obstruction-program and external-constraints docs

These memos describe the obstruction-program interpretation of the Stage I stack and how empirical tests will interface with it:

- `docs/OBSTRUCTION_PROGRAM_OVERVIEW_v1.md` – high-level overview of the obstruction picture, its status, and how it sits on top of the locked phases.
- `docs/THETA_ARCHITECTURE.md` – structural view of the θ-grid and θ*, including an obstruction-program reading of static θ corridors (interpretive, non-binding).
- `docs/OBSTRUCTION_EMPIRICAL_PROGRAM_v1.md` – scope and standards for empirical tests in the obstruction program, with emphasis on static θ corridors and Phase 0 governance.
- `stage2/docs/STAGE2_OBSTRUCTION_TESTING_SPINE_v1.md` – how the existing Stage 2 belts (FRW corridors, mech/measure, joint mech–FRW, FRW data probes, θ* diagnostic) function as an obstruction-testing spine.
- `stage2/docs/STAGE2_EXTERNAL_CONSTRAINTS_DESIGN_v1.md` – design-only memo for future external-style corridors (late-time expansion, early-structure-friendly, and host-consistency filters).
- `stage2/docs/STAGE2_MASTER_VERDICT_v1.md` – Stage 2 synthesis and verdict, including an interpretive paragraph on how the obstruction program reads the current diagnostic outcomes.
- `docs/STAGEII_COSMO_HOSTS_DESIGN_v1.md` – design notes for Stage II cosmology hosts, including an obstruction-aware list of questions about corridor survival and kernel structure.

All obstruction-program docs are interpretive overlays: they do not modify any Phase 0–5 contracts or Stage 2 promotion gates, and any future promotion of obstruction-flavoured statements into phase papers will require separate, tightly scoped rungs.

---

## Obstruction program status (v1)

For a concise summary of what the obstruction program currently adds on top of the Phase 0–5 stack and Stage 2 belts, see:

- `docs/OBSTRUCTION_PROGRAM_STATUS_v1.md` – status snapshot for obstruction-program-v1, including
  - inputs and diagnostic spine,
  - static FRW pre-data kernel definition and helper table,
  - kernel family decomposition and robustness note,
  - verdict and forward roadmap.

---

### Obstruction-program status docs

- `docs/OBSTRUCTION_PROGRAM_STATUS_v1.md` – concise snapshot of the obstruction-program-v1 overlays, current diagnostic outcomes, and the roadmap for external-style corridors and Stage II hosts.

- `docs/OBSTRUCTION_PROGRAM_STATUS_v1.md` — status snapshot of the obstruction program as of 2026-01-21, summarising the static FRW kernel, internal and external-style corridors, the 40 point sweet subset, and the current obstruction verdict and roadmap.
